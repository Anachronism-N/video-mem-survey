# 09 Hybrid Taxonomy and Paper Grading v0.5.2

> Stage: taxonomy and paper-grading lock.  
> Goal: avoid the weakness of a pure lifecycle-based organization while preserving lifecycle as the core explanatory lens.

## 1. Why pure lifecycle is insufficient

A pure lifecycle structure such as `write -> retain -> compress -> retrieve -> inject -> update -> forget -> evaluate` has one clear advantage: it directly explains how memory works. However, it has two problems for a survey paper:

1. **Weak technical-route visibility.** Readers cannot immediately see the landscape of KV-cache memory, RoPE/positional memory, identity/entity memory, retrieval-augmented memory, or world-state memory.
2. **Method fragmentation.** A method such as Echo-Forcing has retain, retrieve, and forget operations. If the paper is split by lifecycle only, the same method is either repeated several times or artificially reduced to one operation.

Therefore, the final survey should use a hybrid organization.

## 2. Proposed hybrid organization

Use:

```text
Primary axis: technical route
Secondary axis: lifecycle role
```

That means:

- **Technical route** decides where a paper is discussed in detail.
- **Lifecycle role** decides which aspect of that paper is emphasized.
- **Memory object** and **memory substrate** remain the coordinate system introduced early in the survey.

This preserves the three-layer route:

```text
Memory object -> Memory substrate -> Memory lifecycle
```

but avoids making lifecycle the only visible organization.

## 3. Final high-level structure after hybridization

### Section 1. Introduction

Motivate memory as a general problem in video-generation-model-based systems.

### Section 2. Background and Scope

Define the scope: video diffusion, video DiT, autoregressive video generation, long-form generation, identity-preserving video generation, narrative generation, video editing, retrieval-augmented video generation, video world models, and embodied/driving simulators.

### Section 3. Memory Failures and Requirements

Explain why common failures are memory failures. This can be independent if long enough; otherwise it can be merged into Section 2.

### Section 4. Three-Layer Taxonomy of Video Memory

Concise taxonomy section:

1. Memory objects: what is remembered?
2. Memory substrates: where is memory stored?
3. Memory lifecycle: how is memory managed?

This section should be table-heavy and concept-heavy, not method-detail-heavy.

### Section 5. Token, KV-Cache, and Attention Memory

Technical route: historical tokens, KV cache, sink tokens, sparse persistent blocks, head-aware caches, memory tokens.

Lifecycle focus: retain, compress, route, retrieve, forget.

Representative mainline papers:

- Echo-Forcing.
- MemRoPE.
- Deep Forcing.
- Pyramid-Forcing.
- Sparse Forcing.
- Future Forcing.
- OmniMem.
- LongLive-RAG.
- KV Cache Quantization for Self-Forcing.

### Section 6. Positional, Coordinate, and Spectral Memory

Technical route: RoPE, positional phase, temporal coordinates, frequency/spectrum regulation.

Lifecycle focus: retain valid temporal meaning, compress without phase conflict, avoid sink collapse, preserve low/high-frequency information.

Representative mainline/supporting papers:

- RIFLEx.
- LoL: Longer than Longer.
- FLEX.
- Infinity-RoPE.
- FreeLong++.
- FreeSpec.
- MemRoPE and Pyramid-Forcing as cross-referenced papers.

### Section 7. Reference, Identity, Entity, and Narrative Memory

Technical route: reference features, identity embeddings, entity tables, object-centric slots, subject reconstruction, story memory, narrative state.

Lifecycle focus: write identity/entity memory, retrieve correct entity, inject reference information, update attributes, avoid duplication and drift.

Representative mainline/supporting papers:

- IAMFlow.
- SlotMemory.
- EM-Vid.
- Memento.
- CoTriSyGen.
- StoryDiffusion.
- Video Storyboarding.
- ConsisID.
- LaVieID.
- ConsistI2V.
- Concat-ID.
- FantasyID.
- AnyID.
- Slot-ID.
- TPIGE.

### Section 8. Retrieval-Augmented and External Memory

Technical route: explicit retrieval banks, scene recall, latent retrieval, external memory banks, content-addressed recall.

Lifecycle focus: retrieve and inject.

Representative papers:

- LongLive-RAG.
- OmniMem.
- Echo-Forcing scene recall frames.
- Context-as-Memory.
- IAMFlow entity recall.
- EM-Vid latent entity bank.

This section may be merged with Sections 5 and 7 if it becomes too short. It is currently a candidate bridge section.

### Section 9. Spatial, World-State, and Embodied Memory

Technical route: spatial memory, episodic memory, global state, out-of-sight dynamics, embodied/driving simulation memory.

Lifecycle focus: write state, update hidden state, remember off-screen objects, maintain causal consistency.

Representative mainline/supporting/background papers:

- WorldMem.
- SpMem.
- RELIC.
- LiveWorld.
- ReMind.
- Mirage.
- MosaicMem.
- WorldPack.
- UniDriveDreamer.
- Sora technical report.
- Genie 2/3.
- V-JEPA 2 as boundary/background.

### Section 10. Evaluating Memory

Technical route: memory-aware benchmarks and diagnostic protocols.

Lifecycle focus: evaluate.

Representative papers/benchmarks:

- MIND.
- MBench.
- WorldScore.
- iWorld-Bench.
- NarraStream-Bench.
- VBench and general metrics as background only.

### Section 11. Open Problems

- Active recall.
- Entity-state memory.
- Memory-aware forgetting.
- Head/layer-specialized memory.
- Coordinate-memory co-design.
- Spectrum-memory co-design.
- Multimodal/embodied memory.
- Diagnostic memory benchmarks.

## 4. Cross-section duplication policy

A paper can have multiple tags, but it must have exactly one **primary route** where it is explained in detail.

Use this rule:

```text
technical route = primary section
lifecycle role = explanation angle
memory object/substrate = table labels
```

Example:

- MemRoPE primary route: Token/KV/Attention Memory.
- Lifecycle role: compress + retain + coordinate correction.
- Secondary route: Positional memory.
- Full explanation appears once; later sections cross-reference it briefly.

Example:

- IAMFlow primary route: Reference/Identity/Entity Memory.
- Lifecycle role: write + retrieve + inject + update entity attributes.
- Secondary route: Retrieval-augmented memory.
- Full explanation appears once; retrieval section only points back to it.

Example:

- LiveWorld primary route: Spatial/World-State Memory.
- Lifecycle role: update hidden world state.
- Secondary route: Evaluation/failure taxonomy.

## 5. Inclusion tiers

### Grade A: Core mainline

Papers that should receive paragraph-level discussion in the main text. These papers explicitly or strongly instantiate memory object + substrate + lifecycle operation.

### Grade B: Main-supporting

Papers that support a main technical route but should receive shorter discussion, usually one or two sentences or table entries.

### Grade C: Background/context

Papers, systems, or technical reports that motivate the survey scope or provide backbone context, but are not themselves memory mechanisms.

### Grade D: Boundary/analogy

Related but not central. Mention only for scope boundaries or analogy.

### Grade E: Exclude or unresolved

Insufficiently verified, too far from video-generation-model-based memory, or redundant with stronger papers.

## 6. Current recommendation

The survey should not be pure lifecycle. The best structure is:

```text
Background -> Failures/Requirements -> Three-Layer Taxonomy -> Technical Routes with Lifecycle Analysis -> Evaluation -> Open Problems
```

This is more readable for survey audiences and still preserves the memory-system thesis.
