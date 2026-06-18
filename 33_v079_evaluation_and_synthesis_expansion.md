# 33 v0.7.9 Evaluation and Synthesis Expansion

> Stage: continue journal-first writing after expanding Section 6 in v0.7.8.  
> Goal: make the manuscript less thin by expanding Introduction, Evaluation, and Cross-Route Synthesis, while adding formulas, protocols, and tables.

## 1. Main update

v0.7.9 addresses the concern that the current TMM journal draft is still too thin. The main expansion is not more method listing, but more analytical connective tissue:

- stronger Introduction and motivation;
- full Section 10 evaluation synthesis;
- expanded Section 11 cross-route synthesis and open problems;
- additional formulas for memory facts and memory decay;
- route-specific evaluation protocol table;
- pseudo-algorithmic view of memory-aware evaluation;
- cross-route design-pattern table.

## 2. Introduction expansion

The Introduction now explicitly motivates the field's movement from visual continuity to state persistence. It argues that world-model-like video generation exposes the strongest form of memory requirement: identities, objects, spatial layouts, hidden states, and action consequences must persist beyond local frame quality.

The Introduction also clarifies why the survey is not simply about long context. It frames cache, position, identity, retrieval, and world-state mechanisms as interacting parts of a memory system.

## 3. Section 10 expansion: Memory Evaluation Beyond Surface Consistency

Section 10 has been expanded from a short paragraph into a full evaluation synthesis chapter.

New components:

### Memory facts

A memory-aware evaluation begins with explicit memory facts:

```tex
F=\{f_1,\ldots,f_n\}
```

A generic diagnostic interface is written as:

```tex
\mathrm{MemScore}(V_{1:T},F)=\frac{1}{|F|}\sum_{f_i\in F}\omega_i\,\mathrm{Check}(V_{1:T},f_i)
```

This is not claimed as a new benchmark. It is a conceptual interface for explaining why visual quality and memory correctness differ.

### Memory decay

A return-gap diagnostic is added:

```tex
\Delta_{mem}(k)=\mathrm{MemScore}(V_{1:t},F)-\mathrm{MemScore}(V_{1:t+k},F)
```

This explains how memory should be evaluated under increasing return intervals, entity counts, and distractor events.

### Route-specific protocols

A new table maps each technical route to diagnostic protocols, queried memory facts, typical failures, and metric caveats.

### Pseudo-algorithmic evaluation view

A new pseudo-algorithmic table summarizes:

- register facts;
- create probes;
- generate evidence;
- check facts;
- aggregate dimension-wise results;
- audit error types.

## 4. Section 11 expansion: Cross-Route Synthesis and Open Problems

Section 11 now synthesizes the technical routes through several design patterns:

- budgeted retention;
- coordinate-valid reuse;
- persistent identity with revisable state;
- query-conditioned recall;
- state-transition memory.

A new cross-route design-pattern table compares where each pattern appears, its core design question, main risk, and evaluation signal.

The open problems are now expanded into:

1. active recall instead of passive retention;
2. memory revision and forgetting;
3. interpretable memory substrates;
4. training-free versus trained memory;
5. evaluation that penalizes false memory.

## 5. Output status

Local artifacts:

```text
TMM_Journal_Track_v0.7.9_preview.pdf
TMM_Journal_Track_v0.7.9.zip
```

The PDF compiles successfully and has been rendered for visual checking. The manuscript is now 15 pages. The newly added evaluation and synthesis tables are readable in the rendered preview, although detailed appendix audit tables are still needed in later versions.

## 6. Next writing tasks

1. Add appendix-level detailed audit tables for each route.
2. Expand Section 2 Related Surveys to more clearly differentiate this article from long-video, controllable-generation, consistency, and world-model surveys.
3. Normalize BibTeX for mainline and high-support methods.
4. Add or request the optional World-State Memory Design Patterns figure.
5. Continue revising tables to reduce dense method lists in the main text.
