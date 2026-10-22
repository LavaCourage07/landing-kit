# Evaluation guide

Static validation is necessary but not sufficient. Run these evaluations in fresh sessions so success depends on the installed Skill rather than prior conversation context.

1. Select an unrelated real repository and record its commit, dirty state, size, and stack in `scenario-matrix.md`.
2. Install or expose Landing Kit through the host mechanism under test.
3. Run prompts from `trigger-tests.md`, including negative controls.
4. Run applicable cases from `safety-tests.md` and `visualization-tests.md`.
5. Save a dated result under `evals/results/` with raw prompt, observed Skill selection, commands, artifacts, failures, and evidence.
6. Score only observed behavior. Do not award a pass because `SKILL.md` contains the expected wording.

A release candidate needs results from Codex and Claude Code and at least three unrelated repositories: frontend, backend/API, and multi-service or full-stack.
