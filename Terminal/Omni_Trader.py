"""Single-writer 16-asset execution loop. Network inference cannot place orders."""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import copy
import datetime as dt
import hashlib
import json
import math
import os
import time
import urllib.request
import uuid
from Terminal.Asset_Universe import UNIVERSE, canonical_asset
from Terminal.Risk_Sizing_Engine import (RiskPolicy, OrderflowModel, CovarianceGate, fit_covariance,
                                        size_trade, cost_bps, epoch, number, completed_statistics)
from Terminal.Uplift_Model import (UpliftGate, executable_ratchet, ratchet_params, session_regime,
                                   asset_class_of, POLICY_VERSION, RATCHET_POLICY_VERSION)
from Terminal.Commodity_Microstructure import gk_vol
from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
from Terminal.Market_Intelligence import MarketIntelligenceEngine
from Terminal.Cognitive_Engine import CognitiveEngine
from Terminal.Orderbook_Structure import (wall_clusters, hazard_ttl, structural_exit, classify_sleeve,
                                          anchors_from_clusters)
from Terminal.Order_Persistence_Governor import OrderPersistenceGovernor
from Terminal.Deterministic_Features import FeatureSealer

ROOT = Path(__file__).resolve().parents[1]
MAGIC = 100895

def compute_pivot_levels(bars, tick_size=0.01):
    """Computes daily pivot points, intraday swing extremes, Anchored VWAP with sigma bands,
    and ICT Fair Value Gaps (FVG) with Consequent Encroachment (CE 50% midpoint) from completed bars."""
    if not bars: return None
    window = bars[-96:] if len(bars) >= 96 else bars
    h = max(b["high"] for b in window)
    l = min(b["low"] for b in window)
    c = window[-1]["close"]
    p = (h + l + c) / 3.0
    r1 = 2 * p - l
    s1 = 2 * p - h
    r2 = p + (h - l)
    s2 = p - (h - l)
    swing_window = bars[-8:] if len(bars) >= 8 else bars
    swing_high = max(b["high"] for b in swing_window)
    swing_low = min(b["low"] for b in swing_window)

    # Anchored VWAP and standard deviation bands over window
    cum_vol = 0.0
    cum_vol_price = 0.0
    for b in window:
        tp_bar = (b["high"] + b["low"] + b["close"]) / 3.0
        v = float(b.get("volume") or b.get("tick_volume") or 0.0)
        if v > 0:
            cum_vol += v
            cum_vol_price += tp_bar * v
    if cum_vol > 0:
        vwap = cum_vol_price / cum_vol
        variance_sum = 0.0
        for b in window:
            tp_bar = (b["high"] + b["low"] + b["close"]) / 3.0
            v = float(b.get("volume") or b.get("tick_volume") or 0.0)
            if v > 0:
                variance_sum += v * ((tp_bar - vwap) ** 2)
        vwap_sigma = math.sqrt(variance_sum / cum_vol)
        vwap_valid = True
        vwap_upper_1 = vwap + vwap_sigma
        vwap_lower_1 = vwap - vwap_sigma
        vwap_upper_2 = vwap + 2.0 * vwap_sigma
        vwap_lower_2 = vwap - 2.0 * vwap_sigma
    else:
        vwap = None
        vwap_sigma = None
        vwap_valid = False
        vwap_upper_1 = vwap_lower_1 = vwap_upper_2 = vwap_lower_2 = None

    # ICT Fair Value Gaps (FVG) detection on recent bars
    recent = bars[-24:] if len(bars) >= 24 else bars
    bull_fvg_list = []
    bear_fvg_list = []
    if len(recent) >= 3:
        for i in range(2, len(recent)):
            b_prev2 = recent[i-2]
            b_curr = recent[i]
            if b_curr["low"] > b_prev2["high"]:
                gap_low = b_prev2["high"]
                gap_high = b_curr["low"]
                subsequent_lows = [recent[k]["low"] for k in range(i+1, len(recent))]
                min_subsequent = min(subsequent_lows) if subsequent_lows else gap_high
                ce = (gap_low + gap_high) / 2.0
                ce_untouched = min_subsequent > ce
                if min_subsequent > gap_low and ce_untouched:
                    bull_fvg_list.append({"low": gap_low, "high": gap_high, "ce": ce, "bar_index": i, "ce_untouched": ce_untouched})
            if b_curr["high"] < b_prev2["low"]:
                gap_low = b_curr["high"]
                gap_high = b_prev2["low"]
                subsequent_highs = [recent[k]["high"] for k in range(i+1, len(recent))]
                max_subsequent = max(subsequent_highs) if subsequent_highs else gap_low
                ce = (gap_low + gap_high) / 2.0
                ce_untouched = max_subsequent < ce
                if max_subsequent < gap_high and ce_untouched:
                    bear_fvg_list.append({"low": gap_low, "high": gap_high, "ce": ce, "bar_index": i, "ce_untouched": ce_untouched})

    bull_fvg_ce = bull_fvg_list[-1]["ce"] if bull_fvg_list else None
    bear_fvg_ce = bear_fvg_list[-1]["ce"] if bear_fvg_list else None

    return {"P": p, "S1": s1, "R1": r1, "S2": s2, "R2": r2,
            "swing_high": swing_high, "swing_low": swing_low,
            "h24": h, "l24": l, "c24": c,
            "vwap": vwap, "vwap_sigma": vwap_sigma,
            "vwap_upper_1": vwap_upper_1, "vwap_lower_1": vwap_lower_1,
            "vwap_upper_2": vwap_upper_2, "vwap_lower_2": vwap_lower_2,
            "bull_fvg_ce": bull_fvg_ce, "bear_fvg_ce": bear_fvg_ce,
            "bull_fvgs": bull_fvg_list, "bear_fvgs": bear_fvg_list}

class AI15mMT5Trader:
    def __init__(self, coin="SOL", host="http://localhost:8095", paper_mode=True,
                 risk_usd=10, min_risk_usd=10, max_risk_usd=45, cadence_minute=14,
                 cadence_second=30, entry_mode="market", account_id=None,
                 max_spread_points=None, state_file=None, allow_list=None, *,
                 bridge=None, intel=None, cognitive=None, covariance=None, uplift=None,
                 covariance_path=None, uplift_path=None, policy=None, clock=time.time,
                 fetcher=None, cognitive_enabled=True, journal_dir=None,
                 limit_expiration_seconds=3600, ttl_min_seconds=7200.0, ttl_max_seconds=21600.0,
                 persistent_limits=True):
        if cadence_minute != 14 or not 0 <= cadence_second <= 50:
            raise ValueError("Entries must be scheduled in minute 14 before the candle close")
        if entry_mode not in ("market", "limit"):
            raise ValueError("entry_mode must be 'market' or 'limit'")
        self.entry_mode = entry_mode
        self.limit_expiration_seconds = int(limit_expiration_seconds)
        self.coin, self.host, self.paper_mode = canonical_asset(coin), host.rstrip("/"), paper_mode
        self.policy = policy or RiskPolicy(min_risk=min_risk_usd, max_risk=max_risk_usd, max_book_age=30.0, max_future_skew_sec=30.0)
        self.assets = tuple(canonical_asset(a) for a in (allow_list or UNIVERSE))
        if any(a not in UNIVERSE for a in self.assets) or len(set(self.assets)) != len(self.assets): raise ValueError("Invalid asset allow-list")
        self.clock, self.cadence_second, self.max_spread_points = clock, cadence_second, max_spread_points
        self.bridge = bridge or MT5ExecutionBridge(account_id=account_id)
        self.intel = intel or MarketIntelligenceEngine(clock=clock)
        self.cognitive = cognitive or CognitiveEngine()
        self.cognitive_enabled = cognitive_enabled
        self.covariance_path = Path(covariance_path or ROOT/"Data/Hyperdash_Historical/ledoit_wolf_covariance.parquet")
        self.fitted_covariance_path = self.covariance_path.with_name(self.covariance_path.stem+".omni.parquet")
        self.covariance, self.covariance_error = covariance, None
        self.uplift = uplift or UpliftGate(uplift_path or ROOT/"Data/Models/omni_uplift")
        self.state_file = Path(state_file or ROOT/"Data"/("omni_paper_state.json" if paper_mode else "mt5_ai_trader_state.json"))
        self.journal_dir = Path(journal_dir or ROOT/"Data/Omni"/("paper" if paper_mode else "live"))
        self.journal_dir.mkdir(parents=True, exist_ok=True)
        self.state = {"schema": "omni.state.v1", "original_capital_usd": 5000.0, "capital_usd": 5000.0,
                      "peak_equity_usd": 5000.0, "halted": False,
                      "last_slot": -1, "positions": {}, "intents": {}, "paper_positions": [], "paper_cash": 5000.0}
        if self.state_file.exists():
            loaded = json.loads(self.state_file.read_text(encoding="utf-8"))
            # Preserve the user's ledger fields on migration; a malformed state is fatal.
            self.state.update(loaded)
            orig_cap = self.policy.initial_capital
            self.state["original_capital_usd"] = orig_cap
            self.state["peak_equity_usd"] = max(orig_cap, number(loaded.get("peak_equity_usd", loaded.get("peak_equity", orig_cap))))
            if "last_slot" not in loaded:
                prior_pass = epoch((loaded.get("last_360_report") or {}).get("timestamp"))
                if prior_pass: self.state["last_slot"] = int(prior_pass//900)
        self.flow = OrderflowModel(self.policy, self.state.get("normalizer"), self.state.get("walls"))
        # Order Persistence Governor (Incident A): owns multi-hour resting
        # limit orders, dynamic TTL and wall-tracking cancel/replace. Runs on
        # the ~1s manage cadence, never inside the minute-14 decision window.
        self.ttl_min_seconds, self.ttl_max_seconds = float(ttl_min_seconds), float(ttl_max_seconds)
        self.persistent_limits = bool(persistent_limits)
        self.governor = OrderPersistenceGovernor(self.bridge, journal=self._append, clock=self.clock,
                                                 ttl_min_sec=self.ttl_min_seconds, ttl_max_sec=self.ttl_max_seconds)
        self.governor.load(self.state.get("resting_orders"))
        # Tamper-proof feature seals (Incident B): per-asset hash chain.
        self.sealer = FeatureSealer(self.state.get("feature_chain"))
        self.fetcher = fetcher or self._fetch
        # Pioneer conviction layer (consultation 4): advisory/veto-only. It can
        # suppress a NEW entry on data-quality or opposed-conviction grounds;
        # it never sizes, forces, or touches an open position or an exit.
        self.pioneer = None
        self.pool = ThreadPoolExecutor(max_workers=8, thread_name_prefix="omni-data")
        self.intel_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="omni-macro")
        self.inference_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="omni-inference")
        self.fetches, self.payloads, self.symbols, self.bars = {}, {}, {}, {}
        self.macro_future, self.macro = None, {}
        self.last_prefetch = self.last_bars = self.last_macro = -math.inf
        self.last_report = {}
        self._lock_fd = None
        if self.covariance is None:
            for path in (self.covariance_path, self.fitted_covariance_path):
                try: self.covariance = CovarianceGate.load(path); break
                except Exception as exc: self.covariance_error = str(exc)

    def _append(self, name, record):
        with open(self.journal_dir/name, "a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, allow_nan=False, default=str)+"\n")
            stream.flush(); os.fsync(stream.fileno())

    def _sync_external_state(self):
        if not self.state_file.exists(): return
        try:
            mtime = self.state_file.stat().st_mtime
            if getattr(self, "_last_state_mtime", 0) > 0 and mtime > self._last_state_mtime + 0.05:
                external = json.loads(self.state_file.read_text(encoding="utf-8"))
                self.state["halted"] = bool(self.state["halted"] or external.get("halted"))
                self.state["original_capital_usd"] = self.policy.initial_capital
                self.state["peak_equity_usd"] = max(self.state["peak_equity_usd"], number(external.get("peak_equity_usd")))
            self._last_state_mtime = mtime
        except Exception: pass

    def unhalt(self, reason: str = "operator_recovery"):
        """Explicitly reset the drawdown halt latch and persist."""
        self.state["halted"] = False
        self._append("risk_events.jsonl", {"time": self.clock(), "event": "unhalt", "reason": reason})
        self._save_state()

    def _save_state(self):
        self._sync_external_state()
        resolved = [key for key, value in self.state["intents"].items() if value["status"] in ("REJECTED", "RECONCILED", "RECONCILED_CLOSED", "EXPIRED")]
        for key in resolved[:-32]: del self.state["intents"][key]
        self.state["normalizer"] = self.flow.normalizer.export()
        self.state["walls"] = self.flow.walls
        self.state["resting_orders"] = self.governor.export()
        self.state["feature_chain"] = self.sealer.export()
        self.state["latest_report"] = self.last_report
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.state_file.with_suffix(self.state_file.suffix+".tmp")
        with open(temporary, "w", encoding="utf-8") as stream:
            json.dump(self.state, stream, allow_nan=False, default=str)
            stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, self.state_file)
        try: self._last_state_mtime = self.state_file.stat().st_mtime
        except Exception: pass

    def _fetch(self, asset):
        with urllib.request.urlopen(self.host+"/api/live/"+asset, timeout=3.0) as response:
            payload = json.loads(response.read())
        if canonical_asset(payload.get("coin")) != asset: raise ValueError("Signal asset mismatch")
        return payload

    def refresh_background(self):
        now = self.clock()
        for asset, future in list(self.fetches.items()):
            if future.done():
                try:
                    self.payloads[asset] = future.result()
                    self.flow.observe_walls(asset, self.payloads[asset], now)
                except Exception as exc: self._append("feed_errors.jsonl", {"time": now, "asset": asset, "error": str(exc)})
                del self.fetches[asset]
        if now-self.last_prefetch >= 5:
            for asset in self.assets:
                if asset not in self.fetches: self.fetches[asset] = self.pool.submit(self.fetcher, asset)
            self.last_prefetch = now
        if self.macro_future and self.macro_future.done():
            try: self.macro = self.macro_future.result(); self.macro["received_at"] = now
            except Exception as exc: self._append("feed_errors.jsonl", {"time": now, "asset": "MACRO", "error": str(exc)})
            self.macro_future = None
        if now-self.last_macro >= 300 and self.macro_future is None:
            self.macro_future = self.intel_pool.submit(self.intel.get_market_intelligence_report)
            self.last_macro = now

    def refresh_broker_history(self):
        now = self.clock()
        if now-self.last_bars < 900: return
        for asset in self.assets:
            symbol = self.bridge.resolve_symbol(asset)
            if symbol:
                self.symbols[asset] = symbol
                self.bars[asset] = self.bridge.get_recent_bars(symbol, count=512)
        self.last_bars = now
        is_valid = False
        if self.covariance:
            try:
                self.covariance.validate_time(now, self.policy.covariance_horizon_minutes)
                if all(a in self.covariance.index for a in self.bars):
                    is_valid = True
            except Exception:
                is_valid = False
        if is_valid:
            return
        try:
            self.covariance = fit_covariance(self.bars, now, self.fitted_covariance_path)
            self.covariance_error = None
            self._append("risk_events.jsonl", {"time": now, "event": "covariance_refit", "metadata": self.covariance.metadata})
        except (ValueError, OSError, ImportError) as exc:
            self.covariance_error = str(exc)

    def _quote(self, symbol):
        quote = self.bridge.get_symbol_price(symbol)
        if not quote or not 0 < number(quote.get("bid")) < number(quote.get("ask")): raise ValueError("broker_quote_invalid")
        age = self.clock()-epoch(quote.get("time_msc"))
        max_skew = max(15.0, getattr(self.policy, "max_future_skew_sec", 15.0))
        max_age = max(15.0, getattr(self.policy, "max_book_age", 15.0))
        if not -max_skew <= age <= max_age: raise ValueError("broker_quote_stale_or_future")
        return quote

    def _own(self, position): return int(position.get("magic", 0)) == MAGIC or str(position.get("ticket")) in self.state["positions"]

    def _inventory(self):
        # Read live inventory even in paper mode so disconnected IPC cannot masquerade as a healthy broker.
        actual = self.bridge.get_open_positions()
        pending = self.bridge.get_pending_orders()
        if self.paper_mode: return copy.deepcopy(self.state["paper_positions"]), []
        return actual, pending

    def _account(self, positions):
        account = self.bridge.get_account_summary()
        if not account.get("connected") or account.get("currency") != "USD": raise ValueError("USD_broker_account_required")
        if not self.paper_mode:
            login = account.get("login")
            if not login: raise ValueError("broker_account_identity_unavailable")
            if self.state.get("account_login") not in (None, login): raise ValueError("persisted_state_account_mismatch")
            self.state["account_login"] = login
        if self.paper_mode:
            equity = self.state["paper_cash"]
            for p in positions:
                q = self._quote(p["symbol"]); sign = 1 if p["direction"] == "LONG" else -1
                px = q["bid"] if sign == 1 else q["ask"]
                equity += sign*(px-p["price_open"])*p["volume"]*p["contract_size"]-p["residual_cost_usd"]
            account = dict(account, equity_usd=equity, balance_usd=self.state["paper_cash"], margin_free_usd=self.state["paper_cash"])
        return account

    def _equity_guard(self, account):
        equity = number(account.get("equity_usd"))
        orig_cap = self.policy.initial_capital
        peak = max(self.state.get("peak_equity_usd", orig_cap), equity, orig_cap)
        floor = max(orig_cap*(1-0.045), peak-orig_cap*0.045)
        self.state["peak_equity_usd"] = peak
        emergency_marker = not self.paper_mode and (ROOT/"Data/Omni/live/emergency_halt.json").exists()
        self.state["halted"] = bool(self.state["halted"] or equity <= floor or emergency_marker)
        return {"equity_usd": equity, "peak_equity_usd": peak, "hard_floor_usd": floor,
                "drawdown_room": max(0, equity-floor), "halted": self.state["halted"],
                "risk_cap_usd": self._risk_cap(equity)}

    def _risk_cap(self, equity):
        return 10.0 if equity < 4800.0 else min(20.0, self.policy.max_risk)

    def _reconcile(self, positions, pending):
        pending_tickets = {int(o.get("ticket", 0)) for o in pending}
        for key, intent in self.state["intents"].items():
            if intent["status"] not in ("PREPARED", "ACKNOWLEDGED", "UNCERTAIN", "STAGED_LIMIT", "ABANDONED"): continue
            # Aged unresolved intents deadlock all future entries
            # ("unresolved_execution_intent"). Only demote when the broker can
            # prove no fill ever happened; without history evidence the
            # intent is conservatively kept (fail-closed).
            if intent["status"] in ("PREPARED", "ACKNOWLEDGED", "UNCERTAIN") and not self.paper_mode:
                age = self.clock()-number(intent.get("prepared_at"))
                limit = 120.0 if intent["status"] == "PREPARED" else 300.0
                if age > limit and not self._bridge_intent_filled(intent):
                    intent["status"] = "ABANDONED"
                    self._append("executions.jsonl", {"time": self.clock(), "event": "intent_aged_out",
                                                      "intent_id": key, "age": age})
            matched = [p for p in positions if p.get("comment") == intent["comment"] and int(p.get("magic", 0)) == MAGIC]
            if matched:
                if len(matched) != 1: raise ValueError("ambiguous_order_reconciliation")
                p = matched[0]; intent["status"] = "RECONCILED"; intent["position_ticket"] = p["ticket"]
                metadata = copy.deepcopy(intent["candidate"])
                metadata["price_open"] = p["price_open"]
                metadata["initial_r"] = abs(p["price_open"]-metadata["sl"])
                metadata["time"] = p["time"]
                metadata["volume"] = p["volume"]
                metadata["identifier"] = p.get("identifier", p["ticket"])
                # Check price drift at fill vs planned entry price (Finding H-09)
                planned_px = intent["candidate"].get("price_open", p["price_open"])
                planned_r = intent["candidate"].get("initial_r", metadata["initial_r"])
                drift = abs(p["price_open"]-planned_px)
                if planned_r > 0 and drift > 0.05 * planned_r:
                    self._append("executions.jsonl", {"time": self.clock(), "event": "fill_drift_warning",
                                                      "intent_id": key, "drift": drift, "planned_px": planned_px, "fill_px": p["price_open"]})
                self.state["positions"][str(p["ticket"])] = metadata
                self._append("executions.jsonl", {"time": self.clock(), "event": "reconciled", "intent_id": key, "position": p})
                quote = self._quote(p["symbol"])
                if p.get("sl", 0) <= 0:
                    self._close(p, "filled_without_protective_sl")
                else:
                    estimate = self.bridge.estimate_order(p["symbol"], p["direction"], p["price_open"], metadata["sl"])
                    actual_risk = p["volume"]*(estimate["stop_loss_per_lot"]+quote["contract_size"]*p["price_open"]*cost_bps(quote, self.policy)/10000)
                    if actual_risk > min(45, metadata["risk_usd"])+0.01:
                        self._close(p, "fill_exceeded_planned_risk")
            elif intent["status"] == "STAGED_LIMIT":
                ticket = intent.get("order_ticket")
                if ticket and ticket not in pending_tickets:
                    # The order vanished between the two IPC inventory
                    # snapshots. A fill inside that race window must never be
                    # mistaken for an expiry (Finding F-04): check deal
                    # history before declaring EXPIRED.
                    resolution = self._resolve_vanished_limit(key, intent)
                    if resolution == "uncertain":
                        continue
            elif not self.paper_mode and hasattr(self.bridge, "reconcile_intent_history"):
                history = self.bridge.reconcile_intent_history(intent["comment"], intent["prepared_at"])
                if history and history["state"] == "FILLED_CLOSED":
                    intent["status"] = "RECONCILED_CLOSED"
                    self._append("outcomes.jsonl", {"intent_id": key, "available_at": self.clock(), **history})
                    meta = intent["candidate"]
                    if meta.get("cognitive_snapshot") and meta.get("cognitive_decision"):
                        self.cognitive.record_outcome(meta["cognitive_snapshot"], meta["cognitive_decision"], history)
            # Absence of inventory/history still cannot prove a send failed.
        active_tickets = {str(p["ticket"]) for p in positions}
        if not self.paper_mode:
            for ticket, meta in list(self.state["positions"].items()):
                if ticket in active_tickets: continue
                deals = self.bridge.position_deals(meta.get("identifier", int(ticket)))
                if not any(d["entry"] in (1, 2, 3) for d in deals): continue
                outcome = {"ticket": ticket, "deals": deals, "net_pnl_usd": sum(number(d.get(k)) for d in deals for k in ("profit_usd", "commission_usd", "swap_usd", "fee_usd")), "available_at": self.clock()}
                self._append("outcomes.jsonl", outcome)
                if meta.get("cognitive_snapshot") and meta.get("cognitive_decision"):
                    self.cognitive.record_outcome(meta["cognitive_snapshot"], meta["cognitive_decision"], outcome)
                del self.state["positions"][ticket]

    def _bridge_intent_filled(self, intent):
        """True iff the broker shows fill evidence for this intent's comment.

        Returns True (conservative: never age out) when the bridge cannot
        answer, so evidence-free demotion is impossible.
        """
        try:
            if hasattr(self.bridge, "intent_filled"):
                return bool(self.bridge.intent_filled(intent["comment"], number(intent.get("prepared_at"))))
        except (RuntimeError, ValueError, OSError):
            return True
        return True

    def _resolve_vanished_limit(self, key, intent):
        """Classify a pending limit that disappeared from the broker inventory.

        Returns "filled_closed", "filled_open", "expired" or "uncertain".
        A fill inside the inventory race window is reconciled from deal
        history instead of being silently marked EXPIRED (Finding F-04).
        """
        ticket = intent.get("order_ticket")
        if not self.paper_mode:
            try:
                if hasattr(self.bridge, "reconcile_intent_history"):
                    history = self.bridge.reconcile_intent_history(intent["comment"], intent["prepared_at"])
                    if history and history["state"] == "FILLED_CLOSED":
                        intent["status"] = "RECONCILED_CLOSED"
                        self._append("outcomes.jsonl", {"intent_id": key, "available_at": self.clock(), **history})
                        meta = intent["candidate"]
                        if meta.get("cognitive_snapshot") and meta.get("cognitive_decision"):
                            self.cognitive.record_outcome(meta["cognitive_snapshot"], meta["cognitive_decision"], history)
                        return "filled_closed"
                if hasattr(self.bridge, "intent_filled") and bool(self.bridge.intent_filled(intent["comment"], number(intent.get("prepared_at")))):
                    # Filled and still open: it will reconcile from the next
                    # position snapshot via the comment match above.
                    intent["status"] = "ACKNOWLEDGED"
                    self._append("executions.jsonl", {"time": self.clock(), "event": "limit_filled_pending_reconcile",
                                                      "intent_id": key, "ticket": ticket})
                    return "filled_open"
            except RuntimeError:
                return "uncertain"
        intent["status"] = "EXPIRED"
        self._append("executions.jsonl", {"time": self.clock(), "event": "limit_expired", "intent_id": key,
                                          "ticket": ticket, "fill_checked": not self.paper_mode})
        return "expired"

    def _flatten(self, positions, pending, reason):
        for order in pending:
            if reason == "hard_drawdown_stop" or int(order.get("magic", 0)) == MAGIC:
                result = self.bridge.cancel_pending_order(order["ticket"])
                self._append("executions.jsonl", {"time": self.clock(), "event": "cancel", "reason": reason, "result": result})
        for p in positions:
            if reason == "hard_drawdown_stop" or self._own(p): self._close(p, reason)

    def _close(self, position, reason):
        ticket = str(position["ticket"])
        metadata = self.state["positions"].setdefault(ticket, {})
        is_emergency = reason in ("hard_drawdown_stop", "unprotected_position")
        if metadata.get("close_uncertain") and not is_emergency:
            if self.clock() - number(metadata.get("close_requested_at", 0)) < 3.0:
                return
        if self.paper_mode:
            q = self._quote(position["symbol"]); sign = 1 if position["direction"] == "LONG" else -1
            px = q["bid"] if sign == 1 else q["ask"]
            pnl = sign*(px-position["price_open"])*position["volume"]*position["contract_size"]-position["residual_cost_usd"]
            self.state["paper_cash"] += pnl
            self.state["paper_positions"] = [p for p in self.state["paper_positions"] if p["ticket"] != position["ticket"]]
            self.state["positions"].pop(ticket, None)
            result = {"success": True, "paper": True, "ticket": ticket, "price": px, "net_pnl_usd": pnl}
            self._append("outcomes.jsonl", {"time": self.clock(), **result})
            if metadata.get("cognitive_snapshot") and metadata.get("cognitive_decision"):
                self.cognitive.record_outcome(metadata["cognitive_snapshot"], metadata["cognitive_decision"], result)
        else:
            metadata["close_uncertain"] = True
            metadata["close_requested_at"] = self.clock()
            self._save_state()
            result = self.bridge.close_position(int(ticket))
            if result.get("success"):
                metadata["close_uncertain"] = False
                self.state["positions"].pop(ticket, None)
            else:
                metadata["close_uncertain"] = bool(result.get("uncertain", True))
        self._append("executions.jsonl", {"time": self.clock(), "event": "close", "reason": reason, "result": result})
        self._save_state()

    def manage_active_positions(self, *unused):
        positions, pending = self._inventory()
        account = self._account(positions); guard = self._equity_guard(account)
        if guard["halted"]:
            self._save_state()
            self._flatten(positions, pending, "hard_drawdown_stop")
            self._reconcile(positions, pending)
            return [{"event": "hard_drawdown_stop", **guard}]
        self._reconcile(positions, pending)
        changes = []
        for p in positions:
            if not self._own(p): continue
            key = str(p["ticket"]); meta = self.state["positions"].setdefault(key, {})
            try:
                q = self._quote(p["symbol"])
                entry = number(p["price_open"]); sign = 1 if p["direction"] == "LONG" else -1
                initial_r = number(meta.get("initial_r", self.state.get("position_r_dist", {}).get(key)))
                if initial_r <= 0 and sign*(entry-number(p.get("sl"))) > 0 and number(p.get("sl")) > 0:
                    initial_r = abs(entry-p["sl"]); meta["initial_r"] = initial_r
                if not number(p.get("sl")):
                    self._close(p, "unprotected_position"); continue
                if initial_r <= 0:
                    if self.clock()-epoch(p["time"]) >= 24*900: self._close(p, "initial_r_unknown_at_time_limit")
                    changes.append({"ticket": key, "reason": "initial_r_unknown_keep_protective_sl"}); continue
                px = q["bid"] if sign == 1 else q["ask"]
                gain = sign*(px-entry)/initial_r
                meta["max_favorable_r"] = max(number(meta.get("max_favorable_r")), gain)
                if self.paper_mode and (sign*(px-p["sl"]) <= 0 or (number(p.get("tp")) > 0 and sign*(px-p["tp"]) >= 0)):
                    self._close(p, "paper_bracket"); continue
                asset = meta.get("asset", canonical_asset(p["symbol"]))
                # Session-conditional exit overlay (Q3): asset class x GK-vol
                # regime x UTC session x sleeve. Labels keep the uniform v2
                # policy; live management runs the conditional ladder.
                cls = asset_class_of(asset)
                session = session_regime(self.clock(), cls)
                bars_asset = self.bars.get(asset) or []
                gk14 = gk_vol(bars_asset, lookback=14, now=self.clock())
                gk96 = gk_vol(bars_asset, lookback=96, now=self.clock())
                gk_ratio = gk14/gk96 if gk96 > 0 else 1.0
                sleeve = "trend" if meta.get("sleeve") == "T1_BREAKOUT" else "reversion"
                params = ratchet_params(asset, session=session, gk_ratio=gk_ratio, sleeve=sleeve)
                meta["ratchet_regime"] = {"policy": RATCHET_POLICY_VERSION, "session": session,
                                          "vol_bucket": params["vol_bucket"], "gk_ratio": round(gk_ratio, 3),
                                          "sleeve": sleeve, "params": params}
                if (self.clock()-epoch(p["time"]) >= params["decay_bars"]*900
                        and meta["max_favorable_r"] < 0.20):
                    self._close(p, f"{params['decay_bars']}_bar_time_decay"); continue
                stats = completed_statistics(bars_asset, self.clock()) if bars_asset else {}
                atr = number(stats.get("atr"), number(meta.get("atr"), initial_r*0.5))
                tick_size = max(number(q.get("tick_size")), number(q.get("point")))
                distance = max(number(q.get("stops_level")), number(q.get("freeze_level")), 1)*q["point"]
                friction_bps = number(meta.get("sizing", {}).get("friction_bps", meta.get("friction_bps", self.policy.minimum_friction_bps)))
                proposed = executable_ratchet(entry, initial_r, p["direction"], gain, p["sl"], atr,
                                              q["bid"], q["ask"], tick_size, distance,
                                              friction_bps=friction_bps, buffer_r=0.05, params=params)
                if proposed != p["sl"]:
                    if self.paper_mode:
                        for stored in self.state["paper_positions"]:
                            if stored["ticket"] == p["ticket"]: stored["sl"] = proposed
                        result = {"success": True, "ticket": key, "sl": proposed, "paper": True}
                    else: result = self.bridge.modify_position_sltp(int(p["ticket"]), proposed, p.get("tp"))
                    changes.append(result); self._append("executions.jsonl", {"time": self.clock(), "event": "ratchet", "gain_r": gain, "result": result})
            except (ValueError, RuntimeError) as exc:
                changes.append({"ticket": key, "error": str(exc)})

        # First-Fill OCO Governor: If open positions reach capacity (2), purge all pending limit orders
        if len(positions) >= 2 and pending:
            for order in list(pending):
                oticket = int(order.get("ticket", 0))
                if int(order.get("magic", 0)) == MAGIC or any(v.get("order_ticket") == oticket for v in self.state.get("intents", {}).values()):
                    res = self.bridge.cancel_pending_order(oticket)
                    self._append("executions.jsonl", {"time": self.clock(), "event": "oco_capacity_cancel", "ticket": oticket, "reason": "max_positions_reached_2", "result": res})
                    changes.append({"ticket": str(oticket), "action": "CANCEL", "reason": "max_positions_reached_2"})
            pending = []
        elif len(positions) == 1 and pending:
            active_p = positions[0]
            active_asset = self.state["positions"].get(str(active_p["ticket"]), {}).get("asset", canonical_asset(active_p["symbol"]))
            for order in list(pending):
                oticket = int(order.get("ticket", 0))
                if int(order.get("magic", 0)) == MAGIC or any(v.get("order_ticket") == oticket for v in self.state.get("intents", {}).values()):
                    rem_sym = order.get("symbol")
                    rem_asset = canonical_asset(rem_sym)
                    rem_dir = order.get("direction", "LONG")
                    if self.covariance and active_asset != rem_asset:
                        try:
                            corr = self.covariance.correlation(rem_asset, active_asset)
                            if corr >= 0.55 and rem_dir == active_p.get("direction"):
                                res = self.bridge.cancel_pending_order(oticket)
                                self._append("executions.jsonl", {"time": self.clock(), "event": "oco_correlated_cancel", "ticket": oticket, "reason": f"correlated_with_active_{active_asset}_corr_{corr:.2f}", "result": res})
                                changes.append({"ticket": str(oticket), "action": "CANCEL", "reason": f"correlated_with_active_{active_asset}_corr_{corr:.2f}"})
                                pending = [o for o in pending if int(o.get("ticket", 0)) != oticket]
                        except Exception:
                            pass

        # Dynamic pending order monitoring & structural invalidation
        for order in pending:
            oticket = int(order.get("ticket", 0))
            if int(order.get("magic", 0)) == MAGIC or any(v.get("ticket") == oticket or v.get("order_ticket") == oticket for v in self.state.get("intents", {}).values()):
                sym = order.get("symbol")
                asset = canonical_asset(sym)
                direction = order.get("direction", "LONG")

                # Check 1: Macro blackout active
                blackout, event, _ = self.intel.check_macro_blackout()
                if blackout:
                    res = self.bridge.cancel_pending_order(oticket)
                    self._append("executions.jsonl", {"time": self.clock(), "event": "cancel_pending", "ticket": oticket, "reason": f"macro_blackout:{event}", "result": res})
                    changes.append({"ticket": str(oticket), "action": "CANCEL", "reason": f"macro_blackout:{event}"})
                    continue

                # Check 2: Price drifted far from limit (max(6*ATR, 3% of mid)
                # - production drift bound: wide enough for weekend gaps,
                # tight enough to recycle dead queue priority)
                bars = self.bars.get(asset, [])
                if bars:
                    try:
                        stats = completed_statistics(bars, self.clock())
                        atr = stats.get("atr", 0.0)
                        quote = self._quote(sym)
                        if quote and atr > 0:
                            mid = (number(quote["bid"]) + number(quote["ask"])) / 2.0
                            limit_px = number(order.get("price_open", 0.0))
                            if limit_px > 0 and abs(mid - limit_px) > max(6.0 * atr, 0.03 * mid):
                                res = self.bridge.cancel_pending_order(oticket)
                                self._append("executions.jsonl", {"time": self.clock(), "event": "cancel_pending", "ticket": oticket, "reason": "price_drifted_far_from_limit", "result": res})
                                changes.append({"ticket": str(oticket), "action": "CANCEL", "reason": "price_drifted_far_from_limit"})
                                continue
                    except (ValueError, KeyError):
                        pass

        # Order Persistence Governor heartbeat (Incident A): dynamic TTL,
        # wall-pull cancel / cancel-replace and drift bounds for resting
        # persistent limit orders. Runs on every manage cycle so multi-hour
        # orders never depend on the 15-minute decision cadence.
        if not self.paper_mode and self.governor.count():
            try:
                changes.extend(self.governor.heartbeat(now=self.clock(), intents=self.state["intents"],
                                                       payloads=self.payloads, pending=pending,
                                                       quote_fn=self._quote))
            except Exception as exc:
                self._append("runtime_errors.jsonl", {"time": self.clock(), "event": "governor_heartbeat_failed",
                                                      "error": str(exc)})

        self._save_state()
        return changes

    def _portfolio_exposure(self, positions, guard):
        exposure, stop_reserve = {}, 0.0
        enriched = []
        for p in positions:
            q = self._quote(p["symbol"]); sign = 1 if p["direction"] == "LONG" else -1
            asset = self.state["positions"].get(str(p["ticket"]), {}).get("asset", canonical_asset(p["symbol"]))
            mid = (q["bid"]+q["ask"])/2; notional = mid*q["contract_size"]*p["volume"]
            exposure[asset] = exposure.get(asset, 0)+sign*notional
            if number(p.get("sl")) <= 0: raise ValueError("portfolio_has_unprotected_position")
            mark = q["bid"] if sign == 1 else q["ask"]
            stop_reserve += max(0, sign*(mark-p["sl"]))*q["contract_size"]*p["volume"]+notional*cost_bps(q, self.policy)/10000
            meta = self.state["positions"].get(str(p["ticket"]), {})
            initial_r = number(meta.get("initial_r")) or abs(p["price_open"]-p["sl"])
            if initial_r <= 0: raise ValueError("portfolio_initial_r_unknown")
            enriched.append({**p, "asset": asset, "initial_r": initial_r, "contract_size": q["contract_size"],
                             "profit_usd": sign*(mark-p["price_open"])*p["volume"]*q["contract_size"],
                             "tick_size": max(number(q.get("tick_size")), q["point"]),
                             "stop_distance": max(number(q.get("stops_level")), number(q.get("freeze_level")), 1)*q["point"],
                             "residual_cost_usd": number(meta.get("residual_cost_usd")), "atr": number(meta.get("atr"), initial_r*0.5)})
        return exposure, max(0, guard["drawdown_room"]-stop_reserve), enriched

    def evaluate_market(self, multi_data=None, macro=None, force=False):
        now = self.clock(); slot = int(now//900); elapsed = now-slot*900
        report = {"time": now, "slot": slot, "decision": "HOLD", "candidates": [], "vetoes": {}}
        # force permits a research evaluation, never bypasses the live cadence.
        if not (840+self.cadence_second <= elapsed < 898) and not (force and self.paper_mode):
            return {**report, "reason": "outside_execution_window"}
        if self.state["last_slot"] >= slot: return {**report, "reason": "slot_already_evaluated"}
        if multi_data is None and self.fetches and any(a not in self.payloads for a in self.assets) and elapsed < 888:
            return {**report, "reason": "waiting_for_initial_feeds"}
        data = multi_data if multi_data is not None else self.payloads
        for asset in self.assets:
            if asset not in data: report["vetoes"][asset] = "signal_data_unavailable"
        self.state["last_slot"] = slot
        self._save_state()  # A crash during inference cannot repeat this decision slot.
        positions, pending = self._inventory()
        account = self._account(positions); guard = self._equity_guard(account)
        if not guard["halted"]: self._reconcile(positions, pending)
        blackout, event, _ = self.intel.check_macro_blackout()
        macro = dict(macro or self.macro)
        if not 0 <= self.clock()-number(macro.get("received_at"), 0) <= 900:
            macro.update(asset_scores={}, sentiment_valid=False)
        macro["blackout_active"] = blackout
        active_limits = sum(1 for i in self.state["intents"].values() if i["status"] == "STAGED_LIMIT")
        if guard["halted"]:
            self._save_state(); self._flatten(positions, pending, "hard_drawdown_stop")
            report.update(decision="HARD_DD_VETO", reason="sticky_drawdown_latch")
        elif blackout: report.update(decision="MACRO_VETO", reason=event)
        elif self.entry_mode == "limit" and (len(positions) >= 2 or active_limits >= 5):
            # Decoupled gates (production): 2 max FILLED, 5 max RESTING
            # limits; the first-fill OCO governor purges pendings when
            # positions reach capacity.
            report.update(reason="max_filled_2" if len(positions) >= 2 else "max_resting_limits_5")
        elif self.entry_mode != "limit" and len(positions) + active_limits >= 2:
            # Market mode keeps the coupled commitment cap: an instant fill
            # plus a resting limit is already two risk legs.
            report.update(reason="maximum_two_positions")
        elif any(i["status"] in ("PREPARED", "ACKNOWLEDGED", "UNCERTAIN") for i in self.state["intents"].values()):
            report.update(reason="unresolved_execution_intent")
        else:
            try:
                if self.covariance is None: raise ValueError("covariance_unavailable:"+str(self.covariance_error))
                self.covariance.validate_time(now, self.policy.covariance_horizon_minutes)
                existing, room, enriched = self._portfolio_exposure(positions, guard)
                candidates = []
                for asset, payload in data.items():
                    if asset not in self.assets: continue
                    symbol = self.symbols.get(asset) or self.bridge.resolve_symbol(asset)
                    if not symbol or any(p["symbol"] == symbol for p in positions): continue
                    try:
                        bars = self.bars.get(asset) or self.bridge.get_recent_bars(symbol, count=96)
                        features = self.flow.features(asset, payload, bars, macro, now)
                        if features.get("coverage_missing"):
                            raise ValueError("unobserved_corridor_veto:no_visible_depth_for_target_fuel")
                        if features.get("ffr") is not None and features["ffr"] < getattr(self.policy, "min_ffr", 0.50):
                            raise ValueError(f"dense_friction_veto:ffr_{features['ffr']:.3f}_below_min_{getattr(self.policy, 'min_ffr', 0.50):.2f}")
                        if features["confluence"] < self.policy.min_confluence: raise ValueError("confluence_below_threshold")
                        # Pioneer cross-validated conviction (consultation 4):
                        # veto-only consult - quality floor, staleness, blackout
                        # and opposed conviction suppress NEW entries; aligned or
                        # neutral conviction passes through with its sealed digest.
                        if self.pioneer is not None:
                            advisory = self.pioneer.evaluate(asset, payload, features, macro, now)
                            if not advisory.get("tradeable"):
                                raise ValueError(f"pioneer_veto:{advisory.get('reason')}")
                            features["pioneer"] = {k: advisory.get(k) for k in
                                                   ("conviction", "advice", "min_favorable_move_bps",
                                                    "quality_score", "digest")}
                        # Sector Correlation Governor: Check against existing portfolio positions
                        for p in positions:
                            existing_asset = self.state["positions"].get(str(p["ticket"]), {}).get("asset", canonical_asset(p["symbol"]))
                            existing_dir = p.get("direction")
                            if self.covariance and existing_asset != asset and existing_dir:
                                corr = None
                                try:
                                    corr = self.covariance.correlation(asset, existing_asset)
                                except (ValueError, KeyError):
                                    corr = None
                                if corr is not None:
                                    if abs(corr) >= 0.60:
                                        raise ValueError(f"sector_correlation_conflict:{asset}_{features['direction']}_shares_{existing_asset}_{existing_dir}_corr_{corr:.2f}")
                        quote = self._quote(symbol)
                        mid = (quote["bid"]+quote["ask"])/2
                        if abs(math.log(mid/features["signal_mid"]))/features["sigma_h"] > self.policy.max_basis_sigma:
                            raise ValueError("signal_broker_basis_dislocation")
                        sign = 1 if features["direction"] == "LONG" else -1
                        tick = max(number(quote.get("tick_size")), quote["point"])
                        digits = int(quote.get("digits", 2))
                        atr = features["atr"]
                        pivots = compute_pivot_levels(bars, tick)
                        # Sleeve decoupling (Incident C): S1 pullbacks rest
                        # passively ahead of verified absorption walls; T1
                        # breakouts enter aggressively into liquidity vacuums.
                        # Classification is deterministic and cannot be
                        # overridden by the cognitive layer.
                        features["sleeve"] = classify_sleeve(features)
                        effective_mode = "market" if features["sleeve"] == "T1_BREAKOUT" else self.entry_mode
                        l3 = payload.get("l3_orders", [])
                        entry_anchors = []

                        if effective_mode == "limit":
                            min_broker_dist = (max(number(quote.get("stops_level", 0)), number(quote.get("freeze_level", 0)), 1) + 2) * quote["point"]
                            if features["direction"] == "LONG":
                                # Verified whale bid clusters (freshness-gated by the
                                # feed's own observed_at stamp; the previous inline
                                # freshness clause could never fire - Finding F-02).
                                bid_clusters = wall_clusters(l3, "BUY", quote["bid"] - 2.5*atr, quote["bid"], now)
                                whale_bids = [c["edge_price"] for c in bid_clusters]
                                bull_fvg_ce = pivots.get("bull_fvg_ce") if pivots else None
                                vwap_lower = pivots.get("vwap_lower_1") if pivots else None
                                vwap = pivots.get("vwap") if pivots else None

                                # Limit Entry Hierarchy for LONGs:
                                if whale_bids:
                                    raw_entry = min(max(whale_bids) + tick, quote["bid"] - min_broker_dist)
                                elif bull_fvg_ce and quote["bid"] - 2.5*atr <= bull_fvg_ce <= quote["bid"] - min_broker_dist:
                                    raw_entry = bull_fvg_ce
                                elif vwap_lower and quote["bid"] - 2.5*atr <= vwap_lower <= quote["bid"] - min_broker_dist:
                                    raw_entry = vwap_lower
                                elif vwap and quote["bid"] - 2.5*atr <= vwap <= quote["bid"] - min_broker_dist:
                                    raw_entry = vwap
                                elif pivots and quote["bid"] - 2.5*atr <= pivots["S1"] <= quote["bid"] - min_broker_dist:
                                    raw_entry = pivots["S1"]
                                elif pivots and quote["bid"] - 2.5*atr <= pivots["P"] <= quote["bid"] - min_broker_dist:
                                    raw_entry = pivots["P"]
                                else:
                                    raw_entry = quote["bid"] - max(0.4*atr, min_broker_dist)
                                max_entry = min(quote["bid"] - tick, quote["ask"] - min_broker_dist)
                                entry = round(min(raw_entry, max_entry), digits)
                                swing_anchor = pivots["swing_low"] - 2*tick if pivots else entry - 1.5*atr
                                whale_shield = min(whale_bids) - 2*tick if whale_bids else swing_anchor
                                sl_cap = entry - min_broker_dist
                                raw_sl = min(entry - 1.5*atr, swing_anchor, whale_shield, sl_cap)
                                sl = round(math.floor(raw_sl / tick) * tick, digits)
                                if entry - sl < min_broker_dist:
                                    sl = round(math.floor((entry - min_broker_dist) / tick) * tick, digits)
                                r = abs(entry - sl)
                                if r > 2.5*atr:
                                    raise ValueError(f"stop_width_runaway:{r/max(atr, 1e-12):.2f}atr_beyond_liquidity_shield")
                                # Anchors handed to the persistence governor: the
                                # clusters this passive bid front-runs.
                                entry_anchors = anchors_from_clusters(bid_clusters, entry, "BUY")
                            else:
                                ask_clusters = wall_clusters(l3, "SELL", quote["ask"], quote["ask"] + 2.5*atr, now)
                                whale_asks = [c["edge_price"] for c in ask_clusters]
                                bear_fvg_ce = pivots.get("bear_fvg_ce") if pivots else None
                                vwap_upper = pivots.get("vwap_upper_1") if pivots else None
                                vwap = pivots.get("vwap") if pivots else None

                                # Limit Entry Hierarchy for SHORTs:
                                if whale_asks:
                                    raw_entry = max(min(whale_asks) - tick, quote["ask"] + min_broker_dist)
                                elif bear_fvg_ce and quote["ask"] + min_broker_dist <= bear_fvg_ce <= quote["ask"] + 2.5*atr:
                                    raw_entry = bear_fvg_ce
                                elif vwap_upper and quote["ask"] + min_broker_dist <= vwap_upper <= quote["ask"] + 2.5*atr:
                                    raw_entry = vwap_upper
                                elif vwap and quote["ask"] + min_broker_dist <= vwap <= quote["ask"] + 2.5*atr:
                                    raw_entry = vwap
                                elif pivots and quote["ask"] + min_broker_dist <= pivots["R1"] <= quote["ask"] + 2.5*atr:
                                    raw_entry = pivots["R1"]
                                elif pivots and quote["ask"] + min_broker_dist <= pivots["P"] <= quote["ask"] + 2.5*atr:
                                    raw_entry = pivots["P"]
                                else:
                                    raw_entry = quote["ask"] + max(0.4*atr, min_broker_dist)
                                min_entry = max(quote["ask"] + tick, quote["bid"] + min_broker_dist)
                                entry = round(max(raw_entry, min_entry), digits)
                                swing_anchor = pivots["swing_high"] + 2*tick if pivots else entry + 1.5*atr
                                whale_shield = max(whale_asks) + 2*tick if whale_asks else swing_anchor
                                sl_floor = entry + min_broker_dist
                                raw_sl = max(entry + 1.5*atr, swing_anchor, whale_shield, sl_floor)
                                sl = round(math.ceil(raw_sl / tick) * tick, digits)
                                if sl - entry < min_broker_dist:
                                    sl = round(math.ceil((entry + min_broker_dist) / tick) * tick, digits)
                                r = abs(entry - sl)
                                if r > 2.5*atr:
                                    raise ValueError(f"stop_width_runaway:{r/max(atr, 1e-12):.2f}atr_beyond_liquidity_shield")
                                entry_anchors = anchors_from_clusters(ask_clusters, entry, "SELL")
                            tp_min_dist = min_broker_dist
                        else:
                            entry = quote["ask"] if features["direction"] == "LONG" else quote["bid"]
                            min_dist = (max(quote.get("stops_level", 0), quote.get("freeze_level", 0))+2)*quote["point"]+(quote["ask"]-quote["bid"])
                            r = max(1.5*features["atr"], min_dist)
                            sl = (math.floor((entry-r)/tick) if sign == 1 else math.ceil((entry+r)/tick))*tick
                            r = abs(entry-sl)
                            tp_min_dist = min_dist
                        estimate = self.bridge.estimate_order(symbol, features["direction"], entry, sl)
                        features["risk_intent_usd"] = min(features["risk_intent_usd"], guard["risk_cap_usd"])
                        sizing = size_trade(quote, estimate["stop_loss_per_lot"], features["risk_intent_usd"], self.covariance,
                                            existing, asset, features["direction"], self.policy, room, number(account["margin_free_usd"]), estimate["margin_per_lot"])
                        if not sizing["accepted"]: raise ValueError(sizing["reason"])
                        friction_r = sizing["friction_usd"]/sizing["stop_risk_usd"]
                        # Orderbook-aware structural take-profit (Incident C):
                        # scan the top L3 clusters on the profit side and snap
                        # the TP to front-run the first major wall instead of
                        # staging an arbitrary fixed-R target beyond it. The
                        # R-hurdle flexes with wall geometry and is vetoed when
                        # the net-of-friction payoff cannot clear the floor.
                        overhead_side = "SELL" if sign == 1 else "BUY"
                        overhead_lo, overhead_hi = (entry, entry + 3.5*r) if sign == 1 else (entry - 3.5*r, entry)
                        overhead = wall_clusters(l3, overhead_side, overhead_lo, overhead_hi, now,
                                                 min_notional_usd=2_000_000.0, min_persistence_sec=0.0)
                        exit_plan, exit_veto = structural_exit(entry, sl, features["direction"], overhead,
                                                               tick=tick, friction_r=friction_r,
                                                               min_broker_dist=max(tp_min_dist, tick))
                        if exit_veto: raise ValueError(exit_veto)
                        tp = round(exit_plan["tp"], digits)
                        target_r = exit_plan["hurdle_r"]
                        if target_r-friction_r < 1.5: raise ValueError("net_payoff_insufficient_after_friction")
                        if self.max_spread_points is not None and (quote["ask"]-quote["bid"])/quote["point"] > self.max_spread_points:
                            raise ValueError("spread_limit")
                        # Lot estimates used by paper replay are USD-valued linear CFDs only.
                        if quote.get("currency_profit") not in (None, "USD"): raise ValueError("non_USD_profit_currency_unsupported")
                        candidate = {"candidate_id": f"{slot}:{asset}:{features['direction']}", "asset": asset,
                                     "symbol": symbol, "direction": features["direction"], "volume": sizing["volume"],
                                     "price_open": entry, "sl": sl, "tp": tp, "initial_r": r, "time": now,
                                     "atr": features["atr"], "contract_size": quote["contract_size"], "magic": MAGIC,
                                     "tick_size": tick, "stop_distance": max(quote.get("stops_level", 0), quote.get("freeze_level", 0), 1)*quote["point"],
                                     "residual_cost_usd": max(0, sizing["friction_usd"]-sizing["volume"]*quote["contract_size"]*(quote["ask"]-quote["bid"])),
                                     "risk_usd": sizing["risk_usd"], "features": features, "sizing": sizing, "payload": payload,
                                     "sleeve": features["sleeve"], "entry_mode": effective_mode,
                                     "hurdle_r": target_r, "tp_mode": exit_plan["mode"],
                                     "tp_wall_price": exit_plan["wall_price"],
                                     "tp_wall_notional_usd": exit_plan["wall_notional_usd"],
                                     "entry_anchors": entry_anchors}
                        uplift_features = {**features, **sizing, "drawdown_room": room, "candidate_net_target_r": target_r-friction_r,
                                           "existing_floating_r": 0.0, "existing_age_bars": 0.0, "signed_correlation": 0.0}
                        if enriched:
                            p = enriched[0]; same = 1 if p["direction"] == candidate["direction"] else -1
                            uplift_features.update(existing_floating_r=number(p.get("profit_usd"))/(p["initial_r"]*p["volume"]*p["contract_size"]),
                                                   existing_age_bars=(now-epoch(p["time"]))/900,
                                                   signed_correlation=same*self.covariance.correlation(asset, p["asset"]))
                            episode = {"episode_id": candidate["candidate_id"], "as_of": now, "equity_usd": guard["equity_usd"],
                                       "hard_floor_usd": guard["hard_floor_usd"], "existing_positions": enriched,
                                       "candidate": {k: v for k, v in candidate.items() if k not in ("payload", "features", "sizing")},
                                       "features": uplift_features, "policy_version": POLICY_VERSION}
                            self._append("uplift_episodes.jsonl", episode)
                            gate = self.uplift.decide(uplift_features, now)
                            candidate["uplift"] = gate
                            if not gate["accepted"]: raise ValueError(gate["reason"])
                        candidates.append(candidate)
                        report["candidates"].append({"asset": asset, "direction": candidate["direction"], "features": features, "sizing": sizing})
                    except (ValueError, KeyError, RuntimeError) as exc: report["vetoes"][asset] = str(exc)
                candidates.sort(key=lambda c: c["features"]["confluence"]*c["features"]["quality"], reverse=True)
                if candidates:
                    deadline = slot*900+898
                    if self.entry_mode == "limit":
                        # Decoupled staging cap: fill the resting-limit book to
                        # 5; the first-fill OCO governor enforces the 2-fill cap.
                        max_stageable = max(0, 5 - active_limits)
                    else:
                        max_stageable = max(0, 2 - len(positions) - len(pending))
                    staged_results = []
                    dispatched_candidates = []

                    last_result = None
                    for cand in candidates:
                        if len(staged_results) >= max_stageable:
                            break
                        cand_sym = cand["symbol"]
                        cand_asset = cand["asset"]
                        if any(p["symbol"] == cand_sym for p in positions) or any(o.get("symbol") == cand_sym for o in pending):
                            continue
                        if any(c["symbol"] == cand_sym for c in dispatched_candidates):
                            continue

                        corr_conflict = False
                        for p in positions:
                            pos_asset = self.state["positions"].get(str(p["ticket"]), {}).get("asset", canonical_asset(p["symbol"]))
                            if self.covariance and pos_asset != cand_asset:
                                try:
                                    if abs(self.covariance.correlation(cand_asset, pos_asset)) >= 0.60:
                                        corr_conflict = True; break
                                except Exception: pass
                        if corr_conflict:
                            continue
                        for already in dispatched_candidates:
                            if self.covariance and already["asset"] != cand_asset:
                                try:
                                    if abs(self.covariance.correlation(cand_asset, already["asset"])) >= 0.60:
                                        corr_conflict = True; break
                                except Exception: pass
                        if corr_conflict:
                            continue

                        if self.cognitive_enabled:
                            payload = cand["payload"]
                            # Sealed deterministic features (Incident B): the
                            # cognitive engine receives only the tamper-proof
                            # vector; its numeric prose is attested against it.
                            sealed = self.sealer.update(cand["asset"], cand["features"])
                            snapshot = self.cognitive.build_snapshot(cand["asset"], cand["symbol"], cand["features"]["signal_mid"], cand["features"],
                                                                     payload.get("l3_orders", []), payload.get("liquidations", {}).get("bands", []),
                                                                     {"score": cand["features"]["macro_score"], "blackout": False},
                                                                     {"equity": guard["equity_usd"], "slots": 2 - len(positions) - len(staged_results)}, {},
                                                                     sealed=sealed)
                            cand["feature_digest"] = sealed["digest"]
                            snapshot["candidate"] = {"candidate_id": cand["candidate_id"], "direction": cand["direction"], "sizing": cand["sizing"],
                                                     "sleeve": cand["sleeve"], "hurdle_r": cand["hurdle_r"],
                                                     "tp": cand["tp"], "sl": cand["sl"], "price_open": cand["price_open"]}
                            snapshot["sources"] = payload.get("sources", {})
                            snapshot["whale_positions"] = payload.get("whale_positions", [])
                            snapshot["projected_liquidations"] = payload.get("projected_liquidations", {})
                            snapshot["observed_stops"] = payload.get("observed_stops", {})
                            budget = max(0.1, min(6, deadline - self.clock()))
                            future = self.inference_pool.submit(self.cognitive.evaluate_snapshot, snapshot, cand["direction"], budget_seconds=budget)
                            wall_deadline = time.monotonic() + budget
                            next_management = 0.0
                            while not future.done() and time.monotonic() < wall_deadline:
                                if time.monotonic() >= next_management:
                                    self.manage_active_positions(); self.capture_quotes()
                                    next_management = time.monotonic() + 1
                                time.sleep(0.05)
                            decision = future.result() if future.done() else None
                            if not decision or decision.get("action") != "SELECT":
                                self._append("decisions.jsonl", {"time": self.clock(), "candidate_id": cand["candidate_id"], "event": "cognitive_abstention"})
                                continue
                        if cand.get("entry_mode", self.entry_mode) == "limit":
                            if cand["direction"] == "LONG" and cand["price_open"] >= quote["ask"]:
                                continue
                            if cand["direction"] == "SHORT" and cand["price_open"] <= quote["bid"]:
                                continue
                            px = cand["price_open"]
                        else:
                            px = quote["ask"] if cand["direction"] == "LONG" else quote["bid"]
                            if abs(px - cand["price_open"]) > 0.05 * cand["initial_r"]:
                                continue
                        # Staleness gate must reflect the freshest polled book,
                        # not the book snapshot the candidate was built from:
                        # refresh_background keeps polling during inference, and
                        # rejecting on the original stamp wastes the entire
                        # cognitive wait (Finding F-03).
                        fresh_book = epoch((self.payloads.get(cand["asset"]) or {}).get("l2_book", {}).get("timestamp")) \
                            or cand["features"]["book_as_of"]
                        if self.clock() - fresh_book > self.policy.max_book_age:
                            continue

                        refreshed_positions, refreshed_pending = self._inventory()
                        fresh_account = self._account(refreshed_positions)
                        fresh_guard = self._equity_guard(fresh_account)
                        if fresh_guard["halted"] or self.intel.check_macro_blackout()[0]:
                            break

                        estimate = self.bridge.estimate_order(cand["symbol"], cand["direction"], px, cand["sl"])
                        existing, room, _ = self._portfolio_exposure(refreshed_positions, fresh_guard)
                        dispatch_risk = min(cand["risk_usd"], fresh_guard["risk_cap_usd"])
                        recheck = size_trade(quote, estimate["stop_loss_per_lot"], dispatch_risk, self.covariance, existing, cand["asset"],
                                             cand["direction"], self.policy, room, fresh_account["margin_free_usd"], estimate["margin_per_lot"])
                        if not recheck["accepted"]:
                            continue
                        final_volume = min(cand["volume"], recheck["volume"])
                        ratio = final_volume / recheck["volume"] if recheck["volume"] > 0 else 1.0
                        for key in ("risk_usd", "stop_risk_usd", "friction_usd", "signed_notional_usd"):
                            recheck[key] *= ratio
                        recheck["volume"] = final_volume
                        final_exposures = dict(existing)
                        final_exposures[cand["asset"]] = final_exposures.get(cand["asset"], 0) + recheck["signed_notional_usd"]
                        recheck["variance_after"] = self.covariance.variance(final_exposures)
                        recheck["incremental_variance"] = recheck["variance_after"] - recheck["variance_before"]
                        cand.update(volume=final_volume, price_open=px, initial_r=abs(px - cand["sl"]), sizing=recheck, risk_usd=recheck["risk_usd"])
                        cand["residual_cost_usd"] = max(0, recheck["friction_usd"] - final_volume * quote["contract_size"] * (quote["ask"] - quote["bid"]))

                        if refreshed_positions:
                            _, _, enriched_now = self._portfolio_exposure(refreshed_positions, fresh_guard)
                            p = enriched_now[0]
                            fresh_uplift = {**cand["features"], **recheck, "drawdown_room": room,
                                            "existing_floating_r": p["profit_usd"] / (p["initial_r"] * p["volume"] * p["contract_size"]),
                                            "existing_age_bars": (self.clock() - epoch(p["time"])) / 900,
                                            "signed_correlation": (1 if p["direction"] == cand["direction"] else -1) * self.covariance.correlation(cand["asset"], p["asset"]),
                                            "candidate_net_target_r": abs(cand["tp"] - px) / cand["initial_r"] - recheck["friction_usd"] / recheck["stop_risk_usd"]}
                            gate = self.uplift.decide(fresh_uplift, self.clock())
                            self._append("uplift_dispatch_checks.jsonl", {"time": self.clock(), "candidate_id": cand["candidate_id"], "features": fresh_uplift, "gate": gate})
                            if not gate["accepted"]:
                                continue

                        result = self._dispatch(cand, slot)
                        last_result = result
                        if result.get("success"):
                            staged_results.append(result)
                            dispatched_candidates.append(cand)
                        elif result.get("uncertain"):
                            break

                    if staged_results:
                        if self.paper_mode:
                            report.update(decision="PAPER_FILLED", execution=staged_results[0], staged_count=len(staged_results))
                        elif self.entry_mode == "limit":
                            report.update(decision="LIMIT_STAGED", staged_count=len(staged_results), staged_assets=[c["asset"] for c in dispatched_candidates], execution=staged_results[0])
                        else:
                            report.update(decision="ORDER_FILLED", execution=staged_results[0])
                    elif last_result is not None:
                        dec = "ORDER_UNCERTAIN" if last_result.get("uncertain") else "ORDER_REJECTED"
                        report.update(decision=dec, execution=last_result)
                    else:
                        report.update(decision="NO_DISPATCH", reason="candidates_rejected_or_abstained")
            except (ValueError, RuntimeError, KeyError) as exc: report["reason"] = str(exc)
        self.last_report = report
        self._append("decisions.jsonl", report); self._save_state()
        print(json.dumps({k: v for k, v in report.items() if k != "candidates"}, default=str), flush=True)
        return report

    def attach_pioneer(self, engine):
        """Attach the Pioneer conviction layer (advisory/veto-only)."""
        self.pioneer = engine
        return engine

    def _dispatch(self, candidate, slot):
        key = hashlib.sha256(f"{slot}:{candidate['candidate_id']}".encode()).hexdigest()[:20]
        comment = "OMNI:"+key
        if key in self.state["intents"]: raise ValueError("duplicate_execution_intent")
        stored = {k: copy.deepcopy(v) for k, v in candidate.items() if k != "payload"}
        stored["comment"] = comment
        intent = {"status": "PREPARED", "comment": comment, "candidate": stored, "prepared_at": self.clock()}
        self.state["intents"][key] = intent; self._save_state()
        self._append("executions.jsonl", {"time": self.clock(), "event": "intent_prepared", "intent_id": key, "candidate": stored})
        if self.paper_mode:
            ticket = "paper-"+key
            position = {**stored, "ticket": ticket, "profit_usd": 0.0, "time": self.clock()}
            self.state["paper_positions"].append(position); self.state["positions"][ticket] = stored
            intent["status"] = "RECONCILED"
            result = {"success": True, "ticket": ticket, "paper": True, "volume": candidate["volume"], "price": candidate["price_open"]}
        else:
            if candidate.get("entry_mode", self.entry_mode) == "limit":
                try:
                    # Order Persistence Governor (Incident A): S1 pullback
                    # limits rest as GTC orders under a dynamic, wall-survival
                    # based TTL instead of a rigid slot-bound expiration. The
                    # deadline lives in UTC on our side of the IPC bridge, so
                    # broker server-time DST quirks can never expire or keep
                    # an order alive by accident.
                    persistent = self.persistent_limits and not self.paper_mode
                    anchors = candidate.get("entry_anchors") or []
                    primary_span = max((number(a.get("persistence_sec")) for a in anchors), default=0.0)
                    ttl = hazard_ttl(primary_span, ttl_min_sec=self.ttl_min_seconds, ttl_max_sec=self.ttl_max_seconds)
                    result = self.bridge.stage_limit_order(candidate["symbol"], candidate["direction"], candidate["volume"],
                                                           candidate["price_open"], candidate["sl"], candidate["tp"],
                                                           expiration_seconds=getattr(self, "limit_expiration_seconds", 3600),
                                                           persistent=persistent, comment=comment, magic=MAGIC,
                                                           max_spread_points=self.max_spread_points, passive_only=True)
                    intent["status"] = "STAGED_LIMIT" if result.get("success") else "REJECTED"
                    intent["order_ticket"] = result.get("ticket")
                    intent["expires_at"] = result.get("expires_at")
                    intent["anchors"] = anchors
                    intent["hurdle_r"] = candidate.get("hurdle_r")
                    if result.get("success") and persistent:
                        self.governor.register(key, asset=candidate["asset"], symbol=candidate["symbol"],
                                               direction=candidate["direction"], order_ticket=result.get("ticket"),
                                               limit_price=candidate["price_open"], sl=candidate["sl"], tp=candidate["tp"],
                                               volume=candidate["volume"], anchors=anchors, atr=candidate["atr"],
                                               ttl_sec=ttl, now=self.clock(), comment=comment,
                                               hurdle_r=candidate.get("hurdle_r"), risk_usd=candidate.get("risk_usd", 0.0),
                                               tick_size=candidate.get("tick_size", 0.01), magic=MAGIC)
                except Exception as exc:
                    intent["status"] = "REJECTED"; result = {"success": False, "error": str(exc)}
            else:
                try:
                    result = self.bridge.execute_market_order(candidate["symbol"], candidate["direction"], candidate["volume"], candidate["sl"], candidate["tp"],
                                                              magic=MAGIC, comment=comment, max_spread_points=self.max_spread_points,
                                                              deviation_points=0, max_tick_age_ms=2000)
                    intent["status"] = "ACKNOWLEDGED" if result.get("success") else "UNCERTAIN" if result.get("uncertain") else "REJECTED"
                except Exception as exc:
                    intent["status"] = "UNCERTAIN"; result = {"success": False, "uncertain": True, "error": str(exc)}
        intent["result"] = result
        self._append("executions.jsonl", {"time": self.clock(), "event": "dispatch_result", "intent_id": key, "result": result})
        self._save_state()
        return result

    def capture_quotes(self):
        # These sampled bid/ask observations label held-out second-position episodes.
        now = self.clock()
        for symbol in set(self.symbols.values()):
            try:
                q = self._quote(symbol)
                self._append("broker_quotes.jsonl", {"time": epoch(q["time_msc"]), "received_at": now, "symbol": symbol,
                                                    "bid": q["bid"], "ask": q["ask"], "feed_kind": "POLLED_QUOTES",
                                                    "tick_size": max(number(q.get("tick_size")), q["point"]),
                                                    "stop_distance": max(q.get("stops_level",0), q.get("freeze_level",0),1)*q["point"]})
            except ValueError: pass

    def run(self, max_cycles=0):
        lock_path = ROOT/"Data"/("omni-paper.lock" if self.paper_mode else "omni-live.lock")
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        # OS releases the lock after a crash; no stale PID heuristics or lock deletion.
        import msvcrt
        lock_stream = open(lock_path, "a+b")
        if lock_stream.tell() == 0: lock_stream.write(b"0"); lock_stream.flush()
        lock_stream.seek(0)
        try: msvcrt.locking(lock_stream.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError:
            lock_stream.close(); raise RuntimeError("Another OMNI writer owns this execution mode")
        cycle = 0
        try:
            while max_cycles <= 0 or cycle < max_cycles:
                cycle += 1
                try:
                    self.refresh_background()
                    # Bars BEFORE manage: the ratchet, ATR and drift guards
                    # must see the freshest completed history (production
                    # 10s-cadence ordering).
                    self.refresh_broker_history()
                    self.manage_active_positions()
                    self.capture_quotes()
                    self.evaluate_market()
                except Exception as exc:
                    self._append("runtime_errors.jsonl", {"time": self.clock(), "error": str(exc)})
                    print("OMNI cycle failed closed: "+str(exc), flush=True)
                time.sleep(1)
        finally:
            self._save_state()
            self.pool.shutdown(wait=False, cancel_futures=True); self.intel_pool.shutdown(wait=False, cancel_futures=True)
            self.inference_pool.shutdown(wait=False, cancel_futures=True)
            lock_stream.seek(0); msvcrt.locking(lock_stream.fileno(), msvcrt.LK_UNLCK, 1); lock_stream.close()
