import sys
import pathlib

import pytest

root_dir = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from Terminal.Hyperdash_Terminal import HyperdashTerminal

def test_terminal_components():
    print("\n--- Testing HyperdashTerminal Headless Render ---")
    term = HyperdashTerminal(default_coin="BTC")

    print("1. Testing render_header...")
    header = term.render_header()
    assert header is not None

    print("2. Testing render_l2_orderbook...")
    ob = term.render_l2_orderbook()
    assert ob is not None

    print("3. Testing render_l3_orders (Wallet Addresses)...")
    l3 = term.render_l3_orders()
    assert l3 is not None

    print("4. Testing render_liquidations...")
    liq = term.render_liquidations()
    assert liq is not None

    print("5. Testing render_stops...")
    stops = term.render_stops()
    assert stops is not None

    print("6. Testing render_trades...")
    trades = term.render_trades()
    assert trades is not None

    print("7. Testing render_universe_matrix...")
    matrix = term.render_universe_matrix()
    assert matrix is not None

    print("8. Testing asset switch to ETH...")
    term.current_coin = "ETH"
    term.refresh_universe()
    # Live-network test (forensics round 2): the Hyperdash API is not
    # reachable from offline/CI environments - skip instead of erroring.
    if "coin" not in term.cached_asset_info:
        pytest.skip("Hyperdash API unreachable (offline/CI environment)")
    assert term.cached_asset_info["coin"] == "ETH"
    eth_ob = term.render_l2_orderbook()
    assert eth_ob is not None
    print(f"PASS: Switched to ETH (Price: ${term.cached_asset_info['mark_px']:.2f})")

    print("\n8. Testing asset switch to SOL...")
    term.current_coin = "SOL"
    term.refresh_universe()
    assert term.cached_asset_info["coin"] == "SOL"
    sol_l3 = term.render_l3_orders()
    assert sol_l3 is not None
    print(f"PASS: Switched to SOL (Price: ${term.cached_asset_info['mark_px']:.2f})")

    print("\n>>> ALL TERMINAL RENDER TESTS PASSED 100%! <<<")

if __name__ == "__main__":
    test_terminal_components()
