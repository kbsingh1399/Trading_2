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
import math
import logging
from typing import Dict, List, Any, Optional, Sequence

try:
    import MetaTrader5 as mt5
    MT5_AVAILABLE = True
except ImportError:
    mt5 = None
    MT5_AVAILABLE = False

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
        self.ensure_connected()

    def ensure_connected(self) -> bool:
        if not MT5_AVAILABLE:
            logger.warning("MetaTrader5 python module is not installed.")
            return False

        if not mt5.terminal_info() or not mt5.terminal_info().connected:
            ok = mt5.initialize()
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
            "login": acc.login,
            "trade_mode": acc.trade_mode,
            "company": acc.company,
            "currency": acc.currency,
            "balance_usd": round(acc.balance, 2),
            "equity_usd": round(acc.equity, 2),
            "profit_usd": round(acc.profit, 2),
            "margin_usd": round(acc.margin, 2),
            "margin_free_usd": round(acc.margin_free, 2),
            "margin_level_pct": round(acc.margin_level, 2) if acc.margin_level else 0.0,
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
        
        # Priority mapping patterns:
        patterns = [
            f"{coin}USD.p",
            f"{coin}USD.pi",
            f"{coin}USDT",
            f"{coin}USD",
            f"{coin[:3]}USD.p" if len(coin) > 3 else f"{coin}USD.p"
        ]

        # Handle known short codes (e.g. DOGE -> DOGUSD.p, LINK -> LNKUSD.p, NEAR -> NERUSD.p)
        known_aliases = {
            "DOGE": "DOGUSD.p",
            "LINK": "LNKUSD.p",
            "NEAR": "NERUSD.p",
            "AVAX": "AVXUSD.p",
            "SOL": "SOLUSD.p",
            "BTC": "BTCUSD.pi",
            "ETH": "ETHUSD.pi",
            "XRP": "XRPUSD.pi",
            "BNB": "BNBUSD.p",
            "ADA": "ADAUSD.p",
            "LTC": "LTCUSD.pi",
            "BCH": "BCHUSD.p"
        }
        if coin in known_aliases and known_aliases[coin] in candidates:
            self._symbol_cache[coin] = known_aliases[coin]
            return known_aliases[coin]

        for p in patterns:
            if p in candidates:
                self._symbol_cache[coin] = p
                return p

        # Partial match
        for s in candidates:
            if coin in s and "USD" in s:
                self._symbol_cache[coin] = s
                return s

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
            "step_lot": info.volume_step
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
        bars = []
        for row in raw:
            def value(name: str, default: float = 0.0) -> float:
                try:
                    item = row[name] if hasattr(row, "dtype") and name in row.dtype.names else getattr(row, name, default)
                    return float(item)
                except (KeyError, TypeError, ValueError, AttributeError):
                    return default
            bars.append({
                "time": value("time"),
                "open": value("open"),
                "high": value("high"),
                "low": value("low"),
                "close": value("close"),
                "volume": value("real_volume", value("tick_volume")),
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
        step = max(float(step), 1e-12)
        minimum, maximum = max(0.0, float(minimum)), max(float(maximum), float(minimum))
        requested = min(max(float(volume), 0.0), maximum)
        if requested < minimum:
            return 0.0
        units = math.floor((requested + 1e-12) / step)
        normalized = units * step
        if normalized < minimum:
            return 0.0
        decimals = max(0, min(8, int(round(-math.log10(step))) if step < 1 else 2))
        return round(min(normalized, maximum), decimals)

    def get_open_positions(self, symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        if not self.ensure_connected():
            return []

        raw_positions = mt5.positions_get(symbol=symbol) if symbol else mt5.positions_get()
        if raw_positions is None:
            return []

        out = []
        for p in raw_positions:
            out.append({
                "ticket": p.ticket,
                "time": p.time,
                "symbol": p.symbol,
                "direction": "LONG" if p.type == mt5.ORDER_TYPE_BUY else "SHORT",
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
        if rounded_sl > 0.0 and current_sl > 0.0:
            if pos.type == mt5.ORDER_TYPE_BUY and rounded_sl < current_sl:
                return {"success": False, "error": "SL ratchet cannot move a buy stop lower"}
            if pos.type == mt5.ORDER_TYPE_SELL and rounded_sl > current_sl:
                return {"success": False, "error": "SL ratchet cannot move a sell stop higher"}
        current_tp = float(getattr(pos, "tp", 0.0) or 0.0)
        rounded_tp = round(float(new_tp), digits) if new_tp is not None and new_tp > 0 else round(current_tp, digits)
        point = max(float(getattr(info, "point", 0.0) or 0.0), 1e-12)
        min_distance = max(
            float(getattr(info, "trade_stops_level", 0) or 0),
            float(getattr(info, "trade_freeze_level", 0) or 0),
        ) * point
        bid, ask = float(getattr(tick, "bid", 0.0) or 0.0), float(getattr(tick, "ask", 0.0) or 0.0)
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

        logger.info(f"✅ Position {ticket} ({symbol}) modified: SL -> {rounded_sl} USD, TP -> {rounded_tp} USD")
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
        if max_tick_age_ms > 0 and tick_time_msc:
            age_ms = int(time.time() * 1000 - tick_time_msc)
            if age_ms > max_tick_age_ms:
                return {"success": False, "error": f"Stale quote: {age_ms} ms", "age_ms": age_ms}

        clamped_vol = self._floor_volume(volume, sym_info.volume_step, sym_info.volume_min, sym_info.volume_max)
        if clamped_vol <= 0.0:
            return {"success": False, "error": "Requested volume is below broker minimum after risk-preserving normalization"}
        rounded_sl = round(float(sl), digits) if sl > 0 else 0.0
        rounded_tp = round(float(tp), digits) if tp > 0 else 0.0
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

        candidates = list(filling_types or [
            getattr(mt5, "ORDER_FILLING_IOC", 1),
            getattr(mt5, "ORDER_FILLING_FOK", 0),
            getattr(mt5, "ORDER_FILLING_RETURN", 2),
        ])
        request["type_filling"] = candidates[0]
        # order_check is a cheap server-side validation and prevents a send
        # when stops, margin, or volume are already invalid.
        if hasattr(mt5, "order_check"):
            try:
                checked = mt5.order_check(request)
                check_code = getattr(checked, "retcode", 0) if checked is not None else 0
                if check_code not in (0, getattr(mt5, "TRADE_RETCODE_DONE", 10009)):
                    return {"success": False, "retcode": check_code, "error": f"order_check rejected: {getattr(checked, 'comment', '')}"}
            except Exception as exc:
                logger.warning("order_check unavailable for %s: %s", symbol, exc)

        result = None
        attempted = []
        for filling in candidates:
            if filling in attempted:
                continue
            attempted.append(filling)
            request["type_filling"] = filling
            result = mt5.order_send(request)
            if result is not None and result.retcode == mt5.TRADE_RETCODE_DONE:
                break
        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
            retcode = result.retcode if result else "None"
            comment_err = result.comment if result else str(mt5.last_error())
            return {"success": False, "retcode": retcode, "error": f"Order rejected: {retcode} ({comment_err})", "spread_points": spread_points}

        logger.info(f"🚀 MT5 Order filled: Deal {result.deal}, Ticket {result.order}, {direction} {clamped_vol} {symbol} at {result.price} USD")
        return {
            "success": True, "ticket": result.order, "deal": result.deal,
            "symbol": symbol, "direction": direction, "volume": clamped_vol,
            "price": result.price, "sl": rounded_sl, "tp": rounded_tp,
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
        expiration_seconds: int = 30,
        max_spread_points: Optional[float] = None,
        passive_only: bool = True,
        magic: int = 100895,
        comment: str = "OFC_AI_15M_LIMIT",
    ) -> Dict[str, Any]:
        """Stage a short-lived limit order with an attached protective bracket.

        This is opt-in.  A passive order inside the spread can miss the trade
        or be adversely selected, so callers should retain a market/marketable
        limit fallback and cancel it at expiry.  The method never silently
        converts a passive order into a market order.
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
        if passive_only and not (float(tick.bid) <= price < float(tick.ask) if is_long else float(tick.bid) < price <= float(tick.ask)):
            return {"success": False, "error": "Limit is not passive and was rejected by passive_only guard"}
        normalized = self._floor_volume(volume, info.volume_step, info.volume_min, info.volume_max)
        if normalized <= 0.0:
            return {"success": False, "error": "Requested volume is below broker minimum"}
        order_type = getattr(mt5, "ORDER_TYPE_BUY_LIMIT", 2) if is_long else getattr(mt5, "ORDER_TYPE_SELL_LIMIT", 3)
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
            "type_time": getattr(mt5, "ORDER_TIME_SPECIFIED", mt5.ORDER_TIME_GTC),
            "expiration": int(time.time()) + max(1, int(expiration_seconds)),
            "type_filling": getattr(mt5, "ORDER_FILLING_RETURN", getattr(mt5, "ORDER_FILLING_IOC", 1)),
        }
        result = mt5.order_send(request)
        placed_codes = {getattr(mt5, "TRADE_RETCODE_DONE", 10009), getattr(mt5, "TRADE_RETCODE_PLACED", 10008)}
        if result is None or result.retcode not in placed_codes:
            retcode = result.retcode if result else "None"
            error = result.comment if result else str(mt5.last_error())
            return {"success": False, "retcode": retcode, "error": f"Limit order rejected: {retcode} ({error})"}
        logger.info("📌 MT5 limit staged: %s %s %s lots at %s (expires in %ss)", direction, normalized, symbol, price, expiration_seconds)
        return {"success": True, "ticket": getattr(result, "order", 0), "symbol": symbol, "direction": direction, "volume": normalized, "price": price, "sl": request["sl"], "tp": request["tp"], "expires_at": request["expiration"], "spread_points": spread_points}

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
        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
            request["type_filling"] = mt5.ORDER_FILLING_FOK
            result = mt5.order_send(request)

        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
            retcode = result.retcode if result else "None"
            err = result.comment if result else str(mt5.last_error())
            return {"success": False, "error": f"Close failed: {retcode} ({err})"}

        logger.info(f"🛑 MT5 Position {ticket} closed at {result.price} USD | Deal: {result.deal}")
        return {"success": True, "ticket": ticket, "price": result.price, "deal": result.deal}


if __name__ == "__main__":
    bridge = MT5ExecutionBridge()
    print("Account Summary:", bridge.get_account_summary())
    sol_symbol = bridge.resolve_symbol("SOL")
    print(f"Resolved SOL -> {sol_symbol}")
    if sol_symbol:
        print("Price Info:", bridge.get_symbol_price(sol_symbol))
    positions = bridge.get_open_positions()
    print(f"Open Positions ({len(positions)}):", positions)
