# 24 Journal Submission Solution v0.6.8

> Stage: journal-oriented strategy after deciding that the long paper should be the main target.  
> Goal: avoid both conference-length undercoverage and journal-style literature listing by converting the manuscript into a thesis-driven, evidence-backed survey article.

## 1. Core problem

The project faces two opposite risks:

1. **Conference risk:** 7--8 pages are not enough to cover the full memory-system landscape, especially after adding token/KV memory, positional/spectral memory, identity/entity/narrative memory, retrieval memory, world-state memory, evaluation, and 100+ papers.
2. **Journal risk:** a long paper that only lists methods will be rejected as an annotated bibliography rather than accepted as a high-level survey contribution.

Therefore, the solution is not simply to write longer. The long version must have a stronger intellectual structure.

## 2. Recommended target strategy

The main target should be a **journal/full-length survey**.

Recommended venue tiers:

1. **Primary target: ACM Computing Surveys (CSUR).**
   Best fit if the article becomes a comprehensive, taxonomy-driven survey with full coverage and strong tutorial value.
2. **Domain-specific alternatives: IEEE TMM or TCSVT.**
   Better fit if the article emphasizes video generation, multimedia systems, streaming/cache budget, benchmarks, and deployment.
3. **High-risk vision venues: IJCV / TPAMI.**
   Possible only if the paper becomes strongly vision-centric and analytically deep, not merely broad.

The AAAI version can remain a condensed concept paper or backup, but the long journal version should be the primary manuscript.

## 3. How to avoid literature-listing

The journal paper should not use the structure:

```text
Method A does X. Method B does Y. Method C does Z.
```

Instead, each section should use a mechanism-comparison structure:

```text
Problem -> Memory object -> Substrate -> Lifecycle -> Training regime -> Representative mechanisms -> Failure modes -> Evaluation implications
```

This eight-part template converts method listing into analytical synthesis.

## 4. The manuscript's claim should be stronger

The paper should be framed as a **conceptual and diagnostic survey**, not just a comprehensive survey.

Main thesis:

```text
Long-horizon, multi-shot, identity-consistent, and world-consistent video generation is not merely a long-context problem; it is a structured memory problem.
```

Main contribution:

```text
The survey introduces a unified memory-system lens that connects memory objects, memory substrates, memory lifecycle operations, training regimes, technical routes, and diagnostic evaluation dimensions.
```

This gives the article an argument rather than a list.

## 5. Journal article architecture

Recommended long-version structure:

```text
1. Introduction
2. Scope and Related Surveys
3. Memory Failures and Requirements
4. Taxonomy: Object, Substrate, Lifecycle, and Training Regime
5. Token/KV/Attention Memory
6. Positional and Spectral Memory
7. Identity, Entity, and Narrative Memory
8. Retrieval-Augmented Recall
9. Spatial and World-State Memory
10. Memory Evaluation Beyond Surface Consistency
11. Cross-Route Synthesis and Design Patterns
12. Open Problems and Research Agenda
13. Conclusion
Appendix A. Full coverage table
Appendix B. Additional figures
Appendix C. Bibliographic audit
```

## 6. Section-level transformation rule

Each method family should be summarized at the mechanism level, not the paper level.

### Example: Token/KV memory

Group papers into:

- retention and sink/anchor memory,
- compression and quantization,
- sparse persistent blocks,
- head-aware routing,
- retrieval from historical KV,
- system memory budget.

Then place methods under these mechanism groups.

### Example: World-state memory

Group papers into:

- static scene revisit,
- spatial layout memory,
- hidden object/subject state,
- geometry-aware implicit memory,
- training-free KV world memory,
- action-conditioned world memory,
- embodied/driving extensions.

Then compare methods by what state they preserve, where it is stored, and how it is revised.

## 7. Required evidence apparatus

The journal version should contain three levels of evidence:

1. **Narrative synthesis in main text.**
   Explains mechanisms and trade-offs.
2. **Compact comparison tables in each section.**
   Shows method, memory object, substrate, lifecycle, training regime, limitation, and evaluation.
3. **Full supplementary coverage table.**
   Proves coverage of all papers, including background and unresolved entries.

This prevents the paper from being accused of cherry-picking.

## 8. Figure strategy for journal version

The journal version can use more figures, but not as decoration.

Recommended main figures:

- F1: overall memory systems map.
- F2: memory failures and requirements.
- F3: three-layer taxonomy.
- F4: lifecycle subway map.
- F6: token/KV memory mechanisms.
- F7: identity/entity/narrative memory.
- F8: world-state persistence hierarchy.
- F10 converted into a LaTeX benchmark table.

Optional new category-level figures:

- Training-free vs trained memory spectrum.
- World-state memory design patterns.

Do not directly copy method figures from papers unless permissions are clear. Redraw category-level synthesis diagrams instead.

## 9. How to meet CCF-A / SCI-Q1 evaluation needs

For evaluation-driven submission, the safest strategy is:

1. Target a recognized high-level survey journal first if time allows.
2. Keep AAAI as a compressed concept-paper track, but do not sacrifice the journal paper.
3. Make the journal version rigorous enough for Q1/CCF-A-style evaluation by adding:
   - systematic coverage protocol,
   - full paper table,
   - precise taxonomy,
   - mechanism-level comparisons,
   - evaluation critique,
   - future research agenda.

## 10. Immediate next writing tasks

1. Deepen Section 9 first, because world-state memory is the strongest differentiator.
2. Then deepen Section 5, because token/KV memory provides the systems mechanism backbone.
3. Convert Figure 10 to a LaTeX benchmark table.
4. Create one full route table per section.
5. Normalize all BibTeX entries for mainline and high-support papers.
6. Move unresolved papers into appendix with verification status rather than hiding them.

## 11. Decision

The main manuscript should now be treated as a **journal-first survey**. The AAAI version can continue as a high-level compressed argument, but the project should not be constrained by AAAI page limits during content development.
