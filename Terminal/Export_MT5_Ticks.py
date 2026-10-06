"""Read-only MT5 quote-history export for paired uplift replay (no order API)."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import json
from pathlib import Path
from Terminal.Risk_Sizing_Engine import epoch
from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge

def export_ticks(episodes_path, output_dir, account_id=None):
    import MetaTrader5 as mt5
    import polars as pl
    bridge=MT5ExecutionBridge(account_id=account_id)
    if not bridge.ensure_connected(): raise RuntimeError("MT5 tick history unavailable")
    episodes=[json.loads(row) for row in Path(episodes_path).read_text(encoding="utf-8").splitlines() if row.strip()]
    windows={}
    for e in episodes:
        start, end=epoch(e["as_of"]),epoch(e["as_of"])+21600
        if end > datetime.now(timezone.utc).timestamp(): continue
        for p in e["existing_positions"]+[e["candidate"]]:
            # Fixed UTC hour boundaries make repeated exports idempotent.
            for hour in range(int(start//3600), int(end//3600)+1): windows[(p["symbol"],hour)]=True
    output=Path(output_dir);output.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for symbol,hour in sorted(windows):
        begin=datetime.fromtimestamp(hour*3600,timezone.utc)
        raw=mt5.copy_ticks_range(symbol,begin,begin+timedelta(hours=1),mt5.COPY_TICKS_INFO)
        if raw is None: raise RuntimeError(f"Tick history read failed for {symbol}: {mt5.last_error()}")
        frame=pl.DataFrame({"time":raw["time_msc"].astype(float)/1000,"symbol":[symbol]*len(raw),
                            "bid":raw["bid"],"ask":raw["ask"],"feed_kind":["FULL_MT5_TICKS"]*len(raw)})
        frame=frame.filter((pl.col("bid")>0)&(pl.col("ask")>pl.col("bid"))&(pl.col("time")>=hour*3600)&(pl.col("time")<(hour+1)*3600))
        safe="".join(c if c.isalnum() or c in "._-" else "_" for c in symbol)
        path=output/f"{safe}_{hour}.parquet";temporary=path.with_suffix(".tmp")
        frame.write_parquet(temporary);temporary.replace(path)
        manifest.append({"path":path.name,"symbol":symbol,"start":hour*3600,"end":(hour+1)*3600,
                         "rows":len(frame),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    (output/"export_manifest.json").write_text(json.dumps({"source":"MT5_COPY_TICKS_INFO","account_id":bridge.get_account_summary().get("login"),
                                                         "created_at":datetime.now(timezone.utc).isoformat(),"chunks":manifest},indent=2),encoding="utf-8")
    return {"chunks":len(manifest),"rows":sum(m["rows"] for m in manifest),"output":str(output)}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes",required=True);parser.add_argument("--output",required=True);parser.add_argument("--account-id",type=int)
    args=parser.parse_args();print(json.dumps(export_ticks(args.episodes,args.output,args.account_id),indent=2))
