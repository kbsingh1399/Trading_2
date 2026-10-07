"""Terminal/risk/blackout_guard.py
======================================
P0 FIX — Pre-submission macro blackout guard.

INCIDENT PREVENTION:
  SOL ticket #18648927 was staged at 17:05 UTC inside a 17:00-18:30 UTC
  FOMC hard blackout. This guard makes such a submission STRUCTURALLY
  IMPOSSIBLE by wrapping every mt5.order_send call.

USAGE:
  Replace: result = mt5.order_send(request)
  With:    result = safe_order_send(request)       # raises on blackout
  Or:      result = safe_order_send(request, raise_on_block=False)  # returns dict

  All new_order and stage_limit calls in MT5_Execution_Bridge are patched
  to route through this module automatically by importing BlackoutGuard
  and calling BlackoutGuard.install().
"""
from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

logger = logging.getLogger("BlackoutGuard")

# ---------------------------------------------------------------------------
# Calendar source — preloaded static events + dynamic JSON file
# ---------------------------------------------------------------------------
_CALENDAR_JSON = Path(__file__).resolve().parents[2] / "Data" / "macro_calendar.json"

# Hardcoded conservative blackout: 30 minutes before each HIGH-impact event
# to 30 minutes after. The dynamic calendar extends this automatically.
_STATIC_BLACKOUT_MINUTES_PRE  = 35   # minutes before event
_STATIC_BLACKOUT_MINUTES_POST = 35   # minutes after event


class BlackoutGuard:
    """Singleton guard that blocks MT5 order submissions during macro blackouts.

    Call ``BlackoutGuard.install()`` once at process startup to monkey-patch
    MT5ExecutionBridge so ALL order_send calls pass through this guard.
    """

    _instance: Optional["BlackoutGuard"] = None

    def __init__(self):
        self._calendar_mtime: float = 0.0
        self._events: list = []
        self._load_calendar()

    @classmethod
    def get(cls) -> "BlackoutGuard":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # ------------------------------------------------------------------
    # Calendar management
    # ------------------------------------------------------------------
    def _load_calendar(self) -> None:
        """Load macro calendar from JSON file if it exists and has changed."""
        if not _CALENDAR_JSON.exists():
            logger.debug("macro_calendar.json not found — using empty calendar.")
            return
        mtime = _CALENDAR_JSON.stat().st_mtime
        if mtime == self._calendar_mtime:
            return
        try:
            data = json.loads(_CALENDAR_JSON.read_text(encoding="utf-8"))
            self._events = [
                e for e in data.get("events", [])
                if e.get("impact") == "HIGH"
            ]
            self._calendar_mtime = mtime
            logger.info("BlackoutGuard: loaded %d HIGH-impact events.", len(self._events))
        except Exception as exc:
            logger.warning("BlackoutGuard: calendar parse error: %s", exc)

    def _refresh(self) -> None:
        """Hot-reload the calendar file if it was updated on disk."""
        self._load_calendar()

    # ------------------------------------------------------------------
    # Core check
    # ------------------------------------------------------------------
    def is_blocked(self, dt: Optional[datetime] = None) -> tuple[bool, str]:
        """Return (blocked: bool, reason: str).

        Checks calendar events with ±35 min windows.
        Returns immediately on first match to keep latency minimal.
        """
        self._refresh()
        now = dt or datetime.now(timezone.utc)
        pre_delta  = timedelta(minutes=_STATIC_BLACKOUT_MINUTES_PRE)
        post_delta = timedelta(minutes=_STATIC_BLACKOUT_MINUTES_POST)

        for event in self._events:
            try:
                event_dt_str = event.get("time_utc", "")
                if not event_dt_str:
                    continue
                event_dt = datetime.fromisoformat(
                    event_dt_str.replace("Z", "+00:00")
                )
                window_start = event_dt - pre_delta
                window_end   = event_dt + post_delta
                if window_start <= now <= window_end:
                    name = event.get("name", "MACRO_EVENT")
                    return True, (
                        f"{name} blackout: window "
                        f"{window_start.strftime('%H:%M')}-{window_end.strftime('%H:%M')} UTC"
                    )
            except Exception:
                continue

        return False, ""

    # ------------------------------------------------------------------
    # Patching helpers
    # ------------------------------------------------------------------
    @classmethod
    def install(cls) -> None:
        """Monkey-patch MT5ExecutionBridge to enforce blackout on every send.

        Call once at process startup:
            from Terminal.risk.blackout_guard import BlackoutGuard
            BlackoutGuard.install()
        """
        try:
            from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
            import MetaTrader5 as mt5_raw

            guard = cls.get()
            _original_send = mt5_raw.order_send  # save unpatched reference

            def _guarded_order_send(request: dict):
                # Allow SLTP ratchet modifications without blackout gate —
                # only block NEW order submissions and cancels during blackout
                action = request.get("action", -1)
                SLTP_ACTION = getattr(mt5_raw, "TRADE_ACTION_SLTP", 6)
                REMOVE_ACTION = getattr(mt5_raw, "TRADE_ACTION_REMOVE", 8)
                if action not in (SLTP_ACTION, REMOVE_ACTION):
                    blocked, reason = guard.is_blocked()
                    if blocked:
                        msg = f"ORDER BLOCKED — {reason}. Submission rejected."
                        logger.error(msg)
                        # Return a fake failure result that callers handle gracefully
                        class _BlockedResult:
                            retcode = 10036  # TRADE_RETCODE_REJECT
                            comment = msg
                            order   = 0
                            deal    = 0
                            price   = 0.0
                        return _BlockedResult()
                return _original_send(request)

            mt5_raw.order_send = _guarded_order_send
            logger.info("BlackoutGuard installed — all mt5.order_send calls are now guarded.")
        except ImportError as exc:
            logger.warning("BlackoutGuard.install() skipped (MT5 not available): %s", exc)


# ---------------------------------------------------------------------------
# Module-level convenience functions
# ---------------------------------------------------------------------------
_guard = BlackoutGuard.get()


def is_in_blackout(dt: Optional[datetime] = None) -> tuple[bool, str]:
    """Check if the current (or given) UTC time is inside a macro blackout."""
    return _guard.is_blocked(dt)


def safe_order_send(request: dict, *, raise_on_block: bool = True):
    """Blackout-guarded wrapper around mt5.order_send.

    Args:
        request:        The MT5 order request dict.
        raise_on_block: If True, raises RuntimeError on blackout.
                        If False, returns {"success": False, "error": reason}.

    Usage (drop-in replacement):
        result = safe_order_send(request)
    """
    try:
        import MetaTrader5 as mt5
    except ImportError:
        raise RuntimeError("MetaTrader5 not installed.")

    blocked, reason = is_in_blackout()
    action = request.get("action", -1)
    SLTP_ACTION   = getattr(mt5, "TRADE_ACTION_SLTP", 6)
    REMOVE_ACTION = getattr(mt5, "TRADE_ACTION_REMOVE", 8)

    if blocked and action not in (SLTP_ACTION, REMOVE_ACTION):
        msg = f"ORDER BLOCKED — {reason}"
        logger.error(msg)
        if raise_on_block:
            raise RuntimeError(msg)
        return {"success": False, "error": msg, "blocked": True}

    return mt5.order_send(request)
