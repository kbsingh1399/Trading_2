"""Deterministic, network-free orderflow replay for promotion Gate 3.

The harness replays cached Hyperdash-style snapshots only.  It never calls
Hyperdash, MT5, or the wall clock.  Every decision is keyed to an explicit
observation and decision timestamp, so quote age, stale data, and future data
can be tested reproducibly.

Snapshot contract (minimum):
    {
        "observed_at": 1_700_000_000.0,
        "decision_at": 1_700_000_005.0,  # optional; defaults to observed_at
        "price": 100.0,
        "l2_book": {...},
        "l3_orders": [...],
        "liquidations": {"bands": [...]}
    }

``timestamp`` is accepted as an alias for ``observed_at``.  Numeric timestamps
larger than 1e11 are interpreted as milliseconds.  ISO-8601 strings are also
accepted.  A missing timestamp is not silently treated as current time.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

try:
    from Terminal.Quantitative_Governance import compute_orderflow_features
except ImportError:  # pragma: no cover - supports direct script execution
    from Quantitative_Governance import compute_orderflow_features


EPS = 1e-12


def parse_replay_timestamp(value: Any) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, datetime):
        dt = value if value.tzinfo else value.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    if isinstance(value, str):
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).timestamp()
        except ValueError:
            return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(number):
        return None
    return number / 1000.0 if number > 100_000_000_000 else number


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ReplayPolicy:
    """Quote-age policy; values are intentionally explicit and versionable."""

    decay_tau_seconds: float = 10.0
    max_quote_age_seconds: float = 30.0
    fresh_age_seconds: float = 10.0
    min_price: float = 0.0


@dataclass
class ReplayRecord:
    sequence: int
    source_index: int
    observed_at: Optional[float]
    decision_at: Optional[float]
    quote_age_seconds: Optional[float]
    decay_weight: float
    state: str
    source_hash: str
    price: float
    features: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ReplayResult:
    policy: ReplayPolicy
    records: List[ReplayRecord]
    input_count: int
    input_digest: str

    @property
    def summary(self) -> Dict[str, Any]:
        counts: Dict[str, int] = {}
        directions: Dict[str, int] = {}
        for record in self.records:
            counts[record.state] = counts.get(record.state, 0) + 1
            direction = str(record.features.get("direction", "NONE"))
            directions[direction] = directions.get(direction, 0) + 1
        return {
            "input_count": self.input_count,
            "replayed_count": len(self.records),
            "state_counts": counts,
            "direction_counts": directions,
            "input_digest": self.input_digest,
            "policy": asdict(self.policy),
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "summary": self.summary,
            "records": [record.to_dict() for record in self.records],
        }


class OrderflowReplayHarness:
    """Replay cached snapshots with deterministic quote-age decay."""

    _SCALED_FIELDS = (
        "l2_imbalance", "tick_imbalance", "whale_imbalance",
        "cvd_direction", "cvd_divergence", "below_liq_strength",
        "above_liq_strength", "l3_bid_strength", "l3_ask_strength",
        "long_score", "short_score", "below_liq_usd_weighted",
        "above_liq_usd_weighted",
    )

    def __init__(self, policy: ReplayPolicy = ReplayPolicy()):
        if policy.decay_tau_seconds <= 0:
            raise ValueError("decay_tau_seconds must be positive")
        if policy.max_quote_age_seconds < 0:
            raise ValueError("max_quote_age_seconds cannot be negative")
        if policy.fresh_age_seconds < 0:
            raise ValueError("fresh_age_seconds cannot be negative")
        self.policy = policy

    def _timestamps(self, snapshot: Mapping[str, Any]) -> Tuple[Optional[float], Optional[float]]:
        observed = parse_replay_timestamp(snapshot.get("observed_at", snapshot.get("timestamp")))
        decision = parse_replay_timestamp(snapshot.get("decision_at", snapshot.get("as_of")))
        if decision is None:
            decision = observed
        return observed, decision

    def _stale_features(self, price: float, state: str, age: Optional[float], weight: float) -> Dict[str, Any]:
        return {
            "direction": "NONE",
            "long_score": 0.0,
            "short_score": 0.0,
            "quote_observation": False,
            "quote_age_seconds": age,
            "quote_decay": weight,
            "replay_state": state,
            "price": price,
        }

    def _apply_decay(self, features: Dict[str, Any], weight: float, age: float, state: str) -> Dict[str, Any]:
        output = dict(features)
        for key in self._SCALED_FIELDS:
            if key in output:
                try:
                    output[key] = float(output[key]) * weight
                except (TypeError, ValueError):
                    output[key] = 0.0
        long_score = float(output.get("long_score", 0.0) or 0.0)
        short_score = float(output.get("short_score", 0.0) or 0.0)
        output["direction"] = (
            "LONG" if long_score >= 3.0 and long_score > short_score + 0.25
            else "SHORT" if short_score >= 3.0 and short_score > long_score + 0.25
            else "NONE"
        )
        output.update({
            "quote_observation": True,
            "quote_age_seconds": age,
            "quote_decay": weight,
            "replay_state": state,
        })
        return output

    def replay(
        self,
        snapshots: Iterable[Mapping[str, Any]],
        *,
        decision_times: Optional[Sequence[Any]] = None,
    ) -> ReplayResult:
        raw = [dict(snapshot) for snapshot in snapshots]
        input_digest = sha256_json(raw)
        prepared: List[Tuple[float, int, Mapping[str, Any], Optional[float], Optional[float]]] = []
        for source_index, snapshot in enumerate(raw):
            observed, decision = self._timestamps(snapshot)
            if decision_times is not None and source_index < len(decision_times):
                decision = parse_replay_timestamp(decision_times[source_index])
            sort_time = decision if decision is not None else float("inf")
            prepared.append((sort_time, source_index, snapshot, observed, decision))
        prepared.sort(key=lambda row: (row[0], row[1]))

        records: List[ReplayRecord] = []
        for sequence, (_, source_index, snapshot, observed, decision) in enumerate(prepared):
            source_hash = sha256_json(snapshot)
            price = float(snapshot.get("price", 0.0) or 0.0)
            age = None if observed is None or decision is None else decision - observed
            if observed is None or decision is None:
                state = "NO_OBSERVATION"
                weight = 0.0
                features = self._stale_features(price, state, age, weight)
            elif age < -EPS:
                state = "FUTURE_OBSERVATION"
                weight = 0.0
                features = self._stale_features(price, state, age, weight)
            elif price <= self.policy.min_price:
                state = "INVALID_PRICE"
                weight = 0.0
                features = self._stale_features(price, state, age, weight)
            elif age > self.policy.max_quote_age_seconds:
                state = "STALE"
                weight = 0.0
                features = self._stale_features(price, state, age, weight)
            else:
                weight = math.exp(-max(0.0, age) / self.policy.decay_tau_seconds)
                state = "FRESH" if age <= self.policy.fresh_age_seconds else "DECAYED"
                features = compute_orderflow_features(snapshot, price, now_seconds=decision)
                features = self._apply_decay(features, weight, max(0.0, age), state)
            records.append(ReplayRecord(
                sequence=sequence,
                source_index=source_index,
                observed_at=observed,
                decision_at=decision,
                quote_age_seconds=age,
                decay_weight=weight,
                state=state,
                source_hash=source_hash,
                price=price,
                features=features,
            ))
        return ReplayResult(self.policy, records, len(raw), input_digest)


def load_snapshots(path: Path) -> List[Mapping[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if isinstance(payload, list):
        return payload
    if isinstance(payload, Mapping) and isinstance(payload.get("snapshots"), list):
        return payload["snapshots"]
    raise ValueError("Replay input must be a JSON list or an object with a snapshots list")


def main() -> None:
    parser = argparse.ArgumentParser(description="Deterministic Hyperdash orderflow replay")
    parser.add_argument("--input", required=True, type=Path, help="JSON snapshot list")
    parser.add_argument("--output", type=Path, help="Optional JSON result path")
    parser.add_argument("--decay-tau", type=float, default=10.0)
    parser.add_argument("--max-age", type=float, default=30.0)
    args = parser.parse_args()
    harness = OrderflowReplayHarness(ReplayPolicy(args.decay_tau, args.max_age, min(args.decay_tau, args.max_age)))
    result = harness.replay(load_snapshots(args.input))
    encoded = json.dumps(result.to_dict(), indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(encoded + "\n", encoding="utf-8")
    else:
        print(encoded)


if __name__ == "__main__":  # pragma: no cover
    main()
