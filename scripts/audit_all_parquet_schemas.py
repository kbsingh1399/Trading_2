"""
Audit all parquet files in Data/feeds — dump complete column schemas, dtypes, row counts,
and sample values to docs/parquet_schema_audit.json
"""
import polars as pl
import pathlib
import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

feeds_dir = pathlib.Path("Data/feeds")
schema_map = {}

for f in sorted(feeds_dir.glob("*.parquet")):
    try:
        df = pl.read_parquet(f)
        sample = df.head(1).to_dicts()
        schema_map[f.name] = {
            "rows": len(df),
            "num_cols": len(df.columns),
            "columns": {c: str(df[c].dtype) for c in df.columns},
            "sample": sample[0] if sample else {}
        }
        print(f"OK  {f.name}: {len(df)} rows, {len(df.columns)} cols")
    except Exception as e:
        schema_map[f.name] = {"error": str(e)}
        print(f"ERR {f.name}: {e}")

out = pathlib.Path("docs/parquet_schema_audit.json")
out.parent.mkdir(parents=True, exist_ok=True)
json.dump(schema_map, open(out, "w", encoding="utf-8"), indent=2, default=str)
print(f"\nWritten: {out} ({out.stat().st_size:,} bytes)")
print(f"Total files audited: {len(schema_map)}")
