#!/usr/bin/env python3
"""
Terminal/Data_Factory/whale_persistence.py
==========================================
Zero-dependency multi-cycle sign persistence evaluator for institutional whale orders.
Pure Python standard library implementation ensuring hermetic execution across all runtimes.
"""
from __future__ import annotations
import time
from typing import Any, Dict, List, Optional, Tuple


def evaluate_sign_persistence(
    hist: List[Dict[str, Any]],
    now_ts: Optional[float] = None,
    min_score: float = 0.25,
    min_adjacent_gap: float = 60.0,
    max_adjacent_gap: float = 300.0,
    max_staleness: float = 300.0
) -> Tuple[bool, str]:
    """
    Evaluates multi-cycle sign persistence across physical harvests (Q3 / C190).
    Requires:
    1. At least 4 consecutive physical harvest records.
    2. Latest physical harvest must be fresh (now_ts - last_epoch <= max_staleness, default 300s).
    3. Consecutive harvests must be strictly adjacent (min_adjacent_gap <= gap <= max_adjacent_gap, 60s to 300s).
    4. Span between first and fourth harvest must be >= 540s (~9 min).
    5. All 4 scores must maintain |S| >= min_score (default 0.25) with identical sign (all >= +0.25 or all <= -0.25).
    """
    if len(hist) < 4:
        return False, f"INSUFFICIENT_HISTORY: {len(hist)} harvests (minimum 4 required)"

    last4 = hist[-4:]
    if now_ts is None:
        now_ts = time.time()

    latest_epoch = float(last4[-1].get("harvest_epoch", 0.0))
    staleness = now_ts - latest_epoch
    if staleness > max_staleness:
        return False, f"LATEST_HARVEST_STALE: {staleness:.1f}s > {max_staleness}s"

    for h_idx in range(1, len(last4)):
        cur_epoch = float(last4[h_idx].get("harvest_epoch", 0.0))
        prev_epoch = float(last4[h_idx - 1].get("harvest_epoch", 0.0))
        gap = cur_epoch - prev_epoch
        if gap < min_adjacent_gap:
            return False, f"HARVEST_GAP_TOO_SHORT: gap={gap:.1f}s < {min_adjacent_gap}s at index {h_idx}"
        if gap > max_adjacent_gap:
            return False, f"HARVEST_GAP_TOO_LARGE: gap={gap:.1f}s > {max_adjacent_gap}s at index {h_idx}"

    span = float(last4[-1].get("harvest_epoch", 0.0)) - float(last4[0].get("harvest_epoch", 0.0))
    if span < 540.0:
        return False, f"TOTAL_SPAN_TOO_SHORT: span={span:.1f}s < 540.0s"

    scores = [float(entry.get("s", 0.0)) for entry in last4]
    all_pos = all(s >= min_score for s in scores)
    all_neg = all(s <= -min_score for s in scores)

    if all_pos:
        return True, f"PERSISTENT_POSITIVE: 4 harvests span={span:.0f}s, min_s={min(scores):.3f}"
    elif all_neg:
        return True, f"PERSISTENT_NEGATIVE: 4 harvests span={span:.0f}s, max_s={max(scores):.3f}"
    else:
        return False, f"SIGN_OR_MAGNITUDE_INCONSISTENT: scores={[round(s, 3) for s in scores]}"
