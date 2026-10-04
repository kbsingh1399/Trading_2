"""Deterministic broker execution simulator for promotion Gate 4.

This module is deliberately broker-API free.  It models the parts of the MT5
bridge that materially change an entry decision: bid/ask spread, a five-times
candle-open spread spike, route latency, quote age, market deviation, passive
limit expiry, and optional limited liquidity.  It does not claim to reproduce
Blueberry's matching engine; it provides a conservative, reproducible stress
contract for comparing ``market`` and ``limit`` policies before live use.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


EPS = 1e-12


def _finite(value: Any, default: float = 0.0) -> float:
    try:
        value = float(value)
        return value if math.isfinite(value) else default
    except (TypeError, ValueError):
        return default


@dataclass(frozen=True)
class SimQuote:
    timestamp: float
    bid: float
    ask: float
    point: float
    available_volume: Optional[float] = None

    @property
    def mid(self) -> float:
        return (self.bid + self.ask) / 2.0

    @property
    def spread_price(self) -> float:
        return max(0.0, self.ask - self.bid)

    @property
    def spread_points(self) -> float:
        return round(self.spread_price / max(self.point, EPS), 8)

    def widen(self, multiplier: float) -> "SimQuote":
        multiplier = max(0.0, float(multiplier))
        half_spread = self.spread_price * multiplier / 2.0
        return replace(self, bid=self.mid - half_spread, ask=self.mid + half_spread)


@dataclass(frozen=True)
class ExecutionRequest:
    symbol: str
    direction: str
    volume: float
    submitted_at: float
    mode: str = "market"
    limit_price: Optional[float] = None
    expiry_seconds: float = 30.0
    route_latency_seconds: float = 0.25
    max_quote_age_seconds: float = 2.0
    max_spread_points: Optional[float] = 40.0
    deviation_points: float = 20.0
    slippage_points: float = 0.0
    passive_only: bool = True
    allow_partial: bool = False

    def normalized_direction(self) -> str:
        value = self.direction.upper()
        if value in {"LONG", "BUY"}:
            return "LONG"
        if value in {"SHORT", "SELL"}:
            return "SHORT"
        raise ValueError(f"Unsupported direction: {self.direction}")

    def normalized_mode(self) -> str:
        value = self.mode.lower()
        if value not in {"market", "limit"}:
            raise ValueError(f"Unsupported execution mode: {self.mode}")
        return value


@dataclass
class ExecutionResult:
    status: str
    mode: str
    direction: str
    symbol: str
    requested_volume: float
    filled_volume: float
    submitted_at: float
    decision_at: Optional[float]
    requested_price: Optional[float]
    fill_price: Optional[float]
    spread_points: Optional[float]
    quote_age_seconds: Optional[float]
    adverse_slippage_points: Optional[float]
    reason: str
    scenario: str = "base"

    @property
    def filled(self) -> bool:
        return self.status in {"FILLED", "PARTIAL"}

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SpreadSpike:
    """A deterministic spread stress applied at each 15-minute candle open."""

    multiplier: float = 5.0
    candle_seconds: float = 900.0
    open_window_seconds: float = 30.0
    candle_epoch: float = 0.0
    name: str = "5x_candle_open_spread"

    def multiplier_at(self, timestamp: float) -> float:
        phase = (float(timestamp) - self.candle_epoch) % self.candle_seconds
        return self.multiplier if phase < self.open_window_seconds else 1.0

    def apply(self, quotes: Iterable[SimQuote]) -> List[SimQuote]:
        return [quote.widen(self.multiplier_at(quote.timestamp)) for quote in quotes]


@dataclass
class StressComparison:
    scenario: str
    market: ExecutionResult
    limit: ExecutionResult

    def to_dict(self) -> Dict[str, Any]:
        return {
            "scenario": self.scenario,
            "market": self.market.to_dict(),
            "limit": self.limit.to_dict(),
        }


class BrokerExecutionSimulator:
    """Replay a quote stream against the bridge's market/limit policies."""

    def __init__(self, *, default_point: float = 0.001):
        self.default_point = max(float(default_point), EPS)

    @staticmethod
    def _sorted_quotes(quotes: Iterable[SimQuote]) -> List[SimQuote]:
        output = sorted(quotes, key=lambda quote: quote.timestamp)
        if not output:
            raise ValueError("At least one quote is required")
        for quote in output:
            if quote.ask < quote.bid or quote.point <= 0:
                raise ValueError("Quotes must satisfy ask >= bid and point > 0")
        return output

    @staticmethod
    def _quote_at_or_after(quotes: Sequence[SimQuote], timestamp: float) -> Optional[SimQuote]:
        for quote in quotes:
            if quote.timestamp >= timestamp:
                return quote
        return None

    @staticmethod
    def _volume_result(request: ExecutionRequest, quote: SimQuote) -> Tuple[str, float, str]:
        requested = max(0.0, request.volume)
        if requested <= 0.0:
            return "REJECTED", 0.0, "non_positive_volume"
        if quote.available_volume is None or quote.available_volume >= requested:
            return "FILLED", requested, "filled"
        available = max(0.0, quote.available_volume)
        if request.allow_partial and available > 0.0:
            return "PARTIAL", available, "partial_liquidity"
        return "REJECTED", 0.0, "insufficient_liquidity"

    @staticmethod
    def _spread_rejected(request: ExecutionRequest, quote: SimQuote) -> bool:
        return request.max_spread_points is not None and quote.spread_points > request.max_spread_points

    @staticmethod
    def _passive_limit_valid(request: ExecutionRequest, quote: SimQuote, limit_price: float) -> bool:
        direction = request.normalized_direction()
        if direction == "LONG":
            return quote.bid <= limit_price < quote.ask
        return quote.bid < limit_price <= quote.ask

    def simulate(self, request: ExecutionRequest, quotes: Iterable[SimQuote], *, scenario: str = "base") -> ExecutionResult:
        ordered = self._sorted_quotes(quotes)
        mode = request.normalized_mode()
        direction = request.normalized_direction()
        first = self._quote_at_or_after(ordered, request.submitted_at)
        common = {
            "mode": mode,
            "direction": direction,
            "symbol": request.symbol,
            "requested_volume": request.volume,
            "submitted_at": request.submitted_at,
            "scenario": scenario,
        }
        if first is None:
            return ExecutionResult(status="NO_QUOTE", filled_volume=0.0, decision_at=None, requested_price=None, fill_price=None, spread_points=None, quote_age_seconds=None, adverse_slippage_points=None, reason="no_quote_after_submission", **common)
        if self._spread_rejected(request, first):
            return ExecutionResult(status="REJECTED", filled_volume=0.0, decision_at=first.timestamp, requested_price=None, fill_price=None, spread_points=first.spread_points, quote_age_seconds=first.timestamp - request.submitted_at, adverse_slippage_points=None, reason="spread_guard_at_submission", **common)

        if mode == "market":
            execution_quote = self._quote_at_or_after(ordered, request.submitted_at + max(0.0, request.route_latency_seconds))
            if execution_quote is None:
                return ExecutionResult(status="NO_QUOTE", filled_volume=0.0, decision_at=None, requested_price=None, fill_price=None, spread_points=None, quote_age_seconds=None, adverse_slippage_points=None, reason="no_quote_after_route_latency", **common)
            age = execution_quote.timestamp - request.submitted_at
            if request.max_quote_age_seconds >= 0 and age > request.max_quote_age_seconds:
                return ExecutionResult(status="REJECTED", filled_volume=0.0, decision_at=execution_quote.timestamp, requested_price=None, fill_price=None, spread_points=execution_quote.spread_points, quote_age_seconds=age, adverse_slippage_points=None, reason="stale_quote", **common)
            if self._spread_rejected(request, execution_quote):
                return ExecutionResult(status="REJECTED", filled_volume=0.0, decision_at=execution_quote.timestamp, requested_price=None, fill_price=None, spread_points=execution_quote.spread_points, quote_age_seconds=age, adverse_slippage_points=None, reason="spread_guard_at_execution", **common)
            reference = first.ask if direction == "LONG" else first.bid
            requested = execution_quote.ask if direction == "LONG" else execution_quote.bid
            if request.deviation_points >= 0 and abs(requested - reference) > request.deviation_points * execution_quote.point:
                return ExecutionResult(status="REJECTED", filled_volume=0.0, decision_at=execution_quote.timestamp, requested_price=requested, fill_price=None, spread_points=execution_quote.spread_points, quote_age_seconds=age, adverse_slippage_points=None, reason="deviation_guard", **common)
            fill = requested + request.slippage_points * execution_quote.point if direction == "LONG" else requested - request.slippage_points * execution_quote.point
            status, filled_volume, reason = self._volume_result(request, execution_quote)
            if status == "REJECTED":
                fill = None
            adverse = None if fill is None else ((fill - reference) / execution_quote.point if direction == "LONG" else (reference - fill) / execution_quote.point)
            return ExecutionResult(status=status, filled_volume=filled_volume, decision_at=execution_quote.timestamp, requested_price=requested, fill_price=fill, spread_points=execution_quote.spread_points, quote_age_seconds=age, adverse_slippage_points=adverse, reason=reason, **common)

        limit_price = request.limit_price
        if limit_price is None:
            return ExecutionResult(status="REJECTED", filled_volume=0.0, decision_at=first.timestamp, requested_price=None, fill_price=None, spread_points=first.spread_points, quote_age_seconds=first.timestamp - request.submitted_at, adverse_slippage_points=None, reason="limit_price_required", **common)
        limit_price = float(limit_price)
        if request.passive_only and not self._passive_limit_valid(request, first, limit_price):
            return ExecutionResult(status="REJECTED", filled_volume=0.0, decision_at=first.timestamp, requested_price=limit_price, fill_price=None, spread_points=first.spread_points, quote_age_seconds=first.timestamp - request.submitted_at, adverse_slippage_points=None, reason="passive_limit_outside_spread", **common)

        expiry = request.submitted_at + max(0.0, request.expiry_seconds)
        for quote in ordered:
            if quote.timestamp < request.submitted_at:
                continue
            if quote.timestamp > expiry:
                break
            age = quote.timestamp - request.submitted_at
            # An already-staged order is explicitly cancelled rather than
            # filled through a spread spike; this models the bridge's safety
            # policy and makes the adverse case visible in the report.
            if self._spread_rejected(request, quote):
                return ExecutionResult(status="CANCELLED_SPREAD", filled_volume=0.0, decision_at=quote.timestamp, requested_price=limit_price, fill_price=None, spread_points=quote.spread_points, quote_age_seconds=age, adverse_slippage_points=None, reason="spread_guard_while_pending", **common)
            crosses = quote.ask <= limit_price if direction == "LONG" else quote.bid >= limit_price
            if not crosses:
                continue
            fill = quote.ask if direction == "LONG" else quote.bid
            status, filled_volume, reason = self._volume_result(request, quote)
            if status == "REJECTED":
                return ExecutionResult(status=status, filled_volume=0.0, decision_at=quote.timestamp, requested_price=limit_price, fill_price=None, spread_points=quote.spread_points, quote_age_seconds=age, adverse_slippage_points=None, reason=reason, **common)
            adverse = ((fill - limit_price) / quote.point if direction == "LONG" else (limit_price - fill) / quote.point)
            return ExecutionResult(status=status, filled_volume=filled_volume, decision_at=quote.timestamp, requested_price=limit_price, fill_price=fill, spread_points=quote.spread_points, quote_age_seconds=age, adverse_slippage_points=max(0.0, adverse), reason=reason, **common)
        return ExecutionResult(status="EXPIRED", filled_volume=0.0, decision_at=expiry, requested_price=limit_price, fill_price=None, spread_points=None, quote_age_seconds=max(0.0, request.expiry_seconds), adverse_slippage_points=None, reason="limit_expired_unfilled", **common)

    def compare_modes(
        self,
        quotes: Iterable[SimQuote],
        *,
        symbol: str,
        direction: str,
        volume: float,
        submitted_at: float,
        limit_price: float,
        scenario: str = "base",
        **policy: Any,
    ) -> StressComparison:
        quote_list = self._sorted_quotes(quotes)
        market_request = ExecutionRequest(symbol, direction, volume, submitted_at, mode="market", **policy)
        limit_request = ExecutionRequest(symbol, direction, volume, submitted_at, mode="limit", limit_price=limit_price, **policy)
        return StressComparison(
            scenario=scenario,
            market=self.simulate(market_request, quote_list, scenario=scenario),
            limit=self.simulate(limit_request, quote_list, scenario=scenario),
        )

    def stress_spread_open(
        self,
        quotes: Iterable[SimQuote],
        *,
        symbol: str,
        direction: str,
        volume: float,
        submitted_at: float,
        limit_price: float,
        spike: SpreadSpike = SpreadSpike(),
        **policy: Any,
    ) -> StressComparison:
        stressed = spike.apply(self._sorted_quotes(quotes))
        return self.compare_modes(
            stressed, symbol=symbol, direction=direction, volume=volume,
            submitted_at=submitted_at, limit_price=limit_price,
            scenario=spike.name, **policy,
        )

    @staticmethod
    def summary(comparisons: Sequence[StressComparison]) -> Dict[str, Any]:
        result: Dict[str, Any] = {"cases": len(comparisons), "modes": {"market": {}, "limit": {}}}
        for mode in ("market", "limit"):
            statuses: Dict[str, int] = {}
            fills = 0
            slippage = []
            for case in comparisons:
                execution: ExecutionResult = getattr(case, mode)
                statuses[execution.status] = statuses.get(execution.status, 0) + 1
                if execution.filled:
                    fills += 1
                    if execution.adverse_slippage_points is not None:
                        slippage.append(execution.adverse_slippage_points)
            result["modes"][mode] = {
                "filled": fills,
                "fill_rate": fills / len(comparisons) if comparisons else 0.0,
                "statuses": statuses,
                "mean_adverse_slippage_points": sum(slippage) / len(slippage) if slippage else None,
            }
        return result


def load_quotes(path: Path, default_point: float = 0.001) -> List[SimQuote]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload if isinstance(payload, list) else payload.get("quotes", [])
    output = []
    for row in rows:
        point = _finite(row.get("point", default_point), default_point)
        output.append(SimQuote(
            timestamp=_finite(row.get("timestamp", row.get("time"))),
            bid=_finite(row.get("bid")),
            ask=_finite(row.get("ask")),
            point=point,
            available_volume=(
                _finite(row.get("available_volume"))
                if row.get("available_volume") is not None else None
            ),
        ))
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Deterministic MT5 market-vs-limit stress simulator")
    parser.add_argument("--input", required=True, type=Path, help="JSON quote list")
    parser.add_argument("--symbol", default="SOLUSD.p")
    parser.add_argument("--direction", choices=["LONG", "SHORT"], default="LONG")
    parser.add_argument("--volume", type=float, default=0.5)
    parser.add_argument("--submitted-at", type=float, required=True)
    parser.add_argument("--limit-price", type=float, required=True)
    parser.add_argument("--max-spread-points", type=float, default=40.0)
    parser.add_argument("--spike-multiplier", type=float, default=5.0)
    args = parser.parse_args()
    quotes = load_quotes(args.input)
    simulator = BrokerExecutionSimulator()
    comparison = simulator.stress_spread_open(
        quotes, symbol=args.symbol, direction=args.direction, volume=args.volume,
        submitted_at=args.submitted_at, limit_price=args.limit_price,
        spike=SpreadSpike(multiplier=args.spike_multiplier),
        max_spread_points=args.max_spread_points,
    )
    print(json.dumps(comparison.to_dict(), indent=2, sort_keys=True))


if __name__ == "__main__":  # pragma: no cover
    main()
