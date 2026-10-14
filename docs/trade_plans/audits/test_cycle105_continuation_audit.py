"""Offline regressions for the nonempty-book Cycle 105 continuation."""
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import cycle105_continuation_audit as audit

HERE = Path(__file__).resolve().parent
REPORT = HERE.parent/'CYCLE_105_CONTINUATION_COUNCIL_REPORT.md'


class Cycle105ContinuationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e=json.loads((HERE/'CYCLE_105_CONTINUATION_EVIDENCE.json').read_text())
        cls.a=cls.e['assets'];cls.p=cls.e['pending_review'];cls.g=cls.e['continuation_counterexamples']

    def test_exact_generation_and_seven_hashes(self):
        self.assertEqual(self.e['generation'],audit.GENERATION)
        self.assertEqual(self.e['root']['as_of_utc'],'2026-10-14 20:22:47 UTC')
        self.assertEqual(self.e['tree']['nodes'],134483)
        self.assertEqual(len(self.e['manifest']),7)
        for path,h in audit.SOURCE_HASHES.items():
            self.assertEqual(self.e['manifest'][path]['sha256'],h)
            self.assertEqual(self.e['manifest'][path]['commit'],audit.COMMIT)

    def test_mutation_not_accepted_on_generation_id_alone(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/audit.base.PATHS[0];p.parent.mkdir(parents=True)
            p.write_text(json.dumps({'generation_id':audit.GENERATION}))
            with self.assertRaisesRegex(ValueError,'Pinned source hash mismatch'):
                audit.extract(folder,'unused')

    def test_actual_pending_inventory_not_flat_history(self):
        inv=self.e['observed_inventory']
        self.assertEqual(inv['active_positions'],[])
        self.assertEqual(len(inv['pending_orders']),1)
        self.assertEqual(inv['pending_orders'][0]['ticket'],18925596)
        self.assertEqual(inv['capacity']['used_joint_fill'],1)
        self.assertEqual(inv['capacity']['available'],3)
        self.assertNotIn('inventory_baseline_verified',self.e)

    def test_recommendation_does_not_execute_or_release(self):
        self.assertEqual(self.p['recommendation'],'DELETE')
        self.assertFalse(self.p['executed'])
        self.assertFalse(self.e['risk_math']['reserve_released'])
        self.assertIn('not executed',REPORT.read_text())
        self.assertIn('cancellation NOT performed or confirmed',REPORT.read_text())

    def test_exact_nonempty_book_risk(self):
        r=audit.risk_reserve('4859.55','9.50','1223.75')
        self.assertEqual(Decimal(r['pending_stress_usd']),Decimal('13.875'))
        self.assertEqual(Decimal(r['stress_per_additional_full_risk_ticket_usd']),Decimal('20.125'))
        expected=['4845.675','4825.550','4805.425','4785.300']
        for n,x in enumerate(expected):
            self.assertEqual(Decimal(r['post_joint_stop_equity_by_additional_full_risk_tickets'][str(n)]),Decimal(x))
            self.assertEqual(Decimal(self.e['risk_math']['post_joint_stop_equity_by_additional_full_risk_tickets'][str(n)]),Decimal(x))
        self.assertNotIn('3',self.e['risk_math']) # No base flat-book risk-map leakage.

    def test_capacity_is_not_margin_or_risk_authorization(self):
        r=self.e['risk_math']
        self.assertEqual(r['maximum_additional_full_risk_tickets_by_buffer_only'],2)
        self.assertEqual(Decimal(r['free_margin_after_fill_usd']),Decimal('3635.80'))
        self.assertFalse(r['post_fill_above_playbook_4000'])
        receipt=self.e['observed_inventory']['risk']
        self.assertEqual(receipt['total_contingent_stress_usd'],13.875)
        self.assertEqual(receipt['pending_margin_on_fill_usd'],1223.75)

    def test_current_eth_sl_inside_mapped_sweep(self):
        self.assertEqual(self.p['contained_mapped_intervals'],[[2447.85,2457.85]])
        self.assertLess(2447.85,self.p['existing_order']['sl'])
        self.assertGreater(2457.85,self.p['existing_order']['sl'])
        self.assertEqual(self.p['contained_raw_bands'][0]['sources'][0]['notional_usd'],2359072.07)

    def test_eth_friction_and_lot_scaling(self):
        self.assertAlmostEqual(self.p['friction_fraction'],2.9/9.5)
        self.assertGreater(self.p['friction_fraction'],.15)
        self.assertFalse(self.p['lot_reduction_changes_friction_ratio'])
        for lots in (.01,.1,.5,1.):
            self.assertAlmostEqual(2.9*lots/(9.5*lots),self.p['friction_fraction'])
        self.assertLess(self.a['ETH']['source_blocks']['quotes']['spread_bps'],35)

    def test_fixed_target_widening_does_not_preserve_R(self):
        self.assertAlmostEqual(self.p['gross_R'],22.5/9.5)
        self.assertAlmostEqual(self.p['minimum_distance_at_15pct_friction'],19.333333333333332)
        self.assertLess(self.p['fixed_target_R_ceiling_at_friction_minimum'],1.17)

    def test_actual_in_range_eth_defense_is_credited(self):
        self.assertTrue(self.p['primary_between_entry_and_stop'])
        self.assertEqual(self.p['mapped_primary_ask'],2448.15)
        self.assertGreater(self.p['primary_ask']['notional_usd'],5e6)
        self.assertEqual(self.p['primary_ask']['persist_s'],1982.2)
        self.assertEqual(self.p['primary_ask']['presence_frac'],.8824)
        mapped_large=self.p['larger_ask_beyond_stop']['price']+self.a['ETH']['basis']['median']
        self.assertGreater(mapped_large,self.p['existing_order']['sl'])

    def test_eth_completed_primary_touch_not_invented(self):
        self.assertFalse(self.p['primary_touched_by_fully_subsequent_completed_bar'])
        self.assertEqual(len(self.p['fully_subsequent_completed_15m_bars']),1)
        self.assertEqual(self.p['fully_subsequent_completed_15m_bars'][0]['high'],2430.9)

    def test_persistence_recovered_but_not_certified_continuous(self):
        self.assertEqual(sum(a['walls']['count']for a in self.a.values()),1055)
        self.assertEqual(sum(a['walls']['age180_count']for a in self.a.values()),645)
        self.assertEqual(sum(len(a['l2_walls'])for a in self.a.values()),54)
        self.assertEqual(sum(w['persist_s']>=180 for a in self.a.values()for w in a['l2_walls']),8)
        for a in self.a.values():
            self.assertTrue(a['wall_persistence_diagnostics']['duration_is_not_continuous_defense'])
            self.assertFalse(a['wall_persistence_diagnostics']['producer_gate_used_as_admission_or_veto'])

    def test_cvd_cutoffs_agree_this_generation(self):
        for a in self.a.values():
            if a['source_blocks']['category']=='CRYPTO':
                for n,w in a['cvd_windows'].items():
                    self.assertTrue(w['complete'])
                    self.assertEqual(w,a['cvd_generation_cutoff_windows'][n])
                    self.assertEqual(w['end'],1792009320)
                    self.assertLessEqual(w['end'],self.e['root']['generation_started_at_epoch'])

    def test_fresh_crypto_flow_directions(self):
        for symbol in ('BTC','SOL'):
            for n in ('5','15','30'):
                self.assertGreater(self.a[symbol]['cvd_windows'][n]['delta_usd'],0)
        for n in ('1','5','15','30'):
            self.assertLess(self.a['ETH']['cvd_windows'][n]['delta_usd'],0)
        self.assertEqual(self.a['ETH']['cvd_windows']['5']['delta_usd'],-416090.74)

    def test_all24_dual_engine_and_fresh_classes(self):
        self.assertEqual(len(self.a),24)
        self.assertEqual(sum(a['analyst_classification']=='WATCHLIST'for a in self.a.values()),5)
        self.assertEqual(sum(a['analyst_classification']=='NO SETUP'for a in self.a.values()),19)
        for symbol,a in self.a.items():
            self.assertLess(abs(a['source_blocks']['causal_indicators']['vwap_z_score']),2)
            self.assertTrue(a['engine1_assessment'].startswith('FAIL:'))
            self.assertTrue(a['engine2_assessment'])
            self.assertIn('| '+symbol+' |',REPORT.read_text())
        self.assertEqual(self.a['USWTI']['analyst_classification'],'NO SETUP')
        self.assertNotIn('{{ASSET_TABLE}}',REPORT.read_text())

    def test_jpy_regime_is_not_stale_range_bound(self):
        a=self.a['USDJPY']
        self.assertEqual(a['source_blocks']['causal_indicators']['trend_regime'],'BEARISH')
        self.assertEqual(a['htf']['1h']['ordering'],'MIXED')
        self.assertEqual(a['htf']['4h']['ordering'],'BULL')
        self.assertGreater(a['source_blocks']['pullback_geometry']['velocity_ratio'],1)

    def test_composite_identity_and_contact_chronology(self):
        gold=self.e['composite_wall_checks']['GOLD'];oil=self.e['composite_wall_checks']['USWTI']
        self.assertAlmostEqual(gold['naive_notional_sum'],789533.81)
        self.assertEqual(gold['distinct_address_side_size_count'],2)
        self.assertEqual(gold['latest_first_seen'],'2026-10-14 20:16:06 UTC')
        self.assertEqual(len(oil['rows']),9)
        self.assertEqual(oil['distinct_address_side_size_count'],3)
        self.assertAlmostEqual(oil['conservative_signature_max_sum'],555499.92)
        self.assertGreater(oil['naive_notional_sum'],.75e6)
        self.assertLess(oil['conservative_signature_max_sum'],.75e6)
        self.assertFalse(oil['unique_order_ids_available'])

    def test_geometry_is_fresh_not_old_counterexamples(self):
        self.assertNotIn('geometry_counterexamples',self.e)
        self.assertNotIn('cycle105_counterexamples',self.e)
        for name,g in self.g.items():
            self.assertFalse(g['executable'],name)
            self.assertTrue(g['contained_raw_bands'],name)
        self.assertLess(self.g['SP500_primary']['gross_R_at_index_minimum'],2)
        self.assertLess(self.g['NAS100_near']['gross_R_at_index_minimum'],2)
        self.assertGreater(self.g['NAS100_deep']['gross_R_at_index_minimum'],2)
        self.assertLess(self.g['NAS100_deep']['research_stop']-self.g['NAS100_deep']['research_entry'],self.g['NAS100_deep']['index_minimum_distance'])
        self.assertLess(self.g['SOL_primary']['R_ceiling_at_friction_minimum_to_selected_target'],1.24)

    def test_oil_fresh_small_bid_and_friction(self):
        g=self.g['USWTI_subthreshold']
        self.assertEqual(g['wall']['price'],93.843)
        self.assertLess(g['wall']['notional_usd'],.75e6)
        self.assertGreater(g['friction_fraction'],.15)
        self.assertLess(g['gross_R'],1)
        self.assertEqual(self.a['USWTI']['source_blocks']['pullback_geometry']['velocity_ratio'],.0412)

    def test_spike_claim_checked_against_adjacent_generation(self):
        r=self.e['adjacent_generation_check']
        self.assertEqual(r['commit'],audit.PREVIOUS_COMMIT)
        self.assertEqual(r['sha256'],audit.PREVIOUS_SHA256)
        self.assertAlmostEqual(r['notional_ratio'],1.000071259215406)
        self.assertFalse(r['over_100x_single_generation_jump'])
        self.assertFalse(r['independent_venue_verification'])

    def test_native_precision_and_htf_limits_remain_explicit(self):
        for symbol in ('EURUSD','GBPUSD'):
            a=self.a[symbol]
            self.assertEqual(a['source_blocks']['quotes']['spread_price'],0)
            self.assertGreater(a['source_blocks']['quotes']['spread_bps'],0)
            self.assertIsNone(a['serialized_min_lot_spread_usd'])
        for a in self.a.values():
            for h in a['htf'].values():
                self.assertEqual(h['n'],96)
                self.assertFalse(h['warmed_ema200_verified'])
            for b in a['bars'].values():
                self.assertEqual(b['nonmonotonic']+b['invalid_ohlc']+b['close_after_cutoff'],0)

    def test_rubric_is_arithmetic_not_independent_consensus(self):
        c=self.e['council_adaptation']
        self.assertFalse(c['independent_agents_dispatched'])
        for option in c['options'].values():
            self.assertEqual(option['weighted_total'],sum(s*w for s,w in zip(option['scores'],c['weights']))/10)
        winner=c['options']['DELETE advice; retain reserve; no new admission']
        self.assertFalse(winner['fatal']);self.assertEqual(winner['weighted_total'],87.5)

    def test_report_appended_once_without_rewriting_desk(self):
        desk=(HERE.parent/'LIVE_COLLABORATIVE_ORDER_DESK.md').read_bytes()
        self.assertEqual(hashlib.sha256(desk[:3563784]).hexdigest(),'c9e0d6483f3cfd583f53ec7a45d3db894be243c10f39749347253a912b25fb0a')
        self.assertEqual(hashlib.sha256(desk[:3374485]).hexdigest(),audit.SOURCE_HASHES[audit.base.PATHS[2]])
        report=REPORT.read_bytes()
        self.assertEqual(desk.count(report),1)

    def test_macro_disabled_and_research_only(self):
        macro=self.e['root']['macro_calendar']
        self.assertFalse(macro['blackout_active'])
        self.assertEqual(macro['blackout_enforcement'],'DISABLED_BY_OPERATOR')
        self.assertIn('No broker calls',self.e['authority'])
        self.assertIn('Main remains untouched',REPORT.read_text())
        self.assertIn('not a production admission-engine change',REPORT.read_text())


if __name__=='__main__':
    unittest.main()
