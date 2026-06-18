# 23 v0.6.7 Venue Strategy

> Goal: decide where to submit the AAAI conference version and the longer journal/full-length version.

## 1. Overall recommendation

Use a dual-track strategy:

1. **AAAI version**: a selective 7-page conference paper that argues for the memory-system view and presents a compact taxonomy, representative method routes, and a memory-aware evaluation agenda.
2. **Journal/full version**: a comprehensive survey article with full coverage tables, more figures, detailed route-level analysis, and extended future directions.

The AAAI version should not read like a traditional exhaustive survey. The journal version can be exhaustive and pedagogical.

## 2. Best-fit journal targets

### First choice: ACM Computing Surveys (CSUR)

Best fit if the final manuscript becomes a comprehensive, taxonomy-driven survey with complete coverage and strong tutorial value.

Why suitable:

- It is dedicated to survey and tutorial articles.
- It can accommodate a long, detailed paper.
- It rewards systematic coverage, conceptual taxonomy, and high-quality references.

Risk:

- The bar for completeness and citation accuracy is extremely high.
- We need normalized BibTeX, a verified coverage table, and a polished taxonomy.

### Strong domain-specific options

#### IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)

Potential fit if the manuscript is framed as a computer vision / video generation / world modeling survey with strong technical synthesis.

Risk: difficult for a pure survey unless the paper makes a strong analytical contribution and is very rigorous.

#### International Journal of Computer Vision (IJCV)

Potential fit if the paper is positioned as a vision-centric review of video generation, consistency, world models, and evaluation.

Risk: journal fit depends on whether the manuscript is sufficiently computer-vision focused rather than broad AI/multimedia.

#### IEEE Transactions on Multimedia (TMM)

Good fit if the paper emphasizes multimedia generation systems, video generation, video benchmarks, deployment regimes, and practical evaluation.

Risk: may prefer technical multimedia contributions over very broad survey/tutorial manuscripts, depending on editorial judgment.

#### IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)

Good fit if the paper emphasizes video technology, long-video generation, memory/compression/cache budget, streaming generation, and evaluation.

Risk: less ideal if the paper becomes too broad on AI/world-model philosophy.

#### ACM TOMM

A reasonable multimedia venue if the final manuscript is multimedia-system oriented. Less ideal than CSUR if the goal is a flagship survey article.

## 3. Conference target: AAAI

AAAI can work if the paper is not framed as an ordinary literature survey. It should be framed as an integrative, conceptually novel paper that introduces a new memory-system lens for video generation models.

AAAI version should emphasize:

- A crisp thesis: long-horizon and interactive video generation is a structured memory problem.
- A compact taxonomy: memory object, memory substrate, memory lifecycle, training regime.
- A method landscape: technical routes with lifecycle phases.
- A diagnostic evaluation agenda: beyond surface consistency.
- A comprehensive supplement proving coverage.

## 4. Practical ranking

### If prioritizing acceptance and fit

1. IEEE TMM or TCSVT.
2. IJCV if vision framing becomes stronger.
3. ACM TOMM.
4. CSUR if the paper becomes fully mature and exhaustive.

### If prioritizing prestige for a survey

1. ACM Computing Surveys.
2. TPAMI / IJCV.
3. IEEE TMM.
4. TCSVT / ACM TOMM.

### If prioritizing the user's near-term deadline

1. AAAI conference version first.
2. Journal full version in parallel.
3. Submit journal version after AAAI submission or after arXiv release.

## 5. Current project-specific judgment

The most natural final home for the long version is **ACM Computing Surveys** if we can complete citation verification and coverage auditing. The most realistic domain-specific journal alternatives are **IEEE TMM** and **TCSVT**. TPAMI/IJCV are possible but require the article to be more sharply positioned around computer vision and video/world-model evaluation.

For AAAI, the paper must become much more selective. It should not attempt to summarize every method in the main text; instead, it should present the memory-system perspective as a new integrative lens and place full coverage in supplementary material.

## 6. Immediate writing implication

- AAAI version: compress, argue, select.
- Journal version: expand, compare, document.
- Supplement: verify, audit, cover all papers.

The full journal track should preserve long-form material rather than losing it during AAAI compression.
