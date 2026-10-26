#!/usr/bin/env python3
"""
Terminal/Data_Factory/asset_registry.py
=======================================
Unified Dynamic Asset Registry & Multi-Venue Reference Price Resolver.

Provides canonical symbol normalization, venue capability discovery, and hierarchical
reference price resolution (MT5 -> Binance Futures -> Hyperliquid -> Fallback) across:
  - Tier 1: 18 Institutional Binance USDT-M Perpetuals
  - Tier 2: Tokenized Gold & Commodities (XAUT, PAXG, XAUUSD, XAGUSD, USWTI, UKBRENT)
  - Tier 3: FX Majors & Liquid Crosses (EURUSD, GBPUSD, USDJPY, etc.)
  - Tier 4: Global Indices & Equities (SP500, NAS100, DJ30, GER40)
"""

from __future__ import annotations

import json
import logging
import os
import pathlib
import threading
import time
import urllib.request
from typing import Any

log = logging.getLogger("AssetRegistry")

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]
CATALOG_PATH = PROJECT_ROOT / "Data" / "metadata" / "master_asset_catalog.json"


class AssetRegistry:
    _instance: AssetRegistry | None = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs) -> AssetRegistry:
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self, catalog_path: pathlib.Path | str | None = None):
        if getattr(self, "_initialized", False):
            return
        self.catalog_path = pathlib.Path(catalog_path) if catalog_path else CATALOG_PATH
        self.assets: dict[str, dict[str, Any]] = {}
        self.alias_map: dict[str, str] = {}
        self._price_cache: dict[str, tuple[float, float]] = {}  # symbol -> (price, timestamp)
        self.cache_ttl_sec = 15.0
        self._load_catalog()
        self._initialized = True

    def _load_catalog(self):
        """Loads canonical catalog from JSON file."""
        if not self.catalog_path.exists():
            log.warning(f"Catalog path {self.catalog_path} does not exist. Using empty asset roster.")
            return

        try:
            with open(self.catalog_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assets = data.get("assets", {})

            # Build alias map
            for canonical, info in self.assets.items():
                self.alias_map[canonical.upper()] = canonical
                display = info.get("display_name", "")
                if display:
                    self.alias_map[display.upper()] = canonical
                slug = info.get("coinglass_slug", "")
                if slug:
                    self.alias_map[slug.upper()] = canonical
                binance_sym = info.get("binance_symbol", "")
                if binance_sym:
                    self.alias_map[binance_sym.upper()] = canonical
                    self.alias_map[binance_sym.replace("USDT", "").upper()] = canonical
                hl_sym = info.get("hl_symbol", "")
                if hl_sym:
                    self.alias_map[hl_sym.upper()] = canonical
                mt5_sym = info.get("mt5_symbol", "")
                if mt5_sym:
                    self.alias_map[mt5_sym.upper()] = canonical
                    self.alias_map[mt5_sym.replace(".pi", "").replace(".p", "").upper()] = canonical
                for tok in info.get("title_tokens", []):
                    self.alias_map[tok.upper()] = canonical

            log.info(f"Loaded {len(self.assets)} assets and {len(self.alias_map)} alias mappings from {self.catalog_path}")
        except Exception as e:
            log.error(f"Failed to load catalog from {self.catalog_path}: {e}")

    def canonical(self, symbol_or_alias: str) -> str:
        """Returns the canonical symbol for any symbol or alias, defaulting to uppercase input."""
        cleaned = symbol_or_alias.strip().upper()
        return self.alias_map.get(cleaned, cleaned)

    def get_asset_info(self, symbol_or_alias: str) -> dict[str, Any] | None:
        """Returns the full metadata dictionary for an asset."""
        can = self.canonical(symbol_or_alias)
        return self.assets.get(can)

    def get_all_canonical_symbols(self) -> list[str]:
        """Returns all canonical symbols in the catalog."""
        return list(self.assets.keys())

    def get_assets_by_tier(self, tiers: list[str]) -> list[str]:
        """Returns list of canonical symbols belonging to any of the specified tiers."""
        norm_tiers = {t.strip().lower() for t in tiers}
        matched = []
        for sym, info in self.assets.items():
            tier = info.get("tier", "").strip().lower()
            if tier in norm_tiers or any(t in tier for t in norm_tiers):
                matched.append(sym)
        return matched

    def get_assets_for_collector(self, collector_name: str) -> list[str]:
        """Returns the tailored list of canonical symbols for a specific collector."""
        cname = collector_name.lower()
        if "liquidation_map" in cname or "8_exchange" in cname:
            # 18 Tier 1 cryptos + Tokenized Gold + Liquid FX Majors available on Bybit
            return [
                "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "TRX", "LINK", "AVAX",
                "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB",
                "XAUT", "PAXG", "EURUSD", "GBPUSD", "USDJPY"
            ]
        elif "spot_netflow" in cname or "2_spot" in cname:
            # Tier 1 + Tokenized Gold
            return [
                "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "TRX", "LINK", "AVAX",
                "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB", "XAUT", "PAXG"
            ]
        elif "ls_ratio" in cname or "3_exchanges" in cname:
            return [
                "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "TRX", "LINK", "AVAX",
                "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB", "XAUT", "PAXG"
            ]
        elif "5_oi" in cname or "open_interest" in cname:
            return [
                "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "TRX", "LINK", "AVAX",
                "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB", "XAUT", "PAXG"
            ]
        elif "technical" in cname or "11_technical" in cname:
            return list(self.assets.keys())
        elif "cvd" in cname or "18_cvd" in cname:
            return list(self.assets.keys())
        elif "auction" in cname or "20_auction" in cname:
            return list(self.assets.keys())
        elif "orderbook" in cname or "17_orderbook" in cname:
            return [
                "BTC", "ETH", "SOL", "XRP", "BNB", "DOGE", "ADA", "TRX", "LINK", "AVAX",
                "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB", "PAXG", "XAUT"
            ]
        elif "hyperdash" in cname or "hyperliquid" in cname:
            return [
                "BTC", "ETH", "SOL", "XRP", "BNB", "DOGE", "ADA", "TRX", "LINK", "AVAX",
                "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB"
            ]
        # Default fallback: Tier 1
        return self.get_assets_by_tier(["Tier 1"])

    def resolve_coinglass_search_term(self, symbol_or_alias: str) -> str:
        """Returns the search query term to input into CoinGlass search boxes."""
        can = self.canonical(symbol_or_alias)
        info = self.assets.get(can)
        if info and info.get("coinglass_slug"):
            return info["coinglass_slug"]
        return can

    def get_expected_title_tokens(self, symbol_or_alias: str) -> list[str]:
        """Returns list of substring tokens expected in CoinGlass chart titles."""
        can = self.canonical(symbol_or_alias)
        info = self.assets.get(can)
        if info and info.get("title_tokens"):
            return info["title_tokens"]
        return [can]

    def get_reference_price(self, symbol_or_alias: str) -> float:
        """
        Hierarchical Reference Price Resolver:
        1. Memory cache (< 15s TTL)
        2. MT5 symbol tick bid/ask (if MetaTrader5 initialized)
        3. Binance Futures ticker REST API
        4. Hyperliquid allMids info REST API
        5. Fallback anchor price from catalog
        """
        can = self.canonical(symbol_or_alias)
        now = time.time()

        # 1. Check Memory Cache
        if can in self._price_cache:
            price, ts = self._price_cache[can]
            if now - ts < self.cache_ttl_sec and price > 0:
                return price

        info = self.assets.get(can, {})
        fallback_p = float(info.get("fallback_price", 1.0))

        # 2. MT5 Symbol Tick (fastest for TradFi, FX, Gold, Indices)
        mt5_sym = info.get("mt5_symbol")
        if mt5_sym:
            try:
                import MetaTrader5 as mt5
                tick = mt5.symbol_info_tick(mt5_sym)
                if tick and tick.bid > 0:
                    mid = (tick.bid + tick.ask) / 2.0
                    self._price_cache[can] = (mid, now)
                    return mid
            except Exception:
                pass

        # 3. Binance Futures Ticker (fastest for Crypto Perpetuals & PAXG)
        binance_sym = info.get("binance_symbol")
        if binance_sym:
            try:
                url = f"https://fapi.binance.com/fapi/v1/ticker/price?symbol={binance_sym}"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=2.5) as resp:
                    data = json.loads(resp.read().decode())
                    if "price" in data:
                        mid = float(data["price"])
                        if mid > 0:
                            self._price_cache[can] = (mid, now)
                            return mid
            except Exception:
                pass

        # 4. Hyperliquid Mids (for HIP-1 perpetuals & crypto)
        hl_sym = info.get("hl_symbol")
        if hl_sym:
            try:
                req_data = json.dumps({"type": "allMids"}).encode("utf-8")
                req = urllib.request.Request(
                    "https://api.hyperliquid.xyz/info",
                    data=req_data,
                    headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req, timeout=2.5) as resp:
                    mids = json.loads(resp.read().decode())
                    clean_hl = hl_sym.replace("xyz:", "")
                    if clean_hl in mids:
                        mid = float(mids[clean_hl])
                        if mid > 0:
                            self._price_cache[can] = (mid, now)
                            return mid
            except Exception:
                pass

        # 5. Return fallback price
        self._price_cache[can] = (fallback_p, now)
        return fallback_p

    def batch_prefetch_binance_prices(self):
        """Batch prefetches all active Binance Futures ticker prices into memory cache."""
        try:
            url = "https://fapi.binance.com/fapi/v1/ticker/price"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=3.5) as resp:
                data = json.loads(resp.read().decode())
                now = time.time()
                for item in data:
                    sym = item.get("symbol", "")
                    if sym.endswith("USDT"):
                        raw_coin = sym.replace("USDT", "")
                        can = self.canonical(raw_coin)
                        try:
                            p = float(item["price"])
                            if p > 0:
                                self._price_cache[can] = (p, now)
                        except (ValueError, TypeError):
                            continue
        except Exception as e:
            log.debug(f"Batch prefetch Binance prices failed: {e}")


# Global Singleton accessor
asset_registry = AssetRegistry()
