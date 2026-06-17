# RELIC: Real-time Long Context Interactive World Models

## 1. Metadata

- Year: 2025
- ID: arXiv:2512.04040
- URL: https://arxiv.org/abs/2512.04040
- Category: S7 Video world model memory 
- Priority: Must-read
- Training-free: Trained/system
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

RELIC unifies real-time long-horizon streaming, spatial memory and action control by encoding compressed historical latent tokens with relative actions and absolute camera poses inside the KV cache.

## 3. Problem / failure mode

Interactive world models need real-time streaming, spatial memory and precise control simultaneously, but long-term memory often hurts performance.

## 4. Memory object

- interactive long-context memory

## 5. Memory substrate

- compressed historical latent tokens + actions + camera poses in KV cache

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes historical latent tokens along with relative actions and absolute camera poses. |
| Store | Compact camera-aware latent tokens in KV cache. |
| Retrieve | Implicit 3D-consistent retrieval from camera-aware memory. |
| Use | Enables memory-aware scene exploration from a single image and text description. |
| Update | Causal student/self-forcing paradigm supports long rollouts from teacher distillation. |
| Forget | Not central; compression is primary memory-budget mechanism. |
| Evaluate | 16 FPS, action following, long-horizon streaming and spatial-memory retrieval on Unreal Engine-rendered data. |

## 7. Strengths for this survey

Best example of KV memory becoming action/camera-aware world memory.

## 8. Limitations / second-pass PDF checks

Large 14B trained system; harder to compare directly with training-free video generators.

## 9. Recommended placement

- Main category: S7 Video world model memory 
- Role: 实时交互 world model 中 latent/history/action/camera 统一进 KV cache。
- Priority: Must-read
