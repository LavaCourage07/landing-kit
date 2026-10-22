# First-version status

Last updated: 2026-10-22

## Completed

- Researched current Agent Skills, Codex plugin, Claude Code Skill, Archify, and Superpowers documentation.
- Defined non-overlapping contracts for all six planned Skills.
- Implemented six shared `SKILL.md` workflows and Codex UI metadata.
- Added Archify-first visualization with explicit Mermaid fallback and no automatic third-party installation.
- Added shared evidence, Git safety, dependency, and cross-platform rules.
- Added portable, Codex-compatible, and Claude Code plugin manifests.
- Added trigger, safety, visualization, and scenario evaluation specifications.
- Added a repository validator for structure, metadata, references, and manifests.
- Completed a developer self-scan with a source-linked Mermaid fallback and an honest conditional-pass result.
- Passed local Claude Code plugin validation; the validator reported non-blocking marketplace icon and unpublished-install-line advice.

## Known limits

- This checkout has not yet been installed through a published Codex or Claude marketplace.
- No marketplace icon is included in v0.1.0 because no brand asset has been selected.
- Archify and Superpowers are not bundled; their end-to-end integrations still require host-level installation tests.
- Multi-stack evaluation prompts are defined, but results from independent real repositories are not yet recorded.
- Mermaid fallback can be source-validated here, but visual quality still requires rendering and human or agent inspection.
- The first version contains workflow instructions, not an independent orchestration service or Web UI.

## Next milestone

Run the scenario matrix against at least three unrelated repositories (frontend, backend, and multi-service), test both host installation paths, inspect generated maps, and revise the Skills from observed failures before a stable release.
