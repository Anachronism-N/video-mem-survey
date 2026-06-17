# 20 v0.6.5 Figures and Supplementary Coverage Table

> Stage: integrate drafted figures, create the first full supplementary coverage table, and continue polishing the paper draft.

## 1. Figure integration

The v0.6.5 working draft inserts the uploaded figures into the LaTeX paper source:

- Figure 1: memory systems overview.
- Figure 2: memory failures and requirements.
- Figure 3: three-layer taxonomy of video memory.
- Figure 4: lifecycle subway map as the preferred non-table method landscape.
- Alternative Figure 4: radial lifecycle view retained for design comparison.
- Figure 5: evaluating memory beyond surface consistency.
- Figure 6: implicit token memory in attention and KV caches.
- Figure 7: identity/entity/narrative memory.
- Figure 8: visual continuity to world-state persistence.
- Figure 9: emergence timeline.
- Figure 10: benchmark/evaluation matrix.

Current recommendation: use the lifecycle subway map as the main Figure 4, keep the radial version as backup or supplementary material, and keep the LaTeX method landscape matrix as an auditable table/appendix.

## 2. Supplementary coverage table

A first supplementary coverage table has been generated as:

```text
supplementary_coverage_v0.6.5.csv
```

Current row count:

- 100 records from the existing local `papers_master.csv`.
- 8 newly added or promoted records from the v0.6.3--v0.6.4 world-memory update.
- 108 total records.

This table intentionally exceeds the earlier 102-paper target because it keeps later additions rather than dropping them. In the next pass, it should be reconciled against the restored 102-note archive and the newest world-model additions to remove duplicates and mark unresolved entries.

## 3. Coverage columns

The table includes:

- coverage_id
- paper
- year
- id
- primary_route
- memory_object
- memory_substrate
- lifecycle_focus
- training_regime
- role_tier
- discussion_role
- url
- verification_status
- source

## 4. Remaining polish tasks

Next pass should:

- Reconcile the 108-row current table with the original 102-note corpus.
- Normalize all main-table references into BibTeX.
- Convert Figure 10 into a LaTeX table if page budget becomes tight.
- Decide whether both Figure 4 variants should remain, or only the subway map should be used in the main paper.
- Continue compressing prose because the figure-integrated PDF is now substantially longer.
- Audit all figures for text readability after switching to the official AAAI author kit.
