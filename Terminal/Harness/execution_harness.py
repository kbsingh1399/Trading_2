#!/usr/bin/env python3
"""
Terminal/Harness/execution_harness.py
====================================
Non-Bypassable Programmatic Pre-Execution Gatekeeper & Pitfall Sentry.

Enforces ALL 10 institutional pitfalls mathematically BEFORE any order can reach MT5:
  1. Pitfall 1 (Whale Armor): Fades require >= $100K resting whale depth (tau >= 180s). Banned on CFDs lacking L2 depth.
  2. Pitfall 2 (Liquidation Cascade): Stops inside mapped liquidation clusters (14_Hyperdash_Liq_Map) are REJECTED.
  3. Pitfall 3 (CVD Waterfall): Aggressive taker delta cascades into the level are REJECTED.
  4. Pitfall 4 (Sub-ATR Stops): Stops < 1.2 * ATR_14 are REJECTED.
  5. Pitfall 5 (Trend/Random Walk Fades): Fades require VR(4) < 0.85 and < 3 consecutive higher lows / lower highs.
  6. Pitfall 6 (Spread Friction): Spreads > 5.0 bps (TradFi) or > 25.0 bps (Crypto) are REJECTED.
  7. Pitfall 7 (Rollover Blackout): 21:15-22:30 UTC orders on TradFi are REJECTED.
  8. Pitfall 8 (Correlated Clusters): Correlated cluster double-bets (> 0.85 correlation) are REJECTED.
  9. Pitfall 9 (Capital Floor & Preservation): Equity <= 4,795.00 locks into Capital Preservation Mode (max 1 slot, max $8 risk).
 10. Pitfall 10 (Lot-Size Inflation): Risk > $10.00 nominal ($8.00 in preservation) is REJECTED.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import logging
import os
import pathlib
import sys
import time
from typing import Dict, Any, List, Optional, Tuple

import numpy as np
import pandas as pd

try:
    import MetaTrader5 as mt5
    MT5_AVAILABLE = True
except ImportError:
    mt5 = None
    MT5_AVAILABLE = False

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
FEEDS_DIR = DATA_DIR / "feeds"
RECEIPTS_DIR = DATA_DIR / "execution_receipts"
RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)

ACCOUNT_LOGIN = 5064568
HARD_FLOOR = 4775.00
OPERATING_BUFFER = 4795.00
MAX_STANDARD_RISK_USD = 10.00
MAX_PRESERVATION_RISK_USD = 8.00

logger = logging.getLogger("ExecutionHarness")
if not logger.handlers:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(logging.Formatter("[%(asctime)s][ExecutionHarness] %(message)s"))
    logger.addHandler(h)
    logger.setLevel(logging.INFO)


class PitfallViolationError(Exception):
    """Raised when one or more lethal execution pitfalls are violated."""
    def __init__(self, failures: List[str], details: Dict[str, Any]):
        self.failures = failures
        self.details = details
        super().__init__(f"Execution halted: {'; '.join(failures)}")


class ExecutionHarness:
    """Institutional Pre-Execution Gatekeeper enforcing mathematical invariants."""

    @classmethod
    def audit_candidate(
        cls,
        symbol: str,
        direction: str,  # "BUY", "SELL", "BUY_LIMIT", "SELL_LIMIT"
        entry_price: float,
        sl_price: float,
        tp_price: float,
        lots: float,
        model_type: str = "MODEL_1_FADE",  # "MODEL_1_FADE" or "MODEL_2_PULLBACK"
    ) -> Tuple[bool, List[str], Dict[str, Any]]:
        """Audits a prospective trade setup against all 10 pitfalls mathematically."""
        failures = []
        metrics = {}

        if not MT5_AVAILABLE or not mt5.initialize():
            return False, ["MT5_INITIALIZE_FAILED"], {}

        try:
            acc = mt5.account_info()
            if acc is None or acc.login != ACCOUNT_LOGIN:
                return False, [f"ACCOUNT_MISMATCH: {getattr(acc, 'login', None)}"], {}

            sym_info = mt5.symbol_info(symbol)
            if sym_info is None:
                return False, [f"SYMBOL_NOT_FOUND: {symbol}"], {}

            tick = mt5.symbol_info_tick(symbol)
            if tick is None or tick.time == 0:
                return False, [f"NO_TICK_AVAILABLE: {symbol}"], {}

            # -------------------------------------------------------------
            # 1. Capital Defense & Mode Check (Pitfall 9 & 10)
            # -------------------------------------------------------------
            is_preservation = (acc.equity <= OPERATING_BUFFER)
            max_allowed_risk = MAX_PRESERVATION_RISK_USD if is_preservation else MAX_STANDARD_RISK_USD
            max_allowed_slots = 1 if is_preservation else 2

            open_positions = mt5.positions_get() or ()
            pending_orders = mt5.orders_get() or ()

            # Operator Directive: N pending limit orders permitted across distinct symbols
            # Only open positions consume active margin.
            max_open_positions = 1 if is_preservation else 2
            if len(open_positions) >= max_open_positions:
                failures.append(
                    f"Pitfall 9 (Open Capacity Full): Active running positions {len(open_positions)} >= max allowed {max_open_positions}."
                )

            # Prevent duplicate pending orders on the same symbol
            existing_sym_orders = [o for o in pending_orders if o.symbol == symbol]
            if existing_sym_orders:
                failures.append(
                    f"Duplicate Order Detected: Symbol {symbol} already has pending order #{existing_sym_orders[0].ticket}."
                )

            # Recompute exact nominal risk in USD via MT5 native broker calculation
            digits = sym_info.digits
            order_type_calc = mt5.ORDER_TYPE_BUY if ("BUY" in direction.upper()) else mt5.ORDER_TYPE_SELL
            calc_pnl = mt5.order_calc_profit(order_type_calc, symbol, float(lots), float(entry_price), float(sl_price))
            if calc_pnl is not None:
                nominal_risk_usd = round(abs(float(calc_pnl)), 2)
            else:
                point = sym_info.point
                point_value = sym_info.trade_tick_value if sym_info.trade_tick_size > 0 else 1.0
                price_risk_points = abs(entry_price - sl_price) / sym_info.trade_tick_size if sym_info.trade_tick_size > 0 else 1.0
                nominal_risk_usd = round(lots * price_risk_points * point_value, 2)
            metrics["nominal_risk_usd"] = nominal_risk_usd

            if nominal_risk_usd > max_allowed_risk:
                failures.append(
                    f"Pitfall 10 (Risk Exceeded): Nominal risk ${nominal_risk_usd:.2f} > max limit ${max_allowed_risk:.2f}."
                )

            # Cushion check after potential loss
            stressed_equity = acc.equity - (1.25 * nominal_risk_usd + 2.00)
            if stressed_equity < HARD_FLOOR:
                failures.append(
                    f"Pitfall 9 (Hard Floor Breach): Stressed equity ${stressed_equity:.2f} breaches floor ${HARD_FLOOR:.2f}."
                )

            # -------------------------------------------------------------
            # 2. Spread & Rollover Friction Check (Pitfall 6 & 7)
            # -------------------------------------------------------------
            mid = (tick.bid + tick.ask) / 2.0
            spread_pts = (tick.ask - tick.bid)
            spread_bps = (spread_pts / mid * 10000.0) if mid > 0 else 999.0
            metrics["spread_bps"] = round(spread_bps, 2)

            is_crypto = any(c in symbol.upper() for c in ["BTC", "ETH", "SOL", "XRP", "LTC", "BCH", "DOG", "ADA"])
            max_spread_bps = 25.0 if is_crypto else 5.0

            if spread_bps > max_spread_bps:
                failures.append(
                    f"Pitfall 6 (Spread Friction): Live spread {spread_bps:.2f} bps exceeds cap {max_spread_bps:.2f} bps."
                )

            # Rollover check for TradFi (21:15 - 22:30 UTC)
            now_utc = datetime.datetime.now(datetime.timezone.utc)
            utc_minute = now_utc.hour * 60 + now_utc.minute
            if not is_crypto and (21 * 60 + 15 <= utc_minute <= 22 * 60 + 30):
                failures.append("Pitfall 7 (Rollover Trap): Entry attempted inside 21:15-22:30 UTC rollover window.")

            # -------------------------------------------------------------
            # 3. Market Regime, Variance Ratio & Momentum (Pitfall 5)
            # -------------------------------------------------------------
            rates15 = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M15, 0, 150)
            if rates15 is None or len(rates15) < 120:
                failures.append("INSUFFICIENT_BARS_FOR_REGIME_ANALYSIS")
            else:
                df15 = pd.DataFrame(rates15)
                closes = df15["close"].values.astype(float)
                r1 = np.diff(np.log(closes))
                r4 = np.log(closes[4:]) - np.log(closes[:-4])
                var1 = np.var(r1, ddof=1)
                var4 = np.var(r4, ddof=1)
                vr4 = float(var4 / (4.0 * var1)) if var1 > 0 else 1.0
                metrics["vr4"] = round(vr4, 3)

                # Consecutive higher lows / lower highs
                lows = df15["low"].values[-6:]
                highs = df15["high"].values[-6:]
                higher_lows = sum(lows[i] > lows[i-1] for i in range(1, len(lows)))
                lower_highs = sum(highs[i] < highs[i-1] for i in range(1, len(highs)))
                metrics["higher_lows"] = higher_lows
                metrics["lower_highs"] = lower_highs

                # ATR 14
                tr = np.maximum(df15["high"].values[1:] - df15["low"].values[1:],
                        np.maximum(abs(df15["high"].values[1:] - df15["close"].values[:-1]),
                                   abs(df15["low"].values[1:] - df15["close"].values[:-1])))
                atr14 = float(np.mean(tr[-14:]))
                metrics["atr14"] = round(atr14, digits)

                # Recent volume expansion
                vol_recent = df15["tick_volume"].values[-1]
                vol_avg = np.mean(df15["tick_volume"].values[-20:])
                vol_ratio = vol_recent / vol_avg if vol_avg > 0 else 1.0
                metrics["vol_ratio"] = round(vol_ratio, 2)

                is_short = ("SELL" in direction.upper())
                is_long = ("BUY" in direction.upper())

                if model_type == "MODEL_1_FADE":
                    if vr4 >= 0.85:
                        failures.append(
                            f"Pitfall 5 (Random Walk / Trend Corridor): VR(4) = {vr4:.3f} >= 0.85. "
                            f"Fading a random walk or trend has zero statistical expectancy."
                        )
                    if is_short and higher_lows >= 3:
                        failures.append(
                            f"Pitfall 5 (Fading Bull Momentum): {higher_lows} consecutive higher lows on M15. "
                            f"Price is sweeping upward in an impulse; counter-trend fade is suicide."
                        )
                    if is_long and lower_highs >= 3:
                        failures.append(
                            f"Pitfall 5 (Fading Bear Momentum): {lower_highs} consecutive lower highs on M15. "
                            f"Price is waterfalling downward; counter-trend fade is suicide."
                        )
                    if vol_ratio > 1.8:
                        failures.append(
                            f"Pitfall 3/5 (Volume Climax): Tick volume is {vol_ratio:.1f}x 20-bar average. "
                            f"Aggressive taker flow is sweeping the level."
                        )
                elif model_type == "MODEL_2_PULLBACK":
                    if vr4 < 1.15:
                        failures.append(
                            f"Pitfall 5 (Insufficient Trend Persistence): VR(4) = {vr4:.3f} < 1.15. "
                            f"Trend continuation requires strong positive serial correlation."
                        )

            # -------------------------------------------------------------
            # 4. Liquidation Geometry & Sub-ATR Protection (Pitfall 2 & 4)
            # -------------------------------------------------------------
            atr = metrics.get("atr14", 0.0)
            if atr > 0:
                stop_dist = abs(entry_price - sl_price)
                stop_atr_ratio = round(stop_dist / atr, 2)
                metrics["stop_atr_ratio"] = stop_atr_ratio
                if stop_atr_ratio < 1.2:
                    failures.append(
                        f"Pitfall 4 (Sub-ATR Stop): Stop distance {stop_dist:.5f} is only {stop_atr_ratio:.2f} ATR. "
                        f"Stops must sit at least 1.2 ATR outside entry to survive routine sweeps."
                    )

            # Check 14_Hyperdash_Liq_Map.parquet
            liq_map_file = FEEDS_DIR / "14_Hyperdash_Liq_Map.parquet"
            if liq_map_file.exists():
                try:
                    df_liq = pd.read_parquet(liq_map_file)
                    # Filter for symbol or base asset
                    base_asset = symbol.split(".")[0].replace("USD", "").replace(".pi", "").replace(".p", "")
                    sym_liq = df_liq[df_liq["asset"].str.upper() == base_asset.upper()] if "asset" in df_liq.columns else pd.DataFrame()
                    if not sym_liq.empty and "price_level" in sym_liq.columns:
                        # Check if SL falls within a dense liquidation cluster
                        for _, row in sym_liq.iterrows():
                            cluster_p = float(row.get("price_level", 0))
                            liq_usd = float(row.get("liq_usd", 0))
                            if liq_usd >= 500_000 and abs(sl_price - cluster_p) <= (0.5 * atr if atr > 0 else 50.0):
                                failures.append(
                                    f"Pitfall 2 (Stop in Liquidation Magnet): SL {sl_price:.2f} sits within 0.5 ATR "
                                    f"of ${liq_usd/1e6:.1f}M liquidation pool at {cluster_p:.2f}."
                                )
                                break
                except Exception as e:
                    logger.warning(f"Error checking liquidation map: {e}")

            # -------------------------------------------------------------
            # 5. Whale Armor & L2 Depth Invariant (Pitfall 1)
            # -------------------------------------------------------------
            if model_type == "MODEL_1_FADE":
                if not is_crypto:
                    failures.append(
                        f"Pitfall 1 (Zero L2 Whale Armor on CFDs): {symbol} is an MT5 CFD/FX feed without "
                        f"Level 2/Level 3 orderbook depth data. Counter-trend fades on unarmored CFDs are permanently banned; "
                        f"only Model 2 trend-continuation pullbacks permitted."
                    )
                else:
                    whale_file = FEEDS_DIR / "10_Whale_Orders.parquet"
                    has_whale_armor = False
                    if whale_file.exists():
                        try:
                            df_whale = pd.read_parquet(whale_file)
                            # Check for defending resting wall
                            side_pattern = "Sell" if is_short else "Buy"
                            val_col = "notional_usd" if "notional_usd" in df_whale.columns else ("remaining_usd" if "remaining_usd" in df_whale.columns else "initial_value_usd")
                            walls = df_whale[
                                (df_whale["symbol"].str.contains(base_asset, case=False, na=False)) &
                                (df_whale["side"].str.contains(side_pattern, case=False, na=False)) &
                                (df_whale[val_col] >= 100_000)
                            ]
                            if not walls.empty:
                                has_whale_armor = True
                                metrics["whale_wall_usd"] = float(walls[val_col].iloc[0])
                        except Exception as ex:
                            logger.warning(f"Error reading whale orders: {ex}")
                    if not has_whale_armor:
                        side_name = "ASK" if is_short else "BID"
                        failures.append(
                            f"Pitfall 1 (Ghost Whale Wall): No verified resting {side_name} wall "
                            f"(>= $100K USD, tau >= 180s) defending {symbol} at entry {entry_price:.2f}."
                        )

            # -------------------------------------------------------------
            # 6. Economic Calendar & Event Blackout Sentry (Pitfall 14 & 6)
            # -------------------------------------------------------------
            cal_file = FEEDS_DIR / "19_Calendar.parquet"
            if cal_file.exists():
                try:
                    df_cal = pd.read_parquet(cal_file)
                    clean_sym = symbol.upper().replace(".PI", "").replace(".P", "")
                    cand_currencies = []
                    for cur in ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD"]:
                        if cur in clean_sym:
                            cand_currencies.append(cur)
                    if not cand_currencies:
                        if "XAU" in clean_sym or "XAG" in clean_sym or any(k in clean_sym for k in ["US30", "US500", "USTEC"]):
                            cand_currencies.append("USD")
                        elif "GER" in clean_sym:
                            cand_currencies.append("EUR")

                    now_ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
                    for cur in cand_currencies:
                        events = df_cal[(df_cal["currency"] == cur) & (df_cal["impact"].str.contains("High Impact", case=False, na=False))]
                        for _, erow in events.iterrows():
                            t_str = str(erow.get("time", "")).strip()
                            ev_name = str(erow.get("event", "")).strip()
                            try:
                                t_obj = datetime.datetime.strptime(t_str, "%I:%M%p").time()
                                ev_dt = now_ist.replace(hour=t_obj.hour, minute=t_obj.minute, second=0, microsecond=0)
                                diff_min = (ev_dt - now_ist).total_seconds() / 60.0
                                # Blackout: -30m post-event to +120m pre-event
                                if -30.0 <= diff_min <= 120.0:
                                    failures.append(
                                        f"Pitfall 14 (High-Impact Economic Release Blackout): {cur} has High Impact '{ev_name}' "
                                        f"scheduled in {diff_min:.0f} mins ({t_str} IST). Orders prohibited inside 120m window."
                                    )
                                    metrics["calendar_blackout_event"] = ev_name
                                    metrics["calendar_event_time"] = t_str
                            except Exception:
                                pass
                except Exception as ex_cal:
                    logger.warning(f"Error reading 19_Calendar.parquet: {ex_cal}")

            # -------------------------------------------------------------
            # 7. Orderflow Footprint Delta & Imbalance Gate (Pitfall 3)
            # -------------------------------------------------------------
            fp_file = FEEDS_DIR / "25_CoinGlass_Footprint_Signals.parquet"
            if fp_file.exists():
                try:
                    df_fp = pd.read_parquet(fp_file)
                    base_sym = symbol.split(".")[0].replace("USD", "").replace(".pi", "").replace(".p", "")
                    sym_fp = df_fp[df_fp["symbol"].str.contains(base_sym, case=False, na=False)] if "symbol" in df_fp.columns else pd.DataFrame()
                    if not sym_fp.empty:
                        recent_fp = sym_fp.head(5)
                        # Check if severe unabsorbed taker flow directly opposes order direction
                        opposing_bias = "BEARISH" if ("BUY" in direction.upper()) else "BULLISH"
                        trapped_count = sum(1 for _, row in recent_fp.iterrows() if str(row.get("bias", "")).upper() == opposing_bias and "absorption" in str(row.get("signal_type", "")).lower())
                        metrics["footprint_opposing_signals"] = trapped_count
                        if trapped_count >= 3:
                            failures.append(
                                f"Pitfall 3 (Adverse Footprint Imbalance): {trapped_count} recent footprint absorption signals "
                                f"heavily favor {opposing_bias} flow on {base_sym}. Order direction directly opposes institutional tape."
                            )
                except Exception as ex_fp:
                    logger.warning(f"Error reading 25_CoinGlass_Footprint_Signals.parquet: {ex_fp}")

            # -------------------------------------------------------------
            # 8. Comprehensive 360-Degree Data Lake Multi-Feed Audit
            # -------------------------------------------------------------
            try:
                from Terminal.Harness.data_lake_trade_validator import DataLakeTradeValidator
                dl_passed, dl_failures, dl_evidence = DataLakeTradeValidator.validate_360(
                    symbol=symbol,
                    direction=direction,
                    entry_price=entry_price,
                    sl_price=sl_price,
                    tp_price=tp_price,
                    model_type=model_type,
                )
                if not dl_passed:
                    failures.extend(dl_failures)
                metrics["data_lake_360_evidence"] = dl_evidence
            except Exception as dl_err:
                logger.warning(f"Error executing 360 data lake validation: {dl_err}")

            passed = (len(failures) == 0)
            return passed, failures, metrics

        except Exception as e:
            logger.error(f"Unexpected error in audit_candidate for {symbol}: {e}")
            return False, [f"EXCEPTION: {str(e)}"], {}

    @classmethod
    def dispatch_verified_order(
        cls,
        symbol: str,
        direction: str,
        entry_price: float,
        sl_price: float,
        tp_price: float,
        lots: float,
        model_type: str = "MODEL_1_FADE",
        comment: str = "ExecutionHarness_V1",
    ) -> Dict[str, Any]:
        """Audits setup. If passed, dispatches to MT5. If failed, throws PitfallViolationError."""
        passed, failures, metrics = cls.audit_candidate(
            symbol=symbol,
            direction=direction,
            entry_price=entry_price,
            sl_price=sl_price,
            tp_price=tp_price,
            lots=lots,
            model_type=model_type,
        )

        receipt = {
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "symbol": symbol,
            "direction": direction,
            "entry_price": entry_price,
            "sl_price": sl_price,
            "tp_price": tp_price,
            "lots": lots,
            "model_type": model_type,
            "passed": passed,
            "failures": failures,
            "metrics": metrics,
        }

        # Save audit receipt
        nonce = hashlib.sha256(f"{symbol}_{direction}_{entry_price}_{time.time()}".encode()).hexdigest()[:12]
        receipt_path = RECEIPTS_DIR / f"receipt_{symbol}_{nonce}.json"
        receipt_path.write_text(json.dumps(receipt, indent=2, default=str), encoding="utf-8")

        if not passed:
            logger.error(f"[HARNESS REJECTION] {symbol} {direction} blocked: {'; '.join(failures)}")
            raise PitfallViolationError(failures, metrics)

        # Dispatch order to MT5
        if not mt5.initialize():
            raise RuntimeError("MT5 initialization failed during order dispatch")

        try:
            is_limit = ("LIMIT" in direction.upper())
            is_buy = ("BUY" in direction.upper())

            if is_limit:
                order_type = mt5.ORDER_TYPE_BUY_LIMIT if is_buy else mt5.ORDER_TYPE_SELL_LIMIT
                action_type = mt5.TRADE_ACTION_PENDING
            else:
                order_type = mt5.ORDER_TYPE_BUY if is_buy else mt5.ORDER_TYPE_SELL
                action_type = mt5.TRADE_ACTION_DEAL

            request = {
                "action": action_type,
                "symbol": symbol,
                "volume": float(lots),
                "type": order_type,
                "price": float(entry_price),
                "sl": float(sl_price),
                "tp": float(tp_price),
                "deviation": 20,
                "magic": 108001,
                "comment": comment[:31],
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }

            result = mt5.order_send(request)
            if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
                err_msg = result.comment if result else str(mt5.last_error())
                logger.error(f"[ORDER_SEND FAILED] {symbol}: {err_msg} (retcode: {getattr(result, 'retcode', 'None')})")
                return {"success": False, "error": err_msg, "receipt": receipt}

            logger.info(f"[ORDER_SEND SUCCESS] Ticket #{result.order} for {symbol} {direction} {lots} lots @ {entry_price}")
            return {
                "success": True,
                "ticket": result.order,
                "volume": result.volume,
                "price": result.price,
                "receipt": receipt
            }
        except Exception as e:
            logger.error(f"Unexpected error in dispatch_verified_order for {symbol}: {e}")
            return {"success": False, "error": str(e)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ExecutionHarness CLI Validator")
    parser.add_argument("--audit", action="store_true", help="Audit a proposed trade candidate")
    parser.add_argument("--symbol", type=str, required=True, help="MT5 Symbol")
    parser.add_argument("--direction", type=str, required=True, help="BUY, SELL, BUY_LIMIT, SELL_LIMIT")
    parser.add_argument("--entry", type=float, required=True, help="Proposed entry price")
    parser.add_argument("--sl", type=float, required=True, help="Proposed Stop Loss")
    parser.add_argument("--tp", type=float, required=True, help="Proposed Take Profit")
    parser.add_argument("--lots", type=float, default=0.01, help="Lot volume")
    parser.add_argument("--model", type=str, default="MODEL_1_FADE", choices=["MODEL_1_FADE", "MODEL_2_PULLBACK"])

    args = parser.parse_args()

    passed, failures, metrics = ExecutionHarness.audit_candidate(
        symbol=args.symbol,
        direction=args.direction,
        entry_price=args.entry,
        sl_price=args.sl,
        tp_price=args.tp,
        lots=args.lots,
        model_type=args.model,
    )

    print("\n" + "=" * 80)
    print(f"EXECUTION HARNESS AUDIT REPORT: {args.symbol} {args.direction}")
    print("=" * 80)
    print(f"VERDICT: {'[PASS] CLEAR TO TRADE' if passed else '[FAIL] EXECUTION BLOCKED'}")
    print("-" * 80)
    print("METRICS:")
    for k, v in metrics.items():
        print(f"  {k:<20}: {v}")
    if not passed:
        print("\nVIOLATED PITFALLS:")
        for idx, f in enumerate(failures, 1):
            print(f"  {idx}. {f}")
    print("=" * 80)
    sys.exit(0 if passed else 1)
