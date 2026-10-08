"""OX_ALPHA_62 deliberate trade-plan stager (fail-closed execution vehicle).

Loads a machine-readable plan document (``docs/trade_plans/*.json``),
re-validates every OX_ALPHA_62 risk invariant client-side, verifies live
account/market state over the HMAC-signed tunnel, and only then submits a
signed ``STAGE_ORDER`` command.  The muscle re-enforces every cap on arrival
(defense in depth), so a plan that passes here can still be refused there.

Governance doctrine (consultation 5/62):
  * fail-closed - degraded tunnel or missing state => NO TRADE, no exceptions;
  * dry-run by default - submission requires the explicit ``--execute`` flag;
  * zero fabricated statistics - the plan carries only deterministic,
    source-attributed inputs; the stager recomputes every derived number.

CLI:
    python -m Terminal.Headless.stage_trade_plan docs/trade_plans/PLAN.json
    python -m Terminal.Headless.stage_trade_plan docs/trade_plans/PLAN.json --execute
    python -m Terminal.Headless.stage_trade_plan --purge-expired

Environment:
    ARENA_TUNNEL_URL   public gateway (default: live OX_ALPHA_62 tunnel)
    OMNI_API_SECRET    HMAC shared secret (required; no fallback -> fail-closed)

Exit codes: 0 ok, 1 usage, 2 plan validation refusal, 3 live precheck
refusal, 4 staging failure.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

STAGER_VERSION = "omni.stage_trade_plan.v1"
PLAN_VERSION = "omni.trade_plan.v1"
PLAN_COMMENT_PREFIX = "ARENA:"
DEFAULT_JOURNAL = "Data/Omni/brain/plan_journal.jsonl"

# --- OX_ALPHA_62 governance envelope (client-side mirror; muscle re-enforces) ---
MIN_RISK_USD = 10.0            # base conviction budget, lower bound
MAX_RISK_USD = 20.0            # hard cap per trade under NO circumstances exceeded
SL_ATR_FLOOR = 1.5             # adaptive stop floor: distance >= 1.5 x ATR(14)
TP_R_MIN = 2.5                 # target band lower edge (2.50R)
TP_R_MAX = 3.14                # target band upper edge (never chase moonshots)
EQUITY_FLOOR_USD = 4775.0      # hard equity defense floor (4.50% of 5,000 USD)
MAX_FILLED_POSITIONS = 2       # MAX_CONCURRENT invariant (filled positions)
MAX_PENDING_TOTAL = 2          # without proven atomic OCO, count every possible joint fill
STATE_STALENESS_S = 120.0      # market_state as_of freshness bound
DEFAULT_MAX_FRICTION_R = 0.35  # round-trip spread cost ceiling, in R units
TTL_BARS_MAX = 24              # the 24-bar decay convention
RISK_DECLARE_TOLERANCE_USD = 0.05
EPS = 1e-9

REQUIRED_FIELDS = ("plan_version", "plan_id", "symbol", "direction",
                   "limit_price", "sl", "tp", "volume", "atr", "risk_usd",
                   "ttl_bars", "comment", "created_at_epoch",
                   "expires_at_epoch", "contract")


class PlanValidationError(ValueError):
    """Offline plan refusal (deterministic; never depends on the network)."""

    def __init__(self, code: str, detail: str = "") -> None:
        super().__init__(f"{code}:{detail}" if detail else code)
        self.code = code
        self.detail = detail


def _num(value: Any, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def _on_tick(price: float, tick: float) -> bool:
    """True when price is aligned to the instrument tick grid."""
    if tick <= 0:
        return False
    steps = price / tick
    return abs(steps - round(steps)) <= 1e-4


def _risk_usd(plan: Dict) -> float:
    contract = _num(plan.get("contract", {}).get("contract_size"), 1.0)
    distance = abs(_num(plan.get("limit_price")) - _num(plan.get("sl")))
    risk = _num(plan.get("volume")) * distance * contract
    # JPY-quoted pairs: the account is USD but the contract denominates one
    # leg in JPY, so USD risk requires division by the entry price (the
    # SPEC-table pitfall the forensics audit flagged; without this every
    # USDJPY plan overstates risk ~158x and can never validate).
    symbol = str(plan.get("symbol", "")).upper()
    if symbol.endswith("JPY") or str(plan.get("asset", "")).upper() == "USDJPY":
        price = _num(plan.get("limit_price"))
        if price > 0:
            risk /= price
    return risk


def _tp_r(plan: Dict) -> float:
    distance = abs(_num(plan.get("limit_price")) - _num(plan.get("sl")))
    if distance <= 0:
        return 0.0
    gain = (_num(plan.get("tp")) - _num(plan.get("limit_price"))) \
        if plan.get("direction") == "LONG" \
        else (_num(plan.get("limit_price")) - _num(plan.get("tp")))
    return gain / distance


# ---------------------------------------------------------------- validation
def validate_plan(plan: Dict, *, now: float) -> Dict:
    """Validate one plan document against the governance envelope.

    Raises :class:`PlanValidationError` on the FIRST violation found
    (deterministic order of checks).  Returns a normalised copy on success.
    """
    if not isinstance(plan, dict):
        raise PlanValidationError("plan_not_a_mapping")
    for field in REQUIRED_FIELDS:
        if field not in plan:
            raise PlanValidationError("missing_field", field)
    if plan["plan_version"] != PLAN_VERSION:
        raise PlanValidationError("unsupported_plan_version", str(plan["plan_version"]))

    symbol = str(plan["symbol"]).strip()
    direction = str(plan["direction"]).strip().upper()
    if not symbol:
        raise PlanValidationError("invalid_symbol")
    if direction not in ("LONG", "SHORT"):
        raise PlanValidationError("invalid_direction", direction)
    comment = str(plan["comment"])
    if not comment.startswith(PLAN_COMMENT_PREFIX):
        raise PlanValidationError("invalid_comment_prefix", comment)

    limit_price = _num(plan["limit_price"])
    sl = _num(plan["sl"])
    tp = _num(plan["tp"])
    atr = _num(plan["atr"])
    if limit_price <= 0 or sl <= 0 or tp <= 0:
        raise PlanValidationError("non_positive_price")
    if atr <= 0:
        raise PlanValidationError("non_positive_atr")

    # Geometry: stop protects, target pays, never crossed.
    if direction == "LONG" and not (sl < limit_price < tp):
        raise PlanValidationError("geometry_violation", "LONG requires sl < limit < tp")
    if direction == "SHORT" and not (tp < limit_price < sl):
        raise PlanValidationError("geometry_violation", "SHORT requires tp < limit < sl")

    contract = plan.get("contract") or {}
    tick = _num(contract.get("tick_size"))
    min_lot = _num(contract.get("min_lot"))
    step_lot = _num(contract.get("step_lot"))
    contract_size = _num(contract.get("contract_size"), 1.0)
    if tick <= 0 or min_lot <= 0 or step_lot <= 0 or contract_size <= 0:
        raise PlanValidationError("invalid_contract_spec")

    for name, price in (("limit_price", limit_price), ("sl", sl), ("tp", tp)):
        if not _on_tick(price, tick):
            raise PlanValidationError("price_off_tick", f"{name}={price}")

    # Adaptive stop floor: SL distance >= 1.5 x ATR(14).
    distance = abs(limit_price - sl)
    if distance + EPS < SL_ATR_FLOOR * atr:
        raise PlanValidationError("sl_inside_atr_floor",
                                  f"distance={distance:.6f} < {SL_ATR_FLOOR}*atr="
                                  f"{SL_ATR_FLOOR * atr:.6f}")

    # Target band: 2.50R .. 3.14R (never chase moonshots).
    tp_r = _tp_r(plan)
    if tp_r + EPS < TP_R_MIN or tp_r > TP_R_MAX + EPS:
        raise PlanValidationError("tp_outside_band", f"tp_r={tp_r:.4f}")

    # Volume feasibility.
    volume = _num(plan["volume"])
    if volume + EPS < min_lot:
        raise PlanValidationError("volume_below_min_lot", f"{volume} < {min_lot}")
    steps = volume / step_lot
    if abs(steps - round(steps)) > EPS:
        raise PlanValidationError("volume_off_step", f"{volume} not multiple of {step_lot}")

    # Risk envelope: 10.00 .. 20.00 USD, declared value must match recomputed.
    risk = _risk_usd(plan)
    if risk + EPS < MIN_RISK_USD:
        raise PlanValidationError("risk_below_floor", f"{risk:.4f} < {MIN_RISK_USD}")
    if risk > MAX_RISK_USD + EPS:
        raise PlanValidationError("risk_above_cap", f"{risk:.4f} > {MAX_RISK_USD}")
    declared = _num(plan["risk_usd"], -1.0)
    if abs(declared - risk) > RISK_DECLARE_TOLERANCE_USD:
        raise PlanValidationError("declared_risk_mismatch",
                                  f"declared={declared:.4f} computed={risk:.4f}")

    # TTL: 1 .. 24 bars (the decay convention).
    ttl = plan["ttl_bars"]
    if not isinstance(ttl, int) or not (1 <= ttl <= TTL_BARS_MAX):
        raise PlanValidationError("invalid_ttl_bars", str(ttl))

    # Plan validity window (data staleness gate; independent of order TTL).
    created = _num(plan["created_at_epoch"], -1.0)
    expires = _num(plan["expires_at_epoch"], -1.0)
    if created <= 0 or expires <= created:
        raise PlanValidationError("invalid_validity_window")
    if now < created - EPS:
        raise PlanValidationError("plan_created_in_future")
    if now >= expires:
        raise PlanValidationError("plan_expired",
                                  f"now={now:.0f} expires={expires:.0f}")

    # Declared blackout windows (Specialist-3 Tier-1 calendar).
    windows = plan.get("blackout_windows") or []
    if not isinstance(windows, list):
        raise PlanValidationError("invalid_blackout_windows")
    for window in windows:
        start = _num(window.get("start_epoch"), -1.0)
        end = _num(window.get("end_epoch"), -1.0)
        if start <= 0 or end <= start:
            raise PlanValidationError("invalid_blackout_window", str(window))
        if start <= now < end:
            raise PlanValidationError("blackout_active",
                                      str(window.get("reason", "tier1_event")))

    max_friction_r = _num(plan.get("max_friction_r"), DEFAULT_MAX_FRICTION_R)
    if not (0.0 < max_friction_r <= 0.5):
        raise PlanValidationError("invalid_max_friction_r", str(max_friction_r))

    normalised = dict(plan)
    normalised.update(direction=direction, symbol=symbol,
                      limit_price=limit_price, sl=sl, tp=tp, atr=atr,
                      volume=volume, computed_risk_usd=round(risk, 6),
                      computed_tp_r=round(tp_r, 6),
                      max_friction_r=max_friction_r)
    return normalised


# ---------------------------------------------------------------- live gate
def _transport_ok(payload: Dict) -> bool:
    return isinstance(payload, dict) and "error" not in payload \
        and not payload.get("http_status")


def _existing_risk_usd(state: Dict) -> float:
    """Count filled AND resting worst-case stop losses; refuse incomplete data."""
    total = 0.0
    quotes = state.get("quotes") or {}
    for row in [*state["positions"], *state["pending_orders"]]:
        if not isinstance(row, dict):
            raise ValueError("invalid_risk_inventory_row")
        symbol = row.get("symbol")
        quote = quotes.get(symbol) or {}
        contract = _num(row.get("contract_size"), _num(quote.get("contract_size")))
        volume = _num(row.get("volume"))
        entry = _num(row.get("entry"), _num(row.get("price_open")))
        sl = _num(row.get("sl"))
        if not symbol or min(contract, volume, entry, sl) <= 0:
            raise ValueError("missing_inventory_stop_or_contract")
        direction = str(row.get("direction", "")).upper()
        if direction not in ("LONG", "SHORT"):
            raise ValueError("unknown_inventory_direction")
        adverse = sl < entry if direction == "LONG" else sl > entry
        risk = volume * abs(entry - sl) * contract if adverse else 0.0
        if symbol.upper().startswith("USDJPY"):
            risk /= entry  # quote currency JPY, account currency USD
        total += risk
    return total


def live_precheck(client: Any, plan: Dict, *, now: float) -> Dict:
    """Fail-closed live verification over the signed tunnel.

    Returns a report dict; ``ok`` is True only when EVERY gate passes.
    """
    checks: Dict[str, Any] = {}
    try:
        state = client.market_state()
    except Exception as exc:                                  # noqa: BLE001
        return {"ok": False, "reason": "market_state_exception",
                "detail": repr(exc), "checks": checks}
    if not _transport_ok(state):
        detail = str(state.get("error", state.get("http_status"))) if isinstance(state, dict) else str(state)
        return {"ok": False, "reason": "tunnel_unreachable",
                "detail": detail,
                "checks": checks}
    checks["transport"] = "ok"

    as_of = _num(state.get("as_of"), 0.0)
    if as_of <= 0 or abs(now - as_of) > STATE_STALENESS_S:
        checks["freshness"] = f"stale:{now - as_of:.0f}s"
        return {"ok": False, "reason": "market_state_stale", "checks": checks}
    checks["freshness"] = "ok"

    from datetime import datetime, timezone
    from Terminal.risk.blackout_guard import is_in_blackout
    blocked, block_reason = is_in_blackout(datetime.fromtimestamp(now, tz=timezone.utc))
    if blocked:
        checks["macro"] = f"blackout:{block_reason}"
        return {"ok": False, "reason": "macro_blackout", "checks": checks}
    macro = state.get("macro") or {}
    if macro.get("blackout_active"):
        checks["macro"] = f"blackout:{macro.get('blackout_event')}"
        return {"ok": False, "reason": "macro_blackout", "checks": checks}
    checks["macro"] = "clear"

    account = state.get("account") or {}
    equity = _num(account.get("equity_usd"), 0.0)
    if equity <= 0:
        return {"ok": False, "reason": "equity_unavailable", "checks": checks}
    if not isinstance(state.get("positions"), list) or not isinstance(state.get("pending_orders"), list):
        return {"ok": False, "reason": "risk_inventory_unavailable", "checks": checks}
    positions = state["positions"]
    pending = state["pending_orders"]
    max_filled = int(state.get("max_filled_positions", MAX_FILLED_POSITIONS))
    max_pending = int(state.get("max_pending_orders", MAX_PENDING_TOTAL))
    if len(positions) >= max_filled:
        return {"ok": False, "reason": "max_filled_positions", "checks": checks}
    if len(positions) + len(pending) >= max_pending:
        return {"ok": False, "reason": "pending_limit_ceiling", "checks": checks}
    plan_risk = _num(plan.get("computed_risk_usd", plan.get("risk_usd")))
    try:
        existing_risk = _existing_risk_usd(state)
    except (KeyError, ValueError, TypeError) as exc:
        return {"ok": False, "reason": "risk_inventory_unavailable",
                "detail": str(exc), "checks": checks}
    balance = _num(account.get("balance_usd"), 0.0)
    if balance <= 0:
        return {"ok": False, "reason": "balance_unavailable", "checks": checks}
    # Broker receiver independently recomputes using native order_calc_profit.
    from Terminal.risk.live_admission import STOP_STRESS_MULTIPLIER, MIN_EXECUTION_COST_USD
    total_risk_stressed = ((existing_risk + plan_risk) * STOP_STRESS_MULTIPLIER
                           + (len(positions) + len(pending) + 1) * MIN_EXECUTION_COST_USD)
    cushion = min(balance, equity) - total_risk_stressed
    checks["account"] = {"equity_usd": round(equity, 2),
                         "existing_risk_usd": round(existing_risk, 2),
                         "plan_risk_usd": round(plan_risk, 2),
                         "stressed_joint_risk_usd": round(total_risk_stressed, 2),
                         "cushion_above_floor_usd": round(cushion - EQUITY_FLOOR_USD, 2)}
    if cushion < EQUITY_FLOOR_USD + 20.0:
        return {"ok": False, "reason": "equity_floor_breach", "checks": checks}
    checks["capacity"] = {"filled": len(positions), "pending": len(pending)}

    quote = (state.get("quotes") or {}).get(plan["symbol"])
    if not isinstance(quote, dict):
        return {"ok": False, "reason": "quote_unavailable",
                "detail": plan["symbol"], "checks": checks}
    bid = _num(quote.get("bid"))
    ask = _num(quote.get("ask"))
    tick = _num(quote.get("tick_size"), _num(plan["contract"].get("tick_size")))
    if bid <= 0 or ask < bid or tick <= 0:
        return {"ok": False, "reason": "quote_invalid", "checks": checks}
    live_contract = _num(quote.get("contract_size"), -1.0)
    plan_contract = _num(plan["contract"].get("contract_size"))
    if live_contract > 0 and abs(live_contract - plan_contract) > EPS:
        return {"ok": False, "reason": "contract_mismatch",
                "detail": f"live={live_contract} plan={plan_contract}",
                "checks": checks}

    # Passive entry: a LONG limit must rest below the ask (SHORT above the
    # bid); marketable limits are refused muscle-side anyway.
    if plan["direction"] == "LONG" and not (plan["limit_price"] < ask - EPS):
        return {"ok": False, "reason": "marketable_limit", "checks": checks}
    if plan["direction"] == "SHORT" and not (plan["limit_price"] > bid + EPS):
        return {"ok": False, "reason": "marketable_limit", "checks": checks}

    # Live friction gate: round-trip cost (full spread + one tick, the
    # conservative live bound) must stay inside the plan's R-unit ceiling.
    # The 41 bps backtest haircut is accounted separately in the plan memo.
    distance = abs(plan["limit_price"] - plan["sl"])
    friction_r = (ask - bid + tick) / distance
    checks["friction"] = {"spread": round(ask - bid, 6),
                          "friction_r": round(friction_r, 4),
                          "ceiling_r": plan["max_friction_r"]}
    if friction_r > plan["max_friction_r"] + EPS:
        return {"ok": False, "reason": "friction_excessive", "checks": checks}

    checks["quote"] = {"bid": bid, "ask": ask}
    return {"ok": True, "reason": None, "checks": checks}


# ---------------------------------------------------------------- execution
def _stage_ok(response: Any) -> bool:
    return isinstance(response, dict) and "error" not in response \
        and not response.get("http_status") and response.get("ok", True) is not False


def execute_plan(client: Any, plan: Dict, *,
                 journal: Optional[Callable[[Dict], None]] = None,
                 now: Optional[float] = None) -> Dict:
    """Submit the signed STAGE_ORDER (the only mutating action)."""
    now = time.time() if now is None else now
    response = client.stage_order(
        symbol=plan["symbol"], direction=plan["direction"],
        volume=plan["volume"], limit_price=plan["limit_price"],
        sl=plan["sl"], tp=plan["tp"], comment=plan["comment"],
        expiration_seconds=int(plan["ttl_bars"]) * 900)
    ok = _stage_ok(response)
    row = {"ts": now, "event": "staged" if ok else "stage_failed",
           "plan_id": plan.get("plan_id"), "symbol": plan["symbol"],
           "direction": plan["direction"], "limit_price": plan["limit_price"],
           "volume": plan["volume"], "risk_usd": plan.get("computed_risk_usd"),
           "expires_at_epoch": now + int(plan["ttl_bars"]) * 900}
    if isinstance(response, dict):
        for key in ("ticket", "order", "risk_usd"):
            if response.get(key) is not None:
                row[key] = response.get(key)
    if journal is not None:
        journal(row)
    return {"ok": ok, "response": response, "journal_row": row}


def stage(client: Any, plan_path: str, *, execute: bool = False,
          now: Optional[float] = None,
          journal_path: Optional[str] = None) -> int:
    """Orchestrator: validate -> live precheck -> (optionally) execute."""
    now = time.time() if now is None else now
    with open(plan_path, "r", encoding="utf-8") as handle:
        plan = json.load(handle)

    journal = _journal_appender(journal_path)
    try:
        plan = validate_plan(plan, now=now)
    except PlanValidationError as exc:
        print(f"[stager] REFUSED offline ({exc.code}): {exc.detail}", flush=True)
        if journal is not None:
            journal({"ts": now, "event": "refused", "plan_id": plan.get("plan_id"),
                     "stage": "offline", "reason": exc.code, "detail": exc.detail})
        return 2
    print(f"[stager] plan {plan['plan_id']} validated offline: "
          f"{plan['symbol']} {plan['direction']} {plan['volume']} lots @ "
          f"{plan['limit_price']} SL {plan['sl']} TP {plan['tp']} "
          f"(risk {plan['computed_risk_usd']:.2f} USD, "
          f"target {plan['computed_tp_r']:.2f}R)", flush=True)

    report = live_precheck(client, plan, now=now)
    for name, value in report.get("checks", {}).items():
        print(f"[stager]   {name}: {value}", flush=True)
    if not report["ok"]:
        print(f"[stager] REFUSED live ({report['reason']}): "
              f"{report.get('detail', '')}", flush=True)
        if journal is not None:
            journal({"ts": now, "event": "refused", "plan_id": plan.get("plan_id"),
                     "stage": "live", "reason": report["reason"]})
        return 3

    if not execute:
        print("[stager] dry-run complete (pass --execute to submit)", flush=True)
        if journal is not None:
            journal({"ts": now, "event": "validated", "plan_id": plan.get("plan_id"),
                     "risk_usd": plan.get("computed_risk_usd")})
        return 0

    outcome = execute_plan(client, plan, journal=journal, now=now)
    if not outcome["ok"]:
        print(f"[stager] STAGE FAILED: {outcome['response']}", flush=True)
        return 4
    print(f"[stager] STAGED: {outcome['response']}", flush=True)
    return 0


# ---------------------------------------------------------------- purge mode
def purge_expired(client: Any, journal_path: str, *,
                  now: Optional[float] = None) -> int:
    """Cancel ARENA plan tickets whose TTL has lapsed (journal-driven)."""
    now = time.time() if now is None else now
    path = Path(journal_path)
    rows: List[Dict] = []
    if path.exists():
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    continue
    staged = {int(r["ticket"]): r for r in rows
              if r.get("event") == "staged" and r.get("ticket") is not None}
    purged = {int(r["ticket"]) for r in rows
              if r.get("event") == "purged" and r.get("ticket") is not None}
    cancelled = 0
    for ticket, row in sorted(staged.items()):
        if ticket in purged:
            continue
        if _num(row.get("expires_at_epoch"), 0.0) > now:
            continue
        try:
            response = client.cancel_order(ticket)
        except Exception as exc:                              # noqa: BLE001
            print(f"[stager] purge {ticket} exception: {exc!r}", flush=True)
            response = {"error": repr(exc)}
        ok = _stage_ok(response)
        print(f"[stager] purge ticket {ticket}: "
              f"{'ok' if ok else 'FAILED ' + str(response)}", flush=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"ts": now, "event": "purged" if ok
                                     else "purge_failed", "ticket": ticket,
                                     "plan_id": row.get("plan_id")}) + "\n")
        cancelled += 1 if ok else 0
    print(f"[stager] purge complete: {cancelled} cancelled", flush=True)
    return 0


def _journal_appender(journal_path: Optional[str]) -> Optional[Callable[[Dict], None]]:
    if not journal_path:
        return None
    path = Path(journal_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    def append(row: Dict) -> None:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(row, default=str) + "\n")

    return append


# --------------------------------------------------------------------- CLI
def _main(argv=None, *, client_factory=None) -> int:
    from Terminal.Headless.arena_continuous_brain import (DEFAULT_SECRET,
                                                          DEFAULT_TUNNEL_URL)
    from Terminal.Headless.brain_client import BrainClient

    parser = argparse.ArgumentParser(
        description="OX_ALPHA_62 fail-closed trade-plan stager")
    parser.add_argument("plan", nargs="?", help="path to plan JSON document")
    parser.add_argument("--execute", action="store_true",
                        help="actually submit the signed STAGE_ORDER "
                             "(default is a dry run)")
    parser.add_argument("--purge-expired", action="store_true",
                        help="cancel ARENA plan tickets whose TTL has lapsed")
    parser.add_argument("--url", default=os.environ.get("ARENA_TUNNEL_URL",
                                                        DEFAULT_TUNNEL_URL))
    parser.add_argument("--secret", default=os.environ.get("OMNI_API_SECRET",
                                                           DEFAULT_SECRET))
    parser.add_argument("--journal", default=DEFAULT_JOURNAL)
    args = parser.parse_args(argv)

    if not args.secret:
        parser.error("OMNI_API_SECRET required (or --secret)")
    make_client = client_factory or (lambda: BrainClient(args.url, args.secret))
    if args.purge_expired:
        return purge_expired(make_client(), args.journal)
    if not args.plan:
        parser.error("plan path required (or --purge-expired)")
    return stage(make_client(), args.plan, execute=args.execute,
                 journal_path=args.journal)


if __name__ == "__main__":
    sys.exit(_main())
