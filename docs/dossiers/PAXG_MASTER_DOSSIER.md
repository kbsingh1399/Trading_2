# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 16:55:01 IST` (`2026-10-30 11:25:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3970.57` | **Live Ask Quote**: `3970.65` | **Mid Price**: `3970.61`
- **Spread Points**: `8.00` | **Spread BPS**: `0.20 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `3995.10` | VWAP Z-Score: `-1.78` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.34` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `37.70` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4025.83` | Lower -3.00σ Band: `3964.38`
  * Upper +2.51σ Band: `4020.81` | Lower -2.51σ Band: `3969.39`
  * Upper +2.01σ Band: `4015.69` | Lower -2.01σ Band: `3974.52`
  * Upper +2.00σ Band: `4015.59` | Lower -2.00σ Band: `3974.62`
  * Upper +1.28σ Band: `4008.21` | Lower -1.28σ Band: `3981.99`
  * Upper +1.00σ Band: `4005.34` | Lower -1.00σ Band: `3984.86`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3982.65` | EMA-20=`3986.28` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3995.03` (Slope: `+0.0000`) | EMA-100=`4006.17`
  * Institutional Anchors: EMA-144=`4012.56` | EMA-200=`4018.08` (Slope: `-0.1016`) | EMA-233=`4021.44`
- **Range Boundaries**: 24H High=`4039.31` | 24H Low=`3965.22` | Weekly High=`4082.75` | Weekly Low=`3965.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4006.65` (Distance: `-0.92%`)
  * Point of Control (POC) = `3990.50` (Distance: `-0.52%`)
  * Value Area Low (VAL) = `3979.46` (Distance: `-0.24%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4053.37` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`3991.98` | Low=`3969.40`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3954.73` - `3986.49`
  * Optimal Trade Entry (OTE 0.705): `3978.55`
  * Structural Invalidation Anchor (0.786): `4002.37`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3985.59` | `3987.37` | `3985.59` | `3985.59` | `72` | 288,968.66 USD | 3,913.86 USD | `+1.35%` | -51,445.92 USD | `+0.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `3985.59` | `3987.59` | `3984.40` | `3984.80` | `195` | 778,403.25 USD | 135,130.70 USD | `+17.36%` | 83,684.78 USD | `+1.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `3984.80` | `3986.16` | `3984.57` | `3985.14` | `21` | 83,967.23 USD | -6,103.54 USD | `-7.27%` | 77,581.24 USD | `-0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `3986.43` | `3989.15` | `3986.00` | `3986.25` | `111` | 441,579.70 USD | 71,280.94 USD | `+16.14%` | -186,609.99 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3986.25` | `3986.25` | `3981.27` | `3985.58` | `193` | 767,768.18 USD | 131,250.20 USD | `+17.10%` | -55,359.79 USD | `+0.73` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3985.59` | `3987.59` | `3984.40` | `3985.14` | `289` | 1,151,335.16 USD | 132,945.01 USD | `+11.55%` | 77,585.23 USD | `+0.70` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4001.22` | `4002.41` | `3991.51` | `3995.66` | `459` | 1,835,738.77 USD | 110,152.21 USD | `+6.00%` | 73,019.48 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `3995.66` | `3995.82` | `3981.27` | `3985.58` | `724` | 2,887,727.74 USD | -259,947.31 USD | `-9.00%` | -186,927.83 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3985.59` | `3987.59` | `3984.40` | `3985.15` | `289` | 1,151,119.96 USD | 133,160.21 USD | `+11.57%` | -53,767.62 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3985.14` | `3,013` | 12,025,637.55 USD | 524,983.41 USD | `+4.37%` | -53,982.82 USD | `+0.65` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3985.14` | `3,013` | 12,025,637.55 USD | 524,983.41 USD | `+4.37%` | -53,982.82 USD | `+0.65` | **`BULLISH`** | `NEUTRAL CHOP` |

- **Deribit Institutional Options Max Pain & Volatility Surface (21_Tradfye_Orderflow.parquet)**:
  * Options Max Pain Price: `0.000000`
  * Call Wall Strike: `0.000000` | Put Wall Strike: `0.000000`

---

## 5. Institutional Whale Armor, Hyperdash Intel & L2 Depth Ladders
*(Sources: 10_Whale_Orders.parquet, 17_Orderbook.parquet, 12_Hyperdash.parquet, 13_Hyperliquid.parquet, 4_Hyperliquid_Analysis.parquet, 16_Hyperdash_telegram_Intel.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Top Defending Bid Wall: `None` (Unarmored)
  * Top Defending Ask Wall: `None` (Unarmored)
| Side | Wall Price (USD) | Size (Coins) | Depth (USD) | Distance (%) | Persistence | Traded % | Venue | Order ID |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `3970.80` | `3.4993` | 13,895.02 USD | 501,191.96 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `3970.90` | `26.4025` | 104,841.69 USD | 487,296.94 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3971.00` | `0.8948` | 3,553.25 USD | 382,455.26 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3971.10` | `2.8227` | 11,209.22 USD | 378,902.01 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3971.20` | `18.7826` | 74,589.46 USD | 367,692.78 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `3971.30` | `3.9749` | 15,785.52 USD | 293,103.32 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3971.40` | `4.5947` | 18,247.39 USD | 277,317.80 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3971.50` | `12.5080` | 49,675.52 USD | 259,070.41 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `3971.60` | `2.6749` | 10,623.63 USD | 209,394.89 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3971.70` | `2.1806` | 8,660.69 USD | 198,771.25 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3971.80` | `10.7345` | 42,635.29 USD | 190,110.56 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3972.00` | `1.2184` | 4,839.48 USD | 147,475.28 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3972.10` | `7.5508` | 29,992.53 USD | 142,635.79 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3972.20` | `7.5537` | 30,004.81 USD | 112,643.26 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3972.30` | `7.5508` | 29,994.04 USD | 82,638.45 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3972.40` | `11.1915` | 44,457.11 USD | 52,644.41 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `3972.60` | `0.5333` | 2,118.59 USD | 8,187.30 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3972.70` | `0.0034` | 13.51 USD | 6,068.71 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3972.80` | `0.2448` | 972.54 USD | 6,055.20 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3973.00` | `1.2793` | 5,082.66 USD | 5,082.66 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3973.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,973.05` | `0.00%` | `-` |
| `ASK` | `3973.10` | `57.8980` | 230,034.54 USD | 230,034.54 USD | `19 orders` | `+0.00%` | `-` |
| `ASK` | `3973.20` | `10.3235` | 41,017.33 USD | 271,051.87 USD | `6 orders` | `+0.00%` | `-` |
| `ASK` | `3973.30` | `63.0186` | 250,391.80 USD | 521,443.68 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3973.40` | `70.6946` | 280,897.92 USD | 802,341.60 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3973.50` | `6.2303` | 24,756.10 USD | 827,097.70 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3973.60` | `15.6029` | 61,999.68 USD | 889,097.38 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3973.70` | `10.3772` | 41,235.88 USD | 930,333.26 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3973.80` | `7.5508` | 30,005.37 USD | 960,338.63 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `3973.90` | `11.1376` | 44,259.71 USD | 1,004,598.34 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `3974.00` | `82.1657` | 326,526.49 USD | 1,331,124.83 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3974.10` | `11.3251` | 45,007.08 USD | 1,376,131.91 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3974.20` | `34.1132` | 135,572.68 USD | 1,511,704.59 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `3974.30` | `23.9061` | 95,010.01 USD | 1,606,714.60 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `3974.40` | `12.6976` | 50,465.34 USD | 1,657,179.94 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3974.50` | `11.3200` | 44,991.34 USD | 1,702,171.28 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3974.60` | `4.2272` | 16,801.43 USD | 1,718,972.71 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3974.70` | `29.1351` | 115,803.28 USD | 1,834,776.00 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `3974.80` | `10.3767` | 41,245.31 USD | 1,876,021.30 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3974.90` | `7.5487` | 30,005.33 USD | 1,906,026.63 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `3975.00` | `7.1617` | 28,467.76 USD | 1,934,494.39 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,823,658.68 USD | `6,489.82` | `4185.46` | `3980.10` | `27415.71` | 1,339,292.33 USD | `+5.19%` | `4X Cross` |
| `49` | `0x4692...164f` | `SHORT` | 25,088,775.75 USD | `6,303.71` | `4127.22` | `3980.10` | `14287.75` | 928,071.05 USD | `+3.70%` | `5X Cross` |
| `63` | `0xb83d...6e36` | `SHORT` | 23,361,025.63 USD | `5,869.90` | `4228.86` | `3980.10` | `22396.67` | 1,461,996.30 USD | `+6.26%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,217,117.90 USD | `4,828.91` | `4157.43` | `3980.10` | `2260.48` | -858,764.42 USD | `-4.47%` | `25X Cross` |
| `145` | `0x645b...87b8` | `LONG` | 14,108,757.74 USD | `3,545.72` | `4127.81` | `3980.10` | `678.45` | -527,312.06 USD | `-3.74%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,004,547.14 USD | `3,268.21` | `4228.94` | `3980.10` | `4384.91` | 816,531.99 USD | `+6.28%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,141,568.34 USD | `2,800.02` | `4364.62` | `3980.10` | `4212.90` | 1,079,475.80 USD | `+9.69%` | `20X Cross` |
| `261` | `0x41e5...0825` | `SHORT` | 8,755,560.00 USD | `2,200.00` | `4112.20` | `3980.10` | `4287.25` | 291,294.59 USD | `+3.33%` | `20X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,753,800.00 USD | `2,200.00` | `4176.09` | `3980.10` | `2649.18` | -433,619.30 USD | `-4.95%` | `25X Cross` |
| `302` | `0xacb6...efbd` | `SHORT` | 7,861,178.87 USD | `1,975.37` | `4048.55` | `3980.10` | `6697.47` | 136,212.84 USD | `+1.73%` | `6X Cross` |
| `365` | `0xc26c...b8f4` | `LONG` | 6,286,786.21 USD | `1,579.95` | `4075.62` | `3980.10` | `0.000000` | -152,510.76 USD | `-2.43%` | `1X Cross` |
| `562` | `0x63da...8add` | `LONG` | 3,979,100.00 USD | `1,000.00` | `4021.46` | `3980.10` | `3564.79` | -42,360.96 USD | `-1.06%` | `25X Cross` |
| `572` | `0xf3dc...1672` | `LONG` | 3,916,609.97 USD | `984.27` | `4018.39` | `3980.10` | `2839.67` | -38,576.72 USD | `-0.98%` | `20X Cross` |
| `596` | `0x9aa5...58af` | `LONG` | 3,799,522.30 USD | `954.75` | `4279.98` | `3980.10` | `0.000000` | -286,788.49 USD | `-7.55%` | `20X Cross` |
| `675` | `0x4a20...3c26` | `LONG` | 3,332,013.41 USD | `837.40` | `4599.73` | `3980.10` | `0.000000` | -519,806.98 USD | `-15.60%` | `20X Cross` |
| `789` | `0x9c06...0560` | `LONG` | 2,892,613.91 USD | `726.95` | `4002.36` | `3980.10` | `0.000000` | -16,915.35 USD | `-0.58%` | `25X Cross` |
| `831` | `0x0fac...7a0a` | `LONG` | 2,731,592.46 USD | `686.49` | `4290.34` | `3980.10` | `1303.11` | -213,666.24 USD | `-7.82%` | `25X Cross` |
| `858` | `0x354b...6425` | `LONG` | 2,635,651.67 USD | `662.21` | `4004.29` | `3980.10` | `0.000000` | -16,025.03 USD | `-0.61%` | `10X Cross` |
| `899` | `0x625e...a354` | `SHORT` | 2,467,476.00 USD | `620.00` | `4122.81` | `3980.10` | `4279.66` | 88,671.03 USD | `+3.59%` | `20X Cross` |
| `930` | `0xeae3...e8ad` | `SHORT` | 2,387,460.00 USD | `600.00` | `4104.77` | `3980.10` | `4268.74` | 75,405.11 USD | `+3.16%` | `20X Cross` |
| `931` | `0xf285...fa82` | `LONG` | 2,379,983.00 USD | `598.11` | `4146.45` | `3980.10` | `3891.93` | -100,036.56 USD | `-4.20%` | `25X Cross` |
| `936` | `0xd8c5...99b0` | `SHORT` | 2,364,938.15 USD | `594.35` | `4175.35` | `3980.10` | `35412.15` | 116,705.88 USD | `+4.93%` | `4X Cross` |
| `948` | `0x12f7...8750` | `LONG` | 2,330,203.54 USD | `585.61` | `4082.77` | `3980.10` | `2764.14` | -60,713.44 USD | `-2.61%` | `10X Cross` |
| `992` | `0x413c...886c` | `LONG` | 2,226,244.62 USD | `559.47` | `4007.05` | `3980.10` | `0.000000` | -15,582.59 USD | `-0.70%` | `2X Cross` |
| `1100` | `0x61ce...a62b` | `SHORT` | 1,979,616.18 USD | `497.50` | `4071.66` | `3980.10` | `4717.62` | 46,052.61 USD | `+2.33%` | `20X Cross` |
| `1174` | `0x2edd...8179` | `LONG` | 1,867,210.11 USD | `468.69` | `4164.68` | `3984.10` | `0.000000` | -84,728.96 USD | `-4.54%` | `10X Cross` |
| `1219` | `0xead5...69f2` | `LONG` | 1,805,969.17 USD | `453.78` | `4220.88` | `3980.10` | `3539.63` | -109,398.89 USD | `-6.06%` | `5X Isolated` |
| `1273` | `0x7a6d...f79c` | `SHORT` | 1,706,533.42 USD | `428.38` | `4136.09` | `3984.10` | `5328.17` | 65,281.58 USD | `+3.83%` | `10X Cross` |
| `1307` | `0x46fc...1195` | `LONG` | 1,654,762.61 USD | `415.77` | `4051.00` | `3980.10` | `2274.87` | -29,523.04 USD | `-1.78%` | `20X Cross` |
| `1346` | `0x6d15...d374` | `LONG` | 1,591,920.00 USD | `400.00` | `4068.25` | `3980.10` | `3842.50` | -35,380.00 USD | `-2.22%` | `25X Cross` |
| `1347` | `0xee02...309d` | `SHORT` | 1,591,640.00 USD | `400.00` | `4438.84` | `3980.10` | `4203.04` | 183,898.60 USD | `+11.55%` | `25X Isolated` |
| `1376` | `0x51f6...2b39` | `LONG` | 1,559,578.02 USD | `391.48` | `4228.25` | `3984.10` | `627.56` | -95,697.67 USD | `-6.14%` | `10X Cross` |
| `1396` | `0x02a7...fe9f` | `SHORT` | 1,551,849.00 USD | `390.00` | `4055.02` | `3980.10` | `4307.36` | 29,610.25 USD | `+1.91%` | `25X Cross` |
| `1439` | `0x7e77...b8d2` | `SHORT` | 1,512,058.00 USD | `380.00` | `4131.92` | `3980.10` | `4294.17` | 58,071.64 USD | `+3.84%` | `20X Cross` |
| `1458` | `0x72c2...9b37` | `LONG` | 1,484,726.76 USD | `373.13` | `4000.98` | `3980.10` | `3778.73` | -8,166.76 USD | `-0.55%` | `13X Isolated` |
| `1473` | `0x781e...96b7` | `SHORT` | 1,458,086.74 USD | `366.00` | `4358.55` | `3984.10` | `12754.98` | 137,158.26 USD | `+9.41%` | `10X Cross` |
| `1505` | `0xaa44...b844` | `LONG` | 1,432,548.00 USD | `360.00` | `4043.10` | `3980.10` | `3225.94` | -22,969.63 USD | `-1.60%` | `7X Cross` |
| `1616` | `0xa41f...d50a` | `LONG` | 1,309,137.57 USD | `328.96` | `4468.89` | `3980.10` | `3802.85` | -160,960.28 USD | `-12.30%` | `15X Cross` |
| `1668` | `0xbf5a...88ba` | `SHORT` | 1,264,012.38 USD | `317.65` | `4091.80` | `3980.10` | `9957.10` | 35,770.65 USD | `+2.83%` | `20X Cross` |
| `1709` | `0xff31...ff6c` | `SHORT` | 1,233,490.00 USD | `310.00` | `4372.43` | `3980.10` | `4789.84` | 121,965.38 USD | `+9.89%` | `10X Isolated` |
| `1734` | `0xada6...6f88` | `LONG` | 1,207,523.55 USD | `303.47` | `4166.46` | `3980.10` | `1812.67` | -56,858.90 USD | `-4.71%` | `5X Cross` |
| `1889` | `0x50e2...d770` | `LONG` | 1,075,791.88 USD | `270.37` | `4243.58` | `3980.10` | `2562.78` | -71,534.58 USD | `-6.65%` | `20X Cross` |
| `1906` | `0x4c92...4f17` | `SHORT` | 1,061,280.87 USD | `266.72` | `4260.98` | `3980.10` | `6482.84` | 75,211.37 USD | `+7.09%` | `20X Cross` |
| `1983` | `0xd346...c4f3` | `LONG` | 1,015,387.58 USD | `255.17` | `4188.66` | `3980.10` | `3311.11` | -53,448.92 USD | `-5.26%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4089.00` | 1,227.52 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 1.23K USD at 4089.0000 USD [API] | `2026-10-07 12:28:33` |
| `ANNOUNCEMENT` | `INFO` | `4089.00` | 12,789.57 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 12.79K USD at 4089.0000 USD [API | `2026-10-07 12:28:33` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4096.30` (Vol: 350,100.00 USD, Dist: `+2.84%`) | Long MP=`3937.38` (Vol: 356,200.00 USD, Dist: `--1.15%`)
  * 48H Horizon: Short MP=`4111.27` (Vol: 328,300.00 USD, Dist: `+3.22%`) | Long MP=`3936.60` (Vol: 378,100.00 USD, Dist: `--1.17%`)
  * 3D Horizon: Short MP=`4111.27` (Vol: 367,600.00 USD, Dist: `+3.22%`) | Long MP=`3949.08` (Vol: 404,600.00 USD, Dist: `--0.85%`)
  * 7D Horizon: Short MP=`4086.31` (Vol: 853,900.00 USD, Dist: `+2.59%`) | Long MP=`3927.24` (Vol: 1,100,000.00 USD, Dist: `--1.40%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3584.80` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3585.50` | 5,800,000.00 USD | 5,800,000.00 USD | 6,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3589.10` | 14,910,000.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3589.60` | 5,800,000.00 USD | 5,800,000.00 USD | 8,470.00 USD | 0.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.40` | 14,890,000.00 USD | 14,890,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3593.70` | 5,780,000.00 USD | 5,780,000.00 USD | 22,620.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.70` | 14,880,000.00 USD | 14,880,000.00 USD | 108,500.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3597.80` | 5,730,000.00 USD | 5,730,000.00 USD | 16,880.00 USD | 0.00 USD | 18,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3601.90` | 5,690,000.00 USD | 5,690,000.00 USD | 28,670.00 USD | 0.00 USD | 36,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3602.00` | 14,750,000.00 USD | 14,750,000.00 USD | 173,930.00 USD | 0.00 USD | 75,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.00` | 5,630,000.00 USD | 5,630,000.00 USD | 58,500.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3606.30` | 14,500,000.00 USD | 14,500,000.00 USD | 152,940.00 USD | 0.00 USD | 43,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.10` | 5,540,000.00 USD | 5,540,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.60` | 14,310,000.00 USD | 14,310,000.00 USD | 72,480.00 USD | 0.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3614.20` | 5,510,000.00 USD | 5,510,000.00 USD | 29,500.00 USD | 0.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3614.90` | 14,210,000.00 USD | 14,210,000.00 USD | 76,990.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.30` | 5,470,000.00 USD | 5,470,000.00 USD | 37,540.00 USD | 0.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.20` | 14,120,000.00 USD | 14,120,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.40` | 5,430,000.00 USD | 5,430,000.00 USD | 50,960.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.50` | 14,060,000.00 USD | 14,060,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3626.50` | 5,370,000.00 USD | 5,370,000.00 USD | 38,770.00 USD | 0.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.80` | 14,000,000.00 USD | 14,000,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.60` | 5,320,000.00 USD | 5,320,000.00 USD | 13,010.00 USD | 0.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.10` | 13,890,000.00 USD | 13,890,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.70` | 5,310,000.00 USD | 5,310,000.00 USD | 7,340.00 USD | 0.00 USD | 204.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.40` | 13,830,000.00 USD | 13,830,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 13,800,000.00 USD | 13,800,000.00 USD | 55,830.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.00` | 13,740,000.00 USD | 13,740,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.30` | 13,700,000.00 USD | 13,700,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.60` | 13,680,000.00 USD | 13,680,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.90` | 13,650,000.00 USD | 13,650,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.20` | 13,610,000.00 USD | 13,610,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.50` | 13,590,000.00 USD | 13,590,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3823.30` | 5,300,000.00 USD | 5,300,000.00 USD | 4,900.00 USD | 0.00 USD | 24,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3825.60` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3827.40` | 5,270,000.00 USD | 5,270,000.00 USD | 33,040.00 USD | 0.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.90` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3831.50` | 5,200,000.00 USD | 5,200,000.00 USD | 21,840.00 USD | 0.00 USD | 69,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3834.20` | 13,470,000.00 USD | 13,470,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3835.60` | 5,110,000.00 USD | 5,110,000.00 USD | 103,760.00 USD | 0.00 USD | 86,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.50` | 13,350,000.00 USD | 13,350,000.00 USD | 334,470.00 USD | 0.00 USD | 99,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3839.70` | 4,920,000.00 USD | 4,920,000.00 USD | 52,420.00 USD | 0.00 USD | 68,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.80` | 12,920,000.00 USD | 12,920,000.00 USD | 569,120.00 USD | 0.00 USD | 199,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3843.80` | 4,800,000.00 USD | 4,800,000.00 USD | 193,270.00 USD | 0.00 USD | 133,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.10` | 12,150,000.00 USD | 12,150,000.00 USD | 416,440.00 USD | 0.00 USD | 143,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3847.90` | 4,470,000.00 USD | 4,470,000.00 USD | 59,930.00 USD | 0.00 USD | 33,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.40` | 11,590,000.00 USD | 11,590,000.00 USD | 257,490.00 USD | 0.00 USD | 74,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.00` | 4,380,000.00 USD | 4,380,000.00 USD | 74,610.00 USD | 0.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.70` | 11,250,000.00 USD | 11,250,000.00 USD | 221,360.00 USD | 0.00 USD | 47,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.10` | 4,270,000.00 USD | 4,270,000.00 USD | 102,960.00 USD | 0.00 USD | 31,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.00` | 10,990,000.00 USD | 10,990,000.00 USD | 147,250.00 USD | 0.00 USD | 28,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.20` | 4,130,000.00 USD | 4,130,000.00 USD | 141,410.00 USD | 0.00 USD | 24,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.30` | 3,970,000.00 USD | 3,970,000.00 USD | 181,210.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.30` | 10,810,000.00 USD | 10,810,000.00 USD | 232,560.00 USD | 0.00 USD | 75,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.40` | 3,760,000.00 USD | 3,760,000.00 USD | 115,210.00 USD | 0.00 USD | 15,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.60` | 10,500,000.00 USD | 10,500,000.00 USD | 285,320.00 USD | 0.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.50` | 3,630,000.00 USD | 3,630,000.00 USD | 50,630.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.90` | 10,190,000.00 USD | 10,190,000.00 USD | 221,120.00 USD | 0.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.60` | 3,570,000.00 USD | 3,570,000.00 USD | 22,590.00 USD | 0.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.20` | 9,930,000.00 USD | 9,930,000.00 USD | 153,170.00 USD | 0.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.70` | 3,540,000.00 USD | 3,540,000.00 USD | 8,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3881.50` | 9,750,000.00 USD | 9,750,000.00 USD | 96,090.00 USD | 0.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3885.80` | 9,630,000.00 USD | 9,630,000.00 USD | 124,650.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.10` | 9,470,000.00 USD | 9,470,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3894.40` | 9,370,000.00 USD | 9,370,000.00 USD | 126,480.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3898.70` | 9,230,000.00 USD | 9,230,000.00 USD | 132,740.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.20` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.00` | 9,090,000.00 USD | 9,090,000.00 USD | 17,060.00 USD | 0.00 USD | 74,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3905.30` | 3,510,000.00 USD | 3,510,000.00 USD | 40,630.00 USD | 0.00 USD | 41,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.30` | 9,000,000.00 USD | 9,000,000.00 USD | 56,630.00 USD | 0.00 USD | 98,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3909.40` | 3,430,000.00 USD | 3,430,000.00 USD | 48,470.00 USD | 0.00 USD | 131,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3911.60` | 8,840,000.00 USD | 8,840,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3913.50` | 3,250,000.00 USD | 3,250,000.00 USD | 185,370.00 USD | 0.00 USD | 107,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3915.90` | 8,710,000.00 USD | 8,710,000.00 USD | 287,340.00 USD | 0.00 USD | 173,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3917.60` | 2,960,000.00 USD | 2,960,000.00 USD | 67,240.00 USD | 0.00 USD | 164,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.20` | 8,250,000.00 USD | 8,250,000.00 USD | 731,980.00 USD | 0.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3921.70` | 2,730,000.00 USD | 2,730,000.00 USD | 178,090.00 USD | 0.00 USD | 207,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3924.50` | 7,340,000.00 USD | 7,340,000.00 USD | 1,280,000.00 USD | 0.00 USD | 465,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3925.80` | 2,340,000.00 USD | 2,340,000.00 USD | 362,630.00 USD | 0.00 USD | 224,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3928.80` | 5,590,000.00 USD | 5,590,000.00 USD | 723,280.00 USD | 0.00 USD | 185,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3929.90` | 1,760,000.00 USD | 1,760,000.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.10` | 4,680,000.00 USD | 4,680,000.00 USD | 340,890.00 USD | 0.00 USD | 133,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.00` | 1,640,000.00 USD | 1,640,000.00 USD | 230,830.00 USD | 0.00 USD | 69,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3937.40` | 4,210,000.00 USD | 4,210,000.00 USD | 466,400.00 USD | 0.00 USD | 56,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.10` | 1,340,000.00 USD | 1,340,000.00 USD | 193,170.00 USD | 0.00 USD | 49,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3941.70` | 3,680,000.00 USD | 3,680,000.00 USD | 312,800.00 USD | 0.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.20` | 1,100,000.00 USD | 1,100,000.00 USD | 295,220.00 USD | 0.00 USD | 61,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.00` | 3,260,000.00 USD | 3,260,000.00 USD | 494,480.00 USD | 0.00 USD | 111,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.30` | 743,440.00 USD | 743,440.00 USD | 348,200.00 USD | 0.00 USD | 44,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.30` | 2,650,000.00 USD | 2,650,000.00 USD | 498,180.00 USD | 0.00 USD | 72,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.40` | 350,580.00 USD | 350,580.00 USD | 217,030.00 USD | 0.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.50` | 113,320.00 USD | 113,320.00 USD | 39,990.00 USD | 0.00 USD | 15,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3954.60` | 2,080,000.00 USD | 2,080,000.00 USD | 417,480.00 USD | 0.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.60` | 57,760.00 USD | 57,760.00 USD | 56,110.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.90` | 1,610,000.00 USD | 1,610,000.00 USD | 275,800.00 USD | 0.00 USD | 41,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.20` | 1,290,000.00 USD | 1,290,000.00 USD | 303,170.00 USD | 0.00 USD | 57,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.50` | 930,280.00 USD | 930,280.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.80` | 753,000.00 USD | 753,000.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.10` | 488,070.00 USD | 488,070.00 USD | 237,870.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.40` | 236,810.00 USD | 236,810.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3984.70` | 59,830.00 USD | 59,830.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3989.00` | 110,560.00 USD | 110,560.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4061.10` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 48,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4062.10` | 171,510.00 USD | 171,510.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4065.20` | 133,280.00 USD | 133,280.00 USD | 40,630.00 USD | 0.00 USD | 44,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4066.40` | 259,800.00 USD | 259,800.00 USD | 0.00 USD | 0.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4069.30` | 299,470.00 USD | 299,470.00 USD | 62,340.00 USD | 0.00 USD | 103,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4070.70` | 373,790.00 USD | 373,790.00 USD | 34,460.00 USD | 0.00 USD | 79,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4073.40` | 573,720.00 USD | 573,720.00 USD | 171,510.00 USD | 0.00 USD | 102,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.00` | 655,770.00 USD | 655,770.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4077.50` | 801,740.00 USD | 801,740.00 USD | 67,240.00 USD | 0.00 USD | 160,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.30` | 1,630,000.00 USD | 1,630,000.00 USD | 793,160.00 USD | 0.00 USD | 181,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4081.60` | 1,190,000.00 USD | 1,190,000.00 USD | 178,090.00 USD | 0.00 USD | 211,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4083.60` | 3,170,000.00 USD | 3,170,000.00 USD | 1,120,000.00 USD | 0.00 USD | 427,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4085.70` | 1,770,000.00 USD | 1,770,000.00 USD | 362,630.00 USD | 0.00 USD | 213,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4087.90` | 4,100,000.00 USD | 4,100,000.00 USD | 730,150.00 USD | 0.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4089.80` | 1,890,000.00 USD | 1,890,000.00 USD | 70,210.00 USD | 0.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.20` | 4,790,000.00 USD | 4,790,000.00 USD | 535,480.00 USD | 0.00 USD | 149,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4093.90` | 2,150,000.00 USD | 2,150,000.00 USD | 195,060.00 USD | 0.00 USD | 60,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4096.50` | 5,270,000.00 USD | 5,270,000.00 USD | 394,180.00 USD | 0.00 USD | 95,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.00` | 2,340,000.00 USD | 2,340,000.00 USD | 155,660.00 USD | 0.00 USD | 38,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4100.80` | 5,640,000.00 USD | 5,640,000.00 USD | 322,520.00 USD | 0.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.10` | 2,710,000.00 USD | 2,710,000.00 USD | 303,270.00 USD | 0.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.10` | 6,180,000.00 USD | 6,180,000.00 USD | 408,250.00 USD | 0.00 USD | 134,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.20` | 3,150,000.00 USD | 3,150,000.00 USD | 385,320.00 USD | 0.00 USD | 49,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4109.40` | 6,760,000.00 USD | 6,760,000.00 USD | 504,830.00 USD | 0.00 USD | 76,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.30` | 3,360,000.00 USD | 3,360,000.00 USD | 184,120.00 USD | 0.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4113.70` | 7,270,000.00 USD | 7,270,000.00 USD | 437,970.00 USD | 0.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.40` | 3,470,000.00 USD | 3,470,000.00 USD | 94,260.00 USD | 0.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.00` | 7,610,000.00 USD | 7,610,000.00 USD | 282,440.00 USD | 0.00 USD | 57,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.50` | 3,510,000.00 USD | 3,510,000.00 USD | 38,710.00 USD | 0.00 USD | 4,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.30` | 7,920,000.00 USD | 7,920,000.00 USD | 286,850.00 USD | 0.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.60` | 3,530,000.00 USD | 3,530,000.00 USD | 24,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4126.60` | 8,230,000.00 USD | 8,230,000.00 USD | 221,890.00 USD | 0.00 USD | 86,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4130.90` | 8,450,000.00 USD | 8,450,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.20` | 8,680,000.00 USD | 8,680,000.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.00` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4139.50` | 8,880,000.00 USD | 8,880,000.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.10` | 3,570,000.00 USD | 3,570,000.00 USD | 17,190.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.80` | 9,130,000.00 USD | 9,130,000.00 USD | 199,160.00 USD | 0.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.20` | 3,640,000.00 USD | 3,640,000.00 USD | 27,370.00 USD | 0.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.10` | 9,280,000.00 USD | 9,280,000.00 USD | 59,830.00 USD | 0.00 USD | 88,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4151.30` | 3,750,000.00 USD | 3,750,000.00 USD | 27,060.00 USD | 0.00 USD | 77,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4152.40` | 9,480,000.00 USD | 9,480,000.00 USD | 133,610.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4155.40` | 3,910,000.00 USD | 3,910,000.00 USD | 91,930.00 USD | 0.00 USD | 73,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.70` | 9,810,000.00 USD | 9,810,000.00 USD | 268,170.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4159.50` | 4,030,000.00 USD | 4,030,000.00 USD | 52,420.00 USD | 0.00 USD | 58,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.00` | 10,360,000.00 USD | 10,360,000.00 USD | 420,240.00 USD | 0.00 USD | 134,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4163.60` | 4,300,000.00 USD | 4,300,000.00 USD | 142,390.00 USD | 0.00 USD | 129,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.30` | 11,050,000.00 USD | 11,050,000.00 USD | 485,080.00 USD | 0.00 USD | 204,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4167.70` | 4,450,000.00 USD | 4,450,000.00 USD | 110,820.00 USD | 0.00 USD | 44,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.60` | 11,490,000.00 USD | 11,490,000.00 USD | 356,490.00 USD | 0.00 USD | 75,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4171.80` | 4,530,000.00 USD | 4,530,000.00 USD | 43,850.00 USD | 0.00 USD | 30,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.90` | 11,710,000.00 USD | 11,710,000.00 USD | 156,630.00 USD | 0.00 USD | 66,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4175.90` | 4,650,000.00 USD | 4,650,000.00 USD | 93,280.00 USD | 0.00 USD | 31,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.20` | 11,970,000.00 USD | 11,970,000.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.00` | 4,770,000.00 USD | 4,770,000.00 USD | 96,160.00 USD | 0.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,150,000.00 USD | 12,150,000.00 USD | 143,730.00 USD | 0.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.10` | 4,960,000.00 USD | 4,960,000.00 USD | 157,730.00 USD | 0.00 USD | 32,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.80` | 12,440,000.00 USD | 12,440,000.00 USD | 219,060.00 USD | 0.00 USD | 65,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.20` | 5,130,000.00 USD | 5,130,000.00 USD | 149,840.00 USD | 0.00 USD | 20,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.10` | 12,720,000.00 USD | 12,720,000.00 USD | 254,710.00 USD | 0.00 USD | 31,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.30` | 5,240,000.00 USD | 5,240,000.00 USD | 108,520.00 USD | 0.00 USD | 9,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.40` | 12,960,000.00 USD | 12,960,000.00 USD | 205,140.00 USD | 0.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.40` | 5,270,000.00 USD | 5,270,000.00 USD | 20,000.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.70` | 13,130,000.00 USD | 13,130,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.50` | 5,300,000.00 USD | 5,300,000.00 USD | 28,060.00 USD | 0.00 USD | 824.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.00` | 13,270,000.00 USD | 13,270,000.00 USD | 116,920.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.30` | 13,400,000.00 USD | 13,400,000.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.60` | 13,500,000.00 USD | 13,500,000.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.90` | 13,610,000.00 USD | 13,610,000.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.20` | 13,740,000.00 USD | 13,740,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.50` | 13,820,000.00 USD | 13,820,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.80` | 13,860,000.00 USD | 13,860,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.10` | 13,920,000.00 USD | 13,920,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4238.40` | 13,930,000.00 USD | 13,930,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4376.80` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.30` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4380.90` | 5,310,000.00 USD | 5,310,000.00 USD | 1,960.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4385.00` | 5,330,000.00 USD | 5,330,000.00 USD | 10,740.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4388.90` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4389.10` | 5,350,000.00 USD | 5,350,000.00 USD | 7,110.00 USD | 0.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4393.20` | 5,400,000.00 USD | 5,400,000.00 USD | 28,070.00 USD | 0.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4393.20` | 13,990,000.00 USD | 13,990,000.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4397.30` | 5,420,000.00 USD | 5,420,000.00 USD | 6,970.00 USD | 0.00 USD | 13,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.50` | 14,100,000.00 USD | 14,100,000.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4399.90` | 5,460,000.00 USD | 5,460,000.00 USD | 18,280.00 USD | 0.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.80` | 14,310,000.00 USD | 14,310,000.00 USD | 143,560.00 USD | 0.00 USD | 66,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.10` | 14,480,000.00 USD | 14,480,000.00 USD | 125,560.00 USD | 0.00 USD | 45,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4410.40` | 14,600,000.00 USD | 14,600,000.00 USD | 103,520.00 USD | 0.00 USD | 18,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.70` | 14,660,000.00 USD | 14,660,000.00 USD | 36,920.00 USD | 0.00 USD | 17,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.00` | 14,730,000.00 USD | 14,730,000.00 USD | 66,780.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.30` | 14,790,000.00 USD | 14,790,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4424.00` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | `Tier 1 CEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3584.80` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `3585.50` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 6,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3589.10` | 14,910,000.00 USD | 0.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3589.60` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 8,470.00 USD | 0.00 USD | 10,730.00 USD |
| `7D` | `3593.40` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3593.70` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 22,620.00 USD | 0.00 USD | 23,990.00 USD |
| `7D` | `3597.70` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 108,500.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3597.80` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 16,880.00 USD | 0.00 USD | 18,980.00 USD |
| `1D` | `3601.90` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 28,670.00 USD | 0.00 USD | 36,250.00 USD |
| `7D` | `3602.00` | 14,750,000.00 USD | 0.00 USD | 14,750,000.00 USD | 173,930.00 USD | 0.00 USD | 75,620.00 USD |
| `1D` | `3606.00` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 58,500.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3606.30` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 152,940.00 USD | 0.00 USD | 43,450.00 USD |
| `1D` | `3610.10` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `3610.60` | 14,310,000.00 USD | 0.00 USD | 14,310,000.00 USD | 72,480.00 USD | 0.00 USD | 20,480.00 USD |
| `1D` | `3614.20` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 29,500.00 USD | 0.00 USD | 11,100.00 USD |
| `7D` | `3614.90` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 76,990.00 USD | 0.00 USD | 16,470.00 USD |
| `1D` | `3618.30` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 37,540.00 USD | 0.00 USD | 4,640.00 USD |
| `7D` | `3619.20` | 14,120,000.00 USD | 0.00 USD | 14,120,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD |
| `1D` | `3622.40` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 50,960.00 USD | 0.00 USD | 10,660.00 USD |
| `7D` | `3623.50` | 14,060,000.00 USD | 0.00 USD | 14,060,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD |
| `1D` | `3626.50` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 38,770.00 USD | 0.00 USD | 5,610.00 USD |
| `7D` | `3627.80` | 14,000,000.00 USD | 0.00 USD | 14,000,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD |
| `1D` | `3630.60` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 13,010.00 USD | 0.00 USD | 3,260.00 USD |
| `7D` | `3632.10` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD |
| `1D` | `3634.70` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 7,340.00 USD | 0.00 USD | 204.34 USD |
| `7D` | `3636.40` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3640.70` | 13,800,000.00 USD | 0.00 USD | 13,800,000.00 USD | 55,830.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3645.00` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `3649.30` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `7D` | `3653.60` | 13,680,000.00 USD | 0.00 USD | 13,680,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3657.90` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3662.20` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3666.50` | 13,590,000.00 USD | 0.00 USD | 13,590,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3823.30` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 4,900.00 USD | 0.00 USD | 24,130.00 USD |
| `7D` | `3825.60` | 13,580,000.00 USD | 0.00 USD | 13,580,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3827.40` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 33,040.00 USD | 0.00 USD | 35,320.00 USD |
| `7D` | `3829.90` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD |
| `1D` | `3831.50` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 21,840.00 USD | 0.00 USD | 69,730.00 USD |
| `7D` | `3834.20` | 13,470,000.00 USD | 0.00 USD | 13,470,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD |
| `1D` | `3835.60` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 103,760.00 USD | 0.00 USD | 86,920.00 USD |
| `7D` | `3838.50` | 13,350,000.00 USD | 0.00 USD | 13,350,000.00 USD | 334,470.00 USD | 0.00 USD | 99,980.00 USD |
| `1D` | `3839.70` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 52,420.00 USD | 0.00 USD | 68,650.00 USD |
| `7D` | `3842.80` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 569,120.00 USD | 0.00 USD | 199,760.00 USD |
| `1D` | `3843.80` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 193,270.00 USD | 0.00 USD | 133,450.00 USD |
| `7D` | `3847.10` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 416,440.00 USD | 0.00 USD | 143,690.00 USD |
| `1D` | `3847.90` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 59,930.00 USD | 0.00 USD | 33,360.00 USD |
| `7D` | `3851.40` | 11,590,000.00 USD | 0.00 USD | 11,590,000.00 USD | 257,490.00 USD | 0.00 USD | 74,890.00 USD |
| `1D` | `3852.00` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 74,610.00 USD | 0.00 USD | 35,310.00 USD |
| `7D` | `3855.70` | 11,250,000.00 USD | 0.00 USD | 11,250,000.00 USD | 221,360.00 USD | 0.00 USD | 47,670.00 USD |
| `1D` | `3856.10` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 102,960.00 USD | 0.00 USD | 31,950.00 USD |
| `7D` | `3860.00` | 10,990,000.00 USD | 0.00 USD | 10,990,000.00 USD | 147,250.00 USD | 0.00 USD | 28,510.00 USD |
| `1D` | `3860.20` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 141,410.00 USD | 0.00 USD | 24,010.00 USD |
| `1D` | `3864.30` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 181,210.00 USD | 0.00 USD | 31,550.00 USD |
| `7D` | `3864.30` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 232,560.00 USD | 0.00 USD | 75,710.00 USD |
| `1D` | `3868.40` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 115,210.00 USD | 0.00 USD | 15,720.00 USD |
| `7D` | `3868.60` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 285,320.00 USD | 0.00 USD | 26,240.00 USD |
| `1D` | `3872.50` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 50,630.00 USD | 0.00 USD | 8,730.00 USD |
| `7D` | `3872.90` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 221,120.00 USD | 0.00 USD | 41,690.00 USD |
| `1D` | `3876.60` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 22,590.00 USD | 0.00 USD | 1,420.00 USD |
| `7D` | `3877.20` | 9,930,000.00 USD | 0.00 USD | 9,930,000.00 USD | 153,170.00 USD | 0.00 USD | 23,330.00 USD |
| `1D` | `3880.70` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 8,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3881.50` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 96,090.00 USD | 0.00 USD | 27,510.00 USD |
| `7D` | `3885.80` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 124,650.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3890.10` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD |
| `7D` | `3894.40` | 9,370,000.00 USD | 0.00 USD | 9,370,000.00 USD | 126,480.00 USD | 0.00 USD | 10,240.00 USD |
| `7D` | `3898.70` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 132,740.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3901.20` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3903.00` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 17,060.00 USD | 0.00 USD | 74,030.00 USD |
| `1D` | `3905.30` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 40,630.00 USD | 0.00 USD | 41,180.00 USD |
| `7D` | `3907.30` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 56,630.00 USD | 0.00 USD | 98,910.00 USD |
| `1D` | `3909.40` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 48,470.00 USD | 0.00 USD | 131,160.00 USD |
| `7D` | `3911.60` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD |
| `1D` | `3913.50` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 185,370.00 USD | 0.00 USD | 107,510.00 USD |
| `7D` | `3915.90` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 287,340.00 USD | 0.00 USD | 173,650.00 USD |
| `1D` | `3917.60` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 67,240.00 USD | 0.00 USD | 164,220.00 USD |
| `7D` | `3920.20` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 731,980.00 USD | 0.00 USD | 181,350.00 USD |
| `1D` | `3921.70` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 178,090.00 USD | 0.00 USD | 207,830.00 USD |
| `7D` | `3924.50` | 7,340,000.00 USD | 0.00 USD | 7,340,000.00 USD | 1,280,000.00 USD | 0.00 USD | 465,510.00 USD |
| `1D` | `3925.80` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 362,630.00 USD | 0.00 USD | 224,770.00 USD |
| `7D` | `3928.80` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 723,280.00 USD | 0.00 USD | 185,470.00 USD |
| `1D` | `3929.90` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD |
| `7D` | `3933.10` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 340,890.00 USD | 0.00 USD | 133,810.00 USD |
| `1D` | `3934.00` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 230,830.00 USD | 0.00 USD | 69,650.00 USD |
| `7D` | `3937.40` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 466,400.00 USD | 0.00 USD | 56,370.00 USD |
| `1D` | `3938.10` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 193,170.00 USD | 0.00 USD | 49,220.00 USD |
| `7D` | `3941.70` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 312,800.00 USD | 0.00 USD | 114,460.00 USD |
| `1D` | `3942.20` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 295,220.00 USD | 0.00 USD | 61,030.00 USD |
| `7D` | `3946.00` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 494,480.00 USD | 0.00 USD | 111,080.00 USD |
| `1D` | `3946.30` | 743,440.00 USD | 0.00 USD | 743,440.00 USD | 348,200.00 USD | 0.00 USD | 44,660.00 USD |
| `7D` | `3950.30` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 498,180.00 USD | 0.00 USD | 72,590.00 USD |
| `1D` | `3950.40` | 350,580.00 USD | 0.00 USD | 350,580.00 USD | 217,030.00 USD | 0.00 USD | 20,230.00 USD |
| `1D` | `3954.50` | 113,320.00 USD | 0.00 USD | 113,320.00 USD | 39,990.00 USD | 0.00 USD | 15,560.00 USD |
| `7D` | `3954.60` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 417,480.00 USD | 0.00 USD | 53,640.00 USD |
| `1D` | `3958.60` | 57,760.00 USD | 0.00 USD | 57,760.00 USD | 56,110.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `3958.90` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 275,800.00 USD | 0.00 USD | 41,700.00 USD |
| `7D` | `3963.20` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 303,170.00 USD | 0.00 USD | 57,060.00 USD |
| `7D` | `3967.50` | 930,280.00 USD | 0.00 USD | 930,280.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `7D` | `3971.80` | 753,000.00 USD | 0.00 USD | 753,000.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `3976.10` | 488,070.00 USD | 0.00 USD | 488,070.00 USD | 237,870.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `3980.40` | 236,810.00 USD | 0.00 USD | 236,810.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD |
| `1D` | `3981.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3983.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3984.70` | 59,830.00 USD | 59,830.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3989.00` | 110,560.00 USD | 110,560.00 USD | 0.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4061.10` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,250.00 USD |
| `7D` | `4062.10` | 171,510.00 USD | 171,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `4065.20` | 133,280.00 USD | 133,280.00 USD | 0.00 USD | 40,630.00 USD | 0.00 USD | 44,390.00 USD |
| `7D` | `4066.40` | 259,800.00 USD | 259,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 88,290.00 USD |
| `1D` | `4069.30` | 299,470.00 USD | 299,470.00 USD | 0.00 USD | 62,340.00 USD | 0.00 USD | 103,860.00 USD |
| `7D` | `4070.70` | 373,790.00 USD | 373,790.00 USD | 0.00 USD | 34,460.00 USD | 0.00 USD | 79,530.00 USD |
| `1D` | `4073.40` | 573,720.00 USD | 573,720.00 USD | 0.00 USD | 171,510.00 USD | 0.00 USD | 102,750.00 USD |
| `7D` | `4075.00` | 655,770.00 USD | 655,770.00 USD | 0.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD |
| `1D` | `4077.50` | 801,740.00 USD | 801,740.00 USD | 0.00 USD | 67,240.00 USD | 0.00 USD | 160,770.00 USD |
| `7D` | `4079.30` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 793,160.00 USD | 0.00 USD | 181,320.00 USD |
| `1D` | `4081.60` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 178,090.00 USD | 0.00 USD | 211,290.00 USD |
| `7D` | `4083.60` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 427,200.00 USD |
| `1D` | `4085.70` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 362,630.00 USD | 0.00 USD | 213,850.00 USD |
| `7D` | `4087.90` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 730,150.00 USD | 0.00 USD | 195,500.00 USD |
| `1D` | `4089.80` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 70,210.00 USD | 0.00 USD | 53,310.00 USD |
| `7D` | `4092.20` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 535,480.00 USD | 0.00 USD | 149,790.00 USD |
| `1D` | `4093.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 195,060.00 USD | 0.00 USD | 60,420.00 USD |
| `7D` | `4096.50` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 394,180.00 USD | 0.00 USD | 95,350.00 USD |
| `1D` | `4098.00` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 155,660.00 USD | 0.00 USD | 38,730.00 USD |
| `7D` | `4100.80` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 322,520.00 USD | 0.00 USD | 42,790.00 USD |
| `1D` | `4102.10` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 303,270.00 USD | 0.00 USD | 67,950.00 USD |
| `7D` | `4105.10` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 408,250.00 USD | 0.00 USD | 134,430.00 USD |
| `1D` | `4106.20` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 385,320.00 USD | 0.00 USD | 49,190.00 USD |
| `7D` | `4109.40` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 504,830.00 USD | 0.00 USD | 76,750.00 USD |
| `1D` | `4110.30` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 184,120.00 USD | 0.00 USD | 25,420.00 USD |
| `7D` | `4113.70` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 437,970.00 USD | 0.00 USD | 63,950.00 USD |
| `1D` | `4114.40` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 94,260.00 USD | 0.00 USD | 15,670.00 USD |
| `7D` | `4118.00` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 282,440.00 USD | 0.00 USD | 57,050.00 USD |
| `1D` | `4118.50` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 38,710.00 USD | 0.00 USD | 4,620.00 USD |
| `7D` | `4122.30` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 286,850.00 USD | 0.00 USD | 30,750.00 USD |
| `1D` | `4122.60` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 24,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4126.60` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 221,890.00 USD | 0.00 USD | 86,130.00 USD |
| `7D` | `4130.90` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD |
| `7D` | `4135.20` | 8,680,000.00 USD | 8,680,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `4139.00` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `4139.50` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4143.10` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 17,190.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `4143.80` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 199,160.00 USD | 0.00 USD | 50,830.00 USD |
| `1D` | `4147.20` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 27,370.00 USD | 0.00 USD | 42,050.00 USD |
| `7D` | `4148.10` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 88,440.00 USD |
| `1D` | `4151.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 27,060.00 USD | 0.00 USD | 77,090.00 USD |
| `7D` | `4152.40` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 133,610.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `4155.40` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 91,930.00 USD | 0.00 USD | 73,830.00 USD |
| `7D` | `4156.70` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 268,170.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4159.50` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 52,420.00 USD | 0.00 USD | 58,400.00 USD |
| `7D` | `4161.00` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 420,240.00 USD | 0.00 USD | 134,730.00 USD |
| `1D` | `4163.60` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 142,390.00 USD | 0.00 USD | 129,270.00 USD |
| `7D` | `4165.30` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 485,080.00 USD | 0.00 USD | 204,730.00 USD |
| `1D` | `4167.70` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 110,820.00 USD | 0.00 USD | 44,760.00 USD |
| `7D` | `4169.60` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 356,490.00 USD | 0.00 USD | 75,190.00 USD |
| `1D` | `4171.80` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 43,850.00 USD | 0.00 USD | 30,380.00 USD |
| `7D` | `4173.90` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 156,630.00 USD | 0.00 USD | 66,900.00 USD |
| `1D` | `4175.90` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 93,280.00 USD | 0.00 USD | 31,990.00 USD |
| `7D` | `4178.20` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD |
| `1D` | `4180.00` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 96,160.00 USD | 0.00 USD | 17,230.00 USD |
| `7D` | `4182.50` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 143,730.00 USD | 0.00 USD | 40,030.00 USD |
| `1D` | `4184.10` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 157,730.00 USD | 0.00 USD | 32,250.00 USD |
| `7D` | `4186.80` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 219,060.00 USD | 0.00 USD | 65,350.00 USD |
| `1D` | `4188.20` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD | 20,960.00 USD |
| `7D` | `4191.10` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 254,710.00 USD | 0.00 USD | 31,760.00 USD |
| `1D` | `4192.30` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 108,520.00 USD | 0.00 USD | 9,300.00 USD |
| `7D` | `4195.40` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 205,140.00 USD | 0.00 USD | 33,460.00 USD |
| `1D` | `4196.40` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 20,000.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `4199.70` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `4200.50` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 28,060.00 USD | 0.00 USD | 824.23 USD |
| `7D` | `4204.00` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 116,920.00 USD | 0.00 USD | 23,560.00 USD |
| `7D` | `4208.30` | 13,400,000.00 USD | 13,400,000.00 USD | 0.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD |
| `7D` | `4212.60` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4216.90` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD |
| `7D` | `4221.20` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `4225.50` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `4229.80` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `7D` | `4234.10` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4238.40` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4376.80` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `4380.30` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4380.90` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD | 5,770.00 USD |
| `1D` | `4385.00` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 10,740.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `4388.90` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4389.10` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 7,110.00 USD | 0.00 USD | 12,700.00 USD |
| `1D` | `4393.20` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 28,070.00 USD | 0.00 USD | 17,360.00 USD |
| `7D` | `4393.20` | 13,990,000.00 USD | 13,990,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `4397.30` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 6,970.00 USD | 0.00 USD | 13,250.00 USD |
| `7D` | `4397.50` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `4399.90` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 18,280.00 USD | 0.00 USD | 19,650.00 USD |
| `7D` | `4401.80` | 14,310,000.00 USD | 14,310,000.00 USD | 0.00 USD | 143,560.00 USD | 0.00 USD | 66,400.00 USD |
| `7D` | `4406.10` | 14,480,000.00 USD | 14,480,000.00 USD | 0.00 USD | 125,560.00 USD | 0.00 USD | 45,370.00 USD |
| `7D` | `4410.40` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 103,520.00 USD | 0.00 USD | 18,970.00 USD |
| `7D` | `4414.70` | 14,660,000.00 USD | 14,660,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 17,590.00 USD |
| `7D` | `4419.00` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | 7,680.00 USD |
| `7D` | `4423.30` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD |
| `7D` | `4424.00` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.50M` | Total OI Tokens: `68,895.4 PAXG`
  * 1h OI Change: `+0.03%` | 4h OI Change: `-0.99%` | 24h OI Change: `-0.35%`
  * Exchange Breakdown: Binance=`104.54M` | Bybit=`24.75M` | OKX=`-` | Hyperliquid=`24.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.70K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0001%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0034%` | **USDT Bitget** | `0.0021%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `44.16%` | `55.84%` | `0.79` | 1,430,000.00 USD |
| `15M` | `Binance` | `50.68%` | `49.32%` | `1.03` | 444,780.00 USD |
| `15M` | `OKX` | `45.28%` | `54.72%` | `0.83` | 131,690.00 USD |
| `15M` | `Bybit` | `39.4%` | `60.6%` | `0.65` | 87,860.00 USD |
| `15M` | `KuCoin` | `46.11%` | `53.89%` | `0.86` | 36,130.00 USD |
| `15M` | `Gate` | `9.48%` | `90.52%` | `0.10` | 147,730.00 USD |
| `15M` | `Bitget` | `6.15%` | `93.85%` | `0.07` | 102,160.00 USD |
| `15M` | `BingX` | `40.89%` | `59.11%` | `0.69` | 41,500.00 USD |
| `15M` | `MEXC` | `39.74%` | `60.26%` | `0.66` | 162,110.00 USD |
| `15M` | `Bitunix` | `38.51%` | `61.49%` | `0.63` | 61,590.00 USD |
| `15M` | `Hyperliquid` | `33.96%` | `66.04%` | `0.51` | 13,910.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.74%` | `50.26%` | `0.99` | 57,240.00 USD |
| `15M` | `Crypto.com` | `99.92%` | `0.08%` | `1249.00` | 1,390.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 135,810.00 USD |
| `15M` | `HTX` | `52%` | `48%` | `1.08` | 8.17 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `8.13%` | `91.87%` | `0.09` | 894.70 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 5.52 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `13.4%` | `86.6%` | `0.15` | 9,580.00 USD |
| `15M` | `Whale Positions` | `50.68%` | `49.32%` | `1.03` | 444,780.00 USD |
| `15M` | `Global Accounts` | `44.16%` | `55.84%` | `0.79` | 1,430,000.00 USD |
| `1H` | `PAXG` | `57.51%` | `42.49%` | `1.35` | 9,090,000.00 USD |
| `1H` | `Binance` | `59.4%` | `40.6%` | `1.46` | 3,200,000.00 USD |
| `1H` | `OKX` | `51.03%` | `48.97%` | `1.04` | 1,220,000.00 USD |
| `1H` | `Bybit` | `65.79%` | `34.21%` | `1.92` | 698,550.00 USD |
| `1H` | `KuCoin` | `52.38%` | `47.62%` | `1.10` | 139,310.00 USD |
| `1H` | `Gate` | `40%` | `60%` | `0.67` | 388,380.00 USD |
| `1H` | `Bitget` | `50.74%` | `49.26%` | `1.03` | 750,960.00 USD |
| `1H` | `BingX` | `32.5%` | `67.5%` | `0.48` | 631,500.00 USD |
| `1H` | `MEXC` | `63.36%` | `36.64%` | `1.73` | 849,360.00 USD |
| `1H` | `Bitunix` | `52.53%` | `47.47%` | `1.11` | 178,940.00 USD |
| `1H` | `Hyperliquid` | `59.86%` | `40.14%` | `1.49` | 110,690.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.16%` | `48.84%` | `1.05` | 258,440.00 USD |
| `1H` | `Crypto.com` | `54.59%` | `45.41%` | `1.20` | 2,570.00 USD |
| `1H` | `WhiteBIT` | `100%` | `0%` | `1.00` | 590,080.00 USD |
| `1H` | `HTX` | `57.71%` | `42.29%` | `1.36` | 323.48 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `37.45%` | `62.55%` | `0.60` | 19,900.00 USD |
| `1H` | `Aster` | `69.29%` | `30.71%` | `2.26` | 108.97 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `8.58%` | `91.42%` | `0.09` | 59,260.00 USD |
| `1H` | `Whale Positions` | `59.4%` | `40.6%` | `1.46` | 3,200,000.00 USD |
| `1H` | `Global Accounts` | `57.51%` | `42.49%` | `1.35` | 9,090,000.00 USD |
| `4H` | `PAXG` | `53.20%` | `46.80%` | `1.14` | 81,030,000.00 USD |
| `4H` | `Binance` | `51.18%` | `48.82%` | `1.05` | 10,220,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `49.67%` | `50.33%` | `0.99` | 7,690,000.00 USD |
| `4H` | `KuCoin` | `37.53%` | `62.47%` | `0.60` | 352,650.00 USD |
| `4H` | `Gate` | `45.58%` | `54.42%` | `0.84` | 2,560,000.00 USD |
| `4H` | `Bitget` | `49.86%` | `50.14%` | `0.99` | 4,190,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `56.33%` | `43.67%` | `1.29` | 47,130,000.00 USD |
| `4H` | `Bitunix` | `50.99%` | `49.01%` | `1.04` | 1,910,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.62%` | `49.38%` | `1.03` | 4,440,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `14.87%` | `85.13%` | `0.17` | 1,840,000.00 USD |
| `4H` | `HTX` | `60.67%` | `39.33%` | `1.54` | 55,860.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `92.04%` | `7.96%` | `11.56` | 646,820.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `51.18%` | `48.82%` | `1.05` | 10,220,000.00 USD |
| `4H` | `Global Accounts` | `53.20%` | `46.80%` | `1.14` | 81,030,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD (XAUUSD.pi) Metal Auction: ROTATION | `4045.64` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -12,410.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -488,620.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -412,180.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -510,530.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -793,520.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,940,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,370,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -459,710.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -504,410.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,800,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,050,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,860,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-12.41K` | 15m=`-488.62K` | 1h=`-510.53K` | 24h=`-1.80M`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
- **Institutional Crypto ETF Capital Flows (1_Crypto_ETF_Flows.parquet)**:
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)

- **High-Impact Macro Economic Events (19_Calendar.parquet)**:
  * `Sun Oct 25` [CHF - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [EUR - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [GBP - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Mon Oct 26` [NZD - Low Impact]: Bank Holiday (Forecast: , Previous: )
  * `Mon Oct 26` [AUD - Low Impact]: RBA Assist Gov Jones Speaks (Forecast: , Previous: )
  * `Mon Oct 26` [EUR - Low Impact]: German ifo Business Climate (Forecast: 90.0, Previous: 89.9)
  * `Mon Oct 26` [GBP - Low Impact]: CBI Realized Sales (Forecast: -47, Previous: -55)
  * `Tue Oct 27` [JPY - Low Impact]: SPPI y/y (Forecast: 3.7%, Previous: 3.5%)
  * `Tue Oct 27` [GBP - Low Impact]: BRC Shop Price Index y/y (Forecast: 1.6%, Previous: 1.4%)
  * `Tue Oct 27` [JPY - Low Impact]: BOJ Core CPI y/y (Forecast: 1.9%, Previous: 1.8%)
  * `Tue Oct 27` [EUR - Low Impact]: Spanish Unemployment Rate (Forecast: 9.9%, Previous: 9.9%)
  * `Tue Oct 27` [EUR - Low Impact]: M3 Money Supply y/y (Forecast: 3.5%, Previous: 3.5%)
  * `Tue Oct 27` [EUR - Low Impact]: Private Loans y/y (Forecast: 3.1%, Previous: 3.1%)
  * `Tue Oct 27` [USD - Low Impact]: ADP Weekly Employment Change (Forecast: , Previous: 17.5K)
  * `Tue Oct 27` [USD - Low Impact]: Core Durable Goods Orders m/m (Forecast: 0.6%, Previous: 0.2%)

- **Breaking Institutional News & Market Intelligence (19_News.parquet)**:
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


---

## 9. TradFi & Interbank Market Mechanics
*(Applicable to Foreign Exchange Majors, Precious Metals, Global Equity Indices, and Commodities)*
- **Central Bank Monetary Policy & Rate Differential**:
  * Prevailing Policy Stance: `Federal Reserve (4.75% - 5.00%) Neutral-Gradualist Stance`
  * 2-Year Sovereign Yield Spread Direction & 10-Year Real Yield Momentum.
- **Interbank Foreign Exchange Mechanics**:
  * London/NY Overlap Window (13:00 - 16:00 UTC): Prime Institutional Liquidity.
  * Rollover Spread Expansion Gate: Execution strictly prohibited between 21:15 UTC and 22:30 UTC.
- **Global Commodity & Index Pricing Drivers**:
  * Precious Metals (XAU/XAG): Real Yield Sensitivity & Geopolitical Safe-Haven Premium.
  * Equity Indices (US30, SP500, NAS100): E-mini Auction VWAP Dispersion & Institutional Gamma Profiles.

---

## 10. Quantitative Trade Formulation & Autonomous Broker Execution Card
*(Sources: Canonical Quant Rules, STANDARDIZED_TRADING_DECISION_CHAIN.md, 10 lethal traps)*
- **Candidate Long Setup (Model 1 / Model 2 VAL Sweep Fade)**:
  * Order Type: `BUY_LIMIT`
  * Execution Entry: `3979.46` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3970.54` (Risk Distance: `8.92` pts)
  * +2.5R Take Profit: `4001.77`
  * Mathematical Lot Sizing: **`1.12 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4006.65` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4015.57` (Risk Distance: `8.92` pts)
  * +2.5R Take Profit: `3984.34`
  * Mathematical Lot Sizing: **`1.12 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4002.37`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
