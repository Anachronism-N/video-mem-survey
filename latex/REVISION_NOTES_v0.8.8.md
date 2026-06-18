# Revision notes for v0.8.8

This update responds to the supplied review comments.

## Main changes

1. Tightened the abstract so the contribution reads as a natural survey contribution rather than a checklist.
2. Strengthened the methodology section with explicit main-evidence vs supplementary/boundary-evidence handling.
3. Clarified the supplementary CSV schema and added fields for publication status, secondary route, evaluation setting, limitation, and main-text priority.
4. Revised the screening-statistics table so bibliographic verification flags are treated as supplementary transparency flags rather than unqualified main-text evidence.
5. Replaced the compact identity-state table with a persistent-vs-mutable field table.
6. Replaced the judge-reliability table with a failure-mode-oriented table covering existence-only bias, identity confusion, stale-state misses, temporal-window limitations, smoothness over-rewarding, and wrong-recall tolerance.
7. Added explicit scope tags to the world-state mechanism table: direct video generation, generative world simulation, interactive video generation, driving/embodied boundary case, and evaluation-only benchmark.
8. Normalized terminology toward coordinate/spectral memory and removed placeholder `Authors` strings from bibliography entries.

## Remaining risk

The full 108-record corpus still includes emerging or supplementary-only records whose metadata should be rechecked before final camera-ready submission. They are now explicitly flagged and should not be used alone as main evidence.

## Artifact note

The compiled PDF and full source archive are returned as downloadable artifacts from the ChatGPT session because this environment has no working `gh` command and the GitHub connector does not provide a normal mounted-file binary upload path for pushing the full zip/PDF package.
