"""Dual-model council scan across all 24 assets. Diagnostic only; changes no verdict."""
import sys, time, collections
sys.path.insert(0, '.')
from Terminal.telemetry_ingest import get_fresh_snapshot, make_git_refresh, measure_snapshot_age
from Terminal.dg_context import evaluate_candidate_dg_v3

def wilder_atr(bars, n=14):
    """Wilder(14) ATR from 15m bars -- all 10 CFDs publish atr_14=None."""
    if len(bars) < n + 1:
        return None
    trs = []
    for i in range(1, len(bars)):
        h, l, pc = bars[i].get("high"), bars[i].get("low"), bars[i - 1].get("close")
        if None in (h, l, pc):
            return None
        trs.append(max(float(h) - float(l), abs(float(h) - float(pc)), abs(float(l) - float(pc))))
    a = sum(trs[:n]) / n
    for t in trs[n:]:
        a = (a * (n - 1) + t) / n
    return a


snap = get_fresh_snapshot(refresh=make_git_refresh())
m = measure_snapshot_age(snap, now=time.time())
am = snap["assets_matrix_24"]
asof = float(snap["as_of_epoch"])
print(f"CYCLE gen={m.generation_id} as_of={snap['as_of_utc']} age={m.age_s:.1f}s")

acc = snap.get("account") or {}
na = snap.get("NATIVE_MT5_ACCOUNT_INFO") or {}
bal = na.get("balance_usd") or acc.get("balance_usd") or acc.get("balance")
eq = na.get("equity_usd") or acc.get("equity_usd") or acc.get("equity")
print(f"ACCOUNT #{na.get('login') or acc.get('login')} {na.get('currency') or acc.get('currency')} "
      f"bal={bal} eq={eq} margin={na.get('margin_used_usd') or acc.get('margin_used_usd')} "
      f"floor=4775.0 cushion={round(float(bal or 0) - 4775.0, 2)}")
cap = snap.get("capacity") or {}
print(f"CAPACITY filled={cap.get('filled')} pending={cap.get('pending')} max={cap.get('max_concurrent')} "
      f"inventory={cap.get('inventory_status')}")
print(f"AUTH={snap.get('trade_authorization')}")
print(f"\n{'SYM':6}{'mid':>10}{'ATR':>9}{'bps':>8}{'gam':>7}{'Z':>7}{'regime':>12}{'M1':>3}{'M2':>3}"
      f"{'eps':>9}{'bind_leg':>18}{'tickAge':>9}")

regimes = collections.Counter()
fails = collections.Counter()
n_m1 = n_m2 = 0
gam_ok15 = gam_ok20 = 0
for s, v in am.items():
    q = v.get("quotes") or {}
    ci = v.get("causal_indicators") or {}
    try:
        mid = float(q["mid"])
    except (KeyError, TypeError, ValueError):
        print(f"{s:6} UNAVAILABLE quote"); continue
    atr = ci.get("atr_14")
    if not isinstance(atr, (int, float)):
        atr = wilder_atr(v.get("bars_15m_ohlcv") or [], 14)
    if not isinstance(atr, (int, float)) or not atr:
        print(f"{s:6}{mid:10.5g} atr_14=None and no usable 15m bars"); continue
    bps = float(q.get("spread_bps") or 0)
    gamma = (mid * bps / 1e4 * 2) / (1.5 * atr)
    gam_ok15 += gamma <= 0.15
    gam_ok20 += gamma <= 0.20
    z = float(ci.get("vwap_z_score") or 0)
    res = {}
    for mdl, direction in (("M1", "LONG"), ("M2", "LONG")):
        try:
            r = evaluate_candidate_dg_v3(
                features={"sweep_z": z, "model": mdl, "direction": direction, "atr_14": atr,
                          "session_vwap": float(ci.get("session_vwap_utc") or mid),
                          "session_sigma": float(ci.get("session_sigma") or 0),
                          "session_bars": ci.get("session_bars"), "rsi_14": ci.get("rsi_14"),
                          "p_win_lower_bound": float(snap.get("p_win_lower_bound") or 0),
                          "p_win_lower_bound_calibrated": bool(snap.get("p_win_lower_bound_calibrated")),
                          "p_win_calibration_sample_n": snap.get("p_win_calibration_sample_n")},
                payload=v, pivots=None, quote=q,
                bars_15m=v.get("bars_15m_ohlcv") or [], bars_1h=v.get("htf_1h_ohlcv") or [],
                bars_4h=v.get("htf_4h_ohlcv") or [],
                entry=mid, sl=mid - 1.5 * atr, tp=mid + 3.75 * atr,
                sizing={"risk_usd": 14.5, "friction_usd": 2.0, "entry": mid,
                        "sl": mid - 1.5 * atr, "tp": mid + 3.75 * atr},
                symbol=s, as_of_epoch=asof)
        except Exception as e:
            r = {"regime": "ERROR", "failures": [type(e).__name__], "stats": {}}
        res[mdl] = r
        for f in (r.get("failures") or []):
            fails[f] += 1
    rg = res["M2"].get("regime") or "UNDEFINED"
    regimes[rg] += 1
    p1 = not res["M1"].get("failures"); p2 = not res["M2"].get("failures")
    n_m1 += p1; n_m2 += p2
    st = res["M2"].get("stats") or {}
    eps = leg = ""
    if st.get("15m"):
        eps = f"{-1.5 - st['15m']['vr_z']:.4f}"; leg = "vr_z_15m"
        if st.get("4h"):
            e4 = 0.30 - st["4h"]["er"]
            if e4 < (-1.5 - st["15m"]["vr_z"]):
                eps = f"{e4:.4f}"; leg = "er_4h"
    print(f"{s:6}{mid:10.5g}{atr:9.5g}{bps:8.2f}{gamma:7.3f}{z:+7.2f}{rg:>12}"
          f"{'Y' if p1 else '-':>3}{'Y' if p2 else '-':>3}{eps:>9}{leg:>18}"
          f"{float(q.get('broker_tick_age_s') or 0):9.2f}")

defined = sum(v for k, v in regimes.items() if k not in ("UNDEFINED", "ERROR"))
print(f"\nregimes defined: {defined}/{len(am)}  ({dict(regimes)})")
print(f"M1 pass: {n_m1}/{len(am)}   M2 pass: {n_m2}/{len(am)}")
print(f"gamma <= 0.15R: {gam_ok15}/{len(am)}   <= 0.20R: {gam_ok20}/{len(am)}")
print(f"failure tokens (M1): {dict(fails)}")
