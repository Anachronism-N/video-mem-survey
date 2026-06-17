# Hybrid Spatial Memory / MosaicMem

## 1. Metadata

- Year: 2026
- ID: arXiv:2603.17117
- URL: https://arxiv.org/abs/2603.17117
- Category: S7 Video world model memory 
- Priority: High
- Training-free: Trained/system
- Original status: Verified by web
- Reading status: web-read
- Source basis: arXiv abstract web-read

## 2. One-sentence takeaway

MosaicMem combines explicit 3D patch lifting with native generative conditioning, preserving stable spatial evidence while allowing dynamic regions to evolve.

## 3. Problem / failure mode

Explicit 3D structures improve reprojection consistency but struggle with moving objects; implicit memory can have inaccurate camera motion.

## 4. Memory object

- controllable spatial world model

## 5. Memory substrate

- 3D patch lifting + native conditioning

## 6. Lifecycle extraction

| Stage | Extracted note |
|---|---|
| Write | Lifts patches into 3D for localization and targeted retrieval. |
| Store | Hybrid spatial memory of spatially aligned patches plus model-native conditioning. |
| Retrieve | Patch-and-compose interface retrieves patches in queried view. |
| Use | Preserves persistent scene components while inpainting what should evolve; supports minute-level navigation and scene editing. |
| Update | Memory alignment methods and autoregressive rollout update spatial memory. |
| Forget | Not a forgetting paper; evolving regions are delegated to model inpainting rather than stored rigidly. |
| Evaluate | Pose adherence, dynamic modeling, navigation, editing and rollout. |

## 7. Strengths for this survey

Excellent contrast to Mirage: hybrid explicit/implicit spatial memory.

## 8. Limitations / second-pass PDF checks

Complex spatial alignment and pose conditioning.

## 9. Recommended placement

- Main category: S7 Video world model memory 
- Role: hybrid spatial memory。
- Priority: High
