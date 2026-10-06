"""Liquidations & stop-loss reconstruction engine (Pillar 3, Q1A/Q1B).

Replaces CoinGlass heatmaps and the Hyperdash stops tab with local math on
public data. Two honest data regimes:

  EMPIRICAL: Binance ``@forceOrder`` prints are real forced liquidations.
      They calibrate and deplete the synthetic model and build the empirical
      heatmap histogram on their own.

  SYNTHETIC: resting liquidation density is reconstructed from rolling open
      interest deltas conditioned on price intervals and leverage tiers.
      Every OI increase during a bar opens a "cohort" of notional at that
      bar's price; every decrease closes cohorts FIFO (positions unwound).
      Each cohort's liquidation ladder is the exchange formula

          P_liq(long, L)  = P_entry * (1 - 1/L + mmr)
          P_liq(short, L) = P_entry * (1 + 1/L - mmr)

      spread over leverage tiers (10x/25x/50x/100x with empirical weights).
      Density then DECAYS with an exponential hazard in (a) elapsed time and
      (b) cumulative traded volume across the band's corridor: a corridor the
      tape has already traded through has consumed whatever rested there.

Stop-loss clusters are reconstructed structurally: fractal swing highs/lows,
ATR multiples (1.0/1.5/2.0), volume-profile POC/VAH/VAL and round numbers,
weighted by recency and the volume that printed at the swing. Output bands
use the exact ``OBSERVED_STOP_ORDERS`` / ``PROJECTED_EXPOSURE`` schema that
``Risk_Sizing_Engine.OrderflowModel.features`` consumes (``min_px``, ``max_px``,
``amount_usd``, ``position_side_at_risk``), so the trader ingests them
unchanged - with an explicit ``coverage`` marker that they are synthetic.

Derived analytics:
  * Liquidation Max Pain - the price maximizing forced-liquidation notional
    cascaded from the current price (prefix-sum sweep over band mids).
  * FAFR - Friction-Adjusted Fuel Ratio: cascade fuel toward a target price
    divided by the 41 bps round-trip friction of reaching it.
"""
from __future__ import annotations
import math
from collections import deque
from Terminal.Risk_Sizing_Engine import number

DEFAULT_LEVERAGE_WEIGHTS = {10: 0.35, 25: 0.40, 50: 0.20, 100: 0.05}
DEFAULT_MMR = {10: 0.004, 25: 0.005, 50: 0.010, 100: 0.008}
BAND_BPS = 25.0                 # geometric band width for density aggregation
DEFAULT_TIME_CONSTANT_SEC = 72 * 3600.0   # 72h half-life-ish cohort aging
DEFAULT_VOLUME_REF_MULT = 3.0   # band density consumed after 3x its own notional trades through


def liq_price(entry, leverage, side, mmr):
    """Exchange liquidation formula. side: 'LONG' or 'SHORT' (the position).

    Returns None for an INVALID tier: when the maintenance margin rate
    reaches 1/L the formula inverts (the position is never margin-callable
    at a coherent price) - real exchanges cap leverage below that point, and
    so does the model rather than emitting a wrong-side level."""
    entry = float(number(entry))
    leverage = float(number(leverage))
    mmr = float(number(mmr))
    if entry <= 0 or leverage <= 1 or 1.0 / leverage <= mmr:
        return None
    if side == "LONG":
        return entry * (1.0 - 1.0 / leverage + mmr)
    if side == "SHORT":
        return entry * (1.0 + 1.0 / leverage - mmr)
    return None


def _band_index(price):
    return int(math.log(max(float(price), 1e-12)) / math.log(1.0 + BAND_BPS / 1e4))


def _band_bounds(index):
    lo = (1.0 + BAND_BPS / 1e4) ** index
    return lo, lo * (1.0 + BAND_BPS / 1e4)


class _Cohort:
    __slots__ = ("ts", "entry_px", "long_usd", "short_usd")

    def __init__(self, ts, entry_px, long_usd, short_usd):
        self.ts, self.entry_px = float(ts), float(entry_px)
        self.long_usd, self.short_usd = float(long_usd), float(short_usd)


class LiquidationReconstructionEngine:
    """Per-asset OI-cohort liquidation density + max pain + FAFR."""

    def __init__(self, *, leverage_weights=None, mmr=None, time_constant_sec=None,
                 volume_ref_mult=None, max_cohorts=2048, max_bands=512):
        weights = dict(leverage_weights or DEFAULT_LEVERAGE_WEIGHTS)
        total = sum(weights.values())
        if total <= 0:
            raise ValueError("leverage weights must sum positive")
        self.leverage_weights = {float(k): v / total for k, v in weights.items()}
        self.mmr = dict(mmr or DEFAULT_MMR)
        self.tau = float(time_constant_sec or DEFAULT_TIME_CONSTANT_SEC)
        self.volume_ref_mult = float(volume_ref_mult or DEFAULT_VOLUME_REF_MULT)
        self.max_cohorts, self.max_bands = int(max_cohorts), int(max_bands)
        self.cohorts = {}             # asset -> deque[_Cohort]
        self.empirical = {}           # asset -> {band_index: {"usd":, "count":, "ts":}}
        self.band_volume = {}         # asset -> {band_index: traded USD}
        self.last_oi = {}             # asset -> last OI USD (for delta computation)
        self.last_price = {}

    # ------------------------------------------------------------- ingestion
    def observe_oi(self, asset, *, ts, price, oi_usd, taker_buy_ratio=0.5):
        """One OI sample per bar/interval. Positive delta opens a cohort at
        ``price`` split long/short by the aggressive tape ratio; negative
        delta unwinds the oldest cohorts FIFO. OI is reported in contracts:
        pass ``oi_usd`` as position notional in USD."""
        ts, price, oi_usd = float(number(ts)), float(number(price)), float(number(oi_usd))
        if ts <= 0 or price <= 0 or oi_usd < 0:
            return None
        cohorts = self.cohorts.setdefault(asset, deque(maxlen=self.max_cohorts))
        previous = self.last_oi.get(asset)
        self.last_oi[asset], self.last_price[asset] = oi_usd, price
        if previous is None:
            return None
        delta = oi_usd - previous
        if abs(delta) < 1e-9:
            return None
        if delta > 0:
            share = min(max(float(number(taker_buy_ratio, 0.5)), 0.0), 1.0)
            cohorts.append(_Cohort(ts, price, delta * share, delta * (1.0 - share)))
        else:
            remaining = -delta
            for cohort in cohorts:
                if remaining <= 0:
                    break
                for attr in ("long_usd", "short_usd"):
                    take = min(getattr(cohort, attr), remaining)
                    setattr(cohort, attr, getattr(cohort, attr) - take)
                    remaining -= take
            while cohorts and cohorts[0].long_usd <= 1e-9 and cohorts[0].short_usd <= 1e-9:
                cohorts.popleft()
        return {"delta_usd": delta, "price": price}

    def observe_trade(self, asset, *, ts, price, notional_usd):
        """Accumulate traded volume per 25 bps band (hazard input)."""
        price = float(number(price))
        if price <= 0 or float(number(notional_usd)) <= 0:
            return None
        index = _band_index(price)
        bands = self.band_volume.setdefault(asset, {})
        bands[index] = bands.get(index, 0.0) + float(number(notional_usd))
        if len(bands) > 4096:
            for key in sorted(bands)[:len(bands) - 4096]:
                del bands[key]
        return index

    def observe_forced(self, asset, *, ts, price, notional_usd, position_side_liquidated):
        """Empirical @forceOrder print: histogram + cohort depletion."""
        price = float(number(price))
        usd = float(number(notional_usd))
        if price <= 0 or usd <= 0:
            return None
        index = _band_index(price)
        bucket = self.empirical.setdefault(asset, {}).setdefault(
            index, {"usd": 0.0, "count": 0, "ts": 0.0, "side": position_side_liquidated})
        bucket["usd"] += usd
        bucket["count"] += 1
        bucket["ts"] = max(bucket["ts"], float(number(ts)))
        bucket["side"] = position_side_liquidated
        attr = "long_usd" if position_side_liquidated == "LONG" else "short_usd"
        remaining = usd
        for cohort in self.cohorts.get(asset, deque()):
            if remaining <= 0:
                break
            take = min(getattr(cohort, attr), remaining)
            setattr(cohort, attr, getattr(cohort, attr) - take)
            remaining -= take
        return index

    # ---------------------------------------------------------- reconstruction
    def _hazard(self, asset, band_index, cohort_usd, now, cohort_ts):
        elapsed = max(0.0, float(now) - float(cohort_ts))
        time_factor = math.exp(-elapsed / self.tau)
        volumes = self.band_volume.get(asset, {})
        # Adjacent price corridors: the tape consuming the neighbourhood of a
        # level has effectively consumed the level.
        traded = sum(volumes.get(band_index + delta, 0.0) for delta in (-1, 0, 1))
        volume_factor = math.exp(-traded / max(cohort_usd * self.volume_ref_mult, 1.0))
        return time_factor * volume_factor

    def reconstruct(self, asset, *, now, current_price=None):
        """Synthetic liquidation bands (Risk_Sizing schema, PROJECTED_EXPOSURE)."""
        current_price = float(number(current_price) or self.last_price.get(asset) or 0.0)
        density = {}   # band_index -> {"LONG": usd, "SHORT": usd}
        for cohort in self.cohorts.get(asset, deque()):
            for leverage, weight in self.leverage_weights.items():
                mmr = self.mmr.get(int(leverage) if int(leverage) in self.mmr else 10, 0.004)
                for side, attr in (("LONG", "long_usd"), ("SHORT", "short_usd")):
                    notional = getattr(cohort, attr) * weight
                    if notional <= 1e-9:
                        continue
                    level = liq_price(cohort.entry_px, leverage, side, mmr)
                    if level is None or level <= 0:
                        continue
                    index = _band_index(level)
                    cell = density.setdefault(index, {"LONG": 0.0, "SHORT": 0.0})
                    cell[side] += notional * self._hazard(asset, index, notional, now, cohort.ts)
        bands, total_long, total_short, count = [], 0.0, 0.0, 0
        for index in sorted(density):
            lo, hi = _band_bounds(index)
            cell = density[index]
            for side, risk in (("LONG", cell["LONG"]), ("SHORT", cell["SHORT"])):
                if risk < 1.0:      # sub-dollar dust
                    continue
                bands.append({"min_px": lo, "max_px": hi, "mid_px": math.sqrt(lo * hi),
                              "amount": risk, "amount_usd": risk,
                              "position_side_at_risk": side,
                              "type": "LONG CASCADE" if side == "LONG" else "SHORT SQUEEZE"})
                count += 1
                if side == "LONG":
                    total_long += risk
                else:
                    total_short += risk
        return {"kind": "PROJECTED_EXPOSURE", "coverage": "SYNTHETIC_OI_DELTA_MODEL",
                "bands": bands[-self.max_bands:], "total_long_size": total_long,
                "total_short_size": total_short, "total_long_count": count,
                "total_short_count": count, "observed_at": float(now),
                "current_price": current_price}

    def empirical_bands(self, asset):
        """Recent forced-liquidation prints aggregated into bands."""
        rows = []
        for index, bucket in sorted(self.empirical.get(asset, {}).items()):
            lo, hi = _band_bounds(index)
            rows.append({"min_px": lo, "max_px": hi, "mid_px": math.sqrt(lo * hi),
                         "amount_usd": bucket["usd"], "amount": bucket["usd"],
                         "count": bucket["count"], "ts": bucket["ts"],
                         "position_side_at_risk": bucket.get("side")})
        return rows

    # ------------------------------------------------------------- analytics
    def cascade(self, asset, *, now, target_price, current_price=None):
        """USD of forced liquidations triggered by a move from current price
        to ``target_price`` (longs below, shorts above)."""
        current = float(number(current_price) or self.last_price.get(asset) or 0.0)
        target = float(number(target_price))
        if current <= 0 or target <= 0:
            return 0.0
        fuel = 0.0
        for band in self.reconstruct(asset, now=now)["bands"]:
            mid = band["mid_px"]
            if target < current and band["position_side_at_risk"] == "LONG" and target <= mid < current:
                fuel += band["amount_usd"]
            if target > current and band["position_side_at_risk"] == "SHORT" and current < mid <= target:
                fuel += band["amount_usd"]
        return fuel

    def max_pain(self, asset, *, now, current_price=None):
        """Price level maximizing cascaded forced-liquidation notional."""
        current = float(number(current_price) or self.last_price.get(asset) or 0.0)
        landscape = self.reconstruct(asset, now=now, current_price=current)
        if not landscape["bands"] or current <= 0:
            return {"price": current, "cascade_usd": 0.0, "direction": "NONE",
                    "total_long_usd": 0.0, "total_short_usd": 0.0}
        best = {"price": current, "cascade_usd": 0.0, "direction": "NONE"}
        for band in landscape["bands"]:
            mid = band["mid_px"]
            if mid < current:
                fuel = self.cascade(asset, now=now, target_price=mid, current_price=current)
                if fuel > best["cascade_usd"]:
                    best = {"price": mid, "cascade_usd": fuel, "direction": "DOWN"}
            elif mid > current:
                fuel = self.cascade(asset, now=now, target_price=mid, current_price=current)
                if fuel > best["cascade_usd"]:
                    best = {"price": mid, "cascade_usd": fuel, "direction": "UP"}
        best["total_long_usd"] = landscape["total_long_size"]
        best["total_short_usd"] = landscape["total_short_size"]
        return best

    def fafr(self, asset, *, now, target_price, notional_usd, friction_bps=41.0,
             current_price=None):
        """Friction-Adjusted Fuel Ratio at a target price.

        fuel_usd  = cascaded liquidation notional between here and the target
        friction  = round-trip friction of our own position (>= 41 bps)
        fafr      = fuel_usd / friction_usd  (>= 1 means the move pays for us)
        """
        fuel = self.cascade(asset, now=now, target_price=target_price,
                            current_price=current_price)
        friction_usd = float(number(notional_usd)) * float(number(friction_bps)) / 1e4
        if friction_usd <= 0:
            return {"fuel_usd": fuel, "friction_usd": 0.0, "fafr": None,
                    "target_price": float(number(target_price))}
        return {"fuel_usd": fuel, "friction_usd": friction_usd, "fafr": fuel / friction_usd,
                "target_price": float(number(target_price))}


# ---------------------------------------------------------------- stop model
def fractal_swings(bars, k=2):
    """Completed-bar fractal pivots: [(index, 'HIGH', price), ...]."""
    rows = [(i, b) for i, b in enumerate(bars)
            if number(b.get("high")) > 0 and number(b.get("low")) > 0]
    swings = []
    for i in range(k, len(rows) - k):
        idx, bar = rows[i]
        window = rows[i - k: i + k + 1]
        highs = [number(b.get("high")) for _, b in window]
        lows = [number(b.get("low")) for _, b in window]
        if number(bar.get("high")) == max(highs):
            swings.append((idx, "HIGH", number(bar.get("high"))))
        if number(bar.get("low")) == min(lows):
            swings.append((idx, "LOW", number(bar.get("low"))))
    return swings


class StopClusterEngine:
    """Structural stop-loss cluster reconstruction (Q1B, stops half)."""

    def __init__(self, *, atr_multiples=(1.0, 1.5, 2.0), min_band_usd=1.0,
                 recency_half_life_bars=48.0):
        self.atr_multiples = tuple(float(m) for m in atr_multiples)
        self.min_band_usd = float(min_band_usd)
        self.recency_half_life_bars = float(recency_half_life_bars)

    def reconstruct(self, bars, *, now, mid, atr, profile=None):
        """Bands of resting stop-loss clusters in the OBSERVED_STOP_ORDERS
        schema. Sell stops (longs' stops) rest BELOW mid at swing lows and
        ATR offsets; buy stops (shorts' stops) rest ABOVE at swing highs."""
        atr = float(number(atr))
        if not bars or mid <= 0 or atr <= 0:
            return {"kind": "OBSERVED_STOP_ORDERS", "coverage": "SYNTHETIC_STRUCTURAL_MODEL",
                    "bands": [], "total_sell_size": 0.0, "total_buy_size": 0.0,
                    "observed_at": float(now)}
        completed = [b for b in bars if number(b.get("time")) > 0]
        completed.sort(key=lambda b: number(b["time"]))
        latest_ts = max(number(b["time"]) for b in completed)
        span_sec = max(900.0, (latest_ts - number(completed[0]["time"])) or 900.0)
        swings = fractal_swings(completed)
        density = {}   # band_index -> {"sell": usd_weight, "buy": usd_weight}

        def add(price, usd, kind):
            # A resting stop must sit on the losing side of CURRENT price:
            # sell stops (longs) strictly below mid, buy stops (shorts) above.
            # A candidate level on the wrong side is already-triggered history.
            if price <= 0 or usd <= 0:
                return
            if kind == "sell" and price >= mid:
                return
            if kind == "buy" and price <= mid:
                return
            index = _band_index(price)
            cell = density.setdefault(index, {"sell": 0.0, "buy": 0.0})
            cell["sell" if kind == "sell" else "buy"] += usd

        # 1) Fractal swing stops, weighted by recency and local volume.
        for idx, kind, price in swings:
            bar = completed[idx]
            age_bars = (latest_ts - number(bar.get("time"))) / 900.0
            recency = 0.5 ** (age_bars / self.recency_half_life_bars)
            volume = number(bar.get("volume") or bar.get("tick_volume") or 1.0)
            weight = recency * math.log1p(max(volume, 1.0)) * 1000.0
            if kind == "LOW":
                add(price - 0.05 * atr, weight, "sell")     # longs stop just under the swing
            else:
                add(price + 0.05 * atr, weight, "buy")
            # 2) ATR-multiple offsets from the swing (measured stops).
            for mult in self.atr_multiples:
                if kind == "LOW":
                    add(price - mult * atr, weight / (1.0 + mult), "sell")
                else:
                    add(price + mult * atr, weight / (1.0 + mult), "buy")
        # 3) Volume-profile anchors: stops rest just beyond POC/VAH/VAL.
        if profile:
            for key, kind in (("val", "sell"), ("poc", "sell"), ("vah", "buy"), ("poc", "buy")):
                level = number(profile.get(key))
                if level > 0:
                    add(level - 0.10 * atr if kind == "sell" else level + 0.10 * atr,
                        0.5 * math.log1p(number(profile.get("total_volume", 1.0))) * 1000.0, kind)
        # 4) Round numbers (psychological stops) within 10% of mid.
        magnitude = 10.0 ** math.floor(math.log10(mid))
        for frac in (0.1, 0.2, 0.25, 0.5, 0.75):
            level = round(mid / (magnitude * frac)) * magnitude * frac
            if 0.9 * mid < level < 1.1 * mid:
                add(level - (0.02 if level < mid else -0.02) * atr, 250.0,
                    "sell" if level < mid else "buy")
        bands, total_sell, total_buy = [], 0.0, 0.0
        for index in sorted(density):
            lo, hi = _band_bounds(index)
            cell = density[index]
            for kind, side_label, side_at_risk in (("sell", "SELL STOPS", "LONG"),
                                                   ("buy", "BUY STOPS", "SHORT")):
                usd = cell[kind]
                if usd < self.min_band_usd:
                    continue
                bands.append({"min_px": lo, "max_px": hi, "mid_px": math.sqrt(lo * hi),
                              "amount": usd, "amount_usd": usd, "side": side_label,
                              "position_side_at_risk": side_at_risk})
                if kind == "sell":
                    total_sell += usd
                else:
                    total_buy += usd
        return {"kind": "OBSERVED_STOP_ORDERS", "coverage": "SYNTHETIC_STRUCTURAL_MODEL",
                "bands": bands, "total_sell_size": total_sell, "total_buy_size": total_buy,
                "total_sell_count": sum(1 for b in bands if b["side"] == "SELL STOPS"),
                "total_buy_count": sum(1 for b in bands if b["side"] == "BUY STOPS"),
                "observed_at": float(now), "span_sec": span_sec}
