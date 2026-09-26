# Acceptance and review

Use a compact record for substantial work. Omit irrelevant rows. Mark each criterion pass, fail, blocked, not run, or not applicable, with evidence. Do not turn subjective scores into proof of quality.

| Dimension | Acceptance question | Useful evidence |
| --- | --- | --- |
| Task completion | Can the intended user finish the main job? | Real entry-to-outcome journey |
| Correctness | Does the durable result match the agreed rule? | Observable persistence and data checks |
| Hierarchy | Is the important information/action visibly prioritized? | Rendered view with realistic content |
| Coherence | Are typography, spacing, states, and controls consistent? | Representative screens/components |
| Responsive behavior | Does content remain useful at stressed widths and zoom? | Inspected mobile/desktop and stress cases |
| Accessibility | Can relevant keyboard/assistive flows operate? | Manual checks plus scan findings where available |
| Recovery | Can users understand and recover from material failures? | Invalid, retry, duplicate, interrupted scenarios |
| Security | Are permissions enforced at the real boundary? | Allowed and denied actor/resource cases |
| Performance | Is the observed bottleneck improved without stale/unsafe behavior? | Comparable measurements and environment |
| Maintainability | Does the change fit the project and avoid unnecessary complexity? | Actual diff and caller inspection |
| Provenance | Can important claims and results be checked? | Sources, calculations, repeatable run artifacts |

Severity:
- Blocker: data loss, unauthorized access, broken main journey, or unmet explicit acceptance criterion. Fix before declaring complete; if blocked, state it.
- Material: substantial confusion, inaccessible interaction, wrong responsive behavior, unreliable recovery. Fix within authorized scope.
- Polish: minor alignment, phrasing, or aesthetic preference. Address when justified; do not use it to expand scope indefinitely.

For an audit, report finding → evidence → user impact → likely cause (label inference) → proposed remedy → verification method. Do not implement an audit-only request.

Example brief: “A committee member checks in a participant on a phone over slow data. Success means the correct record is identified, duplicate taps do not duplicate the update, confirmation reflects saved state, and the result persists after reload.” This implies task, state, permission, recovery, and responsive checks; it does not imply a decorative dashboard redesign.

Example review note: “At narrow width the sticky footer covers the form error and keyboard focus. Adjust content clearance and retest focus traversal.” Avoid vague verdicts such as “not premium enough.”
