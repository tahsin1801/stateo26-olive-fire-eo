# StatEO26 Poster #35 — Supplementary Material

**Title:** Operational Earth Observation for Wildfire Damage Assessment in Olive Groves — An Integrated Court–Agency Case Study from the Mediterranean Region

**Conference:** StatEO26 · ESA-ESRIN · Frascati, Italy · 5–7 May 2026  
**Session:** 1.6 · Poster Session 1  
**Poster:** #35 · Abstract 144  

**Author:** Tahsin Ünal  
**Affiliation:** Ministry of Agriculture & Forestry · Aliağa District Directorate · İzmir, Türkiye

This repository provides non-confidential supplementary material for a court-oriented Earth Observation workflow applied to wildfire damage assessment in traditional Mediterranean olive groves.

---

## Methodology overview

The workflow combines UAV photogrammetry, Sentinel-2 burn-severity analysis, field evidence, and court-oriented agricultural damage accounting.

Main components:

1. **UAV photogrammetry** — ODM/SfM reconstruction, orthophoto, DSM/DTM and CHM products  
2. **Sentinel-2 analysis** — pre/post-fire spectral comparison using vegetation and burn-severity indices  
3. **Tree-level interpretation** — CHM-detected tree candidates classified by per-tree Sentinel-2 dNBR sampling  
4. **Institutional damage assessment** — integration of EO evidence with field observations and agricultural valuation logic  

No supervised model training was applied.

---

## Key numbers — Poster v14

**Tree inventory**

- Manual reference inventory: **169** olive trees  
- CHM-detected tree candidates: **161**  
- CHM completeness against manual reference: **95.3%**  
- Eight trees were locally under-detected in the eastern sparse transition zone  

**Damage assessment**

- Field walk-through evidence: **63** damaged trees  
- UAV × Sentinel-2 fusion estimate: **61** damaged trees  
- CHM + dNBR strict classification: **65** damaged trees  
- Court-accounting inference: **73** damaged trees  
- Convergent damaged-tree range: **61–73**  

---

## Repository status

- ✅ Project introduction and key results  
- 🔄 Method summary — in preparation  
- 🔄 Workflow diagram — in preparation  
- 🔄 Non-confidential code outlines — in preparation  

---

## Disclaimer

This repository contains methodological material only.

No personal data, judicial proceedings, restricted case-file content, raw UAV imagery, or confidential cadastral evidence is shared.

Views expressed are the author's.

---

## How to cite

Ünal, T. (2026). *Operational Earth Observation for Wildfire Damage Assessment in Olive Groves: An Integrated Court–Agency Case Study from the Mediterranean Region.* StatEO26 — Earth Observation for Official Statistics, ESA-ESRIN, Frascati, Italy. Poster #35, Abstract 144, Session 1.6.

---

## License

MIT License — see [LICENSE](LICENSE).
