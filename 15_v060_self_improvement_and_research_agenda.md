# 15 v0.6.0 Self-Improvement and Research Agenda

> Stage: self-review pass after v0.5.9.  
> Goal: continue generating the draft while removing working-note artifacts from the paper body and adding a stronger research agenda.

## 1. Main self-review findings

The v0.5.9 draft made substantial progress, but it still had three issues:

1. It contained a paper-body section that was closer to a figure drawing prompt than a publishable survey section.
2. It ended with “Discussion and Next Steps,” which was useful for the project workflow but not appropriate as a paper conclusion.
3. It lacked a dedicated open-problems section that synthesizes the taxonomy into a future research agenda.

## 2. v0.6.0 changes

The v0.6.0 draft fixes these issues by:

- Replacing the figure-prompt-like section with **Method Landscape and Cross-Route Annotation**.
- Adding a full **Open Problems and Research Agenda** section.
- Adding a research-agenda table that maps open problems to technical routes and evaluation requirements.
- Adding **Scope Limitations and Submission Risks** to explicitly mark breadth, arXiv recency, and AAAI-format risks.
- Adding a real **Conclusion** rather than a project-management note.

## 3. Research agenda added in v0.6.0

The open-problems section now covers:

1. From passive retention to active recall.
2. From frame-indexed memory to entity-state memory.
3. Memory-aware forgetting and conflict resolution.
4. Coordinate-memory co-design.
5. Training-free convenience versus trained memory capability.
6. Memory evaluation beyond consistency scores.

These themes directly follow from the taxonomy and are meant to become the forward-looking contribution of the survey.

## 4. New table added

v0.6.0 adds:

```text
Research agenda suggested by the memory-system view
```

The table aligns open problems with why they matter, promising routes, and evaluation requirements.

## 5. Remaining work toward AAAI-quality submission

Before submission, the next passes should:

- Convert all manual references to normalized BibTeX entries.
- Verify title, author list, arXiv ID, version, and venue status for every A/B-grade paper.
- Draw and insert Figure 1, Figure 3, Figure 4, Figure 5, and Figure 8.
- Replace broad “et al.” references in the bibliography with complete author metadata where possible.
- Migrate to the official AAAI author-kit style once available.
- Audit whether Section 8 should remain independent or be merged with Sections 5 and 7.
- Reduce tables if the official page limit becomes tight, but preserve the core survey apparatus.

## 6. Current output

The current local artifacts are:

```text
Memory_Systems_in_Video_Generation_Models_v0.6.0_working_draft.pdf
Memory_Systems_v0.6.0_latex_source.zip
```

The PDF was compiled and rendered to page images for visual QA.
