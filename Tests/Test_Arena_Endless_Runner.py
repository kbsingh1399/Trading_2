"""Deterministic, network-free tests for the passive minute sentinel."""
import datetime as dt
import importlib.util
from pathlib import Path
import unittest

MODULE = Path(__file__).resolve().parents[1] / "scripts/arena_endless_runner.py"
spec = importlib.util.spec_from_file_location("arena_endless_runner", MODULE)
sentinel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sentinel)
NOW = dt.datetime(2026, 10, 7, 17, 12, tzinfo=dt.timezone.utc)


def snapshot(*, pending=True, balance=4811.62):
    return {
        "protocol": "omni.telemetry.v2", "as_of_utc": "2026-10-07 17:11:00 UTC",
        "as_of_epoch": NOW.timestamp() - 60,
        "account": {"balance_usd": balance, "equity_usd": balance},
        "macro_calendar": {"hard_blackout_window_utc": [
            "2026-10-07 17:00:00 UTC", "2026-10-07 18:30:00 UTC"]},
        "active_positions": [], "pending_orders": ([{
            "ticket": 18648927, "symbol": "SOLUSD.p", "type": "SELL_LIMIT",
            "volume": .07, "price_open": 118, "sl": 119.5}]
            if pending else []),
        "assets_matrix_24": {"SOL": {"symbol_broker": "SOLUSD.p",
                                     "quotes": {"contract_size": 100}}},
    }


class TestArenaEndlessRunner(unittest.TestCase):
    def test_blackout_pending_alert_and_single_risk(self):
        report = sentinel.assess(snapshot(), NOW)
        self.assertEqual(report["pending"], 1)
        self.assertEqual(report["age_s"], 60)
        self.assertTrue(report["blackout"])
        self.assertTrue(any("BLACKOUT_PENDING" in issue and "18648927" in issue
                            for issue in report["issues"]))
        self.assertFalse(any("JOINT_STOP_BUFFER_BREACH" in issue for issue in report["issues"]))

    def test_missing_contract_fails_closed(self):
        data = snapshot()
        data["assets_matrix_24"] = {}
        report = sentinel.assess(data, NOW)
        self.assertTrue(any("UNKNOWN_CONTRACT_RISK" in issue for issue in report["issues"]))

    def test_joint_pair_breaches_operating_buffer(self):
        data = snapshot()
        data["pending_orders"].append({"ticket": 42, "symbol": "SOLUSD.p",
                                        "type": "SELL_LIMIT", "volume": .07,
                                        "price_open": 118, "sl": 119.5})
        report = sentinel.assess(data, NOW)
        self.assertTrue(any("JOINT_STOP_BUFFER_BREACH" in issue for issue in report["issues"]))

    def test_stale_snapshot_fails_closed(self):
        data = snapshot(pending=False)
        data["as_of_epoch"] = NOW.timestamp() - 181
        report = sentinel.assess(data, NOW)
        self.assertTrue(any("TELEMETRY_STALE" in issue for issue in report["issues"]))
        del data["as_of_epoch"]
        self.assertIsNone(sentinel.assess(data, NOW)["age_s"])

    def test_flat_book_and_no_blackout_after_window(self):
        later = dt.datetime(2026, 10, 7, 18, 35, tzinfo=dt.timezone.utc)
        data = snapshot(pending=False)
        data["as_of_epoch"] = later.timestamp() - 30
        report = sentinel.assess(data, later)
        self.assertFalse(report["blackout"])
        self.assertEqual(report["issues"], [])


if __name__ == "__main__":
    unittest.main()
