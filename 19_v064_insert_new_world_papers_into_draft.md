# 19 v0.6.4 Insert New World-Memory Papers into Draft

> Stage: continue v0.6.3 by moving newly added world-memory papers from notes into the main draft.  
> Goal: make HyDRA/HM-World, GIM-World, WorldKV, and related adjacent world models visible in the actual paper text, tables, and bibliography.

## 1. Main draft changes

v0.6.4 inserts the newly added world-memory papers into the main LaTeX draft rather than only storing them in notes.

### Added / promoted mainline methods

- **WorldKV**: added as a bridge between Token/KV Memory and Spatial/World-State Memory.
- **HyDRA / HM-World**: added as a dynamic hidden-subject memory method.
- **GIM-World**: added as a geometry-aware implicit memory method.

### Supporting / adjacent additions

- **HiMem-WAM** remains a supporting embodied/world-action memory method.
- **V-JEPA 2.1** and **ThinkJEPA** are treated as adjacent background for dense and semantic latent world modeling, not as mainline video-generation memory methods.

## 2. Updated sections and tables

v0.6.4 updates:

- Route-by-lifecycle matrix.
- Method landscape matrix.
- Coverage audit table.
- Section 9 world-state memory discussion.
- Spatial/world-state memory method table.
- Method Landscape and Cross-Route Annotation discussion.
- Manual bibliography.

## 3. New world-memory positioning

The updated text makes three distinctions:

1. **Training-free world memory**: WorldKV preserves persistent world state through inference-time retrieval of evicted KV chunks.
2. **Dynamic hidden-subject memory**: HyDRA/HM-World makes out-of-view subject continuity an explicit benchmarked memory problem.
3. **Geometry-aware implicit memory**: GIM-World compresses history into fixed-size memory tokens trained to encode cross-view geometry.

## 4. Figure 4 update

The LaTeX-rendered method landscape matrix now includes:

- WorldKV.
- HyDRA.
- GIM-World.
- V-JEPA 2/2.1 as background.
- ThinkJEPA as background.

The draft also clarifies that the final visual form should probably be a lifecycle subway map, while the matrix remains as an auditable table or appendix.

## 5. Citation update

v0.6.4 adds manual references for:

- WorldKV.
- Out of Sight but Not Out of Mind / HyDRA / HM-World.
- GIM-World.
- V-JEPA 2.1.
- ThinkJEPA.

These should later be normalized into BibTeX entries.

## 6. Output

Current local artifacts:

```text
Memory_Systems_in_Video_Generation_Models_v0.6.4_working_draft.pdf
Memory_Systems_v0.6.4_latex_source.zip
```

The PDF compiles without undefined citations and was rendered for visual checking.
