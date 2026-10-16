import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
src = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
dst = ROOT / "docs" / "telemetry" / "live_snapshot_gemini.json"

def make_slim() -> bool:
    if not src.exists():
        print(f"Source {src} not found!")
        return False

    data = json.loads(src.read_text(encoding="utf-8"))

    for sym, d in data.get("assets_matrix_24", {}).items():
        if not isinstance(d, dict):
            continue
        # Trim raw candles if present
        for k in ["raw_candles_15m", "raw_candles_1h", "raw_candles_4h", "raw_candles_daily"]:
            if k in d:
                del d[k]
        # Trim cvd buckets
        if d.get("cvd_1m_buckets") and isinstance(d["cvd_1m_buckets"], list):
            d["cvd_1m_buckets"] = d["cvd_1m_buckets"][-30:]
        # Trim deep liquidation lists
        liq = d.get("reconstructed_liquidations")
        if isinstance(liq, dict):
            for lk in ["all_long_bands", "all_short_bands", "raw_cascade_clusters"]:
                if lk in liq and isinstance(liq[lk], list):
                    liq[lk] = liq[lk][:12]

    dst.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Successfully generated {dst.name}: {dst.stat().st_size:,} bytes")
    return True

if __name__ == "__main__":
    make_slim()

