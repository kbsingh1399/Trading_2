{
  "cycle_id": "Cycle_014",
  "final_authorization": {
    "new_market_orders": "DENIED_FAIL_CLOSED",
    "resting_book": "CONDITIONAL_MAINTENANCE (cancel 19489155/19489157/19489160; restage 19489158/19489159; keep 19490051)",
    "cycle_verdict": "DENIED_FAIL_CLOSED"
  },
  "account_solvency": {
    "balance_usd": 4762.83, "equity_usd": 4762.83,
    "floors_strict": {"hard": 4775.0, "op_buffer": 4795.0},
    "deficit_vs_strict_hard_floor_usd": -12.17,
    "post_joint_stress_equity_reproduced_usd": 4695.2425,
    "realized_headroom_reproduced_usd": -99.7575,
    "nominal_risk_capacity_clamped_usd": 0.0,
    "capital_mode": "TIER_0_DEFENSIVE", "new_risk_admissible": false
  },
  "disputes_or_rejections": ["D1 Floor desync (recurring)", "D2 Cutoff stamp 24s", "D3 CRITICAL receipt temporal paradox (55.66h stale, nonce-carried)",
    "D4 Unregistered resting orders (6 tickets, zero ledger trace)", "D5 CRITICAL RR breaches BTC 1.52R / BNB 1.20R",
    "D6 SL invariant breaches XAU -9.45% / NAS -12.03% / DJ -7.24%", "D7 Stale-level staging (drift BTC -2.164%, BNB -6.117%)",
    "D8 VR(4)/ER(48) null account-wide", "D9 Max-Pain/FX liquidation holes", "D10 Dossier engine x100 nominal-risk + GER40 corruption",
    "D11 Stress decomposition residual -0.755", "D12 Min-lot violations NAS/DJ", "D13 Whale-armor absence account-wide",
    "D14 Ledger false solvency assertion + 12h46m staleness"]
}