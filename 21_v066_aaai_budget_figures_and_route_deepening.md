# 21 v0.6.6 AAAI Budget, Figure Policy, and Technical-Route Deepening Plan

> Stage: response to v0.6.5 review.  
> Goal: evaluate AAAI page constraints, decide how to use figures, and define the next deepening pass needed to make the survey technically strong enough.

## 1. AAAI page-budget check

The current v0.6.5 PDF is around 20 pages in the working two-column format after inserting F1--F10. This is not compatible with the AAAI main technical-track limit if the next cycle follows the AAAI-26 rule.

AAAI-26 states that submissions may contain **up to 7 pages of technical content plus additional pages solely for references**. It also allows supplementary material, but reviewers are not required to review it; material critical to evaluation should be in the main body.

Therefore, the current draft should be treated as a long internal working draft, not a submission-ready draft.

## 2. Recommended AAAI submission packaging

The paper should be repackaged into three artifacts:

1. **Main paper: 7 technical pages + references.**
   - Only the core thesis, taxonomy, compact method landscape, and the most important examples remain.
2. **Supplementary material.**
   - Full 100+ paper coverage table.
   - Additional method-family tables.
   - Alternative Figure 4, extra figures, and detailed route notes.
3. **Internal long draft.**
   - The current 20-page version remains as the source of material for writing, but is not the submission target.

## 3. Figure policy

The current figures are useful, but too many for a 7-page main paper.

### Main-paper figures to keep

- **Figure 1**: Memory systems overview. Keep; it sells the survey scope.
- **Figure 3**: Three-layer taxonomy. Keep or merge with Figure 1 if space is tight.
- **Figure 4**: Lifecycle subway map. Keep; this should be the main method landscape figure.
- **Figure 5 or Figure 10**: Keep one evaluation figure/table, not both.

### Figures to move to supplement unless space allows

- Figure 2: Memory failures and requirements.
- Figure 6: Token/KV mechanism schematic.
- Figure 7: Identity/entity/narrative schematic.
- Figure 8: World-state persistence staircase.
- Figure 9: Timeline.
- Alternative Figure 4 radial view.

### Figure 10 policy

Figure 10 should probably be converted to a LaTeX table. As an image, it is visually clear in the working draft but may become too small in AAAI format. A LaTeX table is easier to cite, compress, and edit.

## 4. Should we cite figures from other papers?

Directly reproducing paper figures in the main submission is not recommended unless license/permission is explicitly clear. The safer and stronger survey strategy is:

- Do not copy original method figures.
- Study them to identify common modules.
- Redraw category-level synthesis diagrams.
- Cite the papers in captions and surrounding text.

This is especially important because the survey should not look like a collage of existing method figures. It should synthesize common design patterns.

## 5. Category-level synthesis figures to consider

Beyond F1--F10, we should not add many new large figures. However, we can consider small, category-level synthesis figures if they compress multiple papers.

### Candidate A: Training-free vs trained memory spectrum

Purpose: show that memory mechanisms differ by how the memory behavior is obtained.

- Training-free: RIFLEx, LoL, Sparse Forcing, WorldKV.
- Adapter/fine-tuned: identity adapters, some ID-preserving systems.
- Distillation/self-forcing: Self-Forcing, LongLive-like training.
- Memory-oriented training: HyDRA, GIM-World, LiveWorld, ReMind.
- Benchmark-only: MIND, MBench, WorldScore.

Placement: Section 4 or supplement.

### Candidate B: World-state memory design patterns

Purpose: summarize common modules across WorldMem, SpMem, RELIC, WorldKV, HyDRA, GIM-World, LiveWorld, ReMind.

Common modules:

- history encoder,
- compact memory state,
- query mechanism,
- update/revision rule,
- hidden-state evolution,
- geometry/action conditioning,
- diagnostic benchmark.

Placement: Section 9 or supplement.

### Candidate C: Entity-memory loop

F7 already covers most of this. If kept, do not add another large figure.

### Candidate D: Token/KV memory design patterns

F6 already covers most of this. Use F6 in supplement if space is tight.

## 6. Technical-route deepening tasks

The current technical-route discussion still needs to become more precise. Each route should be rewritten with the same template:

1. **Problem and memory failure.**
2. **Memory object.** What information must persist?
3. **Memory substrate.** Where is it stored?
4. **Lifecycle emphasis.** Which of Register/Maintain/Access/Apply/Revise/Validate is central?
5. **Training regime.** Training-free, adapter, self-forcing, memory-oriented training, or benchmark-only.
6. **Representative methods.** Grouped by mechanism, not just chronology.
7. **Shared limitations.** Failure modes and open problems.
8. **Evaluation implications.** Which benchmark dimensions test the route?

## 7. Route-specific deepening checklist

### Token/KV/Attention Memory

Must distinguish:

- cache retention,
- cache compression,
- sparse persistent blocks,
- head-aware cache routing,
- retrieval from historical KV,
- quantized/system memory.

### Positional/Spectral Memory

Must distinguish:

- coordinate extrapolation,
- RoPE phase conflict,
- attention sink collapse,
- frequency/spectral consistency,
- identity-frequency bridges.

### Identity/Entity/Narrative Memory

Must distinguish:

- reference identity anchors,
- learned ID embeddings,
- entity tables,
- object slots,
- attribute-state tracking,
- narrative-role memory,
- reconstruction/verification loops.

### Retrieval-Augmented Memory

Must distinguish:

- latent retrieval,
- KV retrieval,
- scene recall frames,
- entity-conditioned retrieval,
- external corpus retrieval,
- under-recall / over-recall / wrong-recall failure.

### Spatial/World-State Memory

Must distinguish:

- static scene revisit,
- spatial layout memory,
- hidden object/subject state,
- geometry-aware memory,
- action-conditioned state,
- embodied/driving world memory,
- training-free vs trained world memory.

### Evaluation

Must distinguish:

- surface video quality,
- identity/entity consistency,
- environment consistency,
- causal consistency,
- scene revisit,
- out-of-sight dynamics,
- closed-loop action control,
- memory budget.

## 8. Immediate next pass

The next concrete version should be v0.6.7 and should do the following:

1. Reconcile the 108-row supplementary table against the 102-note corpus.
2. Mark duplicates, unresolved records, and newly added papers explicitly.
3. Convert Figure 10 into a LaTeX table.
4. Produce a 7-page AAAI-style compression plan.
5. Rewrite one technical section deeply, preferably Section 5 or Section 9, as a model for the remaining routes.
6. Decide the main/supplement figure split.

## 9. Current judgment

The current draft has enough raw material for a survey, but not yet enough compression, route depth, and citation normalization for AAAI submission. The next major milestone is not adding more text; it is turning the long draft into a selective, technically dense, well-supported 7-page main submission plus a comprehensive supplement.
