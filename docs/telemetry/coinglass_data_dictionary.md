# 📊 COINGLASS DATA DICTIONARY & HARVEST SPECIFICATION
**Last Harvested**: `2026-10-24T03:54:25.014676+00:00` | **Cadence**: `5 Minutes` | **Engine**: `Terminal/Data_Factory/coinglass_harvester.py`

## 1. EXTRACTED DATA DOMAINS & DATA POINTS SUMMARY

| Domain | Endpoint / Page | Extracted Data Points & Metrics | Persistence / Timeline Tracking |
| :--- | :--- | :--- | :--- |
| **Whales** | `/hyperliquid` | Whale User Address, Asset, Side (Long/Short), Notional Position ($USD), Unrealised PnL, Entry Price, Leverage, Liquidation Price, Margin ($USD), Entry Timestamp | **YES**: `duration_hours`, `duration_days` calculated from entry time & tracked in `whale_persistence_ledger.json` |
| **Whales** | `/hl` | 8 Wallet Tiers (Shrimp to Leviathan: Wallets, In Position %, Long/Short notional, Total Position, Winners/Losers, Bias) & 8 PnL Groups (Money Printer to Rekt Master) | Real-time position shifts across capital tiers |
| **Liquidations** | `/liquidation-maxpain` | Asset Symbol, Live Price, Short Max Pain Price ($), Short Max Pain Notional ($M), Distance to Short Max Pain (%), Long Max Pain Price ($), Long Max Pain Notional ($M), Distance to Long Max Pain (%) | 5m cycle tracking of liquidation gravity magnets |
| **Liquidations** | `/liquidations` | 24h Total Liquidation Volume ($USD), Total Long Liquidations ($USD), Total Short Liquidations ($USD), Per-Exchange liquidation breakdown | Exchange liquidation cascades across time |
| **Liquidations** | `/liquidation-levels` | Bitcoin Liquidation Levels Lines & discrete liquidation trigger boundaries | High-density liquidation shelf detection |
| **Liquidations** | `/pro/futures/LiquidationMap` | Cryptocurrency Liquidation Map across major venues | Cross-exchange liquidation cluster concentration |
| **Liquidations** | `/pro/futures/LiquidationHeatMap` | Cumulative Liquidation Heatmap intensity by price level | Identification of high-leverage magnetic liquidity pools |
| **Institutions** | `/etf/bitcoin` | Spot Bitcoin ETF Daily Net Inflows/Outflows ($USD), Cumulative Flows, Individual ETF Holdings (IBIT, FBTC, GBTC, ARKB, BITB), Historical Timeline | Cumulative institutional adoption timeline |
| **Institutions** | `/etf/ethereum` | Spot Ethereum ETF Daily Net Flows ($USD), Total ETH Holdings, Issuer breakdown | Institutional Ethereum accumulation |
| **Sentiment** | `/LongShortRatio` | Global 5m, 15m, 1h, 4h, 24h Long/Short account ratios across Binance, OKX, Bybit | Macro retail vs smart money positioning |
| **Funding** | `/FundingRate` | Predicted and current 8-hour funding rates across BTC, ETH, SOL, altcoins | Cost of carry & funding squeeze indicators |
| **On-Chain** | `/Balance` | Aggregate Bitcoin and Stablecoin reserves held across exchange cold/hot wallets | Exchange reserve depletion / accumulation |
| **On-Chain** | `/pro/i/utxo` | Bitcoin Realized Price UTXO Age Bands (<1d, 1d-1w, 1w-1m, 1m-3m, 3m-6m, 6m-12m, 1y-2y, 2y-3y, 3y-5y, >5y) | **YES**: Realized price per holding duration tier |

## 2. TEMPORAL PERSISTENCE LEDGER SCHEMA (`whale_persistence_ledger.json`)
```json
{
  "BTC_SHORT_0x5b5d..60_76204.7": {
    "asset": "BTC",
    "side": "SHORT",
    "user": "0x5b5d..60",
    "entry_price_raw": "$76204.7 5X Cross",
    "entry_time_raw": "15:36 08-14",
    "entry_time_iso": "2026-08-14T15:36:00+00:00",
    "duration_hours": 1515.35,
    "duration_days": 63.14,
    "cycle_count": 12,
    "notional_usd": 225350000.0,
    "status": "VETERAN_WHALE"
  }
}
```

## 3. INGESTION STATUS & DATA FRESHNESS
- **Latest Ingestion**: `2026-10-24T03:54:25.014676+00:00`
- **Duration**: `41.97 seconds`
- **Sinks**: `C:\Users\SIGMA\Documents\Trading_2\Data\coinglass\latest\coinglass_snapshot.json` and `C:\Users\SIGMA\Documents\Trading_2\Data\coinglass\whale_persistence_ledger.json`