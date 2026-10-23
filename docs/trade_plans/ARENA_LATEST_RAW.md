\n```\n{
  "schema_version": "1.0.0",
  "cycle_id": "Cycle 310",
  "cutoff_utc": "2026-10-23 22:34:05 UTC",
  "evidence_manifest_sha256": "bbc0f2a18b8e18459319fa11fc72f9d3a17b4e517a5a59b0f175c30bea8b2c06",
  "prompt_sha256": null,
  "dispatch_nonce": "76d24e70-0632-4a5e-9c6b-252925fe8278",
  "provenance_status": "FAILED_BAD_CYCLE_ENVELOPE",
  "inventory_status": "UNRECONCILED_ENVELOPE_VS_COMMIT",
  "provenance_details": {
    "git_commit": "d6f7df9add0064e94bcbfbe6cbab672939342cf4",
    "git_tree": "a69298386185939e5552bc2fc1bd785a06d25d8a",
    "git_commit_time_utc": "2026-10-23 22:31:51 UTC",
    "git_commit_verified": true,
    "git_signature_verified": false,
    "git_signature_status": "UNSIGNED",
    "committed_snapshot_as_of_utc": "2026-10-23 22:31:44 UTC",
    "cycle_envelope_artifact_present_in_commit": false,
    "claimed_workbook_sha256": "0b4e3061281cd79fab5a1d07f1b50dac3250a5393338249a72106057f70eb0fc",
    "observed_workbook_sha256": "e855a87fb055ab6f5d8f2be8e5cdab19afe786afaa62ae006984a2c6ef2f6fab",
    "workbook_digest_match": false,
    "observed_master_manifest_file_sha256": "c36b326c64f6226a0c677f60efb99bd2ac84871de5178f580c8539f25f777855",
    "claimed_manifest_digest_bound_to_artifact": false,
    "observed_account_snapshot_sha256": "a1c91179cc7003535ca5e6279a292fc4d2aea1c600d5564cc8e220e677f31fad",
    "canonical_protocol_sha256": "d3653a1e9a8b52e4179297710b50ee089a74bf4e0c80410870bbfb83349b0431"
  },
  "hard_gate_results": {
    "cycle_envelope_valid": false,
    "prompt_digest_verified": false,
    "manifest_digest_verified": false,
    "workbook_digest_verified": false,
    "legal_account_observed": true,
    "legal_account_authorized": null,
    "evidence_freshness_verified": false,
    "calendar_verified": false,
    "event_blackout_active": true,
    "broker_session_open": null,
    "joint_solvency_kernel_met_for_existing_ticket": true,
    "post_joint_stop_balance_usd": 4797.88,
    "required_post_stop_balance_usd": 4795.0,
    "realized_headroom_usd": 2.88,
    "new_risk_authorized": false
  },
  "authenticated_inventory": {
    "as_of_utc": "2026-10-23 22:31:44 UTC",
    "balance_usd": 4799.88,
    "equity_usd": 4828.59,
    "margin_used_usd": 2451.0,
    "margin_free_usd": 2377.59,
    "active_positions_count": 1,
    "pending_orders_count": 0,
    "ticket_19267445_price_current": 81208.0,
    "ticket_19267445_profit_usd": 29.52,
    "trade_authorization": "DENIED_UNVERIFIED_ORDERFLOW",
    "calendar_status": "CALENDAR_UNAVAILABLE",
    "calendar_enforcement": "FAIL_CLOSED_BLOCKED"
  },
  "existing_ticket_actions": [
    {
      "ticket": 19267445,
      "symbol": "BTCUSD.pi",
      "action": "HOLD_NO_MODIFICATION_PENDING_VALID_LIVE_ENVELOPE",
      "evidence_basis": "COMMIT_D6F7DF9_SNAPSHOT_2026-10-23_22:31:44Z",
      "current_sl": 81640.0,
      "tp": 80600.0,
      "authenticated_mark": 81208.0,
      "authenticated_frozen_r0_excursion": 1.23,
      "next_ratchet_trigger": 81040.0,
      "next_ratchet_sl": 81300.0,
      "gross_stop_lock_usd_before_costs_and_gap": 3.6,
      "broker_transmission_authorized": false
    }
  ],
  "candidate_rows": [],
  "arithmetic_validation": "FAILED_PROVENANCE_PRECONDITION_DESPITE_INTERNAL_ENVELOPE_ARITHMETIC",
  "disputes": [
    {
      "id": "C310-D11-01",
      "severity": 1,
      "finding": "The supplied cycle_envelope JSON is syntactically malformed at the market_clocks object and contains trailing/interleaved fragments."
    },
    {
      "id": "C310-D11-02",
      "severity": 1,
      "finding": "prompt_sha256 is absent from the envelope and remains an unresolved ellipsis in the requested response example."
    },
    {
      "id": "C310-D11-03",
      "severity": 1,
      "finding": "The claimed workbook SHA-256 does not match the workbook blob at the specified commit."
    },
    {
      "id": "C310-D11-04",
      "severity": 1,
      "finding": "No cycle_envelope artifact, Cycle-310 UUID, or dispatch nonce exists in the specified commit tree; cycle_state.json still identifies Cycle 309."
    },
    {
      "id": "C310-D11-05",
      "severity": 1,
      "finding": "Envelope inventory at 22:34:05 differs materially from the latest authenticated commit snapshot at 22:31:44 and cannot be source-bound."
    },
    {
      "id": "C310-CALENDAR-01",
      "severity": 1,
      "finding": "The committed snapshot reports CALENDAR_UNAVAILABLE and FAIL_CLOSED_BLOCKED, contradicting event_blackout_active=false in the requested output."
    },
    {
      "id": "C310-RISK-LANGUAGE-01",
      "severity": 2,
      "finding": "The canonical protocol prohibits calling the protected BTC position 100% risk-free; $3.60 is a gross geometric lock before gap, slippage, swap, and closing costs."
    }
  ],
  "unknowns": [
    "Exact broker inventory and mark at 2026-10-23 22:34:05 UTC",
    "Cycle-dispatch prompt SHA-256",
    "Artifact bound to the claimed evidence-manifest digest",
    "Parsed broker-clock and asset-clock fields from the malformed object",
    "Authenticated GLM Cycle-310 response or concurrence",
    "Deterministic canonical serialization required to calculate response_sha256"
  ],
  "authorization": "DENIED_FAIL_CLOSED",
  "response_sha256": null
}\n```\n\n**`DENIED_BAD_CYCLE_ENVELOPE`.**\n\nThe envelope’s account arithmetic is internally coherent—`4799.88 + 37.56 − 0.81 = 4836.63`, and realized stressed headroom remains `$2.88`—but provenance fails first:\n\n- The JSON is malformed.\n- The workbook hash is wrong.\n- No Cycle-310 envelope/nonce is committed.\n- The committed state is Cycle 309.\n- The latest causal snapshot contains different equity, free margin, mark, and profit.\n- Its calendar is unavailable and fail-closed.\n\nSafe fallback from the authenticated `22:31:44Z` snapshot: **no candidates, no new risk, hold BTC `#19267445` at SL `81640` / TP `80600`, and do not ratchet until a fresh broker-authenticated mark reaches `81040` or below.** The envelope’s unverified `81074` mark would not trigger that ratchet anyway.\n\nGraphify was attempted and remained unavailable. This is independent Arena verification only; no authenticated GLM Cycle-310 response was harvested. No broker or repository action was taken.\n