# 10 Detailed Outline and Lifecycle Analysis v0.5.3

> Stage: detailed structure and grading refinement.  
> Goal: explain how lifecycle analysis is used inside each technical route, refine section naming, and provide a more detailed paper outline before drafting.

## 1. Key decision: hybrid route + lifecycle lens

The survey should not be organized purely by lifecycle. A pure lifecycle structure is too abstract and hides technical routes. The final structure should use:

```text
Technical route = chapter-level organization
Lifecycle = within-route analytical lens
Object/substrate = early taxonomy coordinates
```

In other words:

- Sections after the taxonomy are organized by technical route.
- Each technical-route section contains a short lifecycle analysis.
- Lifecycle is not a flat list repeated mechanically; it is used to explain what makes the route a memory mechanism.

## 2. How to analyze lifecycle inside each technical route

Each technical-route section should follow a stable internal template:

```text
1. Problem and memory object
2. Memory substrate used by this route
3. Lifecycle operations emphasized by this route
4. Representative methods
5. Strengths and failure modes
6. Relation to other routes
```

This avoids both extremes:

- It avoids pure domain survey writing such as “Here are ID methods, here are KV methods.”
- It avoids pure lifecycle writing such as “Here is write, here is retrieve,” which hides the technology landscape.

## 3. Section 4.3 should define lifecycle in detail

Because later sections rely on lifecycle vocabulary, Section 4.3 should be more detailed than 4.1 and 4.2. It should define the stages clearly:

### Write

How information enters memory. Examples: first frame, reference image, prompt-extracted entity, historical KV, memory frame, latent patch, pose/state metadata.

### Retain

How information is kept across time. Examples: cache retention, anchor frames, sink tokens, memory tokens, persistent blocks, entity slots, global state.

### Compress

How memory is reduced to fit computation and VRAM budgets. Examples: compressed KV, memory tokens, frame packing, latent patch bank, quantized KV cache, sparse blocks.

### Route

How memory is assigned to layers, heads, entities, or spatial locations. Examples: head-aware cache, identity routers, object slots, entity-indexed patch banks, layer-aware ID injection.

### Retrieve

How old information is recalled. Examples: scene recall frames, sparse KV retrieval, retrieval-augmented latent memory, entity lookup, pose-conditioned spatial recall.

### Inject / Use

How retrieved memory affects generation. Examples: attention injection, reference feature injection, soft prompts, conditioning tokens, cross-attention, cache reuse, state-conditioned rollout.

### Update

How memory changes after new frames, prompts, actions, or observations. Examples: entity attribute update, dynamic state update, reconstruction feedback, closed-loop memory rewriting.

### Forget

How obsolete or harmful memory is removed or weakened. Examples: difference-aware decay, sink-collapse mitigation, cache eviction, prompt-change flushing, conflict-aware memory rewriting.

### Evaluate

How to test whether memory is genuine. Examples: identity consistency, entity consistency, environment consistency, causal consistency, scene revisit, out-of-sight dynamics, closed-loop action control, memory budget.

Section 4.3 can include a table mapping lifecycle stages to memory substrates and representative papers.

## 4. Are the technical-route sections overlapping?

Yes, overlap is unavoidable. The solution is not to eliminate overlap, but to control it with primary-route assignment.

### Main overlap cases

- MemRoPE belongs to both Token/KV Memory and Positional Memory.
- Pyramid-Forcing belongs to Token/KV Memory and head/layer routing.
- Echo-Forcing belongs to Token/KV Memory, Retrieval Memory, and Forgetting.
- IAMFlow belongs to Identity/Entity Memory and Retrieval-Augmented Memory.
- EM-Vid belongs to Entity Memory and Latent Retrieval.
- ConsisID belongs to Identity Memory and Spectral Memory.
- LiveWorld belongs to World-State Memory and Updating/Forgetting.

### Rule

Each paper is explained in detail once, in its primary technical route. Other sections only cross-reference it.

## 5. Are current section names too direct?

Some names are direct, but direct names are acceptable for a survey. However, to make the paper read less like a list of mechanisms, we can use slightly more polished section names.

### Current direct names and improved names

| Direct name | Improved name |
|---|---|
| Token, KV-Cache, and Attention Memory | Implicit Token Memory in Attention and KV Caches |
| Positional, Coordinate, and Spectral Memory | Remembering Time: Positional and Spectral Memory |
| Reference, Identity, Entity, and Narrative Memory | From Identity Anchors to Entity-Narrative Memory |
| Retrieval-Augmented and External Memory | Retrieval-Augmented Recall in Video Generation |
| Spatial, World-State, and Embodied Memory | From Visual Continuity to World-State Persistence |
| Evaluating Memory | Evaluating Memory Beyond Surface Consistency |

Recommended final section names are the improved versions.

## 6. More detailed paper structure

### Section 1. Introduction

1. Video generation models are moving beyond short isolated clips.
2. New use cases require persistence: long-form generation, multi-shot storytelling, identity preservation, editing, interaction, world simulation, embodied driving simulation.
3. Failures such as identity drift, scene forgetting, looped motion, wrong entity state, and out-of-sight freezing reveal memory limitations.
4. Existing surveys cover architectures, control, long-video generation, storytelling, consistency, or world models, but not memory systems as the organizing principle.
5. Contributions:
   - Define memory systems in video generation models.
   - Provide a three-layer taxonomy: object, substrate, lifecycle.
   - Reorganize existing methods by technical route and lifecycle role.
   - Survey memory-aware evaluation and open problems.

### Section 2. Background and Scope

2.1 Video generation model families: diffusion, DiT, AR rollout, streaming generation.  
2.2 Video-generation-model-based systems: long-form video, narrative video, identity-preserving generation, video editing, retrieval-augmented generation, world models, driving simulators.  
2.3 Scope boundaries: exclude pure video understanding, generic LLM memory, generic robotics without generative video base.  
2.4 Adjacent surveys and why this survey differs.

### Section 3. Memory Failures and Requirements

3.1 Identity and appearance drift.  
3.2 Scene/layout forgetting.  
3.3 Motion stagnation and temporal loops.  
3.4 Positional and spectral collapse.  
3.5 Entity duplication, disappearance, and attribute conflict.  
3.6 Out-of-sight and world-state inconsistency.  
3.7 System memory bottlenecks.  
3.8 Requirements derived from failures.

This section can be independent if it has a table/figure and enough content. Otherwise it can be merged into Section 2.

### Section 4. Three-Layer Taxonomy of Video Memory

4.1 Memory objects: what is remembered.  
4.2 Memory substrates: where it is stored.  
4.3 Memory lifecycle: how memory is managed.  
4.4 Hybrid taxonomy: why technical route is primary and lifecycle is the analysis lens.

### Section 5. Implicit Token Memory in Attention and KV Caches

5.1 Why KV cache is memory.  
5.2 Retention: windows, anchors, sinks, persistent blocks.  
5.3 Compression: memory tokens, deep sinks, quantized KV.  
5.4 Routing: head-aware and layer-aware cache policies.  
5.5 Retrieval: sparse historical KV and latent recall.  
5.6 Forgetting: cache eviction, decay, prompt-change handling.  
5.7 Summary table.

Primary papers: Echo-Forcing, MemRoPE, Deep Forcing, Pyramid-Forcing, Sparse Forcing, Future Forcing, OmniMem, LongLive-RAG, KV Cache Quantization.

### Section 6. Remembering Time: Positional and Spectral Memory

6.1 Why retained content still needs valid temporal coordinates.  
6.2 RoPE and positional phase as memory coordinates.  
6.3 Length extrapolation and phase conflict.  
6.4 Sink collapse and multi-head positional conflict.  
6.5 Frequency/spectrum memory for structure, identity, and motion.  
6.6 Relation to token memory and identity memory.

Primary/support papers: RIFLEx, LoL, FLEX, Infinity-RoPE, FreeLong++, FreeSpec, ConsisID; cross-reference MemRoPE and Pyramid-Forcing.

### Section 7. From Identity Anchors to Entity-Narrative Memory

7.1 Reference features as memory.  
7.2 Identity embeddings and identity injection.  
7.3 Temporal identity and identity dynamics.  
7.4 Entity tables and object-centric slots.  
7.5 Narrative memory and multi-shot consistency.  
7.6 Update and conflict resolution: attribute drift, duplication, subject reconstruction.  
7.7 Summary table.

Primary/support papers: IAMFlow, SlotMemory, EM-Vid, Memento, CoTriSyGen, StoryDiffusion, Video Storyboarding, ConsisID, LaVieID, ConsistI2V, Concat-ID, FantasyID, AnyID, Slot-ID, TPIGE.

### Section 8. Retrieval-Augmented Recall in Video Generation

8.1 Why long context is insufficient without selective recall.  
8.2 Scene-level recall.  
8.3 Latent and KV retrieval.  
8.4 Entity-conditioned retrieval.  
8.5 Retrieval failure modes: wrong recall, stale recall, over-recall.  
8.6 Whether this should remain independent or merge into Sections 5 and 7.

Primary papers: LongLive-RAG, OmniMem, Context-as-Memory, Echo-Forcing scene recall, IAMFlow, EM-Vid.

### Section 9. From Visual Continuity to World-State Persistence

9.1 Spatial memory and scene revisit.  
9.2 Episodic memory and pose/time metadata.  
9.3 Persistent global state and out-of-sight dynamics.  
9.4 Latent 3D/spatial caches.  
9.5 Embodied/driving world models as boundary and extension.  
9.6 Technical reports as motivation, not method mainline unless memory mechanism is explicit.

Primary/support/background papers: WorldMem, SpMem, RELIC, LiveWorld, ReMind, Mirage, MosaicMem, WorldPack, UniDriveDreamer, Sora, Genie, V-JEPA 2.

### Section 10. Evaluating Memory Beyond Surface Consistency

10.1 Why generic video metrics are insufficient.  
10.2 Identity, entity, and narrative consistency.  
10.3 Environment and scene revisit consistency.  
10.4 Causal consistency and action control.  
10.5 Out-of-sight dynamics and hidden-state tests.  
10.6 Memory budget and efficiency evaluation.  
10.7 Benchmark summary table.

Primary/support benchmarks: MIND, MBench, WorldScore, iWorld-Bench, NarraStream-Bench.

### Section 11. Open Problems

11.1 Active recall instead of passive retention.  
11.2 Entity-state memory instead of frame-indexed memory.  
11.3 Memory-aware forgetting.  
11.4 Head/layer-specialized memory routing.  
11.5 Coordinate-memory and spectrum-memory co-design.  
11.6 Multimodal and embodied memory.  
11.7 Memory-aware benchmarks and diagnostic protocols.  
11.8 Toward a unified memory API for video generation models.

## 7. Grading refinement plan

The grading table should eventually be merged into the master table with these fields:

```csv
paper,grade,primary_technical_route,lifecycle_focus,secondary_tags,primary_section,include_reason,verification_status
```

Grades:

- A: Core mainline, paragraph-level discussion.
- B: Main-supporting, short discussion or table entry.
- C: Background/context, used for scope and motivation.
- D: Boundary/analogy, used only to clarify what is outside scope.
- E: Exclude/unresolved, not cited until verified.

## 8. Current recommendation

The best current structure is:

```text
Background and Scope
-> Memory Failures and Requirements
-> Three-Layer Taxonomy
-> Technical Routes with Lifecycle Analysis
-> Evaluation
-> Open Problems
```

This is closer to mature survey style than a pure lifecycle outline, while preserving the unique memory-system contribution.
