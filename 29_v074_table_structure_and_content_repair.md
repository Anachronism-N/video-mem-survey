# 29 v0.7.4 Table, Structure, and Content Repair Plan

> Stage: response to review of v0.7.3 TMM preview.  
> Goal: explain why the current TMM preview became shorter, diagnose table-layout problems, clarify the Section 5 / Section 8 boundary, and use the high world-model ratio to strengthen motivation.

## 1. Why v0.7.3 became much shorter

The v0.7.3 PDF is not the full journal manuscript. It is a **TMM/IEEEtran skeleton preview** used to test layout, tables, section flow, and figure/table behavior. It only merged the newly deepened sections and selected route tables. It did not copy the full long draft into the journal source.

Therefore, the shorter length does not mean the previous long-form content was discarded. It means the project currently has two layers:

1. **Long working draft / material bank**: full explanations, figures, route notes, coverage table, and supplementary content.
2. **TMM skeleton preview**: a compact IEEE-style source where polished sections are gradually inserted.

Next step: restore the long-form journal content into the TMM track progressively, but only after each section has been rewritten in mechanism-level style.

## 2. Why the current tables look wrong

The current tables are visually poor because they try to fit too many columns into a single IEEE two-column page. The failure modes are:

- Long method names are forced into narrow columns.
- Evaluation implication text wraps into tall, unreadable vertical blocks.
- Tables use too many analytic dimensions at once.
- The row height becomes excessive.
- The table looks like a compressed spreadsheet rather than a journal-level comparison table.

This is a design problem, not just a LaTeX formatting issue.

## 3. Table repair strategy

Each route table should be split into two levels:

### Main-text compact table

Purpose: high-level mechanism comparison.

Recommended columns:

```text
Mechanism group | Memory object | Substrate | Lifecycle | Training regime | Representative methods
```

This should fit in a two-column or page-width table with readable text.

### Appendix detailed table

Purpose: audit-level evidence.

Recommended columns:

```text
Method | Memory object | Substrate | Lifecycle | Training regime | Key limitation | Evaluation implication | Citation | Verification status
```

This can be longer and may use landscape or supplementary formatting.

## 4. How to repair Table 1--3 immediately

### Token/KV table

Current problem: evaluation implications are too long for a compact table.

Fix:

- Move detailed evaluation implications to Appendix table.
- Keep only mechanism group, object, substrate, lifecycle, training regime, and methods in the main table.
- Use mechanism groups rather than long prose.

### Retrieval table

Current problem: it overlaps conceptually with Token/KV retrieval and may repeat OmniMem / WorldKV.

Fix:

- Define retrieval table by **retrieval interface**, not substrate.
- Rows should be: latent retrieval, KV retrieval, scene recall, entity-conditioned retrieval, external corpus retrieval, conflict filtering.
- Methods that also appear in Section 5 should be marked as cross-route examples, not re-explained.

### World-state table

Current problem: it should be the strongest table but currently risks becoming another method list.

Fix:

- Group by state type: static layout, latent spatial state, KV world memory, hidden subject state, geometry-aware memory, action-conditioned state.
- Keep method names short in the main text.
- Put long explanations into Appendix.

## 5. Does the high proportion of world-model papers affect motivation?

Yes. It should strengthen the motivation rather than distort it.

The current literature distribution shows that many recent papers in the corpus are world-model or world-state related. This implies that the field is moving from **visual continuity** to **state persistence**. The survey should explicitly use this as evidence for the core thesis:

```text
The memory problem becomes most visible when video generation is expected to behave like a world model: entities leave the field of view, scenes are revisited, actions change states, and hidden variables must continue evolving.
```

However, the paper should not become only a world-model survey. Instead, the world-model concentration should be used as the **endpoint of the narrative**:

```text
Token/KV memory -> positional/spectral memory -> identity/entity memory -> retrieval memory -> world-state memory
```

This makes world-state memory the strongest motivation and the final synthesis point, while preserving the broader video-generation-memory scope.

## 6. Are Section 5 and Section 8 repetitive?

Yes, there is real overlap in the current draft.

The boundary should be:

### Section 5: Token/KV/Attention Memory

Focus:

```text
Where is historical evidence stored inside or near the transformer, and how is it retained, compressed, routed, or budgeted?
```

Main objects:

- visual tokens,
- KV cache,
- sink/anchor tokens,
- memory tokens,
- sparse blocks,
- per-head cache,
- quantized/offloaded cache.

Methods such as OmniMem and WorldKV appear here only as examples of historical KV access.

### Section 8: Retrieval-Augmented Recall

Focus:

```text
How does the generator actively select relevant memory from an indexed source and inject it into current generation?
```

Main interfaces:

- query construction,
- indexing,
- retrieval,
- conflict filtering,
- ranking,
- injection,
- update.

Methods such as OmniMem and WorldKV can be cross-referenced, but Section 8 should mainly discuss the **retrieval paradigm** across substrates: latent banks, scene recall frames, entity-indexed memory, external corpora, and KV archives.

## 7. Possible structural decision

Two options are possible:

### Option A: Keep Section 8 independent

Use this if retrieval-augmented generation becomes a major route with enough unique material.

Section 8 title:

```text
Retrieval-Augmented Recall Across Memory Substrates
```

### Option B: Merge Section 8 into other sections

Use this if redundancy remains high.

- KV retrieval goes to Section 5.
- Entity retrieval goes to Section 7.
- Scene/world retrieval goes to Section 9.
- A short cross-route subsection remains in Section 11.

Current recommendation: keep Section 8 for now, but rewrite it around retrieval interface rather than method list.

## 8. Content repair actions for v0.7.4

1. Rebuild Table 1--3 into compact main-text tables.
2. Move detailed evaluation implications to appendix-level tables.
3. Restore more long-form journal content into the TMM track.
4. Strengthen motivation around the world-model-heavy literature distribution.
5. Rewrite Section 5 and Section 8 boundary paragraphs.
6. Add a paragraph explaining why world-state memory is the endpoint of the survey narrative.
7. Continue deepening Section 7 rather than adding more new sections.

## 9. Figure implication

The table problem also confirms the figure strategy:

- Use figures to explain structure and mechanism flow.
- Use compact tables for main-text comparison.
- Use supplementary tables for exhaustive evidence.

New figures should only be added if they compress many methods into a common mechanism pattern. The strongest next figure remains:

```text
World-State Memory Design Patterns
```

A retrieval figure is useful only if Section 8 remains independent after rewriting.
