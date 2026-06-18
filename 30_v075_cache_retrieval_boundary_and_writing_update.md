# 30 v0.7.5 Cache/Retrieval Boundary and Writing Update

> Stage: response to feedback on Section 5 / Section 8 overlap and continued journal writing.  
> Goal: clarify that Section 5 should focus on cache configuration and generic cache-use methods, while Section 8 should focus on retrieval strategies over existing caches or memory stores.

## 1. Revised boundary

The revised boundary is:

```text
Section 5 = cache as memory substrate
Section 8 = retrieval as memory access strategy
```

Section 5 should answer:

```text
How is cache configured, maintained, compressed, indexed, and made usable as an implicit memory substrate?
```

Section 8 should answer:

```text
Given one or more memory stores, how does the generator construct a query, retrieve relevant evidence, filter conflicts, inject the result, and update memory?
```

This means Section 8 can rely on cache, but it should not repeat the cache-setting discussion. KV retrieval methods can appear in both sections with different roles:

- In Section 5, they illustrate archived cache organization.
- In Section 8, they illustrate retrieval policy and query design.

## 2. Section 5 rewrite

Section 5 has been rewritten as **Cache-Centric Token Memory in Attention and KV States**.

It now focuses on:

- active cache, archived cache, and summary cache;
- temporal scope;
- cache granularity;
- layer/head specificity;
- anchor and sink allocation;
- compression and offloading;
- positional validity;
- cache policies as generic memory operations.

The section explicitly avoids over-expanding retrieval, leaving query construction, ranking, filtering, and injection to Section 8.

## 3. Section 8 rewrite

Section 8 has been rewritten as **Retrieval-Augmented Recall Across Memory Substrates**.

It now focuses on:

- retrieval as an access policy;
- query construction;
- candidate memory sources;
- index structure;
- ranking and conflict filtering;
- injection interface;
- write-back and revision.

The section treats cache as one possible memory source, alongside latent banks, scene recall frames, entity-indexed memory, prompt-derived fact tables, and external visual corpora.

## 4. Table repair

The previous table format was too dense for IEEE/TMM two-column reading. v0.7.5 rebuilds the Section 5 and Section 8 tables as compact main-text mechanism tables.

### New Table 1

Focus: cache-setting axes.

Columns:

```text
Cache-setting axis | Typical configuration | Memory role | Representative methods / families | Main risk
```

### New Table 3

Focus: retrieval decisions.

Columns:

```text
Retrieval decision | Common strategies | Retrieved evidence | Representative methods / families | Main risk
```

Long evaluation implications should be moved to appendix-level audit tables rather than squeezed into the main text.

## 5. Current output

Local artifacts:

```text
TMM_Journal_Track_v0.7.5_preview.pdf
TMM_Journal_Track_v0.7.5.zip
```

The PDF compiles successfully and has been rendered for visual checking. The new Table 1 is much more readable than the previous tall multi-column table. Some older route tables, especially identity/entity and world-state tables, should be repaired in the next pass using the same compact-main-table plus detailed-appendix-table strategy.

## 6. Next writing tasks

1. Repair the identity/entity/narrative table using the same compact format.
2. Repair the world-state table or move detailed diagnostics to appendix.
3. Continue deepening Section 7.
4. Strengthen motivation by using the high proportion of world-model papers as evidence that the field is moving from visual continuity to state persistence.
5. Add appendix-level detailed audit tables for evaluation implications, citations, and verification status.
