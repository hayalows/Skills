const nonempty = (value) => typeof value === "string" && value.trim().length > 0;
const phases = ["reconnaissance", "hunting", "candidate-validation", "structured-output", "independent-verification", "audit-report"];
const effects = ["inspect", "read-external", "write-target", "write-artifact", "run-target", "preview", "publish"];
const reviewSkills = {
  "product-design-os": ["product-discovery", "product-design", "product-ux-verification"],
  "product-evidence": ["measurement-design", "measurement-integrity", "comparison-and-limits"],
  "model-assurance": ["model-inputs", "model-baseline", "model-independent-recalculation", "model-limits"],
  "vercel-deployment-steward": ["vercel-target-and-fanout", "vercel-account-and-route"],
};

export function executionPlan(route, intent, input = {}) {
  const selected = new Set(route.skills);
  const security = selected.has("security-audit/SKILL.md");
  const auditMode = security ? (input.auditMode ?? "unresolved") : null;
  if (security && !["focused", "full", "unresolved"].includes(auditMode)) throw new Error("Invalid security audit mode");
  const blockers = [...route.blockers];
  const stages = [];
  const methodOnly = new Set(input.methodOnly ?? []);
  for (const file of methodOnly) {
    if (!selected.has(file) || !["model-assurance/SKILL.md", "product-evidence/SKILL.md"].includes(file)) {
      throw new Error("Method-only stage is unsupported for: " + file);
    }
  }
  function add(id, owner = null, effect = "inspect", requires) {
    if (!/^[a-z][a-z0-9-]*$/.test(id) || stages.some((stage) => stage.id === id)) throw new Error("Invalid or duplicate stage: " + id);
    if (owner && !selected.has(owner)) throw new Error("Stage owner is not selected: " + owner);
    if (!effects.includes(effect)) throw new Error("Unknown stage effect: " + effect);
    const dependsOn = requires ?? stages.slice(-1).map((stage) => stage.id);
    if (!Array.isArray(dependsOn) || dependsOn.some((dependency) => !stages.some((stage) => stage.id === dependency))) {
      throw new Error("Stage dependencies must point to earlier stages: " + id);
    }
    stages.push({ id, owner, effect, dependsOn });
  }
  add("baseline");
  if (auditMode === "unresolved") blockers.push("audit-mode-unresolved");
  if (auditMode === "full" && !input.allowedEffects?.includes("write-artifact")) blockers.push("audit-artifacts-not-authorized");
  if (security) {
    const owner = "security-audit/SKILL.md";
    const auditChecks = new Map(Object.entries(input.auditChecks ?? {}));
    function addAuditStage(id, effect) {
      add(id, owner, effect);
      for (const check of auditChecks.get(id) ?? []) {
        if (!["inspect", "run-target", "write-artifact"].includes(check.effect) ||
            (check.effect === "write-artifact" && auditMode !== "full")) {
          throw new Error("Unsupported audit check effect: " + check.effect);
        }
        add(check.id, owner, check.effect);
      }
      auditChecks.delete(id);
    }
    if (auditMode === "full") addAuditStage("security-audit-setup", "write-artifact");
    add("security-coverage", owner);
    if (auditMode === "focused") {
      addAuditStage("security-source-review");
      addAuditStage("security-verification-disposition");
    }
    if (auditMode === "full") {
      for (const id of phases) {
        addAuditStage("security-" + id, ["reconnaissance", "structured-output", "audit-report"].includes(id) ? "write-artifact" : "inspect");
      }
    }
    if (auditChecks.size) throw new Error("Unknown audit checkpoint: " + [...auditChecks.keys()].join(", "));
  }
  if (route.stages.includes("reproduce")) add("reproduce");
  if (route.stages.includes("define-evidence")) add("define-evidence");
  for (const [skill, checks] of Object.entries(reviewSkills)) {
    const owner = skill + "/SKILL.md";
    if (!selected.has(owner)) continue;
    add(checks[0], owner);
    if (!methodOnly.has(owner)) add(checks[1], owner);
  }
  function addCustom(stage) {
    if (["write-target", "preview", "publish"].includes(stage.effect) || (security && stage.effect === "run-target")) {
      throw new Error("Custom stages cannot bypass mutation gates: " + stage.id);
    }
    add(stage.id, stage.owner, stage.effect, stage.dependsOn);
  }
  for (const stage of input.beforeWork ?? []) addCustom(stage);
  if (route.stages.includes("inspect")) add("inspect");
  if (route.stages.includes("implement")) {
    add("implement", null, input.allowedEffects?.includes("write-artifact") && !input.allowedEffects?.includes("write-target") ? "write-artifact" : "write-target");
  }
  for (const [skill, checks] of Object.entries(reviewSkills)) {
    const owner = skill + "/SKILL.md";
    if (!selected.has(owner)) continue;
    if (methodOnly.has(owner)) add(skill + "-method-review", owner);
    else for (const id of checks.slice(2)) add(id, owner);
  }
  for (const stage of input.beforeVerify ?? []) addCustom(stage);
  add("verify", null, "inspect", stages.slice(1).length ? stages.slice(1).map(({ id }) => id) : ["baseline"]);
  if (route.stages.includes("host-preflight")) add("host-preflight");
  if (route.stages.includes("hosted-build")) add("hosted-build", null, "preview");
  if (route.stages.includes("publish")) add("publish", null, "publish");
  if (route.stages.includes("verify-production")) add("verify-production");
  add("report", null, "inspect", []); // Partial reporting remains possible.
  return { auditMode, stages, blockers };
}

export function checkExecution(route, intent, snapshot, input) {
  const graph = executionPlan(route, intent, input);
  const issues = [...graph.blockers];
  const require = (condition, issue) => { if (!condition) issues.push(issue); };
  require(nonempty(input.objective) && nonempty(input.scope) && nonempty(input.target), "objective-target-scope-required");
  require(nonempty(input.targetRevision), "target-revision-required");
  require(Array.isArray(input.allowedEffects) && input.allowedEffects.includes("inspect") &&
    input.allowedEffects.every((effect) => effects.includes(effect)), "invalid-authorized-effects");
  const allowed = new Set(input.allowedEffects ?? []);
  if (["inspect", "answer"].includes(intent.mode)) require(!allowed.has("write-target"), "read-only-target-write-forbidden");
  require(!allowed.has("publish") || (intent.releaseAuthorized && !["inspect", "answer"].includes(intent.mode)), "publish-forbidden");
  require(!allowed.has("preview") || (intent.hostedBuild && !["inspect", "answer"].includes(intent.mode)), "preview-forbidden");
  if (graph.auditMode) {
    require(!["publish", "preview", "write-target"].some((effect) => allowed.has(effect)), "security-audit-scope-conflict");
    require(!allowed.has("run-target") || nonempty(input.sandboxEvidence), "security-sandbox-unverified");
  }
  const contracts = new Map(Object.entries(input.contracts ?? {}));
  const toolPlan = input.toolPlan ?? {};
  const stageOwners = new Set(graph.stages.map(({ owner }) => owner));
  require(route.skills.length ? contracts.has(input.primary) : input.primary == null, "primary-specialist-required");
  require(contracts.size === route.skills.length, "selected-contract-count-mismatch");
  for (const file of route.skills) {
    const skill = snapshot.skills.find((item) => item.path === file);
    const contract = contracts.get(file);
    require(nonempty(contract?.why) && nonempty(contract?.procedure) && nonempty(contract?.restrictions) &&
      Array.isArray(contract?.references) && contract.references.every(nonempty) && nonempty(contract?.loadEvidence) &&
      contract?.revision === route.revision && (!skill?.sha || contract?.blob === skill.sha), "skill-contract-invalid:" + file);
    require(stageOwners.has(file) || (Array.isArray(contract?.stages) && contract.stages.length > 0 &&
      contract.stages.every((id) => id !== "report" && graph.stages.some((stage) => stage.id === id))), "skill-stage-missing:" + file);
  }
  for (const { id, effect } of graph.stages) {
    require(allowed.has(effect), "stage-effect-not-authorized:" + id);
    const entry = toolPlan[id];
    require(["ready", "blocked", "pending"].includes(entry?.status) && nonempty(entry?.capability) &&
      nonempty(entry?.basis), "tool-plan-missing:" + id);
  }
  const toolBlockers = graph.stages.filter(({ id }) => toolPlan[id]?.status === "blocked").map(({ id }) => id);
  if (input.results == null) return { ...graph, state: issues.length || toolBlockers.length ? "needs-attention" : "planned", issues, toolBlockers };
  const results = new Map(Object.entries(input.results));
  const tools = new Map(Object.entries(input.tools ?? {}));
  for (const id of results.keys()) require(graph.stages.some((stage) => stage.id === id), "unknown-stage-result:" + id);
  for (const stage of graph.stages) {
    const result = results.get(stage.id);
    if (!result || result.status !== "passed") {
      require(result && ["failed", "blocked", "skipped", "pending"].includes(result.status) && nonempty(result.reason),
        "missing-stage-disposition:" + stage.id);
      issues.push("stage-incomplete:" + stage.id);
      continue;
    }
    require(toolPlan[stage.id]?.status === "ready", "stage-tool-not-ready:" + stage.id);
    require(allowed.has(stage.effect) && Array.isArray(result.effects) && result.effects.length === 1 && result.effects[0] === stage.effect, "unauthorized-stage-effect:" + stage.id);
    require(nonempty(result.evidence) && nonempty(result.proves) && Array.isArray(result.tools) && result.tools.length > 0 &&
      result.tools.every((tool) => nonempty(tools.get(tool))), "stage-evidence-invalid:" + stage.id);
    require(stage.dependsOn.every((id) => results.get(id)?.status === "passed"), "stage-dependency-incomplete:" + stage.id);
  }
  if (graph.auditMode && results.get("security-coverage")?.status === "passed") {
    const coverage = input.coverage;
    require(Array.isArray(coverage) && coverage.length > 0 && coverage.every((unit) =>
      nonempty(unit.boundary) && nonempty(unit.scope) && nonempty(unit.evidence) &&
      ["checked", "blocked", "excluded"].includes(unit.status)), "security-coverage-invalid");
    if (Array.isArray(coverage)) {
      require(coverage.some((unit) => unit.status === "checked"), "security-coverage-empty");
      require(!coverage.some((unit) => unit.status === "blocked"), "security-coverage-blocked");
    }
  }
  if (graph.auditMode === "full" && results.get("security-structured-output")?.status === "passed") {
    require(nonempty(input.auditValidators?.findings) && nonempty(input.auditValidators?.coverage), "security-validators-unverified");
  }
  if (graph.auditMode === "full" && results.get("security-audit-report")?.status === "passed") {
    const artifacts = ["run-metadata.json", "architecture.md", "coverage-ledger.json", "findings.json",
      "REPORT.md", "FINDINGS-DETAIL.md", "NEEDS-VALIDATION.md"];
    require(artifacts.every((file) => nonempty(input.auditArtifacts?.[file])), "security-artifacts-unverified");
  }
  if (graph.auditMode === "full" && results.get("security-independent-verification")?.status === "passed") {
    const review = input.auditIndependence;
    require(nonempty(review?.evidence) && (review?.candidates === 0 ||
      (Number.isInteger(review?.candidates) && review.candidates > 0 && Array.isArray(review.reviewerTools) &&
        review.reviewerTools.length > 0 && review.reviewerTools.every((tool) => nonempty(tools.get(tool))))),
    "security-independence-unverified");
  }
  const checker = input.checker;
  require(checker?.status === "ran" && nonempty(checker.evidence), "checker-execution-unverified");
  if (checker?.status === "fallback") require(nonempty(checker.reason) && nonempty(checker.evidence), "fallback-record-incomplete");
  return { ...graph, state: issues.length ? "incomplete" : "complete", issues, toolBlockers };
}
