"""Launch Headless service on port 8080 with native MT5 bridge and HMAC signing."""
import os
import sys
import asyncio
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

os.environ["EXECUTION_BACKEND"] = "native_mt5"
os.environ["OMNI_API_SECRET"] = "0b07f4298deddd67dcb505038002399023601bfed067cf48"
os.environ["OMNI_ASSETS"] = "BTC,ETH,SOL,GOLD"
os.environ["OMNI_ALLOW_PAPER"] = "0"
os.environ["MT5_ACCOUNT_ID"] = "5064568"
os.environ["OMNI_SERVICE_PORT"] = "8080"
os.environ["OMNI_SERVICE_HOST"] = "0.0.0.0"

from Terminal.Headless.__main__ import amain

if __name__ == "__main__":
    print(f"[HEADLESS] Starting OMNI Headless Server on 0.0.0.0:8080 (Account: 5064568)...")
    asyncio.run(amain())
