"""Unified policy constants and mode switches for Antigravity live execution desk.
Eliminates fragmented risk caps and configures Decision Gates V3 execution mode.
"""
import os

# Decision Gates V3 Mode: 'off' | 'shadow' | 'enforce'
# 'shadow': computes all gates and logs verdicts to decisions.jsonl alongside trades
# 'enforce': hard gatekeeper; candidate must pass to be staged
DG_MODE = os.getenv("DG_MODE", "shadow")

# Single binding risk envelope
MIN_RISK_USD = 10.00
MAX_RISK_USD = 14.50
DEFAULT_RISK_CAP_USD = 14.50

# Capital floor defense invariants
HARD_FLOOR_USD = 4775.00
OPERATING_BUFFER_USD = 4795.00
MIN_FLOOR_CUSHION_USD = 20.00

# Maximum concurrent filled positions
MAX_CONCURRENT_POSITIONS = 4
MAX_RESTING_LIMITS = 5
