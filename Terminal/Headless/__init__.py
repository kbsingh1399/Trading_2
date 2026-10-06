"""Headless cloud execution package (OX_ALPHA_60).

  python -m Terminal.Headless    # 24/7 container entrypoint

Composition: ZeroCostDataFactory (continuous data) + RealtimeRunner (refresh
heartbeat) + CrossSourceValidator (sealed quality) + PioneerDecisionEngine
(veto-only conviction) + a Terminal/Execution bridge (native MT5 / cloud
REST / paper) + CandleScheduler (:14/:29/:44/:59 wakes) + HeadlessService
(signed /healthz /readyz /api/v1/evaluate_candle).
"""
from Terminal.Headless.runtime import HeadlessRuntime, SERVICE_VERSION
from Terminal.Headless.scheduler import CandleScheduler
from Terminal.Headless.server import HeadlessService, sign_payload, verify_signed
from Terminal.Headless.llm_contract import (build_consultation_request,
                                            validate_consultation_response,
                                            default_invariant_envelope,
                                            invariant_digest, CONTRACT_VERSION)

__all__ = ["HeadlessRuntime", "HeadlessService", "CandleScheduler", "SERVICE_VERSION",
           "sign_payload", "verify_signed", "build_consultation_request",
           "validate_consultation_response", "default_invariant_envelope",
           "invariant_digest", "CONTRACT_VERSION"]
