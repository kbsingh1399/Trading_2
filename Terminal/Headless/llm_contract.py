"""Deterministic LLM consultation contract for headless candle-close reasoning.

Zero-hallucination by construction - the LLM cannot introduce numbers, only
SELECT or HOLD a candidate that the deterministic engine already sized:

  * The REQUEST embeds the full invariant envelope (hard floor, risk budget,
    41 bps friction, MAX_CONCURRENT, the 3-phase ratchet table) plus its
    SHA-256 ``invariant_digest`` and the sealed feature/pioneer digests.
  * The RESPONSE must echo ``invariant_digest`` unchanged and must echo the
    candidate's pre-computed sl/tp/risk_usd EXACTLY. Any deviation - a
    "better" stop, a bigger risk, a moved target - is a violation and the
    response is rejected. The ratchet math stays on our side of the wall.
  * ``support_refs``/``invalidation_refs`` must be JSON pointers that resolve
    inside the request snapshot (same discipline as CognitiveEngine).
  * HOLD must be silent on candidate specifics; SELECT must name the exact
    candidate the deterministic pipeline proposed.

This complements (does not replace) ``CognitiveEngine``: same ledger, same
attestation philosophy, tightened for the cloud where the model endpoint is
remote and untrusted.
"""
from __future__ import annotations

import hashlib
import json
from typing import List, Optional, Tuple

from Terminal.Risk_Sizing_Engine import number

CONTRACT_VERSION = "omni.headless.llm_contract.v1"

RESPONSE_REQUIRED_KEYS = {"action", "candidate_id", "risk_usd", "sl", "tp",
                          "rationale_summary", "support_refs", "invalidation_refs",
                          "invariant_digest"}

MAX_RATIONALE_CHARS = 600
MAX_REFS = 5


def _canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")


def invariant_digest(envelope: dict) -> str:
    """Stable digest of the invariant envelope the response must echo."""
    return hashlib.sha256(_canonical(envelope)).hexdigest()


def default_invariant_envelope(*, risk_min_usd: float = 10.0, risk_max_usd: float = 20.0) -> dict:
    """The production invariant set (see Uplift_Model.RATCHET_BASE for the
    3-phase piecewise ratchet: 0.80R->0.35R, 1.50R->0.85R, 2.00R trail 0.65R,
    target 2.50R max 2.75R)."""
    from Terminal.Uplift_Model import RATCHET_BASE
    return {"hard_floor_usd": 4775.0,
            "initial_capital_usd": 5000.0,
            "max_drawdown_pct": 4.50,
            "risk_min_usd": float(risk_min_usd),
            "risk_max_usd": float(risk_max_usd),
            "friction_bps_round_trip": 41.0,
            "max_concurrent_filled": 2,
            "max_resting_limits": 5,
            "ratchet": dict(RATCHET_BASE),
            "policy_version": CONTRACT_VERSION}


def build_consultation_request(*, as_of: float, asset: str, features: dict,
                               pioneer: Optional[dict], candidate: dict,
                               envelope: Optional[dict] = None) -> dict:
    """The structured prompt payload sent at candle close."""
    envelope = envelope or default_invariant_envelope(
        risk_min_usd=number((candidate.get("sizing") or {}).get("risk_usd"), 10.0),
        risk_max_usd=max(20.0, number((candidate.get("sizing") or {}).get("risk_usd"), 20.0)))
    request = {"contract_version": CONTRACT_VERSION,
               "as_of": float(as_of), "asset": str(asset).upper(),
               "sealed_features": {"vector": features, "digest": features.get("pioneer", {}).get("digest")},
               "pioneer_advisory": pioneer,
               "candidate": {"candidate_id": candidate.get("candidate_id"),
                             "direction": candidate.get("direction"),
                             "entry": number(candidate.get("price_open")),
                             "sl": number(candidate.get("sl")),
                             "tp": number(candidate.get("tp")),
                             "hurdle_r": number(candidate.get("hurdle_r")),
                             "risk_usd": number((candidate.get("sizing") or {}).get(
                                 "risk_usd", candidate.get("risk_usd")))},
               "invariant_envelope": envelope,
               "invariant_digest": invariant_digest(envelope),
               "response_schema": {"required": sorted(RESPONSE_REQUIRED_KEYS),
                                   "action": ["SELECT", "HOLD"],
                                   "note": "sl/tp/risk_usd must echo candidate values exactly"}}
    return request


def _resolve_pointer(snapshot, pointer: str) -> bool:
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        return False
    value = snapshot
    try:
        for token in pointer.split("/")[1:]:
            token = token.replace("~1", "/").replace("~0", "~")
            value = value[int(token)] if isinstance(value, list) else value[token]
        return True
    except (KeyError, ValueError, IndexError, TypeError):
        return False


def validate_consultation_response(request: dict, response: dict) -> Tuple[bool, List[str]]:
    """Enforce the contract. Returns (ok, violations) - ok only when every
    invariant holds and nothing was invented."""
    violations: List[str] = []
    if not isinstance(response, dict):
        return False, ["response_not_a_dict"]
    if set(response) != RESPONSE_REQUIRED_KEYS:
        return False, [f"keys_mismatch:{sorted(set(response) ^ RESPONSE_REQUIRED_KEYS)}"]

    envelope = request.get("invariant_envelope") or {}
    if response.get("invariant_digest") != request.get("invariant_digest"):
        violations.append("invariant_digest_mismatch")

    action = response.get("action")
    if action not in ("SELECT", "HOLD"):
        violations.append(f"invalid_action:{action}")
        return False, violations

    candidate = request.get("candidate") or {}
    if action == "HOLD":
        if response.get("candidate_id") is not None:
            violations.append("hold_must_not_name_candidate")
        if response.get("risk_usd") is not None or response.get("sl") is not None \
                or response.get("tp") is not None:
            violations.append("hold_must_not_carry_order_terms")
    else:
        if response.get("candidate_id") != candidate.get("candidate_id"):
            violations.append("candidate_id_mismatch")
        # Numeric echoes must be EXACT: the LLM may not move money, stops or targets.
        for key in ("risk_usd", "sl", "tp"):
            expected = number(candidate.get(key))
            got = number(response.get(key), default=None) if response.get(key) is not None else None
            if got is None or abs(float(got) - float(expected)) > 1e-9:
                violations.append(f"{key}_not_echoed:{response.get(key)}!={expected}")
        risk = number(response.get("risk_usd"))
        if not number(envelope.get("risk_min_usd")) <= risk <= number(envelope.get("risk_max_usd")):
            violations.append(f"risk_budget_violation:{risk}")

    rationale = response.get("rationale_summary")
    if not isinstance(rationale, str) or not (1 <= len(rationale) <= MAX_RATIONALE_CHARS):
        violations.append("rationale_summary_invalid")
    for key in ("support_refs", "invalidation_refs"):
        refs = response.get(key)
        if not isinstance(refs, list) or len(refs) > MAX_REFS:
            violations.append(f"{key}_invalid")
            continue
        if action == "SELECT" and not refs:
            violations.append(f"{key}_empty_on_select")
        for pointer in refs:
            if not _resolve_pointer(request, pointer):
                violations.append(f"{key}_unresolved:{pointer}")

    return (not violations), violations
