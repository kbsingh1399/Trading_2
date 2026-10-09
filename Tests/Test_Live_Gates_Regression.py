"""Offline gate regressions; fake MetaTrader5 only, no broker connectivity or sends."""
from __future__ import annotations

import importlib
import json
import sys
import time
import types
import unittest
from pathlib import Path
from datetime import datetime, timezone
from unittest.mock import patch

from Terminal.risk.blackout_guard import BlackoutGuard
from Terminal.risk.live_admission import assert_joint_fill_safe
from Terminal.risk.ratchet_manager import RatchetManager, RatchetPhase
from Terminal.signals.wall_tracker import PersistentWallTracker
from Terminal.signals.funding_rate import _binance_symbol as funding_symbol
from Terminal.signals.open_interest import _binance_symbol as oi_symbol, oi_confirms_short


class TestBlackout(unittest.TestCase):
    def test_fomc_hard_window_boundaries(self):
        guard = BlackoutGuard()
        def check(h, m):
            return guard.is_blocked(datetime(2026, 10, 7, h, m, tzinfo=timezone.utc))[0]
        for h, m in [(16, 55), (17, 0), (17, 5), (17, 24), (18, 30), (18, 34)]:
            self.assertTrue(check(h, m), (h, m))
        self.assertFalse(check(16, 54))
        self.assertFalse(check(18, 35))

    def test_missing_calendar_blocks_new_orders(self):
        with patch("Terminal.risk.blackout_guard._CALENDAR_JSON", Path("/missing_macro_calendar.json")):
            blocked, reason = BlackoutGuard().is_blocked()
        self.assertTrue(blocked)
        self.assertIn("macro_calendar_unavailable", reason)

    @unittest.skipUnless(importlib.util.find_spec("numpy"), "requires bridge numpy dependency")
    def test_bridge_import_reports_guard_only_if_patched(self):
        import numpy  # ensure numpy is permanently resident in sys.modules
        fake = types.ModuleType("MetaTrader5")
        fake.order_send = lambda request: types.SimpleNamespace(retcode=10009)
        with patch.dict(sys.modules, {"MetaTrader5": fake}):
            saved = sys.modules.pop("Terminal.MT5_Execution_Bridge", None)
            try:
                bridge_module = importlib.import_module("Terminal.MT5_Execution_Bridge")
                self.assertTrue(bridge_module._BLACKOUT_GUARD_ACTIVE)
                self.assertTrue(getattr(fake.order_send, "_omni_blackout_guard", False))
            finally:
                if saved is not None:
                    sys.modules["Terminal.MT5_Execution_Bridge"] = saved
                else:
                    sys.modules.pop("Terminal.MT5_Execution_Bridge", None)

    @unittest.skipUnless(importlib.util.find_spec("numpy"), "requires bridge numpy dependency")
    def test_missing_native_currency_is_not_fabricated_as_usd(self):
        import Terminal.MT5_Execution_Bridge as bridge_module
        native = object.__new__(bridge_module.MT5ExecutionBridge)
        native.ensure_connected = lambda: True
        fake_mt5 = types.SimpleNamespace(account_info=lambda: types.SimpleNamespace(
            login=5064568, balance=5000.0, equity=5000.0))
        with patch.object(bridge_module, "mt5", fake_mt5):
            self.assertIsNone(native.get_account_summary()["currency"])
            with self.assertRaisesRegex(ValueError, "risk_account_unavailable_or_non_usd"):
                assert_joint_fill_safe(native, "BTCUSD.pi", "SHORT", .02, 83880, 84430)

    def test_install_blocks_entries_allows_only_verified_close_and_protection(self):
        calls = []
        mt5 = types.ModuleType("MetaTrader5")
        mt5.TRADE_ACTION_DEAL = 1
        mt5.TRADE_ACTION_PENDING = 5
        mt5.TRADE_ACTION_SLTP = 6
        mt5.TRADE_ACTION_REMOVE = 8
        mt5.ORDER_TYPE_BUY = 0
        mt5.ORDER_TYPE_SELL = 1
        mt5.positions_get = lambda ticket: [types.SimpleNamespace(symbol="BTCUSD.pi", volume=.02, type=0)] if ticket == 7 else []
        mt5.order_send = lambda request: calls.append(request) or types.SimpleNamespace(retcode=10009)
        with patch.dict(sys.modules, {"MetaTrader5": mt5}), patch.object(BlackoutGuard, "is_blocked", return_value=(True, "test blackout")):
            self.assertTrue(BlackoutGuard.install())
            wrapper = mt5.order_send
            self.assertTrue(BlackoutGuard.install())
            self.assertIs(mt5.order_send, wrapper)  # idempotent, no circular bridge import
            self.assertEqual(mt5.order_send({"action": 5}).retcode, 10036)
            self.assertEqual(mt5.order_send({"action": 1, "symbol": "BTCUSD.pi"}).retcode, 10036)
            self.assertEqual(mt5.order_send({"action": 1, "position": 7, "symbol": "BTCUSD.pi", "volume": .03, "type": 1}).retcode, 10036)
            for request in ({"action": 6}, {"action": 8},
                            {"action": 1, "position": 7, "symbol": "BTCUSD.pi", "volume": .02, "type": 1}):
                self.assertEqual(mt5.order_send(request).retcode, 10009)
            self.assertEqual(len(calls), 3)


class FakeBridge:
    pending = []
    positions = []
    account = {"connected": True, "currency": "USD", "balance_usd": 4811.62, "equity_usd": 4811.62}
    def get_account_summary(self):
        return self.account
    def get_open_positions(self):
        return self.positions
    def get_pending_orders(self):
        return self.pending
    def estimate_order(self, symbol, direction, entry, sl):
        return {"stop_loss_per_lot": abs(entry - sl)}


class TestJointFill(unittest.TestCase):
    def test_pending_contingent_risk_prevents_second_order(self):
        bridge = FakeBridge()
        bridge.pending = [{"symbol": "BTCUSD.pi", "direction": "SHORT", "volume": .02,
                           "price_open": 83880, "sl": 84430}]
        with self.assertRaisesRegex(ValueError, "joint_fill_floor_breach"):
            assert_joint_fill_safe(bridge, "ETHUSD.pi", "SHORT", .4, 2602.4, 2630)
        bridge.pending = []
        result = assert_joint_fill_safe(bridge, "ETHUSD.pi", "SHORT", .4, 2602.4, 2630)
        self.assertGreaterEqual(result["post_joint_stop_equity_usd"], 4795)

    def test_correlated_pending_rejected_even_with_plenty_of_cash(self):
        bridge = FakeBridge()
        bridge.account = {"connected": True, "currency": "USD", "balance_usd": 5000,
                          "equity_usd": 5000}
        bridge.pending = [{"symbol": "BTCUSD.pi", "direction": "SHORT", "volume": .02,
                           "price_open": 83880, "sl": 84430}]
        with self.assertRaisesRegex(ValueError, "correlated_joint_fill"):
            assert_joint_fill_safe(bridge, "ETHUSD.pi", "SHORT", .4, 2602.4, 2630)

    def test_incomplete_inventory_fails_closed(self):
        bridge = FakeBridge()
        bridge.pending = [{"symbol": "BTCUSD.pi", "direction": "SHORT", "volume": .02,
                           "price_open": 83880}]  # missing native SL
        with self.assertRaisesRegex(ValueError, "risk_inventory_invalid_sl"):
            assert_joint_fill_safe(bridge, "ETHUSD.pi", "SHORT", .4, 2602.4, 2630)
        bridge.pending = None
        with self.assertRaisesRegex(ValueError, "risk_inventory_unavailable"):
            assert_joint_fill_safe(bridge, "ETHUSD.pi", "SHORT", .4, 2602.4, 2630)


class TestRatchetAndWall(unittest.TestCase):
    def test_failed_close_retries(self):
        manager = RatchetManager()
        state = manager.register(99, "BTCUSD.pi", 83880, 84430, 82505, -1,
                                 staged_at=time.time() - 7 * 3600)
        manager._close_at_market = lambda _: False
        result = manager.check_position(99, 83880)
        self.assertEqual(result["action"], "time_decay_exit_failed")
        self.assertEqual(state.phase, RatchetPhase.OPEN)

    def test_wall_side_and_missing_sample_reset(self):
        w = PersistentWallTracker()
        for ts in (1000, 1090, 1180):
            w.update("BTCUSD.pi", [[99.99, 2000]], [[100.01, 2000]], 100, timestamp=ts)
        self.assertEqual({x.side for x in w.get_persistent_walls("BTCUSD.pi", now=1180)}, {"bid", "ask"})
        w.update("BTCUSD.pi", [], [], 100, timestamp=1200)
        w.update("BTCUSD.pi", [], [[100.01, 2000]], 100, timestamp=1210)
        self.assertEqual(w.get_persistent_walls("BTCUSD.pi", now=1210), [])
        self.assertEqual(len(w._walls["BTCUSD.pi"]), 1)

    def test_oi_roc_uses_closed_four_intervals_and_fails_on_gaps(self):
        from Terminal.signals.open_interest import get_oi_roc
        now = 1_800_000_000
        def payload(gap=False):
            rows = []
            for i, value in enumerate((100, 100, 100, 100, 98.9)):
                ts = now * 1000 - (5-i) * 900_000
                if gap and i == 2:
                    ts += 100_000
                rows.append({"timestamp": ts, "sumOpenInterestValue": value})
            rows.append({"timestamp": now * 1000, "sumOpenInterestValue": 500})  # open bucket must be excluded
            return rows
        class Reply:
            def __init__(self, body): self.body = body
            def __enter__(self): return self
            def __exit__(self, *args): return False
            def read(self): return json.dumps(self.body).encode()
        with patch("Terminal.signals.open_interest.time.time", return_value=now):
            with patch("urllib.request.urlopen", return_value=Reply(payload())):
                result = get_oi_roc("BTCUSD.pi", force_refresh=True)
                self.assertTrue(result["blocks_short"])
                self.assertAlmostEqual(result["oi_roc_pct"], -1.1)
            with patch("urllib.request.urlopen", return_value=Reply(payload(gap=True))):
                self.assertEqual(get_oi_roc("BTCUSD.pi", force_refresh=True)["reason"],
                                 "stale_or_gapped_oi_history")
        from Terminal.signals.open_interest import _CACHE
        _CACHE.pop("BTCUSDT", None)

    def test_six_broker_aliases_have_both_mappings(self):
        expected = {"DOGUSD.p": "DOGEUSDT", "DOTUSD.pi": "DOTUSDT",
                    "LNKUSD.p": "LINKUSDT", "LTCUSD.pi": "LTCUSDT",
                    "AVXUSD.p": "AVAXUSDT", "NERUSD.p": "NEARUSDT"}
        for name, symbol in expected.items():
            self.assertEqual(funding_symbol(name), symbol)
            self.assertEqual(oi_symbol(name), symbol)
        with patch("Terminal.signals.open_interest.get_oi_roc", return_value={"available": False}):
            self.assertFalse(oi_confirms_short("BTCUSD.pi"))


    def test_native_pending_order_decoding_and_unknown_type_fail_closed(self):
        import Terminal.MT5_Execution_Bridge as bridge_module
        native = object.__new__(bridge_module.MT5ExecutionBridge)
        native.ensure_connected = lambda: True
        native._utc_offset_seconds = lambda sym: 0

        # Fake MT5 orders with BUY_STOP (4), BUY_STOP_LIMIT (6), SELL_STOP (5)
        Order = types.SimpleNamespace
        fake_orders = [
            Order(ticket=1, symbol="BTCUSD.pi", magic=100895, comment="test", volume_current=0.02,
                  price_open=100.0, sl=90.0, tp=125.0, type=4, time_expiration=0, time_setup=0),
            Order(ticket=2, symbol="ETHUSD.pi", magic=100895, comment="test", volume_current=0.1,
                  price_open=2000.0, sl=2050.0, tp=1875.0, type=5, time_expiration=0, time_setup=0),
        ]
        with patch.object(bridge_module, "mt5", types.SimpleNamespace(orders_get=lambda: fake_orders)):
            pending = native.get_pending_orders()
            self.assertEqual(pending[0]["direction"], "LONG")   # BUY_STOP is LONG, not SHORT
            self.assertEqual(pending[1]["direction"], "SHORT")  # SELL_STOP is SHORT

        # Unknown type must fail closed
        unknown_orders = [
            Order(ticket=3, symbol="BTCUSD.pi", magic=100895, comment="test", volume_current=0.02,
                  price_open=100.0, sl=90.0, tp=125.0, type=99, time_expiration=0, time_setup=0)
        ]
        with patch.object(bridge_module, "mt5", types.SimpleNamespace(orders_get=lambda: unknown_orders)):
            with self.assertRaisesRegex(ValueError, "unsupported_pending_order_type"):
                native.get_pending_orders()

    def test_stage_order_rejects_sub_2_5r_target_and_invalid_levels(self):
        from Terminal.Execution.remote_reconciler import apply_command

        class FakeBridge:
            def get_open_positions(self): return []
            def get_symbol_price(self, sym): return {"bid": 100.0, "ask": 101.0, "contract_size": 1.0}
            def estimate_order(self, sym, direction, entry, sl): return {"stop_loss_per_lot": 10.0}

        # 0.1R target (entry 101, SL 111, TP 100 on SHORT) must be rejected
        params_0_1r = {"symbol": "XAUUSD.pi", "direction": "SHORT", "limit_price": 101.0,
                       "sl": 111.0, "tp": 100.0, "volume": 1.0}
        with self.assertRaisesRegex(ValueError, "r_multiple_below_minimum"):
            apply_command(FakeBridge(), {"type": "STAGE_ORDER", "params": params_0_1r},
                          clock=lambda: 1700000000)

        # Non-protective stop (SL on wrong side) must be rejected
        params_bad_sl = {"symbol": "XAUUSD.pi", "direction": "SHORT", "limit_price": 101.0,
                         "sl": 95.0, "tp": 76.0, "volume": 1.0}
        with self.assertRaisesRegex(ValueError, "protective_stop_must_be_adverse"):
            apply_command(FakeBridge(), {"type": "STAGE_ORDER", "params": params_bad_sl},
                          clock=lambda: 1700000000)

    def test_high_free_margin_does_not_bypass_pending_contingent_loss(self):
        """Astra P0 verification: High free margin must not bypass joint pending risk or drop the buffer."""
        class StressedBridge:
            account = {"connected": True, "currency": "USD", "balance_usd": 4800.0,
                       "equity_usd": 4800.0, "free_margin_usd": 3000.0}
            positions = []
            pending = [
                {"symbol": "BTCUSD.pi", "direction": "LONG", "volume": 0.02, "price_open": 83000, "sl": 82500},
                {"symbol": "XAUUSD.pi", "direction": "LONG", "volume": 0.01, "price_open": 4180, "sl": 4170},
            ]
            def get_account_summary(self): return self.account
            def get_open_positions(self): return self.positions
            def get_pending_orders(self): return self.pending
            def estimate_order(self, sym, direction, entry, sl): return {"stop_loss_per_lot": abs(entry - sl)}

        bridge = StressedBridge()
        # With volume=10.0 and per_lot=1.0, nominal risk is exactly 10.0 USD (within bounds 10.0-15.0 USD).
        # Total stressed loss (2 pending + 1 proposed = ~43.50 USD) leaves equity 4,800 - 43.50 = 4,756.50 < 4,795.00 (HARD_FLOOR + BUFFER).
        # Even with high free margin ($3,000), joint reservation must reject with joint_fill_floor_breach!
        with self.assertRaisesRegex(ValueError, "joint_fill_floor_breach"):
            assert_joint_fill_safe(bridge, "USDJPY.pi", "LONG", 10.0, 158.0, 157.0)

    def test_cached_book_does_not_rejuvenate_received_at(self):
        """Astra P1 verification: Re-reading cached book must preserve original receipt timestamp."""
        from Terminal.Data_Factory.factory import ZeroCostDataFactory
        factory = ZeroCostDataFactory(["BTC"])
        factory.clock = lambda: 1000.0
        book = {"ts": 995.0, "bids": [{"price": 100.0, "size": 1.0}], "asks": [{"price": 101.0, "size": 1.0}]}
        factory.ingest_book("BTC", book)

        # 500 seconds later, read payload at now = 1500.0
        p = factory.payload("BTC", now=1500.0)
        l2 = p.get("l2_book", {})
        self.assertEqual(l2.get("received_at"), 1000.0,
                         "received_at was rejuvenated to current query time instead of original arrival stamp!")

    def test_cvd_excludes_future_dated_trades_due_to_clock_skew(self):
        """Astra P1 verification: Future-stamped trades must not enter the trailing CVD window."""
        from Terminal.Data_Factory.bus import IntelligenceBus
        bus = IntelligenceBus()
        # Ingest trade at ts=1000 (valid) and trade at ts=1050 (future relative to evaluation now=1000)
        bus.publish_trade("BTC", ts=1000.0, price=100.0, size=1.0, side="BUY", venue="BINANCE")
        bus.publish_trade("BTC", ts=1050.0, price=100.0, size=2.0, side="BUY", venue="BINANCE")

        # Evaluate CVD at now = 1000.0 over 300s window
        cvd_val = bus.cvd("BTC", window_sec=300.0, now=1000.0)
        self.assertEqual(cvd_val, 100.0, "Future-dated trade ts=1050 leaked into CVD calculated at now=1000.0!")


if __name__ == "__main__":
    unittest.main()




def test_native_admission_uses_shared_nominal_cap_instead_of_legacy_fifteen():
    from Terminal.policy import MAX_RISK_USD
    from Terminal.risk.live_admission import assert_joint_fill_safe
    bridge = FakeBridge()
    bridge.positions = []
    bridge.pending = []
    bridge.account = {"connected": True, "currency": "USD", "balance_usd": 5000, "equity_usd": 5000}
    with __import__("pytest").raises(ValueError, match="proposed_risk_out_of_bounds"):
        assert_joint_fill_safe(bridge, "BTCUSD", "LONG", MAX_RISK_USD+.25, 100, 99)
