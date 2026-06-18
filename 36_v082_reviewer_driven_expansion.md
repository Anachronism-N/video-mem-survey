# 36 v0.8.2 Reviewer-Driven Expansion

> Stage: continue journal-first writing after v0.8.1.  
> Goal: respond to reviewer-style feedback that the draft has too many short points, insufficient method-level evidence, and weak survey-systematicity.

## 1. Main update

v0.8.2 expands the TMM journal track from a framework-heavy draft into a more evidence-oriented survey draft. The main change is not simply adding more text. The revision adds stronger definitions, more method-level comparisons, survey methodology, failure taxonomy, benchmark audit, and paper-level coding examples.

## 2. Added operational definition

The revision adds a sharper definition of video-generation memory. A method is treated as memory-relevant only if it satisfies operational criteria:

- it registers information from a past prompt, reference, generated frame, action, entity, or chunk;
- the information remains accessible beyond the immediate local context;
- it influences later generation, conditioning, retrieval, or evaluation;
- it has some identifiable storage, access, update, compression, or validation policy.

Negative cases are now discussed explicitly. Ordinary short-context temporal attention, one-shot reference conditioning, and generic temporal smoothing are not automatically treated as full memory mechanisms.

## 3. Added survey methodology

Section 2 now contains a survey methodology and coding protocol. Papers are coded by memory object, substrate, lifecycle phase, training regime, primary route, and secondary route. This addresses the concern that the taxonomy should look like a coded literature map rather than a subjective grouping.

## 4. Expanded technical-route details

The revision adds more detailed method-level analysis in the major technical sections:

- Section 5 expands StreamingT2V, MAGI-style chunk generation, self-forcing/causal rollout, Echo-Forcing, MemRoPE, Sparse Forcing, OmniMem, and WorldKV.
- Section 7 expands StoryDiffusion, ConsisID, AnyID, Slot-ID, SlotMemory, IAMFlow, EM-Vid, and Memento.
- Section 8 expands retrieval strategies over scene recall frames, latent banks, KV archives, entity-indexed memories, and external references.
- Section 9 expands the hierarchy from visual scene memory to spatial/geometric memory, object permanence, causal state, and action-conditioned interactive memory.

## 5. Added new tables

New tables added in v0.8.2:

- operational memory definition table;
- failure-to-requirement table;
- training-regime table;
- cache-priority instantiation table;
- retrieval failure matrix;
- benchmark audit table;
- cross-route multi-label coding table;
- sample paper-level audit table.

The intent is to support the taxonomy with concrete paper-level and route-level evidence.

## 6. Evaluation expansion

Section 10 now includes a benchmark-level comparison and a diagnostic example involving a red mug, camera departure, action update, and return state. This is used to explain why generic visual quality metrics can miss memory errors.

## 7. Compilation status

Local artifacts:

```text
TMM_Journal_Track_v0.8.2_preview.pdf
TMM_Journal_Track_v0.8.2.zip
```

The PDF compiles successfully with no undefined citations or undefined references after repeated LaTeX passes. The rendered preview has 23 pages.

## 8. Remaining work

1. Expand the sample paper-level audit table to the full corpus.
2. Normalize BibTeX metadata and remove placeholder author entries before submission.
3. Add visual failure examples or a World-State Memory Design Patterns figure.
4. Continue replacing dense method lists with detailed mechanism comparison paragraphs.
5. Add publication-status labels for arXiv preprints, technical reports, and peer-reviewed papers.
