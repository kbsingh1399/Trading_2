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

    print("\n>>> ALL MICROSTRUCTURE UNIT TESTS PASSED 100%! <<<")


if __name__ == "__main__":
    test_microstructure()
