"""
CHM-based Individual Tree Crown Detection — V1 Pipeline
========================================================

Public-safe methodology outline for tree-level detection using
photogrammetric Canopy Height Model (CHM).

This is a methodology outline. It contains no coordinates, no parcel
identifiers, no raster paths, and no case-specific data. It documents
the algorithmic logic only.

Context:
    Used for wildfire damage assessment in Mediterranean olive groves.
    Court-oriented application; the per-tree inventory is later 
    classified by Sentinel-2 dNBR for damage severity.

Author:  Tahsin Ünal
Project: StatEO 2026 — ESA-ESRIN, Frascati, Italy
Poster:  #35 · Abstract 144 · Session 1.6
License: MIT (planned for full release post-conference)
"""

# Standard scientific Python stack — no proprietary libraries
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.feature import peak_local_max


# ----------------------------------------------------------------------
# Algorithm parameters (Mediterranean traditional olive grove)
# ----------------------------------------------------------------------

# Smoothing kernel applied to the CHM before peak detection.
# Sigma is in pixels at native CHM resolution (~0.25 m).
# Empirically chosen to suppress branch-level peaks while preserving 
# crown-center maxima.
GAUSSIAN_SIGMA_PX = 2.0

# Minimum height threshold (metres above ground) for a CHM local 
# maximum to be considered a tree-center candidate. 1.0 m excludes 
# shrubs and ground noise while retaining low-canopy traditional olives.
MIN_TREE_HEIGHT_M = 1.0

# Minimum spacing between detected tree centers (metres).
# 2.0 m is conservative for traditional olive spacing; multi-stem trees
# may produce more than one peak per crown, accepted at this stage and
# resolved in downstream fusion if applicable.
MIN_TREE_DISTANCE_M = 2.0


# ----------------------------------------------------------------------
# Core detection function
# ----------------------------------------------------------------------

def detect_tree_centers_from_chm(
    chm_array: np.ndarray,
    pixel_size_m: float,
    polygon_mask: np.ndarray,
    min_height_m: float = MIN_TREE_HEIGHT_M,
    min_distance_m: float = MIN_TREE_DISTANCE_M,
    smoothing_sigma_px: float = GAUSSIAN_SIGMA_PX,
) -> np.ndarray:
    """
    Detect individual tree centers from a Canopy Height Model.

    Workflow:
        1. Replace negative / NoData values with zero.
        2. Apply Gaussian smoothing to suppress branch-level peaks.
        3. Find local maxima above the height threshold, with a 
           minimum spacing constraint.
        4. Restrict detections to inside the analysis polygon mask.

    Parameters
    ----------
    chm_array : ndarray
        2D array of canopy heights in metres. NaN or negative values 
        are treated as no-canopy.
    pixel_size_m : float
        Pixel size of the CHM in metres (typical: 0.25 m).
    polygon_mask : ndarray of bool
        Boolean mask, True inside the analysis polygon. Same shape 
        as `chm_array`.
    min_height_m : float
        Minimum CHM height for a peak to be retained.
    min_distance_m : float
        Minimum spacing between retained peaks, in metres.
    smoothing_sigma_px : float
        Gaussian smoothing sigma in pixels.

    Returns
    -------
    peaks_rowcol : ndarray of shape (n_trees, 2)
        Row/column indices of detected tree centers, restricted to 
        inside the analysis polygon.

    Notes
    -----
    No supervised model training is involved. Thresholds are taken 
    from prior Mediterranean olive-fire literature and field-validated 
    against parcel-level evidence.
    """
    # 1. Clean CHM — treat negatives and NaN as no-canopy
    chm_clean = np.where(chm_array < 0, 0.0, chm_array)
    chm_clean = np.nan_to_num(chm_clean, nan=0.0)

    # 2. Smooth to suppress sub-crown maxima (branches, leaves)
    chm_smooth = gaussian_filter(chm_clean, sigma=smoothing_sigma_px)

    # 3. Detect local maxima with spacing constraint
    min_distance_px = max(2, int(round(min_distance_m / pixel_size_m)))
    peaks = peak_local_max(
        chm_smooth,
        min_distance=min_distance_px,
        threshold_abs=min_height_m,
        exclude_border=2,
    )

    # 4. Restrict to inside analysis polygon
    inside_polygon = polygon_mask[peaks[:, 0], peaks[:, 1]]
    peaks_in_polygon = peaks[inside_polygon]

    return peaks_in_polygon


# ----------------------------------------------------------------------
# Pixel-to-UTM conversion (projection-aware)
# ----------------------------------------------------------------------

def pixel_to_utm(
    rows_cols: np.ndarray,
    origin_x_utm: float,
    origin_y_utm: float,
    pixel_size_m: float,
) -> np.ndarray:
    """
    Convert raster pixel coordinates to UTM (metres).

    Assumes the raster is north-up (no rotation) and given in a 
    projected metric CRS — typical for UTM-based UAV/SfM products.

    Parameters
    ----------
    rows_cols : ndarray of shape (n, 2)
        Pixel coordinates (row, col).
    origin_x_utm, origin_y_utm : float
        UTM coordinates of the top-left pixel center.
    pixel_size_m : float
        Pixel size in metres.

    Returns
    -------
    utm_xy : ndarray of shape (n, 2)
        UTM (Easting, Northing) coordinates in metres.
    """
    cols = rows_cols[:, 1]
    rows = rows_cols[:, 0]
    utm_x = origin_x_utm + cols * pixel_size_m
    utm_y = origin_y_utm - rows * pixel_size_m  # north-up: rows go down
    return np.column_stack([utm_x, utm_y])


# ----------------------------------------------------------------------
# Methodology summary (for documentation, not executed)
# ----------------------------------------------------------------------
"""
Methodology summary
-------------------
The CHM is computed as DSM minus DTM at native UAV/SfM resolution.
A classical lower-envelope DTM is used as the baseline ("V1"). A
Gaussian smoothing is applied to the CHM before local-maximum
detection, ensuring that branch-level peaks within a single crown 
do not produce spurious tree centers.

Each detection is later linked to a Sentinel-2 dNBR sample at its 
UTM coordinate (bilinear interpolation), enabling per-tree fire 
severity classification according to Mediterranean burn-severity 
thresholds.

Limitations
-----------
In sparse traditional olive transition zones, the photogrammetric 
DTM may sit too high relative to the true ground level, locally 
suppressing canopy heights and under-detecting low-canopy trees. 
This is a known boundary condition of the V1 ground-filter design 
and is documented as a sensitivity-analysis target for further 
methodological work.

References
----------
Burn-severity thresholds are interpreted with reference to 
Mediterranean fire-severity literature and local field evidence. 
A full reference list is planned for the methodology paper 
in preparation.
"""
