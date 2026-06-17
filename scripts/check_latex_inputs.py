#!/usr/bin/env python3
"""Check the LaTeX draft structure.

Run from repository root:
  python3 scripts/check_latex_inputs.py
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
MAIN = LATEX / "main.tex"

input_re = re.compile(r"\\input\{([^}]+)\}")
cite_re = re.compile(r"\\cite[t,p]?\{([^}]+)\}")
bib_entry_re = re.compile(r"@\w+\s*\{\s*([^,]+)")


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def main() -> int:
    errors = []
    warnings = []

    if not MAIN.exists():
        print(f"[FAIL] missing {rel(MAIN)}")
        return 1

    main_text = MAIN.read_text(encoding="utf-8")
    tex_files = [MAIN]

    for target in input_re.findall(main_text):
        p = LATEX / f"{target}.tex"
        if not p.exists():
            errors.append(f"missing input file: {rel(p)}")
        else:
            tex_files.append(p)

    for section in list(tex_files):
        if section == MAIN:
            continue
        text = section.read_text(encoding="utf-8")
        for target in input_re.findall(text):
            p = LATEX / f"{target}.tex"
            if not p.exists():
                errors.append(f"missing nested input file: {rel(p)}")
            elif p not in tex_files:
                tex_files.append(p)

    bib = LATEX / "references.bib"
    if not bib.exists():
        errors.append("missing latex/references.bib")
        bib_keys = set()
    else:
        bib_keys = set(bib_entry_re.findall(bib.read_text(encoding="utf-8")))

    all_tex = "\n".join(p.read_text(encoding="utf-8") for p in tex_files if p.exists())
    cite_keys = set()
    for group in cite_re.findall(all_tex):
        for key in group.split(","):
            key = key.strip()
            if key:
                cite_keys.add(key)

    missing_cites = sorted(cite_keys - bib_keys)
    if missing_cites:
        errors.append("missing BibTeX keys: " + ", ".join(missing_cites[:30]))

    if not (LATEX / "aaai26.sty").exists():
        warnings.append("latex/aaai26.sty not found; copy it from the official AAAI author kit before compiling")
    if not ((LATEX / "aaai26.bst").exists() or (LATEX / "aaai.bst").exists()):
        warnings.append("AAAI bibliography style file not found yet")
    if not (LATEX / "figures" / "FIGURE_REQUESTS.md").exists():
        warnings.append("missing latex/figures/FIGURE_REQUESTS.md")

    print(f"Checked {len(tex_files)} LaTeX files.")
    print(f"Citations used: {len(cite_keys)}; BibTeX entries: {len(bib_keys)}")

    for w in warnings:
        print(f"[WARN] {w}")

    if errors:
        for e in errors:
            print(f"[FAIL] {e}")
        return 1

    print("[OK] LaTeX structure checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
