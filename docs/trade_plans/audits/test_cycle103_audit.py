"""Cycle 103 evidence regressions; no network or broker actions."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('cycle103_audit', HERE / 'cycle103_audit.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class Cycle103AuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e = json.loads((HERE / 'CYCLE_103_EVIDENCE.json').read_text())
        cls.a = cls.e['assets']

    def test_exact_main_generation_and_manifest(self):
        self.assertEqual(self.e['generation'], audit.GENERATION)
        self.assertEqual(self.e['tree']['nodes'], 136742)
        self.assertEqual(len(self.a), 24)
        self.assertEqual(len(self.e['manifest']), 7)
        receipt = self.e['manifest'][audit.PATHS[0]]
        self.assertEqual(receipt['commit'], audit.SNAPSHOT_COMMIT)
        self.assertEqual(receipt['sha256'], 'baa5e3d82d560d7abcca1fff201dfcf60e09a6058dd0d958eae2eb10483cc656')

    def test_wrong_generation_is_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            for path in audit.PATHS:
                p = Path(folder) / path
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('{"generation_id":"wrong"}')
            with self.assertRaisesRegex(ValueError, 'Wrong Cycle 103 generation'):
                audit.extract(folder)

    def test_cvd_has_exact_time_coverage(self):
        for a in self.a.values():
            if a['source_blocks']['category'] == 'CRYPTO':
                for w in a['cvd_windows'].values():
                    self.assertTrue(w['complete'])
                    self.assertEqual(w['n'], w['expected_n'])
                    self.assertLessEqual(w['end'], self.e['root']['as_of_epoch'])
        for s in ('BTC', 'ETH'):
            for n in ('5', '15', '30'):
                self.assertLess(self.a[s]['cvd_windows'][n]['delta_usd'], 0)
        self.assertGreater(self.a['BTC']['preceding_5m']['delta_usd'], 0)
        self.assertLess(self.a['ETH']['cvd_windows']['5']['delta_usd'], self.a['ETH']['preceding_5m']['delta_usd'])

    def test_missing_or_duplicate_minute_is_not_complete(self):
        rows = [{'ts': t, 'taker_buy_usd': 3, 'taker_sell_usd': 2, 'cvd_delta_usd': 1}
                for t in range(300, 600, 60)]
        self.assertTrue(audit.window(rows, 600, 5)['complete'])
        self.assertFalse(audit.window(rows[:-1], 600, 5)['complete'])
        self.assertFalse(audit.window(rows[:-1] + [rows[0]], 600, 5)['complete'])

    def test_basis_recovery_is_not_stale_null_claim(self):
        self.assertEqual(sum(a['basis']['median'] is not None for a in self.a.values()), 22)
        self.assertEqual(self.a['BTC']['basis']['median'], -66)
        self.assertEqual(self.a['NAS100']['basis']['median'], -18.135)
        self.assertNotEqual(self.a['USWTI']['basis']['median'], self.a['USWTI']['basis']['spot'])

    def test_wall_chronology_does_not_backdate_defense(self):
        a = self.a['NAS100']
        wall = next(w for w in a['walls']['all_ge500k'] if w['side'] == 'SELL' and w['price'] == 30060)
        high_bar = max(a['bars']['bars_15m_ohlcv']['last_five'], key=lambda r: r['high'])
        first = audit.epoch(wall['first_seen_utc'])
        self.assertGreater(first, high_bar['close_ts'])
        mapped = wall['price'] + a['basis']['median']
        # Even the candle overlapping the first observation never reached the
        # currently mapped wall. This is not a historical-basis certification.
        overlap = next(r for r in a['bars']['bars_15m_ohlcv']['last_five'] if r['ts'] <= first < r['close_ts'])
        self.assertLess(overlap['high'], mapped)
        a = self.a['SP500']
        wall = next(w for w in a['walls']['all_ge500k'] if w['side'] == 'SELL' and w['price'] == 7717.3)
        self.assertGreater(audit.epoch(wall['first_seen_utc']), a['bars']['bars_15m_ohlcv']['last_five'][-1]['close_ts'])

    def test_every_tested_stop_hits_an_adjacent_band(self):
        for g in self.e['geometry_counterexamples'].values():
            self.assertTrue(g['stop_contained_raw_intervals'])
        g = self.e['geometry_counterexamples']['ETH']
        self.assertAlmostEqual(g['hypothetical_stop'], 2466.2743)
        self.assertGreater(g['friction_fraction'], .15)
        oil = self.e['geometry_counterexamples']['USWTI']
        self.assertGreater(oil['hypothetical_stop'], oil['primary_bid_mapped'])

    def test_fx_precision_not_zero_or_exact_cash_claim(self):
        for s in ('EURUSD', 'GBPUSD'):
            self.assertIsNone(self.a[s]['serialized_min_lot_spread_usd'])
            self.assertGreater(abs(self.a[s]['quote_precision']['bps_error']), .1)
        self.assertGreater(self.a['GBPUSD']['source_blocks']['quotes']['spread_price'], 0)

    def test_empty_book_disabled_macro_and_exact_stress(self):
        root = self.e['root']
        self.assertEqual(root['active_positions']['count'], 0)
        self.assertEqual(root['pending_orders']['count'], 0)
        self.assertFalse(root['macro_calendar']['blackout_active'])
        self.assertEqual(root['macro_calendar']['blackout_enforcement'], 'DISABLED_BY_OPERATOR')
        self.assertEqual(self.e['risk_math']['3'], '4799.1750')
        self.assertEqual(self.e['risk_math']['4'], '4779.0500')

    def test_htf_and_all_bar_checks(self):
        for a in self.a.values():
            for h in a['htf'].values():
                self.assertEqual(h['n'], 96)
                self.assertFalse(h['warmed_ema200_verified'])
            for b in a['bars'].values():
                self.assertEqual(b['nonmonotonic'], 0)
                self.assertEqual(b['invalid_ohlc'], 0)
                self.assertEqual(b['close_after_cutoff'], 0)
        self.assertEqual(self.a['GER40']['source_blocks']['causal_indicators']['trend_regime'], 'BEARISH')
        self.assertEqual(self.a['GER40']['htf']['4h']['ordering'], 'BULL')
        self.assertEqual(self.a['GBPUSD']['htf']['4h']['ordering'], 'BEAR')

    def test_late_component_and_duplicate_records_are_disclosed(self):
        self.assertGreater(self.e['global_flow_seconds_after_root'], 5)
        self.assertEqual(sum(a['walls']['duplicate_signature_excess'] for a in self.a.values()), 8)
        self.assertEqual(sum(a['walls']['count'] for a in self.a.values()), 1147)
        self.assertEqual(sum(a['walls']['age180_count'] for a in self.a.values()), 596)

    def test_all_24_separate_verdict_rows(self):
        report = (HERE.parent / 'CYCLE_103_ASTRA_COUNCIL_REPORT.md').read_text()
        table = report.split('## 4. Mandate 1')[1].split('## 5. Fresh geometry')[0]
        rows = [l for l in table.splitlines() if l.endswith(('WATCHLIST |', 'NO SETUP |', 'CANDIDATE |'))]
        self.assertEqual(len(rows), 24)
        self.assertEqual(sum(l.endswith('WATCHLIST |') for l in rows), 7)
        self.assertEqual(sum(l.endswith('NO SETUP |') for l in rows), 17)
        for s in self.a:
            self.assertEqual(sum(l.startswith('| ' + s + ' /') for l in rows), 1)


if __name__ == '__main__':
    unittest.main()
