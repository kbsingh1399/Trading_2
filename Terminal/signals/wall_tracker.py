"""Terminal/signals/wall_tracker.py
==========================================
P2 FIX — Persistent Order Book Wall Tracker.

PROBLEM:
  Snapshot-based wall detection is spoofable. A whale wall present at one
  moment may be pulled 10 seconds later (classic iceberg / spoof cycle).
  We only count walls that have persisted continuously for ≥ 120 seconds.

INTEGRATION:
  Instantiate ONE PersistentWallTracker per session (singleton via get_tracker()).
  The telemetry daemon calls tracker.update() every cycle.
  Entry gates call tracker.get_persistent_walls() to confirm anchor presence.

WALL PERSISTENCE RULE (from ACTIVE_CONTEXT.md Section 6):
  - Minimum wall size: >= 150,000 USD notional
  - Minimum persistence: >= 180 seconds (3 minutes)
  - Maximum distance from price: <= 0.8% for L3 whale classification
"""
from __future__ import annotations

import logging
import time
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger("WallTracker")

# Configurable constants
DEFAULT_MIN_SIZE_USD   = 150_000.0   # Only track walls >= 150k USD
DEFAULT_MIN_AGE_SEC    = 180.0       # Wall must persist >= 3 minutes
DEFAULT_MAX_DIST_PCT   = 0.80        # Only within 0.80% of current price
DEFAULT_CLUSTER_BPS    = 10.0        # Aggregate walls within 10 bps (avoids noise from micro-moves)


class WallRecord:
    """Single level's persistence record."""
    __slots__ = ("price", "side", "first_seen", "last_seen", "max_notional")

    def __init__(self, price: float, side: str, notional: float, ts: float):
        self.price       = price
        self.side        = side          # "bid" or "ask"
        self.first_seen  = ts
        self.last_seen   = ts
        self.max_notional = notional

    def refresh(self, notional: float, ts: float) -> None:
        self.last_seen    = ts
        self.max_notional = max(self.max_notional, notional)

    def age(self, now: float) -> float:
        return now - self.first_seen

    def is_persistent(self, now: float, min_age: float) -> bool:
        """True if wall has been continuously present for >= min_age seconds."""
        return self.age(now) >= min_age

    def is_live(self, now: float, stale_threshold: float = 90.0) -> bool:
        """True if wall was seen within the last stale_threshold seconds."""
        return (now - self.last_seen) <= stale_threshold


class PersistentWallTracker:
    """Track order book walls across time, filtering spoofed/ephemeral walls.

    Usage:
        tracker = PersistentWallTracker()

        # Call on every telemetry cycle with raw bid/ask book
        tracker.update(
            symbol="BTCUSD.pi",
            bids=[[83000, 12.5], [82900, 8.2]],   # [[price, qty], ...]
            asks=[[83900, 6.1], [84000, 4.7]],
            mark_price=83420.0,
            timestamp=time.time(),
        )

        # Check for persistent bid walls (for long setups)
        walls = tracker.get_persistent_walls("BTCUSD.pi", side="bid")
    """

    def __init__(
        self,
        min_size_usd:   float = DEFAULT_MIN_SIZE_USD,
        min_age_sec:    float = DEFAULT_MIN_AGE_SEC,
        max_dist_pct:   float = DEFAULT_MAX_DIST_PCT,
        cluster_bps:    float = DEFAULT_CLUSTER_BPS,
    ):
        self.min_size_usd = min_size_usd
        self.min_age_sec  = min_age_sec
        self.max_dist_pct = max_dist_pct
        self.cluster_bps  = cluster_bps   # aggregate walls within this many bps

        # symbol -> price_rounded -> WallRecord
        self._walls: Dict[str, Dict[float, WallRecord]] = defaultdict(dict)
        self._last_mark: Dict[str, float] = {}  # symbol -> last mark_price

    def update(
        self,
        symbol:     str,
        bids:       List,
        asks:       List,
        mark_price: float,
        timestamp:  Optional[float] = None,
    ) -> None:
        """Ingest a fresh L2 book snapshot for one symbol.

        Args:
            symbol:      MT5 broker symbol.
            bids:        List of [price, quantity] or {"price":..., "qty":...} dicts.
            asks:        Same format as bids.
            mark_price:  Current mid/mark price for distance filtering.
            timestamp:   Unix epoch (defaults to time.time()).
        """
        now = timestamp or time.time()
        self._last_mark[symbol] = mark_price
        active_prices: set[float] = set()

        for side, levels in (("bid", bids), ("ask", asks)):
            for level in levels:
                price, qty = self._parse_level(level, side)
                if price <= 0 or qty <= 0:
                    continue
                notional = price * qty
                if notional < self.min_size_usd:
                    continue
                dist_pct = abs(price - mark_price) / max(mark_price, 1e-9) * 100.0
                if dist_pct > self.max_dist_pct:
                    continue
                # Cluster to nearest cluster_bps band
                cluster_key = self._cluster_price(price, mark_price)
                active_prices.add(cluster_key)
                if cluster_key in self._walls[symbol]:
                    self._walls[symbol][cluster_key].refresh(notional, now)
                else:
                    self._walls[symbol][cluster_key] = WallRecord(
                        price=cluster_key, side=side, notional=notional, ts=now
                    )

        # Expire walls not seen in this snapshot (more than 90s stale)
        stale_threshold = 90.0
        expired = [
            p for p, w in self._walls[symbol].items()
            if not w.is_live(now, stale_threshold)
        ]
        for p in expired:
            del self._walls[symbol][p]
            logger.debug("Wall expired: %s @ %.2f (stale > %ds)", symbol, p, stale_threshold)

    def get_persistent_walls(
        self,
        symbol: str,
        side:   Optional[str] = None,   # "bid" | "ask" | None (both)
        now:    Optional[float] = None,
    ) -> List[WallRecord]:
        """Return walls that have persisted for >= min_age_sec.

        Args:
            symbol: MT5 broker symbol.
            side:   Filter to "bid" (support) or "ask" (resistance). None = all.
            now:    Timestamp for age calculation (defaults to time.time()).
        """
        now = now or time.time()
        result = []
        for wall in self._walls.get(symbol, {}).values():
            if side and wall.side != side:
                continue
            if wall.is_persistent(now, self.min_age_sec) and wall.is_live(now):
                result.append(wall)
        return sorted(result, key=lambda w: w.max_notional, reverse=True)

    def has_persistent_wall(
        self,
        symbol:    str,
        side:      str,
        min_usd:   float = DEFAULT_MIN_SIZE_USD,
        min_age:   float = DEFAULT_MIN_AGE_SEC,
    ) -> bool:
        """Quick gate: True if at least one qualifying persistent wall exists."""
        now = time.time()
        for wall in self._walls.get(symbol, {}).values():
            if wall.side == side and wall.max_notional >= min_usd:
                if wall.is_persistent(now, min_age) and wall.is_live(now):
                    return True
        return False

    def summary(self, symbol: str) -> dict:
        """Return a diagnostic summary for telemetry export."""
        now = time.time()
        all_walls = list(self._walls.get(symbol, {}).values())
        persistent = self.get_persistent_walls(symbol, now=now)
        return {
            "symbol":              symbol,
            "total_walls":         len(all_walls),
            "persistent_walls":    len(persistent),
            "persistent_bid_walls": sum(1 for w in persistent if w.side == "bid"),
            "persistent_ask_walls": sum(1 for w in persistent if w.side == "ask"),
            "max_bid_notional_usd": max((w.max_notional for w in persistent if w.side == "bid"), default=0),
            "max_ask_notional_usd": max((w.max_notional for w in persistent if w.side == "ask"), default=0),
            "min_age_sec":         self.min_age_sec,
            "min_size_usd":        self.min_size_usd,
        }

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------
    def _parse_level(self, level, side: str) -> Tuple[float, float]:
        if isinstance(level, (list, tuple)) and len(level) >= 2:
            return float(level[0]), float(level[1])
        if isinstance(level, dict):
            price = float(level.get("price", level.get("p", 0.0)))
            qty   = float(level.get("qty", level.get("q", level.get("size", 0.0))))
            return price, qty
        return 0.0, 0.0

    def _cluster_price(self, price: float, mark: float) -> float:
        """Snap price to nearest cluster_bps band."""
        if mark <= 0:
            return round(price, 2)
        band_size = mark * self.cluster_bps / 10_000.0
        if band_size <= 0:
            return round(price, 2)
        return round(round(price / band_size) * band_size, 2)


# ---------------------------------------------------------------------------
# Module-level singleton
# ---------------------------------------------------------------------------
_tracker: Optional[PersistentWallTracker] = None


def get_tracker(**kwargs) -> PersistentWallTracker:
    """Return the global PersistentWallTracker, creating it once."""
    global _tracker
    if _tracker is None:
        _tracker = PersistentWallTracker(**kwargs)
    return _tracker
