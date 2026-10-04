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
import logging
from typing import Dict, List, Any, Optional

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

    def modify_position_sltp(self, ticket: int, new_sl: float, new_tp: float) -> Dict[str, Any]:
        """
        Modifies Stop Loss and Take Profit for an active MT5 position.
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
        digits = info.digits if info else 2

        rounded_sl = round(float(new_sl), digits)
        rounded_tp = round(float(new_tp), digits) if new_tp > 0 else 0.0

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
        comment: str = "OFC_AI_15M"
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

        order_type = mt5.ORDER_TYPE_BUY if direction.upper() == "LONG" else mt5.ORDER_TYPE_SELL
        price = tick.ask if direction.upper() == "LONG" else tick.bid
        digits = sym_info.digits

        # Clamp volume to allowed step & bounds
        vol_step = sym_info.volume_step
        vol_min = sym_info.volume_min
        vol_max = sym_info.volume_max
        clamped_vol = max(vol_min, min(vol_max, round(volume / vol_step) * vol_step))
        clamped_vol = round(clamped_vol, 2)

        rounded_sl = round(float(sl), digits) if sl > 0 else 0.0
        rounded_tp = round(float(tp), digits) if tp > 0 else 0.0

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": clamped_vol,
            "type": order_type,
            "price": price,
            "sl": rounded_sl,
            "tp": rounded_tp,
            "deviation": 20,
            "magic": magic,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        result = mt5.order_send(request)
        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
            # Fallback to FOK filling if IOC failed
            request["type_filling"] = mt5.ORDER_FILLING_FOK
            result = mt5.order_send(request)

        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
            retcode = result.retcode if result else "None"
            comment_err = result.comment if result else str(mt5.last_error())
            return {
                "success": False,
                "retcode": retcode,
                "error": f"Order rejected: {retcode} ({comment_err})"
            }

        logger.info(f"🚀 MT5 Order filled: Deal {result.deal}, Ticket {result.order}, {direction} {clamped_vol} {symbol} at {result.price} USD")
        return {
            "success": True,
            "ticket": result.order,
            "deal": result.deal,
            "symbol": symbol,
            "direction": direction,
            "volume": clamped_vol,
            "price": result.price,
            "sl": rounded_sl,
            "tp": rounded_tp
        }

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
