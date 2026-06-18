# 28 TMM Template and Route-Figure Plan v0.7.2

> Stage: continue journal-first optimization.  
> Goal: decide whether each technical route needs a separate figure, and start a TMM-oriented LaTeX track.

## 1. Decision: use TMM/IEEE-style template as the journal working target

The journal track should now use an IEEE Transactions-style LaTeX skeleton as the main working format. Since IEEE Transactions on Multimedia is an IEEE Transactions journal, the practical working template should be based on:

```tex
\documentclass[journal]{IEEEtran}
```

The goal is not to claim the paper is already submission-ready for TMM, but to make the journal manuscript closer to the expected format, citation style, float behavior, and table/figure constraints of an IEEE Transactions journal.

## 2. Why TMM is a reasonable working template

TMM fits the project if the manuscript is framed around multimedia generation systems, video generation, memory mechanisms, reproducibility, benchmarks, and evaluation. The paper should avoid a purely philosophical world-model framing and emphasize video generation technology, multimedia systems, memory/compression, reference conditioning, retrieval, and evaluation.

## 3. Do we need a separate figure for every technical route?

No. A figure for every route would make the paper too figure-heavy and repetitive. The journal paper should use a layered figure strategy:

### Core navigation figures

These figures explain the whole paper and should remain in the main manuscript:

1. **F1: Overall memory systems map.**
2. **F3: Three-layer taxonomy.**
3. **F4: Lifecycle subway map.**
4. **F5 or Table 10: Evaluation beyond surface consistency.**

### Route synthesis figures

Only routes with rich internal mechanisms and strong visual commonality should get a dedicated synthesis figure.

Recommended route figures:

1. **F6: Token/KV/Attention Memory.** Keep. It already summarizes the unified cache-memory route.
2. **F7: Identity/Entity/Narrative Memory.** Keep. It already summarizes the entity-memory loop.
3. **F8: World-State Persistence.** Keep, but later consider replacing or supplementing it with a more method-pattern-oriented world-state memory design figure.
4. **New optional Retrieval-Augmented Memory figure.** Recommended if Section 8 becomes a major section.
5. **New optional World-State Memory Design Patterns figure.** Strongly recommended for the journal version.

Not every route needs a figure:

- Positional/Spectral Memory is better handled by a table plus a small inset or conceptual panel, unless we have space for a compact RoPE/frequency figure.
- Evaluation should mainly use a LaTeX table, not a large image, unless the journal version keeps F5 as a conceptual motivation figure.

## 4. Recommended new route figures

### 4.1 Retrieval-Augmented Memory unified method figure

This figure would unify LongLive-RAG, OmniMem, Echo-Forcing scene recall, EM-Vid, IAMFlow, Context-as-Memory, and DecMem-like methods.

Suggested structure:

```text
Current generation query
        |
        v
Memory query builder
        |
        +--> latent history bank
        +--> KV cache archive
        +--> scene recall frames
        +--> entity-indexed memory
        +--> external visual corpus
        |
        v
Retrieve -> filter conflicts -> rank -> inject/condition -> generate -> update memory
```

Lifecycle mapping:

```text
Register: write history into memory banks
Maintain: index/compress/deduplicate memory
Access: retrieve by query, entity, camera, scene, or prompt
Apply: inject retrieved evidence into generation
Revise: update bank with new evidence or remove stale memory
Validate: test under-recall, over-recall, and wrong-recall
```

### 4.2 World-State Memory Design Patterns figure

This is the most important optional new figure.

Suggested structure:

```text
Observation/history -> state encoder -> compact memory state
                         |              |
                         |              +--> spatial map / latent cache / KV archive / global state
                         v
Query: camera / action / entity / scene revisit / hidden-state request
                         v
State retrieval and update
                         v
Generation conditioning
                         v
Diagnostic evaluation: revisit, occlusion, causal update, closed-loop action
```

This figure should place methods into modules:

- WorldMem / SpMem: spatial layout and scene revisit.
- Mirage / RELIC: latent spatial or interactive context memory.
- WorldKV: training-free KV world memory.
- HyDRA: hybrid background-subject memory.
- GIM-World: geometry-aware implicit memory.
- LiveWorld / ReMind: hidden-state evolution and memory elicitation.
- HiMem-WAM / DriveWAM: embodied and action-conditioned extensions.

## 5. Figure budget for journal track

Recommended main-text figure set for the journal version:

1. F1 Overview.
2. F2 Failure taxonomy or merged with introduction.
3. F3 Three-layer taxonomy.
4. F4 Lifecycle subway map.
5. F6 Token/KV route figure.
6. F7 Identity/entity route figure.
7. Retrieval-Augmented Memory route figure.
8. World-State Memory Design Patterns figure.
9. F5 or a compact evaluation conceptual figure.

Move F9 timeline and radial F4 to supplement unless needed.

## 6. Required tables for journal track

The journal version should use tables as the primary audit layer:

- Table 1: Adjacent surveys and how this paper differs.
- Table 2: Memory objects and substrates.
- Table 3: Lifecycle and training regimes.
- Table 4: Token/KV/Attention memory mechanism table.
- Table 5: Positional/Spectral memory table.
- Table 6: Identity/Entity/Narrative memory table.
- Table 7: Retrieval-Augmented memory table.
- Table 8: Spatial/World-State memory table.
- Table 9: Memory evaluation benchmark table.
- Appendix Table A: full coverage table.

## 7. TMM-oriented source package

A local TMM-oriented LaTeX skeleton is generated as:

```text
TMM_Journal_Track_v0.7.2.zip
```

The package contains:

```text
main.tex
sections/
tables/
figures/README_FIGURE_PLAN.md
references.bib
README.md
```

It is a working skeleton based on IEEEtran journal mode. It should later be populated with the journal-first long draft content and normalized BibTeX entries.

## 8. Immediate next writing actions

1. Move the journal-first Section 5 and Section 9 rewrites into the TMM skeleton.
2. Create the Retrieval-Augmented Memory route figure prompt and table.
3. Create the World-State Memory Design Patterns figure prompt and table.
4. Convert Figure 10 into a LaTeX benchmark table.
5. Continue deepening Section 7: Identity/Entity/Narrative Memory.
