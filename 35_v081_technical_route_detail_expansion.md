# 35 v0.8.1 Technical Route Detail Expansion

> Stage: journal-first writing after v0.8.0 citation integration.
> Goal: expand technical-route and representative-method descriptions.

## Main update

v0.8.1 expands the TMM journal draft with more method-level technical discussion while keeping the article organized by mechanisms rather than as an annotated bibliography.

## Expanded areas

- Section 2 now explains the difference from long-video, video diffusion, controllable-generation, and world-model surveys.
- Section 5 expands cache-centric memory: streaming/chunk caches, rollout-aware exposure, role-separated cache memory, evolving memory tokens, sparse persistent blocks, archived-KV access, and system-level budgets.
- Section 7 expands identity/entity/narrative memory: reference anchors, identity-frequency bridges, heterogeneous identity references, dynamic slots, explicit entity tables, entity-aware memory stores, and verification loops.
- Section 8 expands retrieval-augmented recall: scene recall frames, latent banks, KV archives, entity-indexed retrieval, external memory sources, and under/over/wrong/stale recall failures.
- Section 9 expands world-state memory: static scene revisit, latent spatial context, training-free KV world memory, hidden dynamic subject memory, geometry-aware memory, out-of-sight state evolution, and action-conditioned/embodied memory.

## Compilation status

Local artifacts:

```text
TMM_Journal_Track_v0.8.1_preview.pdf
TMM_Journal_Track_v0.8.1.zip
```

The PDF compiles successfully using the existing BibTeX database. The final LaTeX pass has no undefined citations or undefined references. The rendered preview has 16 pages. One minor overfull warning remains from a long equation but does not visibly damage the PDF.

## Remaining work

1. Add appendix-level paper-by-paper audit tables for all main routes.
2. Continue expanding Section 6 and Section 10 with more method-specific comparisons.
3. Normalize BibTeX metadata for all mainline and high-support methods.
4. Add the optional World-State Memory Design Patterns figure if available.
5. Continue converting dense method lists into mechanism-centered paragraphs and tables.
