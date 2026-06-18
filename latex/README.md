# LaTeX Draft Directory

This directory contains the working LaTeX draft for the survey:

**Memory Systems in Video Generation Models: From Token Retention to Entity and World-State Persistence**

## Current chat-generated revision

A v0.8.8 reviewer-response package was generated from the uploaded v0.8.7 zip. The downloadable package returned in chat contains the full IEEE/TMM source tree, figures, supplementary CSV, revision notes, and compiled PDF.

Key v0.8.8 changes:

- tighter abstract;
- clearer main-evidence vs supplementary/boundary-evidence treatment;
- expanded supplementary CSV schema;
- revised screening-statistics wording;
- persistent-vs-mutable identity-state table;
- judge-failure reliability table;
- explicit world-state scope tags;
- terminology cleanup toward coordinate/spectral memory;
- bibliography cleanup removing placeholder `Authors` citation authors.

## Compile

For the full package returned in chat:

```bash
cd TMM_Journal_Track_v0.8.8
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

In this environment, `bibtex` was available as `/usr/bin/bibtex.original`, so the compiled PDF was generated with:

```bash
pdflatex main
/usr/bin/bibtex.original main
pdflatex main
pdflatex main
```
