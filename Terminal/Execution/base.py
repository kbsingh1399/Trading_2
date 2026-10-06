"""Polymorphic broker execution backends (OX_ALPHA_60 Deliverable 1).

The trading logic in ``Omni_Trader`` never imports ``MetaTrader5`` directly -
it talks to a duck-typed bridge. This package makes that contract explicit
and gives it three production backends:

  * ``NativeMT5Bridge``     - the existing Windows desktop IPC bridge
                               (``Terminal/MT5_Execution_Bridge.py``), unchanged
  * ``HeadlessRESTBridge``  - a Linux/cloud REST gateway bridge (MetaApi-shaped
                               routes, injectable transport, env-based secrets)
  * ``PaperSimulatedBridge`` - a zero-dependency deterministic matching engine
                               that fills resting limits/SL/TP against raw
                               WebSocket orderbook ticks

Selection is FAIL-CLOSED (``create_bridge``): an explicitly requested backend
that cannot prove connectivity raises ``NoExecutionBackend`` - the engine never
silently falls back from live money to paper. Automatic mode probes native MT5,
then the cloud gateway, and only ever selects paper when ``OMNI_ALLOW_PAPER=1``.
"""
from __future__ import annotations

import abc
import os
from typing import Any, Dict, List, Optional

from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge


class BridgeError(RuntimeError):
    """A backend could not honour the execution contract."""


class NoExecutionBackend(BridgeError):
    """Fail-closed: no backend proved connectivity (or the requested one is down)."""


class BaseExecutionBridge(abc.ABC):
    """The mandatory execution contract every backend must honour.

    The seven core methods are abstract (the prompt's mandatory surface); the
    extended surface the trader actually calls (``estimate_order``,
    ``execute_market_order``, ``close_position``, ``position_deals``,
    ``reconcile_intent_history``, ``intent_filled``, ``get_recent_bars``,
    ``resolve_symbol``) carries conservative fail-closed defaults so a minimal
    gateway adapter stays implementable, and every method returns the exact
    dict shapes ``Omni_Trader``/``OrderPersistenceGovernor`` already consume.
    """

    name = "base"

    # ------------------------------------------------------- mandatory surface
    @abc.abstractmethod
    def get_account_summary(self) -> Dict[str, Any]:
        """{"connected", "login", "currency", "balance", "equity_usd",
        "margin_free_usd", "margin_usd"} - equity and free margin in USD."""

    @abc.abstractmethod
    def get_open_positions(self, symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """Open positions with ticket/symbol/direction/volume/price_open/sl/tp/
        profit_usd/time/magic/comment."""

    @abc.abstractmethod
    def get_pending_orders(self) -> List[Dict[str, Any]]:
        """Resting orders with ticket/symbol/direction/volume/price_open/sl/tp."""

    @abc.abstractmethod
    def get_symbol_price(self, symbol: str) -> Optional[Dict[str, Any]]:
        """{"bid", "ask", "point", "tick_size", "time_msc", "digits",
        "contract_size", "min_lot", "step_lot", "max_lot", "stops_level",
        "freeze_level", "currency_profit"}."""

    @abc.abstractmethod
    def stage_limit_order(self, symbol: str, direction: str, volume: float,
                          limit_price: float, sl: float, tp: float, **kwargs) -> Dict[str, Any]:
        """Rest a limit order; returns {"success", "ticket", "expires_at", ...}."""

    @abc.abstractmethod
    def modify_position_sltp(self, ticket: int, new_sl: float,
                             new_tp: Optional[float] = None) -> Dict[str, Any]:
        """Server-side SL/TP modification (the 3-phase ratchet actuator)."""

    @abc.abstractmethod
    def cancel_pending_order(self, order_ticket: int) -> Dict[str, Any]:
        """Cancel a resting order; returns {"success", "ticket"}."""

    # Prompt parity alias: the specification names this ``cancel_order``.
    def cancel_order(self, order_ticket: int) -> Dict[str, Any]:
        return self.cancel_pending_order(order_ticket)

    # ---------------------------------------------------- extended surface
    def resolve_symbol(self, asset: str) -> Optional[str]:
        """Canonical asset -> broker symbol mapping."""
        return None

    def get_recent_bars(self, symbol: str, count: int = 96, timeframe: Any = None) -> List[Dict[str, Any]]:
        """Completed OHLCV bars. Default: none (headless runtimes source bars
        from the Data Factory, which is the authoritative candle feed)."""
        return []

    def estimate_order(self, symbol: str, direction: str, entry: float, sl: float) -> Dict[str, Any]:
        raise BridgeError(f"estimate_order_unsupported:{self.name}")

    def execute_market_order(self, symbol: str, direction: str, volume: float,
                             sl: float, tp: float, **kwargs) -> Dict[str, Any]:
        raise BridgeError(f"market_order_unsupported:{self.name}")

    def close_position(self, ticket: int) -> Dict[str, Any]:
        raise BridgeError(f"close_position_unsupported:{self.name}")

    def position_deals(self, ticket: int) -> List[Dict[str, Any]]:
        return []

    def reconcile_intent_history(self, comment: str, prepared_at: float, magic: int = 100895) -> Dict[str, Any]:
        return {"state": None}

    def intent_filled(self, comment: str, prepared_at: float, magic: int = 100895) -> bool:
        return False

    # ------------------------------------------------------------- health
    def health(self) -> Dict[str, Any]:
        """Connectivity probe used by auto-discovery and the readiness endpoint.

        A backend is healthy only when it can currently read account state -
        the same fail-closed discipline as the data factory."""
        try:
            summary = self.get_account_summary()
            return {"healthy": bool(summary and summary.get("connected")
                                    and number_or(summary.get("equity_usd")) > 0),
                    "backend": self.name, "detail": ""}
        except Exception as exc:                      # noqa: BLE001 - probe isolation
            return {"healthy": False, "backend": self.name, "detail": repr(exc)}


def number_or(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


# ---------------------------------------------------------------- registry
_REGISTRY: Dict[str, Any] = {}


def register_backend(name: str, factory):
    """Register a backend factory: callable(config: dict) -> bridge instance."""
    _REGISTRY[str(name)] = factory


def available_backends():
    return sorted(_REGISTRY)


def _native_available() -> bool:
    try:
        import MetaTrader5                              # noqa: F401
        return True
    except ImportError:
        return False


def _probe(bridge) -> bool:
    return bool(bridge.health().get("healthy"))


def create_bridge(config: Optional[Dict[str, Any]] = None, prefer: Optional[str] = None):
    """Select and construct an execution backend. FAIL-CLOSED.

    Selection order:
      1. ``prefer`` argument, else ``EXECUTION_BACKEND`` env: the explicitly
         requested backend ONLY. If it cannot prove connectivity, raise -
         never silently fall back from the operator's intent.
      2. Auto-discovery: native MT5 (package importable + terminal answers),
         then the cloud REST gateway (token + account + probe),
         then paper - only when ``OMNI_ALLOW_PAPER=1``.
      3. Nothing proved connectivity -> ``NoExecutionBackend`` (no trading).
    """
    cfg = dict(config or {})
    requested = prefer or os.environ.get("EXECUTION_BACKEND", "").strip() or None

    def _build(name):
        if name not in _REGISTRY:
            raise NoExecutionBackend(f"unknown_backend:{name}")
        return _REGISTRY[name](cfg)

    if requested:
        bridge = _build(requested)
        if not _probe(bridge):
            raise NoExecutionBackend(
                f"requested_backend_unhealthy:{requested}:"
                f"{bridge.health().get('detail', '')}")
        return bridge

    order = ["native_mt5", "headless_rest"]
    if str(os.environ.get("OMNI_ALLOW_PAPER", "")).strip() in ("1", "true", "TRUE"):
        order.append("paper")
    failures = []
    for name in order:
        if name == "native_mt5" and not _native_available():
            failures.append("native_mt5:package_unavailable")
            continue
        if name == "headless_rest" and not (os.environ.get("METAAPI_TOKEN")
                                            and os.environ.get("METAAPI_ACCOUNT_ID")):
            failures.append("headless_rest:credentials_unconfigured")
            continue
        try:
            bridge = _build(name)
        except BridgeError as exc:
            failures.append(f"{name}:{exc}")
            continue
        if _probe(bridge):
            return bridge
        failures.append(f"{name}:{bridge.health().get('detail', 'unhealthy')}")
    raise NoExecutionBackend("no_healthy_backend:" + ";".join(failures))


def _register_defaults():
    from Terminal.Execution.native_mt5 import NativeMT5Bridge
    from Terminal.Execution.headless_rest import HeadlessRESTBridge
    from Terminal.Execution.paper import PaperSimulatedBridge

    register_backend("native_mt5",
                     lambda cfg: NativeMT5Bridge(account_id=cfg.get("mt5_account_id")))
    register_backend("headless_rest", lambda cfg: HeadlessRESTBridge(
        token=cfg.get("metaapi_token"), account_id=cfg.get("metaapi_account_id"),
        domain=cfg.get("metaapi_domain")))
    register_backend("paper", lambda cfg: PaperSimulatedBridge(
        clock=cfg.get("clock"), initial_equity=cfg.get("initial_equity", 5000.0)))


_register_defaults()
