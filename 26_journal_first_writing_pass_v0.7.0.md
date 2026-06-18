# 26 Journal-First Writing Pass v0.7.0

> Stage: switch the active writing priority back to the journal survey.  
> Goal: postpone benchmark construction and deepen the journal manuscript as a mechanism-level survey.

## 1. Journal-first decision

From this version onward, the project should be treated as a **journal-first survey**. The conference benchmark idea remains useful, but it should be postponed. The current manuscript should not introduce a new benchmark claim unless we have a real protocol, pilot cases, model outputs, validation plan, and release package. For the journal paper, evaluation should first be handled as a **survey and synthesis of existing diagnostic benchmarks**, not as our own new benchmark.

The main writing goal is therefore:

```text
Build a thesis-driven, mechanism-level survey of memory systems in video generation models, with a complete coverage table and rigorous route-level comparisons.
```

## 2. What changes now

The manuscript should now avoid three mistakes:

1. **Do not write as a compressed conference survey.** The journal version does not need to be limited by seven pages.
2. **Do not write as a literature list.** Each section must synthesize mechanisms rather than enumerate papers.
3. **Do not prematurely claim a new benchmark.** Benchmark design may become a later contribution, but for now evaluation remains a survey chapter.

The new priority is:

1. Deepen Section 9: spatial and world-state memory.
2. Deepen Section 5: token/KV/attention memory.
3. Convert Figure 10 into an auditable LaTeX benchmark table.
4. Build one high-quality mechanism comparison table per technical route.
5. Normalize references for all mainline and high-support methods.
6. Keep unresolved papers visible in appendix with verification status.

## 3. Revised journal contribution

The journal paper should make four contributions:

1. **A memory-system taxonomy** for video-generation-model-based systems, covering memory objects, substrates, lifecycle phases, and training regimes.
2. **A mechanism-level survey** of technical routes: token/KV memory, positional/spectral memory, identity/entity/narrative memory, retrieval memory, and world-state memory.
3. **A coverage-audited literature map** that distinguishes mainline, supporting, background, benchmark, unresolved, and duplicate papers.
4. **An evaluation synthesis and research agenda**, summarizing existing benchmarks and explaining why memory requires diagnostics beyond surface video quality.

The paper should not claim a new benchmark yet. It can state that memory-aware benchmarks are necessary and summarize existing ones, while leaving a proposed benchmark protocol for future work or a later companion paper.

## 4. Journal outline v0.7.0

```text
1. Introduction
2. Scope and Related Surveys
3. Memory Failures and Requirements
4. Taxonomy: Memory Object, Substrate, Lifecycle, and Training Regime
5. Implicit Token Memory in Attention and KV Caches
6. Positional and Spectral Memory
7. Identity, Entity, and Narrative Memory
8. Retrieval-Augmented Recall
9. Spatial and World-State Memory
10. Memory Evaluation Beyond Surface Consistency
11. Cross-Route Synthesis and Design Patterns
12. Open Problems and Research Agenda
13. Conclusion

Appendix A. Full paper coverage table
Appendix B. Additional route tables
Appendix C. Additional figures
Appendix D. Bibliographic audit and unresolved entries
```

## 5. Route-writing template

Every technical route should follow the same analytical template:

1. **Problem and memory failure.** What failure motivates this route?
2. **Memory object.** What must persist?
3. **Memory substrate.** Where is it stored?
4. **Lifecycle focus.** Which of Register, Maintain, Access, Apply, Revise, Validate is central?
5. **Training regime.** Is it training-free, fine-tuned, distilled, memory-trained, or benchmark-only?
6. **Representative mechanism groups.** Group methods by mechanism rather than chronology.
7. **Shared limitations.** What still fails?
8. **Evaluation implications.** Which benchmark dimensions test this route?

## 6. Priority rewrite: Section 9 Spatial and World-State Memory

### 9.1 Problem and failure mode

Spatial and world-state memory becomes necessary when video generation moves from local frame continuity to persistent environments. A model may generate visually plausible frames while failing to remember where objects are, whether a door has already been opened, which entities have left the scene, or how an unseen subject should continue to move. These failures cannot be reduced to local temporal flicker. They are failures of **state persistence**: the generated world does not maintain a coherent latent state across viewpoint changes, occlusions, returns, or actions.

This route therefore asks a stronger question than ordinary video consistency: can the generator preserve and revise a world state that remains valid when evidence is temporarily unobserved?

### 9.2 Memory objects

World-state memory involves several distinct objects:

- **Static scene layout:** room structure, street layout, furniture placement, map-like geometry.
- **Spatial anchors:** camera pose, viewpoint, object positions, and revisit coordinates.
- **Hidden object state:** objects that leave view, become occluded, or are expected to reappear.
- **Dynamic subject state:** identity, trajectory, and motion of actors that leave and later re-enter.
- **Causal environment state:** changes caused by actions, such as opened doors, moved objects, or switched lights.
- **Action-conditioned state:** task or control state in embodied and driving world models.

These objects differ in their update requirements. Static scene layout mostly needs preservation and retrieval; dynamic subjects require hidden-state evolution; causal state requires revision after actions; action-conditioned state requires coupling memory with policy or control.

### 9.3 Memory substrates

Existing methods instantiate world-state memory through different substrates:

- **Memory frames and pose metadata** for revisitable scenes.
- **Spatial memory maps** for long-term layout and scene consistency.
- **Latent spatial caches** that avoid expensive explicit 3D reconstruction.
- **Compressed historical latent tokens** in interactive world models.
- **Evicted KV chunks** reused as training-free world memory.
- **Hybrid memory tokens** for static backgrounds and dynamic subjects.
- **Geometry-aware implicit memory tokens** queried by camera or viewpoint.
- **Persistent global state variables** for out-of-sight dynamics.

The key design question is not simply whether memory is explicit or implicit, but whether the substrate supports the required query: pose query, entity query, action query, camera query, or state-transition query.

### 9.4 Mechanism groups

#### 9.4.1 Static scene revisit and spatial layout memory

Methods in this group focus on returning to a previously observed environment. WorldMem and SpMem are representative because they treat environment consistency as a memory problem rather than as post-hoc frame smoothing. The memory object is the scene layout; the substrate is a pose-aware or spatially organized memory; the lifecycle emphasis is Maintain and Access. The central limitation is that static layout memory does not automatically solve dynamic hidden-state evolution.

#### 9.4.2 Latent spatial memory

Latent spatial memory stores spatial information in the generative latent space rather than through explicit RGB maps or point clouds. This design can reduce conversion cost and preserve information relevant to diffusion generation. Mirage-like methods belong here. The advantage is efficiency and native compatibility with video diffusion; the risk is that the memory may be difficult to interpret and may not expose explicit state variables for evaluation.

#### 9.4.3 Training-free KV world memory

WorldKV shows that world-state persistence can sometimes be treated as an inference-time cache management problem. Instead of retraining the generator, evicted KV chunks are stored, retrieved by camera/action correspondence, compressed, and reinserted into the attention window. This makes WorldKV a bridge between token/KV memory and world-state memory. Its strength is deployability; its limitation is that it can retrieve observed evidence but cannot necessarily infer how unobserved state evolves.

#### 9.4.4 Hidden object and dynamic subject memory

HyDRA / HM-World shifts the route from static scene revisit to dynamic hidden-subject memory. Here the memory object is not just the background but the state of subjects that exit and later re-enter. This requires a distinction between archival background memory and dynamic subject tracking. The lifecycle emphasis shifts toward Revise: the system must update or extrapolate subject state even when direct visual evidence is absent.

#### 9.4.5 Geometry-aware implicit memory

GIM-World represents a geometry-aware version of implicit memory. Its memory tokens are not merely compressed visual history; they are trained to preserve cross-view structure and become queryable by camera state. This design addresses an important weakness of appearance-only memory: a model can remember how a scene looked without preserving the geometric relations needed for consistent novel views.

#### 9.4.6 Action-conditioned and embodied world memory

Embodied and driving world models extend world-state memory from passive scene persistence to action-conditioned state. UniDriveDreamer, DriveWAM, HiMem-WAM, and related driving/world-action systems are important boundary cases. They should not dominate the video-generation taxonomy, but they reveal the next requirement: memory must support actions, subgoals, causal changes, and closed-loop control.

### 9.5 Training regime

World-state memory is more often trained than reference or cache memory. This is not accidental. Preserving visible evidence can sometimes be achieved through reference features, cache reuse, or retrieval. In contrast, hidden-state evolution requires the model to infer state changes without direct observation. That ability usually needs memory-oriented data, event-aware training, geometry supervision, or interactive rollout training.

A useful distinction is:

- **Training-free world memory:** reuse observed evidence more efficiently, as in WorldKV.
- **Memory-oriented world training:** teach state persistence and revision, as in HyDRA, GIM-World, LiveWorld, and ReMind.
- **Embodied/action memory:** couple state memory with action or task dynamics, as in DriveWAM and HiMem-WAM.

### 9.6 Shared limitations

World-state memory methods remain limited in four ways:

1. **Hidden-state hallucination:** models may invent unseen state rather than maintain it.
2. **Over-retention:** stale spatial evidence may conflict with updated causal state.
3. **Viewpoint mismatch:** memory retrieved from a similar camera pose may still be geometrically inconsistent.
4. **Evaluation fragility:** visually plausible returns may hide failures of object permanence or causal state.

These limitations imply that world-state memory should be evaluated through revisit, occlusion, causal update, and action-conditioned tests rather than only visual quality.

### 9.7 Section summary

Spatial and world-state memory marks a shift from remembering appearances to remembering states. Static layout memory, latent spatial caches, training-free KV world memory, dynamic subject memory, geometry-aware implicit memory, and embodied action memory all address different parts of this shift. The route is therefore the clearest evidence that long-horizon video generation is not merely a long-context problem: a generator must maintain and revise an internal model of what continues to exist, where it is, and how it changes.

## 7. Revised treatment of evaluation

For the current journal draft, evaluation should be a **survey chapter**, not an original benchmark proposal. It should cover:

- why generic video metrics are insufficient;
- how MIND, MBench, WorldScore, iWorld-Bench, EntityBench, and Echo-Memory diagnose memory;
- what dimensions remain under-evaluated;
- how future benchmarks should be designed.

Any new benchmark idea should be moved to Future Work or a later companion paper.

## 8. Immediate next writing tasks

1. Insert the Section 9 rewrite into the journal source.
2. Convert Figure 10 into a LaTeX benchmark table.
3. Deepen Section 5 with the same mechanism-based template.
4. Build one route comparison table per section.
5. Move benchmark-proposal language out of the current journal main text.
6. Keep the conference benchmark track as a separate future branch, not the current writing priority.
