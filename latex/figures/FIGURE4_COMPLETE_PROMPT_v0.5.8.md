# Figure 4 Complete Prompt v0.5.8

## Figure title

**Technical Routes with a Lifecycle Lens**

## Purpose

Figure 4 should be a survey-grade method landscape. It should not list only a few methods. It should function like a visual taxonomy map: readers should immediately see the major technical routes, the lifecycle phases emphasized by each route, and representative methods in each cell.

## Drawing prompt

```text
Create a publication-quality survey matrix titled “Technical Routes with a Lifecycle Lens”. White background, landscape orientation, AAAI/IEEE style, high readability. The figure should look like a polished taxonomy figure from a top-tier AI/CV/NLP survey paper.

Use six rows for technical routes:
1. Implicit Token Memory in Attention and KV Caches
2. Remembering Time: Positional and Spectral Memory
3. From Identity Anchors to Entity-Narrative Memory
4. Retrieval-Augmented Recall
5. From Visual Continuity to World-State Persistence
6. Evaluating Memory Beyond Surface Consistency

Use six columns for lifecycle phases:
Register, Maintain, Access, Apply, Revise, Validate.

Each cell should contain compact method chips, grouped when necessary. Use small but legible text. Use route-specific muted colors and thin grid lines. Use solid chips for primary-route methods, hollow chips for secondary-tag methods, and a star marker for benchmark/evaluation methods. Include a small legend explaining these marks.

Include the following methods/families, distributed across appropriate cells:

Token/KV/Attention Memory:
- StreamingT2V
- LongLive
- Rolling Forcing
- Causal Forcing
- Self-Forcing
- Echo-Forcing
- MemRoPE
- Deep Forcing
- Pyramid Forcing
- Sparse Forcing
- Future Forcing
- KV Cache Quantization
- LongLive-RAG
- OmniMem

Positional/Spectral Memory:
- RIFLEx
- LoL
- Infinity-RoPE
- FreeLong
- FreeLong++
- FreeSpec
- ConsisID as a secondary spectral-identity bridge
- MemRoPE as a secondary coordinate-memory bridge

Identity/Entity/Narrative Memory:
- StoryDiffusion
- Video Storyboarding
- ConsisID
- TPIGE
- LaVieID
- ConsistI2V
- Concat-ID
- FantasyID
- AnyID
- Slot-ID
- SlotMemory
- EM-Vid
- IAMFlow
- Memento
- CoTriSyGen
- EntityBench / EntityMem

Retrieval-Augmented Memory:
- LongLive-RAG
- OmniMem
- Echo-Forcing scene recall
- Context-as-Memory
- EM-Vid entity-indexed latent bank
- IAMFlow entity-conditioned recall
- DecMem if verified

Spatial/World-State Memory:
- WorldMem
- SpMem / Long-Term Spatial Memory
- RELIC
- LiveWorld
- ReMind
- Mirage / Latent Spatial Memory
- MosaicMem / Hybrid Spatial Memory
- WorldPack
- UniDriveDreamer
- GAIA / DriveDreamer / MagicDrive family as background
- Sora / Genie as background or motivation, not method mainline

Evaluation:
- MIND
- MBench
- WorldScore
- iWorld-Bench
- NarraStream-Bench
- EntityBench
- General video metrics as baseline only

Layout advice:
- Do not make the figure a dense unreadable spreadsheet.
- Use chips or short labels, not long sentences.
- Group background systems in smaller or lighter chips.
- Make the most important A-grade methods visually prominent.
- Use a small note below the matrix: “Each method has one primary route; secondary tags indicate cross-route relevance.”
- Avoid decorative icons. Prioritize clarity, completeness, and survey-style visual hierarchy.
```

## Caption draft

```text
Figure 4. Technical routes with a lifecycle lens. Rows correspond to major memory mechanisms in video-generation-model-based systems, while columns show the memory lifecycle phases emphasized by each route. Solid chips indicate primary-route methods, hollow chips indicate secondary tags, and stars indicate benchmarks or evaluation protocols. The matrix is a visual guide; method-level details and citations are provided in the accompanying taxonomy tables.
```

## Notes

This figure should be supported by detailed tables in the paper. The figure should be visually complete, but the tables should carry exact citations and method descriptions.
