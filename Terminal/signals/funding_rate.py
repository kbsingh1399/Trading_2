"""Terminal/signals/funding_rate.py
==========================================
P1 FIX — Binance Perpetual Funding Rate signal.

Provides real-time funding rate for any Binance USDT-M perpetual.
Positive funding = longs paying shorts = crowded long positioning.
High positive funding on a bearish VWAP setup = +1 to +2 confluence points.

INTEGRATION STATUS: mapping and source-label hygiene only. No receiving
order-admission caller currently consumes this module's confluence points.
The premiumIndex endpoint does not always provide a predicted next rate.
"""
from __future__ import annotations

import logging
import time
from typing import Optional

logger = logging.getLogger("FundingRate")

# Cache TTL: funding rates change every 8 hours, but we poll every 15m bar
_CACHE: dict[str, tuple[float, Optional[float], float]] = {}  # symbol -> (rate, predicted|None, fetch_time)
_CACHE_TTL_SEC = 300   # 5 minutes cache


def _binance_symbol(mt5_symbol: str) -> Optional[str]:
    """Convert MT5 broker symbol to Binance futures symbol, e.g. BTCUSD.pi -> BTCUSDT, NERUSD.p -> NEARUSDT."""
    try:
        from Terminal.Asset_Universe import canonical_asset
        asset = canonical_asset(mt5_symbol)
        CRYPTO_ASSETS = {"BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "TRX", "DOT", "LINK", "BCH", "LTC", "AVAX", "NEAR"}
        if asset in CRYPTO_ASSETS:
            return f"{asset}USDT"
    except Exception:
        pass
    _MAP = {
        "BTCUSD.pi": "BTCUSDT", "BTCUSD.p": "BTCUSDT", "BTCUSDT": "BTCUSDT", "BTC": "BTCUSDT",
        "ETHUSD.pi": "ETHUSDT", "ETHUSD.p": "ETHUSDT", "ETHUSDT": "ETHUSDT", "ETH": "ETHUSDT",
        "SOLUSD.p": "SOLUSDT", "SOLUSD.pi": "SOLUSDT", "SOLUSDT": "SOLUSDT", "SOL": "SOLUSDT",
        "BNBUSD.p": "BNBUSDT", "BNBUSD.pi": "BNBUSDT", "BNBUSDT": "BNBUSDT", "BNB": "BNBUSDT",
        "XRPUSD.pi": "XRPUSDT", "XRPUSD.p": "XRPUSDT", "XRPUSDT": "XRPUSDT", "XRP": "XRPUSDT",
        "ADAUSD.p": "ADAUSDT", "ADAUSD.pi": "ADAUSDT", "ADAUSDT": "ADAUSDT", "ADA": "ADAUSDT",
        "DOGEUSD.p": "DOGEUSDT", "DOGEUSD.pi": "DOGEUSDT", "DOGUSD.p": "DOGEUSDT", "DOGUSD.pi": "DOGEUSDT", "DOGE": "DOGEUSDT",
        "LINKUSD.p": "LINKUSDT", "LINKUSD.pi": "LINKUSDT", "LNKUSD.p": "LINKUSDT", "LNKUSD.pi": "LINKUSDT", "LINK": "LINKUSDT",
        "LTCUSD.p": "LTCUSDT", "LTCUSD.pi": "LTCUSDT", "LTCUSDT": "LTCUSDT", "LTC": "LTCUSDT",
        "BCHUSD.p": "BCHUSDT", "BCHUSD.pi": "BCHUSDT", "BCHUSDT": "BCHUSDT", "BCH": "BCHUSDT",
        "AVAXUSD.p": "AVAXUSDT", "AVAXUSD.pi": "AVAXUSDT", "AVXUSD.p": "AVAXUSDT", "AVXUSD.pi": "AVAXUSDT", "AVAX": "AVAXUSDT",
        "TRXUSD.p": "TRXUSDT", "TRXUSD.pi": "TRXUSDT", "TRXUSDT": "TRXUSDT", "TRX": "TRXUSDT",
        "DOTUSD.p": "DOTUSDT", "DOTUSD.pi": "DOTUSDT", "DOTUSDT": "DOTUSDT", "DOT": "DOTUSDT",
        "NEARUSD.p": "NEARUSDT", "NEARUSD.pi": "NEARUSDT", "NERUSD.p": "NEARUSDT", "NERUSD.pi": "NEARUSDT", "NEAR": "NEARUSDT",
    }
    return _MAP.get(mt5_symbol)


def get_funding_rate(mt5_symbol: str, *, force_refresh: bool = False) -> dict:
    """Fetch current and predicted funding rate from Binance.

    Args:
        mt5_symbol:     MT5 broker symbol (e.g. 'BTCUSD.pi').
        force_refresh:  Bypass cache.

    Returns:
        {
          "symbol":          "BTCUSDT",
          "funding_rate":    0.00021,    # current 8h rate (signed)
          "predicted_rate":  0.00019,    # next funding rate (Binance estimate)
          "mark_price":      83420.0,
          "rate_bps":        2.1,        # current rate in basis points
          "bias":            "long_crowded" | "short_crowded" | "neutral",
          "confluence_pts":  0,          # +1 to +2 for shorts, -1 to -2 for longs
          "source":          "binance_perp",
          "available":       True,
        }
    """
    binance_sym = _binance_symbol(mt5_symbol)
    if not binance_sym:
        return {"available": False, "symbol": mt5_symbol, "reason": "no_binance_mapping"}

    # Cache hit
    cached = _CACHE.get(binance_sym)
    if cached and not force_refresh and (time.time() - cached[2]) < _CACHE_TTL_SEC:
        rate, predicted, _ = cached
        return _build_result(binance_sym, rate, predicted, None)

    # Fetch from Binance
    try:
        import urllib.request, json
        url = (
            f"https://fapi.binance.com/fapi/v1/premiumIndex"
            f"?symbol={binance_sym}"
        )
        req = urllib.request.Request(url, headers={"User-Agent": "TradingRiskBot/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            d = json.loads(resp.read().decode())

        if d.get("lastFundingRate") is None or d.get("markPrice") is None:
            return {"available": False, "symbol": binance_sym, "reason": "missing_funding_or_mark"}
        rate      = float(d["lastFundingRate"])
        predicted = float(d["nextFundingRate"]) if d.get("nextFundingRate") is not None else None
        mark      = float(d["markPrice"])

        _CACHE[binance_sym] = (rate, predicted, time.time())
        return _build_result(binance_sym, rate, predicted, mark)

    except Exception as exc:
        logger.warning("get_funding_rate(%s) failed: %s", binance_sym, exc)
        return {"available": False, "symbol": binance_sym, "reason": str(exc)}


def _build_result(symbol: str, rate: float, predicted: Optional[float], mark_price: Optional[float]) -> dict:
    rate_bps = rate * 10_000  # e.g. 0.00021 → 2.1 bps

    # Bias classification
    if rate > 0.0010:          # > 10 bps per 8h = extreme long crowding
        bias = "extreme_long_crowded"
        confluence_pts = 2     # very bullish for shorts
    elif rate > 0.0003:        # > 3 bps = elevated long crowding
        bias = "long_crowded"
        confluence_pts = 1     # mild bullish for shorts
    elif rate < -0.0010:       # < -10 bps = extreme short crowding
        bias = "extreme_short_crowded"
        confluence_pts = -2    # bearish for additional shorts
    elif rate < -0.0003:
        bias = "short_crowded"
        confluence_pts = -1
    else:
        bias = "neutral"
        confluence_pts = 0

    return {
        "symbol":           symbol,
        "funding_rate":     round(rate, 6),
        "predicted_rate":   round(predicted, 6) if predicted is not None else None,
        "predicted_source": "nextFundingRate" if predicted is not None else "unavailable",
        "mark_price":       mark_price,
        "rate_bps":         round(rate_bps, 3),
        "bias":             bias,
        "confluence_pts":   confluence_pts,
        "source":           "binance_perp",
        "available":        True,
    }


def funding_short_bias(mt5_symbol: str, threshold_bps: float = 3.0) -> bool:
    """Return True if funding rate provides a SHORT confluence signal.

    Condition: funding rate > threshold_bps per 8h (longs crowded and vulnerable).
    Use this as an additive filter on top of VWAP + CVD + L3 gates.
    """
    result = get_funding_rate(mt5_symbol)
    if not result.get("available"):
        return False
    return result["rate_bps"] > threshold_bps
