"""Cycle 105 source, timing, geometry and report regressions; offline only."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import cycle105_audit as audit

HERE = Path(__file__).resolve().parent
REPORT = HERE.parent / 'CYCLE_105_ASTRA_COUNCIL_REPORT.md'


class Cycle105Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e = json.loads((HERE / 'CYCLE_105_EVIDENCE.json').read_text())
        cls.a = cls.e['assets']
        cls.g = cls.e['cycle105_counterexamples']

    def test_exact_requested_generation_not_newer_main(self):
        self.assertEqual(self.e['generation'], 'd14b626dfa5a47e0a641b86f6ba49dd0')
        self.assertEqual(self.e['root']['as_of_utc'], '2026-10-14 19:30:16 UTC')
        self.assertEqual(self.e['tree']['nodes'], 135588)
        self.assertEqual(len(self.a), 24)
        self.assertEqual(len(self.e['manifest']), 7)
        for p, h in audit.SOURCE_HASHES.items():
            self.assertEqual(self.e['manifest'][p]['sha256'], h)
            self.assertEqual(self.e['manifest'][p]['commit'], audit.COMMIT)

    def test_mutation_with_correct_generation_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/audit.base.PATHS[0];p.parent.mkdir(parents=True)
            p.write_text(json.dumps({'generation_id':audit.GENERATION}))
            with self.assertRaisesRegex(ValueError, 'Pinned source hash mismatch'):
                audit.extract(folder)

    def test_visible_walls_are_not_seasoned_or_absent(self):
        self.assertEqual(sum(a['walls']['count'] for a in self.a.values()), 1108)
        self.assertEqual(sum(a['walls']['age180_count'] for a in self.a.values()), 0)
        self.assertEqual(max(a['wall_persistence_diagnostics']['max_recorded_persist_s'] for a in self.a.values()),141)
        self.assertEqual(max(a['wall_persistence_diagnostics']['max_samples'] for a in self.a.values()),2)
        self.assertEqual(sum(len(a['l2_walls']) for a in self.a.values()),47)
        self.assertTrue(all(w['persist_s']<180 for a in self.a.values() for w in a['l2_walls']))

    def test_wall_histories_follow_all_completed_candles(self):
        for a in self.a.values():
            if a['walls']['count']:
                self.assertTrue(a['wall_persistence_diagnostics']['all_first_seen_after_last_completed_candle'])
        for name,g in self.g.items():
            for wall in g.get('walls',[]):
                self.assertLess(wall['persist_s'],180)
                self.assertEqual(wall['samples'],2)
                self.assertAlmostEqual(wall['presence_frac'],.6667)

    def test_no_unfinalized_boundary_hidden_by_grid_coverage(self):
        for a in self.a.values():
            if a['source_blocks']['category']=='CRYPTO':
                self.assertEqual(a['source_blocks']['cvd_1m_buckets']['count'],59)
                for n,w in a['cvd_windows'].items():
                    earlier=a['cvd_generation_cutoff_windows'][n]
                    self.assertTrue(w['complete']);self.assertTrue(earlier['complete'])
                    self.assertEqual(w['end']-earlier['end'],60)
                    self.assertLessEqual(earlier['end'],self.e['root']['generation_started_at_epoch'])
                    self.assertGreater(w['end'],self.e['root']['generation_started_at_epoch'])
        self.assertLess(self.a['BTC']['cvd_windows']['15']['delta_usd'],0)
        self.assertGreater(self.a['BTC']['cvd_generation_cutoff_windows']['15']['delta_usd'],0)

    def test_eth_selling_robust_to_endpoint_and_sol_mixed(self):
        for field in ('cvd_windows','cvd_generation_cutoff_windows'):
            for n in ('5','15','30'):
                self.assertLess(self.a['ETH'][field][n]['delta_usd'],0)
            self.assertLess(self.a['SOL'][field]['5']['delta_usd'],0)
            self.assertGreater(self.a['SOL'][field]['15']['delta_usd'],0)
        self.assertEqual(self.a['BTC']['cvd_windows']['5']['delta_usd'],-636211.81)

    def test_no_engine1_extreme_but_engine2_rows_still_evaluated(self):
        self.assertTrue(all(abs(a['source_blocks']['causal_indicators']['vwap_z_score'])<2 for a in self.a.values()))
        self.assertEqual(self.a['USWTI']['source_blocks']['causal_indicators']['vwap_z_score'],-.07)
        self.assertEqual(self.a['USWTI']['analyst_classification'],'WATCHLIST')

    def test_nas_primary_sizes_return_without_age_inheritance(self):
        for name in ('NAS100_near','NAS100_deep'):
            g=self.g[name]
            self.assertGreater(g['walls'][0]['notional_usd'],1e6)
            self.assertLess(g['walls'][0]['persist_s'],180)
            self.assertLess(g['entry_distance_atr'],2)
        g=self.g['NAS100_deep']
        self.assertGreater(g['gross_R'],3)
        self.assertLess(g['research_stop']-g['research_entry'],g['index_minimum_distance'])
        self.assertLess((g['research_entry']-g['research_target_5bps'])/g['index_minimum_distance'],2)

    def test_all_fresh_stops_contained_and_intervals_deduplicated(self):
        self.assertNotIn('geometry_counterexamples',self.e)
        for name,g in self.g.items():
            self.assertTrue(g['contained_raw_bands'],name)
        for a in self.a.values():
            pairs=[(b['min_price'],b['max_price'])for b in a['all_unique_band_intervals']]
            self.assertEqual(len(pairs),len(set(pairs)))

    def test_sp_near_is_subthreshold_and_primary_remote(self):
        self.assertLess(self.g['SP500_near_subthreshold']['walls'][0]['notional_usd'],1e6)
        self.assertLess(self.g['SP500_near_subthreshold']['gross_R'],2)
        g=self.g['SP500_primary'];self.assertGreater(g['gross_R'],2)
        self.assertGreater(g['entry_distance_atr'],2)
        self.assertLess(g['research_stop']-g['research_entry'],g['index_minimum_distance'])

    def test_oil_no_stale_velocity_trap_or_passing_friction_claim(self):
        b=self.a['USWTI']['source_blocks'];g=self.g['USWTI_primary']
        self.assertEqual(b['pullback_geometry']['velocity_ratio'],.1321)
        self.assertLess(b['tradfi_orderflow']['15m_tick_cvd'],0)
        self.assertLess(b['quotes']['spread_bps'],5)
        self.assertGreater(g['friction_fraction'],.15)
        self.assertLess(g['gross_R'],2)
        self.assertGreater(g['last_completed_low'],g['mapped_bid'])
        self.assertGreater(g['research_entry'],g['mapped_bid'])

    def test_sol_and_eth_friction_bounds(self):
        self.assertGreater(self.g['SOL_primary']['friction_fraction'],.50)
        self.assertLess(self.g['SOL_primary']['R_ceiling_at_friction_minimum_to_selected_target'],1.14)
        self.assertGreater(self.g['ETH_primary']['friction_fraction'],.15)
        self.assertLess(self.g['ETH_primary']['R_ceiling_at_friction_minimum_to_selected_target'],2.2)

    def test_jpy_mixed_h1_range_and_fast_pullback(self):
        a=self.a['USDJPY']
        self.assertEqual(a['source_blocks']['causal_indicators']['trend_regime'],'RANGE_BOUND')
        self.assertEqual(a['htf']['1h']['ordering'],'MIXED')
        self.assertGreater(a['source_blocks']['pullback_geometry']['velocity_ratio'],1)
        self.assertEqual(a['analyst_classification'],'NO SETUP')

    def test_fx_zero_precision_not_free_and_old_quotes_disclosed(self):
        for s in ('EURUSD','GBPUSD'):
            a=self.a[s];q=a['source_blocks']['quotes']
            self.assertEqual(q['spread_price'],0);self.assertGreater(q['spread_bps'],0)
            self.assertIsNone(a['serialized_min_lot_spread_usd'])
        for s in ('XRP','DOGE','DOT','AVAX'):
            self.assertGreater(self.a[s]['source_blocks']['quotes']['quote_age_s'],10)

    def test_candle_cutoff_and_htf_limits(self):
        for a in self.a.values():
            self.assertEqual(a['source_blocks']['causal_indicators']['ema_200_bars_used'],799)
            self.assertEqual(a['bars']['bars_15m_ohlcv']['last_five'][-1]['close_ts'],1792005300)
            for h in a['htf'].values():
                self.assertEqual(h['n'],96);self.assertFalse(h['warmed_ema200_verified'])
            for b in a['bars'].values():
                self.assertEqual(b['nonmonotonic'],0);self.assertEqual(b['invalid_ohlc'],0);self.assertEqual(b['close_after_cutoff'],0)

    def test_inventory_disabled_macro_and_exact_stress(self):
        self.assertTrue(self.e['inventory_baseline_verified'])
        cal=self.e['root']['macro_calendar'];self.assertFalse(cal['blackout_active'])
        self.assertEqual(cal['blackout_enforcement'],'DISABLED_BY_OPERATOR')
        self.assertEqual(cal['event_release_utc'],'2026-10-15 02:55:00 UTC')
        self.assertEqual(self.e['risk_math']['3'],'4799.1750')
        self.assertEqual(self.e['risk_math']['4'],'4779.0500')

    def test_report_all24_and_rubric_before_verdict(self):
        text=REPORT.read_text();table=text.split('## 5. Mandate 1')[1].split('## 6. Mandates')[0]
        rows=[r for r in table.splitlines()if r.endswith(('WATCHLIST |','NO SETUP |','CANDIDATE |'))]
        self.assertEqual(len(rows),24)
        self.assertEqual(sum(r.endswith('WATCHLIST |')for r in rows),6)
        self.assertEqual(sum(r.endswith('NO SETUP |')for r in rows),18)
        for s,a in self.a.items():
            row=next(r for r in rows if r.startswith('| '+s+' /'))
            self.assertTrue(row.endswith(a['analyst_classification']+' |'))
        self.assertIn('single-agent five-perspective adaptation',text)
        self.assertLess(text.index('## 7. Five-persona'),text.index('## 8. Final verdict'))
        for row in text.splitlines():
            if row.startswith('| H') and row[3:4].isdigit():
                cells=[c.strip()for c in row.split('|')[1:-1]]
                scores=[int(v)for v in cells[1].split('/')]
                self.assertAlmostEqual(sum(x*w for x,w in zip(scores,(30,25,15,20,10)))/10,float(cells[2]))

    def test_desk_preserves_pinned_prefix_and_report_once(self):
        desk=(HERE.parent/'LIVE_COLLABORATIVE_ORDER_DESK.md').read_bytes()
        receipt=self.e['manifest']['docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md']
        self.assertEqual(hashlib.sha256(desk[:receipt['bytes']]).hexdigest(),receipt['sha256'])
        self.assertEqual(desk.count(REPORT.read_bytes()),1)


if __name__=='__main__':
    unittest.main()
