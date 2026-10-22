#!/usr/bin/env python3
"""Validate Landing Kit's repository-level contracts using the standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "landing-scan",
    "landing-map",
    "landing-trace",
    "landing-change",
    "landing-verify",
    "landing-capture",
}
REQUIRED_BODY_TERMS = ("## Inputs", "## Workflow", "## Output", "## Completion standard", "## Failure and fallback")


def error(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def parse_frontmatter(path: Path, failures: list[str]) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        error(f"{path.relative_to(ROOT)} has invalid frontmatter boundaries", failures)
        return {}, text
    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            error(f"{path.relative_to(ROOT)} has malformed frontmatter line: {line}", failures)
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata, match.group(2)


def validate_skills(failures: list[str]) -> None:
    skill_root = ROOT / "skills"
    actual = {path.name for path in skill_root.iterdir() if path.is_dir()}
    if actual != EXPECTED:
        error(f"skill set mismatch: expected {sorted(EXPECTED)}, found {sorted(actual)}", failures)

    descriptions: dict[str, str] = {}
    for name in sorted(EXPECTED):
        folder = skill_root / name
        skill_path = folder / "SKILL.md"
        metadata, body = parse_frontmatter(skill_path, failures)
        if set(metadata) != {"name", "description"}:
            error(f"{name} frontmatter must contain only name and description", failures)
        if metadata.get("name") != name:
            error(f"{name} metadata name is {metadata.get('name')!r}", failures)
        description = metadata.get("description", "")
        if len(description) < 80:
            error(f"{name} description is too vague", failures)
        descriptions[name] = description
        for term in REQUIRED_BODY_TERMS:
            if term not in body:
                error(f"{name} is missing {term}", failures)
        if "TODO" in body or "[TODO" in body:
            error(f"{name} contains a TODO placeholder", failures)
        if "../../references/evidence-and-safety.md" not in body:
            error(f"{name} does not route to shared evidence and safety rules", failures)

        openai_yaml = folder / "agents" / "openai.yaml"
        if not openai_yaml.is_file():
            error(f"{name} is missing agents/openai.yaml", failures)
        else:
            yaml_text = openai_yaml.read_text(encoding="utf-8")
            if f"$%s" % name not in yaml_text:
                error(f"{name} default prompt does not explicitly mention ${name}", failures)

    if len(set(descriptions.values())) != len(descriptions):
        error("two skills have identical routing descriptions", failures)


def validate_manifests(failures: list[str]) -> None:
    paths = [ROOT / "plugin.json", ROOT / ".codex-plugin" / "plugin.json", ROOT / ".claude-plugin" / "plugin.json"]
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            error(f"cannot parse {path.relative_to(ROOT)}: {exc}", failures)
            continue
        if data.get("name") != "landing-kit" or data.get("version") != "0.1.0":
            error(f"{path.relative_to(ROOT)} identity/version mismatch", failures)
        if "TODO" in json.dumps(data):
            error(f"{path.relative_to(ROOT)} contains a TODO placeholder", failures)

    codex = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if codex.get("skills") != "./skills/":
        error("Codex compatibility manifest does not declare ./skills/", failures)


def validate_references(failures: list[str]) -> None:
    required = {
        "references/evidence-and-safety.md",
        "references/dependencies.md",
        "references/cross-platform.md",
        "references/responsibility-contracts.md",
        "evals/scenario-matrix.md",
        "evals/trigger-tests.md",
        "evals/safety-tests.md",
        "evals/visualization-tests.md",
        "README.md",
        "DEVELOPMENT.md",
        "STATUS.md",
        "LICENSE",
    }
    for relative in sorted(required):
        if not (ROOT / relative).is_file():
            error(f"missing required repository file: {relative}", failures)

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "[TODO" in text:
            error(f"{path.relative_to(ROOT)} contains a TODO placeholder", failures)


def main() -> int:
    failures: list[str] = []
    validate_skills(failures)
    validate_manifests(failures)
    validate_references(failures)
    if failures:
        print(f"\nValidation failed with {len(failures)} issue(s).")
        return 1
    print("PASS: six skills, shared references, evals, and three plugin manifests are structurally valid.")
    print("NOTE: static validation does not prove host discovery, runtime behavior, or visual quality.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
