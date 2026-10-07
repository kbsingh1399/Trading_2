"""Terminal/signals/funding_rate.py
==========================================
P1 FIX — Binance Perpetual Funding Rate signal.

Provides real-time funding rate for any Binance USDT-M perpetual.
Positive funding = longs paying shorts = crowded long positioning.
High positive funding on a bearish VWAP setup = +1 to +2 confluence points.

INTEGRATION:
  Score breakdown added to 24-asset telemetry export in
  Terminal/Data_Factory/generate_telemetry_snapshot.py.
"""
from __future__ import annotations

import logging
import time
from typing import Optional

logger = logging.getLogger("FundingRate")

# Cache TTL: funding rates change every 8 hours, but we poll every 15m bar
_CACHE: dict[str, tuple[float, float, float]] = {}  # symbol -> (rate, predicted, fetch_time)
_CACHE_TTL_SEC = 300   # 5 minutes cache


def _binance_symbol(mt5_symbol: str) -> Optional[str]:
    """Convert MT5 broker symbol to Binance futures symbol, e.g. BTCUSD.pi → BTCUSDT."""
    _MAP = {
        "BTCUSD.pi":  "BTCUSDT",
        "ETHUSD.pi":  "ETHUSDT",
        "SOLUSD.p":   "SOLUSDT",
        "BNBUSD.p":   "BNBUSDT",
        "BNBUSD.pi":  "BNBUSDT",
        "XRPUSD.pi":  "XRPUSDT",
        "ADAUSD.p":   "ADAUSDT",
        "DOGEUSD.p":  "DOGEUSDT",
        "LINKUSD.p":  "LINKUSDT",
        "LTCUSD.p":   "LTCUSDT",
        "BCHUSD.p":   "BCHUSDT",
        "AVAXUSD.p":  "AVAXUSDT",
        "TRXUSD.p":   "TRXUSDT",
        "DOTUSD.p":   "DOTUSDT",
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

        rate      = float(d.get("lastFundingRate", 0.0))
        predicted = float(d.get("nextFundingRate", d.get("lastFundingRate", rate)))
        mark      = float(d.get("markPrice", 0.0))

        _CACHE[binance_sym] = (rate, predicted, time.time())
        return _build_result(binance_sym, rate, predicted, mark)

    except Exception as exc:
        logger.warning("get_funding_rate(%s) failed: %s", binance_sym, exc)
        return {"available": False, "symbol": binance_sym, "reason": str(exc)}


def _build_result(symbol: str, rate: float, predicted: float, mark_price: Optional[float]) -> dict:
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
        "predicted_rate":   round(predicted, 6),
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
