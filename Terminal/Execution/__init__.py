"""Polymorphic execution backends: native MT5, headless cloud REST, paper.

    from Terminal.Execution import create_bridge
    bridge = create_bridge()          # fail-closed auto-discovery

Or explicitly (never silently falls back):

    EXECUTION_BACKEND=headless_rest python -m Terminal.Headless
"""
from Terminal.Execution.base import (BaseExecutionBridge, BridgeError,
                                     NoExecutionBackend, create_bridge,
                                     register_backend, available_backends)
from Terminal.Execution.native_mt5 import NativeMT5Bridge
from Terminal.Execution.headless_rest import HeadlessRESTBridge
from Terminal.Execution.paper import PaperSimulatedBridge

__all__ = ["BaseExecutionBridge", "BridgeError", "NoExecutionBackend",
           "create_bridge", "register_backend", "available_backends",
           "NativeMT5Bridge", "HeadlessRESTBridge", "PaperSimulatedBridge"]
