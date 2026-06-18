# 38 v0.8.4 Insert New Figures and Expand Audit Tables

> Stage: continue journal-first writing after v0.8.3.  
> Goal: insert the three newly drawn synthesis figures, expand the paper-level audit evidence, and keep moving the manuscript from conceptual framework toward evidence-backed journal survey.

## 1. Inserted figures

v0.8.4 inserts the three newly drawn figures into the TMM journal track:

1. **Memory Failure Taxonomy in Generated Videos**: inserted in Section III to make the failure taxonomy visible and concrete.
2. **Retrieval-Augmented Recall Across Memory Substrates**: inserted in Section VIII to clarify retrieval as an access pipeline across heterogeneous memory stores.
3. **World-State Memory Design Patterns**: inserted in Section IX to summarize common world-state memory modules across spatial maps, latent caches, KV archives, and global hidden states.

These figures directly address the reviewer-style request for more visual and diagnostic evidence. They also reduce the need for overly fragmented bullet lists by converting route-level design patterns into visual synthesis.

## 2. Expanded audit tables

The paper-level audit section is expanded beyond a small sample table. v0.8.4 adds route-specific core audit tables:

- cache-centric token memory audit;
- identity/entity/narrative memory audit;
- retrieval, world-state, and evaluation audit.

These tables cover representative mainline and high-support works including StreamingT2V, MAGI-style chunk memory, Echo-Forcing, MemRoPE, Sparse Forcing, OmniMem, WorldKV, StoryDiffusion, ConsisID, AnyID, Slot-ID, SlotMemory, IAMFlow, EM-Vid, Memento, VideoMemory, LongLive-RAG, WorldMem, SpMem, RELIC, HyDRA, LiveWorld, ReMind, GIM-World, UniDriveDreamer, HiMem-WAM, MIND, MBench, WorldScore, iWorld-Bench, and Echo-Memory.

The audit tables code each method by memory object, substrate or protocol, access/update policy, and main limitation or diagnostic question. This begins to turn the taxonomy into a falsifiable paper-level coding scheme.

## 3. Compilation and rendering status

Local artifacts:

```text
TMM_Journal_Track_v0.8.4_preview.pdf
TMM_Journal_Track_v0.8.4.zip
```

The PDF compiles successfully with no undefined citations or undefined references after repeated LaTeX passes. The rendered preview has 28 pages. Key pages containing the newly inserted figures were rendered and visually checked:

- page 4: memory failure taxonomy;
- page 14: retrieval-augmented recall figure;
- page 17: world-state memory design patterns.

The new figures are readable in the IEEE/TMM two-column layout. Route tables remain dense and should later be converted into full appendix audit tables or split by route if the final journal venue allows a long supplement.

## 4. Remaining work

1. Expand the audit tables from representative core methods to the full coverage corpus.
2. Normalize BibTeX and publication-status labels.
3. Continue replacing list-like method descriptions with paragraph-level comparisons between representative methods.
4. Add a full benchmark audit table with dataset/task/metric/judge/blind-spot fields.
5. Decide whether the world-state design figure replaces the previous world-state staircase or both remain in the long journal version.
