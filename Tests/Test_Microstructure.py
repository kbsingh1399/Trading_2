import sys
import pathlib
import time

root_dir = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from Terminal.Microstructure import classify_liquidation, safe_imbalance, TokenBucket


def test_microstructure():
    print("\n--- 1. Testing classify_liquidation ---")
    # Explicit provider side
    assert classify_liquidation(70000.0, 80000.0, side="LONG") == "LONG"
    assert classify_liquidation(90000.0, 80000.0, side="BUY") == "LONG"
    assert classify_liquidation(70000.0, 80000.0, side="SHORT") == "SHORT"
    assert classify_liquidation(90000.0, 80000.0, side="SELL") == "SHORT"
    # Fallback heuristic
    assert classify_liquidation(75000.0, 80000.0, side=None) == "LONG"
    assert classify_liquidation(85000.0, 80000.0, side=None) == "SHORT"
    print("PASS: classify_liquidation adheres to explicit side and heuristic fallback.")

    print("\n--- 2. Testing safe_imbalance ---")
    assert safe_imbalance(100.0, 100.0) == 0.0
    assert safe_imbalance(200.0, 0.0) == 1.0
    assert safe_imbalance(0.0, 200.0) == -1.0
    assert safe_imbalance(0.0, 0.0) == 0.0
    # Equal proportions scale-free check
    assert safe_imbalance(75.0, 25.0) == 0.5
    assert safe_imbalance(75000.0, 25000.0) == 0.5
    print("PASS: safe_imbalance is strictly bounded [-1.0, 1.0] and scale-free.")

    print("\n--- 3. Testing TokenBucket ---")
    bucket = TokenBucket(rate=10.0, capacity=2.0)
    t0 = time.monotonic()
    bucket.acquire()
    bucket.acquire()
    elapsed = time.monotonic() - t0
    assert elapsed < 0.2, f"Initial bursts within capacity should be instant, took {elapsed}s"
    print("PASS: TokenBucket smoothly limits and acquires tokens.")

    print("\n--- 4. Testing FFR Unobserved Corridor & Overlapping Depth Fixes ---")
    import importlib.util
    spec = importlib.util.spec_from_file_location("micro_fixtures", root_dir / "Tests/Test_Omni_Engine.py")
    f = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f)
    NOW = f.NOW
    from Terminal.Risk_Sizing_Engine import OrderflowModel

    # Unobserved corridor: zero visible depth with positive fuel must be None, NOT 10.0
    p = f.payload()
    p["sources"]["wallet_risk"] = {"observed_at": NOW}
    p["projected_liquidations"] = {
        "kind": "PROJECTED_EXPOSURE",
        "bands": [{"min_px": 110, "max_px": 120, "amount_usd": 1e6, "position_side_at_risk": "SHORT"}]
    }
    feat = OrderflowModel().features("BTC", p, f.bars(), {}, NOW)
    assert feat["target_friction_usd"] == 0.0
    assert feat["ffr"] is None
    assert feat["coverage_missing"] is True
    assert feat["unobserved_corridor"] is True
    print("PASS: Unobserved corridor returns ffr=None and unobserved_corridor=True (no synthetic 10.0).")

    # Overlapping corridors: unique book levels counted once
    p_overlap = f.payload()
    p_overlap["sources"]["wallet_risk"] = {"observed_at": NOW}
    p_overlap["projected_liquidations"] = {
        "kind": "PROJECTED_EXPOSURE",
        "bands": [
            {"min_px": 100.01, "max_px": 100.10, "amount_usd": 500_000, "position_side_at_risk": "SHORT"},
            {"min_px": 100.05, "max_px": 100.15, "amount_usd": 500_000, "position_side_at_risk": "SHORT"},
        ]
    }
    feat_overlap = OrderflowModel().features("BTC", p_overlap, f.bars(), {}, NOW)

    p_single = f.payload()
    p_single["sources"]["wallet_risk"] = {"observed_at": NOW}
    p_single["projected_liquidations"] = {
        "kind": "PROJECTED_EXPOSURE",
        "bands": [
            {"min_px": 100.01, "max_px": 100.15, "amount_usd": 1_000_000, "position_side_at_risk": "SHORT"}
        ]
    }
    feat_single = OrderflowModel().features("BTC", p_single, f.bars(), {}, NOW)
    assert feat_overlap["target_friction_usd"] == feat_single["target_friction_usd"]
    print("PASS: Overlapping corridors count unique book levels exactly once without repeating depth.")

    print("\n--- 5. Testing Dense Friction Veto in Omni Trader ---")
    import tempfile, contextlib, io
    with tempfile.TemporaryDirectory(prefix="micro_test_") as temp:
        p_dense = f.payload()
        p_dense["projected_liquidations"] = {
            "kind": "PROJECTED_EXPOSURE",
            "bands": [{"min_px": 100.01, "max_px": 100.20, "amount_usd": 1000, "position_side_at_risk": "SHORT"}]
        }
        p_dense["sources"]["wallet_risk"] = {"observed_at": NOW}
        macro = {"received_at": NOW, "sentiment_valid": True, "asset_scores": {"BTC": 1}}
        trader, broker = f.trader(pathlib.Path(temp))
        with contextlib.redirect_stdout(io.StringIO()):
            report = trader.evaluate_market({"BTC": p_dense}, macro)
        assert report["decision"] == "HOLD"
        assert "dense_friction_veto" in report["vetoes"]["BTC"]
        print("PASS: Dense friction raises dense_friction_veto and halts execution (decision=HOLD).")

    print("\n--- 6. Testing Whale Eligibility Filter Hierarchy ---")
    import ast
    source = (root_dir / "Terminal/Omni_Trader.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    whales = next(n for n in ast.walk(tree) if isinstance(n, ast.Assign) and any(isinstance(x, ast.Name) and x.id == "whale_bids" for x in n.targets))

    # Reject small wall
    ns_small = {"payload": {"l3_orders": [{"side": "BUY", "price": 99.99, "notional_usd": 1, "observed_span_s": 0}]},
                "quote": {"bid": 100}, "atr": 1, "number": float}
    exec(compile(ast.Module(body=[whales], type_ignores=[]), "isolated_whale_filter", "exec"), ns_small)
    assert ns_small["whale_bids"] == []

    # Reject non-persistent wall (<180s)
    ns_short = {"payload": {"l3_orders": [{"side": "BUY", "price": 99.99, "notional_usd": 200_000, "persistence_sec": 30}]},
                "quote": {"bid": 100}, "atr": 1, "number": float}
    exec(compile(ast.Module(body=[whales], type_ignores=[]), "isolated_whale_filter", "exec"), ns_short)
    assert ns_short["whale_bids"] == []

    # Accept genuine persistent institutional whale
    ns_inst = {"payload": {"l3_orders": [{"side": "BUY", "price": 99.99, "notional_usd": 200_000, "persistence_sec": 180}]},
               "quote": {"bid": 100}, "atr": 1, "number": float}
    exec(compile(ast.Module(body=[whales], type_ignores=[]), "isolated_whale_filter", "exec"), ns_inst)
    assert ns_inst["whale_bids"] == [99.99]
    print("PASS: Whale filter strictly enforces notional >= 150000 USD and persistence >= 180s.")

    print("\n>>> ALL MICROSTRUCTURE UNIT TESTS PASSED 100%! <<<")


if __name__ == "__main__":
    test_microstructure()
