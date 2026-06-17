# Structure Proposal v0.5

> Stage: discussion draft.  
> This is not the final paper text.

## 1. Proposed central theme

The survey should be framed as:

> **A survey of memory systems in video-generation-model-based systems.**

The key idea is that video generation models are increasingly used not only for short text-to-video synthesis, but also for long-form generation, identity-preserving generation, multi-shot storytelling, interactive generation, video editing, driving simulation, and video world modeling. Across these domains, memory becomes the central hidden mechanism: the model must preserve, retrieve, update, and sometimes forget information across time, entities, prompts, shots, and interactions.

## 2. Core thesis

> Long-horizon and interactive video generation is not merely a long-context problem; it is a structured memory problem.

A more general version:

> As video generation models become long-horizon, interactive, controllable, and world-model-like, their failures increasingly reveal the absence of explicit memory systems.

## 3. What makes this survey different

Existing surveys often focus on:

1. Video diffusion model architectures.
2. Long-video generation paradigms.
3. Controllable video generation.
4. Spatiotemporal consistency.
5. Video world models.
6. Storytelling video generation.

This survey should instead ask:

1. What is remembered?
2. Where is it stored?
3. How is it written?
4. How is it retrieved?
5. How is it used for generation?
6. How is it updated?
7. When should it be forgotten?
8. How should memory be evaluated?

## 4. Proposed article structure

### Section 1: Introduction

Motivation: modern video generation systems are moving from short isolated clips to persistent, interactive, and multi-shot generation. This causes memory failures: identity drift, scene forgetting, frozen motion, entity duplication, wrong state updates, and out-of-sight freezing.

Main message: these failures cannot be fully explained by visual quality or temporal consistency alone; they are failures of memory.

### Section 2: Background: From Video Generation to Video-Generation-Based Systems

Cover the ecosystem:

- Short video diffusion and DiT backbones.
- Long-form and streaming generation.
- Storytelling and multi-shot generation.
- Identity-preserving generation.
- Video editing and video-to-video generation.
- Generative video world models.
- Driving and embodied simulators.

The goal is to explain why memory appears across domains, not to survey every video model.

### Section 3: Memory Failure Taxonomy

Organize common failures:

- Identity drift.
- Scene forgetting.
- Motion loop / frozen video.
- Positional phase conflict.
- Entity disappearance / duplication.
- Attribute inconsistency.
- Out-of-sight state freezing.
- Causal inconsistency.
- System memory overflow.

### Section 4: What Should Video Generation Models Remember?

Memory objects:

- Identity memory.
- Appearance memory.
- Scene/layout memory.
- Motion/event memory.
- Positional/temporal-coordinate memory.
- Spectral/frequency memory.
- Entity/narrative memory.
- Spatial memory.
- World-state memory.
- System/cache memory.

### Section 5: Where Is Memory Stored?

Memory substrates:

- Previous frames / keyframes.
- Latent chunks.
- KV cache.
- Attention sink tokens / frames.
- Memory tokens.
- Sparse persistent blocks.
- RoPE coordinates.
- Frequency spectra.
- Reference features / identity embeddings.
- Entity tables / object slots.
- Retrieval banks.
- 3D/spatial caches.
- Recurrent or state-space states.

### Section 6: How Is Memory Managed?

Memory lifecycle:

- Write.
- Store.
- Retrieve.
- Use.
- Update.
- Forget.
- Evaluate.

This section should compare methods by lifecycle, not by application.

### Section 7: Memory Mechanisms Across Video Generation Domains

Subsections:

1. KV / attention / sparse memory.
2. Positional and spectral memory.
3. Identity and entity memory.
4. Narrative and multi-shot memory.
5. Retrieval-augmented video generation memory.
6. Spatial and world-state memory.
7. System-level memory and deployment constraints.

### Section 8: Evaluation of Memory

Benchmark dimensions:

- Entity consistency.
- Environment consistency.
- Causal consistency.
- Scene revisit consistency.
- Action-control consistency.
- Out-of-sight dynamics.
- Motion-vs-identity tradeoff.
- Efficiency / memory budget.

Main argument: generic video quality metrics and temporal consistency metrics can reward frozen or over-stabilized videos. Memory-aware evaluation needs diagnostic protocols.

### Section 9: Open Problems

- Active recall rather than passive retention.
- Entity-state memory rather than frame-indexed memory.
- Memory-aware forgetting.
- Head/layer-specialized memory routing.
- Content-position-spectrum co-design.
- Multimodal and embodied memory.
- Benchmarks for hidden state and causal memory.
- Unified memory API for video generation models.

## 5. Current decision points

Before paper writing, we should discuss:

1. Should the title emphasize “video generation models” or “generative video systems”?
2. Should video world models be a full section or integrated throughout?
3. Should identity-preserving video generation be a main pillar or background precursor to entity memory?
4. Should efficiency/KV cache memory be treated as system memory or core memory?
5. How much should technical reports such as Sora and Genie contribute to the central argument?
