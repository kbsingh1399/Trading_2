import sys
import re

txt = open('docs/trade_plans/ARENA_LATEST_RAW.md', encoding='utf-8').read()
pattern = r'\{\s*"rank":\s*(\d+),\s*"symbol":\s*"([^"]+)",\s*"asset_class":\s*"([^"]+)",\s*"direction":\s*"([^"]+)",\s*"order_type":\s*"([^"]+)"'
matches = re.finditer(pattern, txt)
for m in matches:
    rank, sym, asset_cls, direction, o_type = m.groups()
    # find entry, sl, tp, lots, risk
    block = txt[m.start():m.start()+1500]
    entry = re.search(r'"entry_price_canonical[^"]*":\s*([0-9\.]+)', block) or re.search(r'"entry_price[^"]*":\s*([0-9\.]+)', block)
    sl = re.search(r'"sl_price_canonical[^"]*":\s*([0-9\.]+)', block) or re.search(r'"sl_price[^"]*":\s*([0-9\.]+)', block)
    tp = re.search(r'"tp_price_canonical[^"]*":\s*([0-9\.]+)', block) or re.search(r'"tp_price[^"]*":\s*([0-9\.]+)', block)
    lots = re.search(r'"recommended_lots":\s*([0-9\.]+)', block)
    risk = re.search(r'"nominal_risk_usd":\s*([0-9\.]+)', block)
    e_val = entry.group(1) if entry else '-'
    sl_val = sl.group(1) if sl else '-'
    tp_val = tp.group(1) if tp else '-'
    lot_val = lots.group(1) if lots else '-'
    risk_val = risk.group(1) if risk else '-'
    print(f"Rank {rank}: {sym:10} ({asset_cls:6}) | {direction:5} {o_type:10} | Entry: {e_val:10} | SL: {sl_val:10} | TP: {tp_val:10} | Lots: {lot_val:5} | Risk: {risk_val} USD")
