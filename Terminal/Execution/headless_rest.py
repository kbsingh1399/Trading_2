"""Backend B: headless cloud REST/WebSocket execution gateway.

Runs on Linux containers with no desktop terminal. The route map follows the
MetaApi cloud gateway REST shape (works with any MetaApi-compatible provider,
and adapts to direct broker REST/FIX gateways by overriding ``_routes``).

Security: the account token is read from ``METAAPI_TOKEN`` (or injected via
constructor/config) - NEVER hardcoded. Every request carries the token in the
``auth`` header; the transport is injectable so tests (and alternative
gateways) never touch a real network.

Fail-closed: any non-2xx response raises ``BridgeError`` - the trader's
existing uncertainty paths take over; nothing is assumed about order state.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Dict, List, Optional

from Terminal.Execution.base import BaseExecutionBridge, BridgeError

DEFAULT_DOMAIN = "mt-client-api-v1.metaapi.cloud"


def _default_transport(method: str, url: str, headers: Dict[str, str],
                       payload: Optional[Dict]) -> tuple:
    """Blocking urllib transport. Returns (status_code, parsed_json_or_None)."""
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(url, data=data, method=method)
    for key, value in (headers or {}).items():
        request.add_header(key, value)
    if data is not None:
        request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            body = response.read()
            return response.status, (json.loads(body) if body else None)
    except urllib.error.HTTPError as exc:
        body = exc.read()
        try:
            parsed = json.loads(body) if body else None
        except ValueError:
            parsed = None
        return exc.code, parsed


class HeadlessRESTBridge(BaseExecutionBridge):
    """Cloud REST execution bridge (MetaApi-shaped, injectable transport)."""

    name = "headless_rest"

    def __init__(self, token: Optional[str] = None, account_id: Optional[str] = None,
                 domain: Optional[str] = None, *, transport: Callable = None,
                 clock=time.time, symbol_specs: Optional[Dict[str, Dict]] = None):
        self.token = token or os.environ.get("METAAPI_TOKEN", "")
        self.account_id = str(account_id or os.environ.get("METAAPI_ACCOUNT_ID", ""))
        self.domain = domain or os.environ.get("METAAPI_DOMAIN", DEFAULT_DOMAIN)
        self.transport = transport or _default_transport
        self.clock = clock
        self._specs = dict(symbol_specs or {})
        self._intent_ledger: Dict[str, Dict[str, Any]] = {}

    # ----------------------------------------------------------- plumbing
    def _base(self) -> str:
        return f"https://{self.domain}/users/current/accounts/{self.account_id}"

    def _call(self, method: str, path: str, payload: Optional[Dict] = None):
        """``path`` is appended to the account base (e.g. /account-summary,
        /symbolPrice/ETHUSD.pi) so symbol-bearing routes stay first-class."""
        if not self.token or not self.account_id:
            raise BridgeError("headless_rest_unconfigured:METAAPI_TOKEN/METAAPI_ACCOUNT_ID")
        url = self._base() + path
        status, body = self.transport(method, url, {"auth": self.token}, payload)
        if status >= 300:
            raise BridgeError(f"gateway_error:{status}:{path}:{str(body)[:200]}")
        return body

    def _spec(self, symbol: str) -> Dict[str, Any]:
        """Contract spec, injected or conservative default (USD-linear CFD)."""
        if symbol not in self._specs:
            self._specs[symbol] = {"point": 0.01, "digits": 2, "contract_size": 100.0,
                                   "min_lot": 0.01, "step_lot": 0.01, "max_lot": 10.0,
                                   "stops_level": 0, "freeze_level": 0}
        return self._specs[symbol]

    # ------------------------------------------------------- mandatory surface
    def get_account_summary(self) -> Dict[str, Any]:
        raw = self._call("GET", "/account-summary") or {}
        return {"connected": True, "login": raw.get("login") or self.account_id,
                "currency": raw.get("currency", "USD"),
                "balance": float(raw.get("balance") or 0.0),
                "equity_usd": float(raw.get("equity") or raw.get("balance") or 0.0),
                "margin_usd": float(raw.get("margin") or 0.0),
                "margin_free_usd": float(raw.get("freeMargin") or raw.get("marginFree") or 0.0)}

    def get_open_positions(self, symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        rows = self._call("GET", "/positions") or []
        out = []
        for p in rows:
            if symbol and p.get("symbol") != symbol:
                continue
            out.append({"ticket": int(p.get("id") or p.get("positionId") or 0),
                        "symbol": p.get("symbol"), "direction": "LONG" if float(p.get("type") == "POSITION_TYPE_BUY" or p.get("type") == "buy") else "SHORT",
                        "volume": float(p.get("volume") or 0.0),
                        "price_open": float(p.get("openPrice") or 0.0),
                        "sl": float(p.get("stopLoss") or 0.0) or None,
                        "tp": float(p.get("takeProfit") or 0.0) or None,
                        "profit_usd": float(p.get("profit") or 0.0),
                        "time": float(p.get("time") or 0.0) / 1000.0 if float(p.get("time") or 0) > 1e11 else float(p.get("time") or 0.0),
                        "magic": int(p.get("magic") or 0), "comment": p.get("comment", "")})
        return out

    def get_pending_orders(self) -> List[Dict[str, Any]]:
        rows = self._call("GET", "/pendingOrders") or []
        out = []
        for o in rows:
            out.append({"ticket": int(o.get("id") or 0), "symbol": o.get("symbol"),
                        "direction": "LONG" if str(o.get("type", "")).upper().endswith("BUY") else "SHORT",
                        "volume": float(o.get("volume") or 0.0),
                        "price_open": float(o.get("openPrice") or 0.0),
                        "sl": float(o.get("stopLoss") or 0.0) or None,
                        "tp": float(o.get("takeProfit") or 0.0) or None,
                        "magic": int(o.get("magic") or 0), "comment": o.get("comment", "")})
        return out

    def get_symbol_price(self, symbol: str) -> Optional[Dict[str, Any]]:
        raw = self._call("GET", f"/symbolPrice/{symbol}") or {}
        bid, ask = float(raw.get("bid") or 0.0), float(raw.get("ask") or 0.0)
        if not 0 < bid < ask:
            return None
        spec = self._spec(symbol)
        ts = float(raw.get("time") or 0.0)
        return {"bid": bid, "ask": ask, "point": spec["point"], "tick_size": spec["point"],
                "time_msc": ts if ts > 1e12 else ts * 1000.0,
                "digits": spec["digits"], "contract_size": spec["contract_size"],
                "min_lot": spec["min_lot"], "step_lot": spec["step_lot"],
                "max_lot": spec["max_lot"], "stops_level": spec["stops_level"],
                "freeze_level": spec["freeze_level"], "currency_profit": "USD"}

    def stage_limit_order(self, symbol: str, direction: str, volume: float,
                          limit_price: float, sl: float, tp: float, **kwargs) -> Dict[str, Any]:
        action = "ORDER_TYPE_BUY_LIMIT" if direction == "LONG" else "ORDER_TYPE_SELL_LIMIT"
        payload = {"action": action, "symbol": symbol, "volume": float(volume),
                   "openPrice": float(limit_price), "stopLoss": float(sl),
                   "takeProfit": float(tp), "comment": kwargs.get("comment", ""),
                   "magic": int(kwargs.get("magic", 100895))}
        raw = self._call("POST", "/trade", payload) or {}
        ticket = raw.get("orderId") or raw.get("numericId") or raw.get("id")
        if ticket is None:
            raise BridgeError(f"stage_limit_no_ticket:{str(raw)[:200]}")
        result = {"success": True, "ticket": int(ticket)}
        if kwargs.get("expiration_seconds"):
            result["expires_at"] = self.clock() + float(kwargs["expiration_seconds"])
        self._intent_ledger[str(kwargs.get("comment", ""))] = {"ticket": int(ticket),
                                                               "symbol": symbol}
        return result

    def modify_position_sltp(self, ticket: int, new_sl: float,
                             new_tp: Optional[float] = None) -> Dict[str, Any]:
        payload = {"action": "MODIFY_POSITION", "positionId": int(ticket),
                   "stopLoss": float(new_sl),
                   "takeProfit": float(new_tp) if new_tp else None}
        self._call("POST", "/trade", payload)
        return {"success": True, "ticket": int(ticket)}

    def cancel_pending_order(self, order_ticket: int) -> Dict[str, Any]:
        self._call("POST", "/trade", {"action": "CANCEL_ORDER", "orderId": int(order_ticket)})
        return {"success": True, "ticket": int(order_ticket)}

    # ---------------------------------------------------- extended surface
    def estimate_order(self, symbol: str, direction: str, entry: float, sl: float) -> Dict[str, Any]:
        spec = self._spec(symbol)
        return {"stop_loss_per_lot": abs(float(entry) - float(sl)) * spec["contract_size"],
                "margin_per_lot": 1000.0}

    def execute_market_order(self, symbol: str, direction: str, volume: float,
                             sl: float, tp: float, **kwargs) -> Dict[str, Any]:
        action = "ORDER_TYPE_BUY" if direction == "LONG" else "ORDER_TYPE_SELL"
        payload = {"action": action, "symbol": symbol, "volume": float(volume),
                   "stopLoss": float(sl), "takeProfit": float(tp),
                   "comment": kwargs.get("comment", ""),
                   "magic": int(kwargs.get("magic", 100895))}
        raw = self._call("POST", "/trade", payload) or {}
        ticket = raw.get("orderId") or raw.get("numericId") or raw.get("id")
        if ticket is None:
            raise BridgeError(f"market_order_no_ticket:{str(raw)[:200]}")
        return {"success": True, "ticket": int(ticket),
                "price_open": float(raw.get("price") or 0.0) or None}

    def close_position(self, ticket: int) -> Dict[str, Any]:
        positions = {p["ticket"]: p for p in self.get_open_positions()}
        p = positions.get(int(ticket))
        if not p:
            return {"success": False, "error": "position_not_found"}
        action = "CLOSE_POSITION"
        payload = {"action": action, "positionId": int(ticket), "volume": p["volume"]}
        self._call("POST", "/trade", payload)
        return {"success": True}

    def intent_filled(self, comment: str, prepared_at: float, magic: int = 100895) -> bool:
        """Client-side ledger + live state: filled iff the staged ticket left
        the pending book and lives in the position book."""
        ledger = self._intent_ledger.get(str(comment))
        if not ledger:
            return False
        ticket = ledger["ticket"]
        if any(o["ticket"] == ticket for o in self.get_pending_orders()):
            return False
        return any(p["ticket"] == ticket for p in self.get_open_positions())
