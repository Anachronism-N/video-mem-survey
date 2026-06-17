# MIND: Benchmarking Memory Consistency and Action Control in World Models

## 1. Metadata

- Year: 2026
- ID: arXiv:2602.08025
- URL: https://arxiv.org/abs/2602.08025
- Category: S7 Video world model memory 
- Priority: Must-read
- Training-free: N/A
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

MIND is a benchmark rather than generation method; it explicitly evaluates memory consistency and action control in open-domain closed-loop revisits.

## 3. Problem / failure mode

World models lack a unified benchmark for remembering and predicting dynamic visual environments under control.

## 4. Memory object

- memory consistency + action control

## 5. Memory substrate

- benchmark / closed-loop revisiting

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | N/A method; benchmark constructs closed-loop revisited evaluation settings. |
| Store | N/A; evaluates whether model memory is consistent across viewpoints/actions. |
| Retrieve | N/A; tests whether model recalls context under revisits. |
| Use | Used to evaluate world models and MIND-World baseline. |
| Update | N/A benchmark. |
| Forget | N/A benchmark; reveals forgetting failures. |
| Evaluate | 250 high-quality 1080p 24FPS videos; first-person/third-person clips, shared and varied action spaces; memory consistency and action control. |

## 7. Strengths for this survey

Essential evaluation reference for world-model memory.

## 8. Limitations / second-pass PDF checks

Focuses world models, not standard T2V/I2V.

## 9. Recommended placement

- Main category: S7 Video world model memory 
- Role: world model memory 评测核心 benchmark。
- Priority: Must-read
