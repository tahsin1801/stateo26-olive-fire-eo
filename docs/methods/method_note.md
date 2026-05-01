# Method Note

This note summarises the non-confidential methodology behind StatEO26 Poster #35 / Abstract 144.

## Study concept

The workflow links Earth Observation, UAV photogrammetry, field evidence, and court-oriented agricultural damage accounting for wildfire damage assessment in traditional Mediterranean olive groves.

## Main workflow

1. **Sentinel-2 burn-severity analysis**  
   Pre- and post-fire spectral comparison was used to derive burn-severity information, including dNBR-based interpretation.

2. **UAV photogrammetry**  
   UAV imagery was processed through an ODM/SfM workflow to support orthophoto, DSM/DTM, and CHM-based interpretation.

3. **CHM-based tree-candidate detection**  
   A canopy height model workflow identified 161 tree candidates against a 169-tree manual reference inventory.

4. **Per-tree burn-severity sampling**  
   Sentinel-2 dNBR values were sampled at CHM-detected tree candidate locations to support tree-level damage interpretation.

5. **Field and institutional evidence integration**  
   EO-derived evidence was checked against field observations and integrated into court-oriented agricultural damage accounting.

## Key methodological result

The CHM workflow detected 161 tree candidates against a 169-tree manual reference, corresponding to 95.3% parcel-scale completeness.

The eight missing trees were locally concentrated in the eastern sparse transition zone, where low-canopy olive trees were under-detected by the photogrammetric DTM.

## Damage convergence

Four methodologically distinct estimates converged within a 61–73 damaged-tree range:

- Field walk-through evidence: 63 damaged trees
- UAV × Sentinel-2 fusion estimate: 61 damaged trees
- CHM + dNBR strict classification: 65 damaged trees
- Court-accounting inference: 73 damaged trees

No supervised model training was applied.

## Confidentiality

This note is methodological only. No personal data, judicial proceedings, restricted case-file content, raw UAV imagery, confidential cadastral evidence, or full coordinate datasets are shared.
