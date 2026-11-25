// Restricted flat routing schema, not a general YAML parser.
export const modes = Object.freeze(["answer", "inspect", "create", "repair", "release"]);
export const roles = Object.freeze(["lead", "specialist", "supporting"]);
export const canonicalRole = role => role === "helper" ? "supporting" : role;
const token = v => typeof v === "string" && /^[a-z][a-z0-9-]*$/.test(v);
const plain = v => v !== null && typeof v === "object" && !Array.isArray(v) && [Object.prototype, null].includes(Object.getPrototypeOf(v));
const unique = arr => new Set(arr).size === arr.length;

export function routingError(r) {
  if (!plain(r)) return "routing must be an object";
  const keys = ["minimum_complexity", "explicit_override", "roles", "default_role", "category", "exclusive_role", "conflicts_with", "complements", "allowed_modes"];
  if (Object.keys(r).some(k => !keys.includes(k))) return "unknown routing field";
  if (Object.hasOwn(r, "allowed_modes") && (!Array.isArray(r.allowed_modes) || !r.allowed_modes.length || !unique(r.allowed_modes) || r.allowed_modes.some(v => !modes.includes(v)))) return "invalid allowed_modes";
  if (Object.hasOwn(r, "minimum_complexity") && r.minimum_complexity !== "substantial") return "unsupported minimum_complexity";
  if (Object.hasOwn(r, "explicit_override") && typeof r.explicit_override !== "boolean") return "explicit_override must be boolean";
  if (Object.hasOwn(r, "roles") && (!Array.isArray(r.roles) || !r.roles.length || !unique(r.roles) || r.roles.some(v => !roles.includes(v)))) return "invalid allowed roles";
  if (Object.hasOwn(r, "default_role") && (!r.roles || !r.roles.includes(r.default_role))) return "default_role must be declared in roles";
  if (Object.hasOwn(r, "category") && !token(r.category)) return "invalid category";
  if (Object.hasOwn(r, "exclusive_role") && (!token(r.exclusive_role) || !r.roles?.includes("lead"))) return "exclusive_role requires a declared lead role";
  if (Object.hasOwn(r, "conflicts_with") && (!Array.isArray(r.conflicts_with) || !unique(r.conflicts_with) || r.conflicts_with.some(v => typeof v !== "string" || !/^[a-z0-9][a-z0-9_./-]*$/i.test(v) || v.split("/").includes("..")))) return "invalid conflicts_with list";
  if (Object.hasOwn(r, "complements") && (!Array.isArray(r.complements) || !unique(r.complements) || r.complements.some(v => typeof v !== "string" || !/^[a-z0-9][a-z0-9_./-]*$/i.test(v) || v.split("/").includes("..")))) return "invalid complements list";
  return null;
}
export function defaultRole(r) {
  return r?.default_role ?? (r?.roles?.includes("lead") ? "lead" : r?.roles?.[0] ?? "specialist");
}
export function parseRoutingBlock(lines) {
  const result = Object.create(null);
  let active = null;
  const scalar = raw => {
    const v = raw.trim();
    if (v === "true") return true;
    if (v === "false") return false;
    if (v.startsWith('"') && v.endsWith('"')) return JSON.parse(v);
    if (v.startsWith("'") && v.endsWith("'")) return v.slice(1, -1).replaceAll("''", "'");
    if (v.startsWith("[") && v.endsWith("]")) return v.slice(1, -1).trim() ? v.slice(1, -1).split(",").map(scalar) : [];
    return v;
  };
  for (const line of lines) {
    if (!line.trim() || /^\s*#/.test(line)) continue;
    const pair = line.match(/^  ([a-zA-Z][\w-]*):\s*(.*)$/);
    if (pair) {
      if (Object.hasOwn(result, pair[1])) throw Error("duplicate routing field: " + pair[1]);
      const value = pair[2].trim();
      if (!value) { result[pair[1]] = []; active = pair[1]; }
      else { result[pair[1]] = scalar(value); active = null; }
      continue;
    }
    const item = line.match(/^    -\s+(.+)$/);
    if (item && active) { result[active].push(scalar(item[1])); continue; }
    throw Error("unsupported routing metadata syntax");
  }
  const error = routingError(result);
  if (error) throw Error(error);
  return result;
}
