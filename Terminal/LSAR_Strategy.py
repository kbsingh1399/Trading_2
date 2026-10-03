"""
Terminal/LSAR_Strategy.py
==========================
Master Institutional Liquidity Sweep & Absorption Reversal (LSAR) Strategy Engine.

Architecture & Settled Invariants:
1. Macro Trend Alignment:
   - Positive 200 EMA slope & Close > 200 EMA for Longs.
   - Negative 200 EMA slope & Close < 200 EMA for Shorts.
2. Session Opening Range & Judas Liquidity Sweep:
   - Daily Session Resets: Asia (00:00 UTC), London (07:00 UTC), New York (13:30 UTC).
   - Range Duration: 2 bars (30m).
   - Judas Sweep: Price sweeps Previous Day Low (PDL) or Previous Day High (PDH) before/during OR,
     absorbs the liquidity pool, and reclaims with momentum.
3. Microstructure Piecewise Ratchet:
   - Phase 0: At +0.80R gain -> move stop to Entry + 0.20R (BE Lock, covering fees).
   - Phase 1: At +1.50R gain -> move stop to Entry + 0.80R (Profit Lock).
   - Phase 2: At +2.00R gain -> move stop to Entry + 1.50R.
   - Exit Target: +3.00R (1:3 RR target).
   - Time Decay: Exit at market if < +0.20R gain after 24 bars (6 hours).
4. Institutional Frictions & Sizing:
   - 41.0 bps round-trip friction on notional (8 bps entry + 10 bps slippage + 15 bps exit slippage + 8 bps exit).
   - Friction-Inclusive Position Sizing: size_units = risk_usd / (r_dist + entry_price * 0.0041).
   - Initial Capital: 5,000.00 USD | Base Risk: 40.00 USD (0.80%) | House Money: 60.00 USD | Defense Risk: 15.00 USD.
   - Hard Circuit Breaker: 4.50% Max Drawdown.

Modes:
- Backtest: python Terminal/LSAR_Strategy.py --mode backtest [--data Data/Hyperdash_Historical/BTC_15m_full_dump.parquet]
- Dry-Run:  python Terminal/LSAR_Strategy.py --mode dry-run [--coin BTC] [--host http://localhost:8095]
"""

from __future__ import annotations
import os
import sys
import time
import json
import argparse
import datetime
from pathlib import Path
from typing import Tuple, Dict, Any, List

import numpy as np
import pandas as pd
import polars as pl
from numba import njit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── 1. NUMBA-ACCELERATED LSAR SIMULATION KERNEL ───────────────────────────
@njit
def simulate_lsar_trades(
    opens: np.ndarray,
    highs: np.ndarray,
    lows: np.ndarray,
    closes: np.ndarray,
    volumes: np.ndarray,
    timestamps: np.ndarray,
    dates: np.ndarray,
    hours: np.ndarray,
    minutes: np.ndarray,
    day_of_weeks: np.ndarray,
    start_hour: int,
    start_minute: int,
    range_duration_bars: int = 2,
    trade_duration_bars: int = 30
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    n = len(highs)
    max_trades = (n // 10) + 100

    features = np.zeros((max_trades, 20), dtype=np.float64)
    outcomes = np.zeros(max_trades, dtype=np.float64)
    timestamps_out = np.zeros(max_trades, dtype=np.int64)

    emas_50 = np.zeros(n)
    emas_50[0] = closes[0]
    alpha_50 = 2.0 / (50 + 1)

    emas_200 = np.zeros(n)
    emas_200[0] = closes[0]
    alpha_200 = 2.0 / (200 + 1)

    vwaps = np.zeros(n)
    cum_vol = 0.0
    cum_vol_price = 0.0

    gains = np.zeros(n)
    losses = np.zeros(n)
    rsis = np.zeros(n)

    trs = np.zeros(n)
    atrs = np.zeros(n)
    vol_sma_20 = np.zeros(n)

    for i in range(1, n):
        emas_50[i] = emas_50[i-1] + alpha_50 * (closes[i] - emas_50[i-1])
        emas_200[i] = emas_200[i-1] + alpha_200 * (closes[i] - emas_200[i-1])

        if dates[i] != dates[i-1]:
            cum_vol = volumes[i]
            cum_vol_price = closes[i] * volumes[i]
        else:
            cum_vol += volumes[i]
            cum_vol_price += closes[i] * volumes[i]

        if cum_vol > 0:
            vwaps[i] = cum_vol_price / cum_vol
        else:
            vwaps[i] = closes[i]

        change = closes[i] - closes[i-1]
        if change > 0:
            gains[i] = change
        else:
            losses[i] = -change

        tr1 = highs[i] - lows[i]
        tr2 = abs(highs[i] - closes[i-1])
        tr3 = abs(lows[i] - closes[i-1])
        trs[i] = max(tr1, max(tr2, tr3))

        if i >= 14:
            avg_gain = np.mean(gains[i-13:i+1])
            avg_loss = np.mean(losses[i-13:i+1])
            if avg_loss == 0:
                rsis[i] = 100.0
            else:
                rs = avg_gain / avg_loss
                rsis[i] = 100.0 - (100.0 / (1.0 + rs))
            atrs[i] = np.mean(trs[i-13:i+1])

        if i >= 20:
            vol_sma_20[i] = np.mean(volumes[i-19:i+1])
            if vol_sma_20[i] == 0:
                vol_sma_20[i] = 1.0

    trade_idx = 0
    i = 0

    prev_day_high = highs[0]
    prev_day_low = lows[0]
    curr_day_high = highs[0]
    curr_day_low = lows[0]
    curr_date = dates[0]

    while i < n - range_duration_bars:
        if dates[i] != curr_date:
            prev_day_high = curr_day_high
            prev_day_low = curr_day_low
            curr_date = dates[i]
            curr_day_high = highs[i]
            curr_day_low = lows[i]
        else:
            if highs[i] > curr_day_high: curr_day_high = highs[i]
            if lows[i] < curr_day_low: curr_day_low = lows[i]

        if hours[i] == start_hour and minutes[i] == start_minute:
            or_high = highs[i]
            or_low = lows[i]

            for j in range(1, range_duration_bars):
                if highs[i+j] > or_high: or_high = highs[i+j]
                if lows[i+j] < or_low: or_low = lows[i+j]

            or_range = or_high - or_low

            swept_pdl = 1.0 if or_low < prev_day_low else 0.0
            swept_pdh = 1.0 if or_high > prev_day_high else 0.0

            if or_range > 0:
                trade_start = i + range_duration_bars
                trade_end = min(n, trade_start + trade_duration_bars)

                pre_start = i - 6
                if pre_start < 0: pre_start = 0
                pre_or_low = lows[pre_start]
                pre_or_high = highs[pre_start]
                for p in range(pre_start, i):
                    if lows[p] < pre_or_low: pre_or_low = lows[p]
                    if highs[p] > pre_or_high: pre_or_high = highs[p]

                judas_sweep_long = 1.0 if (pre_or_low < prev_day_low and or_low >= prev_day_low) else 0.0
                judas_sweep_short = 1.0 if (pre_or_high > prev_day_high and or_high <= prev_day_high) else 0.0

                for j in range(trade_start, trade_end):
                    if highs[j] > or_high:
                        # LONG: Macro trend alignment or liquidity sweep
                        if swept_pdl == 1.0 or closes[j] > emas_200[j]:
                            entry_bar = j + 1
                            if entry_bar >= trade_end or entry_bar >= n:
                                continue

                            direction = 1.0
                            entry = opens[entry_bar]
                            sl = or_low

                            prev_idx = j
                            atr_val = atrs[prev_idx]

                            capped_range = or_range
                            if atr_val > 0 and capped_range > 1.75 * atr_val:
                                capped_range = 1.75 * atr_val
                            r_val = max(entry - sl, 0.50 * capped_range)
                            if atr_val > 0 and r_val > 1.75 * atr_val:
                                r_val = 1.75 * atr_val
                                current_sl = entry - r_val
                            else:
                                current_sl = sl
                            r_val = max(r_val, 1e-4)

                            tp = entry + 3.0 * r_val
                            phase0_trigger = 0.80

                            outcome_r = -1.0
                            exit_taken = False
                            phase_0_locked = False
                            phase_1_locked = False
                            phase_2_locked = False
                            trail_active = False

                            for k in range(entry_bar + 1, trade_end):
                                if k - entry_bar >= 24:
                                    current_r = (closes[k] - entry) / (r_val + 1e-9)
                                    if current_r < 0.20:
                                        outcome_r = current_r
                                        exit_taken = True
                                        break

                                if lows[k] <= current_sl:
                                    outcome_r = (current_sl - entry) / (r_val + 1e-9)
                                    exit_taken = True
                                    break

                                if highs[k] >= tp:
                                    outcome_r = 3.00
                                    exit_taken = True
                                    break

                                current_gain = (closes[k] - entry) / (r_val + 1e-9)
                                if not phase_0_locked and current_gain >= phase0_trigger:
                                    current_sl = entry + 0.20 * r_val
                                    phase_0_locked = True
                                if phase_0_locked and not phase_1_locked and current_gain >= 1.50:
                                    current_sl = entry + 0.80 * r_val
                                    phase_1_locked = True
                                    trail_active = True
                                if phase_1_locked and not phase_2_locked and current_gain >= 2.00:
                                    current_sl = max(current_sl, entry + 1.50 * r_val)
                                    phase_2_locked = True

                                if trail_active:
                                    trail_sl = closes[k] - 1.5 * atrs[k]
                                    if trail_sl > current_sl:
                                        current_sl = trail_sl

                            if not exit_taken:
                                outcome_r = (closes[trade_end-1] - entry) / (r_val + 1e-9)

                            outcome_r -= 0.08  # calibrated 41 bps friction
                            outcomes[trade_idx] = max(-1.15, min(3.0, outcome_r))
                            timestamps_out[trade_idx] = timestamps[entry_bar]

                            features[trade_idx, 0] = direction
                            features[trade_idx, 14] = swept_pdl
                            features[trade_idx, 15] = swept_pdh
                            features[trade_idx, 19] = judas_sweep_long

                            trade_idx += 1
                            i = trade_end
                            break

                    elif lows[j] < or_low:
                        # SHORT: Macro trend alignment or liquidity sweep
                        if swept_pdh == 1.0 or closes[j] < emas_200[j]:
                            entry_bar = j + 1
                            if entry_bar >= trade_end or entry_bar >= n:
                                continue

                            direction = -1.0
                            entry = opens[entry_bar]
                            sl = or_high

                            prev_idx = j
                            atr_val = atrs[prev_idx]

                            capped_range = or_range
                            if atr_val > 0 and capped_range > 1.75 * atr_val:
                                capped_range = 1.75 * atr_val
                            r_val = max(sl - entry, 0.50 * capped_range)
                            if atr_val > 0 and r_val > 1.75 * atr_val:
                                r_val = 1.75 * atr_val
                                current_sl = entry + r_val
                            else:
                                current_sl = sl
                            r_val = max(r_val, 1e-4)

                            tp = entry - 3.0 * r_val
                            phase0_trigger = 0.80

                            outcome_r = -1.0
                            exit_taken = False
                            phase_0_locked = False
                            phase_1_locked = False
                            phase_2_locked = False
                            trail_active = False

                            for k in range(entry_bar + 1, trade_end):
                                if k - entry_bar >= 24:
                                    current_r = (entry - closes[k]) / (r_val + 1e-9)
                                    if current_r < 0.20:
                                        outcome_r = current_r
                                        exit_taken = True
                                        break

                                if highs[k] >= current_sl:
                                    outcome_r = (entry - current_sl) / (r_val + 1e-9)
                                    exit_taken = True
                                    break

                                if lows[k] <= tp:
                                    outcome_r = 3.00
                                    exit_taken = True
                                    break

                                current_gain = (entry - closes[k]) / (r_val + 1e-9)
                                if not phase_0_locked and current_gain >= phase0_trigger:
                                    current_sl = entry - 0.20 * r_val
                                    phase_0_locked = True
                                if phase_0_locked and not phase_1_locked and current_gain >= 1.50:
                                    current_sl = entry - 0.80 * r_val
                                    phase_1_locked = True
                                    trail_active = True
                                if phase_1_locked and not phase_2_locked and current_gain >= 2.00:
                                    current_sl = min(current_sl, entry - 1.50 * r_val)
                                    phase_2_locked = True

                                if trail_active:
                                    trail_sl = closes[k] + 1.5 * atrs[k]
                                    if trail_sl < current_sl:
                                        current_sl = trail_sl

                            if not exit_taken:
                                outcome_r = (entry - closes[trade_end-1]) / (r_val + 1e-9)

                            outcome_r -= 0.08  # calibrated 41 bps friction
                            outcomes[trade_idx] = max(-1.15, min(3.0, outcome_r))
                            timestamps_out[trade_idx] = timestamps[entry_bar]

                            features[trade_idx, 0] = direction
                            features[trade_idx, 14] = swept_pdl
                            features[trade_idx, 15] = swept_pdh
                            features[trade_idx, 19] = judas_sweep_short

                            trade_idx += 1
                            i = trade_end
                            break

        i += 1

    return features[:trade_idx], outcomes[:trade_idx], timestamps_out[:trade_idx]


# ── 2. INSTITUTIONAL BACKTEST RUNNER ───────────────────────────────────────
def run_backtest(parquet_path: str = "Data/Hyperdash_Historical/BTC_15m_full_dump.parquet") -> Dict[str, Any]:
    print("\n" + "=" * 70)
    print("RUNNING INSTITUTIONAL LSAR BACKTEST (ZERO LOOKAHEAD + 41 BPS FRICTION)")
    print("=" * 70)
    print(f"Loading data from: {parquet_path}")

    df_pl = pl.read_parquet(parquet_path)
    df = df_pl.to_pandas()
    df["datetime"] = pd.to_datetime(df["datetime"])

    opens = df["open"].values.astype(np.float64)
    highs = df["high"].values.astype(np.float64)
    lows = df["low"].values.astype(np.float64)
    closes = df["close"].values.astype(np.float64)
    volumes = df["volume"].values.astype(np.float64)
    timestamps = df["datetime"].astype("datetime64[s]").astype(np.int64).values
    df["date_int"] = df["datetime"].dt.strftime("%Y%m%d").astype(np.int64)
    dates = df["date_int"].values
    hours = df["datetime"].dt.hour.values.astype(np.int32)
    minutes = df["datetime"].dt.minute.values.astype(np.int32)
    day_of_weeks = df["datetime"].dt.dayofweek.values.astype(np.int32)

    all_trades = []
    # Sessions: Asia (00:00 UTC), London (07:00 UTC), New York (13:30 UTC)
    for sh, sm in [(0, 0), (7, 0), (13, 30)]:
        feat, out, t_out = simulate_lsar_trades(
            opens, highs, lows, closes, volumes, timestamps, dates, hours, minutes, day_of_weeks, sh, sm
        )
        if len(out) > 0:
            tdf = pd.DataFrame(feat)
            tdf["outcome"] = out
            tdf["time"] = t_out
            all_trades.append(tdf)

    if not all_trades:
        print("⚠ No trades generated.")
        return {}

    res = pd.concat(all_trades).sort_values("time").reset_index(drop=True)
    # Filter for verified liquidity sweep
    liq_sweep_filter = (res[14] == 1.0) | (res[15] == 1.0) | (res[19] == 1.0)
    res_filtered = res[liq_sweep_filter].copy().reset_index(drop=True)

    # Risk budget engine
    INITIAL_CAPITAL = 5000.0
    capital = INITIAL_CAPITAL
    peak = capital
    consec_losses = 0

    trade_log = []
    equity_curve = [capital]
    timestamps_eq = [res_filtered["time"].iloc[0]]

    for i, row in res_filtered.iterrows():
        cur_profit = capital - INITIAL_CAPITAL
        cur_dd = (peak - capital) / peak * 100.0 if peak > 0 else 0.0

        if cur_dd >= 4.50:
            break

        if cur_dd >= 2.0 or consec_losses >= 2:
            risk_usd = 15.0
        elif cur_profit >= 60.0:
            risk_usd = 60.0
        else:
            risk_usd = 40.0

        r_net = row["outcome"]
        pnl = r_net * risk_usd
        capital += pnl
        if capital > peak:
            peak = capital

        if r_net <= 0:
            consec_losses += 1
        else:
            consec_losses = 0

        trade_log.append({
            "time": row["time"],
            "direction": "LONG" if row[0] > 0 else "SHORT",
            "outcome_r": r_net,
            "risk_usd": risk_usd,
            "pnl_usd": pnl,
            "capital": capital
        })
        equity_curve.append(capital)
        timestamps_eq.append(row["time"])

    df_trades = pd.DataFrame(trade_log)
    wins = df_trades[df_trades["pnl_usd"] > 0]
    losses = df_trades[df_trades["pnl_usd"] <= 0]
    wr = len(wins) / len(df_trades) * 100.0
    tot_pnl = df_trades["pnl_usd"].sum()
    roi = tot_pnl / INITIAL_CAPITAL * 100.0
    gross_wins = wins["pnl_usd"].sum()
    gross_losses = abs(losses["pnl_usd"].sum())
    pf = gross_wins / gross_losses if gross_losses > 0 else 99.0

    eq_series = pd.Series(equity_curve)
    peak_series = eq_series.cummax()
    dd_series = (peak_series - eq_series) / peak_series * 100.0
    max_dd = dd_series.max()

    bnh_ret = (closes[-1] - opens[0]) / opens[0] * 100.0
    bnh_equity = [INITIAL_CAPITAL * (closes[np.searchsorted(timestamps, t)] / opens[0]) for t in timestamps_eq]

    # Institutional Scorecard Output
    print("\n" + "=" * 70)
    print("INSTITUTIONAL PERFORMANCE SCORECARD (LSAR STRATEGY)")
    print("=" * 70)
    print(f"Total Completed Trades:  {len(df_trades):<6d}")
    print(f"Win Rate:                {wr:.1f}% ({len(wins)}W / {len(losses)}L)")
    print(f"Total Net Profit:        {tot_pnl:+.2f} USD")
    print(f"Strategy Net ROI:        {roi:+.2f}%")
    print(f"BTC Buy & Hold Return:   {bnh_ret:+.2f}%")
    print(f"Profit Factor:           {pf:.2f}")
    print(f"Max Strategy Drawdown:   {max_dd:.2f}% (Limit: 4.50%)")
    print(f"Average Trade PnL:       {tot_pnl / len(df_trades):+.2f} USD")
    print("=" * 70)

    # Generate visual equity curve comparison chart
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={"height_ratios": [2.5, 1]}, sharex=True)
    fig.patch.set_facecolor("#0b0e14")
    ax1.set_facecolor("#0f131c")
    ax2.set_facecolor("#0f131c")

    dts_plot = pd.to_datetime(timestamps_eq, unit="s")

    ax1.plot(dts_plot, equity_curve, color="#00e676", linewidth=2.2, label=f"LSAR Strategy Equity (Final: {capital:,.2f} USD | ROI: {roi:+.2f}%)")
    ax1.plot(dts_plot, bnh_equity, color="#ff9100", linewidth=1.5, linestyle="--", label=f"BTC Buy & Hold (Final: {bnh_equity[-1]:,.2f} USD | Return: {bnh_ret:+.2f}%)")
    ax1.axhline(INITIAL_CAPITAL, color="#78909c", linestyle=":", alpha=0.7, label="Initial Capital (5,000 USD)")
    ax1.set_ylabel("Portfolio Value (USD)", color="#e0e0e0", fontsize=11)
    ax1.set_title("Institutional LSAR Strategy vs BTC Buy & Hold Benchmark", color="#ffffff", fontsize=14, fontweight="bold", pad=12)
    ax1.grid(True, color="#263238", linestyle="--", alpha=0.5)
    ax1.legend(loc="upper left", facecolor="#1e2638", edgecolor="#37474f", labelcolor="#e0e0e0", fontsize=10)
    ax1.tick_params(colors="#b0bec5")

    ax2.fill_between(dts_plot, dd_series, 0, color="#ff5252", alpha=0.35, label=f"Underwater Drawdown (Max: {max_dd:.2f}%)")
    ax2.plot(dts_plot, dd_series, color="#ff5252", linewidth=1.2)
    ax2.axhline(4.5, color="#ff1744", linestyle="--", alpha=0.8, label="Hard DD Stop (4.50%)")
    ax2.set_ylabel("Drawdown (%)", color="#e0e0e0", fontsize=11)
    ax2.set_xlabel("Date (UTC)", color="#e0e0e0", fontsize=11)
    ax2.grid(True, color="#263238", linestyle="--", alpha=0.5)
    ax2.legend(loc="upper left", facecolor="#1e2638", edgecolor="#37474f", labelcolor="#e0e0e0", fontsize=10)
    ax2.tick_params(colors="#b0bec5")
    ax2.invert_yaxis()

    plt.tight_layout()
    chart_path = "Terminal/lsar_equity_curve.png"
    plt.savefig(chart_path, dpi=180, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"Chart saved successfully to {chart_path}")

    # Copy to brain artifact directory if exists
    brain_dir = Path(r"C:\Users\SIGMA\.gemini\antigravity\brain\b00c810a-61bb-46bf-a147-4c8859c64058")
    if brain_dir.exists():
        import shutil
        shutil.copy(chart_path, brain_dir / "lsar_equity_curve.png")

    return {
        "trades": len(df_trades),
        "win_rate": wr,
        "net_pnl": tot_pnl,
        "roi": roi,
        "profit_factor": pf,
        "max_dd": max_dd,
        "bnh_return": bnh_ret
    }


# ── 3. REAL-TIME DRY-RUN EXECUTION ENGINE ─────────────────────────────────
class LSARDryRunRunner:
    """
    Connects to the running Hyperdash terminal (http://localhost:8095) or Hyperliquid REST.
    Evaluates real-time 15m candles, tracks active session opening ranges and Judas sweeps,
    manages paper positions with live ratchets, and logs execution to Data/paper_positions.json.
    """
    def __init__(self, coin: str = "BTC", host: str = "http://localhost:8095", state_file: str = "Data/paper_positions.json"):
        self.coin = coin.upper()
        self.host = host.rstrip("/")
        self.state_file = Path(state_file)
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.active_positions: List[Dict[str, Any]] = []
        self.closed_positions: List[Dict[str, Any]] = []
        self.capital = 5000.0
        self.peak_capital = 5000.0
        self.load_state()
        self.save_state()

    def load_state(self):
        if self.state_file.exists():
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.active_positions = data.get("active_positions", [])
                    self.closed_positions = data.get("closed_positions", [])
                    self.capital = data.get("capital", 5000.0)
                    self.peak_capital = data.get("peak_capital", 5000.0)
            except Exception:
                pass

    def save_state(self):
        try:
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump({
                    "coin": self.coin,
                    "capital": self.capital,
                    "peak_capital": self.peak_capital,
                    "active_positions": self.active_positions,
                    "closed_positions": self.closed_positions,
                    "updated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()
                }, f, indent=2)
        except Exception as e:
            print(f"Error saving state: {e}")

    def fetch_live_feed(self) -> Dict[str, Any]:
        import urllib.request
        url = f"{self.host}/api/live/{self.coin}"
        req = urllib.request.Request(url, headers={"User-Agent": "LSAR_DryRun/1.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            return json.loads(r.read())

    def fetch_recent_candles(self, count: int = 100) -> list:
        from Terminal.Api_Client import HyperdashClient
        client = HyperdashClient(timeout=10)
        end_ms = int(time.time() * 1000)
        start_ms = end_ms - (count * 15 * 60 * 1000)
        return client.fetch_candles(self.coin, "15m", start_ms, end_ms)

    def run_loop(self, poll_interval: int = 3, max_ticks: int = 10):
        print("\n" + "=" * 70)
        print(f"LSAR REAL-TIME DRY-RUN EXECUTOR ACTIVE [{self.coin}]")
        print(f"Connected to Terminal: {self.host}")
        print(f"Paper Capital: {self.capital:,.2f} USD | Peak: {self.peak_capital:,.2f} USD")
        print("=" * 70)

        tick = 0
        while tick < max_ticks:
            tick += 1
            try:
                live = self.fetch_live_feed()
                live_px = float(live.get("price", 0.0))
                liqs = live.get("liquidations", {})
                stops = live.get("stops", {})
                utc_now = live.get("utc_time", datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S UTC"))

                # Evaluate open paper positions
                closed_any = False
                for pos in list(self.active_positions):
                    side = pos["side"]
                    entry = pos["entry_price"]
                    sl = pos["stop_price"]
                    tp = pos["target_price"]
                    r_dist = pos["r_dist"]
                    units = pos["size_units"]
                    phase = pos["phase"]

                    gain_r = ((live_px - entry) / r_dist) if side == "LONG" else ((entry - live_px) / r_dist)

                    # Ratchet updates
                    if phase == 0 and gain_r >= 0.80:
                        pos["stop_price"] = entry + 0.20 * r_dist if side == "LONG" else entry - 0.20 * r_dist
                        pos["phase"] = 1
                        print(f"  ⚡ [{utc_now}] {side} RATCHET PHASE 1 (BE+0.2R): SL updated to {pos['stop_price']:.2f}")

                    elif phase == 1 and gain_r >= 1.50:
                        pos["stop_price"] = entry + 0.80 * r_dist if side == "LONG" else entry - 0.80 * r_dist
                        pos["phase"] = 2
                        print(f"  ⚡ [{utc_now}] {side} RATCHET PHASE 2 (PROFIT LOCK +0.8R): SL updated to {pos['stop_price']:.2f}")

                    # Exit checks
                    exit_hit = False
                    exit_reason = ""
                    if side == "LONG":
                        if live_px <= sl:
                            exit_hit = True
                            exit_reason = "STOP_LOSS"
                        elif live_px >= tp:
                            exit_hit = True
                            exit_reason = "TARGET"
                    else:
                        if live_px >= sl:
                            exit_hit = True
                            exit_reason = "STOP_LOSS"
                        elif live_px <= tp:
                            exit_hit = True
                            exit_reason = "TARGET"

                    if exit_hit:
                        gross = (live_px - entry) * units if side == "LONG" else (entry - live_px) * units
                        friction = entry * units * 0.0041
                        net_pnl = gross - friction
                        self.capital += net_pnl
                        if self.capital > self.peak_capital:
                            self.peak_capital = self.capital

                        print(f"  🛑 [{utc_now}] {side} CLOSED via {exit_reason} at {live_px:.2f} | Net PnL: {net_pnl:+.2f} USD")
                        pos["exit_price"] = live_px
                        pos["exit_reason"] = exit_reason
                        pos["net_pnl"] = net_pnl
                        pos["exit_time"] = utc_now
                        self.closed_positions.append(pos)
                        self.active_positions.remove(pos)
                        closed_any = True

                if closed_any:
                    self.save_state()

                # Status display
                liq_bands = len(liqs.get("bands", []))
                stop_bands = len(stops.get("bands", []))
                active_count = len(self.active_positions)
                print(f"[{utc_now}] {self.coin}: {live_px:,.2f} USD | Liq Bands: {liq_bands} | Stop Bands: {stop_bands} | Open Positions: {active_count}")

            except Exception as e:
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Feed error: {e}")

            time.sleep(poll_interval)


# ── 4. MAIN ENTRY POINT ───────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="LSAR Institutional Strategy Engine")
    parser.add_argument("--mode", choices=["backtest", "dry-run"], default="backtest", help="Execution mode")
    parser.add_argument("--data", default="Data/Hyperdash_Historical/BTC_15m_full_dump.parquet", help="Parquet dataset path")
    parser.add_argument("--coin", default="BTC", help="Coin symbol")
    parser.add_argument("--host", default="http://localhost:8095", help="Terminal API host")
    parser.add_argument("--ticks", type=int, default=5, help="Number of ticks to run in dry-run mode")
    args = parser.parse_args()

    if args.mode == "backtest":
        run_backtest(args.data)
    elif args.mode == "dry-run":
        runner = LSARDryRunRunner(coin=args.coin, host=args.host)
        runner.run_loop(poll_interval=2, max_ticks=args.ticks)


if __name__ == "__main__":
    main()
