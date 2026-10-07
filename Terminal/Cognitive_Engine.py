import json
import time
import requests
import datetime
from typing import Dict, Any, Optional
from pathlib import Path
import os
from collections import deque
from Terminal.Risk_Sizing_Engine import epoch, number
from Terminal.Deterministic_Features import attest_decision, canon_value, SEAL_KEYS, SEAL_SCHEMA

# Astra's specified schemas
DECISION_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "snapshot_id",
        "action",
        "candidate_id",
        "analyst_thesis",
        "critic_objection",
        "support_refs",
        "counter_refs",
        "invalidation_refs",
        "rationale_summary",
        "abstain_reason"
    ],
    "properties": {
        "snapshot_id": {"type": "string"},
        "action": {"type": "string", "enum": ["SELECT", "HOLD"]},
        "candidate_id": {"type": ["string", "null"]},
        "analyst_thesis": {"type": "string", "maxLength": 800},
        "critic_objection": {"type": "string", "maxLength": 800},
        "support_refs": {
            "type": "array",
            "maxItems": 5,
            "items": {"type": "string"}
        },
        "counter_refs": {
            "type": "array",
            "maxItems": 5,
            "items": {"type": "string"}
        },
        "invalidation_refs": {
            "type": "array",
            "maxItems": 3,
            "items": {"type": "string"}
        },
        "rationale_summary": {
            "type": "string",
            "maxLength": 600
        },
        "abstain_reason": {"type": ["string", "null"]}
    }
}

SYSTEM_PROMPT = """ROLE
You are the Execution Committee for an institutional trading desk. You simulate three specialists:
1. The Conviction Analyst: Focuses on orderflow continuation, liquidation exhaustion, absorption, and target edges.
2. The Risk Critic: Challenges stale evidence, macro sentiment limits, and friction constraints.
3. The Execution Supervisor: Weighs the Analyst and Critic arguments, then renders the final verdict (SELECT or HOLD).

OBJECTIVE
Assess the supplied 15-minute market snapshot.
1. Analyst writes the bull/bear case.
2. Risk Critic aggressively attacks it.
3. Supervisor makes the final decision.

EVIDENCE CONTRACT
Use only the supplied snapshot. Cite facts using JSON Pointer references (e.g., /walls/0/side). Distinguish observations from estimates. Unknowns are not zero.

TASK
Return strictly valid JSON conforming to the decision schema."""

class CognitiveEngine:
    def __init__(self, endpoint_url="http://localhost:8081/v1/chat/completions", ledger_path=None):
        self.endpoint_url = endpoint_url
        self.decision_ledger_path = Path(ledger_path or Path(__file__).resolve().parents[1]/"Data/decision_ledger.jsonl")
        self.decision_ledger_path.parent.mkdir(exist_ok=True, parents=True)

    def build_snapshot(self, coin: str, sym: str, px: float, features: dict, raw_walls: list, raw_bands: list, macro: dict, portfolio: dict, regime: dict, sealed: dict = None) -> Dict[str, Any]:
        """Builds Astra's market_state.v1 snapshot.

        ``sealed`` is the tamper-proof deterministic feature vector (see
        Terminal/Deterministic_Features.py). When supplied, the cognitive
        engine sees ONLY the sealed values as econometrics, never raw or
        self-computed statistics, and the snapshot carries the digest chain so
        any downstream numeric claim can be attested mechanically.
        """
        now = datetime.datetime.now(datetime.timezone.utc)
        snap_id = f"snap_{coin}_{int(now.timestamp())}"
        
        # Format Walls
        walls = []
        for i, w in enumerate(raw_walls[:20]):
            walls.append({
                "id": f"W{i}",
                "side": w.get("side", "UNKNOWN"),
                "price": number(w.get("price")),
                "distance_bps": round(((w.get("price", px) - px) / px) * 10000, 2),
                "visible_notional_usd": number(w.get("notional_usd")),
                "cluster_observed_span_s": w.get("observed_span_s"),
                "observed_at": w.get("observed_at"),
            })
            
        # Format Liquidations
        proj_bands = []
        nearby = sorted(raw_bands, key=lambda b: abs(number(b.get("mid_px"), px)-px))[:10]
        for i, b in enumerate(nearby):
            proj_bands.append({
                "id": f"L{i}",
                "status": b.get("kind", "UNVERIFIED"),
                "position_side_at_risk": b.get("position_side_at_risk"),
                "distance_bps": round(((number(b.get("mid_px"), px) - px) / px) * 10000, 2),
                "estimated_notional_usd": b.get("amount_usd")
            })

        if sealed is not None:
            econometrics = dict(sealed.get("values") or {})
        else:
            # Fallback: numeric subset only, canonically rounded, so that the
            # attestation layer always works on deterministic magnitudes.
            econometrics = {k: canon_value(features.get(k)) for k in SEAL_KEYS if isinstance(features.get(k), (int, float)) or features.get(k) is None}
        snapshot = {
            "schema_version": "market_state.v1",
            "snapshot_id": snap_id,
            "as_of_utc": datetime.datetime.fromtimestamp(features.get("as_of", now.timestamp()), datetime.timezone.utc).isoformat(),
            "instrument": {
                "asset": coin,
                "execution_symbol": sym,
                "signal_venue": "HYPERLIQUID",
                "execution_venue": "MT5_BROKER"
            },
            "bar": {
                "current_bar_complete": False,
                "regime": regime.get("regime", "UNKNOWN"),
                "efficiency_ratio": regime.get("efficiency_ratio", 0.0)
            },
            "flow": {
                "depth_imbalance": features.get("l2_imbalance", 0.0),
                "tick_imbalance": features.get("tick_imbalance", 0.0),
                "target_long_score": features.get("long_score", 0.0),
                "target_short_score": features.get("short_score", 0.0)
            },
            "econometrics": econometrics,
            "attestation": {
                "schema": SEAL_SCHEMA,
                "feature_digest": (sealed or {}).get("digest"),
                "chain_digest": (sealed or {}).get("chain_digest"),
                "policy": "Every numeric claim in the decision prose must match a value in this snapshot; unmatched statistics are rejected as fabricated.",
            },
            "sleeve": features.get("sleeve", "S1_PULLBACK"),
            "candidate": {"candidate_id": f"{coin}_{features.get('direction', 'UNKNOWN')}", "direction": features.get("direction")},
            "walls": walls,
            "liquidations": {
                "projected_bands": proj_bands,
                "coverage": "NEAREST_10_BANDS_SEMANTICS_AS_LABELLED",
            },
            "macro": {
                "sentiment_score": macro.get("score", 0.0),
                "blackout_active": macro.get("blackout", False)
            },
            "portfolio": {
                "equity_usd": portfolio.get("equity", 5000.0),
                "available_position_slots": portfolio.get("slots", 2)
            }
        }
        return snapshot

    def _retrieve_memory(self, coin: str, as_of=None) -> list:
        """Retrieves the last 3 decisions for this specific asset to maintain continuity."""
        if not self.decision_ledger_path.exists():
            return []
        
        memory = []
        try:
            with open(self.decision_ledger_path, "r", encoding="utf-8") as f:
                lines = deque(f, maxlen=2000)
                # Read backwards
                for line in reversed(lines):
                    try:
                        record = json.loads(line)
                        if epoch(record.get("timestamp")) > (as_of or time.time()): continue
                        if record.get("snapshot", {}).get("instrument", {}).get("asset") == coin:
                            memory.append({
                                "timestamp": record.get("timestamp"),
                                "action": record.get("decision", {}).get("action"),
                                "analyst_thesis": record.get("decision", {}).get("analyst_thesis"),
                                "critic_objection": record.get("decision", {}).get("critic_objection"),
                                "outcome": record.get("outcome", "UNRESOLVED")
                            })
                            if len(memory) >= 3:
                                break
                    except:
                        continue
        except Exception as e:
            print(f"  [Cognitive Engine] Memory retrieval failed: {e}")
            
        return memory

    def evaluate_snapshot(self, snapshot: dict, candidate_direction: str = None, budget_seconds=8.0) -> Optional[dict]:
        """Send snapshot to LLM and retrieve decision"""
        coin = snapshot.get("instrument", {}).get("asset", "UNKNOWN")
        recent_memory = self._retrieve_memory(coin, epoch(snapshot.get("as_of_utc")))
        
        try:
            prompt_content = f"Snapshot:\n{json.dumps(snapshot, indent=2)}\n\nSchema:\n{json.dumps(DECISION_SCHEMA, indent=2)}\n"
            if recent_memory:
                prompt_content += f"\nRecent Decisions for {coin}:\n{json.dumps(recent_memory, indent=2)}\n"
            prompt_content += "\nProvide the JSON response."
            
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt_content}
            ]
            
            payload = {
                "model": os.environ.get("OMNI_LLM_MODEL", "gemini-3.5-flash-thinking"),
                "messages": messages,
                "temperature": 0.0,
                "response_format": {"type": "json_object"}
            }
            
            # Forensics round 3: no placeholder credentials. If the key is
            # unset, send no Authorization header (endpoint enforces access).
            _llm_key = os.environ.get("OMNI_LLM_API_KEY")
            headers = {"Authorization": "Bearer " + _llm_key} if _llm_key else {}
            resp = requests.post(self.endpoint_url, json=payload, headers=headers, timeout=max(0.1, min(8.0, budget_seconds)))
            if resp.status_code == 200:
                data = resp.json()
                content = data["choices"][0]["message"]["content"]
                decision = json.loads(content)
                if not self.validate_decision(snapshot, decision):
                    return None
                # Anti-hallucination gate (Incident B): every numeric claim in
                # the decision prose must exist in the sealed snapshot. A
                # fabricated statistic ("+1.8 sigma CVD divergence" when the
                # sealed vector says +0.92) rejects the decision outright.
                attested, violations = attest_decision(snapshot, decision)
                if not attested:
                    self.record_rejection(snapshot, decision, violations)
                    print(f"  [Cognitive Engine] Decision rejected: {len(violations)} unattested numeric claim(s): "
                          + "; ".join(f"{v['field']}:'{v['raw']}'" for v in violations))
                    return None
                self.record_decision(snapshot, decision)
                return decision
            else:
                print(f"  [Cognitive Engine] LLM API Error: {resp.status_code}")
                return None
        except Exception as e:
            print(f"  [Cognitive Engine] Inference failed: {e}")
            return None

    def record_decision(self, snapshot: dict, decision: dict):
        """Append to the decision ledger (Astra's Memory Layer)"""
        record = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "snapshot": snapshot,
            "decision": decision
        }
        with open(self.decision_ledger_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def record_rejection(self, snapshot: dict, decision: dict, violations: list):
        """Journal a fabricated-statistic rejection for forensic review."""
        record = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "event": "cognitive_fabrication_rejection",
            "snapshot_id": snapshot.get("snapshot_id"),
            "feature_digest": (snapshot.get("attestation") or {}).get("feature_digest"),
            "violations": violations,
            "decision": decision
        }
        try:
            with open(self.decision_ledger_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")
        except OSError:
            pass

    @staticmethod
    def validate_decision(snapshot, decision):
        if not isinstance(decision, dict) or set(decision) != set(DECISION_SCHEMA["required"]): return False
        if decision["snapshot_id"] != snapshot["snapshot_id"] or decision["action"] not in ("SELECT", "HOLD"): return False
        candidate_id = snapshot.get("candidate", {}).get("candidate_id")
        if decision["action"] == "SELECT" and decision["candidate_id"] != candidate_id: return False
        if decision["action"] == "HOLD" and decision["candidate_id"] is not None: return False
        for key, limit in (("analyst_thesis", 800), ("critic_objection", 800), ("rationale_summary", 600)):
            if not isinstance(decision[key], str) or len(decision[key]) > limit: return False
        if decision["abstain_reason"] is not None and not isinstance(decision["abstain_reason"], str): return False
        for key, limit in (("support_refs", 5), ("counter_refs", 5), ("invalidation_refs", 3)):
            refs = decision[key]
            if not isinstance(refs, list) or len(refs) > limit: return False
            for pointer in refs:
                if not isinstance(pointer, str) or not pointer.startswith("/"): return False
                value = snapshot
                try:
                    for token in pointer.split("/")[1:]:
                        token = token.replace("~1", "/").replace("~0", "~")
                        value = value[int(token)] if isinstance(value, list) else value[token]
                except (KeyError, ValueError, IndexError, TypeError): return False
        return decision["action"] != "SELECT" or bool(decision["support_refs"] and decision["invalidation_refs"])

    def record_outcome(self, snapshot, decision, outcome):
        record = {"timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(), "snapshot": snapshot,
                  "decision": decision, "outcome": outcome}
        with open(self.decision_ledger_path, "a", encoding="utf-8") as f: f.write(json.dumps(record)+"\n")
