# Revision notes for v0.8.9

This update responds to the latest v0.8.8 review. The review judged the paper no longer under-length, but still requested a harder benchmark audit, better status-label visibility, tighter main-text organization, stronger paper-level comparison, and stricter world-state boundary control.

## Main changes

1. **Benchmark hardening.** Replaced the benchmark audit with a more concrete two-part table that separates task setting, memory facts, return-gap/probe design, judging, metrics, scale/public assets, and blind spots.
2. **Benchmark reporting checklist.** Added a dedicated reporting checklist for prompt/video count, video length, generation mode, return-gap design, memory-fact schema, judge prompts, scoring scripts, human agreement, and release assets.
3. **Status labels visible in main text.** Moved the publication-status coding table into the methodology section and clarified that status is a confidence label, not an exclusion criterion.
4. **Main-text compression.** Moved route-specific pseudo-algorithmic tables from route sections into an appendix-style section. The main sections now emphasize synthesis and method comparison rather than repeating formula-table patterns.
5. **Formula grounding.** Added explicit wording that the formal interfaces are coding lenses, not proposed algorithms or new benchmark definitions.
6. **Identity/entity deepening.** Added a concrete failure pattern: identity can be preserved while mutable fields such as possession, location, relation, or narrative role remain stale.
7. **World-state boundary control.** Recast world-state memory as three layers: scene-revisit memory, hidden-state memory, and action-conditioned world-state memory.
8. **Supplementary CSV closure.** Renamed the machine-readable audit file to `supplementary_coverage_v089_full_corpus.csv` and kept the schema aligned with the main-text statistics.

## Validation

The v0.8.9 PDF was compiled successfully with pdflatex -> bibtex -> pdflatex -> pdflatex and rendered for visual QA. Final compiled length: 35 pages.

## Remaining risk

The corpus still contains many 2025--2026 emerging methods. They are explicitly status-coded and should be rechecked before camera-ready submission, especially for arXiv IDs, public assets, judge prompts, data scale, and venue status.
