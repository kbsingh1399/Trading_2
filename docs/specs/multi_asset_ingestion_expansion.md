# Multi-Asset Ingestion Expansion Implementation Plan

> **For Antigravity:** REQUIRED WORKFLOW: Use `.agent/workflows/execute-plan.md` to execute this plan in single-flow mode.

**Goal:** Expand all 20 Browser CDP Collectors and 12 API Collectors from the legacy 18-crypto asset restriction to the complete institutional multi-asset universe (Cryptos, Tokenized Gold & Commodities, FX Majors & Crosses, Global Indices & Equities), eliminate the Bybit liquidation map exclusion bug, deploy multi-venue reference pricing, and implement single-session multi-timeframe Max Pain tab rotation.

**Architecture:** Implement a unified Dynamic Asset Registry (`Terminal/Data_Factory/asset_registry.py` and `Data/metadata/master_asset_catalog.json`) providing canonical symbol normalization, venue capability discovery, and hierarchical reference price caching (MT5 -> Binance -> Hyperliquid -> CoinGlass). Decouple all 32 collectors from hardcoded lists while maintaining atomic Parquet writing via `parquet_feed_writer.py` to preserve 100% schema backward compatibility.

**Tech Stack:** Python 3.10+, Chrome/Edge DevTools Protocol (CDP), WebSockets, MetaTrader 5 API, Hyperliquid API / Hyperdash GraphQL, Binance Futures REST API, PyArrow / Parquet.

---

## 1. Executive Summary & Problem Diagnosis

### 1.1 The Legacy 18-Asset Bottleneck
Historically, the data pipeline was anchored strictly to 18 Binance USDT-M perpetuals (`BTC, ETH, SOL, XRP, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB`) due to historical backtesting depth (2020–2026). However, the production trading ecosystem now operates across:
- **Blueberry Markets MT5:** 58 Cryptos, 16 Global Indices, 14 Commodities/Metals, 7 FX Majors, 25 FX Crosses.
- **CoinGlass Pro CDP:** Covers multi-exchange perpetuals including Bybit-listed FX perps (EURUSD, GBPUSD), tokenized gold (XAUT, PAXG), tokenized equities (AAPL), and synthetic indices.
- **Hyperliquid L1 & Hyperdash:** Cross-asset HIP-1 perpetuals (Crypto, `xyz:GOLD`, `xyz:SILVER`, `xyz:CL`, `xyz:SP500`, `xyz:QQQ`, `xyz:TSLA`, `xyz:NVDA`).

Hardcoding `DEFAULT_UNIVERSE = [18 assets]` across 12 collector files caused artificial data starvation, preventing cross-asset correlation analysis and multi-market orderflow intelligence.

### 1.2 Forensic Bug Analysis in `8_Exchange_Liquidation_Map_1D.py` & `8_Exchange_Liquidation_Map_7D.py`
Forensic code audit revealed three lethal bugs blocking non-crypto and Bybit-exclusive assets:

1. **Line 363 Exclusion of Bybit-Only Pairs:**
   - In `8_Exchange_Liquidation_Map_1D.py` (and `7D.py`), lines 359-361 compute:
     ```python
     binance_count = sum(1 for r in val["rows"] if r["binanceVal"] > 0)
     okx_count = sum(1 for r in val["rows"] if r["okxVal"] > 0)
     bybit_count = sum(1 for r in val["rows"] if r["bybitVal"] > 0)
     ```
   - But line 363 strictly checks:
     ```python
     if is_bracketed and is_new_chart and is_title_match and (binance_count > 0 or okx_count > 0):
     ```
   - **Root Cause:** If an asset is listed exclusively on Bybit (such as `EURUSD` or `XAUT` Bybit contracts), `binance_count == 0` and `okx_count == 0`. The condition evaluates to `False`, forcing the loop to time out after 35 polls (10.5s) and log: `Integrity check failed: Timed out waiting for valid chart update for EURUSD!`.
   - **The Fix:**
     ```python
     total_exchange_points = binance_count + okx_count + bybit_count
     has_liquidation_data = total_exchange_points > 0 or any((r.get("shortVal") or 0) > 0 or (r.get("longVal") or 0) > 0 for r in val["rows"])
     if is_bracketed and is_new_chart and is_title_match and has_liquidation_data:
     ```

2. **Reference Price Bracketing Race Condition:**
   - `get_binance_reference_prices()` fetches prices from `https://fapi.binance.com/fapi/v1/ticker/price`.
   - For assets not traded on Binance Futures (such as `EURUSD`, `XAUT` on Bybit, `XAUUSD`, `SP500`), Binance returns no data, falling back to `1.0` USD.
   - On line 354: `is_bracketed = (min_p <= expected_price <= max_p)`.
   - For `EURUSD` (Price ~1.123), `min_p` is ~1.10 and `max_p` is ~1.15. `1.10 <= 1.0 <= 1.15` is `False`.
   - For `XAUT` (Price ~4006.8), `min_p` is ~3800 and `max_p` is ~4200. `3800 <= 1.0 <= 4200` is `False`.
   - **Root Cause:** Bracketing fails permanently for all non-Binance assets.
   - **The Fix:** Multi-venue price resolver: query MT5 tick bid/ask first, then Binance, then Hyperliquid mids, and fallback to CoinGlass chart's own detected mid-price if external reference is unavailable.

3. **Title Match Regex Inflexibility:**
   - Line 357: `is_title_match = (sym == "BTC" and ("Bitcoin" in title or "BTC" in title)) or (sym in title)`
   - For `EURUSD`, CoinGlass may render `EUR/USD` or `Euro / US Dollar`.
   - **The Fix:** Canonical alias dictionary resolving `EURUSD` to `["EURUSD", "EUR/USD", "Euro"]`, `XAUT` to `["XAUT", "XAU", "Tether Gold", "Gold"]`.

### 1.3 CoinGlass Liquidation Max Pain Tab Rotation
CoinGlass `/liquidation-maxpain` serves ~747 assets across 15 pages in its React Ant Table. 
The user highlighted:
- Timeframes required: `24H`, `48H`, `3D`, `7D`.
- On the CoinGlass UI, the 7D tab is labeled `1 week`.
- Currently, 4 individual scripts (`9_Liquidation_Max_Pain_24H.py`, `48H.py`, `3D.py`, `7D.py`) each open a separate ephemeral CDP tab, wait 6–10s for page hydration, and scrape.
- **The Optimization:** Single-session tab rotation. A single open CDP tab rotates through `24 hour` -> `48 hour` -> `3 day` -> `1 week`, extracting all 15 pages of candidates per tab and writing to all 4 feeds in a single coordinated pass (< 15 seconds total vs 45+ seconds).

---

## 2. Master Catalog of "All Assets We Have"

### 2.1 The 4-Tier Asset Hierarchy
- **Tier 1: 18 Institutional Binance USDT-M Perpetuals**
  `BTC, ETH, SOL, XRP, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB`
- **Tier 2: Tokenized Gold & Commodities**
  - Gold: `XAUT` (Tether Gold - Bybit/Binance), `PAXG` (Paxos Gold - Binance), `XAUUSD` / `GOLD` (MT5 `XAUUSD.pi`, Hyperliquid `xyz:GOLD`)
  - Silver: `XAGUSD` / `SILVER` (MT5 `XAGUSD.pi`, Hyperliquid `xyz:SILVER`)
  - Energy: `USWTI` / `CL` (MT5 `USWTI.p`, Hyperliquid `xyz:CL`), `UKBRENT` (MT5 `UKBRENT.p`), `GAS` (MT5 `GAS.p`)
  - Industrial & Precious Metals: `COPPER`, `PLATINUM` (`XPTUSD.pi`), `PALLADIUM` (`XPDUSD.pi`), `ALUMINIUM`, `ZINC`, `NICKEL`, `LEAD`
- **Tier 3: FX Majors & Crosses**
  - Majors (7): `EURUSD`, `GBPUSD`, `USDJPY`, `AUDUSD`, `USDCAD`, `USDCHF`, `NZDUSD`
  - Liquid Crosses (25): `EURGBP`, `EURJPY`, `GBPJPY`, `AUDJPY`, `CADJPY`, `CHFJPY`, `EURAUD`, `EURCAD`, `EURCHF`, `EURNZD`, `GBPAUD`, `GBPCAD`, `GBPCHF`, `GBPNZD`, `AUDCAD`, `AUDCHF`, `AUDNZD`, `CADCHF`, `NZDCAD`, `NZDCHF`, `NZDJPY`, `USDCNH`, `USDHKD`, `USDSGD`, `AUDSGD`
- **Tier 4: Global Indices & Tokenized Equities**
  - US Indices: `SP500` (`SP500.p`, `xyz:SP500`), `NAS100` (`NAS100.p`, `xyz:QQQ`), `DJ30` (`DJ30.p`), `US2000` (`US2000.p`)
  - International Indices: `GER40` (`GER40.p`), `UK100`, `FR40`, `JP225`, `AU200`, `STOXX50`, `HK50`, `CHINA50`, `CHINAH`, `NETH25`, `SWISS20`
  - Tokenized Equities: `AAPL`, `TSLA`, `NVDA`, `MSTR`, `KORU`, `SPCX`

### 2.2 Cross-Venue Availability & Routing Matrix

| Canonical Asset | Tier | Class | CoinGlass CDP Slug | Binance API Symbol | Hyperliquid Symbol | MT5 Broker Symbol | Primary Ref Price Source |
|---|---|---|---|---|---|---|---|
| **BTC** | Tier 1 | Crypto Major | `BTC` | `BTCUSDT` | `BTC` | `BTCUSD.pi` | Binance Futures |
| **ETH** | Tier 1 | Crypto Major | `ETH` | `ETHUSDT` | `ETH` | `ETHUSD.pi` | Binance Futures |
| **SOL** | Tier 1 | Crypto Major | `SOL` | `SOLUSDT` | `SOL` | `SOLUSD.p` | Binance Futures |
| **XRP** | Tier 1 | Crypto Major | `XRP` | `XRPUSDT` | `XRP` | `XRPUSD.pi` | Binance Futures |
| **BNB** | Tier 1 | Crypto Major | `BNB` | `BNBUSDT` | `BNB` | `BNBUSD.p` | Binance Futures |
| **DOGE** | Tier 1 | Crypto Meme | `DOGE` | `DOGEUSDT` | `DOGE` | `DOGUSD.p` | Binance Futures |
| **ADA** | Tier 1 | Crypto Alt L1 | `ADA` | `ADAUSDT` | `ADA` | `ADAUSD.p` | Binance Futures |
| **TRX** | Tier 1 | Crypto Alt L1 | `TRX` | `TRXUSDT` | `TRX` | `TRXUSD.p` | Binance Futures |
| **LINK** | Tier 1 | Crypto DeFi | `LINK` | `LINKUSDT` | `LINK` | `LNKUSD.p` | Binance Futures |
| **AVAX** | Tier 1 | Crypto Alt L1 | `AVAX` | `AVAXUSDT` | `AVAX` | `AVXUSD.p` | Binance Futures |
| **SUI** | Tier 1 | Crypto Alt L1 | `SUI` | `SUIUSDT` | `SUI` | `SUIUSD.p` / None | Binance Futures |
| **NEAR** | Tier 1 | Crypto Alt L1 | `NEAR` | `NEARUSDT` | `NEAR` | `NERUSD.p` | Binance Futures |
| **DOT** | Tier 1 | Crypto Alt L1 | `DOT` | `DOTUSDT` | `DOT` | `DOTUSD.pi` | Binance Futures |
| **LTC** | Tier 1 | Crypto PoW | `LTC` | `LTCUSDT` | `LTC` | `LTCUSD.pi` | Binance Futures |
| **BCH** | Tier 1 | Crypto PoW | `BCH` | `BCHUSDT` | `BCH` | `BCHUSD.p` | Binance Futures |
| **APT** | Tier 1 | Crypto Alt L1 | `APT` | `APTUSDT` | `APT` | `APTUSD.p` / None | Binance Futures |
| **OP** | Tier 1 | Crypto Alt L2 | `OP` | `OPUSDT` | `OP` | `OPUSD.p` / None | Binance Futures |
| **ARB** | Tier 1 | Crypto Alt L2 | `ARB` | `ARBUSDT` | `ARB` | `ARBUSD.p` / None | Binance Futures |
| **XAUT** | Tier 2 | Tokenized Gold | `XAUT` | `None` (Spot only) | `None` | `XAUUSD.pi` | Bybit / MT5 Quote |
| **PAXG** | Tier 2 | Tokenized Gold | `PAXG` | `PAXGUSDT` | `None` | `XAUUSD.pi` | Binance Futures |
| **GOLD / XAU** | Tier 2 | Precious Metal | `XAU` / `XAUUSD` | `None` | `xyz:GOLD` | `XAUUSD.pi` | MT5 Quote / Hyperliquid |
| **SILVER / XAG** | Tier 2 | Precious Metal | `XAG` / `XAGUSD` | `None` | `xyz:SILVER` | `XAGUSD.pi` | MT5 Quote / Hyperliquid |
| **USWTI / CL** | Tier 2 | Energy Commodity | `USWTI` / `CL` | `None` | `xyz:CL` | `USWTI.p` | MT5 Quote / Hyperliquid |
| **UKBRENT** | Tier 2 | Energy Commodity | `UKBRENT` | `None` | `None` | `UKBRENT.p` | MT5 Quote |
| **COPPER** | Tier 2 | Industrial Metal | `COPPER` | `None` | `None` | `COPPER.p` | MT5 Quote |
| **EURUSD** | Tier 3 | FX Major | `EURUSD` | `None` | `xyz:EUR` | `EURUSD.pi` | MT5 Quote / Bybit |
| **GBPUSD** | Tier 3 | FX Major | `GBPUSD` | `None` | `xyz:GBP` | `GBPUSD.pi` | MT5 Quote / Bybit |
| **USDJPY** | Tier 3 | FX Major | `USDJPY` | `None` | `xyz:JPY` | `USDJPY.pi` | MT5 Quote / Bybit |
| **AUDUSD** | Tier 3 | FX Major | `AUDUSD` | `None` | `None` | `AUDUSD.pi` | MT5 Quote |
| **USDCAD** | Tier 3 | FX Major | `USDCAD` | `None` | `None` | `USDCAD.pi` | MT5 Quote |
| **USDCHF** | Tier 3 | FX Major | `USDCHF` | `None` | `None` | `USDCHF.pi` | MT5 Quote |
| **NZDUSD** | Tier 3 | FX Major | `NZDUSD` | `None` | `None` | `NZDUSD.pi` | MT5 Quote |
| **EURGBP** | Tier 3 | FX Cross | `EURGBP` | `None` | `None` | `EURGBP.pi` | MT5 Quote |
| **EURJPY** | Tier 3 | FX Cross | `EURJPY` | `None` | `None` | `EURJPY.pi` | MT5 Quote |
| **GBPJPY** | Tier 3 | FX Cross | `GBPJPY` | `None` | `None` | `GBPJPY.pi` | MT5 Quote |
| **SP500 / US500** | Tier 4 | Equity Index US | `SP500` / `SPCX` | `None` | `xyz:SP500` | `SP500.p` | MT5 Quote / Hyperliquid |
| **NAS100 / US100** | Tier 4 | Equity Index Tech | `NAS100` | `None` | `xyz:QQQ` | `NAS100.p` | MT5 Quote / Hyperliquid |
| **DJ30 / US30** | Tier 4 | Equity Index US | `DJ30` | `None` | `None` | `DJ30.p` | MT5 Quote |
| **GER40 / DAX40** | Tier 4 | Equity Index EU | `GER40` | `None` | `None` | `GER40.p` | MT5 Quote |
| **AAPL** | Tier 4 | Tokenized Equity | `AAPL` | `None` | `None` | `None` | CoinGlass DOM / Alpaca |
| **TSLA** | Tier 4 | Tokenized Equity | `TSLA` | `None` | `xyz:TSLA` | `None` | Hyperliquid / CoinGlass |
| **NVDA** | Tier 4 | Tokenized Equity | `NVDA` | `None` | `xyz:NVDA` | `None` | Hyperliquid / CoinGlass |
| **MSTR** | Tier 4 | Tokenized Equity | `MSTR` | `None` | `xyz:MSTR` | `None` | Hyperliquid / CoinGlass |

---

## 3. Dynamic Asset Registry Architecture

### 3.1 Registry Core Module: `Terminal/Data_Factory/asset_registry.py`
A high-speed, thread-safe, singleton asset resolver that caches symbol mappings, aliases, and reference prices.

```python
# Conceptual Architecture for asset_registry.py
class AssetRegistry:
    def __init__(self, catalog_path: Path):
        self.catalog = self.load_catalog(catalog_path)
        self.price_cache = {}
        self.cache_ttl_sec = 10.0

    def get_reference_price(self, canonical_or_alias: str) -> float:
        """
        Hierarchical Price Resolver:
        1. Check memory cache (< 10s fresh)
        2. Query MT5 symbol tick (if MT5 initialized)
        3. Query Binance Futures fapi ticker
        4. Query Hyperliquid allMids info API
        5. Return static anchor / CoinGlass fallback
        """
        ...

    def get_assets_by_tier(self, tiers: list[str]) -> list[dict]: ...
    def get_assets_for_collector(self, collector_name: str) -> list[str]: ...
    def resolve_coinglass_search_term(self, asset: str) -> str: ...
    def get_expected_title_tokens(self, asset: str) -> list[str]: ...
```

### 3.2 Master Catalog JSON: `Data/metadata/master_asset_catalog.json`
Stores the canonical registry persistently with fast JSON deserialization:
- Schema per asset:
  ```json
  {
    "canonical": "XAUT",
    "display_name": "Tether Gold",
    "tier": "Tier 2",
    "category": "Precious Metal",
    "venues": {
      "coinglass_cdp": { "slug": "XAUT", "title_match": ["XAUT", "Tether Gold", "Gold"], "supported_exchanges": ["Bybit", "Binance"] },
      "mt5": { "symbols": ["XAUUSD.pi", "XAUUSD.p", "GOLD"] },
      "binance": { "symbol": null },
      "hyperliquid": { "coin": null }
    },
    "spread_threshold_bps": 5.0,
    "fallback_price": 4000.0
  }
  ```

---

## 4. Implementation Steps: All 20 Browser CDP Collectors

### Collector 1: `1_Crypto_ETF_Flows.py`
- **File:** `Collectors/Browser/1_Crypto_ETF_Flows.py`
- **Changes:**
  - Update `Asset Category` classification on line 25 to tag Multi-Asset, Commodities (Gold/Silver), and Equity ETFs in addition to BTC/ETH/SOL.
  - No dropdown search required; table automatically extracts all listed ETF rows.

### Collector 2: `2_Spot_Netflow_S.py`
- **File:** `Collectors/Browser/2_Spot_Netflow_S.py`
- **Changes:**
  - Replace `DEFAULT_UNIVERSE = [18 assets]` with `get_assets_for_collector("2_Spot_Netflow_S")`.
  - In `harvest_spot_netflows()` line 231, use `asset_registry.resolve_coinglass_search_term(sym)`.
  - In React Fiber dataSource search line 251, check symbol or canonical alias match:
    ```javascript
    const item = f.memoizedProps.dataSource.find(d => d.symbol === '{sym}' || d.baseSymbol === '{sym}');
    ```

### Collectors 3, 4, 5: `3_Exchanges_LS_Ratio_15M.py`, `1H.py`, `4H.py`
- **Files:**
  - `Collectors/Browser/3_Exchanges_LS_Ratio_15M.py`
  - `Collectors/Browser/3_Exchanges_LS_Ratio_1H.py`
  - `Collectors/Browser/3_Exchanges_LS_Ratio_4H.py`
  - `Collectors/Core/coinglass_ls_browser_core.py`
- **Changes:**
  - In `coinglass_ls_browser_core.py` line 45, replace hardcoded `UNIVERSE` with `asset_registry.get_assets_for_collector("3_Exchanges_LS_Ratio")` (includes Tier 1 cryptos + `XAUT`, `PAXG`, `HYPE`).
  - Update line 100 in CDP extraction script: `const targetSymbols = new Set({json.dumps(expanded_universe)});`.

### Collector 6: `4_Hyperliquid_Analysis.py`
- **File:** `Collectors/Browser/4_Hyperliquid_Analysis.py`
- **Changes:**
  - Already iterates through 40 pages (up to 2,000 whale positions).
  - Add asset classification tagging on output records (Crypto, Metal `xyz:GOLD`, Equity `xyz:TSLA`).

### Collector 7: `5_Funding_Rate.py`
- **File:** `Collectors/Browser/5_Funding_Rate.py`
- **Changes:**
  - Remove line 157 filter:
    `const filtered = cur.memoizedProps.dataSource.filter(d => universe.includes(d.symbol));`
  - Change to extract **100% of available funding rates** provided by CoinGlass (hundreds of pairs), or filter against the full catalog.
  - Remove line 172 check `len(raw_data) >= len(symbols) - 2` and replace with `len(raw_data) >= 18`.

### Collector 8: `5_OI.py`
- **File:** `Collectors/Browser/5_OI.py`
- **Changes:**
  - Replace `DEFAULT_UNIVERSE = [18 assets]` with `get_assets_for_collector("5_OI")`.
  - Include tokenized metals (`XAUT`, `PAXG`) and expanded perps.
  - Dynamically format token amounts using `fmt_tokens(val, sym)`.

### Collector 9: `6_Funding_Fee_Settlement.py`
- **File:** `Collectors/Browser/6_Funding_Fee_Settlement.py`
- **Changes:**
  - Already extracts all 19 pages (~950+ pairs).
  - Add category and tier metadata tagging from `asset_registry`.

### Collectors 10 & 11: `7_Liq_Heapmap.py` & `7_Live_Liq.py`
- **Files:**
  - `Collectors/Browser/7_Liq_Heapmap.py`
  - `Collectors/Browser/7_Live_Liq.py`
- **Changes:**
  - Both collectors already extract all stream tiles and live events.
  - Add asset normalization via `canonical_asset(coin)` so that `XAU`, `GOLD`, `EURUSD` map cleanly.

### Collectors 12 & 13: `8_Exchange_Liquidation_Map_1D.py` & `8_Exchange_Liquidation_Map_7D.py`
- **Files:**
  - `Collectors/Browser/8_Exchange_Liquidation_Map_1D.py`
  - `Collectors/Browser/8_Exchange_Liquidation_Map_7D.py`
- **Changes:**
  1. **Fix Line 363 Bug:**
     ```python
     binance_count = sum(1 for r in val["rows"] if r["binanceVal"] > 0)
     okx_count = sum(1 for r in val["rows"] if r["okxVal"] > 0)
     bybit_count = sum(1 for r in val["rows"] if r["bybitVal"] > 0)
     
     total_exchanges = binance_count + okx_count + bybit_count
     has_valid_liqs = total_exchanges > 0 or any((r.get("shortVal") or 0) > 0 or (r.get("longVal") or 0) > 0 for r in val["rows"])
     
     if is_bracketed and is_new_chart and is_title_match and has_valid_liqs:
     ```
  2. **Replace `get_binance_reference_prices()`:**
     Use `asset_registry.get_reference_price(sym)`.
     If reference price is unknown, parse the live mid price directly from the chart's x-axis mid point to prevent false bracketing failures.
  3. **Robust Title Matching:**
     ```python
     expected_tokens = asset_registry.get_expected_title_tokens(sym)
     is_title_match = any(token.lower() in title.lower() for token in expected_tokens)
     ```
  4. **Expand Universe:**
     Loop over all Tier 1 + Tier 2 (`XAUT`, `PAXG`) + Tier 3 (`EURUSD`, `GBPUSD`) assets available on CoinGlass liquidation maps.

### Collectors 14, 15, 16, 17: `9_Liquidation_Max_Pain_24H.py`, `48H.py`, `3D.py`, `7D.py`
- **Files:**
  - `Collectors/Browser/9_Liquidation_Max_Pain_24H.py`
  - `Collectors/Browser/9_Liquidation_Max_Pain_48H.py`
  - `Collectors/Browser/9_Liquidation_Max_Pain_3D.py`
  - `Collectors/Browser/9_Liquidation_Max_Pain_7D.py`
  - `Collectors/Core/liquidation_maxpain_core.py`
- **Changes:**
  1. **Single-Session Tab Rotator:**
     Add `harvest_all_maxpain_timeframes_unified()` to `liquidation_maxpain_core.py`.
     A single open tab clicks:
     - `24 hour` -> wait 1.5s -> extract all ~747 assets -> dump to `9_Liquidation_Max_Pain_24H.parquet`
     - `48 hour` -> wait 1.5s -> extract all ~747 assets -> dump to `9_Liquidation_Max_Pain_48H.parquet`
     - `3 day` -> wait 1.5s -> extract all ~747 assets -> dump to `9_Liquidation_Max_Pain_3D.parquet`
     - `1 week` -> wait 1.5s -> extract all ~747 assets -> dump to `9_Liquidation_Max_Pain_7D.parquet`
  2. Guarantees 100% asset coverage across Crypto, Gold (`XAU`), Equities (`AAPL`), and Indices (`SPCX`) in one rapid sequence.

### Collector 18: `10_Whale_Orders.py`
- **File:** `Collectors/Browser/10_Whale_Orders.py`
- **Changes:**
  - Add asset classification tagging and support non-BTC large orders if present on the page.

### Collectors 19 & 20: `19_Calendar.py` & `19_News.py`
- **Files:**
  - `Collectors/Browser/19_Calendar.py`
  - `Collectors/Browser/19_News.py`
- **Changes:**
  - Tag events with macro asset class (Forex, Central Bank, Commodities, Indices, Crypto).

---

## 5. Implementation Steps: All 12 API Collectors

### Collector 1: `00_MT5_Account_Telemetry.py`
- **File:** `Collectors/API/00_MT5_Account_Telemetry.py`
- **Changes:**
  - Expand universe quote loop to inspect all visible broker symbols and cross-reference with `asset_registry`.
  - Apply adaptive spread gates: TradFi (Indices, FX, Metals, Commodities) <= 5.0 bps; Crypto <= 25.0 bps.

### Collector 2: `11_Technical.py`
- **File:** `Collectors/API/11_Technical.py`
- **Changes:**
  - Replace `ASSET_CATEGORIES` with `asset_registry.get_all_assets()`.
  - Compute Technicals, VWAP bands (Daily anchor & 24H rolling), and EMA ribbons across all 54+ catalog assets.

### Collectors 3, 4, 5, 6: `12_Hyperdash.py`, `13_Hyperliquid.py`, `14_Hyperdash_Liq_Map.py`, `15_Hyperdash_Stops_Map.py`
- **Files:**
  - `Collectors/API/12_Hyperdash.py`
  - `Collectors/API/13_Hyperliquid.py`
  - `Collectors/API/14_Hyperdash_Liq_Map.py`
  - `Collectors/API/15_Hyperdash_Stops_Map.py`
- **Changes:**
  - In `13_Hyperliquid.py`, expand `TOP_WATCHLIST` to include all tradeable assets (Crypto + synthetic `xyz:GOLD`, `xyz:SP500`, `xyz:TSLA`).
  - In `14_Hyperdash_Liq_Map.py` and `15_Hyperdash_Stops_Map.py`, replace `DEFAULT_UNIVERSE = [18 assets]` with all Hyperliquid-supported coins.

### Collector 7: `16_Hyperdash_telegram_Intel.py`
- **File:** `Collectors/API/16_Hyperdash_telegram_Intel.py`
- **Changes:**
  - Enhance regex parser to detect non-crypto assets (e.g. `GOLD`, `CL`, `SP500`, `TSLA`).

### Collector 8: `17_Orderbook.py`
- **File:** `Collectors/API/17_Orderbook.py`
- **Changes:**
  - Expand `DEFAULT_ASSET_ROSTER` on line 64 to include full Tier 1-4 assets available on Hyperliquid/Hyperdash.

### Collector 9: `18_CVD.py`
- **File:** `Collectors/API/18_CVD.py`
- **Changes:**
  - Expand `DEFAULT_ASSET_ROSTER` on line 94 to add missing Forex crosses (`EURJPY`, `GBPJPY`), Precious Metals (`XPTUSD`, `XPDUSD`), and Commodities (`UKBRENT`, `GAS`).
  - Pull Binance taker volume for `PAXGUSDT` and MT5 tick volume for TradFi.

### Collector 10: `20_Auction_Market_Structure.py`
- **File:** `Collectors/API/20_Auction_Market_Structure.py`
- **Changes:**
  - Synchronize `INSTITUTIONAL_ASSETS` with `asset_registry`. Ensure all 54 assets have active Volume Profile, Value Areas, and Session Extremes.

### Collector 11: `21_Tradfye_Orderflow.py`
- **File:** `Collectors/API/21_Tradfye_Orderflow.py`
- **Changes:**
  - Add `PAXGUSDT` (Tokenized Gold) and other high-volume Binance USDT-M pairs to `UNIVERSE_SYMBOLS`.

### Collector 12: `22_Forced_Liquidations_MTF.py`
- **File:** `Collectors/API/22_Forced_Liquidations_MTF.py`
- **Changes:**
  - Aggregator automatically consumes all coins emitted by `7_Live_Liq.parquet`. Verify schema handles cross-asset symbol strings without truncation.

---

## 6. Schema & Parquet Compatibility

1. **Column Preservation:** Every feed preserves its canonical column names and order. Expanding the asset list strictly appends new rows; existing downstream consumers will not break.
2. **Atomic Writes:** All writes proceed through `write_parquet_feed(feed_name, data)` via `os.replace` to prevent race conditions.
3. **Freshness Tracking:** All 33 feeds continue to register completion in `Data/metadata/parquet_all_feeds_checklist.json`, maintaining the strict `< 5.0m` freshness target.

---

## 7. Phased Implementation Roadmap

### Phase 1: Dynamic Asset Registry & Master Catalog
- Task 1.1: Create `Data/metadata/master_asset_catalog.json` with full Tier 1–4 asset specifications.
- Task 1.2: Implement `Terminal/Data_Factory/asset_registry.py` with multi-venue reference pricing and filtering.
- Task 1.3: Create unit tests in `Tests/unit/test_asset_registry.py`.

### Phase 2: CoinGlass Liquidation Map Bug Fix & Expansion
- Task 2.1: Patch `8_Exchange_Liquidation_Map_1D.py` (Line 363 bug, reference pricing, title match, asset list).
- Task 2.2: Patch `8_Exchange_Liquidation_Map_7D.py` with identical fixes.
- Task 2.3: Test harvest for `EURUSD`, `XAUT`, `BTC`, `ETH`.

### Phase 3: Liquidation Max Pain Single-Session Tab Rotation
- Task 3.1: Update `liquidation_maxpain_core.py` to add `harvest_all_maxpain_timeframes_unified()`.
- Task 3.2: Verify tab labels (`24 hour`, `48 hour`, `3 day`, `1 week`).
- Task 3.3: Execute rotation and confirm all 4 Parquet files update with ~747 assets.

### Phase 4: Remaining Browser CDP Expansion
- Task 4.1: Expand `2_Spot_Netflow_S.py` and `coinglass_ls_browser_core.py` (feeds 3_15M, 3_1H, 3_4H).
- Task 4.2: Expand `5_Funding_Rate.py` (unblock all-pairs extraction) and `5_OI.py`.

### Phase 5: API Collectors Expansion
- Task 5.1: Update `11_Technical.py` and `20_Auction_Market_Structure.py` to consume `asset_registry`.
- Task 5.2: Expand `13_Hyperliquid.py`, `14_Hyperdash_Liq_Map.py`, `15_Hyperdash_Stops_Map.py`, `17_Orderbook.py`, `18_CVD.py`, and `21_Tradfye_Orderflow.py`.

### Phase 6: Full-Stack Verification & Freshness Audit
- Task 6.1: Run complete 33-feed telemetry sync.
- Task 6.2: Verify `Data/metadata/parquet_all_feeds_checklist.json` shows all 33 feeds PASS and < 5.0m fresh.

---

## 8. Verification & Testing Protocol

### 8.1 Automated Test Commands
```bash
# 1. Verify Asset Registry Unit Tests
pytest Tests/unit/test_asset_registry.py -v

# 2. Test Bybit-only Liquidation Map Harvest (EURUSD & XAUT)
python Collectors/Browser/8_Exchange_Liquidation_Map_1D.py --symbols EURUSD XAUT BTC ETH

# 3. Test Max Pain Unified Tab Rotation
python Collectors/Core/liquidation_maxpain_core.py --rotate-all-tabs

# 4. Test Funding Rate All-Asset Harvest
python Collectors/Browser/5_Funding_Rate.py

# 5. Full Scorecard Freshness Verification
python Terminal/Data_Factory/parquet_freshness_scorecard.py
```

### 8.2 Success Criteria
- [ ] `8_Exchange_Liquidation_Map_1D` and `7D` harvest `EURUSD` and `XAUT` without timeout.
- [ ] `9_Liquidation_Max_Pain` harvests ~747 multi-asset candidates across 24H, 48H, 3D, 7D.
- [ ] All 33 Parquet feeds update atomically with 0 nulls.
- [ ] Scorecard confirms 100% feed freshness < 5.0m in IST.
