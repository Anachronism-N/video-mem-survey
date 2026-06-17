# 17 v0.6.2 Polish and Figure 4 Coverage Audit

> Stage: polish and coverage audit after v0.6.1.  
> Goal: continue polishing the draft, answer whether Figure 4 should include all papers, and explicitly track world-model omissions.

## 1. Figure 4 coverage count

In the v0.6.2 draft, the LaTeX-rendered method landscape contains:

- 94 displayed chips.
- 88 unique chips after de-duplication.
- Approximately 60 distinct method or benchmark families, because several chips are concepts rather than papers, e.g., `scene recall`, `pose query`, `retrieval relevance`, `coordinate-valid reuse`.

This is larger than the earlier prompt-based Figure 4, but it is still not the full 102-paper library.

## 2. Should Figure 4 include all papers?

No. Figure 4 should not include every collected paper. A single figure has a different role from a master table:

- **Figure 4** should be a navigational map for A/B-grade method families and cross-route relationships.
- **Coverage audit table** should show mainline, supporting, background, benchmark, and unresolved groups.
- **Supplementary master table** should provide full 102-paper coverage and verification status.

Putting all 102 papers into one figure would make it unreadable in a two-column AAAI/IEEE-style layout. It would also blur the distinction between core methods, supporting methods, background systems, and unresolved candidates.

## 3. World-model omissions identified

The world-model route in v0.6.1 already included:

- WorldMem.
- SpMem.
- WorldPack.
- RELIC.
- Mirage.
- MosaicMem.
- LiveWorld.
- ReMind.
- WorldKV.
- UniDriveDreamer.
- DriveWAM.
- HiMem-WAM.
- GAIA / DriveDreamer / MagicDrive as background.
- Sora / Genie / V-JEPA 2 as background or motivation.

v0.6.2 adds or flags additional world-model candidates:

- **HyDRA / Hybrid Memory / HM-World** from “Out of Sight but Not Out of Mind.” This should be added as a dynamic-subject world-memory method after metadata verification.
- **GIM-World** from “Geometry-Aware Implicit Memory for Video World Models.” This should be added as geometry-aware implicit memory after metadata verification.
- **Genie 3 / Project Genie / Waymo World Model** should remain background unless official technical details provide enough memory mechanism detail.

## 4. Revised design decision

The final paper should use three linked artifacts:

1. **Figure 4: Method Landscape Matrix.** Compact, visual, not exhaustive.
2. **Table: Route-by-lifecycle matrix.** More precise than the figure, still not exhaustive.
3. **Appendix / Supplementary table: Full paper coverage.** Exhaustive over the 102-note corpus, with columns:
   - paper,
   - year,
   - route,
   - lifecycle focus,
   - training regime,
   - mainline/support/background/evaluation/unresolved,
   - verification status,
   - citation key.

This is the most defensible top-conference strategy.

## 5. v0.6.2 draft changes

The v0.6.2 working draft improves:

- Explanation of Figure 4’s role and coverage limits.
- World-action and world-model discussion.
- Coverage audit language.
- Discussion of why single-figure exhaustiveness is not desirable.
- The distinction between mainline methods, supporting methods, and background world models.

## 6. Remaining work

Next pass should:

- Add HyDRA/HM-World and GIM-World to the world-state route if metadata verification is completed.
- Create the full 102-paper supplementary coverage table.
- Normalize citation metadata for every paper used in the main tables.
- Draw or refine Figure 1, Figure 3, Figure 5, and Figure 8.
- Migrate to official AAAI style once the author kit is available.
