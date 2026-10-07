#!/usr/bin/env python3
"""
Terminal/MT5_Execution_Bridge.py
================================
Native MetaTrader 5 Execution & Position Management Bridge.
Provides robust IPC communication with MetaTrader 5 terminal:
- Account status inspection (balance, equity, margin)
- Open position tracking and ticket resolution
- Dynamic 3-stage ratchet SL/TP modification (TRADE_ACTION_SLTP)
- Market order execution with contract size awareness
- Auto-discovery symbol mapping (e.g. SOL -> SOLUSD.p, BTC -> BTCUSD.pi)
"""

import sys
import time
import datetime
import logging
from typing import Dict, List, Any, Optional, Sequence
from Terminal.Asset_Universe import broker_candidates
from Terminal.Risk_Sizing_Engine import floor_volume

# Install against MetaTrader5 itself, without importing a partially initialized
# bridge from the guard. Refuse to load a trading bridge if installation fails.
try:
    import MetaTrader5 as mt5
    MT5_AVAILABLE = True
except ImportError:
    mt5 = None
    MT5_AVAILABLE = False

from Terminal.risk.blackout_guard import BlackoutGuard, is_in_blackout
if MT5_AVAILABLE:
    try:
        _BLACKOUT_GUARD_ACTIVE = BlackoutGuard.install()
    except Exception as exc:
        raise RuntimeError(f"MT5 blackout protection unavailable: {exc}") from exc
else:
    _BLACKOUT_GUARD_ACTIVE = False

logger = logging.getLogger("MT5Bridge")
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("[%(asctime)s][MT5Bridge] %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class MT5ExecutionBridge:
    def __init__(self, account_id: Optional[int] = None, timeout_ms: int = 5000):
        self.account_id = account_id
        self.timeout_ms = timeout_ms
        self.initialized = False
        self._symbol_cache: Dict[str, str] = {}
        self._offset_cache: Dict[str, tuple] = {}
        # MetaQuotes ticks are broker server time (EET/UTC+3, offset 10800s)
        self.broker_utc_offset_sec: int = 10800
        self.broker_utc_offset_ms: int = 10800 * 1000
        self.ensure_connected()

    def _normalize_tick_msc(self, raw_msc: int) -> int:
        if not raw_msc:
            return 0
        now_ms = time.time() * 1000
        # If broker tick is ~3 hours ahead (EET server time), normalize to UTC
        if raw_msc - now_ms > 3600 * 1000:
            return int(raw_msc - self.broker_utc_offset_ms)
        return int(raw_msc)

    def _utc_offset_seconds(self, symbol: Optional[str] = None) -> int:
        """Best-effort broker-server-to-UTC offset, snapped to a 30-min grid.

        MT5 bar, position and order timestamps are broker *server* time. Ticks
        carry ``time_msc`` from the same clock, so a fresh tick gives us the
        offset. Returning 0 when the server already runs UTC keeps behaviour
        unchanged for UTC brokers. Cached 300s per symbol; failures are
        treated as offset 0 (the historical behaviour).
        """
        cached = self._offset_cache.get(symbol or "*")
        if cached and abs(time.time() - cached[1]) < 300:
            return cached[0]
        offset = 0
        try:
            if symbol and MT5_AVAILABLE:
                tick = mt5.symbol_info_tick(symbol)
                raw_msc = getattr(tick, "time_msc", 0) if tick else 0
                if raw_msc:
                    delta = raw_msc/1000.0 - time.time()
                    if abs(delta) > 2700:  # > 45 min out: a real TZ offset
                        offset = int(round(delta/1800.0)*1800)
                        offset = max(-14*3600, min(14*3600, offset))
        except Exception:
            offset = 0
        self._offset_cache[symbol or "*"] = (offset, time.time())
        return offset

    def ensure_connected(self) -> bool:
        if not MT5_AVAILABLE:
            logger.warning("MetaTrader5 python module is not installed.")
            return False

        if not mt5.terminal_info() or not mt5.terminal_info().connected:
            ok = mt5.initialize(timeout=self.timeout_ms)
            if not ok:
                logger.error(f"MT5 initialize() failed. Error code: {mt5.last_error()}")
                self.initialized = False
                return False
            self.initialized = True
        else:
            self.initialized = True

        if self.account_id is not None:
            acc = mt5.account_info()
            actual = getattr(acc, "login", None) if acc else None
            if actual != self.account_id:
                logger.error("MT5 account mismatch: expected %s, got %s", self.account_id, actual)
                self.initialized = False
                return False
        return True

    def get_account_summary(self) -> Dict[str, Any]:
        if not self.ensure_connected():
            return {"connected": False, "error": "MT5 not connected"}

        acc = mt5.account_info()
        if not acc:
            return {"connected": False, "error": f"Failed to get account info: {mt5.last_error()}"}

        return {
            "connected": True,
            "login": getattr(acc, "login", 0),
            "trade_mode": getattr(acc, "trade_mode", 0),
            "company": getattr(acc, "company", ""),
            "currency": getattr(acc, "currency", None),  # never infer account denomination
            "balance_usd": round(float(getattr(acc, "balance", 0.0) or 0.0), 2),
            "equity_usd": round(float(getattr(acc, "equity", 0.0) or 0.0), 2),
            "profit_usd": round(float(getattr(acc, "profit", 0.0) or 0.0), 2),
            "margin_usd": round(float(getattr(acc, "margin", 0.0) or 0.0), 2),
            "margin_free_usd": round(float(getattr(acc, "margin_free", 0.0) or 0.0), 2),
            "margin_level_pct": round(float(getattr(acc, "margin_level", 0.0) or 0.0), 2),
        }

    def resolve_symbol(self, coin: str) -> Optional[str]:
        coin = coin.strip().upper()
        if coin in self._symbol_cache:
            return self._symbol_cache[coin]

        if not self.ensure_connected():
            return None

        # Fetch all symbols and search for exact or prefixed/suffixed match
        symbols = mt5.symbols_get()
        if not symbols:
            return None

        candidates = [s.name for s in symbols]
        for name in broker_candidates(coin):
            if name in candidates:
                self._symbol_cache[coin] = name
                return name
        # Unknown aliases must be configured explicitly; substring discovery can
        # map a synthetic index to an unrelated broker instrument.
        return None

    def get_symbol_price(self, symbol: str) -> Optional[Dict[str, Any]]:
        if not self.ensure_connected():
            return None

        if not mt5.symbol_select(symbol, True):
            logger.warning(f"Failed to select symbol {symbol}")
            return None

        tick = mt5.symbol_info_tick(symbol)
        info = mt5.symbol_info(symbol)
        if not tick or not info:
            return None

        raw_msc = getattr(tick, "time_msc", 0) or 0
        utc_msc = self._normalize_tick_msc(raw_msc)
        return {
            "symbol": symbol,
            "bid": tick.bid,
            "ask": tick.ask,
            "last": tick.last if tick.last > 0 else (tick.bid + tick.ask) / 2.0,
            "spread": info.spread,
            "point": info.point,
            "digits": info.digits,
            "contract_size": info.trade_contract_size,
            "min_lot": info.volume_min,
            "max_lot": info.volume_max,
            "step_lot": info.volume_step,
            "time_msc": utc_msc,
            "raw_time_msc": raw_msc,
            "receipt_time": time.time(),
            "tick_size": getattr(info, "trade_tick_size", info.point),
            "stops_level": getattr(info, "trade_stops_level", 0),
            "freeze_level": getattr(info, "trade_freeze_level", 0),
            "trade_mode": getattr(info, "trade_mode", None),
            "currency_profit": getattr(info, "currency_profit", None)
        }

    def get_recent_bars(self, symbol: str, count: int = 96, timeframe: Any = None) -> List[Dict[str, Any]]:
        """Return completed MT5 bars for the local regime classifier.

        The current, still-forming bar is deliberately excluded.  If the
        terminal does not expose ``copy_rates_from_pos`` this returns an empty
        list rather than fabricating candles.
        """
        if not self.ensure_connected() or not hasattr(mt5, "copy_rates_from_pos"):
            return []
        if timeframe is None:
            timeframe = getattr(mt5, "TIMEFRAME_M15", None)
        if timeframe is None or not mt5.symbol_select(symbol, True):
            return []
        try:
            raw = mt5.copy_rates_from_pos(symbol, timeframe, 1, max(8, int(count)))
        except Exception as exc:
            logger.warning("Unable to read recent bars for %s: %s", symbol, exc)
            return []
        if raw is None:
            return []
        # Bar timestamps are broker server time; normalize to UTC epoch so
        # downstream causality filters (epoch(bar)+900 <= now) are not biased
        # by the server timezone (Finding F-06).
        offset = self._utc_offset_seconds(symbol)
        bars = []
        for row in raw:
            def value(name: str, default: float = 0.0) -> float:
                try:
                    item = row[name] if hasattr(row, "dtype") and name in row.dtype.names else getattr(row, name, default)
                    return float(item)
                except (KeyError, TypeError, ValueError, AttributeError):
                    return default
            rv = value("real_volume", 0.0)
            tv = value("tick_volume", 0.0)
            vol = rv if rv > 0 else tv
            bars.append({
                "time": value("time") - offset,
                "open": value("open"),
                "high": value("high"),
                "low": value("low"),
                "close": value("close"),
                "volume": vol,
                "tick_volume": tv,
                "real_volume": rv,
            })
        return bars

    def get_execution_quality(self, symbol: str) -> Optional[Dict[str, float]]:
        """Return a fresh quote and spread metrics used by the execution guard."""
        quote = self.get_symbol_price(symbol)
        if not quote:
            return None
        point = max(float(quote.get("point", 0.0)), 1e-12)
        bid, ask = float(quote.get("bid", 0.0)), float(quote.get("ask", 0.0))
        spread_price = max(0.0, ask - bid)
        mid = (bid + ask) / 2.0 if bid > 0.0 and ask > 0.0 else 0.0
        return {
            "bid": bid,
            "ask": ask,
            "mid": mid,
            "spread_price": spread_price,
            "spread_points": spread_price / point,
            "spread_bps": spread_price / mid * 10_000.0 if mid > 0.0 else 0.0,
            "point": point,
            "digits": float(quote.get("digits", 2)),
        }

    @staticmethod
    def _floor_volume(volume: float, step: float, minimum: float, maximum: float) -> float:
        """Normalize down, never up, so requested stop risk is not exceeded."""
        return floor_volume(volume, step, minimum, maximum)

    def get_open_positions(self, symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        if not self.ensure_connected():
            raise RuntimeError("Position inventory unavailable: MT5 disconnected")

        raw_positions = mt5.positions_get(symbol=symbol) if symbol else mt5.positions_get()
        if raw_positions is None:
            raise RuntimeError(f"Position inventory failed: {mt5.last_error()}")

        out = []
        for p in raw_positions:
            p_type = getattr(p, "type", None)
            if p_type == getattr(mt5, "ORDER_TYPE_BUY", 0):
                direction = "LONG"
            elif p_type == getattr(mt5, "ORDER_TYPE_SELL", 1):
                direction = "SHORT"
            else:
                raise ValueError(f"unsupported_position_type:{p_type}")
            out.append({
                "ticket": p.ticket,
                "identifier": getattr(p, "identifier", p.ticket),
                "time": p.time - self._utc_offset_seconds(p.symbol),
                "symbol": p.symbol,
                "direction": direction,
                "volume": p.volume,
                "price_open": p.price_open,
                "sl": p.sl,
                "tp": p.tp,
                "price_current": p.price_current,
                "profit_usd": round(p.profit, 2),
                "swap_usd": round(p.swap, 2),
                "magic": p.magic,
                "comment": p.comment
            })
        return out

    def get_pending_orders(self):
        if not self.ensure_connected(): raise RuntimeError("Pending inventory unavailable")
        orders = mt5.orders_get()
        if orders is None: raise RuntimeError(f"Pending inventory failed: {mt5.last_error()}")
        buy_types = {getattr(mt5, "ORDER_TYPE_BUY", 0), getattr(mt5, "ORDER_TYPE_BUY_LIMIT", 2),
                     getattr(mt5, "ORDER_TYPE_BUY_STOP", 4), getattr(mt5, "ORDER_TYPE_BUY_STOP_LIMIT", 6),
                     "ORDER_TYPE_BUY", "BUY", "ORDER_TYPE_BUY_LIMIT", "BUY_LIMIT",
                     "ORDER_TYPE_BUY_STOP", "BUY_STOP", "ORDER_TYPE_BUY_STOP_LIMIT", "BUY_STOP_LIMIT"}
        sell_types = {getattr(mt5, "ORDER_TYPE_SELL", 1), getattr(mt5, "ORDER_TYPE_SELL_LIMIT", 3),
                      getattr(mt5, "ORDER_TYPE_SELL_STOP", 5), getattr(mt5, "ORDER_TYPE_SELL_STOP_LIMIT", 7),
                      "ORDER_TYPE_SELL", "SELL", "ORDER_TYPE_SELL_LIMIT", "SELL_LIMIT",
                      "ORDER_TYPE_SELL_STOP", "SELL_STOP", "ORDER_TYPE_SELL_STOP_LIMIT", "SELL_STOP_LIMIT"}
        out = []
        for o in orders:
            o_type = getattr(o, "type", None)
            if o_type in buy_types:
                direction = "LONG"
            elif o_type in sell_types:
                direction = "SHORT"
            else:
                raise ValueError(f"unsupported_pending_order_type:{o_type}")
            out.append({
                "ticket": o.ticket, "symbol": o.symbol, "magic": o.magic, "comment": o.comment,
                "volume": o.volume_current, "price_open": getattr(o, "price_open", 0.0),
                "sl": getattr(o, "sl", 0.0), "tp": getattr(o, "tp", 0.0), "type": o_type,
                "direction": direction,
                "expiration": getattr(o, "time_expiration", 0) - self._utc_offset_seconds(o.symbol),
                "time_setup": getattr(o, "time_setup", getattr(o, "time", 0)) - self._utc_offset_seconds(o.symbol)
            })
        return out

    def intent_filled(self, comment: str, prepared_at: float, magic: int = 100895) -> bool:
        """Fill evidence for an intent: True iff an entry deal exists for it.

        Used by the reconciler to distinguish "limit order expired unfilled"
        from "limit order filled inside the inventory race window" without
        waiting for the next position snapshot.
        """
        if not self.ensure_connected(): raise RuntimeError("Intent history unavailable")
        start = datetime.datetime.fromtimestamp(prepared_at-30, datetime.timezone.utc)
        end = datetime.datetime.now(datetime.timezone.utc)
        deals = mt5.history_deals_get(start, end)
        if deals is None: raise RuntimeError("Intent deal-history query failed")
        return any(d.comment == comment and d.magic == magic and d.entry in (0, 2) for d in deals)

    def estimate_order(self, symbol, direction, entry, sl):
        """Use the broker's CFD calculation mode, not an assumed pip multiplier."""
        if not self.ensure_connected(): raise ValueError("Broker valuation unavailable")
        kind = mt5.ORDER_TYPE_BUY if direction == "LONG" else mt5.ORDER_TYPE_SELL
        profit = mt5.order_calc_profit(kind, symbol, 1.0, entry, sl)
        margin = mt5.order_calc_margin(kind, symbol, 1.0, entry)
        if profit is None or margin is None or profit >= 0 or margin <= 0:
            raise ValueError(f"Broker risk/margin calculation failed: {mt5.last_error()}")
        return {"stop_loss_per_lot": abs(float(profit)), "margin_per_lot": float(margin)}

    def position_deals(self, ticket):
        if not self.ensure_connected(): raise RuntimeError("Deal history unavailable")
        deals = mt5.history_deals_get(position=int(ticket))
        if deals is None: raise RuntimeError("Deal history failed")
        return [{"ticket": d.ticket, "position_id": d.position_id, "time_msc": d.time_msc,
                 "entry": d.entry, "volume": d.volume, "price": d.price,
                 "profit_usd": d.profit, "commission_usd": d.commission, "swap_usd": d.swap,
                 "fee_usd": getattr(d, "fee", 0)} for d in deals]

    def reconcile_intent_history(self, comment, prepared_at, magic=100895):
        """A filled-and-already-closed position can disappear before inventory polling."""
        if not self.ensure_connected(): raise RuntimeError("Intent history unavailable")
        start = datetime.datetime.fromtimestamp(prepared_at-30, datetime.timezone.utc)
        end = datetime.datetime.now(datetime.timezone.utc)
        deals = mt5.history_deals_get(start, end)
        if deals is None: raise RuntimeError("Intent deal-history query failed")
        entries = [d for d in deals if d.comment == comment and d.magic == magic and d.entry in (0, 2)]
        if not entries: return None
        ids = {d.position_id for d in entries}
        if len(ids) != 1: raise RuntimeError("Intent maps to multiple position identifiers")
        identifier = ids.pop(); history = self.position_deals(identifier)
        incoming = sum(d["volume"] for d in history if d["entry"] == 0)
        outgoing = sum(d["volume"] for d in history if d["entry"] in (1, 3))
        if incoming > 0 and outgoing >= incoming-1e-8:
            return {"state": "FILLED_CLOSED", "position_id": identifier, "deals": history,
                    "net_pnl_usd": sum(d[k] for d in history for k in ("profit_usd", "commission_usd", "swap_usd", "fee_usd"))}
        return None

    def modify_position_sltp(self, ticket: int, new_sl: float, new_tp: Optional[float] = None) -> Dict[str, Any]:
        """Modify SL/TP after validating side, quote freshness, and broker stops.

        ``new_tp=None`` preserves the current TP.  The method is idempotent at
        the caller and never moves a stop in the adverse direction; ratchet
        policy remains in ``OF_Strategy.py``.
        """
        if not self.ensure_connected():
            return {"success": False, "error": "MT5 not connected"}

        # Find position to check symbol and digits
        positions = mt5.positions_get(ticket=ticket)
        if not positions or len(positions) == 0:
            return {"success": False, "error": f"Position ticket {ticket} not found"}

        pos = positions[0]
        symbol = pos.symbol
        info = mt5.symbol_info(symbol)
        tick = mt5.symbol_info_tick(symbol)
        if not info or not tick:
            return {"success": False, "error": f"Quote metadata missing for {symbol}"}
        digits = info.digits
        rounded_sl = round(float(new_sl), digits) if new_sl and new_sl > 0 else 0.0
        current_sl = float(getattr(pos, "sl", 0.0) or 0.0)
        if rounded_sl <= 0: return {"success": False, "error": "Protective SL cannot be removed"}
        if rounded_sl > 0.0 and current_sl > 0.0:
            if pos.type == mt5.ORDER_TYPE_BUY and rounded_sl < current_sl:
                return {"success": False, "error": "SL ratchet cannot move a buy stop lower"}
            if pos.type == mt5.ORDER_TYPE_SELL and rounded_sl > current_sl:
                return {"success": False, "error": "SL ratchet cannot move a sell stop higher"}
        current_tp = float(getattr(pos, "tp", 0.0) or 0.0)
        rounded_tp = round(float(new_tp), digits) if new_tp is not None else round(current_tp, digits)
        point = max(float(getattr(info, "point", 0.0) or 0.0), 1e-12)
        min_distance = max(
            float(getattr(info, "trade_stops_level", 0) or 0),
            float(getattr(info, "trade_freeze_level", 0) or 0),
        ) * point
        bid, ask = float(getattr(tick, "bid", 0.0) or 0.0), float(getattr(tick, "ask", 0.0) or 0.0)
        raw_msc = getattr(tick, "time_msc", 0) or 0
        tick_utc_ms = self._normalize_tick_msc(raw_msc)
        tick_age = time.time()*1000 - tick_utc_ms
        if not -30000 <= tick_age <= 30000 or not 0 < bid < ask:
            return {"success": False, "error": f"Stale or invalid ratchet quote: age {tick_age:.0f}ms"}
        min_distance = max(min_distance, point)
        if rounded_sl > 0.0 and min_distance > 0.0:
            if pos.type == mt5.ORDER_TYPE_BUY and rounded_sl > bid - min_distance:
                return {"success": False, "error": "SL violates buy stop/freeze distance"}
            if pos.type == mt5.ORDER_TYPE_SELL and rounded_sl < ask + min_distance:
                return {"success": False, "error": "SL violates sell stop/freeze distance"}
        if rounded_tp > 0.0 and min_distance > 0.0:
            if pos.type == mt5.ORDER_TYPE_BUY and rounded_tp < ask + min_distance:
                return {"success": False, "error": "TP violates buy stop/freeze distance"}
            if pos.type == mt5.ORDER_TYPE_SELL and rounded_tp > bid - min_distance:
                return {"success": False, "error": "TP violates sell stop/freeze distance"}

        request = {
            "action": mt5.TRADE_ACTION_SLTP,
            "position": ticket,
            "symbol": symbol,
            "sl": rounded_sl,
            "tp": rounded_tp
        }

        result = mt5.order_send(request)
        if result is None:
            err = mt5.last_error()
            return {"success": False, "error": f"order_send failed: {err}"}

        if result.retcode != mt5.TRADE_RETCODE_DONE:
            return {
                "success": False,
                "retcode": result.retcode,
                "comment": result.comment,
                "error": f"Retcode: {result.retcode} ({result.comment})"
            }

        logger.info(f"[OK] Position {ticket} ({symbol}) modified: SL -> {rounded_sl} USD, TP -> {rounded_tp} USD")
        return {
            "success": True,
            "ticket": ticket,
            "symbol": symbol,
            "sl": rounded_sl,
            "tp": rounded_tp,
            "retcode": result.retcode
        }

    def execute_market_order(
        self,
        symbol: str,
        direction: str,
        volume: float,
        sl: float,
        tp: float,
        magic: int = 100895,
        comment: str = "OFC_AI_15M",
        *,
        max_spread_points: Optional[float] = None,
        deviation_points: int = 20,
        max_tick_age_ms: int = 2_000,
        filling_types: Optional[Sequence[int]] = None,
    ) -> Dict[str, Any]:
        """
        Executes a live market order on MT5.
        """
        if not self.ensure_connected():
            return {"success": False, "error": "MT5 not connected"}

        if not mt5.symbol_select(symbol, True):
            return {"success": False, "error": f"Symbol {symbol} select failed"}

        sym_info = mt5.symbol_info(symbol)
        tick = mt5.symbol_info_tick(symbol)
        if not sym_info or not tick:
            return {"success": False, "error": f"Failed to get tick for {symbol}"}

        side = direction.upper()
        if side not in {"LONG", "SHORT", "BUY", "SELL"}:
            return {"success": False, "error": f"Unsupported direction: {direction}"}
        is_long = side in {"LONG", "BUY"}
        order_type = mt5.ORDER_TYPE_BUY if is_long else mt5.ORDER_TYPE_SELL
        price = float(tick.ask if is_long else tick.bid)
        digits = sym_info.digits
        point = max(float(sym_info.point), 1e-12)
        spread_points = max(0.0, float(tick.ask - tick.bid) / point)
        if max_spread_points is not None and spread_points > float(max_spread_points):
            return {"success": False, "error": f"Spread guard: {spread_points:.1f} > {max_spread_points} points", "spread_points": spread_points}
        tick_time_msc = getattr(tick, "time_msc", 0) or 0
        if max_tick_age_ms > 0:
            tick_utc_ms = self._normalize_tick_msc(tick_time_msc)
            age_ms = int(time.time() * 1000 - tick_utc_ms)
            if not tick_time_msc or not -30000 <= age_ms <= max_tick_age_ms:
                return {"success": False, "error": f"Stale quote: {age_ms} ms", "age_ms": age_ms}

        clamped_vol = self._floor_volume(volume, sym_info.volume_step, sym_info.volume_min, sym_info.volume_max)
        if clamped_vol <= 0.0:
            return {"success": False, "error": "Requested volume is below broker minimum after risk-preserving normalization"}
        rounded_sl = round(float(sl), digits) if sl > 0 else 0.0
        rounded_tp = round(float(tp), digits) if tp > 0 else 0.0
        if not 0 < tick.bid < tick.ask or rounded_sl <= 0 or rounded_tp <= 0:
            return {"success": False, "error": "Valid two-sided quote and protective bracket required"}
        if not (rounded_sl < price < rounded_tp if is_long else rounded_tp < price < rounded_sl):
            return {"success": False, "error": "Invalid bracket direction"}
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": clamped_vol,
            "type": order_type,
            "price": round(price, digits),
            "sl": rounded_sl,
            "tp": rounded_tp,
            "deviation": max(0, int(deviation_points)),
            "magic": magic,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
        }

        try:
            from Terminal.risk.live_admission import assert_joint_fill_safe
            assert_joint_fill_safe(self, symbol, "LONG" if is_long else "SHORT",
                                   clamped_vol, price, rounded_sl)
        except (ValueError, RuntimeError, TypeError) as exc:
            return {"success": False, "error": f"admission_refused:{exc}"}

        candidates = list(filling_types or [
            getattr(mt5, "ORDER_FILLING_IOC", 1),
            getattr(mt5, "ORDER_FILLING_FOK", 0),
            getattr(mt5, "ORDER_FILLING_RETURN", 2),
        ])
        result = None
        attempted = []
        sent = False
        for filling in candidates:
            if filling in attempted:
                continue
            attempted.append(filling)
            request["type_filling"] = filling
            try:
                checked = mt5.order_check(request)
            except Exception as exc:
                return {"success": False, "error": f"order_check failed: {exc}"}
            if checked is None: return {"success": False, "error": "order_check returned no result"}
            if checked.retcode == getattr(mt5, "TRADE_RETCODE_INVALID_FILL", 10030): continue
            if checked.retcode not in (0, getattr(mt5, "TRADE_RETCODE_DONE", 10009)):
                return {"success": False, "retcode": checked.retcode, "error": f"order_check rejected: {checked.comment}"}
            result = mt5.order_send(request)
            sent = True
            # Only INVALID_FILL proves no fill occurred and permits another send.
            if result is None or result.retcode != getattr(mt5, "TRADE_RETCODE_INVALID_FILL", 10030):
                break
        filled_codes = {mt5.TRADE_RETCODE_DONE, getattr(mt5, "TRADE_RETCODE_DONE_PARTIAL", 10010)}
        if result is None or result.retcode not in filled_codes:
            retcode = result.retcode if result else "None"
            comment_err = result.comment if result else str(mt5.last_error())
            uncertain = (sent and result is None) or retcode in (getattr(mt5, "TRADE_RETCODE_TIMEOUT", 10012), getattr(mt5, "TRADE_RETCODE_CONNECTION", 10031), getattr(mt5, "TRADE_RETCODE_PLACED", 10008))
            return {"success": False, "uncertain": uncertain, "retcode": retcode, "error": f"Order rejected: {retcode} ({comment_err})", "spread_points": spread_points}

        logger.info(f"[FILL] MT5 Order filled: Deal {result.deal}, Ticket {result.order}, {direction} {clamped_vol} {symbol} at {result.price} USD")
        return {
            "success": True, "ticket": result.order, "deal": result.deal,
            "symbol": symbol, "direction": direction, "volume": float(getattr(result, "volume", clamped_vol)),
            "price": result.price, "sl": rounded_sl, "tp": rounded_tp,
            "partial": result.retcode == getattr(mt5, "TRADE_RETCODE_DONE_PARTIAL", 10010), "retcode": result.retcode,
            "spread_points": spread_points, "deviation_points": int(deviation_points),
        }

    def stage_limit_order(
        self,
        symbol: str,
        direction: str,
        volume: float,
        limit_price: float,
        sl: float,
        tp: float,
        *,
        expiration_seconds: int = 3600,
        max_spread_points: Optional[float] = None,
        passive_only: bool = True,
        persistent: bool = False,
        magic: int = 100895,
        comment: str = "OFC_AI_15M_LIMIT",
    ) -> Dict[str, Any]:
        """Stage a limit order with an attached protective bracket.

        ``persistent=True`` stages a GTC order with no broker expiration at
        all. Multi-hour resting orders (the Incident A remediation) must not
        rely on broker-side expirations: MT5 ``ORDER_TIME_SPECIFIED`` deadlines
        are evaluated in broker server time, which is DST-fragile from a UTC
        host. A persistent order is owned by the Order Persistence Governor,
        which enforces its own UTC deadlines and explicit cancels. The method
        never silently converts a passive order into a market order.
        """
        if not self.ensure_connected():
            return {"success": False, "error": "MT5 not connected"}
        side = direction.upper()
        if side not in {"LONG", "SHORT", "BUY", "SELL"}:
            return {"success": False, "error": f"Unsupported direction: {direction}"}
        is_long = side in {"LONG", "BUY"}
        if not mt5.symbol_select(symbol, True):
            return {"success": False, "error": f"Symbol {symbol} select failed"}
        info, tick = mt5.symbol_info(symbol), mt5.symbol_info_tick(symbol)
        if not info or not tick:
            return {"success": False, "error": f"Quote metadata missing for {symbol}"}
        point = max(float(info.point), 1e-12)
        spread_points = max(0.0, float(tick.ask - tick.bid) / point)
        if max_spread_points is not None and spread_points > float(max_spread_points):
            return {"success": False, "error": f"Spread guard: {spread_points:.1f} > {max_spread_points} points"}
        price = round(float(limit_price), info.digits)
        if price <= 0.0:
            return {"success": False, "error": "Limit price must be positive"}
        if passive_only:
            if is_long and price >= float(tick.ask):
                return {"success": False, "error": f"Buy limit {price} crosses ask {tick.ask} (not passive)"}
            if not is_long and price <= float(tick.bid):
                return {"success": False, "error": f"Sell limit {price} crosses bid {tick.bid} (not passive)"}
        tick_size = float(getattr(info, "trade_tick_size", point) or point)
        if abs(price/tick_size-round(price/tick_size)) > 1e-6:
            return {"success": False, "error": "limit_price_not_on_tick_grid"}
        min_distance = max(0, int(getattr(info, "trade_stops_level", 0)))*point
        entry_distance = float(tick.ask)-price if is_long else price-float(tick.bid)
        if entry_distance+point*1e-6 < min_distance:
            return {"success": False, "retcode": 10015, "error": "pending_entry_inside_broker_stops_level"}
        if sl <= 0 or tp <= 0 or (price-sl if is_long else sl-price) <= 0 or (tp-price if is_long else price-tp) <= 0:
            return {"success": False, "error": "pending_protective_bracket_invalid"}
        if min(abs(price-sl), abs(tp-price))+point*1e-6 < min_distance:
            return {"success": False, "retcode": 10016, "error": "pending_bracket_inside_broker_stops_level"}
        normalized = self._floor_volume(volume, info.volume_step, info.volume_min, info.volume_max)
        if normalized <= 0.0:
            return {"success": False, "error": "Requested volume is below broker minimum"}
        order_type = getattr(mt5, "ORDER_TYPE_BUY_LIMIT", 2) if is_long else getattr(mt5, "ORDER_TYPE_SELL_LIMIT", 3)
        broker_now = max(int(getattr(tick, "time", 0)), int(time.time()) + self.broker_utc_offset_sec)
        request = {
            "action": mt5.TRADE_ACTION_PENDING,
            "symbol": symbol,
            "volume": normalized,
            "type": order_type,
            "price": price,
            "sl": round(float(sl), info.digits) if sl > 0 else 0.0,
            "tp": round(float(tp), info.digits) if tp > 0 else 0.0,
            "deviation": 0,
            "magic": magic,
            "comment": comment,
            "type_time": getattr(mt5, "ORDER_TIME_GTC", 0) if persistent else getattr(mt5, "ORDER_TIME_SPECIFIED", mt5.ORDER_TIME_GTC),
            "expiration": 0 if persistent else broker_now + max(1, int(expiration_seconds)),
            "type_filling": getattr(mt5, "ORDER_FILLING_RETURN", getattr(mt5, "ORDER_FILLING_IOC", 1)),
        }
        try:
            from Terminal.risk.live_admission import assert_joint_fill_safe
            assert_joint_fill_safe(self, symbol, "LONG" if is_long else "SHORT",
                                   normalized, price, request["sl"])
        except (ValueError, RuntimeError, TypeError) as exc:
            return {"success": False, "error": f"admission_refused:{exc}"}
        if hasattr(mt5, "order_check"):
            checked = mt5.order_check(request)
            if checked is None or checked.retcode not in (0, getattr(mt5, "TRADE_RETCODE_DONE", 10009)):
                return {"success": False, "retcode": getattr(checked, "retcode", None), "error": "pending_order_check_rejected:"+str(getattr(checked, "comment", mt5.last_error()))}
        result = mt5.order_send(request)
        placed_codes = {getattr(mt5, "TRADE_RETCODE_DONE", 10009), getattr(mt5, "TRADE_RETCODE_PLACED", 10008)}
        if result is None or result.retcode not in placed_codes:
            retcode = result.retcode if result else "None"
            error = result.comment if result else str(mt5.last_error())
            return {"success": False, "retcode": retcode, "error": f"Limit order rejected: {retcode} ({error})"}
        logger.info("[LIMIT] MT5 limit staged: %s %s %s lots at %s (%s)", direction, normalized, symbol, price,
                    "GTC, governor-owned deadline" if persistent else f"expires in {expiration_seconds}s")
        return {"success": True, "ticket": getattr(result, "order", 0), "symbol": symbol, "direction": direction, "volume": normalized, "price": price, "sl": request["sl"], "tp": request["tp"],
                "persistent": bool(persistent), "expires_at": None if persistent else request["expiration"], "spread_points": spread_points}

    def cancel_pending_order(self, order_ticket: int) -> Dict[str, Any]:
        """Cancel one pending order; safe to call after an expiry race."""
        if not self.ensure_connected():
            return {"success": False, "error": "MT5 not connected"}
        result = mt5.order_send({"action": mt5.TRADE_ACTION_REMOVE, "order": int(order_ticket)})
        if result is None or result.retcode != getattr(mt5, "TRADE_RETCODE_DONE", 10009):
            return {"success": False, "retcode": getattr(result, "retcode", None), "error": getattr(result, "comment", str(mt5.last_error()))}
        return {"success": True, "ticket": int(order_ticket), "retcode": result.retcode}

    def close_position(self, ticket: int) -> Dict[str, Any]:
        """
        Closes an active position by ticket at market.
        """
        if not self.ensure_connected():
            return {"success": False, "error": "MT5 not connected"}

        positions = mt5.positions_get(ticket=ticket)
        if not positions or len(positions) == 0:
            return {"success": False, "error": f"Position ticket {ticket} not found"}

        pos = positions[0]
        symbol = pos.symbol
        sym_info = mt5.symbol_info(symbol)
        tick = mt5.symbol_info_tick(symbol)
        if not sym_info or not tick:
            return {"success": False, "error": f"Tick info missing for {symbol}"}

        close_type = mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
        close_price = tick.bid if pos.type == mt5.ORDER_TYPE_BUY else tick.ask

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "position": ticket,
            "symbol": symbol,
            "volume": pos.volume,
            "type": close_type,
            "price": close_price,
            "deviation": 25,
            "magic": pos.magic,
            "comment": "OFC_CLOSE",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        result = mt5.order_send(request)
        if result is not None and result.retcode == getattr(mt5, "TRADE_RETCODE_INVALID_FILL", 10030):
            request["type_filling"] = mt5.ORDER_FILLING_FOK
            result = mt5.order_send(request)

        if result is None or result.retcode not in {mt5.TRADE_RETCODE_DONE, getattr(mt5, "TRADE_RETCODE_DONE_PARTIAL", 10010)}:
            retcode = result.retcode if result else "None"
            err = result.comment if result else str(mt5.last_error())
            return {"success": False, "uncertain": result is None or retcode in (10012, 10031), "error": f"Close failed: {retcode} ({err})"}

        logger.info(f"[CLOSE] MT5 Position {ticket} closed at {result.price} USD | Deal: {result.deal}")
        return {"success": True, "partial": result.retcode != mt5.TRADE_RETCODE_DONE, "ticket": ticket, "price": result.price, "deal": result.deal}


if __name__ == "__main__":
    bridge = MT5ExecutionBridge()
    print("Account Summary:", bridge.get_account_summary())
    sol_symbol = bridge.resolve_symbol("SOL")
    print(f"Resolved SOL -> {sol_symbol}")
    if sol_symbol:
        print("Price Info:", bridge.get_symbol_price(sol_symbol))
    positions = bridge.get_open_positions()
    print(f"Open Positions ({len(positions)}):", positions)
