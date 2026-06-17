# LiveWorld: Simulating Out-of-Sight Dynamics in Generative Video World Models

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.07145
- URL: https://arxiv.org/abs/2603.07145
- Category: S7 Video world model memory 
- Priority: Must-read
- Training-free: Trained/system
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

LiveWorld formalizes out-of-sight dynamics: objects should continue evolving when unobserved, not freeze in observational memory.

## 3. Problem / failure mode

Existing video world models implicitly assume the world evolves only inside the field of view; revisits fail to reflect unseen events.

## 4. Memory object

- out-of-sight dynamic world state

## 5. Memory substrate

- persistent global state: static 3D background + dynamic entities

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes static 3D background and dynamic entities into persistent global state. |
| Store | Persistent global state with static/dynamic decomposition. |
| Retrieve | On revisit, synchronizes evolved dynamic entity state for spatially coherent rendering. |
| Use | Monitor-based mechanism simulates temporal progression of active entities while unobserved. |
| Update | Dynamic entities continue evolving autonomously and are synchronized on revisit. |
| Forget | Not central; persistent evolution rather than forgetting. |
| Evaluate | Introduces LiveBench for maintaining out-of-sight dynamics. |

## 7. Strengths for this survey

Most important paper for world-state memory and hidden-state evolution.

## 8. Limitations / second-pass PDF checks

World-model-specific; not directly a T2V identity baseline.

## 9. Recommended placement

- Main category: S7 Video world model memory 
- Role: out-of-sight dynamics 核心论文：世界不可见时也应继续演化。
- Priority: Must-read
