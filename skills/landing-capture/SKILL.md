---
name: landing-capture
description: Preserve newly verified repository knowledge by incrementally updating the right architecture, module, workflow, decision, setup, testing, or troubleshooting documentation. Use after investigation or change work confirms durable facts, especially when maps or existing guidance became stale. Do not capture speculation, duplicate existing docs, upload private material, or rewrite unrelated documentation.
---

# Landing Capture

Turn durable evidence into the smallest useful documentation update. Read `../../references/evidence-and-safety.md`; read `../../references/dependencies.md` only when considering optional diagram or illustration tools.

## Inputs

Gather the verified findings, evidence paths, decisions and rationale, changed behavior, validation results, intended audience, and repository documentation conventions. Documentation edits require user authorization through the task or repository policy.

## Workflow

1. Search existing README, architecture, ADR, runbook, testing, and troubleshooting material before creating anything.
2. Classify each candidate statement as durable fact, decision, operational procedure, transient result, inference, or unknown. Capture durable verified material; keep transient logs out unless they are needed as a dated incident or evaluation record.
3. Choose the canonical destination. Update an existing document when possible; create a new focused document only when no appropriate home exists.
4. Make a minimal update scoped to knowledge confirmed by the current work. Preserve unrelated wording and authorship.
5. Add source/config/test references and a verification date where drift is likely. Phrase inference and unknowns explicitly.
6. Invoke `landing-map` when component boundaries or a key flow changed. Update only affected maps and their evidence index.
7. Optionally use an installed Xiaohei illustration skill only when the user wants explanatory art and the concept is already verified. Ask before installation or external upload; keep Markdown and Mermaid as the baseline.
8. Check links, commands, diagrams, and statements against current source. Review the documentation diff for duplication, secrets, and unrelated churn.

## Output

Report documents changed, knowledge added or corrected, evidence used, links or commands checked, stale material removed or retained, map updates, explicit unknowns, and remaining maintenance triggers.

## Completion standard

Complete only when the update has one clear canonical home, matches source and validation evidence, does not present inference as fact, avoids duplication, and leaves unrelated documentation untouched.

## Failure and fallback

If existing documents conflict, preserve both until evidence resolves the conflict and flag it clearly. If the correct destination is unclear, return a proposed patch location instead of scattering new files. If optional tools are missing, use plain Markdown and Mermaid without blocking knowledge capture.
