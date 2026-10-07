#!/usr/bin/env python3
"""Read-only, fail-closed 60-second telemetry/blackboard risk sentinel.

This is deterministic monitoring, NOT a continuously thinking Arena chat agent.
It never connects to MT5, dispatches broker commands, or generates trade plans.
It reads the current fixed-branch GitHub snapshot; if --publish is supplied,
it posts material risk alerts to the desk on that branch, at most once per
alert signature every five minutes. Heartbeats always appear in process logs.

    python scripts/arena_endless_runner.py --once
    python scripts/arena_endless_runner.py --daemon --interval 60 --publish --verbose
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import logging
import math
from pathlib import Path
import subprocess
import time
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "arena/83d03e3f-trading-2"
REMOTE = f"refs/remotes/origin/{BRANCH}"
TELEMETRY = "docs/telemetry/live_snapshot_latest.json"
DESK = "docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md"
STATE_FILE = ROOT / "Data/Omni/brain/arena_sentinel_state.json"  # gitignored
FLOOR = 4775.0
BUFFER = 20.0
MAX_AGE_S = 180
REPEAT_ALERT_S = 300
LOG = logging.getLogger("arena.risk_sentinel")


def git(*args: str, timeout: int = 35) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                            text=True, timeout=timeout)
    if result.returncode:
        raise RuntimeError(f"git {' '.join(args[:3])}: {result.stderr.strip()[:350]}")
    return result.stdout


def fetch_snapshot() -> dict[str, Any]:
    """Fetch without changing the working tree; never use stale local data on failure."""
    git("fetch", "--no-tags", "origin", f"refs/heads/{BRANCH}:{REMOTE}")
    if git("branch", "--show-current").strip() != BRANCH:
        raise RuntimeError("wrong_branch: monitoring stopped until session branch restored")
    data = json.loads(git("show", f"{REMOTE}:{TELEMETRY}"))
    if not isinstance(data, dict) or data.get("protocol") != "omni.telemetry.v2":
        raise ValueError("invalid_telemetry_protocol")
    return data


def _number(value: Any) -> float | None:
    try:
        n = float(value)
        if n == n and abs(n) != float("inf"):
            return n
    except (TypeError, ValueError):
        pass
    return None


def _window_active(snapshot: dict[str, Any], now: dt.datetime) -> bool:
    times = (snapshot.get("macro_calendar") or {}).get("hard_blackout_window_utc") or []
    if len(times) != 2:
        return True  # unknown macro window: fail closed
    try:
        start, end = (dt.datetime.strptime(s, "%Y-%m-%d %H:%M:%S UTC").replace(
            tzinfo=dt.timezone.utc) for s in times)
        return start <= now < end
    except (ValueError, TypeError):
        return True


def _risk(snapshot: dict[str, Any], item: dict[str, Any]) -> float | None:
    """Conservative nominal entry-to-stop loss; broker P&L must confirm it."""
    symbol = item.get("symbol")
    asset = next((a for a in (snapshot.get("assets_matrix_24") or {}).values()
                  if a.get("symbol_broker") == symbol), None)
    if asset is None:
        return None
    contract = _number((asset.get("quotes") or {}).get("contract_size"))
    volume = _number(item.get("volume"))
    entry = _number(item.get("price_open"))
    stop = _number(item.get("sl"))
    if None in (contract, volume, entry, stop) or min(contract, volume, entry, stop) <= 0:
        return None
    direction = str(item.get("direction") or item.get("type") or "").upper()
    if "BUY" in direction or direction == "LONG":
        loss_per_contract = max(0.0, entry - stop)
    elif "SELL" in direction or direction == "SHORT":
        loss_per_contract = max(0.0, stop - entry)
    else:
        return None
    risk = volume * contract * loss_per_contract
    if str(symbol).upper().endswith("JPY.PI"):
        risk /= entry  # USD-account estimate for USDJPY; verify with broker
    return risk


def _pending_entry_wall_unconfirmed(snapshot: dict[str, Any], order: dict[str, Any], now: dt.datetime) -> bool:
    """Fail closed when a crypto limit has no persistent exchange wall at its entry.

    This is reference Binance L2, NOT broker-native L3 or proof of an entry trigger.
    A nearby wall only avoids this specific alert; it never authorizes a trade.
    """
    asset = next((a for a in (snapshot.get("assets_matrix_24") or {}).values()
                  if a.get("symbol_broker") == order.get("symbol")), None)
    if not asset or asset.get("category") != "CRYPTO":
        return False  # other-asset strategy gates cannot be verified from this feed
    side = "SELL" if "SELL_LIMIT" in str(order.get("type", "")).upper() else (
        "BUY" if "BUY_LIMIT" in str(order.get("type", "")).upper() else None)
    entry = _number(order.get("price_open"))
    atr = _number((asset.get("causal_indicators") or {}).get("atr_14"))
    book = asset.get("orderbook_live_depth") or {}
    if side is None or entry is None or atr is None or atr <= 0 or not book:
        return True
    # Legacy whale_walls_l3 held anonymous Binance aggregated L2. It cannot
    # validate a wallet-attributed persistent limit wall, even on old v2 JSON.
    if book.get("l3_provider") != "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT":
        return True
    sampled_at = _number(book.get("l3_observed_at"))
    if sampled_at is None or not 0 <= now.timestamp() - sampled_at <= 30:
        return True
    walls = book.get("l3_wallet_orders") or []
    return not any(
        str(w.get("address", "")).startswith("0x")
        and w.get("side") == side
        and (_number(w.get("notional_usd")) or 0) >= 150_000
        and (_number(w.get("persistence_sec")) or 0) >= 180
        and (price := _number(w.get("price"))) is not None
        and abs(price - entry) <= .25 * atr
        for w in walls if isinstance(w, dict))


def assess(snapshot: dict[str, Any], now: dt.datetime) -> dict[str, Any]:
    """Pure, unit-testable snapshot audit. Never returns trade instructions."""
    as_of = _number(snapshot.get("as_of_epoch"))
    age = now.timestamp() - as_of if as_of is not None else float("inf")
    account = snapshot.get("account") or {}
    balance, equity = _number(account.get("balance_usd")), _number(account.get("equity_usd"))
    positions, pending = snapshot.get("active_positions"), snapshot.get("pending_orders")
    issues: list[str] = []
    if age < -30 or age > MAX_AGE_S:
        issues.append("TELEMETRY_STALE_OR_FUTURE: no broker-state assertion is safe")
    if balance is None or equity is None or balance <= 0 or equity <= 0:
        issues.append("ACCOUNT_UNAVAILABLE: fail closed")
    if not isinstance(positions, list) or not isinstance(pending, list):
        issues.append("BOOK_UNAVAILABLE: fail closed")
        positions, pending = [], []
    if balance is not None and equity is not None:
        if min(balance, equity) < FLOOR + BUFFER:
            issues.append("FLOOR_BUFFER_BREACH: equity or balance below 4795.00")
        risks = [_risk(snapshot, x) for x in positions + pending if isinstance(x, dict)]
        if any(x is None for x in risks):
            issues.append("UNKNOWN_CONTRACT_RISK: cannot certify portfolio floor")
        elif balance - sum(risks) < FLOOR + BUFFER:
            issues.append("JOINT_STOP_BUFFER_BREACH: all filled/pending risks exceed nominal headroom")
    blackout = _window_active(snapshot, now)
    if blackout and pending:
        tickets = ",".join(str(x.get("ticket", "?")) for x in pending if isinstance(x, dict))
        issues.append(f"BLACKOUT_PENDING: tickets {tickets}; request MT5 cancellation and broker confirmation")
    if blackout and positions:
        tickets = ",".join(str(x.get("ticket", "?")) for x in positions if isinstance(x, dict))
        issues.append(f"BLACKOUT_FILLED: tickets {tickets}; human/MT5 event-hold or exit audit required")
    unconfirmed = [str(x.get("ticket", "?")) for x in pending if isinstance(x, dict)
                   and _pending_entry_wall_unconfirmed(snapshot, x, now)]
    if unconfirmed:
        issues.append("PENDING_ENTRY_WALL_UNCONFIRMED: tickets " + ",".join(unconfirmed)
                      + "; no >=$150k/180s exchange-side wall within 0.25 ATR of entry; "
                        "request native MT5 review/cancellation if gate remains unmet")
    return {"as_of_utc": snapshot.get("as_of_utc", "UNKNOWN"),
            "age_s": round(age) if math.isfinite(age) else None,
            "balance": balance, "equity": equity, "filled": len(positions),
            "pending": len(pending), "blackout": blackout, "issues": issues}


def _load_state() -> dict[str, Any]:
    try:
        return json.loads(STATE_FILE.read_text())
    except (OSError, ValueError):
        return {}


def _save_state(state: dict[str, Any]) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    temp = STATE_FILE.with_suffix(".tmp")
    temp.write_text(json.dumps(state, sort_keys=True))
    temp.replace(STATE_FILE)


def _entry(report: dict[str, Any], now: dt.datetime) -> str:
    ts = now.strftime("%Y-%m-%d %H:%M UTC")
    lines = [f"\n### [AUTOMATED READ-ONLY RISK SENTINEL] | {ts}",
             f"Source: GitHub telemetry `as_of_utc={report['as_of_utc']}` "
             f"(age {report['age_s']}s); not a direct MT5 acknowledgement.",
             f"Balance {report['balance']} USD; equity {report['equity']} USD; "
             f"filled {report['filled']}; pending {report['pending']}; "
             f"macro blackout {'ACTIVE' if report['blackout'] else 'inactive'}.",
             "**Findings:** " + ("; ".join(report["issues"]) if report["issues"] else
                                "previous alert cleared; re-confirm on MT5."),
             "No order was placed, cancelled, or closed by this monitor. "
             "Antigravity must check broker tickets and act under the agreed risk policy.\n"]
    return "\n".join(lines)


def publish(report: dict[str, Any], now: dt.datetime) -> bool:
    """Publish only material changes; never clobber a dirty checkout or force-push."""
    issues = report["issues"]
    state = _load_state()
    signature = hashlib.sha256(json.dumps(issues, sort_keys=True).encode()).hexdigest()
    if signature == state.get("signature") and now.timestamp() - state.get("last_publish", 0) < REPEAT_ALERT_S:
        return False
    if not issues and not state.get("active"):
        return False
    if git("status", "--porcelain").strip():
        raise RuntimeError("working_tree_dirty: skipped desk publishing; heartbeat continues")
    git("pull", "--ff-only", "origin", BRANCH)
    # The remote could have changed between read and pull; re-evaluate first.
    current = json.loads((ROOT / TELEMETRY).read_text())
    refreshed = assess(current, now)
    if refreshed["issues"] != issues:
        raise RuntimeError("state_changed_during_publish: re-evaluate next minute")
    with (ROOT / DESK).open("a", encoding="utf-8") as fh:
        fh.write(_entry(refreshed, now))
    git("add", "--", DESK)
    git("commit", "-m", "desk: automated read-only risk sentinel alert")
    try:
        git("push", "origin", BRANCH)
    except RuntimeError:
        # Telemetry daemon may push every minute. Rebase only if no desk conflict.
        git("fetch", "--no-tags", "origin", f"refs/heads/{BRANCH}:{REMOTE}")
        try:
            git("rebase", REMOTE)
            git("push", "origin", BRANCH)
        except RuntimeError:
            if (ROOT / ".git/rebase-merge").exists() or (ROOT / ".git/rebase-apply").exists():
                git("rebase", "--abort")
            raise RuntimeError("publish_conflict: alert remains local; no force push")
    _save_state({"signature": signature, "active": bool(issues),
                 "last_publish": now.timestamp()})
    return True


def verbose_report(snapshot: dict[str, Any], report: dict[str, Any], now: dt.datetime) -> str:
    """Human-readable minute report; screens are descriptive, not trade signals."""
    account = snapshot.get("account") or {}
    balance = report["balance"]
    headroom = round(balance - FLOOR - BUFFER, 2) if balance is not None else "UNKNOWN"
    lines = ["=" * 78,
             f"ARENA READ-ONLY MINUTE REPORT | {now:%Y-%m-%d %H:%M:%S} UTC",
             f"Snapshot: {report['as_of_utc']} | age: {report['age_s']}s | "
             f"hard blackout: {'YES' if report['blackout'] else 'no'}",
             f"Balance: {balance} | equity: {report['equity']} | "
             f"free margin: {account.get('margin_free_usd', 'UNKNOWN')} USD",
             f"Floor: {FLOOR:.2f} | required buffer: {BUFFER:.2f} | "
             f"nominal new-risk headroom: {headroom} USD",
             f"Filled: {report['filled']} | pending: {report['pending']}"]
    for kind, rows in (("FILLED", snapshot.get("active_positions") or []),
                       ("PENDING", snapshot.get("pending_orders") or [])):
        for item in rows:
            risk = _risk(snapshot, item)
            lines.append(f"  {kind} #{item.get('ticket', '?')} {item.get('symbol', '?')} "
                         f"{item.get('direction', item.get('type', '?'))} "
                         f"entry={item.get('price_open', '?')} SL={item.get('sl', '?')} "
                         f"gross-risk-estimate={round(risk, 2) if risk is not None else 'UNKNOWN'} USD "
                         f"floating={item.get('profit_usd', '?')} USD")
    lines.append("RISK FINDINGS: " + ("; ".join(report["issues"]) or "none"))
    lines.append("24-ASSET 15m OBSERVATION (price/EMA slope only; VWAP/4H confirmation "
                 "and MT5 validation still required):")
    assets = snapshot.get("assets_matrix_24") or {}
    for asset, row in assets.items():
        q, ind = row.get("quotes") or {}, row.get("causal_indicators") or {}
        bid, ema = _number(q.get("bid")), _number(ind.get("ema_200"))
        slope = _number(ind.get("ema_200_slope_3h_pct"))
        if None in (bid, ema, slope):
            label = "UNKNOWN"
        else:
            label = "BEAR?" if bid < ema and slope < 0 else (
                "BULL?" if bid > ema and slope > 0 else "CHOP?")
        cvd = row.get("cvd_1m_buckets") or []
        cvd5 = sum((_number(x.get("cvd_delta_usd")) or 0) for x in cvd[-5:])
        l2 = row.get("orderbook_live_depth") or {}
        lines.append(f"  {asset:7} {str(row.get('symbol_broker', '?')):11} {label:7} "
                     f"bid={bid} ask={q.get('ask', '?')} EMA200={ema} "
                     f"VWAP={ind.get('session_vwap_utc', '?')} "
                     f"spread={q.get('spread_price', '?')} "
                     f"CVD5={cvd5:+.0f} L2={l2.get('source', '?')}")
    lines.append("No live trading decisions, broker commands or chat messages are generated "
                 "by this log. Reconcile all alerts on MT5.")
    return "\n".join(lines + ["=" * 78])


def execute_cycle(*, do_publish: bool = False, verbose: bool = False,
                  now: dt.datetime | None = None) -> dict[str, Any]:
    now = now or dt.datetime.now(dt.timezone.utc)
    snapshot = fetch_snapshot()
    report = assess(snapshot, now)
    LOG.info("heartbeat snapshot=%s age=%ss balance=%s equity=%s filled=%s pending=%s blackout=%s findings=%s",
             report["as_of_utc"], report["age_s"], report["balance"], report["equity"],
             report["filled"], report["pending"], report["blackout"], "; ".join(report["issues"]) or "none")
    if verbose:
        print(verbose_report(snapshot, report, now), flush=True)
    if do_publish and publish(report, now):
        LOG.warning("published risk alert to %s", BRANCH)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--daemon", action="store_true", help="Repeat until stopped")
    parser.add_argument("--once", action="store_true", help="One cycle, no background process")
    parser.add_argument("--publish", action="store_true", help="Commit/push deduplicated desk alerts")
    parser.add_argument("--verbose", action="store_true", help="Print account, risk and all 24 asset readings every cycle")
    parser.add_argument("--interval", type=int, default=60, help="Heartbeat seconds (default 60)")
    args = parser.parse_args()
    if args.interval < 30:
        parser.error("minimum heartbeat interval is 30 seconds")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    while True:
        try:
            execute_cycle(do_publish=args.publish, verbose=args.verbose)
        except Exception:
            LOG.exception("Sentinel failed closed; no trade action taken")
        if not args.daemon:
            break
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
