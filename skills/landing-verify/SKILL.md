---
name: landing-verify
description: Verify an implementation or repository change against explicit acceptance criteria using risk-based tests, builds, static checks, runtime evidence, and final diff review. Use before claiming a coding task complete, when assessing regressions, or when producing an evidence-based delivery report. Do not treat unexecuted tests, a clean build, or static inspection alone as proof of behavior.
---

# Landing Verify

Decide what the evidence supports, including a qualified failure or partial result. Read `../../references/evidence-and-safety.md` before verification.

## Inputs

Collect acceptance criteria, changed paths, intended behavior, known risks, repository instructions, and checks already run. If acceptance criteria are missing, derive a draft from the request and label it as derived.

## Workflow

1. Inspect Git status and the final diff before testing. Separate pre-existing modifications from changes under review and flag unintended files.
2. Convert each acceptance criterion and material risk into a test matrix row with method, environment, expected result, actual result, and evidence.
3. Select proportionate checks: focused unit tests, contract/API tests, integration or end-to-end tests, build, type/lint/static checks, visual/runtime inspection, data consistency, permissions, and failure paths.
4. Reuse installed Superpowers verification or review practices when applicable. If unavailable, continue with this workflow; do not install it without approval.
5. Run the narrowest diagnostic checks first, then broader regression checks justified by the impact. Record exact commands and exit status. Do not silently rewrite failing tests to make implementation pass.
6. Distinguish failures that reproduce on the baseline from likely regressions when a safe comparison is available. Do not disturb the user's worktree merely to create a baseline.
7. For UI or runtime behavior, inspect the actual rendered or running result when feasible. For external dependencies, report mocks and sandbox evidence separately from live integration evidence.
8. Re-review the diff for secrets, debug artifacts, generated noise, compatibility breaks, and missing documentation.
9. Classify the outcome as pass, conditional pass, fail, or blocked. A conditional pass must state exactly what remains unverified and why.
10. If confirmed architecture, workflow, or operational knowledge changed, recommend `landing-capture` and identify the affected document or map.

## Output

Provide a compact matrix containing criterion, check, actual evidence, and result, followed by exact commands, failure details, unexecuted checks with reasons, diff findings, remaining risk, and the final classification.

## Completion standard

Complete only when every acceptance criterion has an honest status, executed checks have reproducible evidence, skipped checks are explicit, the final diff was reviewed, and the conclusion does not exceed the evidence. Build success alone is never sufficient proof of end-user behavior.

## Failure and fallback

If the environment prevents a check, capture the precise blocker and run the closest safe lower-level check without presenting it as equivalent. If tests are flaky, repeat only enough to characterize the flake and report both outcomes. Never hide a failure behind a summary count.
