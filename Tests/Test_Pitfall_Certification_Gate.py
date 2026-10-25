# Tests/Test_Pitfall_Certification_Gate.py
import pytest

from Terminal.Data_Factory.pitfall_certification_gate import certify_pitfalls, generate_certified_markdown_card

def test_pitfall_gate_catches_intrabar_buying_avalanche():
    # Ticket 19274977 simulation: aggressive taker buy avalanche > +25M USD opposing short
    market_state = {
        "candidate_action": "SELL",
        "symbol": "BTCUSD.pi",
        "entry_price": 80245.0,
        "sl_price": 80620.0,
        "tp_price": 79385.0,
        "current_bid": 80486.0,
        "current_ask": 80503.0,
        "recent_15m_taker_buy_usd": 32000000.0,
        "recent_15m_taker_sell_usd": 6500000.0,
        "net_taker_delta_usd": 25500000.0,  # Massive buying pressure!
        "is_bid_wall": False,
        "overhead_ask_wall_usd": 2000000.0,
        "unswept_stops_between": False,
        "spread_bps": 2.11,
        "realized_equity": 4846.32,
        "stressed_equity": 4826.32,
    }

    cert = certify_pitfalls(market_state)
    assert cert["certified"] is False
    assert "INTRA_BAR_BUYING_AVALANCHE" in cert["violations"]
    card = generate_certified_markdown_card(cert)
    assert "REJECTED FAIL-CLOSED" in card
    assert "Intra-Bar Flow Avalanche" in card

def test_pitfall_gate_passes_clean_confluence():
    clean_state = {
        "candidate_action": "SELL",
        "symbol": "BTCUSD.pi",
        "entry_price": 81500.0,
        "sl_price": 81850.0,
        "tp_price": 80200.0,
        "current_bid": 81200.0,
        "current_ask": 81216.0,
        "recent_15m_taker_buy_usd": 8000000.0,
        "recent_15m_taker_sell_usd": 14000000.0,
        "net_taker_delta_usd": -6000000.0,  # Negative delta aligns with short
        "is_bid_wall": False,
        "overhead_ask_wall_usd": 5000000.0,
        "unswept_stops_between": False,
        "spread_bps": 1.95,
        "regime": "TREND_DOWN",
        "vwap_zscore": -1.2,
        "realized_equity": 4846.32,
        "stressed_equity": 4826.32,
    }
    cert = certify_pitfalls(clean_state)
    assert cert["certified"] is True
    assert len(cert["violations"]) == 0
    card = generate_certified_markdown_card(cert)
    assert "CERTIFIED PASS" in card
