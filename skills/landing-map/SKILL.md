---
name: landing-map
description: Turn verified repository structure, dependencies, and behavior into source-linked architecture, directory, or flow maps. Use during first-time codebase scans, architecture explanation, cross-module tracing, or after changes make existing diagrams stale. Prefer Archify when available and degrade to Mermaid when it is not; do not use for decorative diagrams unsupported by source evidence.
---

# Landing Map

Create the smallest map that makes verified relationships easier to understand. Read `../../references/evidence-and-safety.md` and, when checking or installing a renderer, `../../references/dependencies.md`.

## Inputs

Obtain the repository root, map question, intended audience, relevant scan or trace findings, and output location. When findings are not supplied, inspect the minimum source and configuration needed to verify the nodes and edges.

## Workflow

1. Choose map types from the question rather than generating every possible diagram:
   - system/context map for deployable components and external systems;
   - key-directory map for code ownership and navigation;
   - sequence or flow map for a verified behavior;
   - data or state map when persistence and transitions are central.
2. Build an evidence ledger before rendering. Give every nontrivial node and edge at least one source path, configuration entry, test, or observed runtime fact. Mark inferred relationships explicitly and omit unsupported ones.
3. Check the advertised skills/tools and the host's official discovery mechanism for Archify. Do not infer absence only because a guessed directory does not exist.
4. If Archify is available, invoke its installed skill and follow its current renderer and validation workflow. Pass only verified relationships and request source references in the output.
5. If Archify is unavailable, explain its value and current official installation option from `dependencies.md`. Ask before installing. Continue with Mermaid unless the user specifically requires Archify output and chooses to pause.
6. Save persistent output only when authorized. Follow an existing documentation convention; otherwise propose `docs/landing-kit/`. Keep a Markdown entry point beside generated artifacts.
7. Validate that every edge direction, label, boundary, and source link matches the evidence. Open or render the result when tooling permits; syntax validation alone does not establish visual quality.
8. Record the generation method, validation performed, unresolved relationships, and the source files that should trigger a future update.

## Output contract

Return or write:

- map purpose and scope;
- interactive Archify artifact/link when successfully generated, otherwise Mermaid source;
- evidence index mapping important nodes and edges to source paths;
- confirmed, inferred, and unknown relationships;
- renderer used, validation evidence, and limitations;
- update triggers for later changes.

Never claim Mermaid is an interactive Archify artifact. Never add components solely because their directory names resemble a familiar architecture.

## Completion standard

Complete only when the map answers a defined question, its important relationships are traceable to evidence, the artifact can be opened or its source validates, and fallback limitations are explicit. Visual polish cannot compensate for unsupported relationships.

## Failure and fallback

If Archify invocation fails, retain the concise error, avoid repeated blind retries, and produce Mermaid. If Mermaid rendering is unavailable, return a fenced Mermaid block and state that it was not rendered. If evidence is insufficient, create a partial map with unknown boundaries instead of inventing a complete one.
