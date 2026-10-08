"""Terminal/signals/open_interest.py
===========================================
P1 FIX — Open Interest Rate of Change (OI_ROC) signal.

INSIGHT:
  OI rising while price falls  = new shorts added (institutional conviction → OK to short)
  OI falling while price falls = long liquidations (exhaustion → AVOID new shorts)
  OI rising while price rises  = new longs added (institutional conviction → avoid new longs at resistance)

INTEGRATION STATUS: source freshness and six missing symbol mappings are
fixed here, but the receiving order-admission path does not yet consume this
module. Until then an OI exhaustion veto is not an operational gate.
"""
from __future__ import annotations

import logging
import math
import time
from typing import Optional

logger = logging.getLogger("OpenInterest")

_CACHE: dict[str, tuple[float, float, list, float]] = {}  # symbol -> (roc, latest_oi, history, fetch_ts)
_CACHE_TTL_SEC = 300   # 5 minutes

# OI_ROC thresholds
_OI_ROC_CONVICTION_PCT  = +0.30   # > +0.30% over 4 bars = institutional short conviction
_OI_ROC_EXHAUSTION_PCT  = -1.00   # < -1.00% = liquidation exhaustion, avoid new shorts
_LOOKBACK_BARS          = 4       # 4 × 15m = 1 hour lookback


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


def get_oi_roc(mt5_symbol: str, *, lookback_bars: int = _LOOKBACK_BARS, force_refresh: bool = False) -> dict:
    """Fetch Open Interest Rate of Change from Binance.

    Args:
        mt5_symbol:     MT5 broker symbol (e.g. 'BTCUSD.pi').
        lookback_bars:  Number of 15m bars to measure OI change over.
        force_refresh:  Bypass cache.

    Returns:
        {
          "symbol":         "BTCUSDT",
          "oi_roc_pct":     +0.42,      # OI % change over lookback_bars
          "oi_latest_usd":  2.34e9,     # current OI in USD
          "oi_bars":        [2.31e9, ..., 2.34e9],
          "interpretation": "conviction_short" | "exhaustion_avoid" | "neutral",
          "confirms_short": True,
          "blocks_short":   False,
          "available":      True,
        }
    """
    binance_sym = _binance_symbol(mt5_symbol)
    if not binance_sym:
        return {"available": False, "symbol": mt5_symbol, "reason": "no_binance_mapping"}

    cached = _CACHE.get(binance_sym)
    if cached and not force_refresh and (time.time() - cached[3]) < _CACHE_TTL_SEC:
        roc, latest, history, _ = cached
        return _build_result(binance_sym, roc, latest, history)

    try:
        import urllib.request, json
        n_fetch = lookback_bars + 3   # extra to exclude open/future buckets
        url = (
            f"https://fapi.binance.com/futures/data/openInterestHist"
            f"?symbol={binance_sym}&period=15m&limit={n_fetch}"
        )
        req = urllib.request.Request(url, headers={"User-Agent": "TradingRiskBot/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())

        # Require two closed observations exactly four 15m intervals apart.
        now_ms = time.time() * 1000
        closed = sorted((d for d in data if float(d["timestamp"]) <= now_ms - 900_000),
                        key=lambda d: float(d["timestamp"]))
        if len(closed) < lookback_bars + 1:
            return {"available": False, "symbol": binance_sym, "reason": "insufficient_closed_oi_history"}
        window = closed[-(lookback_bars + 1):]
        stamps = [float(d["timestamp"]) for d in window]
        if now_ms - stamps[-1] > 30 * 60_000 or any(
            abs(stamps[i + 1] - stamps[i] - 900_000) > 60_000
            for i in range(len(stamps) - 1)
        ):
            return {"available": False, "symbol": binance_sym, "reason": "stale_or_gapped_oi_history"}
        oi_values = [float(d["sumOpenInterestValue"]) for d in window]
        oi_start  = oi_values[0]
        oi_end    = oi_values[-1]
        if oi_start <= 0 or oi_end <= 0 or any(not math.isfinite(v) for v in oi_values):
            return {"available": False, "symbol": binance_sym, "reason": "invalid_oi_values"}
        roc = (oi_end - oi_start) / oi_start * 100.0

        _CACHE[binance_sym] = (roc, oi_end, oi_values, time.time())
        return _build_result(binance_sym, roc, oi_end, oi_values)

    except Exception as exc:
        logger.warning("get_oi_roc(%s) failed: %s", binance_sym, exc)
        return {"available": False, "symbol": binance_sym, "reason": str(exc)}


def _build_result(symbol: str, roc: float, latest_oi: float, history: list) -> dict:
    confirms_short = roc >= _OI_ROC_CONVICTION_PCT
    blocks_short   = roc <= _OI_ROC_EXHAUSTION_PCT

    if roc >= _OI_ROC_CONVICTION_PCT:
        interpretation = "conviction_short"     # new shorts added = institutional pressure
    elif roc <= _OI_ROC_EXHAUSTION_PCT:
        interpretation = "exhaustion_avoid"     # longs liquidated = not a clean short
    elif roc > 0:
        interpretation = "mild_build"
    else:
        interpretation = "neutral"

    return {
        "symbol":           symbol,
        "oi_roc_pct":       round(roc, 4),
        "oi_latest_usd":    round(latest_oi, 0),
        "oi_bars":          history,
        "interpretation":   interpretation,
        "confirms_short":   bool(confirms_short),
        "blocks_short":     bool(blocks_short),
        "source":           "binance_perp",
        "available":        True,
    }


def oi_confirms_short(mt5_symbol: str) -> bool:
    """Return True if OI_ROC pattern supports a new short entry (not exhaustion)."""
    result = get_oi_roc(mt5_symbol)
    if not result.get("available"):
        return False  # cannot prove absence of liquidation exhaustion
    # Reject only if clearly in exhaustion territory
    return not result.get("blocks_short", False)
