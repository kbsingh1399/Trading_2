import sys
import pathlib
import polars as pl

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parents[1]
parquet_path = ROOT / "Data" / "feeds" / "00_MT5_Account_Telemetry.parquet"
dossier_dir = ROOT / "docs" / "dossiers"

df = pl.read_parquet(parquet_path)
passing = df.filter((pl.col("Gate_Status") == "PASS") & (pl.col("Broker_Symbol") != "NONE_ACTIVE"))

print(f"Total tradeable assets passing spread gate: {len(passing)}")

sym_aliases = {
    "BTCUSD": "BTC",
    "ETHUSD": "ETH",
    "BCHUSD": "BCH",
    "XRPUSD": "XRP",
    "SOLUSD": "SOL"
}

eligible_dossiers = []
for row in passing.iter_rows(named=True):
    raw_sym = row["Broker_Symbol"]
    clean = raw_sym.replace(".pi", "").replace(".p", "").replace(".m", "")
    target_clean = sym_aliases.get(clean, clean)
    target = dossier_dir / f"{target_clean}_MASTER_DOSSIER.md"
    if target.exists():
        eligible_dossiers.append(str(target))
    else:
        candidates = list(dossier_dir.glob(f"{target_clean}*_MASTER_DOSSIER.md"))
        if candidates:
            eligible_dossiers.append(str(candidates[0]))
        else:
            print(f"Warning: No dossier found for {raw_sym} ({clean})")

seen = set()
unique_dossiers = []
for d in eligible_dossiers:
    if d not in seen:
        seen.add(d)
        unique_dossiers.append(d)

print(f"Total verified master dossiers mapped: {len(unique_dossiers)}")

out_path = ROOT / "scripts" / "cycle_032_eligible_dossiers.txt"
out_path.write_text("\n".join(unique_dossiers), encoding="utf-8")
print(f"Saved {len(unique_dossiers)} master dossier paths to {out_path}")
