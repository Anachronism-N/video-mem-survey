# New World-Model Memory Notes v0.6.3

> Purpose: detailed notes for newly added or promoted world-memory papers.  
> Status: metadata checked from public web/arXiv records, but final BibTeX normalization is still required before submission.

## 1. HyDRA / Hybrid Memory / HM-World

### Paper

**Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models**

### Core problem

Existing video world models often remember environments as relatively static canvases. This is insufficient when dynamic subjects leave the field of view and later re-enter. The failure mode is not merely scene inconsistency, but hidden-subject state loss: subjects may freeze, distort, disappear, or reappear with inconsistent motion.

### Memory object

- Static background memory.
- Dynamic subject identity.
- Dynamic subject motion.
- Exit-entry events.
- Hidden-state continuity.

### Memory substrate

- Hybrid memory tokens.
- Spatiotemporal relevance-driven retrieval.
- Dataset-level memory supervision through HM-World.

### Lifecycle focus

- **Register:** encode background and subject states before occlusion or out-of-view intervals.
- **Maintain:** compress and maintain static and dynamic memories differently.
- **Access:** retrieve subject-relevant motion cues when re-entry or future generation requires them.
- **Revise:** continue dynamic subject state rather than freezing it while hidden.
- **Validate:** HM-World provides exit-entry events for evaluating hybrid coherence.

### Training regime

Memory-oriented training with specialized dataset and architecture.

### Placement in survey

Mainline candidate in Section 9: From Visual Continuity to World-State Persistence.

### Why it matters

This paper is important because it directly targets a memory failure that ordinary identity consistency or scene consistency metrics cannot capture: dynamic hidden subjects must continue to evolve when they are not visible.

### Suggested survey phrasing

HyDRA extends the world-state memory discussion from static scene persistence to hybrid background-subject memory. Its key contribution is to decouple static environmental memory from dynamic subject tracking, making out-of-view subject continuity an explicit memory problem rather than a side effect of temporal consistency.

## 2. GIM-World

### Paper

**Geometry-Aware Implicit Memory for Video World Models**

### Core problem

Long-horizon video world models need to remember scene geometry after observations leave the context window. Explicit memory approaches can be redundant or retrieval-sensitive, while implicit memory approaches may lack geometric constraints.

### Memory object

- Cross-view scene geometry.
- Long-horizon visual state.
- Camera-conditioned spatial information.
- Compact history state.

### Memory substrate

- Fixed-size memory tokens.
- Lightweight transformer encoder over variable-length history.
- Camera-queryable geometry head.
- Information-guided pruning.

### Lifecycle focus

- **Register:** compress variable-length history into memory tokens.
- **Maintain:** keep a fixed-size implicit memory under long-horizon rollout.
- **Access:** query memory with camera/view information.
- **Apply:** condition future generation on geometry-aware memory.
- **Validate:** evaluate long-horizon geometric and visual consistency.

### Training regime

Memory-oriented training with geometry distillation. The geometry teacher is discarded at inference, leaving a lightweight memory module.

### Placement in survey

Mainline candidate in Section 9. It should also be cross-tagged with training regime and implicit-memory substrate.

### Why it matters

GIM-World is important because it makes geometry a first-class constraint on memory. It bridges implicit memory tokens and spatial/world-state persistence.

### Suggested survey phrasing

GIM-World illustrates a shift from appearance-centric memory to geometry-aware memory: rather than merely storing past frames or latents, the memory module is trained to encode cross-view structure that remains queryable under future camera motion.

## 3. WorldKV

### Paper

**WorldKV: Efficient World Memory with World Retrieval and Compression**

### Core problem

Action-conditioned autoregressive video diffusion models need persistent scene memory for revisits, but full KV-cache attention grows linearly with rollout length. Sliding-window inference is efficient but forgets previously seen viewpoints.

### Memory object

- Evicted historical KV chunks.
- Viewpoint-relevant scene memory.
- Camera/action correspondence.

### Memory substrate

- Evicted KV-cache chunks in GPU/CPU memory.
- World Retrieval.
- World Compression through token pruning.

### Lifecycle focus

- **Maintain:** store evicted KV chunks under bounded memory.
- **Access:** retrieve scene-relevant chunks using camera/action correspondence.
- **Apply:** reinsert retrieved chunks into the native attention window.
- **Validate:** compare revisit consistency and throughput against full-KV and sliding-window baselines.

### Training regime

Training-free / inference-time memory.

### Placement in survey

Bridge method between Section 5 Token/KV/Attention Memory and Section 9 Spatial/World-State Memory.

### Why it matters

WorldKV is a key example showing that world-state persistence does not always require retraining. It also demonstrates the importance of deployment regime as a taxonomy axis.

### Suggested survey phrasing

WorldKV reframes long-term world consistency as selective access to evicted KV chunks. Unlike trained world-memory modules, it preserves the frozen generator and instead modifies the inference-time cache policy, making it a strong example of training-free world memory.

## 4. HiMem-WAM

### Paper

**HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation**

### Core problem

World Action Models need task-relevant memory in long-horizon manipulation. Flat latent action models may fail to preserve skill-level state and task progress.

### Memory object

- Motion-centric latent actions.
- High-level skill latents.
- Task state at skill boundaries.
- Long-horizon manipulation context.

### Memory substrate

- Hierarchical latent action framework.
- Boundary-aware memory gate.
- Compact task states.

### Lifecycle focus

- **Register:** write task state at predicted skill transitions.
- **Maintain:** preserve compact state across long-horizon manipulation.
- **Revise:** update memory when skills or subgoals change.
- **Apply:** support causal inference without generating future video at test time.

### Training regime

Memory-oriented training with hierarchical latent actions and boundary-triggered memory updates.

### Placement in survey

Supporting candidate in embodied/world-action extension. It should not dominate the main video-generation discussion unless the survey scope expands explicitly toward robotic world-action models.

### Why it matters

HiMem-WAM extends the memory-system lens from passive video rollout to action-conditioned, task-directed memory. It is especially useful for the open problem of event-boundary memory updates.

## 5. Adjacent background notes

### V-JEPA 2 and V-JEPA 2.1

These are important world-model background papers for understanding, prediction, planning, and dense features. They should be cited as adjacent world-model context rather than mainline video-generation memory methods unless the final paper broadens to include non-generative predictive world models.

### ThinkJEPA

Useful as an adjacent example of semantic long-horizon guidance in latent world models. It may inform the open problem of combining dense dynamics memory with semantic memory.

### Genie 3 / Project Genie / Waymo World Model

These are important public examples of persistent interactive worlds and applied driving simulation. However, unless official technical reports expose the memory architecture, they should remain background or motivation rather than method mainline.

## 6. Recommended additions to main draft

- Add HyDRA and GIM-World to Section 9.
- Add WorldKV as a bridge between Sections 5 and 9.
- Add HiMem-WAM to Section 11 as an embodied/world-action extension.
- Add V-JEPA 2/2.1 and ThinkJEPA to background or open problems.
- Keep Genie 3 / Waymo World Model as motivation and boundary examples.
