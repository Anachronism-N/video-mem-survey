# 39 v0.8.5 Systematic Protocol and Benchmark Audit

> Stage: continue journal-first writing after v0.8.4 figure insertion.  
> Goal: address reviewer comments about survey-systematicity, benchmark-level comparison, publication-status labels, scope boundaries, and draft-like language.

## 1. Main update

v0.8.5 targets the most important remaining review concerns:

1. the survey methodology was still too high-level;
2. the benchmark discussion needed benchmark-level audit rather than only conceptual evaluation;
3. recent arXiv / technical report reliance needed clearer publication-status handling;
4. world-state memory needed sharper boundary control;
5. the manuscript still contained draft-like meta-language.

## 2. Survey protocol table

A new survey protocol table is added in Section II. It explicitly lists:

- time span;
- sources;
- keyword groups;
- inclusion criteria;
- exclusion / weak cases;
- coding axes;
- publication-status labels;
- verification process.

This improves the transition from a subjective literature map to an inspectable survey coding scheme.

## 3. Benchmark-level audit table

The benchmark audit table is expanded into a more detailed comparison with columns:

```text
Benchmark | Year / status | Task setting | Memory facts / dimensions | Probe and judge | Metrics / outputs | Strength | Blind spot
```

It now compares MIND, MBench, WorldScore, iWorld-Bench, NarraStream-Bench, EntityBench, Echo-Memory, and VQeval / long-video metrics.

## 4. Publication-status coding

A new publication-status coding table is added to the audit section. It separates peer-reviewed papers, arXiv preprints, technical reports, benchmark papers, adjacent surveys, and boundary/reference-only methods. This addresses the risk that the manuscript overstates consensus from recent 2025--2026 preprints.

## 5. World-state boundary tags

Section IX now adds explicit boundary tags:

- direct video generation;
- generative world simulation;
- interactive video generation;
- driving / embodied boundary case;
- evaluation-only reference.

This keeps the world-state section from drifting into a general robotics or embodied-AI survey.

## 6. Draft-language cleanup

Several internal-development phrases were removed from the manuscript, including references to a working skeleton, future journal version, and final submission promises. The title was also revised to:

```text
Memory Systems in Video Generation Models: From Token Retention to Entity and World-State Persistence
```

## 7. Compilation and rendering status

Local artifacts:

```text
TMM_Journal_Track_v0.8.5_preview.pdf
TMM_Journal_Track_v0.8.5.zip
```

The PDF compiles successfully with IEEEtran style. There are no undefined citations or undefined references after BibTeX and repeated LaTeX passes. The rendered preview has 30 pages. Key newly affected pages were rendered and visually checked, including the survey protocol table and detailed benchmark audit table.

## 8. Remaining work

1. Extend paper-level audit tables from representative core methods to the complete corpus.
2. Continue method-level deepening in identity/entity memory and positional/spectral memory.
3. Normalize all BibTeX metadata, author order, capitalization, venue, and arXiv IDs.
4. Decide which dense pseudo-algorithmic tables should remain in main text versus appendix.
5. Add real or semi-real generated failure examples in appendix if available.
