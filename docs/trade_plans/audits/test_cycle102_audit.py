"""Regression tests for the read-only Cycle 102 analysis (no broker access)."""
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('cycle102_audit', HERE / 'cycle102_audit.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class Cycle102AuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e = json.loads((HERE / 'CYCLE_102_EVIDENCE.json').read_text())

    def test_full_inventory_and_exact_generation(self):
        self.assertEqual(self.e['root']['generation_id'], audit.EXPECTED)
        self.assertEqual(self.e['tree_inventory']['nodes'], 136143)
        self.assertEqual(len(self.e['assets']), 24)
        self.assertEqual(self.e['source']['sha256'],
                         'b1a0068d61babe0a9e799efbf9263e2e4b09a0af2a541a81fa57d42477d034ae')

    def test_recursive_inventory_counts_nulls_and_empty_containers(self):
        self.assertEqual(audit.inventory({'x': [None, {}]})['nodes'], 4)

    def test_windows_detect_missing_and_duplicate_minutes(self):
        rows = [{'ts': t, 'taker_buy_usd': 3, 'taker_sell_usd': 1,
                 'cvd_delta_usd': 2} for t in range(300, 600, 60)]
        self.assertTrue(audit.cvd_windows(rows, 610)['5']['complete'])
        self.assertFalse(audit.cvd_windows(rows[:-1], 610)['5']['complete'])
        self.assertFalse(audit.cvd_windows(rows[:-1] + [rows[0]], 610)['5']['complete'])
        self.assertEqual(audit.cvd_windows(rows, 610)['5']['delta_usd'], 10)
        self.assertFalse(audit.cvd_windows(rows, 670)['5']['complete'])

    def test_exact_risk_arithmetic(self):
        r = self.e['risk_math']
        self.assertEqual(r['stress_per_max_risk_ticket'], '20.1250')
        self.assertEqual(r['three_ticket_equity'], '4799.1750')
        self.assertEqual(r['four_ticket_equity'], '4779.0500')
        self.assertEqual(r['four_ticket_equal_nominal_ceiling'], '11.31')

    def test_no_fabricated_fx_zero_friction(self):
        for s in ('EURUSD', 'GBPUSD'):
            a = self.e['assets'][s]
            self.assertTrue(a['zero_serialized_spread_positive_bps'])
            self.assertIsNone(a['minimum_lot_spread_cost_usd_estimate'])

    def test_complete_crypto_windows_and_flow_correction(self):
        for a in self.e['assets'].values():
            if a['source_blocks']['category'] == 'CRYPTO':
                self.assertTrue(all(w['complete'] for w in a['cvd_windows'].values()))
        btc = self.e['assets']['BTC']
        self.assertLess(btc['source_blocks']['multi_horizon_cvd']['session_cvd_usd'], 0)
        self.assertTrue(all(w['delta_usd'] > 0 for w in btc['cvd_windows'].values()))

    def test_geometry_counterexamples_really_hit_other_bands(self):
        for symbol, raw_edge in [('SP500', 7750), ('ETH', 2460)]:
            a = self.e['assets'][symbol]; b = a['source_blocks']
            basis = a['spot_hyperliquid_basis_estimate']
            stop = raw_edge + basis + .5 * b['causal_indicators']['atr_14'] + b['quotes']['spread_price'] / 2
            bands = b['structural_stop_clusters']['nearest_buy_stop_clusters_above']
            self.assertTrue(any(x['min_price'] + basis <= stop <= x['max_price'] + basis for x in bands))
        a = self.e['assets']['USWTI']; b = a['source_blocks']; basis = a['spot_hyperliquid_basis_estimate']
        stop = 93.7 + basis - .5 * b['causal_indicators']['atr_14'] - b['quotes']['spread_price'] / 2
        bands = b['structural_stop_clusters']['nearest_sell_stop_clusters_below']
        self.assertTrue(any(x['min_price'] + basis <= stop <= x['max_price'] + basis for x in bands))

    def test_empty_inventory_and_disabled_macro(self):
        self.assertEqual(self.e['root']['active_positions'], [])
        self.assertEqual(self.e['root']['pending_orders'], [])
        self.assertEqual(self.e['root']['macro_calendar']['blackout_enforcement'], 'DISABLED_BY_OPERATOR')

    def test_no_htf_ema200_overclaim(self):
        for a in self.e['assets'].values():
            for h in a['htf_diagnostics'].values():
                self.assertEqual(h['n'], 96)
                self.assertFalse(h['warmed_ema200_verified'])

    def test_report_contains_24_distinct_asset_verdicts(self):
        report = (HERE.parent / 'CYCLE_102_ASTRA_COUNCIL_REPORT.md').read_text()
        table = report.split('## 3. Mandate 1')[1].split('### Priority geometry')[0]
        rows = [line for line in table.splitlines() if line.endswith(('WATCHLIST |', 'NO SETUP |', 'CANDIDATE |'))]
        self.assertEqual(len(rows), 24)
        self.assertEqual(sum(line.endswith('WATCHLIST |') for line in rows), 7)
        self.assertEqual(sum(line.endswith('NO SETUP |') for line in rows), 17)
        for symbol in self.e['assets']:
            self.assertTrue(any(line.startswith('| ' + symbol + ' /') for line in rows))


if __name__ == '__main__':
    unittest.main()
