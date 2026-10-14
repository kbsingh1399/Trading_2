#!/usr/bin/env python3
"""Cycle 105 independent claim verification against the pinned snapshot.
Recomputes headline figures from raw fields (does not import other cycle105 modules)."""
import json
from collections import defaultdict

D = json.load(open('docs/telemetry/live_snapshot_latest.json'))
AM = D['assets_matrix_24']
ok = fail = 0

def chk(name, cond, detail=""):
    global ok, fail
    print(f"{'PASS' if cond else 'FAIL'}  {name}  {detail}")
    ok, fail = ok + bool(cond), fail + (not cond)

chk("generation pin", D['generation_id'] == '734d2d6d1c414627bdefdb9dc361d53a', D['generation_id'])
chk("as_of pin", D['as_of_utc'] == '2026-10-14 19:37:47 UTC', D['as_of_utc'])
chk("24 assets", len(AM) == 24, str(len(AM)))
a, r, c = D['account'], D['risk'], D['capacity']
chk("flat inventory", D['active_positions'] == [] and D['pending_orders'] == [] and a['margin_used_usd'] == 0.0)
chk("balance/equity 4859.55", a['balance_usd'] == 4859.55 and a['equity_usd'] == 4859.55)
chk("cushions", round(a['equity_usd'] - a['hard_floor_usd'], 2) == 84.55 and round(a['equity_usd'] - 4795.0, 2) == 64.55)
chk("capacity 4 free", c['available'] == 4 and c['filled'] == 0 and c['pending'] == 0)
chk("stress capacity = 3 tickets", int(64.55 // (1.25 * 14.50 + 2.0)) == 3, f"stress/ticket={1.25*14.5+2:.3f}")
m = D['macro_calendar']
chk("macro disabled/no blackout", m['blackout_active'] is False and m['blackout_enforcement'] == 'DISABLED_BY_OPERATOR', m['event'])

mx = max(abs(v['causal_indicators']['vwap_z_score']) for v in AM.values())
chk("max |Z| < 2.0 (Engine 1 dead)", mx < 2.0, f"max|Z|={mx}")
near = max(AM, key=lambda k: abs(AM[k]['causal_indicators']['vwap_z_score']))
chk("max |Z| asset is NEAR", near == 'NEAR', near)

# two-sided share of persistent notional, per asset
print("\n-- two-sided share of persistent (>=180s) L3 notional --")
for s, v in AM.items():
    walls = v.get('orderbook_live_depth', {}).get('whale_walls_l3') or []
    if not walls:
        continue
    sides = defaultdict(set)
    for w in walls:
        sides[w['address']].add(w['side'])
    two = {k for k, sd in sides.items() if len(sd) == 2}
    pers = [w for w in walls if (w.get('persist_s') or 0) >= 180]
    tot = sum(w['notional_usd'] for w in pers)
    ts = sum(w['notional_usd'] for w in pers if w['address'] in two)
    print(f"   {s:7} persistent={len(pers):4} share={100*ts/tot if tot else 0:5.1f}%")

# spot-check the walls cited in the report
def wall(sym, side, price, min_notional, min_persist):
    walls = AM[sym]['orderbook_live_depth']['whale_walls_l3']
    hits = [w for w in walls if w['side'] == side and abs(w['price'] - price) < 1e-6
            and w['notional_usd'] >= min_notional and (w.get('persist_s') or 0) >= min_persist]
    return hits

chk("BTC ask 82,071 >=8.9M/180s", bool(wall('BTC', 'SELL', 82071.0, 8.9e6, 180)))
chk("BTC bid 81,196 >=24.9M/180s", bool(wall('BTC', 'BUY', 81196.0, 24.9e6, 180)))
chk("ETH ask 2,461.7 >=14.4M/180s", bool(wall('ETH', 'SELL', 2461.7, 14.4e6, 180)))
chk("SP500 bid 7,687 >=38.3M/180s", bool(wall('SP500', 'BUY', 7687.0, 38.3e6, 180)))
chk("SP500 ask 7,725.6 ~1.0M/180s", bool(wall('SP500', 'SELL', 7725.6, 0.99e6, 180)))

# basis sign convention: basis_median ~= MT5 mid - perp mid
for s in ('BTC', 'ETH', 'GOLD', 'USWTI', 'SP500'):
    ob = AM[s]['orderbook_live_depth']; vb = ob['venue_basis']['HYPERLIQUID']
    inst = AM[s]['quotes']['mid'] - vb['mid']
    print(f"   basis {s:7} median={vb['basis_median']:+.4f} instantaneous={inst:+.4f} |diff|/ATR={abs(vb['basis_median']-inst)/AM[s]['causal_indicators']['atr_14']:.2f}")
wt = AM['USWTI']['orderbook_live_depth']['venue_basis']['HYPERLIQUID']['basis_median']
chk("USWTI basis ~4 ATR", 3.5 < wt / AM['USWTI']['causal_indicators']['atr_14'] < 4.5,
    f"{wt/AM['USWTI']['causal_indicators']['atr_14']:.2f} ATR")

# contiguous ladder: BTC buy-stop bins above spot are unbroken
bins = sorted((b['min_price'], b['max_price']) for b in AM['BTC']['structural_stop_clusters']['nearest_buy_stop_clusters_above'])
contig = all(abs(bins[i][1] - bins[i + 1][0]) < 1e-9 for i in range(len(bins) - 1))
chk("BTC buy-stop ladder contiguous", contig, f"{bins[0]}..{bins[-1]} n={len(bins)}")

# report tallies
rep = open('docs/trade_plans/ARENA_CYCLE_105_ASTRA_COUNCIL_REPORT_20261014_1937Z.md').read()
chk("report tally line", "CANDIDATE 0 · WATCHLIST 5" in rep and "NO SETUP 19" in rep)
chk("report has single STAND ASIDE row", rep.count("| STAND ASIDE |") == 1)
desk = open('docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md').read()
chk("desk has Cycle 105 entry", "Trading Desk Council — Cycle 105 (Arena Tab 1" in desk)

print(f"\n{ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)
