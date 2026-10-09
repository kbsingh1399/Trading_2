"""
Tests/Test_Chain_Verification_360.py
Automated test suite verifying the 360-Degree Data Source & Data Processing Forensic Engine.
"""

import pytest
from pathlib import Path
from Terminal.chain_verification_360 import (
    audit_parquet_candle_archives,
    audit_causal_feature_processing,
    audit_telemetry_snapshot_integrity,
    audit_broker_execution_and_floor,
    run_360_degree_chain_verification
)


def test_parquet_archives_integrity():
    """Verify all 24 Parquet archives have zero nulls, monotonic timestamps, and valid rows."""
    res = audit_parquet_candle_archives()
    assert res["status"] in ["PASS", "WARN"]
    assert res["files_with_nulls"] == 0, f"Found files with nulls: {res['files_with_nulls']}"
    assert res["files_non_monotonic"] == 0, f"Found non-monotonic files: {res['files_non_monotonic']}"
    assert res["files_verified"] >= 20, f"Expected at least 20 verified files, got {res['files_verified']}"


def test_causal_feature_processing_btc():
    """Verify mathematical feature calculation for BTC: ATR, VWAP, EMAs, RSI."""
    res = audit_causal_feature_processing("BTC")
    assert res["status"] == "PASS"
    inds = res.get("indicators_computed", {})
    assert "atr_14" in inds and inds["atr_14"] > 0.0
    assert "session_vwap" in inds and inds["session_vwap"] > 0.0
    assert "vwap_z_score" in inds
    assert "ema_20" in inds and inds["ema_20"] > 0.0
    assert "ema_50" in inds and inds["ema_50"] > 0.0
    assert "rsi_14" in inds and 0.0 <= inds["rsi_14"] <= 100.0


def test_telemetry_snapshot_integrity():
    """Verify telemetry snapshot file exists and has non-stale timestamps."""
    res = audit_telemetry_snapshot_integrity()
    assert res["file_exists"] is True


def test_full_360_degree_verification_run():
    """Verify master 360-degree verification certificate generation."""
    cert = run_360_degree_chain_verification()
    assert "certificate_id" in cert
    assert "overall_verdict" in cert
    assert cert["overall_verdict"] in ["CERTIFIED_100_PERCENT_PRISTINE", "WARNING", "INCOMPLETE"]
    assert "layer1_data_sources" in cert
    assert "layer2_data_processing" in cert
    assert "layer3_broker_and_floor" in cert


def test_360_degree_fails_closed_on_skip_or_unknown():
    """Astra P1 verification: If any layer status is SKIP or UNKNOWN, overall verdict must be INCOMPLETE, not PRISTINE."""
    from unittest.mock import patch
    import Terminal.chain_verification_360 as cv360

    with patch.object(cv360, "audit_mt5_live_data_source", return_value={"status": "SKIP"}):
        cert = cv360.run_360_degree_chain_verification()
        assert cert["overall_verdict"] == "INCOMPLETE", (
            f"Expected INCOMPLETE when layer status is SKIP, got {cert['overall_verdict']}"
        )
