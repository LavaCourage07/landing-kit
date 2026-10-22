# External dependencies

Verified against upstream documentation on 2026-10-22. Recheck before publishing commands because host integrations change.

## Archify

- Purpose: preferred interactive renderer for `landing-map` and the default visualization attempt during `landing-scan`.
- Upstream: <https://github.com/tt-a1i/archify>
- License: MIT.
- Advertised platforms: Claude Code, Codex CLI, Cursor, and OpenCode.
- Current upstream install: `npx skills add tt-a1i/archify -g`.
- Current no-install Codex trial: `npx skills use tt-a1i/archify@archify --agent codex`.
- Detection: inspect the host's advertised skills or official skill/plugin manager first. If shell inspection is appropriate, check the documented platform skill location rather than one hard-coded path.
- Verification: start a fresh session, confirm the `archify` skill is discoverable, generate a small diagram, run its validator, and open the result.
- Fallback: generate evidence-linked Mermaid source and state that it is neither Archify nor an interactive artifact.

Do not run the `npx` commands without approval: they can download and execute third-party packages.

## Superpowers

- Purpose: optional source of mature brainstorming, planning, TDD, systematic debugging, review, and branch-finish workflows.
- Upstream: <https://github.com/obra/superpowers>
- License: MIT.
- Codex: install through the official Codex plugin marketplace by opening `/plugins`, searching for `superpowers`, and selecting install.
- Claude Code: install from Anthropic's official marketplace with `/plugin install superpowers@claude-plugins-official`.
- Detection: use the host's skill/plugin inventory. Do not assume that writing a skill name in another Skill guarantees invocation.
- Verification: start a new session and use a small development request that should activate its planning workflow; confirm the skill actually loads.
- Fallback: use the focused planning, safety, test-first, debugging, and verification steps embedded in `landing-change` and `landing-verify`.

## Xiaohei Illustrations

- Purpose: optional explanatory art after a concept or process has already been verified.
- Upstream: <https://github.com/helloianneo/ian-xiaohei-illustrations>
- Detection and install: follow the host's current Skill mechanism and upstream instructions.
- Verification: generate a disposable preview from non-sensitive material and inspect it visually.
- Fallback: retain Markdown, source-linked Mermaid, and plain explanation.

## NotebookLM

- Purpose: optional external interface over curated project knowledge.
- Security: do not upload repository material until organization policy and user authorization permit it.
- Fallback: keep knowledge in repository Markdown and source-linked diagrams.

## Rules

Check only dependencies relevant to the current task. Explain purpose, impact, official source, verification, and fallback before offering installation. After installation, verify behavior rather than assuming success from a package-manager exit code.
