# 40 v0.8.6 Screening Statistics, Scope Control, and Formalism Binding

> Stage: continue journal-first writing after v0.8.5.  
> Goal: address the new Major Revision comments by adding screening statistics, stronger audit support, benchmark-level fields, scope exclusions, formalism-to-method binding, and draft-language cleanup.

## 1. Main update

v0.8.6 targets the next set of reviewer-style concerns:

1. survey methodology still lacked quantitative screening statistics;
2. the paper-level audit needed a clearer full-corpus evidence layer;
3. benchmark audit needed generation type, probe/return-gap design, judge/metric, and reproducibility blind spots;
4. formulas needed to be tied to method coding rather than used as decorative formalism;
5. the paper needed a clearer "what this survey does not cover" boundary;
6. identity/entity/narrative memory needed more paper-level contrast;
7. the conclusion still contained draft-like "next revision" language.

## 2. Screening and coding statistics

A new screening/statistics table is added in Section II. It reports a current coded corpus of 108 normalized records and summarizes:

- core/mainline memory methods;
- high-support and related works;
- background / adjacent works;
- benchmark records;
- main-text priority records;
- web-verified records;
- records still requiring final bibliographic verification;
- primary-route distribution.

The counts are derived from the full-corpus coding CSV distributed with the source package:

```text
tables/supplementary_coverage_v086_full_corpus.csv
```

This gives the survey a more inspectable evidence layer, even though final manual bibliography normalization remains necessary before submission.

## 3. Full corpus audit artifact

The complete 108-record coding table is now included as a machine-readable supplementary CSV in the source package. It contains fields such as paper, year, arXiv ID, primary route, memory object, memory substrate, lifecycle focus, training regime, role tier, main-body priority, discussion role, URL, verification status, source, normalized key, and arXiv number.

The PDF reports summary counts and route distribution, while the source package contains the full machine-readable audit table. This avoids making the main text unreadable while still making the taxonomy inspectable.

## 4. Benchmark audit expansion

The benchmark audit table is revised with more specific fields:

```text
Benchmark | Status | Generation type / task | Memory facts tested | Probe / return-gap design | Judge / metric | Main strength | Blind spot / reproducibility concern
```

This explicitly separates retrieval quality, generation quality, and memory faithfulness, and it prevents the evaluation section from collapsing into a generic metric discussion.

## 5. Formalism-to-method binding

A new table explains how the main formulas map to method coding:

- cache priority score;
- retrieval score;
- entity record;
- world-state record;
- memory score.

For each interface, the table identifies the terms used for coding, representative instantiations, and the comparison enabled. This addresses the concern that formulas might otherwise appear decorative.

## 6. Scope-control improvements

Section II now includes a "What this survey does not cover" subsection. It excludes pure video understanding, pure robotics policy learning, ordinary LLM memory, non-generative world modeling, and local smoothing methods unless they directly clarify video-generation memory mechanisms, evaluation protocols, or world-state boundary cases.

Section IX had already added boundary tags for direct video generation, generative world simulation, interactive video generation, driving/embodied boundary cases, and evaluation-only references. v0.8.6 reinforces this boundary through the scope statement.

## 7. Identity/entity contrast expansion

Section VII now includes a more explicit paper-level contrast from reference anchors to revisable entity state:

- reference-anchor methods preserve appearance but usually do not specify attribute revision;
- identity embedding / adapter methods strengthen persistent identity but often keep revision implicit;
- slot-based methods help multi-entity disambiguation but require robust slot assignment and merging;
- entity-table and verification-loop methods make identity-state separation explicit.

This strengthens the identity-state disentanglement argument.

## 8. Draft-language cleanup

The conclusion no longer says that the next revision should complete missing contributions. It now presents the paper's current contributions and closes with the integrated research agenda.

## 9. Compilation and rendering status

Local artifacts:

```text
TMM_Journal_Track_v0.8.6_preview.pdf
TMM_Journal_Track_v0.8.6.zip
```

The PDF compiles successfully using IEEEtran style. BibTeX compilation uses `bibtex8` in the current environment. There are no undefined citations or undefined references after repeated LaTeX passes. The rendered preview has 31 pages. Newly affected pages containing the screening/statistics table, benchmark audit, and formalism-binding table were rendered and visually checked.

## 10. Remaining work

1. Continue normalizing BibTeX metadata, author order, capitalization, venues, arXiv IDs, DOIs, project links, and access dates.
2. Decide which dense pseudo-algorithmic views should be moved from main text to appendix in a final journal layout pass.
3. Further expand positional/coordinate memory and identity/entity memory with pairwise method comparisons if space allows.
4. Add real or semi-real generated failure examples in appendix if model outputs become available.
