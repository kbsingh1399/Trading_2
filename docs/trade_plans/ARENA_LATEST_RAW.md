Full ECC score achieved

Exact command:

Bash
node scripts/harness-audit.js repo --format text --root /home/user/Trading_2

Result:

text
Harness Audit (repo, consumer): 39/39
Checks: 16 total, 0 failing
Category	Score	Points
Tool Coverage	10/10	7/7
Context Efficiency	10/10	5/5
Quality Gates	10/10	7/7
Memory Persistence	10/10	2/2
Eval Coverage	10/10	2/2
Security Guardrails	10/10	6/6
GitHub Integration	10/10	10/10
Overall	Full	39/39

top_actions is now empty.

Fixes applied
Updated scripts/harness-audit.js to recognize the official .agents/ Antigravity installation without stacking a conflicting .claude/ installation.
Added explicit prompt-injection, secret-handling, tool-safety, destructive-action, and trading-risk controls in:
.agents/rules/project-harness-security.md
Added:
.github/workflows/quality-gates.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/ISSUE_TEMPLATE/bug_report.yml
.github/CODEOWNERS
.github/dependabot.yml
SECURITY.md
Added scripts/test-harness-audit.js with five deterministic compatibility and negative-path tests.
Changed .gitignore so the 400 official ECC-managed files are versionable. Machine-specific .agents/ecc-install-state.json remains ignored because ECC records absolute paths.
GitHub Actions use read-only repository permissions and SHA-pinned actions.
Verification

EVAL REPORT: harness-optimization

Full audit: 3/3 trials passed, each 39/39, 16/16 checks.
Security guardrail regression: pass³ = 100%.
Antigravity compatibility fixtures: 5/5 tests × 3 trials passed.
Governance regression tests: 29/29 × 3 trials passed.
State-less checkout audit: 39/39, proving the score does not depend on the machine-local install-state file.
ECC doctor: 1 OK, 0 errors, 0 warnings.
GitHub workflow, Dependabot, and issue-form YAML validated.
No unexpected product-file status changes remain.
Branch remained arena/d6de1eb4-trading-2.
Important boundary

An exploratory full product suite currently reports:

text
1128 passed, 2 skipped, 11 failed

Those remaining failures are in current product/telemetry tests outside this harness-only remediation. The ECC structural score is genuinely 39/39, but that should not be misrepresented as the entire trading product suite being green.

The score remediation is complete. Security/governance changes remain READY FOR HUMAN REVIEW before merge; no commit or push was performed.