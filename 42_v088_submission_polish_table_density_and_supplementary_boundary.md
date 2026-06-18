# 42 v0.8.8 Submission Polish: Table Density and Supplementary Boundary

> Stage: continue journal-first writing after v0.8.7.  
> Goal: respond to the latest Minor Revision comments by tightening abstract wording, clarifying supplementary audit availability, reducing main-text table density, standardizing coordinate/spectral terminology, and removing visible placeholder-author wording.

## 1. Main update

v0.8.8 is a submission-polish pass rather than a framework redesign. The latest review recommends Minor Revision / Weak Accept after revision and explicitly says not to expand the taxonomy further. This pass therefore focuses on reducing risk before submission.

## 2. Abstract compressed

The abstract is shortened and made less checklist-like. Instead of listing every contribution separately, it now summarizes the inspectability layer as:

```text
an operational boundary, a reproducible coding protocol, paper-level audit records, publication-status labels, and benchmark-level evaluation analysis
```

This keeps the contribution clear while improving narrative flow.

## 3. Main-text density reduced

Route-specific pseudo-algorithmic views were moved out of the main technical route sections into an appendix-style section:

```text
Pseudo-Algorithmic Coding Views
```

The main sections now preserve their mechanism-level discussion, while the pseudo-algorithmic details are retained as coding aids rather than interrupting the main narrative.

## 4. Supplementary full-corpus audit clarified

Section II now explicitly names the supplementary audit artifact:

```text
tables/supplementary_coverage_v086_full_corpus.csv
```

and states that it contains all 108 normalized records using the same coding fields that produce the screening statistics. Background, boundary, and partial records are described as scope-control and bibliography-tracking entries, not as equal-strength evidence for main taxonomy claims.

## 5. Screening table wording softened

The screening table now labels the 32 unresolved entries as:

```text
Supplement-only partial metadata records
```

rather than presenting them as active main-text evidence. The accompanying explanation states that these records are retained for boundary tracking or late-breaking context and are not primary evidence until their metadata is fully normalized.

## 6. Terminology pass

Visible terminology is standardized toward:

```text
Coordinate and Spectral Memory
```

rather than mixed positional/spectral and coordinate/spectral usage. Some internal labels remain for compatibility, but main-text wording and route summaries now prefer coordinate/spectral memory.

## 7. Bibliography placeholder cleanup

Visible BibTeX author placeholders such as "XYZ Authors" were replaced with more conservative team or organization labels when full metadata is still unavailable. This does not complete bibliography normalization, but it removes the most problematic placeholder-author presentation from the compiled references.

## 8. Compilation and rendering status

Local artifacts:

```text
TMM_Journal_Track_v0.8.8_preview.pdf
TMM_Journal_Track_v0.8.8.zip
```

The PDF compiles successfully with IEEEtran style and BibTeX. There are no undefined citations or undefined references after repeated LaTeX passes. The rendered preview has 35 pages. Key pages containing the screening/statistics table, compact cache table, benchmark judge-reliability table, formalism-binding table, and appendix transition were rendered and visually checked.

## 9. Remaining work before formal submission

1. Complete true bibliography normalization: author order, title capitalization, venue/status, arXiv IDs, DOIs, project links, and access dates.
2. Decide whether the appendix-style pseudo-algorithmic section should remain in the submitted manuscript or be moved fully to supplementary material.
3. Continue final terminology and capitalization pass for method names, benchmark names, and publication-status labels.
4. Add real or semi-real generated failure examples to appendix if model outputs become available.
