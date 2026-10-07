"""Causal, exchange-agnostic microstructure helpers.

These helpers never infer the position side of an actual liquidation event from
price alone. A missing explicit side is unknown, not an observed long/short.
"""
from __future__ import annotations

import math
import threading
import time
from dataclasses import dataclass


def classify_liquidation(price: float, current_price: float, side: str | None = None) -> str:
    """Return LONG/SHORT using explicit position side when available.

    No side is inferred from location: price-relative rules are hypothetical
    positioning models, not observed exchange liquidation events.
    """
    if side:
        s = side.upper()
        if s in {"LONG", "BUY", "B"}: return "LONG"
        if s in {"SHORT", "SELL", "A"}: return "SHORT"
    return "UNKNOWN"


def safe_imbalance(positive: float, negative: float) -> float:
    total = max(0.0, positive) + max(0.0, negative)
    return (positive - negative) / total if total > 0 else 0.0


@dataclass
class TokenBucket:
    rate: float = 0.5
    capacity: float = 2.0
    def __post_init__(self):
        self.tokens = self.capacity
        self.updated = time.monotonic()
        self.lock = threading.Lock()

    def acquire(self) -> None:
        while True:
            with self.lock:
                now = time.monotonic()
                self.tokens = min(self.capacity, self.tokens + (now-self.updated)*self.rate)
                self.updated = now
                if self.tokens >= 1:
                    self.tokens -= 1
                    return
                wait = (1-self.tokens)/self.rate
            time.sleep(max(wait, 0.001))
