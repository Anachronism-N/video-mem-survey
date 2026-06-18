# 31 v0.7.6 Formulas, Pseudocode, and Section Expansion

> Stage: continue journal-first writing after the Section 5 / Section 8 boundary repair.  
> Goal: add analytical formulas and pseudo-algorithmic support in the right places, while continuing manuscript expansion.

## 1. Main update

v0.7.6 keeps the revised boundary:

```text
Section 5 = cache as memory substrate
Section 8 = retrieval as memory access strategy
```

It then adds formulas and pseudo-algorithmic blocks to support this distinction.

## 2. Section 5 additions

Section 5 now includes a cache-centric formal interface.

The cache is decomposed as:

```tex
\mathcal{C}_t = (\mathcal{C}^{act}_t, \mathcal{C}^{arc}_t, \mathcal{C}^{sum}_t)
```

where the active cache is directly visible to attention, the archived cache stores evicted but recoverable history, and the summary cache stores compressed anchors, sink states, or memory tokens.

A generic cache policy is written as:

```tex
\pi_C: (\mathcal{C}_{t-1}, z_t, p_t, B_t) \mapsto (\mathcal{C}_t, E_t)
```

A cache priority score is also added:

```tex
\rho_i = \alpha r_i + \beta s_i + \gamma u_i - \delta c_i - \eta o_i
```

This score interprets cache design in terms of recency, salience, predicted utility, cost, and obsolescence/conflict.

## 3. Section 5 pseudocode

v0.7.6 adds:

```text
Pseudo-algorithmic view of cache-centric memory maintenance
```

The pseudo-algorithm abstracts:

- register new tokens;
- score cache units;
- keep/archive/summarize entries;
- enforce budget through quantization/pruning/offloading;
- expose selected cache to attention;
- revise stale anchors and positional indices.

This supports the argument that cache policies are memory operations, not merely efficiency tricks.

## 4. Section 8 additions

Section 8 now includes a retrieval-centric formal interface.

A retrieval set is defined as:

```tex
R_t = \operatorname{TopK}_{m_i\in\mathcal{B}} S(q_t,m_i;\theta)
```

The retrieval score is decomposed as relevance, state match, age penalty, conflict penalty, and cost:

```tex
S(q_t,m_i)=\lambda_1 sim(q_t,m_i)+\lambda_2 match(q_t,m_i)-\lambda_3 age(m_i)-\lambda_4 conflict(q_t,m_i)-\lambda_5 cost(m_i)
```

The injection operator is written as:

```tex
\tilde{q}_t = \Phi(q_t,R_t), \quad y_{t+1}=G(\tilde{q}_t)
```

This clarifies that retrieval is not just storing more cache. It is an access policy that decides what evidence is relevant and valid for the current query.

## 5. Section 8 pseudocode

v0.7.6 adds:

```text
Pseudo-algorithmic view of retrieval-augmented recall
```

The pseudo-algorithm abstracts:

- build retrieval keys;
- search candidate stores;
- rank candidates;
- filter stale or contradictory memory;
- inject selected memory;
- generate the next segment;
- write back new evidence.

Cache is included as one candidate memory source, but not as the whole retrieval story.

## 6. Section 7 additions

Section 7 now includes a structured entity-memory interface:

```tex
\mathcal{E}_{i,t}=(id_i, v_i, a_{i,t}, r_{i,t}, h_{i,t})
```

where identity, visual embedding, attributes, relations, and evidence history are separated. The update rule:

```tex
\mathcal{E}_{i,t+1}=U(\mathcal{E}_{i,t}, \Delta a_{i,t}, \Delta r_{i,t}, \epsilon_{i,t+1})
```

makes explicit that identity should remain persistent while attribute and relation states remain revisable.

A simple entity consistency score is added to separate identity consistency, attribute accuracy, relation accuracy, and duplication penalty.

## 7. Output status

Local artifacts:

```text
TMM_Journal_Track_v0.7.6_preview.pdf
TMM_Journal_Track_v0.7.6.zip
```

The PDF compiles successfully and has been rendered for visual checking. The new formulas and pseudo-algorithm tables are readable in the IEEE/TMM two-column format. A minor overfull warning remains from one long equation but does not visibly damage the PDF; it can be further polished later.

## 8. Next writing tasks

1. Repair and compact the identity/entity/narrative table.
2. Repair and compact the world-state table.
3. Continue expanding Section 7 around mechanism groups and verification loops.
4. Add appendix-level detailed audit tables for limitations and evaluation implications.
5. Strengthen the introduction using the world-model-heavy literature distribution as evidence that the field is moving from visual continuity to state persistence.
6. Start normalizing BibTeX entries for all mainline methods used in the TMM source.
