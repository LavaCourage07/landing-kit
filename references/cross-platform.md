# Cross-platform behavior

Verified against official OpenAI and Anthropic documentation on 2026-10-22. Recheck before release.

## Common source

Keep portable Skill instructions under `skills/<name>/SKILL.md`. Both hosts discover a Skill from its metadata first and load the body when selected. Keep host-specific metadata outside the shared instructions:

- `plugin.json`: portable Agent Plugins manifest.
- `.codex-plugin/plugin.json`: Codex compatibility and UI metadata.
- `.claude-plugin/plugin.json`: Claude Code plugin metadata.
- `skills/*/agents/openai.yaml`: optional Codex-facing Skill presentation.

Do not embed host-specific tool names in the shared workflow when the same action can be described by capability.

## Codex

Official references:

- <https://developers.openai.com/plugins/build/plugins>
- <https://developers.openai.com/plugins/build/skills>

The portable plugin layout discovers skills from root `skills/`. Local marketplace installation is distinct from merely cloning a repository. During local development, follow the current personal or repository marketplace workflow and restart or refresh as documented. A repository-local `.agents/skills/` copy/link is useful for direct Skill testing but is not proof that plugin packaging works.

Verify separately:

1. manifest validation;
2. plugin installation/discovery in the chosen Codex client;
3. metadata-triggered selection;
4. explicit `$landing-*` invocation;
5. actual file/tool behavior under the client's approval model.

## Claude Code

Official references:

- <https://code.claude.com/docs/en/skills>
- <https://code.claude.com/docs/en/plugins>

Claude Code loads plugin skills from `<plugin>/skills/<name>/SKILL.md` and namespaces commands by plugin. For direct testing, personal skills live under `~/.claude/skills/` and project skills under `.claude/skills/`. Project and personal copies do not prove marketplace/plugin installation, so test both discovery paths when claiming cross-platform acceptance.

Verify separately:

1. plugin manifest and marketplace installation;
2. `/landing-kit:landing-scan` or the command name shown by the host;
3. automatic description-based selection;
4. supporting-file resolution from the installed plugin;
5. tool permissions and confirmation gates.

## Invocation boundary

A Skill may recommend another Skill, but cross-Skill calls are not a portable function-call API. The agent must use the skills advertised by its host. When the target Skill is unavailable, apply the documented fallback and disclose it.

## Release evidence

Do not claim Codex or Claude Code support from file layout alone. Record client/version, installation path, discovery result, trigger prompt, observed workflow, generated artifacts, and any permission prompts in a dated evaluation result.
