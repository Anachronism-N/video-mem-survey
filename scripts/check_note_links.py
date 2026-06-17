#!/usr/bin/env python3
"""Check paper-note index/status links for the video-mem-survey repository.

Run from repository root:
  python3 scripts/check_note_links.py
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "notes" / "paper_notes"
INDEX_FILE = NOTES_DIR / "WEB_READ_INDEX_v0.4.md"
STATUS_FILE = NOTES_DIR / "WEB_READ_STATUS_v0.4.csv"
ALL_NOTES_DIR = NOTES_DIR / "web_read_all_v0.4"

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[OK] {message}")


def warn(message: str) -> None:
    print(f"[WARN] {message}")


def main() -> int:
    errors: list[str] = []

    if not NOTES_DIR.exists():
        errors.append(f"missing notes directory: {rel(NOTES_DIR)}")
    if not ALL_NOTES_DIR.exists():
        errors.append(f"missing note directory: {rel(ALL_NOTES_DIR)}")
    if not INDEX_FILE.exists():
        errors.append(f"missing index: {rel(INDEX_FILE)}")
    if not STATUS_FILE.exists():
        errors.append(f"missing status CSV: {rel(STATUS_FILE)}")

    if errors:
        for e in errors:
            fail(e)
        return 1

    note_files = sorted(ALL_NOTES_DIR.glob("*.md"))
    if len(note_files) == 102:
        ok("found 102 per-paper Markdown notes")
    else:
        errors.append(f"expected 102 per-paper notes, found {len(note_files)}")

    index_text = INDEX_FILE.read_text(encoding="utf-8")
    index_links = LINK_RE.findall(index_text)
    missing_index_links = []
    for link in index_links:
        target = (INDEX_FILE.parent / link).resolve()
        if not target.exists():
            missing_index_links.append(link)
    if missing_index_links:
        errors.append("broken links in WEB_READ_INDEX_v0.4.md: " + ", ".join(missing_index_links[:10]))
    else:
        ok(f"all {len(index_links)} Markdown links in WEB_READ_INDEX_v0.4.md resolve")

    with STATUS_FILE.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) == 102:
        ok("WEB_READ_STATUS_v0.4.csv has 102 rows")
    else:
        errors.append(f"expected 102 rows in status CSV, found {len(rows)}")

    missing_status_paths = []
    status_counts: dict[str, int] = {}
    for row in rows:
        status = row.get("reading_status", "").strip() or "<empty>"
        status_counts[status] = status_counts.get(status, 0) + 1
        note_path = row.get("note_path", "").strip()
        if not note_path:
            missing_status_paths.append("<empty note_path>")
            continue
        target = ROOT / note_path
        if not target.exists():
            missing_status_paths.append(note_path)
    if missing_status_paths:
        errors.append("missing note_path targets in status CSV: " + ", ".join(missing_status_paths[:10]))
    else:
        ok("all note_path targets in WEB_READ_STATUS_v0.4.csv exist")

    print("\nReading-status counts:")
    for key in sorted(status_counts):
        print(f"  {key}: {status_counts[key]}")

    if errors:
        print("\nErrors:")
        for e in errors:
            fail(e)
        return 1

    print("\nAll note-link checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
