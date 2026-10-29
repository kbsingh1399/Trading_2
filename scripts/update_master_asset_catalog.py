#!/usr/bin/env python3
"""
scripts/update_master_asset_catalog.py
======================================
Updates Data/metadata/master_asset_catalog.json to comprehensively include
all 156 tradable assets from 00_MT5_Account_Telemetry.parquet.
Preserves existing manual overrides while enriching all newly cataloged symbols.
"""

import json
import pathlib
import datetime
import polars as pl

ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "Data" / "metadata" / "master_asset_catalog.json"
TELEMETRY_PATH = ROOT / "Data" / "feeds" / "00_MT5_Account_Telemetry.parquet"


def get_display_and_meta(broker_sym: str, mid_price: float = None):
    clean = broker_sym.replace(".pi", "").replace(".p", "")
    
    # 1. Metals
    metals_map = {
        "XAUUSD": ("Gold Spot (USD)", "Precious Metal", "Tier 1"),
        "XAGUSD": ("Silver Spot (USD)", "Precious Metal", "Tier 1"),
        "PLATINUM": ("Platinum Spot", "Precious Metal", "Tier 2"),
        "PALLADIUM": ("Palladium Spot", "Precious Metal", "Tier 2"),
        "COPPER": ("High Grade Copper", "Base Metal", "Tier 2"),
        "ALUMINIUM": ("Aluminium", "Base Metal", "Tier 2"),
        "ZINC": ("Zinc", "Base Metal", "Tier 2"),
        "NICKEL": ("Nickel", "Base Metal", "Tier 2"),
        "LEAD": ("Lead", "Base Metal", "Tier 2"),
    }
    for k, (dname, cat, tier) in metals_map.items():
        if k in clean:
            return clean, dname, cat, tier, None, None

    # 2. Commodities / Energy
    energy_map = {
        "USWTI": ("WTI Crude Oil", "Energy / Commodity", "Tier 1"),
        "UKBRENT": ("Brent Crude Oil", "Energy / Commodity", "Tier 1"),
        "GAS": ("Natural Gas", "Energy / Commodity", "Tier 2"),
        "NGAS": ("Natural Gas", "Energy / Commodity", "Tier 2"),
        "GASOLINE": ("RBOB Gasoline", "Energy / Commodity", "Tier 2"),
        "HEATING": ("Heating Oil", "Energy / Commodity", "Tier 2"),
    }
    for k, (dname, cat, tier) in energy_map.items():
        if k in clean:
            return clean, dname, cat, tier, None, None

    # 3. Equity Indices
    indices_map = {
        "SP500": ("S&P 500 Index", "Equity Index", "Tier 1"),
        "US500": ("S&P 500 Index", "Equity Index", "Tier 1"),
        "DJ30": ("Dow Jones 30 Index", "Equity Index", "Tier 1"),
        "US30": ("Dow Jones 30 Index", "Equity Index", "Tier 1"),
        "NAS100": ("Nasdaq 100 Index", "Equity Index", "Tier 1"),
        "USTEC": ("Nasdaq 100 Index", "Equity Index", "Tier 1"),
        "GER40": ("German DAX 40 Index", "Equity Index", "Tier 1"),
        "GER30": ("German DAX Index", "Equity Index", "Tier 1"),
        "UK100": ("FTSE 100 Index", "Equity Index", "Tier 1"),
        "FRA40": ("CAC 40 Index", "Equity Index", "Tier 2"),
        "FR40": ("CAC 40 Index", "Equity Index", "Tier 2"),
        "JP225": ("Nikkei 225 Index", "Equity Index", "Tier 1"),
        "AU200": ("ASX 200 Index", "Equity Index", "Tier 2"),
        "STOXX50": ("Euro Stoxx 50 Index", "Equity Index", "Tier 1"),
        "EU50": ("Euro Stoxx 50 Index", "Equity Index", "Tier 1"),
        "HK50": ("Hang Seng 50 Index", "Equity Index", "Tier 2"),
        "CHINA50": ("China A50 Index", "Equity Index", "Tier 2"),
        "CHINAH": ("Hang Seng China Enterprises Index", "Equity Index", "Tier 2"),
        "US2000": ("Russell 2000 Index", "Equity Index", "Tier 2"),
        "SWISS20": ("Swiss Market Index 20", "Equity Index", "Tier 2"),
        "SWI20": ("Swiss Market Index 20", "Equity Index", "Tier 2"),
        "ES35": ("IBEX 35 Index", "Equity Index", "Tier 2"),
        "IT40": ("FTSE MIB 40 Index", "Equity Index", "Tier 2"),
    }
    for k, (dname, cat, tier) in indices_map.items():
        if k in clean:
            return clean, dname, cat, tier, None, None

    # 4. Crypto Majors & Altcoins
    crypto_names = {
        "BTC": "Bitcoin", "ETH": "Ethereum", "SOL": "Solana", "XRP": "Ripple",
        "BNB": "BNB", "DOGE": "Dogecoin", "ADA": "Cardano", "TRX": "Tron",
        "LINK": "Chainlink", "AVAX": "Avalanche", "SUI": "Sui", "NEAR": "Near Protocol",
        "DOT": "Polkadot", "LTC": "Litecoin", "BCH": "Bitcoin Cash", "APT": "Aptos",
        "OP": "Optimism", "ARB": "Arbitrum", "UNI": "Uniswap", "AAVE": "Aave",
        "AVE": "Aave", "AVX": "Avalanche", "BAR": "FC Barcelona", "BAT": "Basic Attention Token",
        "ALG": "Algorand", "ARW": "Arweave", "ATM": "Atletico Madrid", "AXS": "Axie Infinity",
        "CHZ": "Chiliz", "CRV": "Curve DAO", "EGL": "MultiversX", "EOS": "EOS",
        "FIL": "Filecoin", "FTM": "Fantom", "ICP": "Internet Computer", "MAN": "Decentraland",
        "MAT": "Polygon", "MKR": "Maker", "NEA": "NEAR Protocol", "SAN": "The Sandbox",
        "SHI": "Shiba Inu", "THE": "Theta", "VEC": "VeChain", "WLD": "Worldcoin",
        "XLM": "Stellar", "XMR": "Monero", "YFI": "Yearn Finance", "ZEC": "Zcash", "CEL": "Celsius"
    }
    for sym_prefix, dname in crypto_names.items():
        if clean.startswith(sym_prefix) and clean.endswith("USD"):
            cat = "Crypto Major" if sym_prefix in ["BTC", "ETH", "SOL", "XRP", "BNB"] else "Crypto Altcoin"
            tier = "Tier 1" if cat == "Crypto Major" else "Tier 2"
            base_coin = sym_prefix
            if base_coin == "AVE": base_coin = "AAVE"
            if base_coin == "AVX": base_coin = "AVAX"
            if base_coin == "ALG": base_coin = "ALGO"
            if base_coin == "MAT": base_coin = "MATIC"
            if base_coin == "MAN": base_coin = "MANA"
            if base_coin == "SAN": base_coin = "SAND"
            binance_sym = f"{base_coin}USDT"
            return clean, f"{dname} / USD", cat, tier, binance_sym, base_coin

    # 5. Forex Majors
    fx_majors = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", "NZDUSD"]
    if clean in fx_majors:
        b = clean[:3]
        q = clean[3:]
        return clean, f"{b}/{q}", "Forex Major", "Tier 1", None, None

    # 6. Forex Crosses vs Exotics
    exotic_ccys = ["HKD", "CNH", "SGD", "ZAR", "MXN", "TRY", "SEK", "NOK", "PLN", "HUF", "CZK", "DKK", "THB"]
    if len(clean) == 6:
        b = clean[:3]
        q = clean[3:]
        is_exotic = any(c in clean for c in exotic_ccys)
        cat = "Forex Exotic" if is_exotic else "Forex Cross"
        tier = "Tier 3" if is_exotic else "Tier 2"
        return clean, f"{b}/{q}", cat, tier, None, None

    return clean, clean, "Other Asset", "Tier 2", None, None


def main():
    if not TELEMETRY_PATH.exists():
        print(f"Error: {TELEMETRY_PATH} does not exist.")
        return

    df = pl.read_parquet(TELEMETRY_PATH)
    tradable = df.filter(pl.col("Category") == "SPREAD_GATE")
    print(f"[CatalogUpdate] Ingested {len(tradable)} tradable assets from telemetry.")

    catalog_data = {}
    if CATALOG_PATH.exists():
        with open(CATALOG_PATH, "r", encoding="utf-8") as f:
            catalog_data = json.load(f)

    existing_assets = catalog_data.get("assets", {})
    print(f"[CatalogUpdate] Existing catalog asset count: {len(existing_assets)}")

    updated_assets = dict(existing_assets)

    for row in tradable.iter_rows(named=True):
        broker_sym = row.get("Broker_Symbol")
        mid_price = row.get("Mid_Price")
        
        canonical, dname, cat, tier, binance_sym, hl_sym = get_display_and_meta(broker_sym, mid_price)
        
        # Determine lookup key in catalog
        key = canonical
        # If key already in catalog, preserve and enrich
        if key in updated_assets:
            entry = updated_assets[key]
            entry["mt5_symbol"] = broker_sym
            if mid_price is not None:
                entry["fallback_price"] = float(mid_price)
            continue
        
        # Check if canonical alias exists (e.g. BTC vs BTCUSD)
        found_alias = False
        for ek, ev in updated_assets.items():
            if ev.get("mt5_symbol") == broker_sym or ek == canonical or ek == canonical.replace("USD", ""):
                ev["mt5_symbol"] = broker_sym
                if mid_price is not None:
                    ev["fallback_price"] = float(mid_price)
                found_alias = True
                break
        if found_alias:
            continue

        # New asset entry
        new_entry = {
            "canonical": canonical,
            "display_name": dname,
            "tier": tier,
            "category": cat,
            "coinglass_slug": canonical if "Crypto" in cat else None,
            "title_tokens": [canonical, dname.split("/")[0].strip() if "/" in dname else dname],
            "binance_symbol": binance_sym,
            "hl_symbol": hl_sym,
            "mt5_symbol": broker_sym,
            "fallback_price": float(mid_price) if mid_price is not None else 0.0,
        }
        updated_assets[key] = new_entry

    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    output_catalog = {
        "version": "2.0.0",
        "updated_at": now_utc,
        "total_tradable_assets": len(updated_assets),
        "assets": updated_assets
    }

    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        json.dump(output_catalog, f, indent=2)

    print(f"[CatalogUpdate] Successfully updated {CATALOG_PATH}!")
    print(f"[CatalogUpdate] Total assets now cataloged: {len(updated_assets)}")


if __name__ == "__main__":
    main()
