# 25 Conference Benchmark Track and Journal Plan v0.6.9

> Stage: deciding whether the conference version should pivot from a compressed survey to a benchmark/evaluation paper, while keeping the journal version as the main long-form survey.

## 1. Core judgment

A pure 7--8 page conference survey is not strong enough for this project because the field is broad and the paper needs to cover too many memory mechanisms. A better conference strategy is to turn the short version into a **benchmark/evaluation-oriented paper**, while keeping the journal version as a comprehensive survey.

This creates a two-output plan:

1. **Conference paper:** a compact benchmark/evaluation paper on memory in video-generation/world-model systems.
2. **Journal paper:** a comprehensive taxonomy-driven survey with full coverage, mechanism-level synthesis, and extended future directions.

## 2. Why benchmark is a better conference angle

A conference benchmark paper can have a clearer contribution than a compressed survey:

- It defines a concrete task family.
- It releases prompts, protocols, evaluation scripts, and possibly curated input specifications.
- It reports comparative results on accessible models.
- It connects directly to the survey taxonomy but does not need to explain every method.

This also addresses the page-limit problem: the conference paper can focus on one evaluative thesis rather than summarizing the whole literature.

## 3. Echo-Memory as a useful reference pattern

Echo-Memory is useful because it does not simply propose another model. It performs a **controlled study** of memory mechanisms in action-conditioned world models. Its key pattern is:

```text
Fix the action-to-video generation interface.
Control the backbone and generation pipeline.
Vary only the memory mechanism.
Evaluate memory using multiple return/revisit protocols.
```

This is a much stronger conference template than a short survey.

## 4. Our feasible benchmark direction

Because many video-generation/world-model codes are not open-source, the benchmark should avoid depending on training or modifying proprietary models. It should be designed as a **black-box or light-gray-box evaluation benchmark**.

### Possible benchmark title

```text
MemBench-VG: Diagnosing Memory Failures in Video Generation Models
```

or

```text
EchoBench-VG: Return-and-Revisit Evaluation for Video Generation Memory
```

### Core idea

Evaluate whether a model remembers entities, scene layout, attributes, hidden objects, and causal state after the prompt or camera/viewpoint forces a departure and return.

## 5. Benchmark task families

Recommended task families:

1. **Identity return.**
   A subject appears, leaves or changes context, then reappears. Test whether identity attributes persist.

2. **Object permanence / hidden state.**
   An object is placed, hidden, moved off-screen, or occluded. Test whether it reappears consistently.

3. **Scene revisit.**
   A camera leaves a room/street/viewpoint and later returns. Test whether layout and salient objects remain stable.

4. **Attribute-state update.**
   An entity changes state, e.g., holding a key, opening a box, wearing an item. Test whether state updates persist.

5. **Causal return.**
   A previous action changes the environment. Test whether later frames respect the changed state.

6. **Memory budget / degradation.**
   Increase sequence length, number of entities, or return interval. Test where memory collapses.

## 6. Data construction without heavy model training

The benchmark can be built using structured prompts and generated/evaluated clips rather than training data.

### Input format

Each sample can contain:

- initial scene prompt,
- entity list,
- attribute/state list,
- event/action sequence,
- departure interval,
- return query,
- expected memory facts.

### Output format

Generated video plus extracted evidence:

- entity consistency score,
- scene layout score,
- object permanence score,
- state update score,
- causal consistency score,
- memory decay curve.

## 7. Evaluation protocol

Use a three-level evaluation design:

1. **Rule-based checks where possible.**
   Example: object count, color consistency, whether an object is present after return.

2. **Vision-language model judging.**
   Use VLM-based question answering on key frames or clips to assess memory facts.

3. **Human subset validation.**
   A small human-labeled subset validates whether automatic metrics align with human judgment.

The paper can release prompts, metadata, evaluation questions, and scripts even if model generation code is not released.

## 8. What must be open-sourced for a benchmark paper

Even if generation models are not open-source, the benchmark should release:

- benchmark prompts;
- expected memory facts;
- evaluation questions;
- scoring scripts;
- VLM judging prompts;
- sample generated outputs when license allows;
- leaderboard format;
- metadata schema.

This is enough to make the benchmark reproducible at the evaluation level.

## 9. Minimum viable conference experiment

A minimum viable benchmark paper should evaluate:

- 3--5 representative video generation or world-model systems;
- 5--6 memory task families;
- 50--200 benchmark cases, depending on generation cost;
- several return intervals or difficulty levels;
- automatic scoring plus a small human validation set.

## 10. Relationship to existing benchmarks

The conference paper should clearly distinguish itself from:

- MIND: memory consistency and action control in world models;
- MBench: entity/environment/causal memory dimensions;
- Echo-Memory: controlled memory mechanisms in action world models;
- iWorld-Bench: interactive world model tasks;
- WorldScore: world generation evaluation.

Our differentiator should be a **video-generation-model-centered return-and-revisit benchmark** with explicit memory facts and black-box usability.

## 11. Conference contribution statement

Possible conference contribution:

```text
We introduce a black-box memory diagnostic benchmark for video-generation-model-based systems. The benchmark decomposes memory failures into identity return, object permanence, scene revisit, attribute-state update, causal return, and memory-budget degradation. Unlike model-specific studies, our protocol requires no access to model internals and evaluates generated clips through structured memory facts, VLM-based evidence extraction, and human validation. Experiments reveal that models with high short-term visual quality can fail systematic return-and-revisit memory tests.
```

## 12. Journal plan after benchmark pivot

The journal version should absorb the benchmark as one chapter:

```text
Section 10. Memory Evaluation Beyond Surface Consistency
```

The journal paper then becomes stronger because it includes not only a taxonomy, but also an evaluative framework and possibly empirical evidence.

### Revised journal contribution

The journal paper should claim:

1. a memory-system taxonomy;
2. full literature coverage;
3. mechanism-level comparison;
4. benchmark/evaluation synthesis;
5. a proposed or preliminary diagnostic benchmark;
6. open problems and research agenda.

## 13. Recommended next steps

1. Keep the journal survey as the main long-term paper.
2. Create a small benchmark specification document.
3. Define 30--50 pilot cases across identity, scene revisit, object permanence, and state update.
4. Run pilot evaluation on accessible systems.
5. Expand to 100--200 cases if results are promising.
6. Convert the conference paper into a benchmark/evaluation paper rather than a compressed survey.

## 14. Decision

The best strategy is:

```text
Conference: benchmark/evaluation paper inspired by Echo-Memory.
Journal: comprehensive survey + benchmark synthesis.
```

This avoids the weakness of an under-sized conference survey and prevents the journal paper from becoming a literature list.
