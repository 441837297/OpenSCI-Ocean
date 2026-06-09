"""
P0-03: Download ERA5 daily u10 for the full study period, extended domain.

Covers 2022-12-01 to 2024-01-15, 130°E-180°, 5°S-5°N — one dataset usable
for all 7 Kelvin events. Extends west of 150°E because p1_06b found the
KE01-KE03 westerly peaks pinned at the 150°E domain edge.

Uses ARCO-ERA5 zarr on GCS (anonymous access).
Output: data/era5/u10_eq_fullyear_130E-180E.nc
"""
from pathlib import Path

import xarray as xr

BASE = Path(__file__).resolve().parents[1]
ERA5_DIR = BASE / "data" / "era5"
ERA5_DIR.mkdir(parents=True, exist_ok=True)

OUT = ERA5_DIR / "u10_eq_fullyear_130E-180E.nc"

if OUT.exists():
    print(f"Already exists: {OUT}")
    raise SystemExit(0)

print("Opening ARCO-ERA5 zarr...")
ds_full = xr.open_zarr(
    "gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3",
    chunks={"time": 24},
    storage_options={"token": "anon"},
)

sub = ds_full["10m_u_component_of_wind"].sel(
    latitude=slice(5, -5),
    longitude=slice(130, 180),
    time=slice("2022-12-01", "2024-01-15"),
)

print(f"Subset: {sub.sizes} — resampling to daily means...")
daily = sub.resample(time="1D").mean()

print("Computing and writing (this can take a while)...")
daily.to_dataset(name="u10").to_netcdf(OUT)
print(f"Saved: {OUT}")
