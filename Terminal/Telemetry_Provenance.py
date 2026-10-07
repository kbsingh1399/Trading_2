"""Fail-closed provenance checks for venue-attributed risk observations.

A fresh receipt alone is not proof of an observed order. Model bands and
anonymous aggregated L2 depth must never be promoted into wallet L3 or stops.
"""
from __future__ import annotations


def validate_observed_snapshot(payload):
    """Reject old/model-backed snapshots before the minute Git publisher stages them."""
    if payload.get("protocol") != "omni.telemetry.v3.observed_only" or payload.get("trade_authorization") != "DENIED_UNVERIFIED_ORDERFLOW":
        return False
    assets = payload.get("assets_matrix_24")
    if not isinstance(assets, dict) or len(assets) != 24:
        return False
    for entry in assets.values():
        quote = entry.get("quotes") or {}
        if quote.get("quote_source") not in ("MT5_L1_TICK", "UNAVAILABLE"):
            return False
        if quote.get("quote_source") == "UNAVAILABLE" and any(quote.get(k) is not None for k in ("bid", "ask", "mid", "spread_bps")):
            return False
        book = entry.get("orderbook_live_depth") or {}
        if book.get("whale_walls_l3"):
            return False
        stops = entry.get("structural_stop_clusters") or {}
        liqs = entry.get("reconstructed_liquidations") or {}
        if stops.get("source") != "UNAVAILABLE" or stops.get("top_sell_stop_clusters_below") or stops.get("top_buy_stop_clusters_above"):
            return False
        if liqs.get("source") not in ("UNAVAILABLE", "NOT_APPLICABLE") or liqs.get("top_long_cascade_bands_below") or liqs.get("top_short_squeeze_bands_above"):
            return False
        if (entry.get("pioneer_microstructure_eval") or {}).get("confluence_trade_setup") is not None:
            return False
    return True


def verified_wallet_block(payload, field, now):
    """Return a fresh, sampled Hyperliquid wallet block, otherwise None.

    This is NOT full-market coverage. Liquidation prices in this block are
    exchange-reported *position* prices, not observed liquidation events.
    """
    block = payload.get(field) or {}
    receipt = (payload.get("sources") or {}).get("wallet_risk") or {}
    expected = {"observed_stops": "OBSERVED_STOP_ORDERS",
                "projected_liquidations": "PROJECTED_EXPOSURE"}.get(field)
    if (block.get("kind") != expected or block.get("coverage") != "SAMPLED_WALLETS"
            or receipt.get("coverage") != "SAMPLED_WALLETS"
            or receipt.get("provider") != "HYPERLIQUID_PUBLIC_INFO"):
        return None
    try:
        age = float(now) - float(receipt["observed_at"])
    except (TypeError, ValueError, KeyError):
        return None
    if not 0 <= age <= 60:
        return None
    wallets = set(block.get("wallets") or [])
    if not wallets or any(not isinstance(w, str) or not w.startswith("0x") for w in wallets):
        return None
    bands = block.get("bands") or []
    if any(b.get("address") not in wallets or b.get("kind") != expected for b in bands):
        return None
    if field == "observed_stops":
        # A stop is a trigger at ONE observed price. A price-wide band allocates
        # hidden stop quantities to places where no order was reported.
        try:
            if any(not (float(b["min_px"]) == float(b["max_px"]) == float(b["mid_px"]) > 0)
                   or float(b.get("amount_usd") or 0) <= 0 for b in bands):
                return None
        except (KeyError, ValueError, TypeError):
            return None
    return block


def verified_wallet_l3(payload, now):
    """Require wallet-attributed Hyperdash receipt, not sampled anonymous L2."""
    receipt = (payload.get("sources") or {}).get("l3") or {}
    if receipt.get("provider") != "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT":
        return []
    try:
        age = float(now) - float(receipt["observed_at"])
    except (TypeError, ValueError, KeyError):
        return []
    if not 0 <= age <= 30:
        return []
    return [w for w in payload.get("l3_orders") or []
            if isinstance(w, dict) and str(w.get("address", "")).startswith("0x")]
