#!/usr/bin/env python3
"""Cycle 105 telemetry digest: per-asset compact extraction."""
import json, sys

D = json.load(open('docs/telemetry/live_snapshot_latest.json'))
AM = D['assets_matrix_24']

def f(x, n=2):
    if x is None:
        return 'None'
    if isinstance(x, (int, float)):
        return f"{x:,.{n}f}" if abs(x) >= 1000 else f"{x:.{n}f}"
    return str(x)

def bandlist(lst, n=4, key='notional_usd'):
    out = []
    for b in (lst or [])[:n]:
        out.append(f"[{b['min_price']:.6g}-{b['max_price']:.6g}] ${b['notional_usd']/1e6:.3f}M d={b.get('distance_pct')}%")
    return ' | '.join(out) if out else 'none'

def cvd_windows(buckets):
    if not buckets:
        return 'none'
    b = sorted(buckets, key=lambda x: x['ts'])
    def s(n):
        seg = b[-n:] if len(b) >= n else b
        return sum(x['cvd_delta_usd'] for x in seg)
    return f"1m={s(1)/1e3:+.1f}k 5m={s(5)/1e3:+.1f}k 15m={s(15)/1e3:+.1f}k 30m={s(30)/1e3:+.1f}k (n={len(b)})"

for sym, a in AM.items():
    q = a['quotes']; ci = a['causal_indicators']; vp = a.get('volume_profile', {})
    pg = a.get('pullback_geometry', {}); sc = a.get('structural_stop_clusters', {})
    rl = a.get('reconstructed_liquidations', {}); ob = a.get('orderbook_live_depth', {})
    mc = a.get('multi_horizon_cvd', {}); tf = a.get('tradfi_orderflow', {})
    hp = a.get('htf_auction_profiles', {})
    ex = a.get('execution_specs', {})
    print('=' * 100)
    print(f"### {sym} [{a['category']}] broker={a.get('symbol_broker')}")
    print(f"  QUOTE bid={f(q.get('bid'),5)} ask={f(q.get('ask'),5)} mid={f(q.get('mid'),5)} spread={q.get('spread_bps')}bps fresh={q.get('quote_freshness')} age={q.get('quote_age_s'):.2f}s")
    print(f"  SPEC tick={ex.get('tick_size')} contract={ex.get('contract_size')} minlot={ex.get('min_lot')} steplot={ex.get('step_lot')} maxlot={ex.get('max_lot')} stops_level={ex.get('stops_level')} digits={ex.get('digits')} point={ex.get('point')}")
    print(f"  CAUSAL vwap={f(ci.get('session_vwap_utc'),5)} sigma={f(ci.get('session_sigma'),5)} Z={ci.get('vwap_z_score')} RSI={ci.get('rsi_14')} ATR={f(ci.get('atr_14'),5)} atr%={ci.get('atr_pct')}")
    print(f"         EMA20={f(ci.get('ema_20'),5)} EMA50={f(ci.get('ema_50'),5)} EMA200={f(ci.get('ema_200'),5)} slope3h={ci.get('ema_200_slope_3h_pct')} REGIME={ci.get('trend_regime')} bars_last_close={ci.get('bars_last_close_utc')} age={ci.get('indicator_age_min')}min")
    print(f"  VPROF POC={f(vp.get('poc'),5)} VAH={f(vp.get('vah'),5)} VAL={f(vp.get('val'),5)}")
    print(f"  PULLBK dir={pg.get('direction')} retrace={pg.get('retrace')} depth_sig={pg.get('depth_sigma')} vel={pg.get('velocity_ratio')} bars_pb={pg.get('bars_pullback')}/{pg.get('bars_impulse')}")
    print(f"  HTFAUC pdPOC={f(hp.get('prior_day_poc'),5)} pdVAH={f(hp.get('prior_day_vah'),5)} pdVAL={f(hp.get('prior_day_val'),5)} pwPOC={f(hp.get('prior_week_poc'),5)} wkVWAP={f(hp.get('weekly_vwap'),5)}")
    print(f"  CVD sess={mc.get('session_cvd_usd',0)/1e6:+.2f}M wk={mc.get('weekly_cvd_usd',0)/1e6:+.2f}M 24h={mc.get('cvd_24h_usd',0)/1e6:+.2f}M 15mbar={mc.get('bar_delta_15m_usd',0)/1e3:+.1f}k div={mc.get('divergence')}")
    print(f"      WINDOWS {cvd_windows(a.get('cvd_1m_buckets'))}")
    print(f"  TRADFI status={tf.get('status')} bias={tf.get('flow_bias')} tick_cvd={tf.get('session_tick_cvd')} ofi={tf.get('order_flow_imbalance')} delta15m={tf.get('delta_15m_usd')} buy_agg={tf.get('buyer_aggression_pct')} sell_agg={tf.get('seller_aggression_pct')}")
    print(f"  TRAPPED={a.get('trapped_traders_signal')}")
    print(f"  BOOK binance_mid={f(ob.get('binance_mid'),5)} basis_median={ob.get('basis_median')} top20bid=${(ob.get('top20_bid_depth_usd') or 0)/1e3:.1f}k top20ask=${(ob.get('top20_ask_depth_usd') or 0)/1e3:.1f}k imb={ob.get('book_imbalance')} skew={ob.get('skew_ratio')}")
    vb = ob.get('venue_basis') or {}
    for vk, vv in vb.items():
        print(f"        basis[{vk}] mid={vv.get('mid')} basis_median={vv.get('basis_median')}")
    walls = ob.get('whale_walls_l3') or []
    elig = [w for w in walls if w.get('gate_g7_eligible')]
    pers = [w for w in walls if (w.get('persist_s') or 0) >= 180]
    print(f"  WHALES total={len(walls)} eligible={len(elig)} persist>=180s={len(pers)}")
    for lbl, side in (('BUY', 'BUY'), ('SELL', 'SELL')):
        sub = sorted([w for w in walls if w['side'] == lbl], key=lambda w: -w['notional_usd'])[:6]
        for w in sub:
            print(f"        {side} {w['price']:.6g} ${w['notional_usd']/1e6:.3f}M persist={w.get('persist_s')}s frac={w.get('presence_frac')} status={w.get('persistence_status')} elig={w.get('gate_g7_eligible')} d={w.get('distance_pct')}% cls={w.get('wall_class')} first={w.get('first_seen_utc')}")
    l2 = ob.get('l2_wall_levels') or []
    for w in sorted(l2, key=lambda w: -w['notional_usd'])[:6]:
        print(f"        L2 {w['side']} {w['price']:.6g} ${w['notional_usd']/1e6:.3f}M persist={w.get('persist_s')}s status={w.get('persistence_status')} elig={w.get('gate_g7_eligible')} d={w.get('distance_pct')}%")
    print(f"  STOPS below(near): {bandlist(sc.get('nearest_sell_stop_clusters_below'),5)}")
    print(f"        above(near): {bandlist(sc.get('nearest_buy_stop_clusters_above'),5)}")
    print(f"        below(TOP ): {bandlist(sc.get('top_sell_stop_clusters_below'),4)}")
    print(f"        above(TOP ): {bandlist(sc.get('top_buy_stop_clusters_above'),4)}")
    print(f"  LIQ  long-below(near): {bandlist(rl.get('nearest_long_cascade_bands_below'),5)}")
    print(f"        short-above(near): {bandlist(rl.get('nearest_short_squeeze_bands_above'),5)}")
    print(f"        long-below(TOP ): {bandlist(rl.get('top_long_cascade_bands_below'),4)}")
    print(f"        short-above(TOP ): {bandlist(rl.get('top_short_squeeze_bands_above'),4)}")
    fr = a.get('funding_and_rates') or {}
    print(f"  FUND last={fr.get('last_funding_rate_bps')}bps mark={fr.get('mark_price')} index={fr.get('index_price')}")
    # HTF
    for tf_key in ('htf_1h_ohlcv', 'htf_4h_ohlcv'):
        bars = a.get(tf_key) or []
        if bars:
            last = bars[-1]
            print(f"  {tf_key} n={len(bars)} last O={last['open']} H={last['high']} L={last['low']} C={last['close']}")
            last6 = bars[-6:]
            print(f"      last6: " + ' '.join(f"{b['close']}" for b in last6))
    h = a.get('htf_history') or {}
    print(f"  HTFREADY entry_eligible={h.get('entry_eligible')} 1h={ (h.get('1h') or {}).get('status')}/{(h.get('1h') or {}).get('completed_count')} 4h={(h.get('4h') or {}).get('status')}/{(h.get('4h') or {}).get('completed_count')}")
    pm = a.get('pioneer_microstructure_eval') or {}
    print(f"  PIONEER status={pm.get('status')} setup={pm.get('confluence_trade_setup')} gating={pm.get('portfolio_gating')}")
