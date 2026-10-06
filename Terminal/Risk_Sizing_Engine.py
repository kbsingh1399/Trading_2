"""Causal orderflow features, cost-inclusive risk and signed-notional covariance.

Covariance units are decimal log-return squared over the manifest's horizon.
Risk is planned stop loss PLUS round-trip costs, never a notional allocation.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from decimal import Decimal, ROUND_FLOOR
from pathlib import Path
import hashlib
import json
import math
import time
import numpy as np
from Terminal.Asset_Universe import canonical_asset

def number(value, default=0.0):
    try:
        value = float(value)
        return value if math.isfinite(value) else default
    except (TypeError, ValueError):
        return default

def epoch(value):
    if isinstance(value, str) and not value.replace(".", "", 1).isdigit():
        from datetime import datetime, timezone
        try:
            parsed = datetime.fromisoformat(value.replace(" UTC", "+00:00").replace("Z", "+00:00"))
            return parsed.replace(tzinfo=timezone.utc).timestamp() if parsed.tzinfo is None else parsed.timestamp()
        except ValueError: return 0.0
    value = number(value)
    return value / 1000 if value > 1e11 else value

@dataclass(frozen=True)
class RiskPolicy:
    initial_capital: float = 5000.0
    drawdown_fraction: float = 0.045
    min_risk: float = 10.0
    max_risk: float = 45.0
    max_positions: int = 2
    minimum_friction_bps: float = 41.0
    commission_bps: float = 0.0
    slippage_bps: float = 2.0
    sigma_budget_usd: float = 45.0
    covariance_horizon_minutes: int = 15
    volatility_lookback: int = 96
    min_confluence: float = 0.35
    max_book_age: float = 10.0
    max_basis_sigma: float = 1.0
    max_future_skew_sec: float = 0.0

    def __post_init__(self):
        if not (10 <= self.min_risk <= self.max_risk <= 45):
            raise ValueError("Risk must stay inside 10 to 45 USD")
        if self.initial_capital != 5000 or self.drawdown_fraction != 0.045 or self.max_positions != 2:
            raise ValueError("OMNI capital, drawdown and position invariants are fixed")
        if self.minimum_friction_bps < 41 or self.sigma_budget_usd <= 0:
            raise ValueError("Invalid friction/variance budget")

def floor_volume(volume, step, minimum, maximum):
    if step <= 0 or minimum <= 0 or maximum < minimum: return 0.0
    capped = Decimal(str(min(volume, maximum)))
    unit = Decimal(str(step))
    result = (capped / unit).to_integral_value(rounding=ROUND_FLOOR) * unit
    return float(result) if float(result) >= minimum else 0.0

def completed_statistics(bars, as_of, lookback=96, horizon_minutes=15):
    """MT5 bar timestamps are opens. Exclude any bar not closed at decision time."""
    ordered = sorted((b for b in bars if epoch(b.get("time")) + 900 <= as_of), key=lambda b: epoch(b["time"]))
    ordered = ordered[-lookback-1:]
    if len(ordered) < 25: raise ValueError("volatility_history_insufficient")
    closes = np.array([number(b.get("close")) for b in ordered])
    if np.any(closes <= 0): raise ValueError("invalid_bar_price")
    times = np.array([epoch(b["time"]) for b in ordered])
    if as_of-times[-1]-900 > 900: raise ValueError("completed_bars_stale")
    returns = np.diff(np.log(closes))
    # Session gaps are not treated as one ordinary 15-minute observation.
    returns = returns[np.diff(times) == 900]
    if len(returns) < 24: raise ValueError("continuous_return_history_insufficient")
    sigma = float(np.std(returns, ddof=1)) * math.sqrt(horizon_minutes / 15)
    if not math.isfinite(sigma) or sigma <= 1e-8: raise ValueError("volatility_unavailable")
    tr = [max(number(b["high"])-number(b["low"]), abs(number(b["high"])-closes[i-1]),
              abs(number(b["low"])-closes[i-1])) for i, b in enumerate(ordered[1:], 1)]
    atr = float(np.mean(tr[-14:]))
    movement = float(np.sum(np.abs(np.diff(closes[-21:]))))
    er = abs(float(closes[-1]-closes[-21])) / movement if movement else 0.0
    return {"sigma_h": sigma, "atr": atr, "efficiency_ratio": er,
            "last_bar_close": float(times[-1]+900), "bar_count": len(ordered)}

class RobustNormalizer:
    def __init__(self, history=None, window=256):
        self.history = {k: deque(v[-window:], maxlen=window) for k, v in (history or {}).items()}
        self.window = window

    def score_then_observe(self, key, value):
        past = self.history.setdefault(key, deque(maxlen=self.window))
        z = None
        if len(past) >= 24:
            values = np.array(past)
            median = float(np.median(values))
            scale = max(1.4826 * float(np.median(np.abs(values-median))), 0.05)
            z = float(np.clip((value-median)/scale, -3, 3))
        past.append(float(value))
        return z

    def export(self): return {k: list(v) for k, v in self.history.items()}

class OrderflowModel:
    def __init__(self, policy=None, history=None, walls=None):
        self.policy = policy or RiskPolicy()
        self.normalizer = RobustNormalizer(history)
        self.walls = walls or {}

    def observe_walls(self, asset, payload, as_of):
        sources = payload.get("sources") or {}
        wall_asof = epoch(sources.get("l3", {}).get("observed_at") or payload.get("timestamp"))
        if not wall_asof or not 0.0 <= as_of-wall_asof <= 30: return False
        previous = self.walls.get(asset, {})
        if previous and wall_asof < max(v["last"] for v in previous.values()): return False
        current = {}
        for w in payload.get("l3_orders", []):
            px, usd, side = number(w.get("price")), number(w.get("notional_usd")), w.get("side")
            if px <= 0 or usd <= 0 or side not in ("BUY", "SELL"): continue
            key = str(w.get("order_id") or f"{w.get('address')}:{side}:{px}")
            old = previous.get(key, {})
            first = number(old.get("first"), wall_asof) if wall_asof-number(old.get("last"), wall_asof) <= 30 else wall_asof
            current[key] = {"first": first, "last": wall_asof}
            span = max(number(w.get("observed_span_s") or w.get("persistence_sec") or 0.0), wall_asof - first)
            w["observed_span_s"] = span
            w["persistence_sec"] = span
            w["is_stale"] = False
        self.walls[asset] = current
        return True

    @staticmethod
    def _levels(rows, mid, sigma, side):
        out = []
        for row in rows[:20]:
            px = number(row.get("price", row.get("px")))
            size = number(row.get("size", row.get("sz")))
            if px <= 0 or size <= 0 or side*(mid-px) < 0: continue
            distance = abs(math.log(px/mid)) / sigma
            usd = px * size  # Hyperliquid quantities are base units, already USD quoted.
            if not math.isfinite(usd): continue
            out.append((px, usd, distance, usd*math.exp(-distance)))
        return out

    def features(self, asset, payload, bars, macro, as_of):
        stats = completed_statistics(bars, as_of, self.policy.volatility_lookback,
                                     self.policy.covariance_horizon_minutes)
        book = payload.get("l2_book") or {}
        observed = epoch(book.get("timestamp"))
        received = number(book.get("received_at"))
        check_time = received if received > 0 else observed
        skew_limit = self.policy.max_future_skew_sec
        if not check_time or not -skew_limit <= as_of-check_time <= self.policy.max_book_age:
            raise ValueError("book_stale_or_future")
        if observed and observed - as_of > max(30.0, skew_limit):
            raise ValueError("book_stale_or_future")
        bid, ask = number(book.get("best_bid")), number(book.get("best_ask"))
        if not (0 < bid < ask): raise ValueError("book_crossed_or_missing")
        mid, sigma = (bid+ask)/2, stats["sigma_h"]
        bids, asks = self._levels(book.get("bids", []), mid, sigma, 1), self._levels(book.get("asks", []), mid, sigma, -1)
        if not bids or not asks: raise ValueError("depth_missing")
        b, a = sum(x[3] for x in bids), sum(x[3] for x in asks)
        if not math.isfinite(b+a) or b+a <= 0: raise ValueError("weighted_depth_invalid")
        imbalance = (b-a)/(b+a)
        z = self.normalizer.score_then_observe(asset, imbalance)
        anomaly = math.tanh(z/2) if z is not None else 0.0
        l2 = float(np.clip(0.8*imbalance+0.2*anomaly, -1, 1))
        sources = payload.get("sources") or {}
        wall_asof = epoch(sources.get("l3", {}).get("observed_at") or payload.get("timestamp"))
        fresh_walls = self.observe_walls(asset, payload, as_of)
        wall_totals = {"BUY": 0.0, "SELL": 0.0}
        tracked = self.walls.get(asset, {})
        if fresh_walls:
            for w in payload.get("l3_orders", []):
                px, usd, side = number(w.get("price")), number(w.get("notional_usd")), w.get("side")
                if px <= 0 or usd <= 0 or side not in wall_totals: continue
                key = str(w.get("order_id") or f"{w.get('address')}:{side}:{px}")
                first = number(tracked.get(key, {}).get("first"))
                if not first or wall_asof <= first: continue
                persistence = min(1.0, max(0.0, (wall_asof-first)/60))
                distance = abs(math.log(px/mid)) / max(sigma * 3.0, 0.01)
                wall_totals[side] += usd*math.exp(-distance)*persistence
        wall_sum = sum(wall_totals.values())
        wall_imb = (wall_totals["BUY"]-wall_totals["SELL"])/wall_sum if wall_sum else 0.0
        buy = sell = 0.0
        seen = set()
        for t in payload.get("recent_trades", []):
            ts = epoch(t.get("time"))
            uid = str(t.get("trade_id") or t.get("tid") or (ts, t.get("price"), t.get("size"), t.get("side")))
            if uid in seen or not 0.0 <= as_of-ts <= 60: continue
            seen.add(uid)
            usd = number(t.get("notional_usd")) * math.exp(-(as_of-ts)/30)
            if t.get("side") == "BUY": buy += usd
            elif t.get("side") == "SELL": sell += usd
        tape = (buy-sell)/(buy+sell) if buy+sell else 0.0
        # Deterministic robust z-scores for the aggressor tape (CVD) and wall
        # imbalance. These are the ground-truth values the cognitive engine is
        # attested against; it can never substitute its own statistics.
        z_tape = self.normalizer.score_then_observe(asset+":aggressor", tape)
        z_wall = self.normalizer.score_then_observe(asset+":walls", wall_imb)
        # Match each cluster corridor against visible depth in that exact corridor.
        # Do not infer stop/liquidation exposure from historical realized prints.
        pressure = {"LONG": 0.0, "SHORT": 0.0}
        corridor_records = []
        for name in ("liquidations", "stops"):
            observed_name = "projected_liquidations" if name == "liquidations" else "observed_stops"
            sampled_data = payload.get(observed_name) or {}
            data = sampled_data if sampled_data.get("kind") in ("PROJECTED_EXPOSURE", "OBSERVED_STOP_ORDERS") else payload.get(name) or {}
            if data.get("kind") not in ("PROJECTED_EXPOSURE", "OBSERVED_STOP_ORDERS"): continue
            component_asof = epoch(sources.get("wallet_risk" if data is sampled_data else name, {}).get("observed_at") or payload.get("timestamp"))
            if not component_asof or not 0.0 <= as_of-component_asof <= 60: continue
            for band in data.get("projected_bands", data.get("bands", [])):
                low, high = number(band.get("min_px")), number(band.get("max_px"))
                amt_raw = number(band.get("amount_usd") or band.get("amount"))
                amount = amt_raw * ((low+high)/2) if amt_raw < 1e5 and not band.get("amount_usd") else amt_raw
                if not 0 < low <= high or amount <= 0: continue
                side = band.get("position_side_at_risk")
                if side is None:
                    b_type = str(band.get("type", "")).upper()
                    if "LONG" in b_type: side = "LONG"
                    elif "SHORT" in b_type: side = "SHORT"
                    elif name == "stops": side = "LONG" if high < mid else "SHORT" if low > mid else None
                if side not in pressure: continue
                rows = bids if side == "LONG" else asks
                if rows:
                    min_book_px, max_book_px = min(x[0] for x in rows), max(x[0] for x in rows)
                    corridor_low = max(low, min_book_px)
                    corridor_high = min(high, max_book_px)
                    if corridor_low <= corridor_high and high > low:
                        corridor_overlap = (corridor_high - corridor_low) / (high - low)
                        effective_amount = amount * corridor_overlap
                        depth = sum(x[1] for x in rows if corridor_low <= x[0] <= corridor_high)
                        ratio = effective_amount / depth if depth > 0 else None
                    else:
                        depth, ratio = 0.0, None
                else:
                    depth, ratio = 0.0, None
                corridor_records.append({"kind": name, "side": side, "low": low, "high": high,
                                         "depth_usd": depth, "exposure_usd": amount, "ratio": ratio})
                if ratio is not None:
                    pressure[side] += math.log1p(min(ratio, 100.0))*math.exp(-abs(math.log((low+high)/2/mid))/sigma)
        total_pressure = sum(pressure.values())
        liq_delta = (pressure["SHORT"]-pressure["LONG"])/total_pressure if total_pressure else 0.0
        macro_value = number(macro.get("asset_scores", {}).get(asset), 0.0) if macro.get("sentiment_valid") else 0.0
        quality = (0.55 + 0.15*bool(buy+sell) + 0.10*fresh_walls +
                   0.10*bool(total_pressure) + 0.10*bool(macro.get("sentiment_valid")))
        signed = 0.25*l2 + 0.15*macro_value + 0.20*wall_imb + 0.15*tape + 0.10*liq_delta
        direction = 1 if signed > 0 else -1
        B, M, W, T, L = [direction*x for x in (l2, macro_value, wall_imb, tape, liq_delta)]
        target_fuel = pressure["SHORT"] if direction == 1 else pressure["LONG"]
        opposing_magnet = pressure["LONG"] if direction == 1 else pressure["SHORT"]
        liquidity_vacuum = bool(opposing_magnet > 1e-5 and target_fuel <= 0.0)
        active_weight = 0.25 + (0.15 if abs(macro_value) > 0.001 else 0.0) + 0.20 + 0.15 + 0.10 + (0.15 if abs(macro_value) > 0.001 else 0.0)
        raw_confluence = 0.25*B + 0.15*M + 0.20*W + 0.15*T + 0.10*L + 0.15*math.sqrt(max(B, 0)*max(M, 0))
        confluence = 0.0 if liquidity_vacuum else float(np.clip(raw_confluence / active_weight, 0, 1))
        target_corridors = [c for c in corridor_records if (direction == 1 and c["side"] == "SHORT" and c["high"] >= mid) or
                            (direction == -1 and c["side"] == "LONG" and c["low"] <= mid)]
        opposing_corridors = [c for c in corridor_records if (direction == 1 and c["side"] == "LONG" and c["low"] <= mid) or
                              (direction == -1 and c["side"] == "SHORT" and c["high"] >= mid)]
        target_fuel_usd = sum(c["exposure_usd"] for c in target_corridors)
        opposing_levels = asks if direction == 1 else bids
        if target_corridors:
            target_friction_usd = sum(usd for px, usd, dist, w_usd in opposing_levels
                                      if any(c["low"] <= px <= c["high"] for c in target_corridors))
        else:
            target_friction_usd = 0.0
        coverage_missing = bool(target_fuel_usd > 0 and target_friction_usd <= 0.0)
        if target_friction_usd > 0:
            ffr = float(target_fuel_usd / target_friction_usd)
        elif coverage_missing:
            ffr = None
        else:
            ffr = 1.0
        # Friction-adjusted fuel ratio (FAFR): fuel exposure measured against
        # corridor depth PLUS the round-trip friction carried by a
        # minimum-risk reference position (stop = 1.5*ATR, risk = min_risk).
        # Deterministic from already-computed quantities; None when undefined.
        stop_ref = 1.5*stats["atr"]
        friction_ref_usd = (mid/stop_ref)*self.policy.min_risk*(self.policy.minimum_friction_bps/10000.0) if stop_ref > 0 else 0.0
        fafr_denominator = target_friction_usd + friction_ref_usd
        friction_adjusted_fuel_ratio = float(target_fuel_usd/fafr_denominator) if fafr_denominator > 0 else None
        return {**stats, "asset": asset, "as_of": as_of, "signal_mid": mid, "book_as_of": observed,
                "direction": "LONG" if direction == 1 else "SHORT", "l2_imbalance": imbalance,
                "l2_signal": l2, "l2_robust_z": z, "wall_imbalance": wall_imb,
                "wall_imbalance_robust_z": z_wall,
                "aggressor_imbalance": tape, "aggressor_robust_z": z_tape,
                "liquidation_delta": liq_delta, "macro_score": macro_value,
                "confluence": confluence, "quality": quality, "corridors": corridor_records,
                "liquidity_vacuum": liquidity_vacuum, "target_fuel": target_fuel, "opposing_magnet": opposing_magnet,
                "ffr": ffr, "friction_adjusted_fuel_ratio": friction_adjusted_fuel_ratio,
                "coverage_missing": coverage_missing, "unobserved_corridor": coverage_missing,
                "fresh_walls": fresh_walls,
                "friction_bps": self.policy.minimum_friction_bps,
                "target_fuel_usd": target_fuel_usd, "target_friction_usd": target_friction_usd,
                "risk_intent_usd": self.policy.min_risk + (self.policy.max_risk-self.policy.min_risk)*(quality*confluence)**2}

class CovarianceGate:
    def __init__(self, assets, matrix, metadata=None):
        self.assets = [canonical_asset(a) for a in assets]
        self.matrix = np.asarray(matrix, dtype=float)
        self.metadata = metadata or {}
        n = len(self.assets)
        if len(set(self.assets)) != n or self.matrix.shape != (n, n) or not np.isfinite(self.matrix).all():
            raise ValueError("invalid_covariance_labels_or_shape")
        if not np.allclose(self.matrix, self.matrix.T, rtol=1e-5, atol=1e-12): raise ValueError("asymmetric_covariance")
        if np.min(np.linalg.eigvalsh(self.matrix)) < -1e-12 or np.any(np.diag(self.matrix) <= 0):
            raise ValueError("covariance_not_positive_semidefinite")
        self.index = {a: i for i, a in enumerate(self.assets)}

    @classmethod
    def load(cls, path):
        import polars as pl
        path = Path(path)
        metadata = json.loads(path.with_suffix(".json").read_text(encoding="utf-8"))
        if metadata.get("sha256") != hashlib.sha256(path.read_bytes()).hexdigest(): raise ValueError("covariance_checksum_mismatch")
        df = pl.read_parquet(path)
        label = metadata.get("label_column", "asset")
        assets = df[label].to_list()
        return cls(assets, df.select(assets).to_numpy(), metadata)

    def validate_time(self, as_of, horizon_minutes=15):
        meta = self.metadata
        if meta.get("return_units") != "decimal_log_return" or meta.get("horizon_minutes") != horizon_minutes:
            raise ValueError("covariance_units_or_horizon_unknown")
        data_end = epoch(meta.get("data_end"))
        if epoch(meta.get("created_at")) > as_of: raise ValueError("covariance_future_vintage")
        max_age = min(number(meta.get("max_age_seconds"), 86400.0), 86400.0)
        if not data_end or data_end > as_of or as_of-data_end > max_age:
            raise ValueError("covariance_stale_or_future")

    def variance(self, exposures):
        vector = np.zeros(len(self.assets))
        for asset, notional in exposures.items():
            key = canonical_asset(asset)
            if key not in self.index: raise ValueError(f"covariance_asset_missing:{key}")
            vector[self.index[key]] += number(notional)
        return max(0.0, float(vector @ self.matrix @ vector))

    def scale_candidate(self, existing, asset, signed_notional, sigma_budget):
        key = canonical_asset(asset)
        if key not in self.index: raise ValueError(f"covariance_asset_missing:{key}")
        i = self.index[key]
        v = np.zeros(len(self.assets))
        for a, n in existing.items():
            if canonical_asset(a) not in self.index: raise ValueError(f"covariance_asset_missing:{a}")
            v[self.index[canonical_asset(a)]] += n
        before = float(v @ self.matrix @ v)
        A = signed_notional**2*self.matrix[i, i]
        B = 2*signed_notional*float(self.matrix[i] @ v)
        C = before-sigma_budget**2
        after = before+A+B
        if after <= sigma_budget**2: scale = 1.0
        else:
            disc = B*B-4*A*C
            upper = (-B+math.sqrt(disc))/(2*A) if A > 0 and disc >= 0 else 0.0
            scale = max(0.0, min(1.0, upper))
            if before+A*scale**2+B*scale > sigma_budget**2+1e-8: scale = 0.0
        return {"scale": scale, "variance_before": before, "variance_after": before+A*scale**2+B*scale,
                "incremental_variance": A*scale**2+B*scale, "sigma_budget_usd": sigma_budget}

    def correlation(self, a, b):
        i, j = self.index[canonical_asset(a)], self.index[canonical_asset(b)]
        return float(self.matrix[i, j]/math.sqrt(self.matrix[i, i]*self.matrix[j, j]))

def fit_covariance(bars_by_asset, as_of, path, min_observations=48):
    """Fit aligned, completed 15-minute broker returns; never mix venues/horizons."""
    import polars as pl
    from sklearn.covariance import LedoitWolf
    series = {}
    for asset, bars in bars_by_asset.items():
        rows = sorted([b for b in bars if epoch(b.get("time"))+900 <= as_of], key=lambda b: epoch(b["time"]))
        values = {}
        for left, right in zip(rows, rows[1:]):
            if epoch(right["time"])-epoch(left["time"]) != 900: continue
            if number(left["close"]) <= 0 or number(right["close"]) <= 0: continue
            values[epoch(right["time"])+900] = math.log(number(right["close"])/number(left["close"]))
        if len(values) >= min_observations: series[asset] = values
    if not series: raise ValueError("covariance_history_unavailable")
    aligned = sorted(set.intersection(*(set(v) for v in series.values())))
    if len(aligned) < min_observations: raise ValueError("covariance_common_history_insufficient")
    assets = sorted(series)
    returns = np.array([[series[a][t] for a in assets] for t in aligned])
    estimator = LedoitWolf().fit(returns)
    # Guard completely constant broker histories before declaring valid coverage.
    if np.any(np.std(returns, axis=0) <= 1e-8): raise ValueError("covariance_constant_asset_history")
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    frame = pl.DataFrame({"asset": assets, **{a: estimator.covariance_[:, i] for i, a in enumerate(assets)}})
    temp = path.with_suffix(".parquet.tmp"); frame.write_parquet(temp); temp.replace(path)
    metadata = {"schema": "omni.covariance.v1", "label_column": "asset", "assets": assets,
                "return_units": "decimal_log_return", "horizon_minutes": 15, "data_start": aligned[0],
                "data_end": aligned[-1], "created_at": as_of, "max_age_seconds": 86400,
                "source": "MT5_completed_M15", "observations": len(aligned), "shrinkage": float(estimator.shrinkage_),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    path.with_suffix(".json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    return CovarianceGate(assets, estimator.covariance_, metadata)

def cost_bps(quote, policy):
    mid = (number(quote.get("bid"))+number(quote.get("ask")))/2
    if mid <= 0: raise ValueError("invalid_broker_quote")
    spread = (number(quote.get("ask"))-number(quote.get("bid")))/mid*10000
    return max(policy.minimum_friction_bps, spread+policy.commission_bps+policy.slippage_bps)

def size_trade(quote, stop_loss_per_lot, risk_budget, covariance, existing, asset, direction,
               policy, drawdown_room, free_margin, margin_per_lot):
    mid = (number(quote["bid"])+number(quote["ask"]))/2
    notional_per_lot = mid*number(quote.get("contract_size"))
    if min(notional_per_lot, stop_loss_per_lot, margin_per_lot) <= 0: raise ValueError("broker_valuation_missing")
    friction_per_lot = notional_per_lot*cost_bps(quote, policy)/10000
    loss_per_lot = stop_loss_per_lot+friction_per_lot
    budget = min(policy.max_risk, risk_budget, max(0, drawdown_room)*0.90)
    if budget < policy.min_risk: return {"accepted": False, "reason": "drawdown_or_risk_room"}
    volume = min(budget/loss_per_lot, max(0, free_margin)*0.80/margin_per_lot)
    sign = 1 if direction == "LONG" else -1
    check = covariance.scale_candidate(existing, asset, sign*volume*notional_per_lot, policy.sigma_budget_usd)
    volume = floor_volume(volume*check["scale"], number(quote["step_lot"]), number(quote["min_lot"]), number(quote["max_lot"]))
    planned = volume*loss_per_lot
    if volume <= 0 or planned < policy.min_risk: return {"accepted": False, "reason": "minimum_lot_or_variance_budget", **check}
    exposure = dict(existing); exposure[asset] = exposure.get(asset, 0)+sign*volume*notional_per_lot
    variance = covariance.variance(exposure)
    if planned > budget+1e-8 or variance > policy.sigma_budget_usd**2+1e-8: raise ValueError("sizing_invariant_failure")
    return {"accepted": True, "volume": volume, "risk_usd": planned, "stop_risk_usd": volume*stop_loss_per_lot,
            "friction_usd": volume*friction_per_lot, "friction_bps": cost_bps(quote, policy),
            "signed_notional_usd": sign*volume*notional_per_lot, **check, "variance_after": variance}
