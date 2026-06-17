# LaTeX Draft Directory

This directory contains an AAAI-style LaTeX draft skeleton for the survey:

**Memory Systems in Video Generation and Video World Models: From KV Cache to Entity and World-State Memory**

## Important AAAI template note

`main.tex` is written against the AAAI author-kit convention:

```tex
\documentclass[letterpaper]{article}
\usepackage[submission]{aaai26}
```

The official AAAI style files are **not bundled here** because they should be obtained from the official AAAI author kit for the target year. Place the official files in this directory before compiling, typically:

```text
latex/aaai26.sty
latex/aaai.bst or latex/aaai26.bst
```

If the target venue changes, replace `aaai26` with the style file from the corresponding AAAI author kit.

## Compile

```bash
cd latex
latexmk -pdf main.tex
```

or:

```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

## Directory

```text
latex/
├── main.tex
├── references.bib
├── sections/
├── tables/
└── figures/
```
