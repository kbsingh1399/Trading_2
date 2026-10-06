"""Backend A: the native Windows MetaTrader 5 desktop IPC bridge.

This is the existing, battle-tested ``MT5ExecutionBridge`` from
``Terminal/MT5_Execution_Bridge.py`` - unchanged. The subclass only adds the
``BaseExecutionBridge`` contract (so the polymorphic registry can probe it)
and a health() override that re-asserts terminal connectivity.

MRO note: the concrete implementation must precede the ABC so MT5's real
methods (not the ABC's abstract stubs) win attribute resolution.
"""
from __future__ import annotations

from typing import Dict

from Terminal.Execution.base import BaseExecutionBridge
from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge


class NativeMT5Bridge(MT5ExecutionBridge, BaseExecutionBridge):
    """Windows desktop IPC: terminal64.exe named-pipe transport."""

    name = "native_mt5"

    def health(self) -> Dict:
        try:
            connected = bool(self.ensure_connected())
            summary = self.get_account_summary() if connected else {}
            return {"healthy": connected and bool(summary.get("connected")),
                    "backend": self.name,
                    "login": summary.get("login"),
                    "detail": "" if connected else "terminal_unreachable"}
        except Exception as exc:                      # noqa: BLE001 - probe isolation
            return {"healthy": False, "backend": self.name, "detail": repr(exc)}

    def cancel_order(self, order_ticket: int) -> Dict:
        return self.cancel_pending_order(order_ticket)
