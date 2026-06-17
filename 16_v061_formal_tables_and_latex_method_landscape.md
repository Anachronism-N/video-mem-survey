# 16 v0.6.1 Formal Tables and LaTeX Method Landscape

> Stage: self-review pass after v0.6.0.  
> Goal: strengthen the draft with more formulas, pseudocode, comprehensive coverage tables, and a LaTeX-native replacement for the previous Figure 4 prompt.

## 1. Main response to current comments

The v0.6.0 draft still had three weaknesses:

1. It contained too few formulas and pseudocode blocks for a technical survey.
2. Some tables were useful but still too sparse for top-conference survey standards.
3. The previous Figure 4 design was described as a drawing prompt, but the content is naturally a matrix and can be rendered directly in LaTeX.

v0.6.1 addresses these issues.

## 2. Formalism added in v0.6.1

The draft now includes additional lightweight formalism:

- A memory priority score for retaining, compressing, retrieving, or evicting memories.
- A token/KV cache selector that exposes relevance, stability, future utility, and cost terms.
- An entity-memory update abstraction that separates persistent identity from mutable attributes and historical evidence.
- A generic retrieval score with embedding similarity, metadata match, age penalty, and conflict penalty.
- A vector-valued memory score for reporting identity, entity, environment, causal, revisit, out-of-sight, and budget dimensions.

These are not claimed as new algorithms. They are analytical interfaces for comparing papers.

## 3. Pseudocode added in v0.6.1

The draft now includes:

- Algorithm 1: Generic lifecycle of a memory-augmented video generator.
- Algorithm 2: Budgeted cache maintenance and retrieval.
- Algorithm 3: Retrieval-augmented recall with conflict filtering.

These pseudocode blocks are written in LaTeX tables to avoid depending on fragile algorithm packages and to keep the working draft portable.

## 4. Figure 4 change

The old Figure 4 prompt is no longer the main artifact. v0.6.1 adds a LaTeX-rendered method landscape matrix directly in the paper.

The matrix covers:

- Token/KV/Attention memory.
- Positional/Spectral memory.
- Identity/Entity/Narrative memory.
- Retrieval-Augmented memory.
- Spatial/World-State memory.

It includes many more methods than the earlier prompt, including:

- StreamingT2V, LongLive, Rolling Forcing, Causal Forcing, Self-Forcing.
- Echo-Forcing, MemRoPE, Deep Forcing, Pyramid Forcing, Sparse Forcing, Future Forcing, KV Quantization.
- LongLive-RAG, OmniMem, WorldKV, Context-as-Memory, DecMem.
- RIFLEx, FLEX, LoL, Infinity-RoPE, FreeLong, FreeLong++, FreeSpec.
- StoryDiffusion, Video Storyboarding, ConsisID, AnyID, LaVieID, FantasyID, Concat-ID, TPIGE.
- Slot-ID, SlotMemory, EM-Vid, IAMFlow, Memento, CoTriSyGen.
- WorldMem, SpMem, WorldPack, RELIC, Mirage, MosaicMem, LiveWorld, ReMind.
- MIND, MBench, WorldScore, iWorld-Bench, EntityBench, NarraStream-Bench.
- Sora, Genie, V-JEPA 2 as background/motivation chips rather than mainline method chips.

This does not yet guarantee every one of the 102 collected notes is represented in the figure, but it is substantially more complete and audit-friendly. Full 102-paper coverage should live in a supplemental table, not in a single figure.

## 5. New coverage audit table

v0.6.1 also adds a coverage audit table. It groups papers into:

- mainline methods,
- supporting or secondary methods,
- background, benchmark, or unresolved items.

This makes coverage more transparent and prevents the paper from appearing to discuss only a small subset of methods.

## 6. Current output

The current local artifacts are:

```text
Memory_Systems_in_Video_Generation_Models_v0.6.1_working_draft.pdf
Memory_Systems_v0.6.1_latex_source.zip
```

The PDF compiles without undefined citations and has been rendered for visual checking.
