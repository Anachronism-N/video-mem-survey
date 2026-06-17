# 18 v0.6.3 New World-Model Papers and Figure 4 Visual Alternatives

> Stage: add newly identified world-memory papers and redesign Figure 4 beyond a pure table.  
> Goal: add detailed notes for new papers and provide several top-conference-style visual alternatives for Figure 4.

## 1. Newly added / promoted papers

This pass adds or promotes four papers into the world-state / world-action memory discussion:

1. **Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models**  
   Working label: HyDRA / Hybrid Memory / HM-World.  
   Recommended status: mainline candidate after metadata verification.  
   Route: Spatial / World-State Memory.  
   Lifecycle focus: Maintain -> Access -> Revise -> Validate.  
   Training regime: memory-oriented training with specialized dataset and memory architecture.

2. **Geometry-Aware Implicit Memory for Video World Models**  
   Working label: GIM-World.  
   Recommended status: mainline candidate after metadata verification.  
   Route: Spatial / World-State Memory.  
   Lifecycle focus: Register -> Maintain -> Access -> Apply.  
   Training regime: memory-oriented training with geometry distillation; lightweight memory module at inference.

3. **WorldKV: Efficient World Memory with World Retrieval and Compression**  
   Recommended status: mainline / strong supporting.  
   Route: Token/KV Memory + Spatial/World-State Memory bridge.  
   Lifecycle focus: Maintain -> Access -> Apply.  
   Training regime: training-free / inference-time memory.

4. **HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation**  
   Recommended status: supporting candidate, because it is embodied/action-oriented rather than standard video generation.  
   Route: World-Action Memory / Embodied extension.  
   Lifecycle focus: Register -> Maintain -> Revise.  
   Training regime: memory-oriented training with hierarchical latent actions and boundary-triggered memory updates.

## 2. Background / adjacent papers to track

The following should be tracked as adjacent or background unless the final paper scope explicitly expands to all world models:

- **V-JEPA 2**: self-supervised video model for understanding, prediction, and planning; important as world-model background, but not a video generation memory method in the same sense as WorldKV or HyDRA.
- **V-JEPA 2.1**: dense-feature extension; useful background for representation-level world memory.
- **ThinkJEPA**: VLM-guided latent world model; useful background for semantic long-horizon guidance.
- **Genie 3 / Project Genie**: strong motivation for persistent interactive worlds, but should remain background unless official technical details expose the memory mechanism.
- **Waymo World Model**: important applied world-model example, but should remain background unless a citable technical report or paper reveals memory architecture.

## 3. Detailed notes file

Detailed notes are stored in:

```text
notes/paper_notes/NEW_WORLD_MODEL_MEMORY_NOTES_v0.6.3.md
```

## 4. Figure 4 redesign

We now keep the LaTeX method landscape table as a reliable, citable, auditable artifact. But Figure 4 can be redesigned as a more visual, top-conference-style schematic.

Recommended strategy:

```text
Figure 4 = visual navigation map
Table 1/appendix = auditable coverage table
Supplement = full 102-paper master table
```

This avoids forcing every paper into one unreadable visual while still preserving full coverage.

## 5. Proposed non-table Figure 4 forms

The new prompt file provides several alternatives:

1. Lifecycle subway map.
2. Memory-flow Sankey diagram.
3. Radial lifecycle wheel.
4. Layered memory-stack map.
5. Route-lifecycle terrain map.
6. Hybrid metro-matrix with mini chips.

The prompts are stored in:

```text
latex/figures/FIGURE4_NON_TABLE_VISUAL_PROMPTS_v0.6.3.md
```

## 6. Recommended choice

For a top-conference survey, the best choice is likely:

```text
Figure 4: Lifecycle subway map
Appendix/Table: full method landscape matrix
```

The subway map is more visually memorable than a table, but still preserves route identity and lifecycle order. It also naturally handles cross-route methods through transfer stations.

## 7. Remaining work

Next pass should:

- Insert HyDRA, GIM-World, WorldKV, and HiMem-WAM into the main LaTeX draft.
- Add BibTeX entries or normalized references for these papers.
- Add their rows to the supplementary coverage table.
- Decide whether V-JEPA 2.1 and ThinkJEPA enter the main paper as adjacent background or remain in supplement.
- Draw one Figure 4 candidate and compare readability against the current LaTeX matrix.
