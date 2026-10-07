"""Launch Headless service on port 8080 with native MT5 bridge and HMAC signing."""
import os
import sys
import asyncio
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

os.environ["EXECUTION_BACKEND"] = "native_mt5"
# P0 forensics fix (2026-10-07): the HMAC secret was HARDCODED here in clear
# text - anyone with repo access could forge signed STAGE_ORDER / CLOSE_POSITION
# / MODIFY_SLTP commands against the laptop service. Consultation-5 invariant:
# secrets enter ONLY via environment variables. The leaked value must be
# ROTATED on both ends (it remains in git history regardless of this fix).
# Fail-closed: refuse to start the signed service without an explicit secret;
# local unsigned mode requires a deliberate opt-in.
if not os.environ.get("OMNI_API_SECRET"):
    if os.environ.get("OMNI_ALLOW_UNSIGNED_LOCAL") == "1":
        print("[HEADLESS] WARNING: OMNI_API_SECRET not set - running in LOCAL UNSIGNED mode "
              "(loopback/lab use only; the server refuses remote command endpoints without a secret).")
    else:
        raise SystemExit(
            "FAIL_CLOSED: OMNI_API_SECRET is not set. Provide it via environment variable "
            "(see deploy/.env.example). Set OMNI_ALLOW_UNSIGNED_LOCAL=1 only for isolated local runs."
        )
os.environ["OMNI_ASSETS"] = "BTC,ETH,SOL,GOLD"
os.environ["OMNI_ALLOW_PAPER"] = "0"
os.environ["MT5_ACCOUNT_ID"] = "5064568"
os.environ["OMNI_SERVICE_PORT"] = "8080"
os.environ["OMNI_SERVICE_HOST"] = "0.0.0.0"

from Terminal.Headless.__main__ import amain

if __name__ == "__main__":
    print(f"[HEADLESS] Starting OMNI Headless Server on 0.0.0.0:8080 (Account: 5064568)...")
    asyncio.run(amain())
