{
  "audit_type": "INSTITUTIONAL_360_REVIEW",
  "evidence_anchor": {"snapshot_gen": "35ecb6d9", "as_of_utc": "2026-10-27T16:35:35Z", "publication_stall_s": 6139},
  "floor_basis": {"live_hard_floor": 4775.0, "prior_basis": 4600.0, "rebaseline_flag": "BASIS_INSTABILITY"},
  "book_verification": {"live_positions": 1, "live_pendings": 2, "message_claimed": 5,
    "disputed": ["BTC_19379711_pending_vs_claimed_filled", "ETH_19383569_absent", "XAU_19381300_absent"],
    "balance_drift_unexplained_usd": -10.09},
  "stress_ledger": {
    "nominal_joint_usd": 40.42, "canonical_joint_usd": 62.77,
    "stressed_equity_usd": 4768.78, "hard_floor_usd": 4775.0,
    "floor_surplus_canonical_usd": -6.22, "floor_surplus_nominal_usd": 16.13,
    "max_safe_canonical_stress_usd": 54.55, "overcommitment_usd": 8.22,
    "verdict": "STRESS_INSOLVENT_UNDER_CANONICAL_CONVENTION"},
  "ticket_verdicts": {
    "BTC_19379711": {"sl_clearance_atr": 0.245, "required": ">=0.40 (SL 80897.8)", "tp_defect": "1.40 THROUGH absorption shelf 79,911.40", "verdict": "FIX_SL_OR_CLOSE"},
    "ETH_19383569": {"entry_in_band": "[2340,2350]_2.13M", "sl_in_band": "[2360,2370]_4.38M", "compliant_risk_usd": 12.69, "envelope_max": 10.0, "verdict": "SIZING_IMPOSSIBLE_CANCEL"},
    "USDJPY_19376039": {"entry_z": 1.58, "model1_min_z": 2.0, "fomc_exposure": "EXTREME", "verdict": "CLOSE_BY_PURGE_2026-10-28T17:25Z"},
    "UKBRENT_19378313": {"monitoring_coverage": "ABSENT_FROM_MATRIX", "verdict": "WATCHLIST_ONLY_UNTIL_COVERED"},
    "XAU_19381300": {"monitoring_coverage": "ABSENT_FROM_MATRIX", "verdict": "WATCHLIST_ONLY_UNTIL_COVERED"}},
  "governance": {"trade_authorization": "DENIED_UNVERIFIED_ORDERFLOW_5TH_CYCLE", "trading_while_denied": true,
    "slot_cap_status": "5_OF_4_USED", "calibration_n": 17, "calibration_frozen": true},
  "ratchet_findings": {"mechanism_validated": "GBPUSD_+0.80R_EXACT_TO_CENT", "mfe_capture_pct": 33,
    "recommended": ["chandelier_2.5xATR_trail", "partial_50pct_at_1R", "hysteresis_max(0.10ATR,2xspread)", "ATR_scaled_time_decay"]},
  "acceleration": {"needed_usd": 668.45, "tickets_at_lcb": 168, "tickets_at_p50": 100,
    "tier2_gate_recommendation": "balance>4900 AND n>=30 AND LCB>=0.45"},
  "mandated_actions": ["cancel_ETH_or_close_USDJPY", "USDJPY_purge_deadline", "BTC_SL_to_80897.8", "balance_reconciliation_-10.09", "ingest_calibration_win", "restart_stalled_publisher"],
  "overall": "PORTFOLIO_STRESS_INSOLVENT__IMMEDIATE_HEADROOM_RESTORE_REQUIRED"
}