#!/usr/bin/env python3
"""Terminal/risk/autonomous_ratchet_daemon.py
================================================
Continuous autonomous ratchet & trade-lifecycle manager daemon.
Polls active MetaTrader 5 positions every 15 seconds to enforce:
  - Phase 0 (BE Lock):    At +0.80R gain -> move SL to Entry + 0.15R (locking spread/friction)
  - Phase 1 (Profit Lock):At +1.50R gain -> move SL to Entry + 0.80R
  - Phase 2 (Trail):      At +2.00R gain -> trail SL to Entry + 1.50R
  - Time-Decay Exit:      Exit at market if < +0.20R gain after 24 bars (6 hours)
"""
from __future__ import annotations

import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][RatchetDaemon] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("RatchetDaemon")

def main():
    logger.info("Initializing Autonomous Ratchet Daemon...")
    
    # Import bridge & ratchet manager
    try:
        from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
        from Terminal.risk.ratchet_manager import RatchetManager
    except ImportError as exc:
        logger.error(f"Failed to import MT5 bridge or RatchetManager: {exc}")
        sys.exit(1)

    bridge = MT5ExecutionBridge()
    if not bridge.ensure_connected():
        logger.error("Failed to connect MT5ExecutionBridge at startup.")
        sys.exit(1)

    rm = RatchetManager(bridge)
    journal_path = Path("Data/ratchet_actions.jsonl")
    journal_path.parent.mkdir(parents=True, exist_ok=True)

    poll_interval = 15  # seconds
    logger.info(f"Ratchet Daemon started. Monitoring open positions every {poll_interval}s...")

    last_heartbeat = 0

    while True:
        try:
            now = time.time()
            if now - last_heartbeat >= 300:
                pos_count = len(rm._positions)
                logger.info(f"Heartbeat: Ratchet daemon healthy. Active managed tickets: {pos_count} ({list(rm._positions.keys())})")
                last_heartbeat = now

            actions = rm.run_once()
            if actions:
                for action in actions:
                    logger.info(f"RATCHET EVENT: {action}")
                    entry = {
                        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                        **action
                    }
                    with open(journal_path, "a", encoding="utf-8") as f:
                        f.write(json.dumps(entry) + "\n")

        except Exception as exc:
            logger.error(f"Error in ratchet daemon loop: {exc}", exc_info=True)

        time.sleep(poll_interval)

if __name__ == "__main__":
    main()
