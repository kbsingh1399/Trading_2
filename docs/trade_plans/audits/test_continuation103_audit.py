"""Pinned 18:21:56 continuation regressions; no broker or network access."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import continuation103_audit as audit

HERE = Path(__file__).resolve().parent
REPORT = HERE.parent / 'CYCLE_103_CONTINUATION_182156_ASTRA_REPORT.md'


class Continuation103Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e = json.loads((HERE / 'CYCLE_103_CONTINUATION_182156_EVIDENCE.json').read_text())
        cls.a = cls.e['assets']

    def test_pinned_generation_and_all_seven_sources(self):
        self.assertEqual(self.e['generation'], audit.GENERATION)
        self.assertEqual(self.e['tree']['nodes'], 136419)
        self.assertEqual(len(self.a), 24)
        self.assertEqual(len(self.e['manifest']), 7)
        for path, expected_hash in audit.SOURCE_HASHES.items():
            self.assertEqual(self.e['manifest'][path]['sha256'], expected_hash)
            self.assertEqual(self.e['manifest'][path]['commit'], audit.COMMIT)
        self.assertEqual(self.e['manifest'][audit.base.PATHS[0]]['bytes'], 4443852)

    def test_mutated_source_with_correct_generation_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / audit.base.PATHS[0]
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({'generation_id': audit.GENERATION}))
            with self.assertRaisesRegex(ValueError, 'Pinned source hash mismatch'):
                audit.extract(folder)

    def test_cvd_complete_and_eth_recovery_not_overwritten(self):
        for a in self.a.values():
            if a['source_blocks']['category'] == 'CRYPTO':
                for w in a['cvd_windows'].values():
                    self.assertTrue(w['complete'])
                    self.assertEqual(w['n'], w['expected_n'])
                    self.assertLessEqual(w['end'], self.e['root']['as_of_epoch'])
        for n in ('5', '15', '30'):
            self.assertLess(self.a['BTC']['cvd_windows'][n]['delta_usd'], 0)
        for n in ('5', '15'):
            self.assertGreater(self.a['ETH']['cvd_windows'][n]['delta_usd'], 0)
        self.assertLess(self.a['ETH']['cvd_windows']['30']['delta_usd'], 0)
        self.assertEqual(self.a['BTC']['source_blocks']['multi_horizon_cvd']['divergence'], 'BULLISH_ABSORPTION')

    def test_sol_new_aged_wall_passes_size_but_spread_fails(self):
        a = self.a['SOL']
        w = next(w for w in a['walls']['all_ge500k'] if w['side'] == 'SELL' and w['price'] == 105.95)
        self.assertGreater(w['notional_usd'], 5000000)
        self.assertGreater(w['persist_s'], 180)
        self.assertGreater(a['source_blocks']['quotes']['spread_bps'], 35)
        self.assertGreater(abs(w['price'] + a['basis']['median'] - a['source_blocks']['quotes']['mid']) / a['source_blocks']['causal_indicators']['atr_14'], 2)

    def test_sp_wall_overlaps_but_completed_candle_did_not_reach_it(self):
        g = self.e['refresh_geometry_counterexamples']['SP500']
        self.assertFalse(g['first_seen_after_last_completed_bar'])
        self.assertEqual(len(g['completed_bars_overlapping_or_after_first_seen']), 1)
        self.assertLess(g['completed_bars_overlapping_or_after_first_seen'][0]['high'], g['research_entry'])
        self.assertAlmostEqual(g['research_entry'], 7712.455)

    def test_other_primary_walls_cannot_defend_earlier_completed_bar(self):
        for s in ('BTC', 'ETH', 'NAS100'):
            g = self.e['refresh_geometry_counterexamples'][s]
            self.assertTrue(g['first_seen_after_last_completed_bar'])
            self.assertEqual(g['completed_bars_overlapping_or_after_first_seen'], [])

    def test_fresh_geometry_replaces_old_cases_and_all_stops_hit_bands(self):
        self.assertNotIn('geometry_counterexamples', self.e)
        for s, g in self.e['refresh_geometry_counterexamples'].items():
            self.assertTrue(g['contained_raw_bands'], s)
        g = self.e['refresh_geometry_counterexamples']['NAS100']
        self.assertGreater(g['gross_R'], 2.9)
        atr = self.a['NAS100']['source_blocks']['causal_indicators']['atr_14']
        self.assertLess(g['research_stop'] - g['research_entry'], 1.5 * atr)
        self.assertLess((g['research_entry'] - g['research_target_5bps']) / (1.5 * atr), 2)
        self.assertGreater(self.e['refresh_geometry_counterexamples']['ETH']['friction_fraction'], .15)
        self.assertGreater(self.e['refresh_geometry_counterexamples']['USWTI']['friction_fraction'], .20)

    def test_jpy_changed_regime_and_oil_proximity_credited(self):
        self.assertEqual(self.a['USDJPY']['source_blocks']['causal_indicators']['trend_regime'], 'RANGE_BOUND')
        self.assertEqual(self.a['USDJPY']['htf']['4h']['ordering'], 'BULL')
        self.assertLess(self.e['refresh_geometry_counterexamples']['USWTI']['entry_distance_atr'], 2)
        self.assertGreater(self.a['USWTI']['source_blocks']['quotes']['spread_bps'], 5)

    def test_inventory_macro_and_exact_stress(self):
        self.assertTrue(self.e['inventory_baseline_verified'])
        self.assertEqual(self.e['root']['active_positions']['count'], 0)
        self.assertEqual(self.e['root']['pending_orders']['count'], 0)
        self.assertFalse(self.e['root']['macro_calendar']['blackout_active'])
        self.assertEqual(self.e['root']['macro_calendar']['blackout_enforcement'], 'DISABLED_BY_OPERATOR')
        self.assertEqual(self.e['risk_math']['3'], '4799.1750')
        self.assertEqual(self.e['risk_math']['4'], '4779.0500')

    def test_schema_limits_and_array_validation(self):
        self.assertGreater(self.e['global_flow_seconds_after_root'], 5)
        self.assertEqual(sum(a['walls']['count'] for a in self.a.values()), 1133)
        self.assertEqual(sum(a['walls']['age180_count'] for a in self.a.values()), 549)
        self.assertEqual(sum(a['walls']['duplicate_signature_excess'] for a in self.a.values()), 7)
        for a in self.a.values():
            for h in a['htf'].values():
                self.assertEqual(h['n'], 96)
                self.assertFalse(h['warmed_ema200_verified'])
            for b in a['bars'].values():
                self.assertEqual(b['nonmonotonic'], 0)
                self.assertEqual(b['invalid_ohlc'], 0)
                self.assertEqual(b['close_after_cutoff'], 0)
        for s in ('EURUSD', 'GBPUSD'):
            self.assertIsNone(self.a[s]['serialized_min_lot_spread_usd'])

    def test_report_all24_and_six_research_watches(self):
        text = REPORT.read_text()
        table = text.split('## 3. Mandate 1')[1].split('## 4. Fresh geometry')[0]
        rows = [line for line in table.splitlines() if line.endswith(('WATCHLIST |', 'NO SETUP |', 'CANDIDATE |'))]
        self.assertEqual(len(rows), 24)
        self.assertEqual(sum(r.endswith('WATCHLIST |') for r in rows), 6)
        self.assertEqual(sum(r.endswith('NO SETUP |') for r in rows), 18)
        for s in self.a:
            self.assertEqual(sum(r.startswith('| ' + s + ' /') for r in rows), 1)
        self.assertIn('single-agent five-perspective adaptation', text)
        self.assertIn('Silver does have nearby aged ask clusters exceeding 0.75 M', text)

    def test_desk_append_preserves_pinned_prefix_and_report_once(self):
        desk = (HERE.parent / 'LIVE_COLLABORATIVE_ORDER_DESK.md').read_bytes()
        prefix_receipt = self.e['manifest']['docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md']
        self.assertEqual(hashlib.sha256(desk[:prefix_receipt['bytes']]).hexdigest(), prefix_receipt['sha256'])
        report = REPORT.read_bytes()
        self.assertEqual(desk.count(report), 1)


if __name__ == '__main__':
    unittest.main()
