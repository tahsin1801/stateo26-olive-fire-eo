# Workflow Summary

This document summarises the non-confidential analytical workflow behind StatEO26 Poster #35 / Abstract 144.

## 1. Study objective

The objective was to develop an operational Earth Observation workflow for wildfire damage assessment in traditional Mediterranean olive groves.

The workflow was designed to support public-authority and court-oriented agricultural damage assessment by combining satellite evidence, UAV photogrammetry, field observations, and institutional damage accounting.

## 2. Data streams

The workflow integrates four main evidence streams:

1. **Sentinel-2 optical imagery**  
   Used for pre- and post-fire vegetation and burn-severity assessment.

2. **UAV photogrammetry**  
   Used to generate high-resolution orthophoto, DSM/DTM, and CHM products.

3. **Tree-level field evidence**  
   Used to support interpretation of canopy damage, scorch patterns, trunk damage, and tree-level mortality indicators.

4. **Agricultural damage accounting**  
   Used to translate technical evidence into a court-oriented damaged-tree estimate.

## 3. Processing logic

The workflow followed a structured sequence:

1. Define parcel-level area of interest.
2. Process UAV imagery through an ODM/SfM workflow.
3. Generate structural surface products including DSM/DTM and CHM.
4. Detect tree candidates from the CHM.
5. Compare detected tree candidates against manual reference inventory.
6. Derive Sentinel-2 burn-severity indicators.
7. Sample per-tree dNBR values at detected tree-candidate locations.
8. Classify damage severity using threshold-based interpretation.
9. Compare EO-derived results with field and institutional evidence.
10. Report convergent damaged-tree estimates.

## 4. Key results

The workflow produced the following poster-level results:

- Manual reference inventory: **169 olive trees**
- CHM-detected tree candidates: **161**
- CHM completeness against manual reference: **95.3%**
- CHM + dNBR strict damaged-tree classification: **65**
- Field walk-through evidence: **63 damaged trees**
- UAV × Sentinel-2 fusion estimate: **61 damaged trees**
- Court-accounting inference: **73 damaged trees**
- Convergent damaged-tree range: **61–73**

## 5. Known limitation

The CHM workflow locally under-detected eight trees in the eastern sparse transition zone.

This limitation was associated with low-canopy olive trees and local photogrammetric DTM behaviour. The issue was treated as a methodological boundary condition rather than a failure of the overall parcel-scale workflow.

## 6. Model training

No supervised model training was applied.

The workflow used rule-based processing, threshold-based burn-severity interpretation, structural tree-candidate detection, field evidence, and institutional cross-checking.

## 7. Confidentiality

This workflow summary does not include raw UAV data, cadastral coordinates, full-resolution raster products, judicial records, personal data, or complete coordinate datasets.

The purpose is methodological transparency without disclosure of restricted spatial or case-file evidence.
