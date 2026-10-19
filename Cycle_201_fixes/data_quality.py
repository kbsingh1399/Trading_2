"""Cycle 201 data-quality helpers. Pure functions; no I/O.

Each function fixes one defect found in the Cycle 201 audit.
Depends on fail_closed.py in the same folder.
"""
from __future__ import annotations

import math
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple
from urllib.parse import urlsplit

try:
    from .fail_closed import NA, num, spread_bps
except ImportError:
    from fail_closed import NA, num, spread_bps

UNKNOWN = "UNKNOWN"

# ---------------------------------------------------------------- status colour
# Whole-token matching only. RED wins over AMBER, AMBER over GREEN.
_RED_TOKENS = {
    "DENIED", "BLOCKED", "REJECTED", "UNVERIFIED", "UNKNOWN", "STALE",
    "MISSING", "FAILED", "HARD FLOOR", "CRITICAL", "VIOLATION", "OFFLINE"
}
_AMBER_TOKENS = {
    "MONITORED", "STANDBY", "CALIBRATING", "ELEVATED", "WARNING", "PENDING"
}
_GREEN_TOKENS = {
    "ACTIVE", "VERIFIED", "AUTHENTICATED", "CONFIRMED", "OPEN", "SAFE",
    "NOMINAL", "COMPLIANT", "SYNCHRONIZED", "PROTECTED", "ONLINE", "HEALTHY"
}

_WORD_SPLIT = re.compile(r"[^A-Za-z0-9]+")


def status_color(val: Any) -> Optional[str]:
    """Evaluates the status string with whole-token matching and strict priority:
    RED > AMBER > GREEN.
    Returns 'RED', 'AMBER', 'GREEN', or None.
    Prevents bugs like 'DENIED_UNVERIFIED_ORDERFLOW' turning green due to 'VERIFIED'.
    """
    if val is None:
        return None
    s = str(val).upper().strip()
    if not s or s == "N/A":
        return None

    # Check whole tokens
    tokens = set(_WORD_SPLIT.split(s))
    tokens.discard("")

    # Also check multi-word tokens like "HARD FLOOR"
    if any(rt in s for rt in ["HARD FLOOR"]):
        return "RED"

    if any(t in _RED_TOKENS for t in tokens):
        return "RED"

    if any(t in _AMBER_TOKENS for t in tokens):
        return "AMBER"

    if any(t in _GREEN_TOKENS for t in tokens):
        return "GREEN"

    return None


# ---------------------------------------------------------------- time parsing (24h)
_TIME_AGO = re.compile(
    r"^(?:about\s+)?(\d+)\s*(s|sec|secs|seconds|m|min|mins|minutes|h|hr|hrs|hours|d|day|days)\s*(?:ago)?$",
    re.IGNORECASE
)


def parse_time_ago_seconds(label: Any) -> Optional[float]:
    """Parses '2h ago', '15m ago', '30s', '1 day ago' into total seconds.
    Returns None for invalid or unparseable labels.
    """
    if label is None:
        return None
    s = str(label).strip().lower()
    if not s or s == "n/a":
        return None

    m = _TIME_AGO.match(s)
    if not m:
        return None

    val = float(m.group(1))
    unit = m.group(2).lower()
    if unit.startswith("s"):
        return val
    elif unit.startswith("m") and not unit.startswith("mo"):
        return val * 60.0
    elif unit.startswith("h"):
        return val * 3600.0
    elif unit.startswith("d"):
        return val * 86400.0
    return None


def is_within_24h(label: Any, max_seconds: float = 86400.0) -> bool:
    """True if time label is within the trailing 24 hours."""
    sec = parse_time_ago_seconds(label)
    if sec is None:
        return False
    return 0.0 <= sec <= max_seconds


# ---------------------------------------------------------------- chain token parsing
_CHAIN_MAP = {
    "eth": "Ethereum", "ethereum": "Ethereum",
    "btc": "Bitcoin", "bitcoin": "Bitcoin",
    "sol": "Solana", "solana": "Solana",
    "tron": "Tron", "trx": "Tron",
    "arb": "Arbitrum", "arbitrum": "Arbitrum",
    "op": "Optimism", "optimism": "Optimism",
    "base": "Base",
    "polygon": "Polygon", "matic": "Polygon",
    "bsc": "BNB Chain", "binance": "BNB Chain", "bnb": "BNB Chain",
    "avax": "Avalanche", "avalanche": "Avalanche"
}


def parse_chain_from_url_or_text(src: Any) -> str:
    """Extracts authentic blockchain name by path/token parsing,
    avoiding naive substring bugs (e.g. 'database' matching 'base').
    """
    if not src:
        return "Unknown"
    s = str(src).strip()
    if "://" in s or "/" in s:
        try:
            parts = urlsplit(s).path.strip("/").split("/")
            # Check path components and query
            for p in parts:
                p_clean = p.lower().replace(".svg", "").replace(".png", "")
                if p_clean in _CHAIN_MAP:
                    return _CHAIN_MAP[p_clean]
        except Exception:
            pass

    # Tokenized word search
    words = [w.lower() for w in _WORD_SPLIT.split(s) if w]
    for w in words:
        if w in _CHAIN_MAP:
            return _CHAIN_MAP[w]

    return "Unknown"


# ---------------------------------------------------------------- whale percentage
def parse_whale_change_pct(val: Any) -> Optional[float]:
    """Parses whale 24h change into float decimal for Excel '0.00%' formatting.
    e.g. '0.4%' -> 0.004
         0.4    -> 0.004
         '-2.5%' -> -0.025
    Rejects malformed values. Does NOT use ambiguous x/100 thresholding.
    """
    if val is None or isinstance(val, bool):
        return None
    s = str(val).strip()
    is_pct_str = s.endswith("%")
    clean = s.replace("%", "").replace(",", "").strip()
    x = num(clean)
    if x is None:
        return None
    # In Excel, a cell formatted as 0.00% displays 0.01 as 1.00%.
    # If the input was '0.4' or '0.4%', both represent 0.4%, so the decimal value is 0.004.
    return x / 100.0


# ---------------------------------------------------------------- ratios & basis
def long_short_ratio(long_vol: Any, short_vol: Any) -> Optional[float]:
    """Calculates long/short ratio.
    Returns None if short_vol <= 0 or either volume is missing.
    Never divides by 1.0 to produce a distorted USD value.
    """
    l = num(long_vol)
    s = num(short_vol)
    if l is None or s is None or s <= 0 or l < 0:
        return None
    return l / s


def exchange_basis_bps(mark_price: Any, index_price: Any) -> Optional[float]:
    """Basis premium/discount in basis points: (mark - index) / index * 10000.
    Returns None if index_price is missing, zero, or mark_price is missing.
    Never defaults index to mark (which would falsely produce 0.0 bps).
    """
    m = num(mark_price)
    idx = num(index_price)
    if m is None or idx is None or idx <= 0:
        return None
    return (m - idx) / idx * 10000.0


# ---------------------------------------------------------------- largest holding
def extract_largest_holding(holdings: Any) -> Tuple[str, str]:
    """Finds the true largest holding by USD value / amount, rather than assuming index 0 is largest."""
    if not holdings:
        return ("", "")

    if isinstance(holdings, list) and holdings:
        # Sort by value_usd or amount
        def get_val(item: dict) -> float:
            if not isinstance(item, dict):
                return 0.0
            return num(item.get("value_usd")) or num(item.get("amount")) or 0.0

        best = max(holdings, key=get_val)
        if isinstance(best, dict):
            sym = best.get("symbol", "")
            amt = best.get("amount", "")
            val_u = best.get("value_usd", "")
            amt_str = f"{amt} ({val_u})" if amt or val_u else ""
            return (sym, amt_str)

    elif isinstance(holdings, dict) and holdings:
        def get_dict_val(item_tuple: tuple) -> float:
            v = item_tuple[1]
            if isinstance(v, dict):
                return num(v.get("usd_value")) or num(v.get("amount")) or 0.0
            return num(v) or 0.0

        best_item = max(holdings.items(), key=get_dict_val)
        sym = str(best_item[0])
        val = best_item[1]
        if isinstance(val, dict):
            amt = val.get("amount", 0)
            usd = val.get("usd_value", 0)
            return (sym, f"{amt:,.2f} ({usd:,.0f} USD)")
        return (sym, str(val))

    return ("", "")


# ---------------------------------------------------------------- deduplication
def dedup_arkham_transfers(transfers: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Deduplicates Arkham transfers by composite identity:
    (tx_hash, token_symbol, usd_value, from_address, to_address).
    """
    seen = set()
    out = []
    for t in transfers:
        tx = t.get("tx_hash", "").strip().lower()
        tok = t.get("token", "").strip().upper()
        usd = str(t.get("usd_val", "")).strip()
        fa = t.get("from_addr", "").strip().lower()
        ta = t.get("to_addr", "").strip().lower()

        # If tx_hash is present and >= 10 chars, use it + token
        key = (tx, tok, usd, fa, ta) if tx else (tok, usd, fa, ta, t.get("time_str", ""))
        if key in seen:
            continue
        seen.add(key)
        out.append(t)
    return out


# ---------------------------------------------------------------- unified whale thresholds
WHALE_THRESHOLDS = {
    "ARKHAM_MIN_USD": 100_000.0,
    "RESTING_WALL_MIN_USD": 100_000.0,
    "HYPERDASH_TIER1_USD": 40_000.0,
    "HYPERDASH_TIER2_USD": 20_000.0,
    "HYPERDASH_TIER3_USD": 5_000.0,
}
