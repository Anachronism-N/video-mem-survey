# 12 Prewriting Lock v0.5.5

> Stage: final prewriting lock before LaTeX drafting.  
> Goal: freeze the working theme, lifecycle vocabulary, section structure, paper grading policy, and figure plan before starting prose writing.

## 1. Locked working title

Main title:

> **Memory Systems in Video Generation Models**

Candidate subtitles:

1. **From Token Retention to Entity-State Persistence**
2. **From Token Memory to Entity and World-State Memory**
3. **Mechanisms, Failures, and Evaluation**

Current preferred subtitle:

> **From Token Retention to Entity-State Persistence**

Rationale: it captures the field trajectory from implicit token/cache retention to explicit entity, spatial, and world-state persistence.

## 2. Locked scope

The survey is not limited to long video generation or video world models. It covers memory-related mechanisms in video-generation-model-based systems, including:

- Video diffusion and video DiT models.
- Autoregressive / streaming video generation.
- Long-form and multi-shot generation.
- Identity-preserving video generation.
- Narrative and story-based video generation.
- Retrieval-augmented video generation.
- Video editing and video-to-video generation if memory is central.
- Generative video world models.
- Driving / embodied video simulators if video generation is the base.
- Memory-aware evaluation benchmarks.

A paper can be included even if it does not call itself a memory system, as long as it uses reference features, KV/cache state, entity tables, slots, spatial caches, retrieval banks, positional/frequency mechanisms, or state persistence to solve memory-like failures.

## 3. Locked taxonomy principle

The paper uses a three-layer conceptual taxonomy:

```text
Memory Object -> Memory Substrate -> Memory Lifecycle
```

But these are not equal-length sections.

- Memory Object: short classification of what is remembered.
- Memory Substrate: short classification of where memory is stored.
- Memory Lifecycle: a more detailed vocabulary for how memory is registered, maintained, accessed, applied, revised, and validated.

After Section 4, the paper uses a hybrid organization:

```text
Technical route = section-level organization
Lifecycle = within-section analysis lens
```

## 4. Locked lifecycle vocabulary

Use six story-level phases:

```text
Register -> Maintain -> Access -> Apply -> Revise -> Validate
```

Definitions:

- **Register**: what becomes memory in the first place.
- **Maintain**: how memory remains usable under time, context, and compute constraints.
- **Access**: which memory is selected when the current generation step needs history.
- **Apply**: how selected memory affects generation.
- **Revise**: how memory is updated, overwritten, decayed, or forgotten as the scene, prompt, action, or hidden state changes.
- **Validate**: how memory is tested through diagnostic benchmarks.

Fine-grained operations remain in tables:

```text
write / encode / anchor
retain / preserve / stabilize
compress / route / index
retrieve / recall / select
inject / condition / control
update / overwrite / decay / forget
evaluate / diagnose / stress-test
```

## 5. Locked section structure for drafting

### Section 1. Introduction

Motivate why video generation models now require memory systems.

### Section 2. Background and Scope

Define video-generation-model-based systems and distinguish this survey from adjacent surveys.

### Section 3. Memory Failures and Requirements

Explain identity drift, scene forgetting, motion loops, coordinate collapse, entity conflict, out-of-sight inconsistency, and system memory bottlenecks as memory failures.

### Section 4. Three-Layer Taxonomy of Video Memory

Introduce memory objects, memory substrates, and memory lifecycle.

### Section 5. Implicit Token Memory in Attention and KV Caches

Cover KV cache, sink tokens, memory tokens, sparse persistent blocks, head-aware caches, and token-level retrieval.

### Section 6. Remembering Time: Positional and Spectral Memory

Cover RoPE, temporal coordinates, phase conflict, sink collapse, and spectral/frequency memory.

### Section 7. From Identity Anchors to Entity-Narrative Memory

Cover reference features, identity embeddings, entity tables, object slots, subject reconstruction, and narrative state.

### Section 8. Retrieval-Augmented Recall in Video Generation

Cover scene recall, latent retrieval, external banks, content-addressed retrieval, and entity-conditioned recall. This section may later be merged with Sections 5 and 7 if it becomes too short.

### Section 9. From Visual Continuity to World-State Persistence

Cover spatial memory, episodic memory, global state, out-of-sight dynamics, and embodied/driving extensions.

### Section 10. Evaluating Memory Beyond Surface Consistency

Cover memory-specific benchmarks and why standard video metrics are insufficient.

### Section 11. Open Problems

Discuss active recall, entity-state memory, memory-aware forgetting, head/layer specialization, coordinate-memory co-design, multimodal memory, and diagnostic benchmarks.

## 6. Writing order

Recommended first writing pass:

1. Section 1: Introduction.
2. Section 2: Background and Scope.
3. Section 3: Memory Failures and Requirements.
4. Section 4: Three-Layer Taxonomy.
5. Section 5: Token/KV/Attention Memory.
6. Section 7: Identity/Entity/Narrative Memory.
7. Section 9: Spatial/World-State Memory.
8. Section 10: Evaluation.
9. Sections 6, 8, and 11.

Reason: Sections 1--4 lock the conceptual contribution; Sections 5/7/9 are the three strongest technical pillars; Section 10 anchors evaluation.

## 7. Figure strategy

Prefer original survey figures rather than directly copying figures from papers.

- Draw original conceptual figures for taxonomy, lifecycle, technical routes, failures, and evaluation.
- Use paper figures only as cited references or redrawn conceptual summaries, not direct copied images, unless license and permission are clear.
- For method-specific diagrams, use minimal redrawn abstractions with citations in the caption.

The full figure plan and drawing prompts are stored in:

```text
latex/figures/FIGURE_PLAN_AND_PROMPTS_v0.5.5.md
```

## 8. Before writing checklist

Completed:

- v0.4 full paper notes restored and verified.
- v0.5 supplement candidates added.
- Metadata-only resolution table created.
- Hybrid taxonomy created.
- Lifecycle vocabulary refined.
- A/B/C/D/E paper grading table created.
- Detailed outline created.

Remaining before final writing lock:

- Merge `paper_grading_hybrid_v0.5.3.csv` into `papers_master.csv` or create `papers_master_v0.5.6.csv`.
- Verify unresolved E-grade entries or keep them excluded.
- Decide whether Section 8 remains independent or merges into Sections 5 and 7 after a first prose draft.
- Add figure placeholders to LaTeX once figures are selected.
