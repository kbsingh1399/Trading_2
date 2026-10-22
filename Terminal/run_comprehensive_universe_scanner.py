"""
Terminal/run_comprehensive_universe_scanner.py
===============================================
Comprehensive 156-Asset Multi-Asset Opportunity Scanner.
Scans all tradeable symbols on Blueberry Markets MT5.
Applies:
1. Spread friction gate (Spread / TP <= 15.0%)
2. Structural invalidation stops (tight 0.35-0.50 ATR beyond swing extremes)
3. Expanded R:R targets (2.50R - 4.50R)
4. MT5 broker profit calculation (mt5.order_calc_profit)
5. Solvency defense (Individual Stressed Equity >= 4,795.00 USD)
Outputs a ranked Master Candidate Radar Matrix across Crypto, Metals, Indices, Forex.
"""

import MetaTrader5 as mt5
import numpy as np
import json
import pathlib
from datetime import datetime, timezone

if not mt5.initialize():
    print("MT5 initialization failed")
    exit(1)

acc = mt5.account_info()
equity = acc.equity
hard_floor = 4775.00
buffer_floor = 4795.00

# Get all symbols available on the broker
all_symbols = mt5.symbols_get()
print(f"Total Broker Symbols Found: {len(all_symbols)}")

# Focus on tradeable symbols
tradeable = [s for s in all_symbols if s.trade_mode != 0 and s.visible]
print(f"Active Visible Symbols: {len(tradeable)}")

candidates = []

for s in tradeable:
    sym = s.name
    tick = mt5.symbol_info_tick(sym)
    if not tick or tick.bid == 0 or tick.ask == 0:
        continue
    
    spread = tick.ask - tick.bid
    if spread <= 0:
        continue
        
    # Get M15 rates (last 60 bars)
    rates = mt5.copy_rates_from_pos(sym, mt5.TIMEFRAME_M15, 0, 60)
    if rates is None or len(rates) < 30:
        continue
        
    highs = np.array([r[2] for r in rates])
    lows = np.array([r[3] for r in rates])
    closes = np.array([r[4] for r in rates])
    
    # ATR 14
    tr = np.maximum(highs[1:] - lows[1:], np.maximum(np.abs(highs[1:] - closes[:-1]), np.abs(lows[1:] - closes[:-1])))
    atr = float(np.mean(tr[-14:]))
    if atr <= 0:
        continue
        
    # EMA 20 & 50
    alpha20 = 2.0 / 21.0
    alpha50 = 2.0 / 51.0
    ema20 = float(closes[0])
    ema50 = float(closes[0])
    for c in closes[1:]:
        ema20 = alpha20 * c + (1.0 - alpha20) * ema20
        ema50 = alpha50 * c + (1.0 - alpha50) * ema50
        
    recent_high = float(np.max(highs[-20:]))
    recent_low = float(np.min(lows[-20:]))
    current_close = float(closes[-1])
    
    ts = s.trade_tick_size
    if ts <= 0:
        ts = 10 ** (-s.digits)
        
    # Determine Asset Category
    category = "Other"
    sym_u = sym.upper()
    if any(k in sym_u for k in ["BTC", "ETH", "SOL", "XRP", "DOGE", "AVAX", "NEAR", "ADA", "BNB", "DOT", "LINK", "LTC", "BCH", "UNI", "AAVE", "ZEC", "XLM", "XMR"]):
        category = "Crypto"
    elif any(k in sym_u for k in ["XAU", "GOLD", "XAG", "SILVER", "WTI", "BRENT", "OIL", "COPPER", "GAS"]):
        category = "Commodities/Metals"
    elif any(k in sym_u for k in ["SP500", "NAS100", "DJ30", "GER40", "UK100", "US30", "US100", "US500", "JP225", "AU200", "HK50", "STOXX50"]):
        category = "Indices"
    elif any(k in sym_u for k in ["EUR", "GBP", "USD", "AUD", "CAD", "CHF", "JPY", "NZD", "SEK", "NOK"]):
        category = "Forex"
        
    # --- SETUP 1: BUY_LIMIT (Bullish Pullback / Sweep of recent low) ---
    # Entry at recent_low or EMA20 pullback (if trend is up)
    if current_close >= ema50: # Bullish or consolidating
        entry_b = recent_low
        sl_b = entry_b - (0.35 * atr)
        risk_pts_b = entry_b - sl_b
        tp_b = entry_b + (3.0 * risk_pts_b)
        
        # Snap to tick
        entry_b = round(round(entry_b / ts) * ts, s.digits)
        sl_b = round(round(sl_b / ts) * ts, s.digits)
        tp_b = round(round(tp_b / ts) * ts, s.digits)
        
        # Check passivity: entry must be below current bid
        if entry_b < tick.bid:
            dist_pct_b = (tick.bid - entry_b) / tick.bid * 100.0
            tp_dist_b = abs(tp_b - entry_b)
            spread_tp_b = (spread / tp_dist_b * 100.0) if tp_dist_b > 0 else 999.0
            
            if spread_tp_b <= 15.0 and dist_pct_b <= 4.0: # Good friction and within 4% of market
                # Calculate lot for target risk $20.00
                loss_min = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, sym, s.volume_min, entry_b, sl_b)
                if loss_min and loss_min < 0:
                    scale = abs(20.0 / loss_min)
                    lot = round(s.volume_min * scale / s.volume_step) * s.volume_step
                    lot = max(s.volume_min, min(lot, s.volume_max))
                    lot = round(lot, 2)
                    
                    act_loss = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, sym, lot, entry_b, sl_b)
                    act_prof = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, sym, lot, entry_b, tp_b)
                    
                    if act_loss and act_prof and act_loss < 0 and act_prof > 0:
                        stressed_loss = abs(act_loss) * 1.25 + 2.0
                        stressed_eq = equity - stressed_loss
                        
                        if stressed_eq >= buffer_floor: # Preserves $4,795 buffer!
                            rr = abs(act_prof / act_loss)
                            candidates.append({
                                "symbol": sym,
                                "category": category,
                                "side": "BUY_LIMIT",
                                "entry": entry_b,
                                "sl": sl_b,
                                "tp": tp_b,
                                "lot": lot,
                                "risk_usd": round(abs(act_loss), 2),
                                "profit_usd": round(act_prof, 2),
                                "rr": round(rr, 2),
                                "spread_tp_pct": round(spread_tp_b, 2),
                                "dist_to_fill_pct": round(dist_pct_b, 2),
                                "stressed_equity": round(stressed_eq, 2),
                                "buffer_surplus": round(stressed_eq - buffer_floor, 2),
                                "floor_surplus": round(stressed_eq - hard_floor, 2)
                            })
                            
    # --- SETUP 2: SELL_LIMIT (Bearish Rally / Sweep of recent high) ---
    if current_close <= ema20: # Bearish or relief rally
        entry_s = recent_high
        sl_s = entry_s + (0.35 * atr)
        risk_pts_s = sl_s - entry_s
        tp_s = entry_s - (3.0 * risk_pts_s)
        
        entry_s = round(round(entry_s / ts) * ts, s.digits)
        sl_s = round(round(sl_s / ts) * ts, s.digits)
        tp_s = round(round(tp_s / ts) * ts, s.digits)
        
        # Check passivity: entry must be above current ask
        if entry_s > tick.ask:
            dist_pct_s = (entry_s - tick.ask) / tick.ask * 100.0
            tp_dist_s = abs(entry_s - tp_s)
            spread_tp_s = (spread / tp_dist_s * 100.0) if tp_dist_s > 0 else 999.0
            
            if spread_tp_s <= 15.0 and dist_pct_s <= 4.0:
                loss_min_s = mt5.order_calc_profit(mt5.ORDER_TYPE_SELL, sym, s.volume_min, entry_s, sl_s)
                if loss_min_s and loss_min_s < 0:
                    scale_s = abs(20.0 / loss_min_s)
                    lot_s = round(s.volume_min * scale_s / s.volume_step) * s.volume_step
                    lot_s = max(s.volume_min, min(lot_s, s.volume_max))
                    lot_s = round(lot_s, 2)
                    
                    act_loss_s = mt5.order_calc_profit(mt5.ORDER_TYPE_SELL, sym, lot_s, entry_s, sl_s)
                    act_prof_s = mt5.order_calc_profit(mt5.ORDER_TYPE_SELL, sym, lot_s, entry_s, tp_s)
                    
                    if act_loss_s and act_prof_s and act_loss_s < 0 and act_prof_s > 0:
                        stressed_loss_s = abs(act_loss_s) * 1.25 + 2.0
                        stressed_eq_s = equity - stressed_loss_s
                        
                        if stressed_eq_s >= buffer_floor:
                            rr_s = abs(act_prof_s / act_loss_s)
                            candidates.append({
                                "symbol": sym,
                                "category": category,
                                "side": "SELL_LIMIT",
                                "entry": entry_s,
                                "sl": sl_s,
                                "tp": tp_s,
                                "lot": lot_s,
                                "risk_usd": round(abs(act_loss_s), 2),
                                "profit_usd": round(act_prof_s, 2),
                                "rr": round(rr_s, 2),
                                "spread_tp_pct": round(spread_tp_s, 2),
                                "dist_to_fill_pct": round(dist_pct_s, 2),
                                "stressed_equity": round(stressed_eq_s, 2),
                                "buffer_surplus": round(stressed_eq_s - buffer_floor, 2),
                                "floor_surplus": round(stressed_eq_s - hard_floor, 2)
                            })

mt5.shutdown()

print(f"\nTotal Qualified Candidates Identified: {len(candidates)}")

# Group by category and sort by proximity to fill (dist_to_fill_pct)
categories = ["Crypto", "Commodities/Metals", "Indices", "Forex"]
output_report = {}

for cat in categories:
    cat_candidates = [c for c in candidates if c["category"] == cat]
    cat_candidates.sort(key=lambda x: x["dist_to_fill_pct"])
    output_report[cat] = cat_candidates
    print(f"\n=== {cat.upper()} ({len(cat_candidates)} Candidates) ===")
    for i, c in enumerate(cat_candidates[:8]): # Top 8 closest to execution
        print(f"  {i+1}. {c['symbol']:12s} {c['side']:10s} Vol={c['lot']:.2f} | Entry={c['entry']} | SL={c['sl']} | TP={c['tp']} | R:R={c['rr']} | Risk=${c['risk_usd']} | Profit=+${c['profit_usd']} | Dist={c['dist_to_fill_pct']:.2f}% | Spread={c['spread_tp_pct']:.1f}%")

# Save to JSON
out_path = pathlib.Path("Data/telemetry/potential_candidates_pipeline.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({"timestamp": datetime.now(timezone.utc).isoformat(), "total": len(candidates), "pipeline": output_report}, f, indent=2)

print(f"\nSaved full pipeline to {out_path}")
