{
  "cycle_id": "Cycle_026",
  "seat": "Seat #3 — Z.ai Sovereign Council (Adversarial Solvency Arbiter)",
  "envelope_binding": {
    "uuid": "bf927e4e-2217-4b4b-ab5f-1c3f219ed550",
    "dispatch_nonce": "cdf3c6fc-407d-42ab-ba47-b25ebac082b7",
    "cutoff_utc_governing": "2026-10-30 05:13:53",
    "header_cutoff": "2026-10-30 05:14:32",
    "cutoff_drift_seconds": 39
  },
  "account_solvency": {
    "login": 5064568, "server": "BlueberryMarketsSVG-Live",
    "balance": 4762.83, "equity": 4769.55, "equity_identity": "EXACT",
    "floating_pnl": 6.72, "margin_used": 187.39, "margin_free": 4582.16,
    "margin_level_pct": 2545.2532,
    "hard_floor_usd": 4775.0, "operating_buffer_usd": 4795.0,
    "hard_floor_cushion_usd": -5.45, "operating_buffer_cushion_usd": -25.45,
    "balance_vs_floor_usd": -12.17,
    "cushion_trajectory": {"C24": -1.69, "C25": -0.89, "C26": -5.45},
    "capital_mode": "TIER_0_DEFENSIVE",
    "nominal_risk_capacity_usd": 0.0,
    "new_risk_admissible": false,
    "joint_stress": {
      "desk_booked_usd": 65.4875, "desk_model_reproducible": false,
      "verified_best_usd": 31.45, "verified_worst_usd": 82.1875,
      "post_joint_desk_usd": 4695.3425, "post_joint_v_worst_usd": 4680.6425, "post_joint_v_best_usd": 4731.38,
      "capacity_zero_robust": true
    },
    "posture": "MARKET_ORDERS_DENIED_FAIL_CLOSED"
  },
  "active_staged_orders": [
    {"card_id": "C26-A-RATIFY", "action": "RATIFY_SL_0.70282_STANDING", "retired_directive": 0.70288, "protocol": "P3-BE", "class": "GOVERNANCE"},
    {"card_id": "C26-B-RECOVERY-CLOSE", "priority": "P1_ARMED", "ticket": 19490051, "action": "MARKET_CLOSE",
     "trigger_bid": 0.70450, "realizes_usd": 14.40, "post_balance_usd": 4777.23, "min_recovery_bid": 0.70423,
     "fallback": "FLATTEN_BY_2026-10-30T20:45Z", "class": "RISK_REDUCING"},
    {"card_id": "C26-C-CANCEL-PENDINGS", "priority": "P1_ESCALATED_GOVERNANCE_BREACH", "action": "CANCEL_PENDING",
     "tickets": [19489155, 19489157, 19489158, 19489159, 19489160],
     "evidence": ["RR 1.517R/1.195R breaches", "entries +0.46% to +2.25% beyond fresh VAH", "BTC/BNB dossiers ABSENT", "DJ dossier posture STAND_ASIDE_MONITOR", "concurrency 6>4", "C25 directive ignored"],
     "receipt_required": "C27 envelope", "class": "RISK_RETIRING"},
    {"card_id": "C26-D-VAH-GATE", "priority": "P2_ARMED", "ticket": 19490051, "action": "MARKET_CLOSE_AT_ENVELOPE",
     "trigger": "C27 price_current <= 0.70340 (fresh VAH surrender)", "realizes_usd": 5.60, "optional_hardening": "SELL_STOP 0.08 @ 0.70340", "class": "RISK_REDUCING"}
  ],
  "high_confluence_formulated_trades": [],
  "rearm_templates": [
    {"symbol": "DJ30.p", "source": "dossier Section 10 verbatim", "order": "SELL_LIMIT 52398.41", "sl": 52468.06,
     "tp": 52224.28, "lots": 0.10, "risk_usd": 6.97, "rr": 2.5, "dossier_posture": "STAND_ASIDE_MONITOR",
     "status": "NOT_POSTURED / NO_FILL_AUTHORIZATION"}
  ],
  "disputes_or_rejections": [
    {"id": "D1", "sev": "HIGH_ESCALATED", "item": "3rd consecutive preflight nonce-rebind (one stale Oct-27 object, three hashes: 05ac220e/78f4fcea/d2407f19)", "action": "VOID; pipeline quarantine; +/-120s freshness gate"},
    {"id": "D4", "sev": "CRITICAL_ESCALATED", "item": "C25 Card C IGNORED; 5 GTC pendings still PLACED = pre-authorized risk at capacity 0.00", "action": "GOVERNANCE BREACH; done-receipts required in C27"},
    {"id": "D6", "sev": "LOW", "item": "Cutoff drift 39s (6s in C25, growing)", "action": "Envelope governs"},
    {"id": "D7", "sev": "MEDIUM", "item": "All 4 provenance hashes identical across C24-C26", "action": "Bind instantiated-prompt hash per cycle"},
    {"id": "D8", "sev": "MEDIUM", "item": "MT5 trade-history demand standing (-139.41 leg; positive-slippage fill at open)", "action": "Disclose statement"},
    {"id": "D10", "sev": "HIGH", "item": "Registry/ledger frozen re-confirmed (last writes 08:27:01/08:05 UTC Oct-29; content unchanged on re-fetch)", "action": "Per-cycle registry write mandate"},
    {"id": "D11", "sev": "MEDIUM", "item": "Millisecond telemetry (time_update == time_msc) proves ZERO SL/TP modifications ever; C21-C25 ratchet narrative refuted; execution surface = open/close/cancel", "action": "P3-BE ratified; P4 close-form doctrine adopted"},
    {"id": "D12", "sev": "MEDIUM", "item": "Equity cushion -0.89 -> -5.45 (2nd consecutive decline)", "action": "VAH-surrender gate C26-D instituted"},
    {"id": "D13", "sev": "HIGH", "item": "Desk stress aggregate 65.4875 irreproducible under dossier-verified multipliers (DJ/NAS $1.00/pt/lot vs implied 10); BNB nominal unbounded [0.41, 41.00]", "action": "broker_spec receipts for BNBUSD.p; worst-case bound adopted"},
    {"id": "D14", "sev": "MEDIUM", "item": "Dossier Section-10 completeness 1/4; the only complete card postures STAND_ASIDE_MONITOR while the book rests a contrarian order", "action": "Fix dossier generator; reconcile engine posture with book"}
  ],
  "artifacts": {
    "verification_script": "scripts/cycle_026_seat3_math.py",
    "script_sha256": "9d0554434fbf48c773fe24f9db85b71f75e1bda641bfcda1accea11b765089b3",
    "sidecar": "download/Cycle_026_seat3_sidecar.json",
    "sidecar_sha256": "7eb6eb01ad1ced7542cf04e0fbe6eaaec77a4e9840468fa564348e9897680600"
  },
  "authorization_echo": "DENIED_PENDING_FULL_HARD_GATES -> SEAT3_POSTURE: DENIED_FAIL_CLOSED_MAINTAINED (close/cancel-form directives only)"
}