"""Terminal/risk/blackout_guard.py
======================================
P0 FIX — Pre-submission macro blackout guard.

INCIDENT PREVENTION:
  SOL ticket #18648927 was staged at 17:05 UTC inside a 17:00-18:30 UTC
  FOMC hard blackout. This guard wraps native mt5.order_send calls from
  the bridge; other execution transports require their own receiving veto.

USAGE:
  Replace: result = mt5.order_send(request)
  With:    result = safe_order_send(request)       # raises on blackout
  Or:      result = safe_order_send(request, raise_on_block=False)  # returns dict

  The native bridge installs the MetaTrader5 module wrapper at import time.
  The remote reconciler independently checks the calendar before calling
  headless/MetaApi transports, which do not use this native wrapper.
"""
from __future__ import annotations

import json
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

logger = logging.getLogger("BlackoutGuard")

# ---------------------------------------------------------------------------
# Calendar source — preloaded static events + dynamic JSON file
# ---------------------------------------------------------------------------
_CALENDAR_JSON = Path(__file__).resolve().parents[2] / "Data" / "macro_calendar.json"

# Default ±35-minute blackout for ordinary HIGH-impact events. Explicit
# calendar windows (and a pre-event purge cutoff) override this for FOMC.
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
        self._calendar_error = "calendar_unavailable"
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
        try:
            mtime = _CALENDAR_JSON.stat().st_mtime
            if mtime == self._calendar_mtime and not self._calendar_error:
                return
            data = json.loads(_CALENDAR_JSON.read_text(encoding="utf-8"))
            events = [e for e in data["events"] if e.get("impact") == "HIGH"]
            if not events:
                raise ValueError("no HIGH-impact events")
            # Never keep an old, apparently valid calendar after a bad refresh.
            self._events = events
            self._calendar_mtime = mtime
            self._calendar_error = ""
            logger.info("BlackoutGuard: loaded %d HIGH-impact events.", len(events))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            self._calendar_error = f"macro_calendar_unavailable:{exc}"
            logger.error("BlackoutGuard: %s; blocking new orders", self._calendar_error)

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
        if self._calendar_error:
            return True, self._calendar_error
        now = dt or datetime.now(timezone.utc)
        if now.tzinfo is None:
            return True, "naive_datetime_not_utc"
        for event in self._events:
            try:
                def parse(value):
                    return datetime.fromisoformat(value.replace("Z", "+00:00"))

                event_dt = parse(event["time_utc"])
                window_start = parse(event["blackout_start_utc"]) if event.get("blackout_start_utc") else event_dt - timedelta(minutes=_STATIC_BLACKOUT_MINUTES_PRE)
                window_end = parse(event["blackout_end_utc"]) if event.get("blackout_end_utc") else event_dt + timedelta(minutes=_STATIC_BLACKOUT_MINUTES_POST)
                # Pre-event purge is a separate operator task, but absolutely
                # no replacement entry may be sent after its deadline.
                if event.get("purge_at_utc"):
                    window_start = min(window_start, parse(event["purge_at_utc"]))
                if window_end <= window_start:
                    raise ValueError("inverted blackout window")
                if window_start <= now < window_end:
                    name = event.get("name", "MACRO_EVENT")
                    return True, f"{name} blackout: window {window_start:%H:%M}-{window_end:%H:%M} UTC"
            except (KeyError, TypeError, ValueError) as exc:
                return True, f"invalid_macro_event:{exc}"
        return False, ""

    # ------------------------------------------------------------------
    # Patching helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _is_verified_close(request: dict, mt5) -> bool:
        """Only allow a genuine, non-increasing position close in blackout."""
        if request.get("action") != getattr(mt5, "TRADE_ACTION_DEAL", 1):
            return False
        ticket = request.get("position")
        if not ticket:
            return False
        try:
            positions = mt5.positions_get(ticket=int(ticket))
            if positions is None or len(positions) != 1:
                return False
            position = positions[0]
            volume = float(request.get("volume", 0))
            return (request.get("symbol") == position.symbol
                    and 0 < volume <= float(position.volume)
                    and request.get("type") == (
                        mt5.ORDER_TYPE_SELL if position.type == mt5.ORDER_TYPE_BUY
                        else mt5.ORDER_TYPE_BUY))
        except (AttributeError, TypeError, ValueError):
            return False

    @classmethod
    def install(cls) -> bool:
        """Patch the MT5 module directly; never import the partially loaded bridge.

        Missing MT5, a broken calendar or a non-writable order_send is a hard
        failure. Return True only after verifying that the guard is installed.
        """
        import MetaTrader5 as mt5_raw

        current = mt5_raw.order_send
        if getattr(current, "_omni_blackout_guard", False):
            return True
        if not callable(current):
            raise RuntimeError("MT5 order_send is not callable")
        guard = cls.get()

        def guarded_order_send(request: dict):
            action = request.get("action", -1)
            if action not in (getattr(mt5_raw, "TRADE_ACTION_SLTP", 6),
                              getattr(mt5_raw, "TRADE_ACTION_REMOVE", 8)):
                blocked, reason = guard.is_blocked()
                if blocked and not cls._is_verified_close(request, mt5_raw):
                    logger.error("ORDER BLOCKED — %s", reason)
                    return SimpleNamespace(retcode=10036, comment=f"ORDER BLOCKED — {reason}",
                                           order=0, deal=0, price=0.0)
            return current(request)

        guarded_order_send._omni_blackout_guard = True
        mt5_raw.order_send = guarded_order_send
        if mt5_raw.order_send is not guarded_order_send:
            raise RuntimeError("MT5 order_send guard installation failed")
        logger.info("BlackoutGuard installed on MT5.order_send")
        return True


# ---------------------------------------------------------------------------
# Module-level convenience functions
# ---------------------------------------------------------------------------
_guard = BlackoutGuard.get()


def is_in_blackout(dt: Optional[datetime] = None) -> tuple[bool, str]:
    """Check if the current (or given) UTC time is inside a macro blackout."""
    return _guard.is_blocked(dt)


def safe_order_send(request: dict, *, raise_on_block: bool = True):
    """Fail closed on guard installation failure; never bypass the patch."""
    try:
        BlackoutGuard.install()
        import MetaTrader5 as mt5
    except (ImportError, RuntimeError, AttributeError) as exc:
        raise RuntimeError(f"MT5 blackout guard unavailable: {exc}") from exc
    result = mt5.order_send(request)
    if getattr(result, "retcode", None) == 10036 and str(getattr(result, "comment", "")).startswith("ORDER BLOCKED"):
        if raise_on_block:
            raise RuntimeError(result.comment)
        return {"success": False, "error": result.comment, "blocked": True}
    return result
