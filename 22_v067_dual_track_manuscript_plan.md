# 22 v0.6.7 Dual-Track Manuscript Plan

> Stage: split the project into an AAAI conference track and a full-length journal track.  
> Goal: preserve all technical material while producing a page-constrained AAAI version.

## 1. Rationale

The project now contains enough material for two related but different manuscripts:

1. **AAAI conference version.**  
   A selective, dense, 7-page technical-content paper with references. Its goal is to present the central memory-system taxonomy, show the strongest evidence, and demonstrate novelty relative to adjacent surveys.

2. **Journal / full-length version.**  
   A comprehensive version without the current page constraint. Its goal is to provide full route-level analysis, extensive method tables, detailed figure discussion, supplementary coverage, and more complete future directions.

Both versions should share the same title family, bibliography, paper database, figure assets, and coverage table. They should differ in scope, density, and figure/table placement.

## 2. Shared source assets

Both versions should use:

- `tables/supplementary_coverage_*`: full coverage table.
- `latex/figures/`: F1--F10 and later refined figures.
- `notes/paper_notes/`: detailed paper notes.
- `latex/references.bib`: normalized bibliography after cleanup.
- A shared taxonomy vocabulary:
  - Memory Object.
  - Memory Substrate.
  - Memory Lifecycle.
  - Training Regime.

## 3. AAAI version target

### Target structure

```text
Abstract
1. Introduction
2. Memory Failures and Requirements
3. Three-Layer Taxonomy of Video Memory
4. Method Landscape: Technical Routes with a Lifecycle Lens
5. Deep Dive: Memory Mechanisms across Representative Routes
6. Evaluation and Open Problems
7. Conclusion
References
```

### Main figures/tables

Keep only:

- Figure 1: memory systems overview, possibly compressed.
- Figure 4: lifecycle subway map.
- One compact LaTeX evaluation table, converted from Figure 10.
- One compact route-by-lifecycle table if space allows.

Move to supplementary:

- Figure 2, Figure 3 if merged into Figure 1, Figure 5, Figure 6, Figure 7, Figure 8, Figure 9, alternative Figure 4 radial view, image-version Figure 10.
- Detailed method-family tables.
- Full coverage table.

### Writing style

The AAAI version should be argumentative and selective:

- It should not attempt to describe every paper in the main text.
- It should use representative methods to support the taxonomy.
- It should repeatedly point to the full supplementary coverage table.
- It should emphasize what is new compared with adjacent surveys.

## 4. Journal / full-length version target

### Target structure

```text
Abstract
1. Introduction
2. Background and Related Surveys
3. Memory Failures and Requirements
4. Three-Layer Taxonomy of Video Memory
5. Training Regimes for Video Memory Systems
6. Implicit Token Memory in Attention and KV Caches
7. Remembering Time: Positional and Spectral Memory
8. From Identity Anchors to Entity-Narrative Memory
9. Retrieval-Augmented Recall in Video Generation
10. From Visual Continuity to World-State Persistence
11. Memory Evaluation Beyond Surface Consistency
12. Method Landscape and Cross-Route Interactions
13. Open Problems and Research Agenda
14. Conclusion
Appendix A. Full paper coverage table
Appendix B. Additional method-family tables
Appendix C. Additional figures and prompt/design notes
```

### Figures/tables

The journal version can keep:

- F1--F10.
- Both Figure 4 variants if they serve different explanatory purposes.
- Category-level synthesis figures, especially:
  - training-free vs trained memory spectrum;
  - world-state memory design patterns.
- Full method tables for each route.
- Full benchmark comparison table.
- Full 100+ paper coverage table.

### Writing style

The journal version should be comprehensive and pedagogical:

- Each route should follow the eight-part analysis template.
- It should discuss method limitations and evaluation implications in detail.
- It should include more direct comparisons among methods.
- It should explain why some background world models are not mainline memory methods.

## 5. Directory proposal

Create the following structure in a later pass:

```text
latex_aaai/
  main.tex
  sections/
  tables/
  figures/

latex_journal/
  main.tex
  sections/
  tables/
  figures/

shared/
  figures/
  bib/
  coverage/
```

For now, the existing `latex/` directory can continue to hold the working draft. The split should happen after references and coverage table are cleaned enough.

## 6. Versioning policy

Use:

```text
v0.6.x = working material and planning
v0.7.x = dual-track source split begins
v0.8.x = AAAI-style 7-page draft stabilizes
v0.9.x = official AAAI template migration and final citation audit
```

The journal track can progress in parallel but should not block the AAAI version.

## 7. Immediate next action

The next practical pass should:

1. Create a journal outline source from the long draft.
2. Keep the current compression draft as the AAAI skeleton.
3. Convert Figure 10 to LaTeX table in both tracks.
4. Deepen Section 9 or Section 5 first in the journal version.
5. Use the deepened section to compress a representative paragraph into the AAAI version.

## 8. Important rule

Do not delete detailed material when compressing the AAAI version. Move it to the journal draft or supplement. The AAAI paper should be selective; the journal paper should be comprehensive.
