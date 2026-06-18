# 34 v0.8.0 Citation Integration and Bibliography Expansion

> Stage: continue journal-first writing after v0.7.9.  
> Goal: add in-text citations and expand the BibTeX database so the manuscript starts to become a properly cited journal survey rather than an uncited working draft.

## 1. Main update

v0.8.0 adds citation support across the TMM journal track. The previous draft had mechanism-level text but very few citations. This pass adds citations to the Introduction, Related Surveys, Memory Failures, Taxonomy, and Sections 5--11.

## 2. Bibliography expansion

The BibTeX database has been expanded from a minimal one-entry file to roughly forty entries covering:

- long-video and video-diffusion background;
- adjacent surveys;
- cache/KV memory methods;
- positional and spectral memory methods;
- identity/entity/narrative memory methods;
- retrieval-augmented memory methods;
- world-state memory methods;
- evaluation and benchmark papers.

Representative added references include Sora, StreamingT2V, MAGI-1, Echo-Forcing, MemRoPE, Sparse Forcing, WorldKV, RIFLEx, LoL, StoryDiffusion, ConsisID, AnyID, Slot-ID, SlotMemory, IAMFlow, EM-Vid, Memento, VideoMemory, WorldMem, SpMem, RELIC, LiveWorld, ReMind, HyDRA, GIM-World, HiMem-WAM, MIND, MBench, WorldScore, iWorld-Bench, Echo-Memory, and adjacent survey papers.

## 3. Citation placement

Citations have been added at route-level anchor points rather than after every sentence. The goal is to support the mechanism-level claims without making the writing unreadable.

Examples:

- Introduction cites representative systems motivating long-form, identity, retrieval, and world-model memory.
- Related Surveys cites long-video, video diffusion, controllable generation, and world-model surveys.
- Section 5 cites StreamingT2V, Echo-Forcing, MemRoPE, Sparse Forcing, OmniMem, and WorldKV for cache and KV memory.
- Section 6 cites RIFLEx, LoL, MemRoPE, and ConsisID for coordinate/spectral memory.
- Section 7 cites StoryDiffusion, ConsisID, AnyID, Slot-ID, SlotMemory, IAMFlow, EM-Vid, VideoMemory, and Memento.
- Section 8 cites Echo-Forcing, LongLive-RAG, OmniMem, WorldKV, IAMFlow, and EM-Vid.
- Section 9 cites WorldMem, SpMem, RELIC, WorldKV, HyDRA, GIM-World, LiveWorld, ReMind, UniDriveDreamer, and HiMem-WAM.
- Section 10 cites MIND, MBench, WorldScore, iWorld-Bench, Echo-Memory, and LVSA/VQeval-style evaluation work.

## 4. Compilation status

Local artifacts:

```text
TMM_Journal_Track_v0.8.0_preview.pdf
TMM_Journal_Track_v0.8.0.zip
```

The PDF compiles successfully with IEEEtran bibliography style. No undefined citations or undefined references remain after BibTeX compilation. The rendered preview has 16 pages.

## 5. Remaining bibliography work

This is a citation-integrated draft, not yet the final bibliography-audited submission. Remaining work:

1. Replace generic author placeholders with official metadata for unresolved entries.
2. Verify every arXiv ID and title against the final PDF or arXiv page.
3. Normalize capitalization and author order.
4. Decide which background papers should remain in the main reference list versus appendix only.
5. Add citation keys to route-level appendix audit tables once those tables are created.

## 6. Next writing tasks

1. Continue expanding Section 2 Related Surveys with a comparison table.
2. Add appendix-level detailed audit tables for each technical route.
3. Continue reducing dense method lists in the main text.
4. Start a dedicated bibliography audit file for mainline/high-support papers.
5. Add the World-State Memory Design Patterns figure if the user provides it.
