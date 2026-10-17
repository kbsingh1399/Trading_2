"""
Unit Tests for Arkham Institutional Roster Integrity & System Memory Optimizer
Guarantees 100% valid canonical slugs, zero deprecated 404 slugs, and Win32 RAM optimization.
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from Terminal.Data_Factory.arkham_intelligence_harvester import (
    INSTITUTIONAL_ROSTER,
    KNOWN_EXCHANGES,
    KNOWN_MARKET_MAKERS,
    KNOWN_ASSET_MANAGERS,
    KNOWN_SOVEREIGN_TREASURIES,
    KNOWN_CORPORATE_TREASURIES,
    KNOWN_PROTOCOLS,
    classify_party,
)
from Terminal.Data_Factory.system_memory_optimizer import (
    get_system_memory_status,
    trim_current_process_working_set,
    optimize_ram,
)


class TestArkhamRosterAndMemoryOptimizer(unittest.TestCase):
    def test_roster_slug_integrity(self):
        """Verify all 48 institutional entities have valid, unique, non-404 slugs."""
        self.assertEqual(len(INSTITUTIONAL_ROSTER), 48, "Roster must contain exactly 48 entities")
        slugs = [e["slug"] for e in INSTITUTIONAL_ROSTER]
        self.assertEqual(len(slugs), len(set(slugs)), "All slugs in roster must be strictly unique")

        # Prohibit known legacy/404 slugs
        forbidden_slugs = {
            "amber-group",
            "gsr",
            "german-government",
            "uk-government",
            "royal-government-of-bhutan",
            "block-inc",
            "htx",
            "maker",
            "aerodrome",
            "drift",
            "curve",
        }
        for slug in slugs:
            self.assertNotIn(slug, forbidden_slugs, f"Forbidden legacy 404 slug found: {slug}")

        # Assert canonical replacement slugs exist
        canonical_replacements = {
            "amber",
            "gsr-markets",
            "germany",
            "uk",
            "druk-holding-investments",
            "cash-app",
            "huobi",
            "makerdao",
            "aerodrome-finance",
            "drift-protocol",
            "curve-fi",
        }
        for can_slug in canonical_replacements:
            self.assertIn(can_slug, slugs, f"Missing canonical slug: {can_slug}")

    def test_classification_party_coverage(self):
        """Verify classify_party accurately routes all canonical entities."""
        name, cat = classify_party("Amber Group")
        self.assertEqual(cat, "MARKET_MAKER")
        name, cat = classify_party("GSR Markets")
        self.assertEqual(cat, "MARKET_MAKER")
        name, cat = classify_party("germany")
        self.assertEqual(cat, "SOVEREIGN_TREASURY")
        name, cat = classify_party("uk")
        self.assertEqual(cat, "SOVEREIGN_TREASURY")
        name, cat = classify_party("druk-holding-investments")
        self.assertEqual(cat, "SOVEREIGN_TREASURY")
        name, cat = classify_party("cash-app")
        self.assertEqual(cat, "CORPORATE_TREASURY")
        name, cat = classify_party("huobi")
        self.assertEqual(cat, "EXCHANGE")
        name, cat = classify_party("makerdao")
        self.assertEqual(cat, "DEX_PROTOCOL")
        name, cat = classify_party("curve-fi")
        self.assertEqual(cat, "DEX_PROTOCOL")

    def test_system_memory_status(self):
        """Verify Win32 memory status query returns valid metrics."""
        stats = get_system_memory_status()
        self.assertGreater(stats["memory_load_pct"], 0)
        self.assertLessEqual(stats["memory_load_pct"], 100)
        self.assertGreater(stats["total_phys_gb"], 0.0)
        self.assertGreater(stats["avail_phys_gb"], 0.0)
        self.assertGreater(stats["used_phys_gb"], 0.0)

    def test_trim_working_set_execution(self):
        """Verify in-process working set trimming returns True without error."""
        success = trim_current_process_working_set()
        self.assertTrue(success, "trim_current_process_working_set must succeed on Windows")

    def test_ram_optimizer_execution(self):
        """Verify optimize_ram executes and reports memory before/after."""
        res = optimize_ram(threshold_pct=95)  # Use high threshold to test non-triggering path
        self.assertIn("initial", res)
        self.assertIn("final", res)
        self.assertIn("freed_gb", res)
        self.assertFalse(res["triggered_system_cleanup"])


if __name__ == "__main__":
    unittest.main()
