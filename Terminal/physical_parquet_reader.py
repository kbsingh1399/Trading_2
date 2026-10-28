import os
import pathlib
import pandas as pd
import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
FEEDS_DIR = ROOT / "Data" / "feeds"

def physically_read_all_parquet():
    files = sorted(list(FEEDS_DIR.glob("*.parquet")))
    print(f"=== INITIATING PHYSICAL READ OF ALL {len(files)} PARQUET FEEDS ===")
    
    total_rows = 0
    total_bytes = 0
    feed_audit = []
    
    for f in files:
        f_size = f.stat().st_size
        total_bytes += f_size
        try:
            df = pd.read_parquet(f)
            rows, cols = df.shape
            total_rows += rows
            sample_cols = list(df.columns[:4])
            feed_audit.append({
                "feed": f.name,
                "rows": rows,
                "cols": cols,
                "bytes": f_size,
                "sample_cols": sample_cols,
                "status": "PHYSICALLY_READ_OK"
            })
            print(f"READ OK: {f.name:<38} | Rows: {rows:<6} | Cols: {cols:<3} | Size: {f_size / 1024:.1f} KB")
        except Exception as e:
            print(f"READ ERROR: {f.name} -> {e}")
            feed_audit.append({
                "feed": f.name,
                "error": str(e),
                "status": "FAIL"
            })
            
    print("=" * 80)
    print(f"TOTAL FEEDS READ: {len(feed_audit)} | TOTAL ROWS: {total_rows:,} | TOTAL SIZE: {total_bytes / (1024*1024):.2f} MB")
    return feed_audit

if __name__ == "__main__":
    physically_read_all_parquet()
