#!/usr/bin/env python3
"""Cycle 105 candidate card arithmetic (MT5 space, executable-side)."""
import json
D = json.load(open('docs/telemetry/live_snapshot_latest.json'))
AM = D['assets_matrix_24']
BAL = 4859.55

def card(sym, side, entry, sl, tp, note):
    a = AM[sym]; q = a['quotes']; ex = a['execution_specs']; ci = a['causal_indicators']
    atr = ci['atr_14']; cs = ex['contract_size']; step = ex['step_lot']; minlot = ex['min_lot']
    risk_d = abs(sl - entry); rew_d = abs(tp - entry)
    rr = rew_d / risk_d if risk_d else 0
    # choose lots: largest step multiple with risk in [7.5,14.5], prefer ~12
    best = None
    lots = minlot
    while lots <= ex['max_lot'] + 1e-9:
        r = risk_d * cs * lots
        if 7.5 <= r <= 14.5:
            best = (lots, r)
            if r >= 11.5:
                break
        lots = round(lots + step, 10)
    spread_cost = q['spread_price'] * cs * (best[0] if best else minlot)
    fric = 100 * spread_cost / (best[1] if best else (risk_d * cs * minlot))
    print(f"{sym} {side} E={entry} SL={sl} TP={tp} | riskDist={risk_d:.4f} ({risk_d/atr:.2f} ATR) "
          f"rewDist={rew_d:.4f} ({rew_d/atr:.2f} ATR) RR={rr:.2f} | entryDistFromMid={abs(entry-q['mid'])/atr:.2f} ATR "
          f"| lots={best} spreadCost=${spread_cost:.2f} friction={fric:.1f}%  [{note}]")
    if best:
        stress = 1.25 * best[1] + 2.0
        print(f"      stressed loss=${stress:.2f}  post-stop equity=${BAL-stress:.2f} (buffer 4795, cushion {BAL-stress-4795:+.2f})")

# BTC Engine2 short at the 82,071 perp ask wall (MT5 81,994.75)
card('BTC', 'SELL', 81994.75, 82161.00, 81585.00, 'SL = above [82023.75,82123.75]+0.5ATR -> lands inside [82123.75,82223.75]')
# BTC deeper at EMA50/82,441 wall
card('BTC', 'SELL', 82364.75, 82561.00, 81585.00, 'entry 2.48 ATR from mid -> proximity fail')
# ETH Engine2 short at EMA20/2,441 ask
card('ETH', 'SELL', 2439.28, 2463.80, 2419.20, 'SL above [2447.98,2457.98] squeeze +0.5ATR -> inside [2457.98,2467.98]')
# SP500 Engine2 short at EMA20 7,725 ask wall
card('SP500', 'SELL', 7725.00, 7741.60, 7703.40, 'SL = entry+1.5ATR (index rule); TP front-runs [7689.5,7699.5]')
card('SP500', 'SELL', 7725.00, 7741.60, 7673.40, 'alt TP at [7659.5,7669.5] magnet (blocked by 38.4M bid)')
# NAS100 Engine2 short at EMA20 30,044
card('NAS100', 'SELL', 30044.00, 30185.00, 29885.00, 'illustrative: SL above [30077.9,30177.9]+buffer, TP front of [29877.9,29977.9]')
# GOLD Engine2 short at EMA50 4,110
card('GOLD', 'SELL', 4110.25, 4122.10, 4081.90, 'TP front-runs [4067.6,4077.6]')
# SILVER Engine2 short at EMA20 55.92
card('SILVER', 'SELL', 55.918, 56.116, 55.415, 'TP front-runs [55.3665,55.4665]')
# USWTI Engine2 long at VAL 94.636
card('USWTI', 'BUY', 94.636, 94.300, 95.430, 'TP front-runs [95.4372,95.5373] buy-stops; SL below [94.3372,94.4372]-0.5ATR')
# EURUSD Engine2 short at pdVAL 1.1173
card('EURUSD', 'SELL', 1.11730, 1.11870, 1.11300, 'illustrative')
# SOL Engine2 short at 105.17 ask wall
card('SOL', 'SELL', 105.10, 106.31, 104.05, 'TP front-runs [103,104] combined magnet')
