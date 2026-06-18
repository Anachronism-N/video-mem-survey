# 37 v0.8.3 Method Profiles and Figure Prompts

> Stage: continue journal-first writing after v0.8.2 reviewer-driven expansion.  
> Goal: reduce excessive bulleting by adding a representative method-profile section and provide figure prompts for external drawing.

## 1. Main update

v0.8.3 adds a new manuscript section:

```text
Representative Method Profiles and Cross-Route Evidence
```

The purpose is to answer the review concern that the draft has many framework points but insufficient method-level explanation. The new section gives more detailed profiles for representative works while preserving the mechanism-level organization.

## 2. Added method profiles

The new section expands representative works across routes:

- Cache/token memory: StreamingT2V, MAGI-style chunk memory, Echo-Forcing, MemRoPE, Sparse Forcing, OmniMem, WorldKV.
- Coordinate/spectral memory: RIFLEx, LoL, ConsisID.
- Identity/entity/narrative memory: StoryDiffusion, AnyID, Slot-ID, SlotMemory, IAMFlow, EM-Vid, VideoMemory, Memento.
- Retrieval memory: Echo-Forcing, LongLive-RAG, IAMFlow, EM-Vid.
- World-state memory: WorldMem, SpMem, RELIC, WorldKV, HyDRA, LiveWorld, ReMind, GIM-World, UniDriveDreamer, HiMem-WAM.

The profiles emphasize what each method remembers, where the memory lives, how it is accessed, whether it supports revision, and why it belongs to one or more routes.

## 3. Figure prompts added

The source package now includes prompts for three figures:

```text
figures/prompts/memory_failure_taxonomy_prompt_v083.md
figures/prompts/world_state_memory_design_patterns_prompt_v083.md
figures/prompts/retrieval_augmented_memory_prompt_v083.md
```

Recommended priority:

1. Memory Failure Taxonomy in Generated Videos.
2. World-State Memory Design Patterns.
3. Retrieval-Augmented Memory Across Substrates.

## 4. Compilation status

Local artifacts:

```text
TMM_Journal_Track_v0.8.3_preview.pdf
TMM_Journal_Track_v0.8.3.zip
```

The PDF compiles successfully with no undefined citations or references. It renders to 25 pages. Pages were rendered for visual checking, and the newly added method-profile section is readable in the TMM/IEEE two-column layout.

## 5. Remaining work

1. Expand the paper-level audit table to cover the full corpus.
2. Convert remaining paper lists into deeper pairwise or grouped comparisons.
3. Normalize BibTeX and publication status labels.
4. Insert externally drawn failure and world-state figures after they are generated.
5. Continue tightening route boundaries while preserving multi-label coding.
