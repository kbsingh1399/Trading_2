"""Cycle 201 round-2 corrections. Pure functions; no I/O.

Replaces four scorecard fixes that would re-introduce defects:
  * quote age defaulted to 0.5 s (fabricated freshness);
  * orderbook spread freshness relaxed to 60 s (contradicts the 5 s gate);
  * INACTIVE / UNKNOWN colours claimed without a defined rule;
  * a sheet-count check cannot detect a renamed or missing sheet.
Depends on fail_closed.py and data_quality.py in this folder.
"""
from __future__ import annotations

from typing import Iterable, Optional, Tuple

try:
    from .fail_closed import num, spread_bps
    from .data_quality import quote_or_na, age_hours
except ImportError:  # run as plain script / tests
    from fail_closed import num, spread_bps
    from data_quality import quote_or_na, age_hours

FRESHNESS_MAX_S = 5.0  # must match fail_closed.spread_bps default and SOP step S4


def quote_age_or_none(v) -> Optional[float]:
    """Age in seconds, or None. No default: a missing age is never fresh."""
    x = num(v)
    return x if (x is not None and x >= 0) else None


def execution_status(bid, ask, quote_age_s) -> Tuple[str, str]:
    """Return (status, colour). A missing or stale age can never be ACTIVE."""
    b, a = quote_or_na(bid), quote_or_na(ask)
    if b is None or a is None:
        return "MISSING QUOTE", "RED"
    if a <= b:
        return "INACTIVE", "AMBER"            # crossed book
    age = quote_age_or_none(quote_age_s)
    if age is None or age > FRESHNESS_MAX_S:
        return "INACTIVE", "AMBER"            # stale or unknown age
    return "ACTIVE EXECUTION", "GREEN"


def orderbook_spread(bid, ask, quote_age_s) -> Optional[float]:
    """Mid-based spread bps with the 5 s freshness gate. No relaxation."""
    return spread_bps(bid, ask, quote_age_or_none(quote_age_s), max_age_s=FRESHNESS_MAX_S)


def within_window(label, window_h: float = 24.0) -> bool:
    """True only if the label parses and is within the window.

    'just now' and 'now' count as age 0. Unparseable labels return False,
    but the caller must count them as rejected rather than dropping them.
    """
    if label is not None and str(label).strip().lower() in ("just now", "now"):
        return True
    a = age_hours(label)
    return a is not None and a <= window_h


_BASE58_ALPHABET = set("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")
_HEX_ALPHABET = set("0123456789abcdefABCDEF")


def is_valid_tx_hash(tx: str) -> bool:
    """Validates EVM (66-char 0x hex), BTC/Tron (64-char hex), or Solana (64-88 base58)."""
    if not tx:
        return False
    if tx.startswith(("0x", "0X")):
        return len(tx) == 66 and all(c in _HEX_ALPHABET for c in tx[2:])
    if len(tx) == 64 and all(c in _HEX_ALPHABET for c in tx):
        return True  # 64-char BTC or Tron raw hex
    if 64 <= len(tx) <= 88 and all(c in _BASE58_ALPHABET for c in tx):
        return True  # Solana base58 signature
    return False


def canonical_tx(raw: str) -> str:
    """Canonicalises on-chain transaction hashes.
    0x-prefixed EVM hex is lowercased.
    64-char raw hex (BTC/Tron) is lowercased.
    Base58 (Solana) is case-sensitive and preserved without lowercasing.
    """
    if raw[:2] in ("0x", "0X"):
        return raw.lower()
    if len(raw) == 64 and all(c in _HEX_ALPHABET for c in raw):
        return raw.lower()
    return raw  # base58 (Solana): case-sensitive, never lowercased


def harvest_key(t: dict, harvest_epoch: float = 0.0) -> Optional[tuple]:
    """Key on the on-chain identity. The time label is not part of the key.

    Returns None when there is no full transaction hash; such rows must be
    flagged for review, not deduplicated on weaker fields.
    Accommodates 66-char EVM hex (0x...), 64-char BTC/Tron hex, and base58 Solana.
    Includes log_index / event_index to distinguish multiple transfers within one tx.
    """
    raw_tx = str(t.get("tx_hash", "")).strip()
    if not is_valid_tx_hash(raw_tx):
        return None
    tx = canonical_tx(raw_tx)
    s = lambda k: str(t.get(k, "")).strip().lower()  # noqa: E731
    log_idx = str(t.get("log_index") if t.get("log_index") is not None else (t.get("event_index") if t.get("event_index") is not None else (t.get("idx") if t.get("idx") is not None else ""))).strip()
    return (tx, s("from_address"), s("to_address"), s("token_symbol"),
            s("token_value"), s("usd_value"), log_idx)


def sheet_guard(actual: Iterable[str], required: Iterable[str]) -> Tuple[list, list]:
    """Return (missing, unexpected) sheet names.

    Missing sheets are a hard failure. Unexpected sheets are a warning. The
    required list must come from the specification, not from a single run.
    """
    act = set(actual)
    req = list(required)
    missing = [r for r in req if r not in act]
    unexpected = sorted(act - set(req))
    return missing, unexpected
