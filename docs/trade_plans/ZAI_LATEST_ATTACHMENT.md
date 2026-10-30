{
  "cycle_id": "Cycle_015",
  "final_authorization": {
    "new_market_orders": "DENIED_FAIL_CLOSED",
    "resting_book": "FULL_CANCEL - blanket rollover invalidation (D15) + carried per-ticket breaches; restage window post-22:30 UTC",
    "recovery_path": "realized 4775.00 -> kernel 4795.00 -> 10-USD-ticket unlock 4809.50",
    "cycle_verdict": "DENIED_FAIL_CLOSED"
  },
  "account_solvency": {
    "balance_usd": 4762.83, "equity_usd": 4762.83,
    "floors_strict": {"hard": 4775.0, "op_buffer": 4795.0},
    "deficit_vs_strict_hard_floor_usd": -12.17,
    "post_joint_stress_equity_reproduced_usd": 4695.2425,
    "realized_headroom_reproduced_usd": -99.7575,
    "nominal_risk_capacity_clamped_usd": 0.0,
    "capital_mode": "TIER_0_DEFENSIVE", "new_risk_admissible": false,
    "realized_floor_breach": "flat-book post-GCR equity 4760.83 = -14.17 vs strict Hard Floor - breach is REALIZED, not contingent"
  },
  "active_staged_orders": "6/6 CANCEL (blanket own-card blackout invalidation; supplementary grounds per ticket)",
  "high_confluence_formulated_trades": ["FC-015-01 XAU deferred restage", "FC-015-02 NAS deferred restage", "FC-015-03 AUD reevaluate", "FC-015-04 BTC/BNB/DJ excluded"],
  "disputes_or_rejections": ["D1 floor desync (carried)", "D2 cutoff delta 24s -> 121s ESCALATED", "D3 CRITICAL receipt cache-stamping PROVEN SYSTEMATIC (fresh nonce over identical 56.13h-old observation)",
    "D4 unregistered orders, ledger 13h15m stale", "D5 RR breaches BTC 1.52R / BNB 1.20R (carried)", "D6 SL under-pads XAU/NAS/DJ (carried)",
    "D7 stale-level staging, drift updated", "D8 VR(4)/ER(48) null - second cycle", "D9 Max-Pain/FX liq holes (carried)", "D10 engine x100 defects (carried)",
    "D11 stress residual -0.755 (carried)", "D12 min-lot violations (carried)", "D13 whale-armor absence (carried)", "D14 ledger false assertion (carried)",
    "D15 NEW rollover invalidation active - all 6 orders breach own cards", "D16 NEW realized strict-floor breach at zero exposure"]
}