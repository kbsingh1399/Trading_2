"""Remote command reconciler - the "Arena Brain -> laptop muscle" link
(OX_ALPHA_61 Deliverables 1 and 2).

PATHWAY SELECTION (full decision matrix in
docs/audits/OMNI_Arena_Brain_Link_20261007.md):

  PRIMARY   Pathway A - Cloudflare Tunnel (zero open router ports, sub-second
            dispatch): the laptop runs Terminal/Headless/server.py on 8080 and
            ``cloudflared tunnel`` exposes it; the Arena brain POSTs signed
            commands to /api/v1/stage_order and /api/v1/modify_sltp.
  FALLBACK  Pathway C - THIS module: the brain publishes signed command
            envelopes to any JSON store reachable by plain HTTPS GET (GitHub
            Gist raw URL, Supabase REST, Redis over HTTP); the laptop polls,
            verifies, and applies idempotently. Zero open ports by design.
  REJECTED as primary  Pathway B (MetaApi direct-to-broker REST): it hands
            cloud-side code live-money authority with none of the laptop's
            fail-closed gates (pioneer veto, exhaustion gate, governor, floor)
            - it remains available as an execution backend, never as the
            command channel.

SECURITY MODEL (both pathways share it):
  * HMAC-SHA256 over the canonical command JSON with a shared secret
    (OMNI_API_SECRET env - never hardcoded, never in the URL).
  * Timestamp window (default 30s) kills stale captures.
  * Nonce replay ledger: every accepted nonce is single-use; a replayed
    command is refused even inside the window.
  * Idempotency: ``command_id`` is single-use too - a store that re-delivers
    an old command is a no-op, not a double order.

The reconciler NEVER bypasses local risk: every applied command goes through
the same bridge contract (min lot, broker distance) with protocol-level caps
(risk <= 10.00 USD for test limits, <= 20.00 USD for generic orders,
MAX_CONCURRENT = 2 respected by refusing when 2 filled positions exist).
"""
from __future__ import annotations

import hashlib
import hmac
import json
import math
import os
import time
import urllib.request
from typing import Any, Callable, Dict, List, Optional

from Terminal.Risk_Sizing_Engine import number

PROTOCOL_VERSION = "omni.arena_remote.v1"
TEST_LIMIT_COMMENT = "ARENA:TEST_LIMIT_v1"
TEST_LIMIT_MAX_BARS = 24               # 24 x 15m = 6 hours, then auto-purge
TEST_LIMIT_RISK_CAP_USD = 10.00        # strictly <=, preserving the floor cushion
GENERIC_RISK_CAP_USD = 20.00
REPLAY_WINDOW_SEC = 30.0
COMMAND_TYPES = ("STAGE_TEST_LIMIT", "STAGE_ORDER", "MODIFY_SLTP",
                 "CANCEL_ORDER", "CLOSE_POSITION", "PURGE_TEST_LIMITS")


# --------------------------------------------------------------- signing
def _canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")


def _command_body(command: Dict) -> bytes:
    """The bytes covered by the signature: everything except the signature."""
    core = {k: v for k, v in command.items() if k != "signature"}
    return _canonical(core)


def sign_command(command: Dict, secret: str) -> Dict:
    """Attach an HMAC-SHA256 signature to a command envelope."""
    if not secret:
        raise ValueError("signing_requires_secret")
    body = _command_body(command)
    digest = hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()
    return {**command, "signature": digest}


def verify_command(command: Dict, secret: str, *, now: Optional[float] = None,
                   replay_window: float = REPLAY_WINDOW_SEC,
                   seen_nonces: Optional[set] = None,
                   applied_ids: Optional[set] = None) -> Dict:
    """Verify signature + timestamp + nonce + idempotency.

    Returns {"ok": bool, "reason": str}. ``seen_nonces``/``applied_ids`` are
    caller-owned ledgers (the reconciler and the HTTP server each keep one).
    """
    if not isinstance(command, dict):
        return {"ok": False, "reason": "not_a_dict"}
    if not secret:
        return {"ok": False, "reason": "no_secret_configured"}
    signature = str(command.get("signature", ""))
    if not signature:
        return {"ok": False, "reason": "missing_signature"}
    try:
        expected = hmac.new(secret.encode("utf-8"), _command_body(command),
                            hashlib.sha256).hexdigest()
    except (TypeError, ValueError):
        return {"ok": False, "reason": "unsignable_body"}
    if not hmac.compare_digest(expected, signature):
        return {"ok": False, "reason": "bad_signature"}
    ts = number(command.get("ts"), 0.0)
    now = float(now if now is not None else time.time())
    if not 0.0 <= now - ts <= replay_window:
        return {"ok": False, "reason": "outside_replay_window"}
    nonce = str(command.get("nonce", ""))
    if not nonce:
        return {"ok": False, "reason": "missing_nonce"}
    if seen_nonces is not None:
        if nonce in seen_nonces:
            return {"ok": False, "reason": "nonce_replayed"}
        seen_nonces.add(nonce)
    command_id = str(command.get("command_id", ""))
    if not command_id:
        return {"ok": False, "reason": "missing_command_id"}
    if applied_ids is not None and command_id in applied_ids:
        return {"ok": False, "reason": "command_already_applied"}
    if str(command.get("type", "")) not in COMMAND_TYPES:
        return {"ok": False, "reason": "unknown_command_type"}
    return {"ok": True, "reason": ""}


def new_command(type_: str, params: Dict, *, nonce: Optional[str] = None,
                ts: Optional[float] = None) -> Dict:
    """Build a fresh unsigned command envelope."""
    return {"protocol": PROTOCOL_VERSION,
            "command_id": "arena-" + hashlib.sha256(
                (f"{type_}|{nonce or os.urandom(8).hex()}|{number(ts, time.time()):.3f}")
                .encode("utf-8")).hexdigest()[:16],
            "type": str(type_), "ts": float(ts if ts is not None else time.time()),
            "nonce": str(nonce or os.urandom(16).hex()), "params": dict(params or {})}


# ------------------------------------------------------------- protocol math
def wilder_atr(bars: List[Dict], period: int = 14) -> Optional[float]:
    """Wilder-smoothed ATR over completed bars (h/l/c keys)."""
    rows = [b for b in (bars or []) if number(b.get("high")) > 0 and number(b.get("low")) > 0]
    if len(rows) < period + 1:
        return None
    trs = []
    for i in range(1, len(rows)):
        high, low = number(rows[i].get("high")), number(rows[i].get("low"))
        prev_close = number(rows[i - 1].get("close"))
        trs.append(max(high - low, abs(high - prev_close), abs(low - prev_close)))
    atr = sum(trs[:period]) / period
    for tr in trs[period:]:
        atr = (atr * (period - 1) + tr) / period
    return atr


def plan_test_limit(*, direction: str, limit_price: float, volume: float,
                    atr: float, contract_size: float = 100.0,
                    risk_cap_usd: float = TEST_LIMIT_RISK_CAP_USD,
                    tp_atr_multiple: float = 2.5):
    """Compute SL/TP for the Arena test limit and ENFORCE the risk cap.

    SL distance is 1.5 x Wilder ATR(14); TP is tp_atr_multiple x ATR. Returns
    the plan dict or raises ValueError (fail-closed) when the risk cap or the
    sanity checks fail. The ETH lesson applies to test orders too: the stop
    must be honest volatility distance, not a token offset.
    """
    direction = str(direction).upper()
    limit_price, volume, atr = float(limit_price), float(volume), float(atr)
    if direction not in ("LONG", "SHORT"):
        raise ValueError("invalid_direction")
    if limit_price <= 0 or volume <= 0:
        raise ValueError("invalid_price_or_volume")
    if atr is None or atr <= 0:
        raise ValueError("atr_unavailable")
    sl_distance = 1.5 * atr
    if direction == "LONG":
        sl, tp = limit_price - sl_distance, limit_price + tp_atr_multiple * atr
    else:
        sl, tp = limit_price + sl_distance, limit_price - tp_atr_multiple * atr
    risk_usd = volume * float(contract_size) * sl_distance
    if risk_usd > risk_cap_usd + 1e-9:
        raise ValueError(f"test_limit_risk_cap_exceeded:{risk_usd:.2f}>{risk_cap_usd:.2f}")
    if min(sl, tp, limit_price) <= 0:
        raise ValueError("non_positive_level")
    return {"direction": direction, "limit_price": limit_price, "volume": volume,
            "sl": sl, "tp": tp, "atr": atr, "risk_usd": round(risk_usd, 4),
            "risk_cap_usd": risk_cap_usd, "comment": TEST_LIMIT_COMMENT,
            "expires_after_bars": TEST_LIMIT_MAX_BARS}


def _assert_non_crossing(quote: Dict, direction: str, limit_price: float):
    """A test limit must REST, never cross: sell >= ask, buy <= bid."""
    bid, ask = number(quote.get("bid")), number(quote.get("ask"))
    if not 0 < bid < ask:
        raise ValueError("quote_unavailable")
    if direction == "SHORT" and limit_price < ask:
        raise ValueError(f"sell_limit_crosses_market:{limit_price}<ask_{ask}")
    if direction == "LONG" and limit_price > bid:
        raise ValueError(f"buy_limit_crosses_market:{limit_price}>bid_{bid}")


def _capacity_open(bridge) -> bool:
    """MAX_CONCURRENT = 2: refuse new orders at capacity (fail-closed)."""
    return len(bridge.get_open_positions()) < 2


# ------------------------------------------------------------- application
def apply_command(bridge, command: Dict, *, clock: Callable = time.time,
                  bars_provider: Optional[Callable] = None) -> Dict:
    """Apply ONE verified command through the bridge. Shared by the HTTP
    endpoints (Pathway A) and the polling reconciler (Pathway C) so both
    pathways enforce identical risk. Raises ValueError on any violation."""
    params = command.get("params") or {}
    type_ = command.get("type")
    now = float(clock())

    if type_ == "STAGE_TEST_LIMIT":
        symbol = str(params.get("symbol", ""))
        if not symbol:
            raise ValueError("missing_symbol")
        if not _capacity_open(bridge):
            raise ValueError("max_concurrent_positions_reached")
        quote = bridge.get_symbol_price(symbol)
        if not quote:
            raise ValueError("quote_unavailable")
        direction = str(params.get("direction", "SHORT")).upper()
        limit_price = float(number(params.get("limit_price"), 0.0))
        volume = float(number(params.get("volume"), 0.0))
        _assert_non_crossing(quote, direction, limit_price)
        bars = None
        if bars_provider is not None:
            try:
                bars = bars_provider(symbol)
            except Exception:                     # noqa: BLE001 - bars are best-effort
                bars = None
        atr = number(params.get("atr"), 0.0) or (wilder_atr(bars) if bars else None)
        if not atr or atr <= 0:
            raise ValueError("atr_unavailable")
        plan = plan_test_limit(direction=direction, limit_price=limit_price,
                               volume=volume, atr=atr,
                               contract_size=number(quote.get("contract_size"), 100.0))
        result = bridge.stage_limit_order(
            symbol, direction, plan["volume"], plan["limit_price"], plan["sl"], plan["tp"],
            expiration_seconds=TEST_LIMIT_MAX_BARS * 900,
            comment=TEST_LIMIT_COMMENT, magic=int(number(params.get("magic"), 100895)),
            persistent=False)
        result.update(comment=TEST_LIMIT_COMMENT, risk_usd=plan["risk_usd"],
                      sl=plan["sl"], tp=plan["tp"], atr=plan["atr"],
                      expires_at=now + TEST_LIMIT_MAX_BARS * 900,
                      staged_at=now, protocol=PROTOCOL_VERSION)
        return result

    if type_ == "STAGE_ORDER":
        symbol = str(params.get("symbol", ""))
        direction = str(params.get("direction", "")).upper()
        if not symbol or direction not in ("LONG", "SHORT"):
            raise ValueError("invalid_symbol_or_direction")
        if not _capacity_open(bridge):
            raise ValueError("max_concurrent_positions_reached")
        limit_price = float(number(params.get("limit_price"), 0.0))
        sl = float(number(params.get("sl"), 0.0))
        tp = float(number(params.get("tp"), 0.0))
        volume = float(number(params.get("volume"), 0.0))
        quote = bridge.get_symbol_price(symbol)
        if not quote:
            raise ValueError("quote_unavailable")
        _assert_non_crossing(quote, direction, limit_price)
        estimate = bridge.estimate_order(symbol, direction, limit_price, sl)
        risk_usd = volume * number(estimate.get("stop_loss_per_lot"), 0.0)
        if risk_usd > GENERIC_RISK_CAP_USD + 1e-9:
            raise ValueError(f"order_risk_cap_exceeded:{risk_usd:.2f}>"
                             f"{GENERIC_RISK_CAP_USD:.2f}")
        result = bridge.stage_limit_order(
            symbol, direction, volume, limit_price, sl, tp,
            expiration_seconds=int(number(params.get("expiration_seconds"), 3600)),
            comment=str(params.get("comment", "ARENA:ORDER")),
            magic=int(number(params.get("magic"), 100895)), persistent=False)
        result.update(risk_usd=round(risk_usd, 4), staged_at=now,
                      protocol=PROTOCOL_VERSION)
        return result

    if type_ == "MODIFY_SLTP":
        ticket = int(number(params.get("ticket"), 0))
        if ticket <= 0:
            raise ValueError("missing_ticket")
        sl = float(number(params.get("sl"), 0.0))
        tp = params.get("tp")
        return bridge.modify_position_sltp(ticket, sl,
                                           None if tp is None else float(number(tp, 0.0)))

    if type_ == "CLOSE_POSITION":
        ticket = int(number(params.get("ticket"), 0))
        if ticket <= 0:
            raise ValueError("missing_ticket")
        reason = str(params.get("reason", "brain_close"))
        result = bridge.close_position(ticket)
        result.setdefault("success", False)
        result["reason"] = reason
        return result

    if type_ == "CANCEL_ORDER":
        ticket = int(number(params.get("ticket"), 0))
        if ticket <= 0:
            raise ValueError("missing_ticket")
        return bridge.cancel_pending_order(ticket)

    if type_ == "PURGE_TEST_LIMITS":
        purged = purge_expired_test_limits(bridge, clock=clock)
        return {"success": True, "purged": purged}

    raise ValueError(f"unknown_command_type:{type_}")


def purge_expired_test_limits(bridge, *, clock: Callable = time.time,
                              max_age_sec: float = TEST_LIMIT_MAX_BARS * 900,
                              journal: Optional[Callable] = None) -> List[Dict]:
    """Auto-cancel unfilled ARENA:TEST_LIMIT_v1 orders older than 24 bars
    (6 hours). Double-guards the broker-side expiration: whichever fires
    first wins, and the second is a no-op."""
    now = float(clock())
    purged = []
    for order in bridge.get_pending_orders():
        comment = str(order.get("comment", ""))
        if not comment.startswith(TEST_LIMIT_COMMENT):
            continue
        staged_at = number(order.get("time"), 0.0)
        if staged_at <= 0:
            continue                     # unknown age: leave it to broker expiry
        if now - staged_at >= max_age_sec:
            result = bridge.cancel_pending_order(order["ticket"])
            row = {"ticket": order["ticket"], "age_sec": now - staged_at,
                   "result": result}
            purged.append(row)
            if journal is not None:
                try:
                    journal("arena_protocol.jsonl", {"time": now, "event": "test_limit_purged",
                                                     **row})
                except Exception:                     # noqa: BLE001
                    pass
    return purged


# ------------------------------------------------------------- pathway C
def gist_fetch(url: str, timeout: float = 10.0) -> List[Dict]:
    """Fetch signed command envelopes from any HTTPS JSON store (GitHub Gist
    raw URL, Supabase REST row, Redis-over-HTTP array). Pure urllib."""
    with urllib.request.urlopen(url, timeout=timeout) as response:
        body = response.read()
    payload = json.loads(body)
    if isinstance(payload, dict):
        payload = payload.get("commands") or []
    return [row for row in payload if isinstance(row, dict)]


class RemoteCommandReconciler:
    """Pathway C: poll a remote store of signed commands and apply them.

    Runs on the laptop beside the trader. Every poll: fetch -> verify
    (signature, window, nonce, idempotency) -> apply through the bridge with
    full local risk enforcement -> purge expired test limits. One dead poll
    never stops the loop; one bad command never touches the account.
    """

    def __init__(self, bridge, *, secret: str, fetch: Callable[[], List[Dict]],
                 clock: Callable = time.time, poll_interval: float = 5.0,
                 journal: Optional[Callable] = None, bars_provider: Optional[Callable] = None):
        self.bridge = bridge
        self.secret = str(secret)
        self.fetch = fetch
        self.clock = clock
        self.poll_interval = float(poll_interval)
        self.journal = journal
        self.bars_provider = bars_provider
        self.seen_nonces: set = set()
        self.applied_ids: set = set()
        self.stats = {"polls": 0, "applied": 0, "refused": 0, "errors": 0, "purged": 0}

    def poll_once(self) -> List[Dict]:
        """One reconcile cycle. Returns the results of applied commands."""
        now = self.clock()
        results = []
        try:
            commands = self.fetch() or []
        except Exception as exc:                          # noqa: BLE001 - store unreachable
            self.stats["errors"] += 1
            self._journal({"time": now, "event": "fetch_error", "error": repr(exc)})
            return results
        self.stats["polls"] += 1
        for command in commands:
            verdict = verify_command(command, self.secret, now=now,
                                     seen_nonces=self.seen_nonces,
                                     applied_ids=self.applied_ids)
            if not verdict["ok"]:
                self.stats["refused"] += 1
                self._journal({"time": now, "event": "command_refused",
                               "reason": verdict["reason"],
                               "command_id": command.get("command_id")})
                continue
            try:
                result = apply_command(self.bridge, command, clock=self.clock,
                                       bars_provider=self.bars_provider)
                self.applied_ids.add(str(command["command_id"]))
                self.stats["applied"] += 1
                results.append({"command_id": command["command_id"],
                                "type": command["type"], "result": result})
                self._journal({"time": now, "event": "command_applied",
                               "command_id": command["command_id"],
                               "type": command["type"], "result": result})
            except Exception as exc:                      # noqa: BLE001 - command isolation
                self.stats["errors"] += 1
                self._journal({"time": now, "event": "apply_error",
                               "command_id": command.get("command_id"),
                               "error": repr(exc)})
        try:
            purged = purge_expired_test_limits(self.bridge, clock=self.clock)
            if purged:
                self.stats["purged"] += len(purged)
        except Exception:                                 # noqa: BLE001 - purge isolation
            pass
        return results

    def run_forever(self, *, stop=None, sleep=time.sleep):
        """Blocking poll loop (the laptop side); injectable sleep for tests."""
        while stop is None or not stop.is_set():
            self.poll_once()
            sleep(self.poll_interval)

    def _journal(self, record: Dict):
        if self.journal is not None:
            try:
                self.journal("arena_protocol.jsonl", record)
            except Exception:                             # noqa: BLE001
                pass


# ------------------------------------------------------------- laptop CLI
def reconciler_from_env(*, bridge=None, environ=None):
    """Build the Pathway-C fallback reconciler from the environment.

    Env (see deploy/.env.example):
      ARENA_COMMANDS_URL   HTTPS JSON store of signed commands (gist raw /
                           Supabase REST / Redis-over-HTTP)
      OMNI_API_SECRET      the shared HMAC secret (required)
      ARENA_POLL_INTERVAL  poll cadence seconds (default 5)
      EXECUTION_BACKEND / OMNI_ALLOW_PAPER / MT5_ACCOUNT_ID govern the
      fail-closed bridge discovery exactly as in Terminal.Headless.
    """
    env = dict(environ if environ is not None else os.environ)
    url = env.get("ARENA_COMMANDS_URL", "").strip()
    secret = env.get("OMNI_API_SECRET", "").strip()
    if not url or not secret:
        raise ValueError("reconciler_requires:ARENA_COMMANDS_URL+OMNI_API_SECRET")
    if bridge is None:
        from Terminal.Execution import create_bridge
        bridge = create_bridge()          # fail-closed: no healthy backend, no trading
    interval = number(env.get("ARENA_POLL_INTERVAL"), 5.0)
    return RemoteCommandReconciler(bridge, secret=secret,
                                   fetch=lambda: gist_fetch(url),
                                   poll_interval=max(1.0, float(interval)))


def _main(argv=None):
    """Laptop-side Pathway C entrypoint:

        python -m Terminal.Execution.remote_reconciler

    Runs until SIGINT/SIGTERM: poll -> verify -> apply (full local risk) ->
    purge expired test limits. Zero open ports; outbound HTTPS only."""
    import argparse
    import signal
    import threading

    parser = argparse.ArgumentParser(description="Arena Brain Pathway-C reconciler "
                                                 "(laptop muscle side)")
    parser.add_argument("--url", default=os.environ.get("ARENA_COMMANDS_URL", ""),
                        help="HTTPS JSON store of signed commands")
    parser.add_argument("--secret", default=os.environ.get("OMNI_API_SECRET", ""))
    parser.add_argument("--interval", type=float,
                        default=float(os.environ.get("ARENA_POLL_INTERVAL", "5") or 5))
    args = parser.parse_args(argv)
    environ = dict(os.environ)
    if args.url:
        environ["ARENA_COMMANDS_URL"] = args.url
    if args.secret:
        environ["OMNI_API_SECRET"] = args.secret
    environ["ARENA_POLL_INTERVAL"] = str(args.interval)
    reconciler = reconciler_from_env(environ=environ)
    stop = threading.Event()

    def _signal(_sig, _frame):
        stop.set()

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            signal.signal(sig, _signal)
        except (ValueError, OSError):              # pragma: no cover - non-main thread
            pass
    print(f"[arena-reconciler] polling {environ['ARENA_COMMANDS_URL']} every "
          f"{reconciler.poll_interval:.0f}s until SIGINT", flush=True)
    reconciler.run_forever(stop=stop)
    print(f"[arena-reconciler] stopped: {reconciler.stats}", flush=True)


if __name__ == "__main__":
    _main()
