"""HeadlessRuntime: the 24/7 cloud composition root (OX_ALPHA_60 Deliverable 3/4).

Wires, with everything injectable for offline tests:

  ZeroCostDataFactory + RealtimeRunner   - continuous data (Pillars 1-6)
  CrossSourceValidator                   - sealed data quality
  PioneerDecisionEngine                  - cross-validated conviction (veto-only)
  execution bridge (Terminal/Execution)   - native MT5 / cloud REST / paper
  AI15mMT5Trader                         - the unchanged decision engine
  CandleScheduler                        - :14/:29/:44/:59 boundary wakes
  HeadlessService                        - signed /healthz /readyz /evaluate_candle

Fail-closed semantics: if the bridge cannot prove connectivity, readiness
goes false and evaluate_candle returns a NO-TRADE payload - new entries stop,
while open positions stay protected by their broker-server-side SL/TP (the
3-phase ratchets already live server-side once armed).
"""
from __future__ import annotations

import asyncio
import os
import time
from typing import List, Optional

from Terminal.Risk_Sizing_Engine import number

SERVICE_VERSION = "omni.headless.v1"


def _env_float(name: str, default: float) -> float:
    try:
        return float(os.environ.get(name, "") or default)
    except ValueError:
        return default


class HeadlessRuntime:
    """Composition root. All collaborators are injectable; ``from_env`` wires
    production defaults from environment variables (never hardcoded secrets)."""

    def __init__(self, *, assets: List[str], bridge=None, factory=None, validator=None,
                 runner=None, trader=None, pioneer=None, scheduler=None,
                 risk_min_usd: float = 10.0, risk_max_usd: float = 20.0,
                 clock=time.time):
        self.assets = [str(a).upper() for a in assets]
        self.clock = clock
        self.risk_min_usd = float(risk_min_usd)
        self.risk_max_usd = float(risk_max_usd)
        self.bridge = bridge
        self.factory = factory
        self.validator = validator
        self.runner = runner
        self.trader = trader
        self.pioneer = pioneer
        self.scheduler = scheduler
        self.last_evaluation: Optional[dict] = None

    # ------------------------------------------------------------ factory
    @classmethod
    def from_env(cls, assets: Optional[List[str]] = None, *, clock=time.time,
                 bridge=None, trader=None):
        """Production wiring from environment (see deploy/.env.example)."""
        from Terminal.Data_Factory import (ZeroCostDataFactory, CrossSourceValidator,
                                           RealtimeRunner, LivePolicy)
        from Terminal.Execution import create_bridge
        from Terminal.Pioneer_Decision_Engine import PioneerDecisionEngine

        assets = assets or [a.strip().upper() for a in
                            os.environ.get("OMNI_ASSETS", "BTC,ETH,SOL,GOLD").split(",") if a.strip()]
        factory = ZeroCostDataFactory(assets, clock=clock,
                                      fng=None, farside=None)
        validator = CrossSourceValidator(factory, clock=clock)
        runner = RealtimeRunner(factory, validator, policy=LivePolicy(), clock=clock)
        bridge = bridge or create_bridge()
        pioneer = PioneerDecisionEngine(
            quality_provider=lambda asset: (runner.last_quality or {}).get("assets", {}).get(asset)
            or {"quality_score": -1.0},
            clock=clock)

        trader = trader or cls._build_trader(assets, bridge, factory, pioneer,
                                             int(os.environ.get("OMNI_PAPER", "0") or 0) == 1,
                                             _env_float("OMNI_RISK_MIN_USD", 10.0),
                                             _env_float("OMNI_RISK_MAX_USD", 20.0),
                                             clock)
        return cls(assets=assets, bridge=bridge, factory=factory, validator=validator,
                   runner=runner, trader=trader, pioneer=pioneer,
                   risk_min_usd=_env_float("OMNI_RISK_MIN_USD", 10.0),
                   risk_max_usd=_env_float("OMNI_RISK_MAX_USD", 20.0), clock=clock)

    @staticmethod
    def _build_trader(assets, bridge, factory, pioneer, paper, risk_min, risk_max, clock):
        from Terminal.Market_Intelligence import MarketIntelligenceEngine
        from Terminal.Omni_Trader import AI15mMT5Trader
        from Terminal.Asset_Universe import UNIVERSE

        allowed = [a for a in UNIVERSE if a in assets]
        trader = AI15mMT5Trader(
            coin=allowed[0] if allowed else "SOL", bridge=bridge,
            intel=MarketIntelligenceEngine(clock=clock),
            covariance=None,                      # loaded from parquet by the ctor
            risk_usd=risk_min, min_risk_usd=risk_min, max_risk_usd=risk_max,
            paper_mode=paper, entry_mode="limit",
            allow_list=allowed or list(UNIVERSE),
            fetcher=factory.payload_fetcher(), clock=clock)
        trader.attach_pioneer(pioneer)
        return trader

    # ---------------------------------------------------------- read gates
    def readiness(self):
        """(ready, reasons). Fail-closed: bridge health + at least one live book."""
        reasons = []
        if self.bridge is None:
            reasons.append("no_bridge")
        else:
            health = self.bridge.health() if hasattr(self.bridge, "health") else {"healthy": True}
            if not health.get("healthy"):
                reasons.append(f"bridge_unhealthy:{health.get('backend', '')}:{health.get('detail', '')[:80]}")
        fresh_book = False
        if self.factory is not None:
            now = self.clock()
            for asset in self.assets:
                book = self.factory.bus.book(asset) or {}
                ts = number(book.get("ts"), 0.0)
                if ts > 0 and 0.0 <= now - ts <= 30.0:
                    fresh_book = True
                    break
            if not fresh_book:
                reasons.append("no_fresh_book")
        return (not reasons), reasons

    # -------------------------------------------------------- market state
    def market_state(self, assets=None):
        """Signed-read endpoint payload: live positions, pending orders,
        quotes and per-asset orderflow snapshots for the brain's
        deliberation. Read-only; no secrets; no account credentials."""
        now = self.clock()
        positions = []
        if self.bridge is not None:
            try:
                positions = self.bridge.get_open_positions() or []
            except Exception as exc:                      # noqa: BLE001
                positions = [{"error": repr(exc)}]
        pending = []
        if self.bridge is not None:
            try:
                pending = self.bridge.get_pending_orders() or []
            except Exception:                             # noqa: BLE001
                pending = []
        quotes = {}
        symbols = {p.get("symbol") for p in positions if p.get("symbol")}
        symbols |= {o.get("symbol") for o in pending if o.get("symbol")}
        trader_symbols = getattr(getattr(self, "trader", None), "symbols", {}) or {}
        for asset in (assets or self.assets):
            symbol = trader_symbols.get(asset)
            if not symbol and self.bridge is not None and hasattr(self.bridge, "resolve_symbol"):
                try:
                    symbol = self.bridge.resolve_symbol(asset)
                except Exception:
                    symbol = None
            if symbol:
                symbols.add(symbol)
        if self.bridge is not None:
            for symbol in sorted(s for s in symbols if s):
                try:
                    quote = self.bridge.get_symbol_price(symbol)
                    if quote:
                        # Full contract spec so the brain can size locally
                        # (the muscle re-enforces every cap on arrival).
                        quotes[symbol] = {k: quote.get(k) for k in
                                          ("bid", "ask", "tick_size", "contract_size",
                                           "min_lot", "step_lot", "digits")}
                except Exception:                         # noqa: BLE001
                    continue
        account = {}
        if self.bridge is not None:
            try:
                summary = self.bridge.get_account_summary() or {}
                account = {"balance_usd": summary.get("balance"),
                           "equity_usd": summary.get("equity_usd"),
                           "margin_free_usd": summary.get("margin_free_usd")}
            except Exception:                             # noqa: BLE001
                account = {}
        orderflow = {}
        if self.factory is not None:
            for asset in (assets or self.assets):
                try:
                    book = self.factory.bus.book(asset) or {}
                    ts = number(book.get("ts"), 0.0)
                    if ts > 0 and 0.0 <= now - ts <= 120.0:
                        snap = self.factory.bus.snapshot(asset, now)
                        snap["atr"] = self.factory._atr(asset)
                        orderflow[asset] = snap
                except Exception:                         # noqa: BLE001
                    continue
        macro = {}
        try:
            if self.trader is not None and hasattr(self.trader.intel, "check_macro_blackout"):
                blackout, event, _minutes = self.trader.intel.check_macro_blackout()
                macro = {"blackout_active": bool(blackout), "blackout_event": event}
        except Exception:                                 # noqa: BLE001
            macro = {"blackout_active": True, "blackout_event": "MACRO_UNAVAILABLE"}
        return {"service": SERVICE_VERSION, "as_of": now, "positions": positions,
                "pending_orders": pending, "quotes": quotes, "symbols": trader_symbols,
                "orderflow": orderflow, "macro": macro, "account": account}

    # --------------------------------------------------------------- status
    def status(self):
        """Muscle health for the brain: bridge, data pillars, sealed quality,
        last evaluation. Deliberately carries NO account balances - health
        only; the brain's Macro analyst gets equity from its own signed
        evaluate_candle payloads."""
        now = self.clock()
        ready, reasons = self.readiness()
        bridge_health = {}
        if self.bridge is not None and hasattr(self.bridge, "health"):
            try:
                bridge_health = self.bridge.health() or {}
            except Exception as exc:                      # noqa: BLE001
                bridge_health = {"healthy": False, "detail": repr(exc)}
        runner_status = {}
        if self.runner is not None and hasattr(self.runner, "status"):
            try:
                runner_status = self.runner.status() or {}
            except Exception:                             # noqa: BLE001
                runner_status = {}
        quality = None
        if self.runner is not None and getattr(self.runner, "last_quality", None):
            quality = {"score": self.runner.last_quality.get("quality_score"),
                       "digest": self.runner.last_quality.get("digest")}
        last = self.last_evaluation or {}
        return {"service": SERVICE_VERSION, "as_of": now, "ready": ready,
                "reasons": list(reasons),
                "bridge": {"backend": getattr(self.bridge, "name", None),
                           "healthy": bridge_health.get("healthy"),
                           "detail": bridge_health.get("detail", "")},
                "pillars": runner_status.get("pillars"),
                "stall_streaks": runner_status.get("stall_streaks"),
                "data_quality": quality,
                "last_evaluation": {"decision": last.get("decision"),
                                    "as_of": last.get("as_of"),
                                    "traded": last.get("traded")} if last else None}

    # ------------------------------------------------------------- evaluate
    def evaluate_candle(self, force: bool = False) -> dict:
        """One candle-close evaluation. Returns the signed microservice payload
        body (signing happens in HeadlessService). NEVER raises for market
        reasons - degraded states return ok=False no-trade payloads."""
        now = self.clock()
        base = {"service": SERVICE_VERSION, "as_of": now,
                "slot": int(now // 900), "ok": False, "traded": False}
        ready, reasons = self.readiness()
        if not ready:
            base.update(reason="|".join(reasons), decision="NO_TRADE_FAIL_CLOSED")
            self.last_evaluation = base
            return base
        try:
            macro = None
            if self.trader is not None and hasattr(self.trader.intel, "get_market_intelligence_report"):
                macro = self.trader.intel.get_market_intelligence_report()
            payloads = {}
            if self.factory is not None:
                for asset in self.assets:
                    try:
                        payloads[asset] = self.factory.payload(asset, now)
                    except ValueError:
                        pass                    # no book yet for this asset: skip
            if not payloads:
                base.update(reason="no_payloads", decision="NO_TRADE_FAIL_CLOSED")
                self.last_evaluation = base
                return base
            report = self.trader.evaluate_market(payloads, macro, force=force) \
                if self.trader is not None else {"decision": "NO_TRADER", "vetoes": {}}
            pioneer_vector = {}
            if self.pioneer is not None:
                for asset, advisory in (self.pioneer.last or {}).items():
                    pioneer_vector[asset] = {k: advisory.get(k) for k in
                                             ("conviction", "advice", "quality_score",
                                              "min_favorable_move_bps", "digest")}
            staged = []
            for intent in (getattr(self.trader, "state", {}).get("intents") or {}).values():
                if intent.get("status") == "STAGED_LIMIT":
                    candidate = intent.get("candidate") or {}
                    staged.append({"asset": candidate.get("asset"),
                                   "direction": candidate.get("direction"),
                                   "order_ticket": intent.get("order_ticket"),
                                   "limit_price": candidate.get("price_open"),
                                   "sl": candidate.get("sl"), "tp": candidate.get("tp"),
                                   "volume": candidate.get("volume"),
                                   "risk_usd": candidate.get("risk_usd"),
                                   "expires_at": intent.get("expires_at")})
            quality = None
            if self.validator is not None and self.runner is not None \
                    and self.runner.last_quality is not None:
                quality = {"score": self.runner.last_quality.get("quality_score"),
                           "digest": self.runner.last_quality.get("digest")}
            result = {**base, "ok": True,
                      "decision": report.get("decision", "HOLD"),
                      "reason": report.get("reason", ""),
                      "vetoes": report.get("vetoes", {}),
                      "pioneer_conviction_vector": pioneer_vector,
                      "staged_order_tickets": staged,
                      "data_quality": quality,
                      "traded": report.get("decision") in ("PAPER_FILLED", "ORDER_FILLED",
                                                           "LIMIT_STAGED")}
            self.last_evaluation = result
            return result
        except Exception as exc:                      # noqa: BLE001 - fail-closed wrapper
            base.update(reason=f"evaluate_error:{exc!r}", decision="NO_TRADE_FAIL_CLOSED")
            self.last_evaluation = base
            return base

    # ------------------------------------------------------------ lifecycle
    async def run_forever(self, *, stop_event: Optional[asyncio.Event] = None,
                          service: Optional[object] = None):
        """Start the data runner and the candle scheduler; optionally the
        signed HTTP service. Runs until ``stop_event`` fires."""
        from Terminal.Headless.scheduler import CandleScheduler

        stop_event = stop_event if stop_event is not None else asyncio.Event()
        tasks = []
        if self.runner is not None:
            tasks.append(asyncio.create_task(self._runner_task(stop_event)))
        scheduler = self.scheduler or CandleScheduler(clock=self.clock)
        tasks.append(asyncio.create_task(
            scheduler.run(lambda deadline: self.evaluate_candle(),
                          stop_event=stop_event, on_wake_async=self._evaluate_async)))
        if service is not None:
            tasks.append(asyncio.create_task(service.run()))
        await stop_event.wait()
        for task in tasks:
            task.cancel()

    async def _runner_task(self, stop_event):
        try:
            await self.runner.run(assets=self.assets, stop_event=stop_event)
        except asyncio.CancelledError:
            pass

    async def _evaluate_async(self, deadline):
        await asyncio.to_thread(self.evaluate_candle)
