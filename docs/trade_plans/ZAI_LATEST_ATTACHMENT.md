{
  "cycle_id": "Cycle_023",
  "uuid": "682d10f7-d614-4066-898b-2577d2e8ce2f",
  "dispatch_nonce": "a9ee1a8d-c999-431d-ad4c-b962a893ed71",
  "cutoff_utc": "2026-10-30 03:19:02 UTC",
  "seat": "#3 Z.ai Sovereign Council (Risk Arbiter)",
  "account_solvency": {
    "login": 5064568, "balance_usd": 4762.83, "equity_usd": 4772.75,
    "margin_used_usd": 187.39, "margin_level_pct": 2546.960884,
    "floor_union": {"outer_statutory": [4600.0, 4650.0], "inner_binding": [4775.0, 4795.0]},
    "kernel_headroom_usd": -98.96, "equity_vs_4775_usd": -2.25,
    "post_joint_stress_equity_usd": 4696.04,
    "stress_reconstruction": {"reported_usd": 64.7875, "independent_band_usd": [52.22, 74.29],
      "feasible_decompositions": ["bnb_c10/aud_excluded: s=6.87", "bnb_c10/aud_flat-BE: s=5.27"],
      "resilience_multiplier_vs_4600": 2.4824},
    "capital_mode": "TIER_0_DEFENSIVE", "new_risk_admissible": false,
    "verdict_new_risk": "DENIED_FAIL_CLOSED"
  },
  "active_staged_orders": [
    {"ticket": 19490051, "symbol": "AUDUSD.pi", "role": "RUNNER", "ruling": "MANAGE_HOLD",
     "directives": ["R-1 SL->0.70288", "R-2 @0.70450->SL 0.70366", "R-3 TP 0.70570", "R-4 decay mark 04:28:55Z dormant", "R-5 weekend carry-or-flatten by 20:45Z"]},
    {"ticket": 19489155, "symbol": "BTCUSD.pi", "ruling": "VOID", "grounds": ["stale-anchor", "dossier-404", "weekend-gap-tail"]},
    {"ticket": 19489157, "symbol": "BNBUSD.p", "ruling": "VOID", "grounds": ["stale-anchor", "dossier-404", "wall-unverifiable"]},
    {"ticket": 19489158, "symbol": "XAUUSD.pi", "ruling": "VOID_REANCHORABLE", "fresh_vah": 4013.16, "stale_vs_pd_vah": 0.83},
    {"ticket": 19489159, "symbol": "NAS100.p", "ruling": "VOID_INVALID", "grounds": ["min-lot 0.01<0.10", "stale +650.41 vs fresh VAH"]},
    {"ticket": 19489160, "symbol": "DJ30.p", "ruling": "VOID_REANCHORABLE", "fresh_card": {"entry": 52398.41, "sl": 52468.06, "tp": 52224.28, "lots": 0.10, "risk_usd": 6.97}}
  ],
  "high_confluence_formulated_trades": [],
  "readmission_gates": ["min(bal,eq)-stress-2 >= 4795 on receipt <=15min", "dossier <=24h matching Section 10 card", "concurrency <= 4", "live spread gate"],
  "disputes_or_rejections": [
    "D-1 cutoff stamp delta 54s (envelope canonical)",
    "D-2 floor-regime divergence resolved to conservative union (4775/4795 binding)",
    "D-3 preflight receipt 62.12h stale, candidate matches no live ticket — freshness gate FAIL",
    "D-4 ledger frozen Cycle_004 / registry ghost book — 0 of 6 live tickets listed",
    "D-5 stress figure consistent-in-band but undecomposed — per-ticket stress receipt demanded",
    "D-6 AUD dossier footprint series vs live quote mismatch — envelope binding",
    "D-7 NAS100.p (and DJ30.p) pending 0.01 lots < volume_min 0.10 — symbol_info re-pull required",
    "D-8 staged anchors == prior-day VAHs — one-session staleness proven",
    "D-9 SL 0.70282 vs Cycle_021 directive 0.70288 (-0.6 pip) — capital-safe, logged",
    "D-10 concurrency latent breach 6 > 4"
  ],
  "verification": {"script": "scripts/cycle_023_seat3_math.py", "checks_total": 35, "checks_passed": 32,
    "intentional_fail_closed_findings": 3,
    "sidecar": "download/cycle_023_seat3_verdict.json",
    "sidecar_sha256": "918aca727653b7c46fd3f37b20c06ede4dc8df6f479968078b55589db3d4314c"}
}