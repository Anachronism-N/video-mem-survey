# Pyramid Forcing

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.13111
- URL: https://arxiv.org/abs/2605.13111
- Category: S3 Positional / RoPE memory 
- Priority: Must-read
- Training-free: Yes
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

Pyramid Forcing makes attention-head heterogeneity central: Anchor, Wave, and Veil heads have different temporal dependencies and therefore need different KV policies.

## 3. Problem / failure mode

Unified historical-frame retention assumes homogeneous dependencies across attention heads and causes long-term degradation.

## 4. Memory object

- long-horizon temporal coordinates

## 5. Memory substrate

- dynamic RoPE remap + head-aware cache

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Profiles attention heads offline and writes history into heterogeneous head-aware cache structures. |
| Store | Ragged/pyramidal KV cache with behavior-specific cache lengths and policies. |
| Retrieve | Anchor heads access broad context; Wave heads retrieve periodic dependencies; Veil heads focus on initial/adjacent frames. |
| Use | Improves long-horizon generation quality on Self Forcing and Causal Forcing. |
| Update | Cache is updated according to head type rather than global FIFO policy. |
| Forget | Implicit through per-head cache policy and retention budgets. |
| Evaluate | VBench-Long; reported 60s Self Forcing score improvement from 77.87 to 81.21. |

## 7. Strengths for this survey

Core reference for head/layer-specialized memory and a natural precursor to identity/motion/layout head routing.

## 8. Limitations / second-pass PDF checks

Head types are temporal roles, not explicit semantic roles such as identity/entity/layout.

## 9. Recommended placement

- Main category: S3 Positional / RoPE memory 
- Role: 将位置 remap 和 head-aware cache 结合。
- Priority: Must-read
