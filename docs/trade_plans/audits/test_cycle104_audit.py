"""Cycle 104 evidence/report regressions; no network or execution calls."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import cycle104_audit as audit

HERE = Path(__file__).resolve().parent
REPORT = HERE.parent / 'CYCLE_104_ASTRA_COUNCIL_REPORT.md'


class Cycle104Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e = json.loads((HERE / 'CYCLE_104_EVIDENCE.json').read_text())
        cls.a = cls.e['assets']
        cls.g = cls.e['cycle104_research_counterexamples']

    def test_exact_generation_and_every_source_hash(self):
        self.assertEqual(self.e['generation'], audit.GENERATION)
        self.assertEqual(self.e['root']['as_of_utc'], '2026-10-14 18:41:47 UTC')
        self.assertEqual(self.e['tree']['nodes'], 136486)
        self.assertEqual(len(self.a), 24)
        self.assertEqual(len(self.e['manifest']), 7)
        for p, h in audit.SOURCE_HASHES.items():
            self.assertEqual(self.e['manifest'][p]['sha256'], h)
            self.assertEqual(self.e['manifest'][p]['commit'], audit.COMMIT)

    def test_same_generation_different_bytes_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / audit.base.PATHS[0]
            p.parent.mkdir(parents=True)
            p.write_text(json.dumps({'generation_id': audit.GENERATION}))
            with self.assertRaisesRegex(ValueError, 'Pinned source hash mismatch'):
                audit.extract(folder)

    def test_root_anchored_complete_crypto_windows(self):
        for a in self.a.values():
            if a['source_blocks']['category'] == 'CRYPTO':
                for w in a['cvd_windows'].values():
                    self.assertTrue(w['complete'])
                    self.assertEqual(w['n'], w['expected_n'])
                    self.assertLessEqual(w['end'], self.e['root']['as_of_epoch'])
        for n in ('5', '15', '30'):
            self.assertGreater(self.a['BTC']['cvd_windows'][n]['delta_usd'], 0)
        self.assertEqual(self.a['BTC']['cvd_windows']['15']['delta_usd'], 2135351.98)
        self.assertEqual(self.a['BTC']['preceding_5m']['delta_usd'], 1572274.02)
        self.assertLess(self.a['ETH']['cvd_windows']['5']['delta_usd'], 0)
        self.assertLess(self.a['ETH']['cvd_windows']['15']['delta_usd'], 0)
        self.assertGreater(self.a['ETH']['cvd_windows']['30']['delta_usd'], 0)

    def test_sp_crossed_price_predates_new_wall(self):
        g = self.g['SP500_near']
        bar = self.a['SP500']['bars']['bars_15m_ohlcv']['last_five'][-1]
        self.assertGreater(bar['high'], g['research_entry'])
        self.assertTrue(g['first_seen_after_last_completed_bar'])
        self.assertEqual(g['completed_bars_overlapping_first_observation_or_later'], [])
        self.assertGreater(audit.base.epoch(g['walls_at_raw_entry'][0]['first_seen_utc']), bar['close_ts'])

    def test_btc_eth_walls_now_overlap_but_were_not_touched(self):
        for name in ('BTC_primary', 'ETH_primary'):
            g = self.g[name]
            self.assertFalse(g['first_seen_after_last_completed_bar'])
            self.assertTrue(g['completed_bars_overlapping_first_observation_or_later'])
            self.assertTrue(all(r['high'] < g['research_entry'] for r in g['completed_bars_overlapping_first_observation_or_later']))

    def test_nas_previous_primary_absent_and_local_aggregate_under_one_million(self):
        a = self.a['NAS100']
        self.assertFalse(any(w['side'] == 'SELL' and w['price'] == 30081 for w in a['walls']['all_ge500k']))
        self.assertLess(a['walls']['age180_max_by_side']['SELL'], 1000000)
        near = [w for w in a['aged_l3_nearby'] if w['side'] == 'SELL']
        self.assertAlmostEqual(sum(w['notional_usd'] for w in near), 830359.37)
        l2 = next(w for w in a['l2_walls'] if w['side'] == 'SELL' and w['price'] == 29942)
        self.assertGreater(l2['notional_usd'], 1000000)
        self.assertLess(l2['persist_s'], 180)
        self.assertEqual(a['analyst_classification'], 'NO SETUP')

    def test_all_fresh_research_stops_hit_other_known_intervals(self):
        self.assertNotIn('geometry_counterexamples', self.e)
        for name, g in self.g.items():
            self.assertTrue(g['contained_raw_bands'], name)
        for a in self.a.values():
            pairs = [(b['min_price'], b['max_price']) for b in a['all_unique_band_intervals']]
            self.assertEqual(len(pairs), len(set(pairs)))

    def test_sp_deep_apparent_two_R_not_valid_after_index_distance(self):
        g = self.g['SP500_deep']
        self.assertGreater(g['gross_R'], 2)
        self.assertLess(g['research_stop'] - g['research_entry'], g['index_total_distance_minimum'])
        self.assertLess((g['research_entry'] - g['research_target_5bps']) / g['index_total_distance_minimum'], 2)
        self.assertGreater(g['entry_distance_atr'], 2)

    def test_sol_nominal_spread_improved_but_dynamic_geometry_fails(self):
        self.assertLess(self.a['SOL']['source_blocks']['quotes']['spread_bps'], 35)
        g = self.g['SOL_primary']
        self.assertGreater(g['walls_at_raw_entry'][0]['notional_usd'], 5000000)
        self.assertGreater(g['gross_R'], 2.5)
        self.assertGreater(g['friction_fraction'], .46)
        self.assertLess(g['R_upper_bound_at_friction_minimum_to_selected_target'], 1.24)

    def test_oil_spread_and_friction_improve_without_certifying_entry(self):
        a = self.a['USWTI']; g = self.g['USWTI_primary']
        self.assertLess(a['source_blocks']['quotes']['spread_bps'], 5)
        self.assertLess(g['friction_fraction'], .15)
        self.assertLess(g['entry_distance_atr'], 1)
        self.assertGreater(g['last_completed_bar_low'], g['primary_bid_mapped'])
        self.assertTrue(g['contained_raw_bands'])
        self.assertLess(g['POC_gross_R'], 2)
        self.assertGreater(g['research_entry'], g['primary_bid_mapped'])
        self.assertEqual(a['source_blocks']['pullback_geometry']['direction'], 'SHORT')
        self.assertEqual(a['source_blocks']['causal_indicators']['trend_regime'], 'BULLISH')

    def test_gold_cluster_credited_not_blanket_absence(self):
        a = self.a['GOLD']
        cluster = [w for w in a['aged_l3_nearby'] if w['side'] == 'SELL' and w['price'] in (4108, 4109)]
        self.assertAlmostEqual(sum(w['notional_usd'] for w in cluster), 783905.73)
        self.assertLess(a['walls']['age180_max_by_side']['SELL'], 750000)

    def test_jpy_regime_and_no_double_counted_primary(self):
        a = self.a['USDJPY']
        self.assertEqual(a['source_blocks']['causal_indicators']['trend_regime'], 'RANGE_BOUND')
        self.assertEqual(a['htf']['4h']['ordering'], 'BULL')
        self.assertLess(a['walls']['age180_max_by_side']['BUY'], 500000)
        self.assertEqual(a['analyst_classification'], 'NO SETUP')

    def test_friction_precision_and_silver_improvement(self):
        for s in ('EURUSD', 'GBPUSD'):
            self.assertIsNone(self.a[s]['serialized_min_lot_spread_usd'])
        for s in ('XRP', 'ADA', 'DOGE', 'TRX', 'LTC', 'NEAR'):
            self.assertGreater(self.a[s]['serialized_min_lot_spread_usd'], 2.175)
        self.assertAlmostEqual(self.a['SILVER']['serialized_min_lot_spread_usd'], 1.8)
        self.assertGreater(self.a['SILVER']['source_blocks']['quotes']['spread_bps'], 5)

    def test_inventory_calendar_and_exact_stress(self):
        self.assertTrue(self.e['inventory_baseline_verified'])
        cal = self.e['root']['macro_calendar']
        self.assertFalse(cal['blackout_active'])
        self.assertEqual(cal['blackout_enforcement'], 'DISABLED_BY_OPERATOR')
        self.assertEqual(cal['event'], 'Fed Bowman Speech: Bangkok Economic Festival')
        self.assertEqual(cal['event_release_utc'], '2026-10-15 02:55:00 UTC')
        self.assertEqual(self.e['risk_math']['3'], '4799.1750')
        self.assertEqual(self.e['risk_math']['4'], '4779.0500')

    def test_array_checks_and_measurement_limits(self):
        self.assertEqual(sum(a['walls']['count'] for a in self.a.values()), 1133)
        self.assertEqual(sum(a['walls']['age180_count'] for a in self.a.values()), 576)
        self.assertEqual(sum(a['walls']['duplicate_signature_excess'] for a in self.a.values()), 5)
        self.assertGreater(self.e['global_flow_seconds_after_root'], 5.6)
        for a in self.a.values():
            for h in a['htf'].values():
                self.assertEqual(h['n'], 96)
                self.assertFalse(h['warmed_ema200_verified'])
            for b in a['bars'].values():
                self.assertEqual(b['nonmonotonic'], 0)
                self.assertEqual(b['invalid_ohlc'], 0)
                self.assertEqual(b['close_after_cutoff'], 0)

    def test_all24_dual_engine_rows_and_deliberation_before_final(self):
        text = REPORT.read_text()
        table = text.split('## 4. Mandate 1')[1].split('## 5. Mandates')[0]
        rows = [r for r in table.splitlines() if r.endswith(('WATCHLIST |', 'NO SETUP |', 'CANDIDATE |'))]
        self.assertEqual(len(rows), 24)
        self.assertEqual(sum(r.endswith('WATCHLIST |') for r in rows), 5)
        self.assertEqual(sum(r.endswith('NO SETUP |') for r in rows), 19)
        for s, a in self.a.items():
            row = next(r for r in rows if r.startswith('| ' + s + ' /'))
            self.assertTrue(row.endswith(a['analyst_classification'] + ' |'))
        self.assertIn('single-agent five-perspective adaptation', text)
        self.assertLess(text.index('## 6. Five-persona'), text.index('## 7. Final verdict'))
        self.assertIn('cannot honestly certify', text)

    def test_append_only_desk_contains_full_report_once(self):
        desk = (HERE.parent / 'LIVE_COLLABORATIVE_ORDER_DESK.md').read_bytes()
        receipt = self.e['manifest']['docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md']
        self.assertEqual(hashlib.sha256(desk[:receipt['bytes']]).hexdigest(), receipt['sha256'])
        self.assertEqual(desk.count(REPORT.read_bytes()), 1)


if __name__ == '__main__':
    unittest.main()
