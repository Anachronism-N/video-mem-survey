# ReMind: Dynamic Memory for Out-of-Sight State Evolution

## 1. Metadata

- Year: 2026
- ID: arXiv:2605.25333
- URL: https://arxiv.org/html/2605.25333v1
- Category: S7 Video world model memory 
- Priority: High
- Training-free: Trained/system
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

ReMind teaches video generators to use KV cache as dynamic memory through memory-oriented data, event-aware training and cache adaptation.

## 3. Problem / failure mode

Video generators freeze hidden states after interruptions because they are rarely trained to use non-local KV retrieval as dynamic memory.

## 4. Memory object

- hidden state evolution

## 5. Memory substrate

- memory-oriented data + event-aware training + cache adaptation

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Constructs camera-annotated frame graphs with protected anchors, degraded intervals and temporal gaps. |
| Store | KV cache/pathways adapted for dynamic memory; PM-RoPE supports camera-phase retrieval. |
| Retrieve | Node-structured curriculum forces retrieval of relevant past states across interruptions. |
| Use | Supports frontier continuation and reference-cache training for out-of-sight state evolution. |
| Update | Event-aware training and cache adaptation induce dynamic memory behavior. |
| Forget | Uses noisy memory/node-drop/degraded intervals to robustify retrieval under missing/dirty memory. |
| Evaluate | STEVO-Bench and recovery tasks; also checks general I2V to avoid catastrophic forgetting. |

## 7. Strengths for this survey

Important training-data/curriculum counterpart to LiveWorld.

## 8. Limitations / second-pass PDF checks

Requires new data/training rather than training-free inference.

## 9. Recommended placement

- Main category: S7 Video world model memory 
- Role: out-of-sight state evolution。
- Priority: High
