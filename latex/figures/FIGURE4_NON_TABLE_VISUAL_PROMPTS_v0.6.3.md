# Figure 4 Non-Table Visual Prompts v0.6.3

> Goal: provide alternatives to a pure matrix/table for Figure 4.  
> Principle: Figure 4 should be visually memorable and publication-ready, while tables/appendix provide exhaustive coverage.

## Recommended strategy

Use a non-table visual Figure 4 in the main paper and keep the LaTeX method landscape matrix as a table or appendix.

Recommended main-paper choice:

```text
Lifecycle subway map
```

Reason: it naturally represents multiple technical routes, shared lifecycle stations, cross-route transfer methods, and background/evaluation nodes.

## Alternative A: Lifecycle Subway Map

### Concept

Each technical route is a colored metro line. The lifecycle phases are stations. Methods are placed as stops or transfer hubs. Cross-route methods appear as transfer stations. Evaluation benchmarks appear as terminal or diagnostic stations.

### Prompt

```text
Create a publication-quality survey figure titled “Memory Systems in Video Generation: A Lifecycle Map”. White background, landscape orientation, AAAI/IEEE survey style. Draw a subway-map-like schematic with six vertical or diagonal lifecycle stations: Register, Maintain, Access, Apply, Revise, Validate. Use colored metro lines for technical routes: Token/KV/Attention Memory; Positional/Spectral Memory; Identity/Entity/Narrative Memory; Retrieval-Augmented Recall; Spatial/World-State Memory; Evaluation. Place method chips as stops along each line. Use larger transfer-station nodes for cross-route methods: MemRoPE between Token/KV and Positional; Echo-Forcing between Token/KV and Retrieval; WorldKV between Token/KV and World-State; IAMFlow between Identity/Entity and Retrieval; HyDRA between World-State and Evaluation; MIND/MBench as evaluation terminals. Include representative stops: StreamingT2V, LongLive, Rolling Forcing, Causal Forcing, Self-Forcing, Echo-Forcing, MemRoPE, Deep Forcing, Pyramid Forcing, Sparse Forcing, Future Forcing, LongLive-RAG, OmniMem, RIFLEx, LoL, Infinity-RoPE, FreeLong++, StoryDiffusion, ConsisID, AnyID, Slot-ID, SlotMemory, EM-Vid, IAMFlow, Memento, CoTriSyGen, WorldMem, SpMem, RELIC, Mirage, WorldKV, HyDRA, GIM-World, LiveWorld, ReMind, HiMem-WAM, MIND, MBench, WorldScore, iWorld-Bench, EntityBench. Put background systems such as Sora, Genie, V-JEPA 2, GAIA, DriveDreamer, MagicDrive in smaller pale gray stops. Use thin lines, compact text, no decorative icons, visually balanced, readable at paper size.
```

### Caption draft

```text
Figure 4. A lifecycle map of memory mechanisms in video-generation-model-based systems. Colored routes denote technical families, stations denote lifecycle phases, and transfer nodes denote methods that bridge multiple memory mechanisms. The map is intended as a visual guide; exhaustive paper coverage and citations are provided in the accompanying tables and supplement.
```

## Alternative B: Memory-Flow Sankey Diagram

### Concept

Show how memory objects flow into memory substrates, lifecycle operations, and technical routes. This is visually stronger than a table but less exhaustive.

### Prompt

```text
Create a clean academic Sankey-style figure titled “From Memory Objects to Technical Routes”. White background, landscape orientation. Left column: memory objects with compact labels: Token History, Temporal Position, Identity, Entity State, Scene Layout, Spatial Geometry, World State, Evaluation Signal. Middle-left column: memory substrates: KV Cache, Memory Tokens, RoPE/Frequency, Reference Features, Entity Tables, Retrieval Banks, Spatial Caches, Global State. Middle-right column: lifecycle operations: Register, Maintain, Access, Apply, Revise, Validate. Right column: technical routes: Token/KV/Attention, Positional/Spectral, Identity/Entity/Narrative, Retrieval-Augmented, Spatial/World-State, Evaluation. Draw smooth thin flows; use muted colors; place representative method chips near flows: MemRoPE, Echo-Forcing, WorldKV, IAMFlow, HyDRA, GIM-World, MIND, MBench. Use line thickness only subtly, not as quantitative data. Publication-ready, AAAI/IEEE survey style.
```

### Caption draft

```text
Figure 4. Memory-flow view of video-generation memory systems. The figure traces how memory objects are represented through substrates, managed by lifecycle operations, and instantiated by technical routes.
```

## Alternative C: Radial Lifecycle Wheel

### Concept

The six lifecycle phases form a ring. Technical routes are concentric bands or radial arcs. Methods sit near their dominant lifecycle phase. Cross-route methods appear as bridges across rings.

### Prompt

```text
Create a radial lifecycle wheel titled “Memory Lifecycle across Technical Routes”. White background, circular academic infographic style. Use six outer sectors labeled Register, Maintain, Access, Apply, Revise, Validate. Use concentric rings for technical routes: Token/KV/Attention, Positional/Spectral, Identity/Entity/Narrative, Retrieval-Augmented, Spatial/World-State, Evaluation. Place method chips inside sectors according to lifecycle focus: StreamingT2V, Echo-Forcing, MemRoPE, Pyramid Forcing, Sparse Forcing, RIFLEx, LoL, StoryDiffusion, ConsisID, AnyID, Slot-ID, IAMFlow, Memento, WorldKV, HyDRA, GIM-World, LiveWorld, ReMind, MIND, MBench, iWorld-Bench. Draw thin bridge lines for cross-route methods. Use muted colors, readable labels, no clutter, no icons, top-tier survey paper style.
```

### Caption draft

```text
Figure 4. Radial view of the memory lifecycle. Methods are positioned by their dominant lifecycle phase and technical route; bridge lines mark cross-route mechanisms.
```

## Alternative D: Layered Memory Stack Map

### Concept

A stack-style figure shows four layers: memory object, memory substrate, lifecycle operation, technical route. It is good for explaining the taxonomy but less dynamic than the subway map.

### Prompt

```text
Create a layered stack diagram titled “A Memory Stack for Video Generation Models”. White background, landscape orientation. Draw four horizontal layers from bottom to top: Memory Objects, Memory Substrates, Lifecycle Operations, Technical Routes. In Memory Objects, include Token History, Time, Identity, Entity, Scene, Geometry, World State. In Memory Substrates, include KV Cache, Sink Tokens, Memory Tokens, RoPE/Frequency, Reference Features, Entity Slots, Retrieval Bank, Spatial Cache, Global State. In Lifecycle Operations, show Register, Maintain, Access, Apply, Revise, Validate as connected nodes. In Technical Routes, show Token/KV/Attention, Positional/Spectral, Identity/Entity/Narrative, Retrieval-Augmented, Spatial/World-State, Evaluation. Add representative method chips on the relevant connections: MemRoPE, Echo-Forcing, IAMFlow, WorldKV, HyDRA, GIM-World, MIND, MBench. Use muted colors, thin lines, high readability, no dense table layout.
```

### Caption draft

```text
Figure 4. A layered memory stack for video generation models, linking remembered objects, storage substrates, lifecycle operations, and technical routes.
```

## Alternative E: Route-Lifecycle Terrain Map

### Concept

A stylized map with regions for technical routes and paths for lifecycle phases. Methods are landmarks. This is visually distinctive but risks being less formal.

### Prompt

```text
Create a polished academic “terrain map” taxonomy figure titled “Landscape of Memory Systems in Video Generation”. Use a white background with softly separated regions: Token Cache Region, Time/Position Region, Identity/Entity Region, Retrieval Region, World-State Region, Evaluation Region. Overlay a thin left-to-right lifecycle path: Register → Maintain → Access → Apply → Revise → Validate. Place method chips as landmarks in regions: Echo-Forcing, MemRoPE, Sparse Forcing, RIFLEx, LoL, IAMFlow, SlotMemory, WorldKV, HyDRA, GIM-World, LiveWorld, ReMind, MIND, MBench. Use small bridge paths between regions for cross-route methods. Avoid cartoonish map styling; make it look like a modern top-tier survey taxonomy figure.
```

### Caption draft

```text
Figure 4. Landscape view of memory systems. Regions denote technical routes, while the lifecycle path shows how memory is registered, maintained, accessed, applied, revised, and validated.
```

## Alternative F: Hybrid Metro-Matrix

### Concept

A compromise between table and visual map. Rows are technical routes, columns are lifecycle phases, but instead of table cells, use curved route lines and method chips.

### Prompt

```text
Create a hybrid metro-matrix figure titled “Technical Routes with a Lifecycle Lens”. White background, landscape layout. Use six lifecycle columns: Register, Maintain, Access, Apply, Revise, Validate. Use colored curved paths for technical routes running across the columns: Token/KV/Attention Memory, Positional/Spectral Memory, Identity/Entity/Narrative Memory, Retrieval-Augmented Recall, Spatial/World-State Memory, Evaluation. Place method chips along the paths at relevant columns. Use transfer nodes for methods crossing routes: MemRoPE, Echo-Forcing, WorldKV, IAMFlow, HyDRA, GIM-World. Use stars for benchmarks: MIND, MBench, WorldScore, iWorld-Bench, EntityBench. Use compact but readable typography, muted colors, thin lines, and a small legend. This should look like a highly polished taxonomy figure from a top-tier AI survey.
```

### Caption draft

```text
Figure 4. Hybrid metro-matrix of technical routes and lifecycle phases. Route lines encode technical families; columns encode lifecycle phases; transfer nodes indicate methods that bridge routes.
```

## Final recommendation

Use **Alternative A: Lifecycle Subway Map** as the main Figure 4.

Use the current LaTeX matrix as a detailed table or appendix. This gives the paper both visual appeal and auditability.
