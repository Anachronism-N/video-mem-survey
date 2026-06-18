# 41 v0.8.7 Final Polish: Judge Reliability and Identity-State Disentanglement

> Stage: continue journal-first writing after v0.8.6.  
> Goal: respond to the latest Minor Revision / Weak Accept style comments by tightening evidence-layer explanations, judge reliability, identity-state disentanglement, and final manuscript polish.

## 1. Main update

v0.8.7 focuses on finishing issues rather than redesigning the framework. The latest review states that the paper is now closer to a Transactions-level survey, but still needs final polishing on bibliography verification, full-corpus audit availability, benchmark judge reliability, table density, and terminology consistency.

This pass addresses several of these issues directly in the manuscript.

## 2. Full-corpus audit relation clarified

Section II and the audit section now more explicitly explain the relation between:

- compact main-text tables;
- representative route-level audit tables;
- the full machine-readable supplementary corpus audit CSV.

The text now states that the supplementary coverage CSV contains the full normalized corpus and that background or adjacent records are retained for scope control rather than treated as equally strong evidence for the main taxonomy.

## 3. Identity-state disentanglement table added

Section VII now includes a new table distinguishing:

- persistent identity fields;
- mutable state fields;
- revision evidence;
- validation signals.

This responds to the reviewer suggestion that identity/entity/narrative memory should more clearly center on stable identity versus revisable state. The table explains failure modes under both over-stability and under-stability.

## 4. Benchmark judge reliability strengthened

Section X now includes a judge-reliability table for memory-aware evaluation. It separates memory facts by object existence, identity preservation, scene/layout revisit, causal update, narrative role, and memory budget/decay. For each fact type, it reports preferred evidence windows, useful judge types, reliability risks, and recommended reporting fields.

This directly addresses the concern that VLM-as-judge may identify local attributes but miss temporal causality, entity identity, location correctness, or relation consistency.

## 5. Benchmark audit wording updated

The benchmark-level audit table now uses the field:

```text
Judge / metric / reliability
```

and several entries are revised to mention human validation, prompt/script release, VLM reliability, and generation-side causality concerns.

## 6. Compilation and rendering status

Local artifacts:

```text
TMM_Journal_Track_v0.8.7_preview.pdf
TMM_Journal_Track_v0.8.7.zip
```

The PDF compiles successfully with IEEEtran style and BibTeX. There are no undefined citations or undefined references after repeated LaTeX passes. The rendered preview has 32 pages. Newly affected pages containing the identity-state table, benchmark audit, and judge-reliability table were rendered and visually checked.

## 7. Remaining work before formal submission

1. Fully normalize bibliography metadata and remove all placeholder author fields.
2. Decide which dense pseudo-algorithmic tables should move to appendix or supplementary material.
3. Complete a final terminology pass for Coordinate/Spectral Memory, method capitalization, benchmark names, and publication-status labels.
4. If available, add real or semi-real generated failure examples to an appendix.
