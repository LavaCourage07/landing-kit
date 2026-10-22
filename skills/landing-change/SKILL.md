---
name: landing-change
description: Plan and implement a focused, authorized change in an existing repository while preserving uncommitted work and established conventions. Use for features, fixes, refactors, or cross-module changes that require impact analysis, safe editing, and handoff to verification. Do not use for analysis-only requests, production deployment, destructive migration, or unrelated cleanup unless explicitly authorized.
---

# Landing Change

Implement the smallest coherent change that satisfies explicit acceptance criteria. Read `../../references/evidence-and-safety.md`; consult `../../references/dependencies.md` only if reusing Superpowers.

## Inputs

Establish the requested behavior, acceptance criteria, constraints, non-goals, repository root, and whether edits are authorized. Resolve only questions whose answers materially change behavior, safety, or public contracts.

## Workflow

1. Read repository instructions and inspect branch, status, and relevant diffs. Treat all pre-existing changes as user work. Do not overwrite, revert, stage, or reformat them unnecessarily.
2. Invoke `landing-trace` when the change crosses unfamiliar boundaries or the real call chain is not yet supported by evidence.
3. Identify affected contracts, files, tests, data, permissions, dependencies, compatibility promises, and operational risks.
4. Prefer the applicable installed Superpowers workflow for brainstorming, planning, TDD, systematic debugging, or review. Do not assume skill-to-skill invocation is supported: use the host's advertised skill mechanism. If unavailable, apply the equivalent compact steps here and mention the fallback; do not install without approval.
5. Form a minimal plan with acceptance checks. Use an isolated branch or worktree only when it benefits the task and does not hide or strand current changes. Creating or deleting worktrees, branches, or stashes requires alignment with user intent and repository policy.
6. Add or update the narrowest useful test first when behavior is testable. Confirm the test's failure reason before implementation when practical.
7. Edit only relevant files, preserve local style and public contracts, and avoid speculative abstraction or adjacent cleanup.
8. Run focused checks while iterating. When blocked, diagnose from concrete errors; do not repeatedly apply the same unverified fix.
9. Hand the acceptance criteria, changed paths, known risks, and commands already run to `landing-verify`.

## Safety gates

Obtain confirmation before destructive Git operations, dependency installation, production deployment, irreversible migration, secret or credential changes, external writes, or broad deletion. Never expose secrets in logs. Never claim implementation complete before verification.

## Output

Report acceptance criteria, impact and risk, implementation summary, changed files, checks run so far, pre-existing work preserved, and remaining issues. Do not create a commit, push, or deploy unless the user requested it.

## Completion standard

Implementation is ready for verification only when the requested code change exists, scope is controlled, pre-existing work is intact, relevant tests were added or their absence explained, and `landing-verify` has a concrete acceptance contract.

## Failure and fallback

If repository state overlaps the intended edits, pause before overwriting and explain the exact conflict. If a required dependency or environment is unavailable, preserve partial work, report the verified blocker, and propose a reversible next step. Do not broaden scope to work around a product decision without approval.
