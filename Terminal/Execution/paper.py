"""Backend C: zero-dependency institutional paper matching simulator.

Fills resting limit orders, stop losses and take profits against raw price
ticks - the same ticks the Data Factory bus already carries - with zero
network, zero dependencies and full determinism (injectable clock, explicit
``set_price``/``on_tick``). This is the backend for headless simulation,
CI, and the deterministic offline test suite.

Matching semantics (conservative by design):
  * BUY limit fills when the ask trades at or below the limit (fill at the
    limit price or better);
  * SELL limit fills when the bid reaches the limit or better;
  * market orders fill at the quote plus configurable slippage bps;
  * LONG stops/triggers fire on the BID, SHORT on the ASK (no phantom fills
    from spread artifacts);
  * SL/TP fill exactly at their level (the server-side semantics the
    ratchets assume).
"""
from __future__ import annotations

import copy
import time
from typing import Any, Callable, Dict, List, Optional

from Terminal.Execution.base import BaseExecutionBridge

GOLD_MAP = {"GOLD": "XAUUSD", "SILVER": "XAGUSD"}
DIRECTION_MAP = {"LONG": "LONG", "BUY": "LONG", "SHORT": "SHORT", "SELL": "SHORT"}


def default_symbol_of(asset: str) -> str:
    asset = str(asset).upper()
    return GOLD_MAP.get(asset, asset + "USD")


def asset_of_symbol(symbol: str) -> str:
    s = str(symbol).upper().split(".")[0]
    for asset, mapped in GOLD_MAP.items():
        if s == mapped:
            return asset
    return s[:-3] if s.endswith("USD") else s


class PaperSimulatedBridge(BaseExecutionBridge):
    """Deterministic paper matching against an injectable tick feed."""

    name = "paper"

    def __init__(self, clock: Callable = time.time, *, initial_equity: float = 5000.0,
                 spread: float = 0.02, slippage_bps: float = 2.0,
                 point: float = 0.01, digits: int = 2, contract_size: float = 100.0,
                 min_lot: float = 0.01, step_lot: float = 0.01, max_lot: float = 10.0,
                 margin_per_lot: float = 1000.0, login: int = 5064568):
        self.clock = clock or time.time
        self.cash = float(initial_equity)
        self.spread = float(spread)
        self.slippage_bps = float(slippage_bps)
        self.point = float(point)
        self.digits = int(digits)
        self.contract_size = float(contract_size)
        self.min_lot = float(min_lot)
        self.step_lot = float(step_lot)
        self.max_lot = float(max_lot)
        self.margin_per_lot = float(margin_per_lot)
        self.login = int(login)
        self.positions: List[Dict[str, Any]] = []
        self.pending: List[Dict[str, Any]] = []
        self.deals: List[Dict[str, Any]] = []
        self._prices: Dict[str, Dict[str, float]] = {}
        self._next_ticket = 1000

    # ------------------------------------------------------------- feed
    def set_price(self, symbol: str, bid: float, ask: float, ts: Optional[float] = None):
        """Prime/override the quote for one symbol."""
        self._prices[str(symbol)] = {"bid": float(bid), "ask": float(ask),
                                     "ts": float(ts if ts is not None else self.clock())}
        self._pump()

    def on_tick(self, symbol: str, price: float, ts: Optional[float] = None):
        """One raw tick: quote becomes price +/- half spread, then pump."""
        half = self.spread / 2.0
        self.set_price(symbol, price - half, price + half, ts)

    @classmethod
    def from_bus(cls, bus, assets, **kwargs):
        """A bridge whose quotes are the Data Factory bus mids (headless sim)."""
        bridge = cls(**kwargs)
        quote = bridge.quote

        def bus_quote(symbol):
            mid = bus.mid(asset_of_symbol(symbol))
            if mid:
                half = bridge.spread / 2.0
                return mid - half, mid + half
            return None
        bridge.quote = lambda symbol: bus_quote(symbol) or quote(symbol)
        return bridge

    def quote(self, symbol: str):
        row = self._prices.get(str(symbol))
        if not row:
            return None
        return row["bid"], row["ask"]

    # ------------------------------------------------------------- engine
    def _pump(self):
        """Event-driven matching: resting limits, then SL/TP on open positions."""
        for order in list(self.pending):
            quote = self.quote(order["symbol"])
            if not quote:
                continue
            bid, ask = quote
            if order["direction"] == "LONG" and ask <= order["price_open"]:
                self._fill_pending(order, min(order["price_open"], ask))
            elif order["direction"] == "SHORT" and bid >= order["price_open"]:
                self._fill_pending(order, max(order["price_open"], bid))
        for position in list(self.positions):
            quote = self.quote(position["symbol"])
            if not quote:
                continue
            bid, ask = quote
            if position["direction"] == "LONG":
                if position.get("sl") and bid <= position["sl"]:
                    self._close_position(position, position["sl"], "stop_loss")
                elif position.get("tp") and bid >= position["tp"]:
                    self._close_position(position, position["tp"], "take_profit")
            else:
                if position.get("sl") and ask >= position["sl"]:
                    self._close_position(position, position["sl"], "stop_loss")
                elif position.get("tp") and ask <= position["tp"]:
                    self._close_position(position, position["tp"], "take_profit")

    def _ticket(self):
        self._next_ticket += 1
        return self._next_ticket

    def _fill_pending(self, order, fill_price):
        self.pending.remove(order)
        position = {**order, "price_open": float(fill_price), "ticket": order["ticket"],
                    "profit_usd": 0.0, "time": self.clock()}
        self.positions.append(position)
        self.deals.append({"ticket": order["ticket"], "event": "fill",
                           "price": float(fill_price), "volume": order["volume"],
                           "time": self.clock(), "comment": order.get("comment", "")})

    def _close_position(self, position, exit_price, reason):
        self.positions.remove(position)
        sign = 1.0 if position["direction"] == "LONG" else -1.0
        pnl = sign * (exit_price - position["price_open"]) * position["volume"] * self.contract_size
        self.cash += pnl
        self.deals.append({"ticket": position["ticket"], "event": reason,
                           "price": float(exit_price), "volume": position["volume"],
                           "pnl_usd": pnl, "time": self.clock(),
                           "comment": position.get("comment", "")})

    def _floating(self):
        total = 0.0
        for position in self.positions:
            quote = self.quote(position["symbol"])
            if not quote:
                continue
            bid, ask = quote
            exit_price = bid if position["direction"] == "LONG" else ask
            sign = 1.0 if position["direction"] == "LONG" else -1.0
            total += sign * (exit_price - position["price_open"]) * position["volume"] * self.contract_size
        return total

    # ------------------------------------------------------- mandatory surface
    def get_account_summary(self) -> Dict[str, Any]:
        self._pump()
        floating = self._floating()
        equity = self.cash + floating
        margin = sum(p["volume"] * self.margin_per_lot for p in self.positions)
        return {"connected": True, "login": self.login, "currency": "USD",
                "balance": round(self.cash, 2), "equity_usd": round(equity, 2),
                "margin_usd": round(margin, 2),
                "margin_free_usd": round(max(0.0, equity - margin), 2)}

    def get_open_positions(self, symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        self._pump()
        rows = self.positions if symbol is None else [p for p in self.positions
                                                      if p["symbol"] == symbol]
        return copy.deepcopy(rows)

    def get_pending_orders(self) -> List[Dict[str, Any]]:
        self._pump()
        return copy.deepcopy(self.pending)

    def get_symbol_price(self, symbol: str) -> Optional[Dict[str, Any]]:
        quote = self.quote(symbol)
        if not quote:
            return None
        bid, ask = quote
        return {"bid": bid, "ask": ask, "point": self.point, "tick_size": self.point,
                "time_msc": self.clock() * 1000.0, "digits": self.digits,
                "contract_size": self.contract_size, "min_lot": self.min_lot,
                "step_lot": self.step_lot, "max_lot": self.max_lot,
                "stops_level": 0, "freeze_level": 0, "currency_profit": "USD"}

    def stage_limit_order(self, symbol: str, direction: str, volume: float,
                          limit_price: float, sl: float, tp: float, **kwargs) -> Dict[str, Any]:
        self._pump()
        direction = DIRECTION_MAP.get(str(direction).upper(), str(direction).upper())
        ticket = self._ticket()
        order = {"ticket": ticket, "symbol": symbol, "direction": direction,
                 "volume": float(volume), "price_open": float(limit_price),
                 "sl": float(sl), "tp": float(tp),
                 "magic": int(kwargs.get("magic", 100895)),
                 "comment": kwargs.get("comment", ""), "time": self.clock()}
        self.pending.append(order)
        self._pump()          # an already-crossed limit fills immediately
        result = {"success": True, "ticket": ticket}
        if kwargs.get("expiration_seconds"):
            result["expires_at"] = self.clock() + float(kwargs["expiration_seconds"])
        return result

    def modify_position_sltp(self, ticket: int, new_sl: float,
                             new_tp: Optional[float] = None) -> Dict[str, Any]:
        self._pump()
        for position in self.positions:
            if position["ticket"] == int(ticket):
                position["sl"] = float(new_sl) if new_sl else None
                position["tp"] = float(new_tp) if new_tp else position.get("tp")
                self.deals.append({"ticket": int(ticket), "event": "modify_sltp",
                                   "sl": position["sl"], "tp": position["tp"],
                                   "time": self.clock()})
                self._pump()
                return {"success": True, "ticket": int(ticket)}
        return {"success": False, "error": "position_not_found"}

    def cancel_pending_order(self, order_ticket: int) -> Dict[str, Any]:
        self._pump()
        for order in self.pending:
            if order["ticket"] == int(order_ticket):
                self.pending.remove(order)
                self.deals.append({"ticket": int(order_ticket), "event": "cancel",
                                   "time": self.clock()})
                return {"success": True, "ticket": int(order_ticket)}
        return {"success": False, "error": "order_not_found"}

    # ---------------------------------------------------- extended surface
    def resolve_symbol(self, asset: str) -> Optional[str]:
        return default_symbol_of(asset)

    def estimate_order(self, symbol: str, direction: str, entry: float, sl: float) -> Dict[str, Any]:
        return {"stop_loss_per_lot": abs(float(entry) - float(sl)) * self.contract_size,
                "margin_per_lot": self.margin_per_lot}

    def execute_market_order(self, symbol: str, direction: str, volume: float,
                             sl: float, tp: float, **kwargs) -> Dict[str, Any]:
        self._pump()
        direction = DIRECTION_MAP.get(str(direction).upper(), str(direction).upper())
        quote = self.quote(symbol)
        if not quote:
            return {"success": False, "uncertain": True, "error": "no_quote"}
        bid, ask = quote
        slip = self.slippage_bps / 1e4
        fill = ask * (1 + slip) if direction == "LONG" else bid * (1 - slip)
        ticket = self._ticket()
        position = {"ticket": ticket, "symbol": symbol, "direction": direction,
                    "volume": float(volume), "price_open": round(fill, self.digits),
                    "sl": float(sl) if sl else None, "tp": float(tp) if tp else None,
                    "magic": int(kwargs.get("magic", 100895)),
                    "comment": kwargs.get("comment", ""), "profit_usd": 0.0,
                    "time": self.clock()}
        self.positions.append(position)
        self.deals.append({"ticket": ticket, "event": "market_fill",
                           "price": position["price_open"], "volume": float(volume),
                           "time": self.clock(), "comment": position["comment"]})
        self._pump()
        return {"success": True, "ticket": ticket, "price_open": position["price_open"]}

    def close_position(self, ticket: int) -> Dict[str, Any]:
        self._pump()
        for position in self.positions:
            if position["ticket"] == int(ticket):
                quote = self.quote(position["symbol"])
                if not quote:
                    return {"success": False, "uncertain": True, "error": "no_quote"}
                bid, ask = quote
                exit_price = bid if position["direction"] == "LONG" else ask
                self._close_position(position, exit_price, "manual_close")
                return {"success": True}
        return {"success": False, "error": "position_not_found"}

    def position_deals(self, ticket: int) -> List[Dict[str, Any]]:
        return copy.deepcopy([d for d in self.deals if d["ticket"] == int(ticket)])

    def intent_filled(self, comment: str, prepared_at: float, magic: int = 100895) -> bool:
        self._pump()
        label = str(comment)
        if any(o.get("comment") == label for o in self.pending):
            return False
        return any(p.get("comment") == label for p in self.positions)

    def health(self) -> Dict[str, Any]:
        return {"healthy": True, "backend": self.name, "detail": "paper_simulation"}
