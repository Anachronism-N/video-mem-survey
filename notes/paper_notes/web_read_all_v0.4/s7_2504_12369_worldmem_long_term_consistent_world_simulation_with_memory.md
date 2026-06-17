# WorldMem: Long-term Consistent World Simulation with Memory

## 1. Metadata

- Year: 2025
- ID: arXiv:2504.12369
- URL: https://arxiv.org/abs/2504.12369
- Category: S7 Video world model memory 
- Priority: Must-read
- Training-free: Trained/system
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

WorldMem stores memory frames together with states such as poses and timestamps, making world memory state-conditioned rather than raw-frame-only.

## 3. Problem / failure mode

Limited temporal context causes failures in long-term consistency, especially 3D spatial consistency.

## 4. Memory object

- scene/world memory

## 5. Memory substrate

- memory frames + states such as pose/timestamp

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Writes memory frames and their states (pose, timestamp) into a memory bank. |
| Store | Memory units combining visual frames and state metadata. |
| Retrieve | Memory attention extracts relevant memory frames based on states. |
| Use | Reconstructs previously observed scenes under viewpoint/temporal gaps and supports dynamic evolution via timestamps. |
| Update | Memory bank grows/updates as world is observed over time. |
| Forget | Not emphasized; memory selection/retrieval is more central. |
| Evaluate | Virtual and real scenarios; spatial reconstruction and interaction. |

## 7. Strengths for this survey

Canonical world-model memory paper: memory must include state metadata.

## 8. Limitations / second-pass PDF checks

Frame/state bank can be heavier than latent memory; PDF needed for details.

## 9. Recommended placement

- Main category: S7 Video world model memory 
- Role: 视频世界模型 memory bank 代表。
- Priority: Must-read
