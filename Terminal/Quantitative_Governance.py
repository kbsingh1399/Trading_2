"""Causal, lightweight quantitative governance primitives for the live trader.

This module intentionally contains no broker or network calls.  It turns the
raw Hyperdash/MT5 observations into bounded features that can be replayed in a
unit test and applied consistently in paper and live mode.

The functions are not alpha by themselves.  Their weights and thresholds must
be fitted on purged, out-of-sample data and then versioned with the feature
schema.  Missing data is represented explicitly rather than being treated as
positive evidence.
"""
from __future__ import annotations

import math
import time
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Deque, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import numpy as np


EPS = 1e-12


def _num(value: Any, default: float = 0.0) -> float:
    try:
        value = float(value)
        return value if math.isfinite(value) else default
    except (TypeError, ValueError):
        return default


def _bounded_imbalance(positive: float, negative: float) -> float:
    positive = max(0.0, _num(positive))
    negative = max(0.0, _num(negative))
    total = positive + negative
    return (positive - negative) / total if total > EPS else 0.0


def _sigmoid_strength(value: float, scale: float) -> float:
    """Map a non-negative notional to [0, 1] without a hard dollar cutoff."""
    if value <= 0.0 or scale <= 0.0:
        return 0.0
    return float(math.tanh(math.log1p(value / scale)))


def _timestamp_seconds(value: Any) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, datetime):
        dt = value if value.tzinfo else value.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    if isinstance(value, str):
        try:
            text = value.replace("Z", "+00:00")
            dt = datetime.fromisoformat(text)
            return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()
        except ValueError:
            return None
    number = _num(value, default=float("nan"))
    if not math.isfinite(number):
        return None
    # Unix milliseconds are larger than any plausible Unix-second timestamp.
    return number / 1000.0 if number > 100_000_000_000 else number


def _observation_age_seconds(item: Mapping[str, Any], now_seconds: float) -> Optional[float]:
    for key in ("observed_at", "timestamp", "time", "last_seen", "updated_at"):
        stamp = _timestamp_seconds(item.get(key))
        if stamp is not None:
            return max(0.0, now_seconds - stamp)
    return None


def _level_volumes(book: Mapping[str, Any]) -> Tuple[float, float]:
    """Read both the terminal's aggregate schema and a raw bid/ask schema."""
    bid = _num(book.get("bid_volume_usd", book.get("bid_volume", 0.0)))
    ask = _num(book.get("ask_volume_usd", book.get("ask_volume", 0.0)))
    if bid == 0.0 and ask == 0.0:
        for level in book.get("bids", []) or []:
            if isinstance(level, Mapping):
                bid += _num(level.get("notional_usd", level.get("total_usd", level.get("size", 0.0))))
            elif isinstance(level, (list, tuple)) and len(level) >= 2:
                bid += _num(level[1]) * _num(level[0])
        for level in book.get("asks", []) or []:
            if isinstance(level, Mapping):
                ask += _num(level.get("notional_usd", level.get("total_usd", level.get("size", 0.0))))
            elif isinstance(level, (list, tuple)) and len(level) >= 2:
                ask += _num(level[1]) * _num(level[0])
    return max(0.0, bid), max(0.0, ask)


def _trade_flow(trades: Sequence[Mapping[str, Any]], whale_min_usd: float = 50_000.0) -> Dict[str, float]:
    buy = sell = whale_buy = whale_sell = 0.0
    for trade in trades or []:
        side = str(trade.get("side", "")).upper()
        notional = _num(trade.get("notional_usd", 0.0))
        if notional <= 0.0:
            notional = _num(trade.get("price", trade.get("px", 0.0))) * _num(trade.get("size", trade.get("sz", 0.0)))
        if side in {"BUY", "B", "BID"}:
            buy += notional
            if bool(trade.get("is_whale", False)) or notional >= whale_min_usd:
                whale_buy += notional
        elif side in {"SELL", "S", "ASK"}:
            sell += notional
            if bool(trade.get("is_whale", False)) or notional >= whale_min_usd:
                whale_sell += notional
    return {
        "buy_notional": buy,
        "sell_notional": sell,
        "whale_buy_notional": whale_buy,
        "whale_sell_notional": whale_sell,
        "tick_imbalance": _bounded_imbalance(buy, sell),
        "whale_imbalance": _bounded_imbalance(whale_buy, whale_sell),
    }


def _cvd_metrics(data: Mapping[str, Any], trade_flow: Mapping[str, float], price: float) -> Tuple[float, float, bool]:
    """Return directional CVD, CVD/price divergence, and an availability flag."""
    history: Any = data.get("cvd_history", data.get("cvd", []))
    if not isinstance(history, (list, tuple)):
        history = []
    values = [_num(x.get("value", x.get("cvd", 0.0)) if isinstance(x, Mapping) else x) for x in history]
    values = [x for x in values if math.isfinite(x)]
    slope = _num(data.get("cvd_slope", 0.0))
    available = "cvd_slope" in data or len(values) >= 2
    if len(values) >= 2:
        slope = (values[-1] - values[0]) / max(1, len(values) - 1)
    scale = abs(_num(data.get("cvd_scale", 0.0)))
    if scale <= EPS:
        scale = max(trade_flow.get("buy_notional", 0.0) + trade_flow.get("sell_notional", 0.0), 1.0)
    cvd_direction = math.tanh(slope / scale)

    price_return = _num(data.get("price_return", data.get("return_15m", 0.0)))
    price_scale = abs(_num(data.get("atr_pct", 0.0)))
    if price_scale <= EPS:
        price_scale = 0.01
    price_direction = math.tanh((price_return / max(price, 1.0)) / price_scale) if price > 0 else 0.0
    # Positive means CVD is stronger than the price move: absorption/divergence
    divergence = math.tanh(1.5 * (cvd_direction - price_direction)) if available else 0.0
    return cvd_direction, divergence, available


def compute_orderflow_features(
    data: Mapping[str, Any],
    price: float,
    *,
    now_seconds: Optional[float] = None,
    max_distance_pct: float = 3.0,
    l3_distance_pct: float = 0.8,
    whale_min_usd: float = 150_000.0,
    liq_scale_usd: float = 100_000.0,
    l3_tau_seconds: float = 90.0,
    l3_ttl_seconds: float = 900.0,
) -> Dict[str, Any]:
    """Build normalized, direction-aware microstructure features.

    Liquidation and L3 notionals are converted to saturating strengths instead
    of being counted at fixed $100k/$500k thresholds.  A resting order has no
    predictive value after its observation TTL and is exponentially decayed
    before then.  CVD and tick imbalance are optional; missing fields never add
    points.
    """
    now_seconds = time.time() if now_seconds is None else float(now_seconds)
    price = max(_num(price), EPS)
    liqs = data.get("liquidations", {}) or {}
    bands = liqs.get("bands", []) or []
    
    stops = data.get("stops", {}) or {}
    stop_bands = stops.get("bands", []) or []
    bands.extend(stop_bands)

    below = above = 0.0
    for band in bands:
        if not isinstance(band, Mapping):
            continue
        level = _num(band.get("mid_px", band.get("price", 0.0)))
        amount = abs(_num(band.get("amount_usd", band.get("amount", 0.0))))
        if level <= 0.0 or amount <= 0.0:
            continue
        distance = abs((level - price) / price * 100.0)
        if distance > max_distance_pct:
            continue
        # Nearest bands carry more usable information than the tail of a heatmap.
        distance_weight = max(0.0, 1.0 - distance / max(max_distance_pct, EPS))
        if level < price:
            below += amount * distance_weight
        elif level > price:
            above += amount * distance_weight

    l2 = data.get("l2_book", {}) or {}
    bid_volume, ask_volume = _level_volumes(l2)
    l2_imbalance = _bounded_imbalance(bid_volume, ask_volume)

    flow = _trade_flow(data.get("recent_trades", []) or [], whale_min_usd=50_000.0)
    cvd_direction, cvd_divergence, cvd_available = _cvd_metrics(data, flow, price)

    l3_bid = l3_ask = 0.0
    l3_bid_count = l3_ask_count = 0
    for order in data.get("l3_orders", []) or []:
        if not isinstance(order, Mapping):
            continue
        level = _num(order.get("price", 0.0))
        notional = abs(_num(order.get("notional_usd", 0.0)))
        if level <= 0.0 or notional < whale_min_usd:
            continue
        distance = abs(_num(order.get("dist_pct", (level - price) / price * 100.0)))
        if distance > l3_distance_pct:
            continue
        age = _observation_age_seconds(order, now_seconds)
        if age is not None and age > l3_ttl_seconds:
            continue
        decay = math.exp(-age / max(l3_tau_seconds, EPS)) if age is not None else 1.0
        distance_weight = max(0.0, 1.0 - distance / max(l3_distance_pct, EPS))
        contribution = notional * decay * distance_weight
        side = str(order.get("side", "")).upper()
        if side in {"BUY", "BID"}:
            l3_bid += contribution
            l3_bid_count += 1
        elif side in {"SELL", "ASK"}:
            l3_ask += contribution
            l3_ask_count += 1

    features = {
        "l2_imbalance": float(l2_imbalance),
        "tick_imbalance": float(flow["tick_imbalance"]),
        "whale_imbalance": float(flow["whale_imbalance"]),
        "cvd_direction": float(cvd_direction),
        "cvd_divergence": float(cvd_divergence),
        "cvd_available": bool(cvd_available),
        "below_liq_usd_weighted": float(below),
        "above_liq_usd_weighted": float(above),
        "below_liq_strength": _sigmoid_strength(below, liq_scale_usd),
        "above_liq_strength": _sigmoid_strength(above, liq_scale_usd),
        "l3_bid_strength": _sigmoid_strength(l3_bid, whale_min_usd),
        "l3_ask_strength": _sigmoid_strength(l3_ask, whale_min_usd),
        "l3_bid_count": l3_bid_count,
        "l3_ask_count": l3_ask_count,
        "book_observation": bool(bid_volume > 0.0 or ask_volume > 0.0),
        "tape_observation": bool(flow["buy_notional"] > 0.0 or flow["sell_notional"] > 0.0),
    }

    # Continuous six-factor score.  This is a transparent prior, not a claim
    # that the weights are optimal; fit them with logistic regression out of sample.
    weights = {
        "liq": 1.00,
        "l2": 0.90,
        "l3": 0.90,
        "whale": 0.85,
        "tick": 0.65,
        "cvd": 0.70,
    }
    total_weight = sum(weights.values())
    long_evidence = (
        weights["liq"] * features["below_liq_strength"]
        + weights["l2"] * max(l2_imbalance, 0.0)
        + weights["l3"] * features["l3_bid_strength"]
        + weights["whale"] * max(flow["whale_imbalance"], 0.0)
        + weights["tick"] * max(flow["tick_imbalance"], 0.0)
        + weights["cvd"] * max(cvd_divergence, 0.0)
    )
    short_evidence = (
        weights["liq"] * features["above_liq_strength"]
        + weights["l2"] * max(-l2_imbalance, 0.0)
        + weights["l3"] * features["l3_ask_strength"]
        + weights["whale"] * max(-flow["whale_imbalance"], 0.0)
        + weights["tick"] * max(-flow["tick_imbalance"], 0.0)
        + weights["cvd"] * max(-cvd_divergence, 0.0)
    )
    features["long_score"] = round(float(6.0 * long_evidence / total_weight), 3)
    features["short_score"] = round(float(6.0 * short_evidence / total_weight), 3)
    features["direction"] = (
        "LONG" if features["long_score"] >= 3.0 and features["long_score"] > features["short_score"] + 0.25
        else "SHORT" if features["short_score"] >= 3.0 and features["short_score"] > features["long_score"] + 0.25
        else "NONE"
    )
    return features


def front_run_offset(
    *,
    price: float,
    atr: float,
    point: float,
    spread_points: float = 0.0,
    atr_fraction: float = 0.025,
    min_ticks: int = 2,
    max_atr_fraction: float = 0.10,
) -> float:
    """Return a scale-aware TP front-run distance in price units.

    The offset is the greater of a broker-valid tick distance, a small spread
    allowance, and a fraction of ATR, capped so it cannot consume the entire
    expected move.  A fixed $0.10 is therefore never used across instruments.
    """
    point = max(abs(_num(point)), EPS)
    atr = max(abs(_num(atr)), 0.0)
    tick_offset = max(1, int(min_ticks)) * point
    spread_offset = max(0.0, _num(spread_points)) * point * 0.25
    atr_offset = atr * max(0.0, atr_fraction)
    raw = max(tick_offset, spread_offset, atr_offset)
    if atr > 0.0:
        raw = min(raw, atr * max(max_atr_fraction, atr_fraction))
    return round(max(raw, tick_offset), 12)


def _bar_value(bar: Mapping[str, Any], key: str) -> float:
    return _num(bar.get(key, bar.get(key[0].upper() + key[1:], 0.0)))


def classify_market_regime(bars: Sequence[Mapping[str, Any]], lookback: int = 20) -> Dict[str, Any]:
    """Classify chop, trend, momentum, or volatility shock using OHLC only.

    Parkinson and Garman-Klass volatility are range estimators.  Kaufman's
    efficiency ratio separates directional movement from back-and-forth noise.
    All calculations use completed bars supplied by the caller; no future bar
    is accessed.
    """
    if not bars or len(bars) < max(lookback + 1, 8):
        return {"regime": "UNKNOWN", "available": False, "reason": "insufficient_completed_bars", "allow": True}
    clean = []
    for bar in bars:
        o, h, low, c = (_bar_value(bar, k) for k in ("open", "high", "low", "close"))
        if min(o, h, low, c) <= 0.0 or h < low:
            continue
        clean.append((o, h, low, c))
    if len(clean) < max(lookback + 1, 8):
        return {"regime": "UNKNOWN", "available": False, "reason": "invalid_ohlc", "allow": True}

    arr = np.asarray(clean, dtype=float)
    o, h, low, c = arr.T
    log_hl = np.log(np.maximum(h, EPS) / np.maximum(low, EPS))
    log_co = np.log(np.maximum(c, EPS) / np.maximum(o, EPS))
    gk = 0.5 * log_hl ** 2 - (2.0 * math.log(2.0) - 1.0) * log_co ** 2
    gk = np.maximum(gk, 0.0)
    park = log_hl ** 2 / (4.0 * math.log(2.0))

    n = min(lookback, len(c) - 1)
    current_vol = math.sqrt(max(float(np.mean(gk[-n:])), 0.0))
    baseline_window = min(max(4 * n, 32), len(gk))
    baseline_vol = float(np.median(np.sqrt(np.maximum(gk[-baseline_window:], 0.0))))
    baseline_vol = max(baseline_vol, EPS)
    vol_ratio = current_vol / baseline_vol

    net_move = abs(c[-1] - c[-1 - n])
    path = float(np.sum(np.abs(np.diff(c[-1 - n:]))) + EPS)
    efficiency_ratio = min(1.0, net_move / path)
    slope = (c[-1] - c[-1 - n]) / max(float(np.mean(c[-1 - n:])), EPS)
    park_vol = math.sqrt(max(float(np.mean(park[-n:])), 0.0))

    if vol_ratio >= 2.25:
        regime = "SHOCK"
    elif efficiency_ratio >= 0.45 and vol_ratio >= 1.10:
        regime = "MOMENTUM"
    elif efficiency_ratio < 0.25 and vol_ratio < 1.50:
        regime = "CHOP"
    elif efficiency_ratio >= 0.40:
        regime = "TREND"
    else:
        regime = "RANGE"
    return {
        "regime": regime,
        "available": True,
        "parkinson_vol": park_vol,
        "garman_klass_vol": current_vol,
        "vol_ratio": vol_ratio,
        "efficiency_ratio": efficiency_ratio,
        "slope": slope,
        "allow": True,
    }


def regime_allows(regime: Mapping[str, Any], setup_kind: str, direction: str) -> Tuple[bool, str]:
    """Apply the two requested regime vetoes, leaving the policy explicit."""
    name = str(regime.get("regime", "UNKNOWN")).upper()
    setup = str(setup_kind).upper()
    if name == "UNKNOWN":
        return True, "regime_unknown_no_veto"
    if setup == "BREAKOUT" and name in {"CHOP", "RANGE"}:
        return False, f"breakout_veto_{name.lower()}"
    if setup in {"MEAN_REVERSION", "LIQUIDATION_FADE", "ORDERFLOW_FADE"} and name in {"MOMENTUM", "SHOCK", "TREND"}:
        return False, f"mean_reversion_veto_{name.lower()}"
    return True, "regime_permitted"


@dataclass
class PortfolioBetaRisk:
    """Rolling BTC-factor risk model using completed 15-minute observations."""
    lookback: int = 96
    min_observations: int = 24
    histories: Dict[str, Deque[Tuple[float, float]]] = None

    def __post_init__(self) -> None:
        if self.histories is None:
            self.histories = defaultdict(lambda: deque(maxlen=self.lookback + 1))

    def update(self, asset: str, price: float, timestamp: Optional[float] = None) -> None:
        price = _num(price)
        if price <= 0.0:
            return
        self.histories[asset.upper()].append((time.time() if timestamp is None else float(timestamp), price))

    def beta(self, asset: str, benchmark: str = "BTC") -> float:
        asset = asset.upper()
        benchmark = benchmark.upper()
        if asset == benchmark:
            return 1.0
        a = {round(t, 3): p for t, p in self.histories.get(asset, [])}
        b = {round(t, 3): p for t, p in self.histories.get(benchmark, [])}
        common = sorted(set(a).intersection(b))
        if len(common) < self.min_observations + 1:
            # Conservative crypto fallback until there is enough aligned history.
            return 1.0
        ar = np.diff(np.log(np.asarray([a[t] for t in common], dtype=float)))
        br = np.diff(np.log(np.asarray([b[t] for t in common], dtype=float)))
        variance = float(np.var(br, ddof=1)) if len(br) > 1 else 0.0
        if variance <= EPS:
            return 1.0
        value = float(np.cov(ar, br, ddof=1)[0, 1] / variance)
        return float(np.clip(value, -3.0, 3.0))

    @staticmethod
    def _position_risk(position: Mapping[str, Any], contract_size: float = 1.0) -> float:
        explicit = _num(position.get("risk_usd", 0.0))
        if explicit > 0.0:
            return explicit
        entry = _num(position.get("price_open", position.get("entry", 0.0)))
        stop = _num(position.get("sl", position.get("stop_loss", 0.0)))
        volume = _num(position.get("volume", position.get("units", 0.0)))
        if entry > 0.0 and stop > 0.0 and volume > 0.0:
            return abs(entry - stop) * volume * max(contract_size, 1.0)
        return 0.0

    def exposures(self, positions: Iterable[Mapping[str, Any]], contract_sizes: Optional[Mapping[str, float]] = None) -> Dict[str, float]:
        net = gross = 0.0
        for position in positions:
            symbol = str(position.get("coin", position.get("symbol", "BTC"))).upper()
            asset = symbol.split("USD")[0].split("USDT")[0]
            direction = 1.0 if str(position.get("direction", "LONG")).upper() in {"LONG", "BUY"} else -1.0
            cs = _num((contract_sizes or {}).get(position.get("symbol", ""), 1.0), 1.0)
            risk = self._position_risk(position, cs)
            factor_risk = risk * self.beta(asset)
            net += direction * factor_risk
            gross += abs(factor_risk)
        return {"net_beta_risk_usd": net, "gross_beta_risk_usd": gross}

    def check_candidate(
        self,
        positions: Iterable[Mapping[str, Any]],
        *,
        asset: str,
        direction: str,
        risk_usd: float,
        equity_usd: float,
        max_net_fraction: float = 0.025,
        max_gross_fraction: float = 0.05,
        contract_sizes: Optional[Mapping[str, float]] = None,
    ) -> Dict[str, Any]:
        current = self.exposures(positions, contract_sizes)
        sign = 1.0 if direction.upper() in {"LONG", "BUY"} else -1.0
        candidate = sign * _num(risk_usd) * self.beta(asset)
        projected_net = current["net_beta_risk_usd"] + candidate
        projected_gross = current["gross_beta_risk_usd"] + abs(candidate)
        equity = max(_num(equity_usd), EPS)
        net_limit = equity * max_net_fraction
        gross_limit = equity * max_gross_fraction
        allowed = abs(projected_net) <= net_limit and projected_gross <= gross_limit
        return {
            "allowed": bool(allowed),
            "asset_beta": self.beta(asset),
            "candidate_beta_risk_usd": candidate,
            "current_net_beta_risk_usd": current["net_beta_risk_usd"],
            "projected_net_beta_risk_usd": projected_net,
            "projected_gross_beta_risk_usd": projected_gross,
            "net_limit_usd": net_limit,
            "gross_limit_usd": gross_limit,
            "reason": "beta_budget_ok" if allowed else "beta_budget_veto",
        }

    @staticmethod
    def beta_neutral_notional(reference_notional: float, reference_beta: float, hedge_beta: float) -> float:
        """Notional of a hedge asset that offsets a reference BTC-factor beta."""
        if abs(hedge_beta) <= EPS:
            return 0.0
        return abs(_num(reference_notional) * _num(reference_beta) / hedge_beta)
