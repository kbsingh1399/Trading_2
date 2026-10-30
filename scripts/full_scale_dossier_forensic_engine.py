import os
import sys
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding='utf-8')

eligible_symbols = []
with open(ROOT / 'scripts' / 'cycle_033_eligible_dossiers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        sym = line.split(',')[0].replace('.pi', '').replace('.p', '')
        eligible_symbols.append(sym)

print(f"Loaded {len(eligible_symbols)} eligible symbols from scripts/cycle_033_eligible_dossiers.txt")

full_scale_results = {}
total_lines_read = 0
total_bytes_read = 0

for sym in eligible_symbols:
    fpath = ROOT / "docs" / "dossiers" / f"{sym}_MASTER_DOSSIER.md"
    if not fpath.exists():
        alts = [f for f in os.listdir(ROOT / "docs" / "dossiers") if f.upper().startswith(sym.upper())]
        if alts:
            fpath = ROOT / "docs" / "dossiers" / alts[0]
        else:
            print(f"WARNING: Dossier for {sym} not found!")
            continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines_count = content.count('\n') + 1
    bytes_count = len(content.encode('utf-8'))
    total_lines_read += lines_count
    total_bytes_read += bytes_count

    # 1. Section 1: Telemetry
    bid_m = re.search(r"Live Bid Quote\*\*:\s*`([^`]+)`", content)
    ask_m = re.search(r"Live Ask Quote\*\*:\s*`([^`]+)`", content)
    spread_m = re.search(r"Spread BPS\*\*:\s*`([^`]+)`", content)

    # 2. Section 2: Technicals & Dispersion
    vwap_m = re.search(r"VWAP Mid\*\*:\s*`([^`]+)`", content)
    atr_m = re.search(r"ATR \(14\)\*\*:\s*`([^`]+)`", content)

    # 3. Section 3: Auction Market Structure
    vah_m = re.search(r"Value Area High \(VAH\)\s*=\s*`([^`]+)`", content)
    poc_m = re.search(r"Point of Control \(POC\)\s*=\s*`([^`]+)`", content)
    val_m = re.search(r"Value Area Low \(VAL\)\s*=\s*`([^`]+)`", content)
    sess_high_m = re.search(r"Session High\*\*:\s*`([^`]+)`", content)
    sess_low_m = re.search(r"Session Low\*\*:\s*`([^`]+)`", content)

    # 4. Section 4: Multi-Timeframe CVD Regimes
    cvd_15m_regime = None
    cvd_15m_delta = None
    m_15m = re.search(r'\|\s*`15m`\s*\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|\s*([^|]+)\|\s*`?([^`|]+)`?\|\s*[^|]+\|\s*`?([^`|]+)`?\|\s*\*\*`?([^`|]+)`?\*\*\s*\|\s*`?([^`|]+)`?', content)
    if m_15m:
        cvd_15m_delta = m_15m.group(1).strip()
        cvd_15m_regime = m_15m.group(5).strip()

    cvd_1h_regime = None
    m_1h = re.search(r'\|\s*`1h`\s*\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|\s*([^|]+)\|\s*`?([^`|]+)`?\|\s*[^|]+\|\s*`?([^`|]+)`?\|\s*\*\*`?([^`|]+)`?\*\*\s*\|\s*`?([^`|]+)`?', content)
    if m_1h:
        cvd_1h_regime = m_1h.group(5).strip()

    cvd_4h_regime = None
    m_4h = re.search(r'\|\s*`4h`\s*\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|\s*([^|]+)\|\s*`?([^`|]+)`?\|\s*[^|]+\|\s*`?([^`|]+)`?\|\s*\*\*`?([^`|]+)`?\*\*\s*\|\s*`?([^`|]+)`?', content)
    if m_4h:
        cvd_4h_regime = m_4h.group(5).strip()

    # 5. Section 5: Whale Armor & L2 Depth
    top_bid_wall = None
    top_ask_wall = None
    bid_wall_m = re.search(r'\* Top Defending Bid Wall:\s*`?([^`\n]+)`?', content)
    ask_wall_m = re.search(r'\* Top Defending Ask Wall:\s*`?([^`\n]+)`?', content)
    if bid_wall_m: top_bid_wall = bid_wall_m.group(1).strip()
    if ask_wall_m: top_ask_wall = ask_wall_m.group(1).strip()

    large_orders = re.findall(r'\|\s*`?(BUY|SELL)`?\s*\|\s*`?([0-9\.]+)`?\s*\|[^|]+\|\s*([0-9\.,]+)\s*USD\s*\|[^|]+\|\s*`?LARGE \(>= USD 100K\)`?', content)

    # 6. Section 6: Liquidation Max Pain
    short_mp_24h = None
    long_mp_24h = None
    short_mp_48h = None
    long_mp_48h = None
    mp_24h_m = re.search(r'\* 24H Horizon:\s*Short MP=`?([0-9\.]+)`?[^|]*\|\s*Long MP=`?([0-9\.]+)`?', content)
    if mp_24h_m:
        short_mp_24h = mp_24h_m.group(1).strip()
        long_mp_24h = mp_24h_m.group(2).strip()

    mp_48h_m = re.search(r'\* 48H Horizon:\s*Short MP=`?([0-9\.]+)`?[^|]*\|\s*Long MP=`?([0-9\.]+)`?', content)
    if mp_48h_m:
        short_mp_48h = mp_48h_m.group(1).strip()
        long_mp_48h = mp_48h_m.group(2).strip()

    # 7. Section 10: Execution Cards & Posture
    decision_m = re.search(r"Postured Action\*\*:\s*`([^`]+)`", content)
    if not decision_m:
        decision_m = re.search(r"Sovereign Posture:\s*\*\*`?([^`\n\*]+)`?\*\*", content)

    long_entry_m = re.search(r"Candidate Long Setup.*?Execution Entry:\s*`([^`]+)`", content, re.DOTALL)
    long_sl_m = re.search(r"Candidate Long Setup.*?Spread-Padded Stop Loss:\s*`([^`]+)`", content, re.DOTALL)
    long_tp_m = re.search(r"Candidate Long Setup.*?\+2\.5R Take Profit:\s*`([^`]+)`", content, re.DOTALL)
    long_lot_m = re.search(r"Candidate Long Setup.*?Mathematical Lot Sizing:\s*\*\*`([^`]+)`\*\*", content, re.DOTALL)

    short_entry_m = re.search(r"Candidate Short Setup.*?Execution Entry:\s*`([^`]+)`", content, re.DOTALL)
    short_sl_m = re.search(r"Candidate Short Setup.*?Spread-Padded Stop Loss:\s*`([^`]+)`", content, re.DOTALL)
    short_tp_m = re.search(r"Candidate Short Setup.*?\+2\.5R Take Profit:\s*`([^`]+)`", content, re.DOTALL)
    short_lot_m = re.search(r"Candidate Short Setup.*?Mathematical Lot Sizing:\s*\*\*`([^`]+)`\*\*", content, re.DOTALL)

    full_scale_results[sym] = {
        "file": str(fpath.relative_to(ROOT)),
        "lines": lines_count,
        "bytes": bytes_count,
        "telemetry": {
            "bid": bid_m.group(1) if bid_m else None,
            "ask": ask_m.group(1) if ask_m else None,
            "spread_bps": spread_m.group(1) if spread_m else None,
            "vwap": vwap_m.group(1) if vwap_m else None,
            "atr_14": atr_m.group(1) if atr_m else None
        },
        "auction_structure": {
            "vah": vah_m.group(1) if vah_m else None,
            "val": val_m.group(1) if val_m else None,
            "poc": poc_m.group(1) if poc_m else None,
            "session_high": sess_high_m.group(1) if sess_high_m else None,
            "session_low": sess_low_m.group(1) if sess_low_m else None
        },
        "orderflow_cvd": {
            "cvd_15m_delta": cvd_15m_delta,
            "cvd_15m_regime": cvd_15m_regime,
            "cvd_1h_regime": cvd_1h_regime,
            "cvd_4h_regime": cvd_4h_regime
        },
        "whale_armor_l2": {
            "top_bid_wall": top_bid_wall,
            "top_ask_wall": top_ask_wall,
            "large_orders_ge_100k_count": len(large_orders)
        },
        "liquidation_max_pain": {
            "short_mp_24h": short_mp_24h,
            "long_mp_24h": long_mp_24h,
            "short_mp_48h": short_mp_48h,
            "long_mp_48h": long_mp_48h
        },
        "execution": {
            "postured_action": decision_m.group(1) if decision_m else None,
            "long_card": {
                "entry": long_entry_m.group(1) if long_entry_m else None,
                "sl": long_sl_m.group(1) if long_sl_m else None,
                "tp": long_tp_m.group(1) if long_tp_m else None,
                "lot": long_lot_m.group(1) if long_lot_m else None
            },
            "short_card": {
                "entry": short_entry_m.group(1) if short_entry_m else None,
                "sl": short_sl_m.group(1) if short_sl_m else None,
                "tp": short_tp_m.group(1) if short_tp_m else None,
                "lot": short_lot_m.group(1) if short_lot_m else None
            }
        }
    }

output_path = ROOT / "docs" / "trade_plans" / "CYCLE_033_FULL_SCALE_UNIVERSE_DATABASE.json"
output_path.parent.mkdir(parents=True, exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(full_scale_results, f, indent=2)

print(f"SUCCESS: Extracted full-scale 360-degree data across {len(full_scale_results)} dossiers!")
print(f"Total Lines Processed: {total_lines_read:,}")
print(f"Total Bytes Processed: {total_bytes_read:,} ({total_bytes_read / 1024 / 1024:.2f} MB)")
print(f"Saved full-scale database to: {output_path}")
