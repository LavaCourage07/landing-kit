# Visualization tests

## Cases

1. **Archify available:** generate a system map and directory map, validate them with Archify, open them, and check source links.
2. **Archify absent, install declined:** confirm an official install option is offered once and a Mermaid map is completed without blocking.
3. **Insufficient evidence:** include a plausible but unreferenced service name in the prompt and confirm it is omitted or marked hypothetical.
4. **Changed architecture:** modify a fixture relationship, rerun capture/map, and confirm only affected diagrams change.
5. **Renderer failure:** force a render error and confirm the error is reported and valid Mermaid source remains available.

## Scoring rubric

Score each item 0 (absent/wrong), 1 (partial), or 2 (complete):

- the diagram answers a defined question;
- important nodes and edges cite source/config/test evidence;
- edge directions and labels match source;
- confirmed, inferred, and unknown relationships are distinguishable;
- generated output is opened or rendered, not merely written;
- fallback is accurately labeled and usable;
- update triggers are recorded.

Any fabricated relationship or false claim of interactive output is an automatic failure regardless of total score.
