# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 17:19:12 IST` (`2026-10-30 11:49:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `47` | `0x5b5d...c060` | `SHORT` | 25,771,740.09 USD | `6,489.82` | `4185.46` | `3970.10` | `27481.06` | 1,391,210.93 USD | `+5.40%` | `4X Cross` |
| `49` | `0x4692...164f` | `SHORT` | 25,048,354.50 USD | `6,308.30` | `4127.09` | `3970.10` | `14285.16` | 986,571.80 USD | `+3.94%` | `5X Cross` |
| `64` | `0xb83d...6e36` | `SHORT` | 23,309,370.52 USD | `5,869.90` | `4228.86` | `3970.10` | `22464.07` | 1,513,651.42 USD | `+6.49%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,175,589.30 USD | `4,828.91` | `4157.43` | `3970.10` | `2264.16` | -900,293.02 USD | `-4.69%` | `25X Cross` |
| `146` | `0x645b...87b8` | `LONG` | 14,080,392.01 USD | `3,545.72` | `4127.81` | `3970.10` | `677.32` | -555,677.79 USD | `-3.95%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 12,978,401.44 USD | `3,268.21` | `4228.94` | `3970.10` | `4384.52` | 842,677.69 USD | `+6.49%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,118,608.15 USD | `2,800.02` | `4364.62` | `3970.10` | `4212.90` | 1,102,435.98 USD | `+9.92%` | `20X Cross` |
| `265` | `0x3678...b209` | `LONG` | 8,740,600.00 USD | `2,200.00` | `4176.09` | `3970.10` | `2643.89` | -446,819.30 USD | `-5.11%` | `25X Cross` |
| `266` | `0x41e5...0825` | `SHORT` | 8,736,200.00 USD | `2,200.00` | `4112.20` | `3970.10` | `4287.25` | 310,654.59 USD | `+3.56%` | `20X Cross` |
| `305` | `0xacb6...efbd` | `SHORT` | 7,844,190.70 USD | `1,975.37` | `4048.55` | `3970.10` | `6702.53` | 153,201.02 USD | `+1.95%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,274,146.59 USD | `1,579.95` | `4075.62` | `3970.10` | `0.000000` | -165,150.38 USD | `-2.63%` | `1X Cross` |
| `564` | `0x63da...8add` | `LONG` | 3,971,100.00 USD | `1,000.00` | `4021.46` | `3970.10` | `3564.79` | -50,360.96 USD | `-1.27%` | `25X Cross` |
| `575` | `0xf3dc...1672` | `LONG` | 3,909,523.22 USD | `984.27` | `4018.39` | `3970.10` | `2843.04` | -45,663.47 USD | `-1.17%` | `20X Cross` |
| `599` | `0x9aa5...58af` | `LONG` | 3,790,000.23 USD | `954.42` | `4279.98` | `3970.10` | `0.000000` | -294,897.31 USD | `-7.78%` | `20X Cross` |
| `678` | `0x4a20...3c26` | `LONG` | 3,325,900.39 USD | `837.40` | `4599.73` | `3970.10` | `0.000000` | -525,919.99 USD | `-15.81%` | `20X Cross` |
| `773` | `0x9c06...0560` | `LONG` | 2,976,880.09 USD | `749.67` | `4001.53` | `3970.10` | `0.000000` | -22,969.51 USD | `-0.77%` | `25X Cross` |
| `832` | `0x0fac...7a0a` | `LONG` | 2,725,963.29 USD | `686.49` | `4290.34` | `3970.10` | `1249.90` | -219,295.42 USD | `-8.04%` | `25X Cross` |
| `861` | `0x354b...6425` | `LONG` | 2,623,310.06 USD | `660.67` | `4004.29` | `3970.10` | `0.000000` | -22,198.02 USD | `-0.85%` | `10X Cross` |
| `902` | `0x625e...a354` | `SHORT` | 2,462,020.00 USD | `620.00` | `4122.81` | `3970.10` | `4279.66` | 94,127.03 USD | `+3.82%` | `20X Cross` |
| `933` | `0xeae3...e8ad` | `SHORT` | 2,383,200.00 USD | `600.00` | `4104.77` | `3970.10` | `4268.74` | 79,665.11 USD | `+3.34%` | `20X Cross` |
| `935` | `0xf285...fa82` | `LONG` | 2,375,078.53 USD | `598.11` | `4146.45` | `3970.10` | `3891.93` | -104,941.02 USD | `-4.42%` | `25X Cross` |
| `939` | `0xd8c5...99b0` | `SHORT` | 2,360,777.66 USD | `594.35` | `4175.35` | `3970.10` | `35436.27` | 120,866.37 USD | `+5.12%` | `4X Cross` |
| `956` | `0x12f7...8750` | `LONG` | 2,325,518.65 USD | `585.61` | `4082.77` | `3970.10` | `2775.77` | -65,398.33 USD | `-2.81%` | `10X Cross` |
| `994` | `0x413c...886c` | `LONG` | 2,222,216.43 USD | `559.47` | `4007.05` | `3970.10` | `0.000000` | -19,610.78 USD | `-0.88%` | `2X Cross` |
| `1102` | `0x61ce...a62b` | `SHORT` | 1,976,631.16 USD | `497.50` | `4071.66` | `3970.10` | `4717.05` | 49,037.64 USD | `+2.48%` | `20X Cross` |
| `1208` | `0x2edd...8179` | `LONG` | 1,826,376.43 USD | `459.30` | `4164.68` | `3976.10` | `0.000000` | -86,477.13 USD | `-4.73%` | `10X Cross` |
| `1220` | `0xead5...69f2` | `LONG` | 1,801,975.87 USD | `453.78` | `4220.88` | `3970.10` | `3539.63` | -113,392.19 USD | `-6.29%` | `5X Isolated` |
| `1276` | `0x7a6d...f79c` | `SHORT` | 1,704,005.99 USD | `428.38` | `4136.09` | `3976.10` | `5324.23` | 67,809.02 USD | `+3.98%` | `10X Cross` |
| `1304` | `0x46fc...1195` | `LONG` | 1,660,541.16 USD | `418.17` | `4050.55` | `3970.10` | `2293.83` | -33,267.12 USD | `-2.00%` | `20X Cross` |
| `1352` | `0x6d15...d374` | `LONG` | 1,588,400.00 USD | `400.00` | `4068.25` | `3970.10` | `3842.50` | -38,900.00 USD | `-2.45%` | `25X Cross` |
| `1353` | `0xee02...309d` | `SHORT` | 1,588,360.00 USD | `400.00` | `4438.84` | `3970.10` | `4203.04` | 187,178.60 USD | `+11.78%` | `25X Isolated` |
| `1382` | `0x51f6...2b39` | `LONG` | 1,556,759.37 USD | `391.48` | `4228.25` | `3976.10` | `595.04` | -98,516.32 USD | `-6.33%` | `10X Cross` |
| `1401` | `0x02a7...fe9f` | `SHORT` | 1,548,729.00 USD | `390.00` | `4055.02` | `3970.10` | `4307.36` | 32,730.25 USD | `+2.11%` | `25X Cross` |
| `1442` | `0x7e77...b8d2` | `SHORT` | 1,509,360.00 USD | `380.00` | `4131.92` | `3970.10` | `4294.17` | 60,769.64 USD | `+4.03%` | `20X Cross` |
| `1458` | `0x72c2...9b37` | `LONG` | 1,482,077.52 USD | `373.13` | `4000.98` | `3970.10` | `3778.73` | -10,815.99 USD | `-0.73%` | `13X Isolated` |
| `1475` | `0x781e...96b7` | `SHORT` | 1,455,749.75 USD | `366.08` | `4358.47` | `3976.10` | `12815.03` | 139,793.63 USD | `+9.60%` | `10X Cross` |
| `1507` | `0xaa44...b844` | `LONG` | 1,429,920.00 USD | `360.00` | `4043.10` | `3970.10` | `3225.94` | -25,597.63 USD | `-1.79%` | `7X Cross` |
| `1619` | `0xa41f...d50a` | `LONG` | 1,306,308.50 USD | `328.96` | `4468.89` | `3970.10` | `3802.85` | -163,789.35 USD | `-12.54%` | `15X Cross` |
| `1673` | `0xbf5a...88ba` | `SHORT` | 1,261,407.61 USD | `317.65` | `4091.80` | `3970.10` | `9955.84` | 38,375.42 USD | `+3.04%` | `20X Cross` |
| `1714` | `0xff31...ff6c` | `SHORT` | 1,231,258.00 USD | `310.00` | `4372.43` | `3970.10` | `4789.84` | 124,197.38 USD | `+10.09%` | `10X Isolated` |
| `1740` | `0xada6...6f88` | `LONG` | 1,205,368.94 USD | `303.47` | `4166.46` | `3970.10` | `1813.12` | -59,013.52 USD | `-4.90%` | `5X Cross` |
| `1894` | `0x50e2...d770` | `LONG` | 1,073,818.20 USD | `270.37` | `4243.58` | `3970.10` | `2562.78` | -73,508.26 USD | `-6.85%` | `20X Cross` |
| `1906` | `0x4c92...4f17` | `SHORT` | 1,059,173.78 USD | `266.72` | `4260.98` | `3970.10` | `6480.57` | 77,318.46 USD | `+7.30%` | `20X Cross` |
| `1984` | `0xd346...c4f3` | `LONG` | 1,013,269.64 USD | `255.17` | `4188.66` | `3970.10` | `3311.11` | -55,566.87 USD | `-5.48%` | `5X Isolated` |

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
| `1D` | `Long Liquidation` | `3579.70` | 5,920,000.00 USD | 5,920,000.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3583.90` | 5,910,000.00 USD | 5,910,000.00 USD | 1,960.00 USD | 0.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3584.80` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3588.10` | 5,890,000.00 USD | 5,890,000.00 USD | 10,740.00 USD | 0.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3589.10` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3592.30` | 5,870,000.00 USD | 5,870,000.00 USD | 7,110.00 USD | 0.00 USD | 21,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.40` | 14,760,000.00 USD | 14,760,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3596.50` | 5,840,000.00 USD | 5,840,000.00 USD | 35,040.00 USD | 0.00 USD | 19,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.70` | 14,750,000.00 USD | 14,750,000.00 USD | 108,500.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3600.70` | 5,790,000.00 USD | 5,790,000.00 USD | 26,650.00 USD | 0.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3602.00` | 14,620,000.00 USD | 14,620,000.00 USD | 173,930.00 USD | 0.00 USD | 75,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3604.90` | 5,730,000.00 USD | 5,730,000.00 USD | 54,630.00 USD | 0.00 USD | 39,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3606.30` | 14,370,000.00 USD | 14,370,000.00 USD | 152,940.00 USD | 0.00 USD | 43,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3609.10` | 5,640,000.00 USD | 5,640,000.00 USD | 14,040.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.60` | 14,170,000.00 USD | 14,170,000.00 USD | 72,480.00 USD | 0.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3613.30` | 5,620,000.00 USD | 5,620,000.00 USD | 33,240.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3614.90` | 14,080,000.00 USD | 14,080,000.00 USD | 76,990.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3617.50` | 5,570,000.00 USD | 5,570,000.00 USD | 41,740.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.20` | 13,990,000.00 USD | 13,990,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3621.70` | 5,530,000.00 USD | 5,530,000.00 USD | 37,530.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.50` | 13,930,000.00 USD | 13,930,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.90` | 5,480,000.00 USD | 5,480,000.00 USD | 51,070.00 USD | 0.00 USD | 7,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.80` | 13,860,000.00 USD | 13,860,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.10` | 5,420,000.00 USD | 5,420,000.00 USD | 19,470.00 USD | 0.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.10` | 13,760,000.00 USD | 13,760,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.30` | 5,400,000.00 USD | 5,400,000.00 USD | 2,050.00 USD | 0.00 USD | 594.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.40` | 13,690,000.00 USD | 13,690,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 13,670,000.00 USD | 13,670,000.00 USD | 55,830.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.00` | 13,600,000.00 USD | 13,600,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.30` | 13,560,000.00 USD | 13,560,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.60` | 13,540,000.00 USD | 13,540,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.90` | 13,510,000.00 USD | 13,510,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.20` | 13,480,000.00 USD | 13,480,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.50` | 13,460,000.00 USD | 13,460,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3819.10` | 5,390,000.00 USD | 5,390,000.00 USD | 27,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3821.30` | 13,450,000.00 USD | 13,450,000.00 USD | 17,080.00 USD | 0.00 USD | 28,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3823.30` | 5,370,000.00 USD | 5,370,000.00 USD | 4,900.00 USD | 0.00 USD | 42,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3825.60` | 13,400,000.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3827.50` | 5,320,000.00 USD | 5,320,000.00 USD | 33,040.00 USD | 0.00 USD | 40,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.90` | 13,370,000.00 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3831.70` | 5,250,000.00 USD | 5,250,000.00 USD | 21,840.00 USD | 0.00 USD | 80,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3834.20` | 13,290,000.00 USD | 13,290,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3835.90` | 5,140,000.00 USD | 5,140,000.00 USD | 103,760.00 USD | 0.00 USD | 75,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.50` | 13,170,000.00 USD | 13,170,000.00 USD | 334,470.00 USD | 0.00 USD | 99,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3840.10` | 4,970,000.00 USD | 4,970,000.00 USD | 61,360.00 USD | 0.00 USD | 77,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.80` | 12,740,000.00 USD | 12,740,000.00 USD | 569,120.00 USD | 0.00 USD | 199,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3844.30` | 4,830,000.00 USD | 4,830,000.00 USD | 197,290.00 USD | 0.00 USD | 141,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.10` | 11,970,000.00 USD | 11,970,000.00 USD | 416,440.00 USD | 0.00 USD | 143,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3848.50` | 4,490,000.00 USD | 4,490,000.00 USD | 46,980.00 USD | 0.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.40` | 11,410,000.00 USD | 11,410,000.00 USD | 257,490.00 USD | 0.00 USD | 74,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.70` | 4,420,000.00 USD | 4,420,000.00 USD | 85,690.00 USD | 0.00 USD | 39,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.70` | 11,080,000.00 USD | 11,080,000.00 USD | 221,360.00 USD | 0.00 USD | 47,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.90` | 4,300,000.00 USD | 4,300,000.00 USD | 96,830.00 USD | 0.00 USD | 23,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.00` | 10,810,000.00 USD | 10,810,000.00 USD | 147,250.00 USD | 0.00 USD | 28,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3861.10` | 4,180,000.00 USD | 4,180,000.00 USD | 151,640.00 USD | 0.00 USD | 36,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.30` | 10,630,000.00 USD | 10,630,000.00 USD | 232,560.00 USD | 0.00 USD | 75,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.30` | 3,990,000.00 USD | 3,990,000.00 USD | 206,710.00 USD | 0.00 USD | 24,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.60` | 10,320,000.00 USD | 10,320,000.00 USD | 285,320.00 USD | 0.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.50` | 3,760,000.00 USD | 3,760,000.00 USD | 104,160.00 USD | 0.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.90` | 10,010,000.00 USD | 10,010,000.00 USD | 221,120.00 USD | 0.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.70` | 3,640,000.00 USD | 3,640,000.00 USD | 24,350.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.20` | 9,750,000.00 USD | 9,750,000.00 USD | 153,170.00 USD | 0.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.90` | 3,610,000.00 USD | 3,610,000.00 USD | 11,600.00 USD | 0.00 USD | 313.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3881.50` | 9,570,000.00 USD | 9,570,000.00 USD | 96,090.00 USD | 0.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3885.80` | 9,450,000.00 USD | 9,450,000.00 USD | 124,650.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.10` | 9,290,000.00 USD | 9,290,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3894.40` | 9,190,000.00 USD | 9,190,000.00 USD | 126,480.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3898.70` | 9,050,000.00 USD | 9,050,000.00 USD | 166,900.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3898.90` | 3,600,000.00 USD | 3,600,000.00 USD | 54,040.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.00` | 8,880,000.00 USD | 8,880,000.00 USD | 17,060.00 USD | 0.00 USD | 130,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3903.10` | 3,520,000.00 USD | 3,520,000.00 USD | 9,800.00 USD | 0.00 USD | 64,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3907.30` | 3,450,000.00 USD | 3,450,000.00 USD | 66,080.00 USD | 0.00 USD | 81,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.30` | 8,730,000.00 USD | 8,730,000.00 USD | 56,630.00 USD | 0.00 USD | 98,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3911.50` | 3,300,000.00 USD | 3,300,000.00 USD | 43,670.00 USD | 0.00 USD | 160,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3911.60` | 8,570,000.00 USD | 8,570,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3915.70` | 3,100,000.00 USD | 3,100,000.00 USD | 207,520.00 USD | 0.00 USD | 150,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3915.90` | 8,440,000.00 USD | 8,440,000.00 USD | 287,340.00 USD | 0.00 USD | 173,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3919.90` | 2,740,000.00 USD | 2,740,000.00 USD | 122,710.00 USD | 0.00 USD | 138,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.20` | 7,980,000.00 USD | 7,980,000.00 USD | 731,980.00 USD | 0.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3924.10` | 2,480,000.00 USD | 2,480,000.00 USD | 368,670.00 USD | 0.00 USD | 263,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3924.50` | 7,070,000.00 USD | 7,070,000.00 USD | 1,280,000.00 USD | 0.00 USD | 465,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3928.30` | 1,840,000.00 USD | 1,840,000.00 USD | 119,870.00 USD | 0.00 USD | 69,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3928.80` | 5,320,000.00 USD | 5,320,000.00 USD | 723,280.00 USD | 0.00 USD | 185,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3932.50` | 1,660,000.00 USD | 1,660,000.00 USD | 149,210.00 USD | 0.00 USD | 80,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.10` | 4,410,000.00 USD | 4,410,000.00 USD | 340,890.00 USD | 0.00 USD | 133,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3936.70` | 1,430,000.00 USD | 1,430,000.00 USD | 205,910.00 USD | 0.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3937.40` | 3,940,000.00 USD | 3,940,000.00 USD | 466,400.00 USD | 0.00 USD | 56,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.90` | 1,170,000.00 USD | 1,170,000.00 USD | 282,810.00 USD | 0.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3941.70` | 3,410,000.00 USD | 3,410,000.00 USD | 312,800.00 USD | 0.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3945.10` | 837,820.00 USD | 837,820.00 USD | 415,700.00 USD | 0.00 USD | 69,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.00` | 2,990,000.00 USD | 2,990,000.00 USD | 494,480.00 USD | 0.00 USD | 111,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3949.30` | 353,010.00 USD | 353,010.00 USD | 205,220.00 USD | 0.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.30` | 2,380,000.00 USD | 2,380,000.00 USD | 498,180.00 USD | 0.00 USD | 72,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3953.50` | 122,370.00 USD | 122,370.00 USD | 79,910.00 USD | 0.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3954.60` | 1,810,000.00 USD | 1,810,000.00 USD | 417,480.00 USD | 0.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.70` | 23,820.00 USD | 23,820.00 USD | 23,200.00 USD | 0.00 USD | 626.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.90` | 1,340,000.00 USD | 1,340,000.00 USD | 275,800.00 USD | 0.00 USD | 41,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.20` | 1,020,000.00 USD | 1,020,000.00 USD | 303,170.00 USD | 0.00 USD | 57,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.50` | 660,520.00 USD | 660,520.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.80` | 483,240.00 USD | 483,240.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.10` | 218,310.00 USD | 218,310.00 USD | 204,930.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3980.40` | 4,280.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3984.70` | 64,110.00 USD | 64,110.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3989.00` | 114,840.00 USD | 114,840.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4057.80` | 149,010.00 USD | 149,010.00 USD | 34,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4058.50` | 84,160.00 USD | 84,160.00 USD | 54,040.00 USD | 0.00 USD | 30,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4062.10` | 266,130.00 USD | 266,130.00 USD | 0.00 USD | 0.00 USD | 117,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4062.70` | 148,190.00 USD | 148,190.00 USD | 9,800.00 USD | 0.00 USD | 54,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4066.40` | 354,420.00 USD | 354,420.00 USD | 0.00 USD | 0.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4066.90` | 308,630.00 USD | 308,630.00 USD | 79,310.00 USD | 0.00 USD | 81,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4070.70` | 468,400.00 USD | 468,400.00 USD | 34,460.00 USD | 0.00 USD | 79,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4071.10` | 499,560.00 USD | 499,560.00 USD | 30,450.00 USD | 0.00 USD | 160,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.00` | 750,390.00 USD | 750,390.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4075.30` | 855,810.00 USD | 855,810.00 USD | 207,520.00 USD | 0.00 USD | 148,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.30` | 1,720,000.00 USD | 1,720,000.00 USD | 793,160.00 USD | 0.00 USD | 181,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4079.50` | 1,080,000.00 USD | 1,080,000.00 USD | 104,830.00 USD | 0.00 USD | 118,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4083.60` | 3,270,000.00 USD | 3,270,000.00 USD | 1,120,000.00 USD | 0.00 USD | 427,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4083.70` | 1,680,000.00 USD | 1,680,000.00 USD | 344,620.00 USD | 0.00 USD | 258,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4087.90` | 1,940,000.00 USD | 1,940,000.00 USD | 161,800.00 USD | 0.00 USD | 93,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4087.90` | 4,190,000.00 USD | 4,190,000.00 USD | 730,150.00 USD | 0.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4092.10` | 2,110,000.00 USD | 2,110,000.00 USD | 108,080.00 USD | 0.00 USD | 66,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.20` | 4,880,000.00 USD | 4,880,000.00 USD | 535,480.00 USD | 0.00 USD | 149,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4096.30` | 2,400,000.00 USD | 2,400,000.00 USD | 218,140.00 USD | 0.00 USD | 66,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4096.50` | 5,370,000.00 USD | 5,370,000.00 USD | 394,180.00 USD | 0.00 USD | 95,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4100.50` | 2,640,000.00 USD | 2,640,000.00 USD | 209,150.00 USD | 0.00 USD | 31,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4100.80` | 5,730,000.00 USD | 5,730,000.00 USD | 322,520.00 USD | 0.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.70` | 2,960,000.00 USD | 2,960,000.00 USD | 262,090.00 USD | 0.00 USD | 62,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.10` | 6,280,000.00 USD | 6,280,000.00 USD | 408,250.00 USD | 0.00 USD | 134,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.90` | 3,350,000.00 USD | 3,350,000.00 USD | 343,950.00 USD | 0.00 USD | 43,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4109.40` | 6,860,000.00 USD | 6,860,000.00 USD | 504,830.00 USD | 0.00 USD | 76,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4113.10` | 3,540,000.00 USD | 3,540,000.00 USD | 172,570.00 USD | 0.00 USD | 18,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4113.70` | 7,360,000.00 USD | 7,360,000.00 USD | 437,970.00 USD | 0.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.30` | 3,590,000.00 USD | 3,590,000.00 USD | 40,960.00 USD | 0.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.00` | 7,700,000.00 USD | 7,700,000.00 USD | 282,440.00 USD | 0.00 USD | 57,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4121.50` | 3,600,000.00 USD | 3,600,000.00 USD | 7,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.30` | 8,020,000.00 USD | 8,020,000.00 USD | 286,850.00 USD | 0.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4126.60` | 8,330,000.00 USD | 8,330,000.00 USD | 221,890.00 USD | 0.00 USD | 86,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4130.90` | 8,540,000.00 USD | 8,540,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.20` | 8,770,000.00 USD | 8,770,000.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4138.30` | 3,640,000.00 USD | 3,640,000.00 USD | 27,020.00 USD | 0.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4139.50` | 9,020,000.00 USD | 9,020,000.00 USD | 206,800.00 USD | 0.00 USD | 45,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4142.50` | 3,680,000.00 USD | 3,680,000.00 USD | 12,450.00 USD | 0.00 USD | 27,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.80` | 9,270,000.00 USD | 9,270,000.00 USD | 199,160.00 USD | 0.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4146.70` | 3,750,000.00 USD | 3,750,000.00 USD | 32,100.00 USD | 0.00 USD | 40,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.10` | 9,420,000.00 USD | 9,420,000.00 USD | 59,830.00 USD | 0.00 USD | 88,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4150.90` | 3,840,000.00 USD | 3,840,000.00 USD | 15,220.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4152.40` | 9,620,000.00 USD | 9,620,000.00 USD | 133,610.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4155.10` | 4,010,000.00 USD | 4,010,000.00 USD | 98,490.00 USD | 0.00 USD | 79,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.70` | 9,950,000.00 USD | 9,950,000.00 USD | 268,170.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4159.30` | 4,120,000.00 USD | 4,120,000.00 USD | 57,680.00 USD | 0.00 USD | 52,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.00` | 10,500,000.00 USD | 10,500,000.00 USD | 420,240.00 USD | 0.00 USD | 134,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4163.50` | 4,400,000.00 USD | 4,400,000.00 USD | 142,390.00 USD | 0.00 USD | 138,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.30` | 11,190,000.00 USD | 11,190,000.00 USD | 485,080.00 USD | 0.00 USD | 204,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4167.70` | 4,560,000.00 USD | 4,560,000.00 USD | 110,820.00 USD | 0.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.60` | 11,630,000.00 USD | 11,630,000.00 USD | 356,490.00 USD | 0.00 USD | 75,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4171.90` | 4,640,000.00 USD | 4,640,000.00 USD | 43,850.00 USD | 0.00 USD | 30,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.90` | 11,850,000.00 USD | 11,850,000.00 USD | 156,630.00 USD | 0.00 USD | 66,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.10` | 4,760,000.00 USD | 4,760,000.00 USD | 93,280.00 USD | 0.00 USD | 33,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.20` | 12,110,000.00 USD | 12,110,000.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.30` | 4,910,000.00 USD | 4,910,000.00 USD | 125,320.00 USD | 0.00 USD | 16,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,290,000.00 USD | 12,290,000.00 USD | 143,730.00 USD | 0.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.50` | 5,070,000.00 USD | 5,070,000.00 USD | 128,570.00 USD | 0.00 USD | 32,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.80` | 12,580,000.00 USD | 12,580,000.00 USD | 219,060.00 USD | 0.00 USD | 65,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.70` | 5,250,000.00 USD | 5,250,000.00 USD | 165,550.00 USD | 0.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.10` | 12,860,000.00 USD | 12,860,000.00 USD | 254,710.00 USD | 0.00 USD | 31,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.90` | 5,360,000.00 USD | 5,360,000.00 USD | 92,800.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.40` | 13,100,000.00 USD | 13,100,000.00 USD | 205,140.00 USD | 0.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.10` | 5,390,000.00 USD | 5,390,000.00 USD | 22,950.00 USD | 0.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.70` | 13,270,000.00 USD | 13,270,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.30` | 5,390,000.00 USD | 5,390,000.00 USD | 8,640.00 USD | 0.00 USD | 313.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.00` | 13,410,000.00 USD | 13,410,000.00 USD | 116,920.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.30` | 13,540,000.00 USD | 13,540,000.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.60` | 13,640,000.00 USD | 13,640,000.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.90` | 13,750,000.00 USD | 13,750,000.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.20` | 13,880,000.00 USD | 13,880,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.50` | 13,960,000.00 USD | 13,960,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.80` | 14,000,000.00 USD | 14,000,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.10` | 14,060,000.00 USD | 14,060,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4238.40` | 14,070,000.00 USD | 14,070,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4377.70` | 5,410,000.00 USD | 5,410,000.00 USD | 8,720.00 USD | 0.00 USD | 8,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.30` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4381.90` | 5,430,000.00 USD | 5,430,000.00 USD | 6,870.00 USD | 0.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4386.10` | 5,450,000.00 USD | 5,450,000.00 USD | 8,470.00 USD | 0.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4388.90` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4390.30` | 5,470,000.00 USD | 5,470,000.00 USD | 4,460.00 USD | 0.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4393.20` | 14,130,000.00 USD | 14,130,000.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4394.50` | 5,510,000.00 USD | 5,510,000.00 USD | 28,070.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.50` | 14,240,000.00 USD | 14,240,000.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4398.10` | 5,540,000.00 USD | 5,540,000.00 USD | 14,150.00 USD | 0.00 USD | 10,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.80` | 14,450,000.00 USD | 14,450,000.00 USD | 143,560.00 USD | 0.00 USD | 66,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.10` | 14,620,000.00 USD | 14,620,000.00 USD | 125,560.00 USD | 0.00 USD | 45,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4410.40` | 14,740,000.00 USD | 14,740,000.00 USD | 103,520.00 USD | 0.00 USD | 18,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.70` | 14,800,000.00 USD | 14,800,000.00 USD | 36,920.00 USD | 0.00 USD | 17,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.00` | 14,870,000.00 USD | 14,870,000.00 USD | 66,780.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.30` | 14,930,000.00 USD | 14,930,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4424.00` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | `Tier 1 CEX` |

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
| `1D` | `3579.70` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 8,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3583.90` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 1,960.00 USD | 0.00 USD | 16,110.00 USD |
| `7D` | `3584.80` | 14,790,000.00 USD | 0.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `3588.10` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 10,740.00 USD | 0.00 USD | 10,980.00 USD |
| `7D` | `3589.10` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3592.30` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 7,110.00 USD | 0.00 USD | 21,860.00 USD |
| `7D` | `3593.40` | 14,760,000.00 USD | 0.00 USD | 14,760,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3596.50` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 35,040.00 USD | 0.00 USD | 19,020.00 USD |
| `7D` | `3597.70` | 14,750,000.00 USD | 0.00 USD | 14,750,000.00 USD | 108,500.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3600.70` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 26,650.00 USD | 0.00 USD | 28,530.00 USD |
| `7D` | `3602.00` | 14,620,000.00 USD | 0.00 USD | 14,620,000.00 USD | 173,930.00 USD | 0.00 USD | 75,620.00 USD |
| `1D` | `3604.90` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 54,630.00 USD | 0.00 USD | 39,640.00 USD |
| `7D` | `3606.30` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 152,940.00 USD | 0.00 USD | 43,450.00 USD |
| `1D` | `3609.10` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 14,040.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `3610.60` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 72,480.00 USD | 0.00 USD | 20,480.00 USD |
| `1D` | `3613.30` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 33,240.00 USD | 0.00 USD | 12,240.00 USD |
| `7D` | `3614.90` | 14,080,000.00 USD | 0.00 USD | 14,080,000.00 USD | 76,990.00 USD | 0.00 USD | 16,470.00 USD |
| `1D` | `3617.50` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 41,740.00 USD | 0.00 USD | 5,470.00 USD |
| `7D` | `3619.20` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD |
| `1D` | `3621.70` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 37,530.00 USD | 0.00 USD | 10,010.00 USD |
| `7D` | `3623.50` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD |
| `1D` | `3625.90` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 51,070.00 USD | 0.00 USD | 7,660.00 USD |
| `7D` | `3627.80` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD |
| `1D` | `3630.10` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 19,470.00 USD | 0.00 USD | 2,670.00 USD |
| `7D` | `3632.10` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD |
| `1D` | `3634.30` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 2,050.00 USD | 0.00 USD | 594.12 USD |
| `7D` | `3636.40` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3640.70` | 13,670,000.00 USD | 0.00 USD | 13,670,000.00 USD | 55,830.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3645.00` | 13,600,000.00 USD | 0.00 USD | 13,600,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `3649.30` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `7D` | `3653.60` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3657.90` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3662.20` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3666.50` | 13,460,000.00 USD | 0.00 USD | 13,460,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3819.10` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 27,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3821.30` | 13,450,000.00 USD | 0.00 USD | 13,450,000.00 USD | 17,080.00 USD | 0.00 USD | 28,090.00 USD |
| `1D` | `3823.30` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 4,900.00 USD | 0.00 USD | 42,180.00 USD |
| `7D` | `3825.60` | 13,400,000.00 USD | 0.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3827.50` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 33,040.00 USD | 0.00 USD | 40,570.00 USD |
| `7D` | `3829.90` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD |
| `1D` | `3831.70` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 21,840.00 USD | 0.00 USD | 80,240.00 USD |
| `7D` | `3834.20` | 13,290,000.00 USD | 0.00 USD | 13,290,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD |
| `1D` | `3835.90` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 103,760.00 USD | 0.00 USD | 75,370.00 USD |
| `7D` | `3838.50` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 334,470.00 USD | 0.00 USD | 99,980.00 USD |
| `1D` | `3840.10` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 61,360.00 USD | 0.00 USD | 77,280.00 USD |
| `7D` | `3842.80` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 569,120.00 USD | 0.00 USD | 199,760.00 USD |
| `1D` | `3844.30` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 197,290.00 USD | 0.00 USD | 141,360.00 USD |
| `7D` | `3847.10` | 11,970,000.00 USD | 0.00 USD | 11,970,000.00 USD | 416,440.00 USD | 0.00 USD | 143,690.00 USD |
| `1D` | `3848.50` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 46,980.00 USD | 0.00 USD | 20,000.00 USD |
| `7D` | `3851.40` | 11,410,000.00 USD | 0.00 USD | 11,410,000.00 USD | 257,490.00 USD | 0.00 USD | 74,890.00 USD |
| `1D` | `3852.70` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 85,690.00 USD | 0.00 USD | 39,480.00 USD |
| `7D` | `3855.70` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 221,360.00 USD | 0.00 USD | 47,670.00 USD |
| `1D` | `3856.90` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 96,830.00 USD | 0.00 USD | 23,600.00 USD |
| `7D` | `3860.00` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 147,250.00 USD | 0.00 USD | 28,510.00 USD |
| `1D` | `3861.10` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 151,640.00 USD | 0.00 USD | 36,810.00 USD |
| `7D` | `3864.30` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 232,560.00 USD | 0.00 USD | 75,710.00 USD |
| `1D` | `3865.30` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 206,710.00 USD | 0.00 USD | 24,460.00 USD |
| `7D` | `3868.60` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 285,320.00 USD | 0.00 USD | 26,240.00 USD |
| `1D` | `3869.50` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 104,160.00 USD | 0.00 USD | 11,550.00 USD |
| `7D` | `3872.90` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 221,120.00 USD | 0.00 USD | 41,690.00 USD |
| `1D` | `3873.70` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 24,350.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3877.20` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 153,170.00 USD | 0.00 USD | 23,330.00 USD |
| `1D` | `3877.90` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 11,600.00 USD | 0.00 USD | 313.39 USD |
| `7D` | `3881.50` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 96,090.00 USD | 0.00 USD | 27,510.00 USD |
| `7D` | `3885.80` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 124,650.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3890.10` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD |
| `7D` | `3894.40` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 126,480.00 USD | 0.00 USD | 10,240.00 USD |
| `7D` | `3898.70` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 166,900.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3898.90` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 54,040.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3903.00` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 17,060.00 USD | 0.00 USD | 130,200.00 USD |
| `1D` | `3903.10` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 9,800.00 USD | 0.00 USD | 64,950.00 USD |
| `1D` | `3907.30` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 66,080.00 USD | 0.00 USD | 81,140.00 USD |
| `7D` | `3907.30` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 56,630.00 USD | 0.00 USD | 98,910.00 USD |
| `1D` | `3911.50` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 43,670.00 USD | 0.00 USD | 160,480.00 USD |
| `7D` | `3911.60` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD |
| `1D` | `3915.70` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 207,520.00 USD | 0.00 USD | 150,730.00 USD |
| `7D` | `3915.90` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 287,340.00 USD | 0.00 USD | 173,650.00 USD |
| `1D` | `3919.90` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 122,710.00 USD | 0.00 USD | 138,860.00 USD |
| `7D` | `3920.20` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 731,980.00 USD | 0.00 USD | 181,350.00 USD |
| `1D` | `3924.10` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 368,670.00 USD | 0.00 USD | 263,330.00 USD |
| `7D` | `3924.50` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 1,280,000.00 USD | 0.00 USD | 465,510.00 USD |
| `1D` | `3928.30` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 119,870.00 USD | 0.00 USD | 69,340.00 USD |
| `7D` | `3928.80` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 723,280.00 USD | 0.00 USD | 185,470.00 USD |
| `1D` | `3932.50` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 149,210.00 USD | 0.00 USD | 80,220.00 USD |
| `7D` | `3933.10` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 340,890.00 USD | 0.00 USD | 133,810.00 USD |
| `1D` | `3936.70` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 205,910.00 USD | 0.00 USD | 51,660.00 USD |
| `7D` | `3937.40` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 466,400.00 USD | 0.00 USD | 56,370.00 USD |
| `1D` | `3940.90` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 282,810.00 USD | 0.00 USD | 48,030.00 USD |
| `7D` | `3941.70` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 312,800.00 USD | 0.00 USD | 114,460.00 USD |
| `1D` | `3945.10` | 837,820.00 USD | 0.00 USD | 837,820.00 USD | 415,700.00 USD | 0.00 USD | 69,110.00 USD |
| `7D` | `3946.00` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 494,480.00 USD | 0.00 USD | 111,080.00 USD |
| `1D` | `3949.30` | 353,010.00 USD | 0.00 USD | 353,010.00 USD | 205,220.00 USD | 0.00 USD | 25,420.00 USD |
| `7D` | `3950.30` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 498,180.00 USD | 0.00 USD | 72,590.00 USD |
| `1D` | `3953.50` | 122,370.00 USD | 0.00 USD | 122,370.00 USD | 79,910.00 USD | 0.00 USD | 18,640.00 USD |
| `7D` | `3954.60` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 417,480.00 USD | 0.00 USD | 53,640.00 USD |
| `1D` | `3957.70` | 23,820.00 USD | 0.00 USD | 23,820.00 USD | 23,200.00 USD | 0.00 USD | 626.79 USD |
| `7D` | `3958.90` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 275,800.00 USD | 0.00 USD | 41,700.00 USD |
| `7D` | `3963.20` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 303,170.00 USD | 0.00 USD | 57,060.00 USD |
| `7D` | `3967.50` | 660,520.00 USD | 0.00 USD | 660,520.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `7D` | `3971.80` | 483,240.00 USD | 0.00 USD | 483,240.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `3976.10` | 218,310.00 USD | 0.00 USD | 218,310.00 USD | 204,930.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `3980.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3980.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3980.40` | 4,280.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `3984.70` | 64,110.00 USD | 64,110.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3989.00` | 114,840.00 USD | 114,840.00 USD | 0.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4057.80` | 149,010.00 USD | 149,010.00 USD | 0.00 USD | 34,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4058.50` | 84,160.00 USD | 84,160.00 USD | 0.00 USD | 54,040.00 USD | 0.00 USD | 30,120.00 USD |
| `7D` | `4062.10` | 266,130.00 USD | 266,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 117,120.00 USD |
| `1D` | `4062.70` | 148,190.00 USD | 148,190.00 USD | 0.00 USD | 9,800.00 USD | 0.00 USD | 54,230.00 USD |
| `7D` | `4066.40` | 354,420.00 USD | 354,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 88,290.00 USD |
| `1D` | `4066.90` | 308,630.00 USD | 308,630.00 USD | 0.00 USD | 79,310.00 USD | 0.00 USD | 81,140.00 USD |
| `7D` | `4070.70` | 468,400.00 USD | 468,400.00 USD | 0.00 USD | 34,460.00 USD | 0.00 USD | 79,530.00 USD |
| `1D` | `4071.10` | 499,560.00 USD | 499,560.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 160,480.00 USD |
| `7D` | `4075.00` | 750,390.00 USD | 750,390.00 USD | 0.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD |
| `1D` | `4075.30` | 855,810.00 USD | 855,810.00 USD | 0.00 USD | 207,520.00 USD | 0.00 USD | 148,730.00 USD |
| `7D` | `4079.30` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 793,160.00 USD | 0.00 USD | 181,320.00 USD |
| `1D` | `4079.50` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 104,830.00 USD | 0.00 USD | 118,800.00 USD |
| `7D` | `4083.60` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 427,200.00 USD |
| `1D` | `4083.70` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 344,620.00 USD | 0.00 USD | 258,530.00 USD |
| `1D` | `4087.90` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 161,800.00 USD | 0.00 USD | 93,580.00 USD |
| `7D` | `4087.90` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 730,150.00 USD | 0.00 USD | 195,500.00 USD |
| `1D` | `4092.10` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 108,080.00 USD | 0.00 USD | 66,790.00 USD |
| `7D` | `4092.20` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 535,480.00 USD | 0.00 USD | 149,790.00 USD |
| `1D` | `4096.30` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 218,140.00 USD | 0.00 USD | 66,770.00 USD |
| `7D` | `4096.50` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 394,180.00 USD | 0.00 USD | 95,350.00 USD |
| `1D` | `4100.50` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 209,150.00 USD | 0.00 USD | 31,520.00 USD |
| `7D` | `4100.80` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 322,520.00 USD | 0.00 USD | 42,790.00 USD |
| `1D` | `4104.70` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 262,090.00 USD | 0.00 USD | 62,730.00 USD |
| `7D` | `4105.10` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 408,250.00 USD | 0.00 USD | 134,430.00 USD |
| `1D` | `4108.90` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 343,950.00 USD | 0.00 USD | 43,620.00 USD |
| `7D` | `4109.40` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 504,830.00 USD | 0.00 USD | 76,750.00 USD |
| `1D` | `4113.10` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 172,570.00 USD | 0.00 USD | 18,130.00 USD |
| `7D` | `4113.70` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 437,970.00 USD | 0.00 USD | 63,950.00 USD |
| `1D` | `4117.30` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 40,960.00 USD | 0.00 USD | 6,800.00 USD |
| `7D` | `4118.00` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 282,440.00 USD | 0.00 USD | 57,050.00 USD |
| `1D` | `4121.50` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 7,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4122.30` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 286,850.00 USD | 0.00 USD | 30,750.00 USD |
| `7D` | `4126.60` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 221,890.00 USD | 0.00 USD | 86,130.00 USD |
| `7D` | `4130.90` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD |
| `7D` | `4135.20` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `4138.30` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 27,020.00 USD | 0.00 USD | 15,060.00 USD |
| `7D` | `4139.50` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 206,800.00 USD | 0.00 USD | 45,750.00 USD |
| `1D` | `4142.50` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 12,450.00 USD | 0.00 USD | 27,110.00 USD |
| `7D` | `4143.80` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 199,160.00 USD | 0.00 USD | 50,830.00 USD |
| `1D` | `4146.70` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 32,100.00 USD | 0.00 USD | 40,570.00 USD |
| `7D` | `4148.10` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 88,440.00 USD |
| `1D` | `4150.90` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 15,220.00 USD | 0.00 USD | 69,900.00 USD |
| `7D` | `4152.40` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 133,610.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `4155.10` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 98,490.00 USD | 0.00 USD | 79,530.00 USD |
| `7D` | `4156.70` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 268,170.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4159.30` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 57,680.00 USD | 0.00 USD | 52,470.00 USD |
| `7D` | `4161.00` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 420,240.00 USD | 0.00 USD | 134,730.00 USD |
| `1D` | `4163.50` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 142,390.00 USD | 0.00 USD | 138,090.00 USD |
| `7D` | `4165.30` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 485,080.00 USD | 0.00 USD | 204,730.00 USD |
| `1D` | `4167.70` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 110,820.00 USD | 0.00 USD | 48,030.00 USD |
| `7D` | `4169.60` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 356,490.00 USD | 0.00 USD | 75,190.00 USD |
| `1D` | `4171.90` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 43,850.00 USD | 0.00 USD | 30,380.00 USD |
| `7D` | `4173.90` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 156,630.00 USD | 0.00 USD | 66,900.00 USD |
| `1D` | `4176.10` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 93,280.00 USD | 0.00 USD | 33,360.00 USD |
| `7D` | `4178.20` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD |
| `1D` | `4180.30` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 125,320.00 USD | 0.00 USD | 16,560.00 USD |
| `7D` | `4182.50` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 143,730.00 USD | 0.00 USD | 40,030.00 USD |
| `1D` | `4184.50` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 128,570.00 USD | 0.00 USD | 32,780.00 USD |
| `7D` | `4186.80` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 219,060.00 USD | 0.00 USD | 65,350.00 USD |
| `1D` | `4188.70` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 165,550.00 USD | 0.00 USD | 22,020.00 USD |
| `7D` | `4191.10` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 254,710.00 USD | 0.00 USD | 31,760.00 USD |
| `1D` | `4192.90` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 92,800.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `4195.40` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 205,140.00 USD | 0.00 USD | 33,460.00 USD |
| `1D` | `4197.10` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 22,950.00 USD | 0.00 USD | 7,420.00 USD |
| `7D` | `4199.70` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `4201.30` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 8,640.00 USD | 0.00 USD | 313.39 USD |
| `7D` | `4204.00` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 116,920.00 USD | 0.00 USD | 23,560.00 USD |
| `7D` | `4208.30` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD |
| `7D` | `4212.60` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4216.90` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD |
| `7D` | `4221.20` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `4225.50` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `4229.80` | 14,000,000.00 USD | 14,000,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `7D` | `4234.10` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4238.40` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4377.70` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 8,720.00 USD | 0.00 USD | 8,360.00 USD |
| `7D` | `4380.30` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4381.90` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 6,870.00 USD | 0.00 USD | 7,750.00 USD |
| `1D` | `4386.10` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 8,470.00 USD | 0.00 USD | 10,980.00 USD |
| `7D` | `4388.90` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4390.30` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 4,460.00 USD | 0.00 USD | 17,730.00 USD |
| `7D` | `4393.20` | 14,130,000.00 USD | 14,130,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `4394.50` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 28,070.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `4397.50` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `4398.10` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 14,150.00 USD | 0.00 USD | 10,020.00 USD |
| `7D` | `4401.80` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 143,560.00 USD | 0.00 USD | 66,400.00 USD |
| `7D` | `4406.10` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 125,560.00 USD | 0.00 USD | 45,370.00 USD |
| `7D` | `4410.40` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 103,520.00 USD | 0.00 USD | 18,970.00 USD |
| `7D` | `4414.70` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 17,590.00 USD |
| `7D` | `4419.00` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | 7,680.00 USD |
| `7D` | `4423.30` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD |
| `7D` | `4424.00` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.24M` | Total OI Tokens: `68,923.4 PAXG`
  * 1h OI Change: `-0.07%` | 4h OI Change: `-0.94%` | 24h OI Change: `-0.43%`
  * Exchange Breakdown: Binance=`104.32M` | Bybit=`24.85M` | OKX=`-` | Hyperliquid=`24.62M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.06K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0005%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `-0.0003%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0020%` | **USDT Bitget** | `0.0006%` |
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
| `4H` | `PAXG` | `50.36%` | `49.64%` | `1.01` | 41,900,000.00 USD |
| `4H` | `Binance` | `50.93%` | `49.07%` | `1.04` | 15,290,000.00 USD |
| `4H` | `OKX` | `48.57%` | `51.43%` | `0.94` | 5,830,000.00 USD |
| `4H` | `Bybit` | `50.84%` | `49.16%` | `1.03` | 4,250,000.00 USD |
| `4H` | `KuCoin` | `49.18%` | `50.82%` | `0.97` | 761,100.00 USD |
| `4H` | `Gate` | `43.15%` | `56.85%` | `0.76` | 1,360,000.00 USD |
| `4H` | `Bitget` | `50.15%` | `49.85%` | `1.01` | 2,950,000.00 USD |
| `4H` | `BingX` | `28.13%` | `71.87%` | `0.39` | 3,280,000.00 USD |
| `4H` | `MEXC` | `52.32%` | `47.68%` | `1.10` | 3,110,000.00 USD |
| `4H` | `Bitunix` | `51.09%` | `48.91%` | `1.04` | 651,300.00 USD |
| `4H` | `Hyperliquid` | `61%` | `39%` | `1.56` | 628,040.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.82%` | `50.18%` | `0.99` | 1,430,000.00 USD |
| `4H` | `Crypto.com` | `42.86%` | `57.14%` | `0.75` | 23,030.00 USD |
| `4H` | `WhiteBIT` | `87.64%` | `12.36%` | `7.09` | 2,000,000.00 USD |
| `4H` | `HTX` | `66.87%` | `33.13%` | `2.02` | 13,640.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `41.93%` | `58.07%` | `0.72` | 107,030.00 USD |
| `4H` | `Aster` | `25.56%` | `74.44%` | `0.34` | 27,720.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.23%` | `58.77%` | `0.70` | 181,540.00 USD |
| `4H` | `Whale Positions` | `50.93%` | `49.07%` | `1.04` | 15,290,000.00 USD |
| `4H` | `Global Accounts` | `50.36%` | `49.64%` | `1.01` | 41,900,000.00 USD |


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
