"""Offline Cycle 106 regressions; no network or broker dependencies."""
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import cycle106_audit as audit

HERE = Path(__file__).resolve().parent
REPORT = HERE.parent/'CYCLE_106_ASTRA_COUNCIL_REPORT.md'


class Cycle106Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e = json.loads((HERE/'CYCLE_106_EVIDENCE.json').read_text())
        cls.a = cls.e['assets']; cls.p = cls.e['pending_review']; cls.g = cls.e['cycle106_counterexamples']

    def test_exact_generation_and_seven_sources(self):
        self.assertEqual(self.e['generation'],audit.GENERATION)
        self.assertEqual(self.e['root']['as_of_utc'],'2026-10-14 20:40:24 UTC')
        self.assertEqual(self.e['tree']['nodes'],133829)
        self.assertEqual(len(self.e['manifest']),7)
        for path,h in audit.SOURCE_HASHES.items():
            self.assertEqual(self.e['manifest'][path]['sha256'],h)
            self.assertEqual(self.e['manifest'][path]['commit'],audit.COMMIT)
        for path in audit.base.PATHS[1:]:
            self.assertEqual(audit.SOURCE_HASHES[path],audit.PRIOR_HASHES[path])

    def test_source_mutation_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/audit.base.PATHS[0];p.parent.mkdir(parents=True)
            p.write_text(json.dumps({'generation_id':audit.GENERATION}))
            with self.assertRaisesRegex(ValueError,'Pinned source hash mismatch'):
                audit.extract(directory,'unused')

    def test_receipt_hash_guards(self):
        prior=HERE/'CYCLE_105_CONTINUATION_EVIDENCE.json'
        self.assertEqual(hashlib.sha256(prior.read_bytes()).hexdigest(),audit.PRIOR_EVIDENCE_HASH)
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'adjacent.json';p.write_text('{}')
            with self.assertRaisesRegex(ValueError,'adjacent snapshot'):
                audit.checked_bytes(p,audit.ADJACENT_HASH,'adjacent snapshot')

    def test_inventory_pending_not_realized_profit(self):
        inv=self.e['observed_inventory']
        self.assertEqual(inv['active_positions'],[])
        self.assertEqual(len(inv['pending_orders']),1)
        self.assertEqual(inv['pending_orders'][0]['ticket'],18925596)
        self.assertEqual(inv['capacity']['used_joint_fill'],1)
        self.assertTrue(self.p['current_ask_below_pending_TP'])
        self.assertTrue(self.p['pending_is_not_realized_profit'])
        self.assertEqual(self.p['order']['price_open'],2447.5)

    def test_advice_not_execution_or_reserve_release(self):
        self.assertEqual(self.p['recommendation'],'DELETE')
        self.assertFalse(self.p['executed'])
        self.assertFalse(self.e['risk_math']['reserve_released'])
        self.assertIn('NOT executed',REPORT.read_text())
        self.assertIn('no broker action',REPORT.read_text())

    def test_exact_joint_risk_and_margin(self):
        risk=self.e['risk_math']
        expected=['4845.675','4825.550','4805.425','4785.300']
        for n,value in enumerate(expected):
            self.assertEqual(Decimal(risk['post_joint_stop_equity_by_additional_full_risk_tickets'][str(n)]),Decimal(value))
        self.assertEqual(Decimal(risk['pending_stress_usd']),Decimal('13.875'))
        self.assertEqual(Decimal(risk['stress_per_additional_full_risk_ticket_usd']),Decimal('20.125'))
        self.assertEqual(Decimal(risk['free_margin_after_fill_usd']),Decimal('3635.80'))
        self.assertEqual(risk['maximum_additional_full_risk_tickets_by_buffer_only'],2)
        self.assertFalse(risk['post_fill_above_playbook_4000'])

    def test_new_eth_basis_and_band_containment(self):
        self.assertEqual(self.a['ETH']['basis']['median'],-2.2)
        self.assertEqual(self.p['contained_mapped_intervals'],[[2447.8,2457.8]])
        self.assertEqual(self.p['contained_raw_bands'][0]['sources'][0]['notional_usd'],2347725.95)
        self.assertLess(self.p['order']['sl'],2457.8)
        self.assertGreater(self.p['order']['sl'],2447.8)

    def test_eth_friction_and_fixed_target_bound(self):
        self.assertAlmostEqual(self.p['friction_fraction'],2.9/9.5)
        self.assertGreater(self.p['friction_fraction'],.15)
        self.assertAlmostEqual(self.p['gross_R'],22.5/9.5)
        self.assertLess(self.p['fixed_target_R_ceiling_at_friction_minimum'],1.17)
        for lots in (.01,.1,.5,1.):
            self.assertAlmostEqual(2.9*lots/(9.5*lots),self.p['friction_fraction'])

    def test_largest_eth_ask_now_in_range_not_stale_outside(self):
        asks=self.p['large_ask_locations']
        largest=max(asks,key=lambda w:w['wall']['notional_usd'])
        self.assertEqual(largest['mapped_price'],2450.)
        self.assertEqual(largest['location'],'between_entry_and_stop')
        self.assertEqual(largest['wall']['persist_s'],131.3)
        self.assertEqual(largest['wall']['notional_usd'],14429638.63)
        self.assertEqual({w['location']for w in asks},{'below_entry','between_entry_and_stop','beyond_stop'})
        self.assertFalse(self.p['age_inherited_from_same_wallet'])

    def test_current_and_adjacent_histories_unseasoned(self):
        p=self.e['persistence_comparison']
        self.assertEqual(p['current']['L3_rows'],1020)
        self.assertEqual(p['current']['L3_age180_rows'],0)
        self.assertEqual(p['current']['L2_rows'],53)
        self.assertEqual(p['current']['L2_age180_rows'],0)
        self.assertEqual(p['current']['max_recorded_span_s'],131.3)
        self.assertEqual(p['current']['max_samples'],2)
        self.assertEqual(p['adjacent']['L3_rows'],1031)
        self.assertEqual(p['adjacent']['max_recorded_span_s'],0)
        self.assertEqual(p['adjacent']['max_samples'],1)
        self.assertEqual(p['published_prior_receipt']['L3_age180_rows'],645)

    def test_recurrence_discontinuity_not_spoofing_proof(self):
        rows=[a['cross_audit_exact_large_signature_recurrence']for a in self.a.values()]
        self.assertEqual(sum(r['count']for r in rows),77)
        self.assertEqual(sum(r['shorter_reported_span_count']for r in rows),75)
        self.assertTrue(all(not r['continuous_survival_proven']for r in rows))
        self.assertFalse(self.e['persistence_comparison']['liquidity_disappearance_or_spoofing_proven'])
        self.assertTrue(self.e['persistence_comparison']['cause'].startswith('UNKNOWN'))

    def test_current_recorded_first_seen_after_completed_candle(self):
        for a in self.a.values():
            self.assertTrue(a['wall_timing']['all_first_seen_after_latest_completed_15m_close'])
            self.assertFalse(a['wall_timing']['inherited_age_or_producer_gate_used'])
            self.assertEqual(a['bars']['bars_15m_ohlcv']['last_five'][-1]['close_ts'],1792009800)

    def test_completed_cvd_and_new_directions(self):
        for a in self.a.values():
            if a['source_blocks']['category']=='CRYPTO':
                for n,w in a['cvd_windows'].items():
                    self.assertTrue(w['complete'])
                    self.assertEqual(w,a['cvd_generation_cutoff_windows'][n])
                    self.assertEqual(w['end'],1792010400)
        for symbol in ('BTC','ETH'):
            for n in ('5','15','30'):
                self.assertLess(self.a[symbol]['cvd_windows'][n]['delta_usd'],0)
        self.assertLess(self.a['SOL']['cvd_windows']['5']['delta_usd'],0)
        self.assertLess(self.a['SOL']['cvd_windows']['15']['delta_usd'],0)
        self.assertGreater(self.a['SOL']['cvd_windows']['30']['delta_usd'],0)

    def test_all24_both_engines_and_five_watches(self):
        self.assertEqual(len(self.a),24)
        self.assertEqual(sum(a['analyst_classification']=='WATCHLIST'for a in self.a.values()),5)
        self.assertEqual(sum(a['analyst_classification']=='NO SETUP'for a in self.a.values()),19)
        for symbol,a in self.a.items():
            self.assertLess(abs(a['source_blocks']['causal_indicators']['vwap_z_score']),2)
            self.assertTrue(a['engine1_assessment'].startswith('FAIL'))
            self.assertTrue(a['engine2_assessment'])
            self.assertIn('| '+symbol+' |',REPORT.read_text())
        self.assertEqual(self.a['NEAR']['source_blocks']['causal_indicators']['vwap_z_score'],-1.93)

    def test_jpy_velocity_improvement_not_old_veto(self):
        a=self.a['USDJPY']
        self.assertEqual(a['source_blocks']['pullback_geometry']['velocity_ratio'],.6154)
        self.assertEqual(a['htf']['1h']['ordering'],'MIXED')
        self.assertEqual(a['htf']['4h']['ordering'],'BULL')
        self.assertEqual(a['analyst_classification'],'NO SETUP')
        self.assertIn('not stale fast-velocity failure',a['engine2_assessment'])

    def test_old_gold_pair_not_inherited(self):
        rows=self.e['gold_prior_pair_current_rows']
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]['price'],4113.8)
        self.assertEqual(rows[0]['notional_usd'],453101.75)

    def test_geometry_new_levels_and_every_trial_contained(self):
        self.assertNotIn('geometry_counterexamples',self.e)
        self.assertNotIn('continuation_counterexamples',self.e)
        self.assertEqual(len(self.g),10)
        for name,g in self.g.items():
            self.assertTrue(g['contained_raw_bands'],name)
            self.assertFalse(g['executable'],name)
        self.assertEqual(self.g['ETH_in_range_primary']['research_entry'],2450.)
        self.assertGreater(self.g['ETH_in_range_primary']['friction_fraction'],.15)
        self.assertLess(self.g['ETH_in_range_primary']['gross_R'],2.2)
        self.assertLess(self.g['SP500_primary']['gross_R_at_index_minimum'],2)
        self.assertLess(self.g['NAS100_primary']['gross_R_at_index_minimum'],2)
        self.assertGreater(self.g['NAS100_deep']['gross_R_at_index_minimum'],2)
        self.assertEqual(self.g['USWTI_subthreshold']['wall']['price'],93.815)
        self.assertGreater(self.g['USWTI_subthreshold']['friction_fraction'],.15)
        self.assertLess(self.g['USWTI_subthreshold']['gross_R'],2)

    def test_fresh_precision_and_spread_changes(self):
        eur=self.a['EURUSD']['source_blocks']['quotes'];gbp=self.a['GBPUSD']['source_blocks']['quotes']
        self.assertEqual(eur['bid'],eur['ask']);self.assertEqual(eur['spread_price'],0)
        self.assertEqual(gbp['bid'],gbp['ask']);self.assertEqual(gbp['spread_price'],.0001)
        self.assertGreater(eur['spread_bps'],0);self.assertGreater(gbp['spread_bps'],0)
        self.assertGreater(self.a['AVAX']['source_blocks']['quotes']['spread_bps'],35)
        self.assertEqual(self.a['XRP']['serialized_min_lot_spread_usd'],3.)
        self.assertIsNone(self.a['GBPUSD']['serialized_min_lot_spread_usd'])

    def test_candle_integrity_and_htf_limit(self):
        for a in self.a.values():
            for h in a['htf'].values():
                self.assertEqual(h['n'],96);self.assertFalse(h['warmed_ema200_verified'])
            for b in a['bars'].values():
                self.assertEqual(b['nonmonotonic']+b['invalid_ohlc']+b['close_after_cutoff'],0)
        self.assertFalse(self.e['root']['p_win_lower_bound_calibrated'])
        self.assertEqual(self.e['root']['p_win_calibration_sample_n'],17)

    def test_rubric_arithmetic_and_disclosure(self):
        c=self.e['council_adaptation']
        self.assertFalse(c['independent_agents_dispatched'])
        for option in c['options'].values():
            self.assertEqual(option['weighted_total'],sum(s*w for s,w in zip(option['scores'],c['weights']))/10)
        self.assertEqual(c['options']['Inherit prior wall age and admit NAS']['weighted_total'],45.5)
        self.assertFalse(c['options']['DELETE advice; retain reserve; await fresh defense']['fatal'])

    def test_desk_prefix_and_single_append(self):
        desk=(HERE.parent/'LIVE_COLLABORATIVE_ORDER_DESK.md').read_bytes()
        self.assertEqual(hashlib.sha256(desk[:3589567]).hexdigest(),'3373a7485116e4805f73245aad12364337e3e2ee1303af001fc317f655bef337')
        self.assertEqual(hashlib.sha256(desk[:3374485]).hexdigest(),audit.SOURCE_HASHES[audit.base.PATHS[2]])
        self.assertEqual(desk.count(REPORT.read_bytes()),1)
        self.assertNotIn('{{ASSET_TABLE}}',REPORT.read_text())
        self.assertNotIn('{{GEOMETRY_TABLE}}',REPORT.read_text())

    def test_no_macro_veto_or_broker_mutation(self):
        self.assertEqual(self.e['root']['macro_calendar']['blackout_enforcement'],'DISABLED_BY_OPERATOR')
        self.assertFalse(self.e['root']['macro_calendar']['blackout_active'])
        self.assertIn('no broker cancellation',self.e['authority'])
        self.assertIn('not a production trading-engine change',REPORT.read_text())
        self.assertIn('Main untouched',REPORT.read_text())


if __name__=='__main__':
    unittest.main()
