#!/usr/bin/env python3
"""Check the local (offline) links and images in the README.

Only the standard library is used, so CI needs no installs.
External URLs are NOT checked here on purpose: they change often and
would make CI fail for reasons unrelated to the code.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_SRC = re.compile(r'(?:src|href)="([^"]+)"')
HEADING = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)


def slugify(heading: str) -> str:
    """Approximate GitHub's heading anchor rules."""
    text = heading.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)  # drops emoji and punctuation
    return text.replace(" ", "-")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:"))


def main() -> int:
    content = README.read_text(encoding="utf-8")
    anchors = {slugify(h) for h in HEADING.findall(content)}
    targets = MD_LINK.findall(content) + HTML_SRC.findall(content)

    errors = []
    checked = 0
    for target in targets:
        if is_external(target):
            continue
        checked += 1
        if target.startswith("#"):
            if target[1:] not in anchors:
                errors.append(f"Broken anchor: {target}")
            continue
        path_part = target.split("#", 1)[0]
        if not (ROOT / path_part).exists():
            errors.append(f"Missing file: {path_part}")

    print(f"Checked {checked} local links and images.")
    for err in errors:
        print(f"ERROR: {err}")
    if errors:
        return 1
    print("All local links are OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
