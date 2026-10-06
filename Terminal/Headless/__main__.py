"""Container entrypoint: ``python -m Terminal.Headless``.

Environment (see deploy/.env.example - no secret is ever hardcoded):
  OMNI_ASSETS              comma-separated canonical assets (default BTC,ETH,SOL,GOLD)
  EXECUTION_BACKEND        native_mt5 | headless_rest | paper (explicit; fail-closed)
  METAAPI_TOKEN/ACCOUNT_ID cloud gateway credentials (headless_rest)
  MT5_ACCOUNT_ID           native desktop terminal login
  OMNI_ALLOW_PAPER         1 to allow automatic paper fallback (default: off)
  OMNI_API_SECRET          HMAC secret for the signed microservice endpoints
  OMNI_SERVICE_HOST/PORT   bind address (default 0.0.0.0:8080)
  OMNI_RISK_MIN/MAX_USD    dynamic risk budget envelope (default 10 / 20)
"""
from __future__ import annotations

import asyncio
import logging
import os
import signal

from Terminal.Headless.runtime import HeadlessRuntime
from Terminal.Headless.scheduler import CandleScheduler
from Terminal.Headless.server import HeadlessService

logger = logging.getLogger("omni.headless")


async def amain():
    logging.basicConfig(level=os.environ.get("OMNI_LOG_LEVEL", "INFO"),
                        format="[%(asctime)s][%(name)s] %(message)s")
    runtime = HeadlessRuntime.from_env()
    scheduler = CandleScheduler(cadence_second=float(os.environ.get("OMNI_CADENCE_SECOND", "30")))
    service = HeadlessService(runtime,
                              host=os.environ.get("OMNI_SERVICE_HOST", "0.0.0.0"),
                              port=int(os.environ.get("OMNI_SERVICE_PORT", "8080")),
                              secret=os.environ.get("OMNI_API_SECRET") or None)
    stop = asyncio.Event()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop = asyncio.get_running_loop()
            loop.add_signal_handler(sig, stop.set)
        except (NotImplementedError, RuntimeError):   # pragma: no cover - win32
            pass
    logger.info("headless runtime starting: assets=%s bridge=%s service=%s:%s",
                ",".join(runtime.assets), getattr(runtime.bridge, "name", "n/a"),
                service.host, service.port)
    await runtime.run_forever(stop_event=stop, service=service)


if __name__ == "__main__":
    asyncio.run(amain())
