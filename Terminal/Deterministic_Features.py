"""Tamper-proof deterministic feature schema and cognitive attestation (Incident B).

The cognitive engine must never be the *source* of a statistic. It receives a
sealed vector of pre-computed, deterministic values produced by the
Risk_Sizing_Engine normalizers, and every numeric claim in its prose is
mechanically attested against that vector before a decision is accepted.

Components:
  * ``seal_vector`` / ``FeatureSealer``: canonical (sorted-key, 6-significant-
    digit) serialization of the feature vector, SHA-256 digested and hash-
    chained per asset (each seal commits to the previous seal's chain digest),
    so retro-active edits to journalled features are detectable.
  * ``extract_numeric_claims`` / ``attest_decision``: every number in the
    LLM's analyst/critic/rationale prose must match a value present in the
    snapshot (with rounding tolerance), otherwise the decision is rejected as
    fabricated. This is the mechanical fix for the "+1.8 sigma CVD divergence"
    hallucination that forensic querying of the raw feed disproved (+0.92).

Attestation tolerances are deliberately two-tier: statistics (|v| <= 10:
z-scores, imbalances, ratios) allow 2.5% relative error plus 0-2 decimal
rounding; magnitudes (prices, notionals) allow 0.1% relative error. Small
integer prose ordinals ("within 2 hours", "3 walls", "15-minute") are exempt
because they are not statistics. Qualitative structure claims ("empty book")
cannot be attested by numbers alone and are instead made *harmless*: the
deterministic pipeline computes exits and sizing, and the cognitive verdict is
advisory on an already-vetted candidate.
"""
from __future__ import annotations
import hashlib
import json
import math
import re

# Ordered canonical keys of the sealed econometric vector.
SEAL_KEYS = ("as_of", "signal_mid", "sigma_h", "atr", "efficiency_ratio",
             "l2_imbalance", "l2_robust_z", "aggressor_imbalance", "aggressor_robust_z",
             "wall_imbalance", "wall_imbalance_robust_z", "liquidation_delta",
             "macro_score", "confluence", "quality", "target_fuel", "opposing_magnet",
             "ffr", "friction_adjusted_fuel_ratio", "friction_bps", "risk_intent_usd")

SEAL_SCHEMA = "sealed_features.v1"


def canon_value(value):
    """Deterministic 6-significant-digit rounding; None for missing/non-finite."""
    if value is None:
        return None
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(value):
        return None
    return float(f"{value:.6g}")


def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False)


def seal_vector(values, prev_digest):
    """Seal a feature vector: canonical values + digest + per-asset chain link."""
    sealed = {k: canon_value(values.get(k)) for k in SEAL_KEYS}
    digest = hashlib.sha256(canonical_json(sealed).encode("utf-8")).hexdigest()
    chain_digest = hashlib.sha256(((prev_digest or "genesis") + digest).encode("utf-8")).hexdigest()
    return {"schema": SEAL_SCHEMA, "values": sealed, "digest": digest,
            "prev_digest": prev_digest, "chain_digest": chain_digest}


def verify_seal(sealed):
    """Recompute the digest of a sealed vector; detects any value tampering."""
    if not isinstance(sealed, dict) or sealed.get("schema") != SEAL_SCHEMA:
        return False
    try:
        recomputed = seal_vector(sealed.get("values", {}), sealed.get("prev_digest"))
    except (TypeError, ValueError):
        return False
    return recomputed["digest"] == sealed.get("digest")


class FeatureSealer:
    """Per-asset hash chain of sealed feature vectors."""

    def __init__(self, history=None):
        self.heads = {str(k): str(v) for k, v in (history or {}).items()}

    def update(self, asset, features):
        sealed = seal_vector(features or {}, self.heads.get(str(asset)))
        self.heads[str(asset)] = sealed["chain_digest"]
        return sealed

    def export(self):
        return dict(self.heads)


# --------------------------------------------------------------- attestation
_NUMBER_RE = re.compile(r"[-+]?\d+(?:[,_\s]?\d{3})*(?:\.\d+)?")
_SUFFIX_RE = re.compile(r"^\s*(k|m|bn|b)(?![a-z])", re.IGNORECASE)


def extract_numeric_claims(text):
    """Numeric literals in prose, with K/M/B suffix and percent handling."""
    claims = []
    text = text or ""
    for match in _NUMBER_RE.finditer(text):
        raw = match.group(0)
        try:
            value = float(raw.replace(",", "").replace(" ", "").replace("_", ""))
        except ValueError:
            continue
        tail = text[match.end():match.end() + 8]
        suffixed = False
        suffix_match = _SUFFIX_RE.match(tail)
        if suffix_match:
            scale = {"k": 1e3, "m": 1e6, "bn": 1e9, "b": 1e9}[suffix_match.group(1).lower()]
            value *= scale
            suffixed = True
        percent = tail.lstrip()[:1] == "%"
        if percent:
            value *= 0.01
            suffixed = True
        claims.append({"raw": raw, "value": value, "decimal": "." in raw,
                       "suffixed": suffixed, "percent": percent,
                       "context": text[max(0, match.start() - 24):match.end() + 24].strip()})
    return claims


def _claim_exempt(claim):
    """Small integer prose ordinals and time/bar counts are not statistics.

    Calendar and counting prose ("within 2 hours", "3 walls", "15-minute
    candle") is exempt by magnitude: only decimals, suffixed magnitudes
    (8.04M, 5.2%) or integers > 31 (41 bps) are treated as attestable
    statistics. This keeps the false-rejection rate near zero while catching
    fabricated z-scores, ratios, prices and notionals.
    """
    if claim["decimal"] or claim["suffixed"]:
        return False
    value = claim["value"]
    return value == int(value) and 0 <= value <= 31


def _round_variants(value):
    """Rounding variants a truthful prose citation may legitimately use.

    Statistics (|v| <= 10) may be cited to 0-2 decimals. Magnitudes (prices,
    notionals) may only be cited to 1-2 decimals: integer-rounding a
    two-decimal price ("122.00" for a wall at 122.34) is exactly the class of
    fabrication the attestation exists to catch. Notionals >= 1000 may
    additionally be cited to 1-3 significant digits ("8M" for 8.04M).
    """
    variants = set()
    for k in ((0, 1, 2) if abs(value) <= 10.0 else (1, 2)):
        variants.add(round(value, k))
    if abs(value) >= 1000.0:
        for digits in (1, 2, 3):
            try:
                variants.add(float(f"{value:.{digits}g}"))
            except (ValueError, OverflowError):
                pass
    return variants


def _matches(value, leaves):
    tolerance = 0.025 * abs(value) if abs(value) <= 10.0 else max(0.02, 0.001 * abs(value))
    for leaf in leaves:
        if leaf is None or not math.isfinite(leaf):
            continue
        if abs(value - leaf) <= max(1e-9, tolerance):
            return True
        if value in _round_variants(leaf):
            return True
    return False


def flatten_numbers(obj, out=None):
    if out is None:
        out = []
    if isinstance(obj, bool):
        return out
    if isinstance(obj, (int, float)):
        out.append(float(obj))
    elif isinstance(obj, dict):
        for value in obj.values():
            flatten_numbers(value, out)
    elif isinstance(obj, (list, tuple)):
        for value in obj:
            flatten_numbers(value, out)
    return out


def attest_decision(snapshot, decision):
    """Return (ok, violations): every statistic cited must exist in the snapshot."""
    leaves = flatten_numbers(snapshot)
    violations = []
    for field in ("analyst_thesis", "critic_objection", "rationale_summary"):
        for claim in extract_numeric_claims((decision or {}).get(field) or ""):
            if _claim_exempt(claim):
                continue
            candidates = [claim["value"]]
            if claim["percent"]:
                candidates.append(claim["value"] * 100.0)  # also accept the unscaled reading
            if not any(_matches(c, leaves) for c in candidates):
                violations.append({"field": field, "raw": claim["raw"],
                                   "value": claim["value"], "context": claim["context"]})
    return (not violations), violations
