# Figure Plan and Drawing Prompts v0.5.5

> Stage: prewriting figure plan.  
> Principle: prefer original survey figures. Do not directly copy paper figures unless permissions/license are clear. When a figure is inspired by a paper-specific mechanism, redraw it as an abstract schematic and cite the paper in the caption.

## Figure priority overview

### Must-have figures

1. Figure 1: Memory systems overview.
2. Figure 2: Memory failures and requirements.
3. Figure 3: Three-layer taxonomy: object, substrate, lifecycle.
4. Figure 4: Hybrid taxonomy: technical routes with lifecycle lens.
5. Figure 5: Evaluation beyond surface consistency.

### Optional but valuable figures

6. Figure 6: Token/KV/attention memory route.
7. Figure 7: Identity/entity/narrative memory route.
8. Figure 8: From visual continuity to world-state persistence.
9. Figure 9: Method landscape timeline.
10. Figure 10: Memory benchmark matrix.

## Figure 1. Memory Systems in Video Generation Models

### Purpose

This is the main overview figure for the paper. It should communicate the core thesis: memory systems in video generation models can be understood through memory objects, memory substrates, and memory lifecycle, across multiple technical routes.

### Draw or cite?

Draw original figure. Do not cite a single source figure.

### Suggested placement

Introduction or Section 4.

### Content

Left side: video-generation-model-based systems.

- Long-form video generation.
- Identity-preserving generation.
- Narrative/multi-shot generation.
- Retrieval-augmented generation.
- Generative world models.
- Embodied/driving simulators.

Middle: three-layer memory framework.

- Memory objects.
- Memory substrates.
- Memory lifecycle.

Right side: technical routes.

- Token/KV/attention memory.
- Positional/spectral memory.
- Identity/entity/narrative memory.
- Retrieval-augmented memory.
- Spatial/world-state memory.
- Evaluation.

### Drawing prompt

```text
Create a clean academic survey figure on a white background, IEEE/AAAI style, landscape layout. Title: “Memory Systems in Video Generation Models”. Use three columns connected left-to-right. Left column: “Video-generation-model-based systems” with six rounded boxes: Long-form generation, Identity-preserving generation, Narrative/multi-shot generation, Retrieval-augmented generation, Generative world models, Embodied/driving simulators. Middle column: “Three-layer memory framework” with three stacked layers: Memory Objects, Memory Substrates, Memory Lifecycle. Right column: “Technical routes” with six rounded boxes: Token/KV/Attention Memory, Positional & Spectral Memory, Identity/Entity/Narrative Memory, Retrieval-Augmented Memory, Spatial/World-State Memory, Memory Evaluation. Use thin 1.2pt lines, muted blue/green/orange accents, no icons that look cartoonish, high readability, vector-diagram style, suitable for a survey paper.
```

## Figure 2. Memory Failures and Requirements

### Purpose

Motivates why memory is a useful organizing lens. It maps visible failure modes to memory requirements.

### Draw or cite?

Draw original figure. It can use simplified symbolic panels, not copied examples from papers.

### Suggested placement

Section 3.

### Content

Rows or panels:

- Identity drift -> identity memory.
- Scene/layout forgetting -> scene/layout memory.
- Motion loop/frozen video -> motion/event memory.
- Positional/spectral collapse -> coordinate/spectrum memory.
- Entity duplication/disappearance -> entity-state memory.
- Out-of-sight inconsistency -> world-state memory.
- System memory overflow -> efficient/cache memory.

### Drawing prompt

```text
Create a clean academic taxonomy figure on a white background. Title: “Memory Failures and Requirements”. Use a 2-column mapping layout. Left column: “Observed failure” with seven small schematic panels: Identity drift, Scene/layout forgetting, Motion loop or frozen video, Positional or spectral collapse, Entity duplication/disappearance, Out-of-sight inconsistency, System memory overflow. Right column: “Memory requirement” with corresponding boxes: Identity memory, Scene/layout memory, Motion/event memory, Coordinate/spectral memory, Entity-state memory, World-state memory, Efficient system/cache memory. Use arrows from each failure to the corresponding requirement. Use simple abstract icons only: face silhouette, room grid, repeated frames, timeline wave, two duplicate objects, hidden object behind wall, overflowing cache block. Use muted colors, thin lines, no realistic images, publication-ready vector style.
```

## Figure 3. Three-Layer Taxonomy: Object, Substrate, Lifecycle

### Purpose

Explains the core taxonomy before method sections.

### Draw or cite?

Draw original figure.

### Suggested placement

Section 4.

### Content

Three linked panels:

1. Memory Object: identity, scene, motion, coordinate, spectrum, entity, spatial, world-state, system.
2. Memory Substrate: frames, latent chunks, KV cache, sink tokens, memory tokens, sparse blocks, RoPE coordinates, frequency spectra, reference features, entity tables, retrieval banks, spatial caches, state variables.
3. Memory Lifecycle: Register, Maintain, Access, Apply, Revise, Validate.

### Drawing prompt

```text
Create a clean three-panel taxonomy diagram for an academic survey paper. White background, landscape orientation. Title: “A Three-Layer Taxonomy of Video Memory”. Panel 1: “Memory Objects: What is remembered?” with compact tags: Identity, Appearance, Scene/Layout, Motion/Event, Temporal Coordinate, Spectrum, Entity/Narrative, Spatial State, World State, System State. Panel 2: “Memory Substrates: Where is it stored?” with tags: Frames/Keyframes, Latent Chunks, KV Cache, Sink Tokens, Memory Tokens, Sparse Blocks, RoPE Coordinates, Frequency Spectra, Reference Features, Entity Tables, Retrieval Banks, Spatial Caches, State Variables. Panel 3: “Memory Lifecycle: How is it managed?” with a horizontal flow: Register → Maintain → Access → Apply → Revise → Validate. Connect the three panels with subtle arrows. Use compact typography, thin borders, muted colors, no decorative background, suitable for LaTeX inclusion.
```

## Figure 4. Hybrid Taxonomy: Technical Routes with Lifecycle Lens

### Purpose

Shows how the paper is organized after Section 4: technical route is the primary axis, lifecycle is the within-route lens.

### Draw or cite?

Draw original figure.

### Suggested placement

End of Section 4 or start of Section 5.

### Content

A matrix:

Rows = technical routes.

- Implicit Token Memory in Attention and KV Caches.
- Remembering Time: Positional and Spectral Memory.
- From Identity Anchors to Entity-Narrative Memory.
- Retrieval-Augmented Recall.
- From Visual Continuity to World-State Persistence.
- Evaluating Memory Beyond Surface Consistency.

Columns = lifecycle phases.

- Register.
- Maintain.
- Access.
- Apply.
- Revise.
- Validate.

Cells contain representative methods or check marks.

### Drawing prompt

```text
Create a publication-quality matrix figure on a white background. Title: “Technical Routes with a Lifecycle Lens”. Rows are six technical routes: Implicit Token Memory in Attention and KV Caches; Remembering Time: Positional and Spectral Memory; From Identity Anchors to Entity-Narrative Memory; Retrieval-Augmented Recall; From Visual Continuity to World-State Persistence; Evaluating Memory Beyond Surface Consistency. Columns are lifecycle phases: Register, Maintain, Access, Apply, Revise, Validate. Fill cells with short method names where relevant: Echo-Forcing, MemRoPE, Pyramid-Forcing, Sparse Forcing, RIFLEx, LoL, IAMFlow, SlotMemory, EM-Vid, LongLive-RAG, WorldMem, LiveWorld, MIND, MBench. Use a light heatmap style with muted colors, but keep all text readable. Avoid dense clutter; use abbreviations only if necessary. Thin grid lines, AAAI/IEEE survey style.
```

## Figure 5. Evaluating Memory Beyond Surface Consistency

### Purpose

Clarifies why generic video quality or temporal consistency metrics are insufficient.

### Draw or cite?

Draw original conceptual figure.

### Suggested placement

Section 10.

### Content

Three failure cases:

- Stable but frozen.
- Dynamic but identity drifts.
- Plausible but world-state wrong.

Map to benchmark requirements:

- Identity/entity consistency.
- Environment consistency.
- Causal consistency.
- Out-of-sight dynamics.
- Closed-loop action control.
- Memory budget.

### Drawing prompt

```text
Create a clean academic figure titled “Evaluating Memory Beyond Surface Consistency”. White background. Top row: three simplified video-strip examples, each with 4 frames: (1) Stable but frozen: same frame repeated; (2) Dynamic but identity drifts: character changes appearance across frames; (3) Plausible but world-state wrong: hidden object reappears incorrectly or causal state changes incorrectly. Bottom row: diagnostic memory metrics connected by arrows: Identity/Entity Consistency, Environment Consistency, Causal Consistency, Out-of-Sight Dynamics, Closed-loop Action Control, Memory Budget. Use schematic icons and simple frame boxes, not realistic images. Make it look like an IEEE/AAAI survey illustration, vector style, clear labels, muted colors.
```

## Figure 6. Implicit Token Memory in Attention and KV Caches

### Purpose

Explains the technical route for Section 5.

### Draw or cite?

Draw original abstraction. Cite representative papers in caption.

### Suggested placement

Section 5.

### Content

Input video chunks -> KV cache/history -> memory maintenance mechanisms:

- recent window.
- anchor/sink.
- memory tokens.
- sparse persistent blocks.
- head-aware cache.
- quantized/compressed cache.

Output: generated next chunks.

### Drawing prompt

```text
Create a clean technical schematic titled “Implicit Token Memory in Attention and KV Caches”. White background, left-to-right flow. Left: sequence of video chunks entering an autoregressive video generation model. Middle: a large “Historical token / KV cache memory” module containing sub-blocks: Recent Window, Anchor/Sink Tokens, Memory Tokens, Sparse Persistent Blocks, Head-Aware Cache, Quantized Cache. Show arrows from cache memory into a Video DiT / Attention block. Right: generated future video chunks. Include a small lifecycle strip below: Register → Maintain → Access → Apply → Revise. Use thin lines, muted colors, no photorealistic content, vector diagram suitable for a survey paper.
```

## Figure 7. From Identity Anchors to Entity-Narrative Memory

### Purpose

Explains Section 7.

### Draw or cite?

Draw original abstraction. Cite identity/entity memory papers in caption.

### Content

Reference inputs -> identity/entity memory -> generation control.

- Reference image/video.
- Prompt entities and attributes.
- Entity table / object slots.
- Identity embeddings.
- Narrative state.
- VLM or reconstruction-based revision.

### Drawing prompt

```text
Create a clean academic schematic titled “From Identity Anchors to Entity-Narrative Memory”. White background. Left: inputs including Reference Image, Reference Video, Prompt, Previous Shots. Middle: an “Entity-Narrative Memory” module with subcomponents: Identity Embeddings, Entity Table, Object Slots, Attribute State, Narrative Role, Subject Reconstruction / Verification. Right: multi-shot generated video strip with consistent character identity and updated attributes. Use arrows labeled Register, Access, Apply, Revise. Use abstract human silhouettes and object icons, not realistic faces. Muted colors, thin lines, vector style, publication-ready.
```

## Figure 8. From Visual Continuity to World-State Persistence

### Purpose

Explains Section 9 and the jump from visual consistency to world-state memory.

### Draw or cite?

Draw original conceptual figure. Cite world-memory papers in caption.

### Content

Levels:

1. Visual continuity.
2. Scene revisit consistency.
3. Spatial memory.
4. Hidden / out-of-sight state evolution.
5. Embodied or action-conditioned world-state persistence.

### Drawing prompt

```text
Create a clean layered pyramid or staircase diagram titled “From Visual Continuity to World-State Persistence”. White background. Five ascending levels: Visual Continuity, Scene Revisit Consistency, Spatial Memory, Out-of-Sight State Evolution, Action-Conditioned World-State Persistence. Place representative method labels near levels: ConsistI2V/StoryDiffusion near Visual Continuity; Echo-Forcing/LongLive-RAG near Scene Revisit; WorldMem/SpMem/Mirage near Spatial Memory; LiveWorld/ReMind near Out-of-Sight State Evolution; UniDriveDreamer/Genie/Sora as background near Action-Conditioned World-State Persistence. Use subtle arrows upward, muted colors, academic vector style.
```

## Figure 9. Method Landscape Timeline

### Purpose

Shows the recent emergence of memory-related mechanisms.

### Draw or cite?

Draw original timeline.

### Suggested placement

Introduction or appendix.

### Content

Timeline 2024--2026 with routes:

- Token/KV memory.
- Positional/spectral memory.
- Identity/entity memory.
- World-state memory.
- Evaluation.

### Drawing prompt

```text
Create a horizontal academic timeline titled “Emergence of Memory Mechanisms in Video Generation Models”. Timeline from 2024 to 2026. Use five horizontal lanes: Token/KV Memory, Positional/Spectral Memory, Identity/Entity Memory, World-State Memory, Evaluation. Place method labels approximately by year: StreamingT2V, StoryDiffusion, ConsistI2V, Sora in 2024; MAGI-1, RIFLEx, FreeLong++, LaVieID, WorldMem, SpMem in 2025; Echo-Forcing, MemRoPE, Pyramid-Forcing, Sparse Forcing, IAMFlow, SlotMemory, LiveWorld, MIND, MBench in 2026. Clean white background, muted color by lane, thin lines, compact labels, survey-paper style.
```

## Figure 10. Benchmark Matrix for Memory Evaluation

### Purpose

Summarizes evaluation tasks and benchmarks.

### Draw or cite?

Draw original table/matrix.

### Suggested placement

Section 10.

### Content

Rows = benchmark dimensions:

- Identity consistency.
- Entity consistency.
- Environment consistency.
- Causal consistency.
- Scene revisit.
- Out-of-sight dynamics.
- Closed-loop action control.
- Memory budget.

Columns = benchmarks:

- MIND.
- MBench.
- WorldScore.
- iWorld-Bench.
- NarraStream-Bench.
- General video metrics.

### Drawing prompt

```text
Create a clean benchmark matrix figure titled “Memory Evaluation Dimensions”. White background. Rows: Identity Consistency, Entity Consistency, Environment Consistency, Causal Consistency, Scene Revisit, Out-of-Sight Dynamics, Closed-loop Action Control, Memory Budget. Columns: MIND, MBench, WorldScore, iWorld-Bench, NarraStream-Bench, General Video Metrics. Fill cells with check marks, partial marks, or blank circles. Use muted blue-green heatmap intensity to indicate coverage. Include a small note: “General video metrics are insufficient for diagnostic memory evaluation.” Thin grid lines, high readability, publication-ready.
```

## Which figures to cite from papers?

Avoid direct copying unless permission is clear. Recommended policy:

1. Do not directly reproduce paper figures in the main survey.
2. Redraw abstracted method schematics when needed.
3. Cite the original papers in captions and surrounding text.
4. If a paper has a highly recognizable architecture figure, use it only as a reading reference, not as a copied survey figure.

Potential paper figures to consult while redrawing:

- Echo-Forcing: scene memory, scene recall frames, memory decay.
- MemRoPE: memory tokens and online RoPE indexing.
- Pyramid-Forcing: head-aware cache policy.
- IAMFlow: entity extraction, global ID, memory verification loop.
- SlotMemory / EM-Vid: object/entity memory structures.
- WorldMem / SpMem / LiveWorld / ReMind / Mirage: spatial or world-state memory diagrams.
- MIND / MBench: benchmark task taxonomy.

## Recommended first figure batch

Draw these first:

1. Figure 1: Memory systems overview.
2. Figure 3: Three-layer taxonomy.
3. Figure 4: Hybrid taxonomy matrix.
4. Figure 5: Evaluation beyond surface consistency.
5. Figure 8: From visual continuity to world-state persistence.

These five figures are enough to support the first writing pass.
