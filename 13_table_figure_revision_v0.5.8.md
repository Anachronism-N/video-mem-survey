# 13 Table and Figure Revision v0.5.8

> Stage: response to review comments on v0.5.7.  
> Goal: restore top-conference-level survey apparatus: complete Figure 4 design, necessary high-quality tables, and formal mechanism descriptions for Sections 5--7.

## 1. Corrections from v0.5.7

The v0.5.7 working draft had three problems:

1. Figure 4 prompt listed only a small subset of related papers and could not support a complete method-landscape figure.
2. Tables were removed rather than audited and improved.
3. Sections 5--7 contained prose but lacked mechanism-level tables and formal definitions.

v0.5.8 corrects these issues.

## 2. Figure 4 design principle

Figure 4 should be a survey-grade method landscape, not a sparse illustration. It should follow a design pattern common in mature survey papers:

- A figure provides a navigable map.
- Rows represent high-level technical routes.
- Columns represent lifecycle phases.
- Cells contain compact method-family chips.
- Tables provide the full details, citations, and method-level comparisons.

Thus Figure 4 should not try to include long explanations. It should be visually compact but method-complete.

## 3. Revised Figure 4 prompt

Use the full prompt in:

```text
latex/figures/FIGURE4_COMPLETE_PROMPT_v0.5.8.md
```

The prompt now includes substantially more methods and families:

- StreamingT2V.
- LongLive.
- Rolling/Causal/Self-Forcing.
- Echo-Forcing.
- MemRoPE.
- Deep Forcing.
- Pyramid Forcing.
- Sparse Forcing.
- Future Forcing.
- KV Cache Quantization.
- LongLive-RAG.
- OmniMem.
- RIFLEx.
- LoL.
- Infinity-RoPE.
- FreeLong / FreeLong++.
- StoryDiffusion.
- ConsisID.
- AnyID.
- Slot-ID.
- SlotMemory.
- EM-Vid.
- IAMFlow.
- Memento.
- CoTriSyGen.
- EntityBench / EntityMem.
- WorldMem.
- SpMem.
- Mirage.
- LiveWorld.
- ReMind.
- MIND.
- MBench.
- WorldScore.
- iWorld-Bench.
- NarraStream-Bench.

## 4. Table policy

Do not delete all tables. Instead, keep only tables that perform a real survey function.

### Required tables

1. Route-by-lifecycle matrix: shows global organization.
2. Token/KV/attention memory table: compares memory substrates and lifecycle roles.
3. Positional/spectral memory table: compares coordinate/frequency mechanisms.
4. Identity/entity/narrative memory table: compares reference, entity, and narrative memory.
5. Evaluation benchmark table: to be added in the next pass.
6. Spatial/world-state memory table: to be added in the next pass.

### Tables to avoid

- Tables that only repeat subsection names.
- Tables with vague labels such as “good / bad / medium.”
- Tables without citations.
- Tables that are too small to be useful.
- Tables that mix verified and unresolved papers without status flags.

## 5. Formalism policy

Current sections should contain enough formalism to clarify concepts, but not heavy math. The following lightweight interface is now used:

```text
Register:  z_t = Reg(x_<=t, c_t)
Maintain:  M_t = Maint(M_{t-1}, z_t; B_t)
Access:    a_t = Access(q_t, M_t)
Apply:     y_{t+1} = Gen(q_t, a_t)
Revise:    M_{t+1} = Revise(M_t, y_{t+1}, e_{t+1})
```

A budgeted memory objective is also introduced:

```text
M*_t = argmax_{cost(M) <= B_t} U(M; q_t) - lambda R(M)
```

This is not intended as a new model. It is a common interface for comparing token caches, identity memories, retrieval banks, and spatial memories.

## 6. v0.5.8 draft changes

The v0.5.8 working draft adds:

- Formal memory interface in Section 4.
- Route-by-lifecycle matrix.
- Mechanism table for Section 5.
- Mechanism table for Section 6.
- Mechanism table for Section 7.
- Revised Figure 4 prompt in the draft appendix/section.
- Expanded citations in tables and text.

## 7. Remaining work

Next pass should add:

- High-quality Section 8 retrieval table.
- High-quality Section 9 spatial/world-state memory table.
- High-quality Section 10 benchmark table.
- Official AAAI template migration once the official author kit files are available.
- Final BibTeX normalization for all A/B-grade papers.
