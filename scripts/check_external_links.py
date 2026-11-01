#!/usr/bin/env python3
"""Report broken external links in the README.

This script never fails the build. External sites go down or rate-limit
requests at random, so the result is only a report. The report is written
to the GitHub job summary and printed to the log.

Standard library only.
"""

import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
TIMEOUT = 15
DELAY = 0.5  # seconds between requests, to be polite to servers
USER_AGENT = "Mozilla/5.0 (llm-course-link-checker)"
URL_PATTERN = re.compile(r"https?://[^\s\)\"'<>]+")


def extract_urls(text: str) -> list[str]:
    urls = []
    seen = set()
    for raw in URL_PATTERN.findall(text):
        url = raw.rstrip(".,;:")
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def check(url: str) -> tuple[bool, str]:
    """Return (ok, status). Try HEAD first, then GET if the server refuses HEAD."""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return True, str(resp.status)
        except urllib.error.HTTPError as err:
            if method == "HEAD" and err.code in (403, 405, 501):
                continue  # some servers do not allow HEAD, so retry with GET
            return False, str(err.code)
        except (urllib.error.URLError, TimeoutError, ValueError) as err:
            return False, type(err).__name__
    return False, "unknown"


def write_summary(lines: list[str]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")


def main() -> int:
    urls = extract_urls(README.read_text(encoding="utf-8"))
    broken = []
    for i, url in enumerate(urls, 1):
        ok, status = check(url)
        if not ok:
            broken.append((url, status))
            print(f"[{i}/{len(urls)}] BROKEN ({status}) {url}")
        else:
            print(f"[{i}/{len(urls)}] ok ({status}) {url}")
        time.sleep(DELAY)

    lines = [
        "## External link report",
        "",
        f"Checked **{len(urls)}** unique external links. Broken: **{len(broken)}**.",
        "",
    ]
    if broken:
        lines += ["| Status | URL |", "|---|---|"]
        lines += [f"| {status} | {url} |" for url, status in broken]
    write_summary(lines)

    print(f"Done. {len(broken)} broken out of {len(urls)}.")
    return 0  # report only: never fail the build


if __name__ == "__main__":
    sys.exit(main())
