import json
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
paths_file = ROOT / "scripts" / "eligible_dossier_paths.txt"
paths = [p.strip() for p in paths_file.read_text(encoding="utf-8").splitlines() if p.strip()]

forensics = []
for p_str in paths:
    p = pathlib.Path(p_str)
    if not p.exists():
        continue
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()

    sym_clean = p.stem.replace("_MASTER_DOSSIER", "")
    sec_match = re.search(r"Macro Sector:\s*`([^`]+)`", text)
    sector = sec_match.group(1) if sec_match else "Forex Majors & Crosses"

    bid_m = re.search(r"Bid:\s*`?([\d\.]+)", text)
    ask_m = re.search(r"Ask:\s*`?([\d\.]+)", text)
    spread_m = re.search(r"Spread:\s*`?([\d\.]+)\s*bps", text)
    vah_m = re.search(r"VAH:\s*`?([\d\.,]+)", text)
    val_m = re.search(r"VAL:\s*`?([\d\.,]+)", text)
    poc_m = re.search(r"POC:\s*`?([\d\.,]+)", text)

    bid = float(bid_m.group(1)) if bid_m else 0.0
    ask = float(ask_m.group(1)) if ask_m else 0.0
    spread = float(spread_m.group(1)) if spread_m else 0.0
    vah = vah_m.group(1) if vah_m else "N/A"
    val = val_m.group(1) if val_m else "N/A"
    poc = poc_m.group(1) if poc_m else "N/A"

    forensics.append({
        "symbol": sym_clean,
        "clean_sym": sym_clean,
        "sector": sector,
        "dossier_file": p.name,
        "lines": len(lines),
        "bytes": len(text.encode("utf-8")),
        "bid": bid,
        "ask": ask,
        "spread_bps": spread,
        "vah": vah,
        "val": val,
        "poc": poc,
        "decision": "STAND_ASIDE_MONITOR",
        "rationale": "TIER_0_DEFENSIVE capital defense. Equity 4763.23 < 4775.00 Hard Floor."
    })

out_p = ROOT / "docs" / "trade_plans" / "CYCLE_031_DOSSIER_FORENSICS_ALL_95.json"
out_p.parent.mkdir(parents=True, exist_ok=True)
with open(out_p, "w", encoding="utf-8") as f:
    json.dump(forensics, f, indent=2)

print(f"Successfully compiled {len(forensics)} asset forensics to {out_p}")
