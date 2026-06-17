# 08 Taxonomy and Structure Design v0.5.1

> Stage: discussion and taxonomy lock.  
> This document answers four design questions: how to balance memory object/substrate/lifecycle, how to classify papers that do not call themselves memory methods, whether memory failure taxonomy should be independent, and how to avoid duplicated discussion across sections.

## 1. Core decision

The survey title is fixed as:

> **Memory Systems in Video Generation Models**

The subtitle remains open. Current preferred candidates:

1. **From Token Retention to Entity-State Persistence**
2. **From Token Memory to Entity and World-State Memory**
3. **Mechanisms, Failures, and Evaluation**

The scope is any memory-related mechanism in systems whose base is a video generation model, including video diffusion models, video diffusion transformers, autoregressive video generators, generative video world models, and video-generation-based simulators.

## 2. How to balance the three-layer route

We keep the route:

```text
Memory object -> Memory substrate -> Memory lifecycle
```

But the three layers should not be written as equally long sections.

### Correct balance

- **Memory object**: short conceptual classification. It answers what needs to be remembered.
- **Memory substrate**: short structural classification. It answers where memory is stored.
- **Memory lifecycle**: long mechanism-oriented classification. It answers how methods work.

Therefore, Section 3 should introduce all three layers with tables and diagrams, while Sections 4 onward should mainly expand the lifecycle dimension.

## 3. Proposed macro-structure

### Section 1: Introduction

Explain why memory is becoming a core issue in video-generation-model-based systems.

### Section 2: Background and Scope

Define video-generation-model-based systems, including long-form generation, identity-preserving generation, narrative/multi-shot generation, video editing, retrieval-augmented generation, generative world models, and driving/embodied simulators.

### Section 3: A Three-Layer Taxonomy of Video Memory

This is the taxonomy foundation, not the method-detail section.

#### 3.1 Memory objects: what is remembered?

- Identity / appearance.
- Scene / layout.
- Motion / event.
- Temporal coordinate / position.
- Spectrum / frequency.
- Entity / narrative state.
- Spatial state.
- World state.
- System/cache state.

#### 3.2 Memory substrates: where is it stored?

- Previous frames / keyframes.
- Latent chunks.
- KV cache.
- Attention sink tokens or sink frames.
- Memory tokens.
- Sparse persistent blocks.
- RoPE / temporal coordinates.
- Frequency spectra.
- Reference features / identity embeddings.
- Entity tables / object slots.
- Retrieval banks.
- 3D / spatial caches.
- Recurrent or state-space states.

#### 3.3 Memory lifecycle: how is it managed?

Lifecycle stages:

- Write.
- Retain.
- Compress.
- Retrieve.
- Inject / use.
- Update.
- Forget.
- Evaluate.

Section 3 should only define these categories and give one table. It should not deeply discuss every paper.

### Section 4: Writing and Retaining Memory

Main question: how do video generation models first write memory and decide what to retain?

Representative methods:

- StreamingT2V.
- Echo-Forcing.
- MemRoPE.
- Sparse Forcing.
- IAMFlow.
- SlotMemory.
- WorldMem.
- LiveWorld.

### Section 5: Compressing and Routing Memory

Main question: how is memory made efficient and routed to the right layer/head/entity?

Representative methods:

- Deep Forcing.
- Pyramid-Forcing.
- Sparse VideoGen.
- KV Cache Quantization for Self-Forcing.
- EM-Vid.
- Slot-ID.
- Mirage.

### Section 6: Retrieving and Injecting Memory

Main question: when and how is historical memory recalled and injected into generation?

Representative methods:

- LongLive-RAG.
- OmniMem.
- Echo-Forcing scene recall frames.
- IAMFlow.
- AnyID.
- Concat-ID.
- CoTriSyGen.
- WorldMem.

### Section 7: Updating and Forgetting Memory

Main question: how do models change memory after new frames, prompts, states, or interactions?

Representative methods:

- Echo-Forcing difference-aware memory decay.
- LoL sink-collapse mitigation.
- LiveWorld out-of-sight state evolution.
- ReMind dynamic memory.
- CoTriSyGen closed-loop memory.
- Memento subject reconstruction.

### Section 8: Evaluating Memory

Main question: how do we test whether memory is real rather than superficial consistency?

Representative benchmarks:

- MIND.
- MBench.
- WorldScore.
- iWorld-Bench.
- NarraStream-Bench, if retained.

### Section 9: Open Problems

- Active recall.
- Entity-state memory.
- Memory-aware forgetting.
- Head/layer-specialized memory.
- Coordinate-memory co-design.
- Memory benchmark design.
- Unified memory interface for video-generation-based systems.

## 4. How to classify papers that do not claim to be memory systems

Many papers do not use the term memory, but they solve memory-like problems through memory-like mechanisms. These should be included if they satisfy at least one of the following criteria:

1. They store information from previous frames, chunks, references, prompts, entities, or states.
2. They retrieve or reuse stored information later.
3. They preserve identity, entity, scene, layout, motion, or world state across time.
4. They use reference features as persistent anchors.
5. They modify attention/KV/position/frequency mechanisms to maintain temporal or identity consistency.
6. They define benchmarks for persistence, revisit consistency, entity consistency, environment consistency, causal consistency, or out-of-sight dynamics.

Thus, identity-preserving video generation methods can be included even if they do not call themselves memory systems, as long as the paper uses reference features, identity embeddings, temporal identity tokens, attention injection, or reconstruction to preserve persistent identity.

## 5. Four-tier paper inclusion policy

### Tier 1: Mainline memory papers

A paper enters the mainline if it explicitly proposes or strongly implies a memory object, memory substrate, and lifecycle operation.

Examples:

- Echo-Forcing.
- MemRoPE.
- Deep Forcing.
- Pyramid-Forcing.
- Sparse Forcing.
- LongLive-RAG.
- IAMFlow.
- SlotMemory.
- EM-Vid.
- Memento.
- CoTriSyGen.
- WorldMem.
- SpMem.
- RELIC.
- LiveWorld.
- ReMind.
- Mirage.
- MIND.
- MBench.

### Tier 2: Supporting memory-related papers

A paper enters supporting discussion if it solves a memory-related failure through reference conditioning, consistency preservation, positional correction, attention sparsity, or identity anchoring, but does not present a full memory system.

Examples:

- StreamingT2V.
- Sparse VideoGen.
- RIFLEx.
- LoL.
- FreeLong++.
- FreeSpec.
- Video Storyboarding.
- ConsisID.
- LaVieID.
- ConsistI2V.
- Concat-ID.
- FantasyID.
- AnyID.
- Slot-ID.
- WorldScore.
- iWorld-Bench.

### Tier 3: Background / system context

A paper or technical report is background if it motivates why memory matters, but does not itself contribute a memory mechanism.

Examples:

- Sora technical report.
- Genie 2 / Genie 3.
- V-JEPA 2.
- MAGI-1.
- SkyReels-V2.
- Pyramid Flow.
- Self-Forcing / Rolling Forcing / LongLive.
- Driving world-model family.

### Tier 4: Boundary / not main discussion

A paper is boundary if it belongs to a related area but does not directly help explain memory in video generation models.

Examples:

- Generic video diffusion surveys.
- Generic controllable video generation surveys.
- Generic robotics world-model surveys.
- Generic LLM KV-cache methods unless used only as analogy.

## 6. Should Memory Failure Taxonomy be independent?

Decision: keep it, but not necessarily as a long independent chapter.

Recommended name:

> **Memory Failures and Requirements**

It should be a short section before the taxonomy. Its role is motivational: to show why identity drift, scene forgetting, motion loops, entity duplication, position collapse, and out-of-sight freezing are all memory failures.

Possible placement:

- Option A: Section 2.2 inside Background and Scope.
- Option B: Independent Section 3, followed by taxonomy as Section 4.

The final choice depends on length. If the failure discussion grows beyond 1.5 pages and has a table/figure, make it independent. If not, keep it as a subsection.

## 7. How to avoid duplicated discussion across sections

Papers may belong to multiple categories, but each paper should have exactly one **primary discussion location**.

Use the following rule:

1. Assign each paper one primary lifecycle role.
2. Other roles can be mentioned briefly as cross-references.
3. Use one table to show multi-label relationships, but avoid repeating full method descriptions.

Example:

- MemRoPE primary location: compressing/retaining memory with positional correction.
- Cross-reference: positional memory.
- Do not fully explain MemRoPE twice.

- IAMFlow primary location: retrieving/injecting entity memory.
- Cross-reference: identity/narrative memory.
- Do not fully explain IAMFlow twice.

- LiveWorld primary location: updating world-state memory.
- Cross-reference: spatial/world-state memory.
- Do not fully explain LiveWorld twice.

## 8. Primary-location assignment examples

| Paper | Primary section | Secondary tags |
|---|---|---|
| Echo-Forcing | Section 4/7: retain + forget | scene memory, KV memory |
| MemRoPE | Section 5: compress + coordinate memory | positional memory, memory token |
| Deep Forcing | Section 5: compress/routing | sink token, motion preservation |
| Pyramid-Forcing | Section 5: head-aware routing | KV cache, head role |
| Sparse Forcing | Section 4/5: retain persistent blocks | sparse KV memory |
| LongLive-RAG | Section 6: retrieve memory | retrieval bank, latent memory |
| IAMFlow | Section 6: retrieve/inject entity memory | identity/narrative memory |
| SlotMemory | Section 4/6: write/retrieve object slots | entity memory, KV memory |
| EM-Vid | Section 5/6: entity-indexed latent memory | latent patch bank |
| CoTriSyGen | Section 6/7: inject/update closed-loop memory | narrative memory |
| LiveWorld | Section 7: update hidden world state | out-of-sight dynamics |
| MBench | Section 8: evaluate memory | entity/environment/causal consistency |

## 9. Current recommended structure after this revision

### Section 1 Introduction

### Section 2 Background and Scope

### Section 3 Memory Failures and Requirements

May be independent or merged into Section 2 depending on length.

### Section 4 Three-Layer Taxonomy: Object, Substrate, Lifecycle

This is concise and table/figure-heavy.

### Section 5 Writing and Retaining Memory

### Section 6 Compressing and Routing Memory

### Section 7 Retrieving and Injecting Memory

### Section 8 Updating and Forgetting Memory

### Section 9 Evaluating Memory

### Section 10 Open Problems and Future Directions

## 10. Key revision from v0.5

The previous structure categorized papers by domains such as token memory, coordinate memory, identity memory, and world-state memory. This risks overlap because many methods span multiple domains.

The revised structure uses:

- Object and substrate as taxonomy coordinates.
- Lifecycle as the primary method narrative.
- Domain tags as secondary labels.

This should reduce duplication and make the survey more coherent.
