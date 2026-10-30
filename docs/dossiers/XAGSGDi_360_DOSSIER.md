# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 10:13:37 IST` (`2026-10-30 04:43:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `65.73` | **Live Ask Quote**: `65.76` | **Mid Price**: `65.74`
- **Spread Points**: `27.00` | **Spread BPS**: `4.11 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `5,000.0` | Digits: `3` | Point: `0.001`
  * Point Value (1.0 Lot): `5.00 USD` | Point Value (0.01 Lot): `0.0500 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `51.46` | VWAP Z-Score: `-0.24` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2419` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.82` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.08` | Lower -3.00σ Band: `50.85`
  * Upper +2.51σ Band: `51.98` | Lower -2.51σ Band: `50.95`
  * Upper +2.01σ Band: `51.88` | Lower -2.01σ Band: `51.05`
  * Upper +2.00σ Band: `51.87` | Lower -2.00σ Band: `51.05`
  * Upper +1.28σ Band: `51.73` | Lower -1.28σ Band: `51.20`
  * Upper +1.00σ Band: `51.67` | Lower -1.00σ Band: `51.26`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`51.38` | EMA-20=`51.53` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.88` (Slope: `+0.0000`) | EMA-100=`52.30`
  * Institutional Anchors: EMA-144=`52.57` | EMA-200=`52.81` (Slope: `-0.3426`) | EMA-233=`52.97`
- **Range Boundaries**: 24H High=`53.50` | 24H Low=`51.08` | Weekly High=`54.61` | Weekly Low=`51.08`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `51.63` (Distance: `-0.36%`)
  * Point of Control (POC) = `51.40` (Distance: `+0.08%`)
  * Value Area Low (VAL) = `51.12` (Distance: `+0.64%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.53` | Weekly POC=`53.89` | Weekly VAL=`52.81`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`66.01` | Low=`65.48`
  * New York Session (13:00-21:00 UTC): High=`66.14` | Low=`65.35`
  * Initial Balance (First Hour): IB High=`65.94` | IB Low=`65.55`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `65.48` - `66.01`
  * Optimal Trade Entry (OTE 0.705): `65.87`
  * Structural Invalidation Anchor (0.786): `66.27`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `51.48` | `51.51` | `51.38` | `51.49` | `2,772` | 142,721.96 USD | 45,758.19 USD | `+32.06%` | -864,549.47 USD | `+0.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `51.49` | `51.58` | `51.44` | `51.47` | `2,329` | 119,875.96 USD | -43,631.32 USD | `-36.40%` | -908,180.80 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `51.47` | `51.48` | `51.27` | `51.38` | `2,667` | 137,038.46 USD | -20,654.12 USD | `-15.07%` | -928,834.92 USD | `-0.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.78` | `51.80` | `51.09` | `51.26` | `11,936` | 611,803.55 USD | -389,526.48 USD | `-63.67%` | -2,249,910.06 USD | `-3.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.26` | `51.58` | `51.15` | `51.47` | `8,843` | 455,158.05 USD | 224,945.01 USD | `+49.42%` | -2,024,965.05 USD | `+2.02` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `51.47` | `51.50` | `51.19` | `51.26` | `9,598` | 491,945.49 USD | -321,286.88 USD | `-65.31%` | -2,346,251.92 USD | `-2.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `51.96` | `52.01` | `51.81` | `51.92` | `6,169` | 320,319.16 USD | -7,812.66 USD | `-2.44%` | -1,854,423.11 USD | `+0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `51.92` | `52.06` | `51.73` | `51.78` | `13,804` | 714,757.32 USD | -415,480.10 USD | `-58.13%` | -2,269,903.21 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `51.78` | `51.80` | `51.09` | `51.55` | `37,249` | 1,920,036.95 USD | -43,513.59 USD | `-2.27%` | -2,313,416.79 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -3,777,102.90 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -4,778,205.92 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.43` | `74,077` | 3,809,631.96 USD | -980,148.03 USD | `-25.73%` | -5,758,353.95 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -3,330,572.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -2,783,791.99 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -3,777,102.90 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -4,778,205.92 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.43` | `74,077` | 3,809,631.96 USD | -980,148.03 USD | `-25.73%` | -5,758,353.95 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `51.45` | `86.3600` | 4,443.65 USD | 821,616.08 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.45` | `58.4300` | 3,006.46 USD | 824,622.53 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.45` | `1087.5900` | 55,959.77 USD | 880,582.30 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `51.45` | `87.7900` | 4,516.97 USD | 885,099.27 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.46` | `121.3900` | 6,247.21 USD | 109,577.93 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `51.46` | `3385.7900` | 174,242.91 USD | 283,820.84 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `51.46` | `237.0100` | 12,197.01 USD | 296,017.85 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `51.46` | `3969.0700` | 204,252.31 USD | 500,270.16 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `51.46` | `73.6600` | 3,790.54 USD | 504,060.71 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `51.46` | `79.2800` | 4,079.67 USD | 508,140.37 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.46` | `87.7400` | 4,514.92 USD | 512,655.30 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.46` | `5918.0100` | 304,517.12 USD | 817,172.42 USD | `2 orders` | `-0.03%` | `-` |
| `ASK` | `51.47` | `82.5300` | 4,248.15 USD | 4,248.15 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `51.47` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 51.47` | `0.00%` | `-` |
| `BID` | `51.47` | `47.2000` | 2,429.53 USD | 2,429.53 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `51.47` | `57.8700` | 2,978.68 USD | 5,408.21 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `51.47` | `1608.4200` | 82,786.99 USD | 88,195.20 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `51.47` | `96.6300` | 4,973.55 USD | 93,168.74 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `51.47` | `159.0400` | 8,185.63 USD | 101,354.37 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `51.47` | `24.9100` | 1,282.07 USD | 102,636.44 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `51.47` | `13.2900` | 683.98 USD | 103,320.42 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `51.47` | `0.2000` | 10.29 USD | 103,330.72 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `51.48` | `1589.9500` | 81,856.99 USD | 114,429.74 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `51.48` | `95.0600` | 4,893.97 USD | 32,572.76 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `51.48` | `4.0100` | 206.44 USD | 27,678.78 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.48` | `1.3100` | 67.44 USD | 27,472.34 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.48` | `8.7900` | 452.51 USD | 27,404.90 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.48` | `205.3000` | 10,568.64 USD | 26,952.39 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `51.48` | `92.4800` | 4,760.69 USD | 16,383.75 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.48` | `14.2200` | 732.00 USD | 11,623.07 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.48` | `65.8000` | 3,387.12 USD | 10,891.06 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `51.48` | `63.2500` | 3,255.79 USD | 7,503.94 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `51.49` | `650.7700` | 33,511.40 USD | 367,141.14 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `51.49` | `69.8100` | 3,594.80 USD | 333,629.74 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `51.49` | `79.2800` | 4,082.37 USD | 330,034.94 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.49` | `56.7900` | 2,924.23 USD | 325,952.58 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.49` | `2837.3000` | 146,092.58 USD | 323,028.34 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `51.49` | `174.8100` | 9,000.79 USD | 176,935.77 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `51.49` | `972.9400` | 50,094.73 USD | 167,934.98 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `51.49` | `65.7700` | 3,386.30 USD | 117,840.24 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `51.49` | `0.4700` | 24.20 USD | 114,453.94 USD | `1 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,823,497.21 USD | `346,127.65` | `58.90` | `51.49` | `529.98` | 2,562,862.88 USD | `+14.38%` | `5X Cross` |
| `123` | `0x4692...164f` | `SHORT` | 15,987,672.64 USD | `310,524.66` | `52.92` | `51.49` | `253.10` | 445,388.26 USD | `+2.79%` | `5X Cross` |
| `205` | `0xacb6...efbd` | `SHORT` | 10,356,355.16 USD | `201,133.33` | `59.63` | `51.49` | `76.83` | 1,636,301.95 USD | `+15.80%` | `6X Cross` |
| `240` | `0xc26c...b8f4` | `LONG` | 9,344,276.83 USD | `181,463.41` | `55.43` | `51.49` | `0.000000` | -714,478.24 USD | `-7.65%` | `2X Cross` |
| `286` | `0x49e9...e1d0` | `SHORT` | 8,230,694.39 USD | `159,887.61` | `55.44` | `51.49` | `102.41` | 633,061.32 USD | `+7.69%` | `4X Cross` |
| `353` | `0x645b...87b8` | `LONG` | 6,587,825.99 USD | `127,956.22` | `56.57` | `51.49` | `0.000000` | -650,616.58 USD | `-9.88%` | `3X Cross` |
| `357` | `0xd8c5...99b0` | `SHORT` | 6,503,587.26 USD | `126,320.04` | `61.98` | `51.49` | `199.18` | 1,325,750.59 USD | `+20.38%` | `3X Cross` |
| `389` | `0xe9ff...5903` | `SHORT` | 5,817,264.19 USD | `112,996.08` | `60.07` | `51.49` | `178.29` | 970,686.61 USD | `+16.69%` | `5X Cross` |
| `613` | `0x9aa5...58af` | `LONG` | 3,667,469.29 USD | `71,243.43` | `61.59` | `51.49` | `0.000000` | -720,688.23 USD | `-19.65%` | `20X Cross` |
| `742` | `0x2056...8396` | `LONG` | 3,089,400.00 USD | `60,000.00` | `66.92` | `51.49` | `21.35` | -925,927.14 USD | `-29.97%` | `10X Cross` |
| `751` | `0x354b...6425` | `SHORT` | 3,047,642.75 USD | `59,195.92` | `51.38` | `51.49` | `231.17` | -6,322.04 USD | `-0.21%` | `10X Cross` |
| `881` | `0x0242...ffa1` | `SHORT` | 2,569,959.75 USD | `49,916.67` | `56.48` | `51.49` | `315.91` | 249,172.11 USD | `+9.70%` | `10X Cross` |
| `887` | `0x960b...f0fc` | `LONG` | 2,546,788.19 USD | `49,457.96` | `55.82` | `51.49` | `0.000000` | -214,148.84 USD | `-8.41%` | `25X Cross` |
| `974` | `0x8b9d...7b28` | `LONG` | 2,307,153.65 USD | `44,823.47` | `58.35` | `51.49` | `0.000000` | -308,294.90 USD | `-13.36%` | `10X Cross` |
| `1049` | `0x5647...e7de` | `LONG` | 2,073,134.25 USD | `40,262.07` | `57.38` | `51.49` | `0.000000` | -237,103.35 USD | `-11.44%` | `20X Cross` |
| `1059` | `0xa2ce...3126` | `LONG` | 2,058,880.00 USD | `40,000.00` | `74.30` | `51.49` | `0.000000` | -913,175.49 USD | `-44.35%` | `20X Cross` |
| `1092` | `0xb078...de15` | `SHORT` | 2,008,266.51 USD | `39,000.01` | `52.58` | `51.49` | `202.95` | 42,252.44 USD | `+2.10%` | `8X Cross` |
| `1344` | `0xce97...7e78` | `LONG` | 1,618,231.32 USD | `31,428.07` | `51.51` | `51.49` | `0.000000` | -758.99 USD | `-0.05%` | `5X Cross` |
| `1422` | `0x3678...b209` | `LONG` | 1,544,550.00 USD | `30,000.00` | `57.15` | `51.49` | `0.000000` | -169,950.00 USD | `-11.00%` | `20X Cross` |
| `1423` | `0x5a88...d997` | `LONG` | 1,544,520.00 USD | `30,000.00` | `59.50` | `51.49` | `38.60` | -240,367.59 USD | `-15.56%` | `25X Cross` |
| `1651` | `0x7ea9...fc7f` | `LONG` | 1,286,800.00 USD | `25,000.00` | `53.60` | `51.49` | `34.93` | -53,204.05 USD | `-4.13%` | `25X Cross` |
| `1750` | `0x24fb...ed0f` | `LONG` | 1,189,517.92 USD | `23,110.00` | `51.37` | `51.49` | `0.000000` | 2,340.59 USD | `+0.20%` | `20X Cross` |
| `1789` | `0xf517...c032` | `LONG` | 1,165,089.98 USD | `22,627.50` | `66.29` | `51.49` | `0.000000` | -334,905.13 USD | `-28.75%` | `20X Cross` |
| `1920` | `0xcc9f...d218` | `LONG` | 1,056,605.69 USD | `20,520.60` | `52.63` | `51.49` | `26.86` | -23,302.36 USD | `-2.21%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.36` (Vol: 4,300,000.00 USD, Dist: `+3.87%`) | Long MP=`51.16` (Vol: 1,900,000.00 USD, Dist: `--0.42%`)
  * 48H Horizon: Short MP=`54.84` (Vol: 4,200,000.00 USD, Dist: `+6.76%`) | Long MP=`51.17` (Vol: 2,500,000.00 USD, Dist: `--0.39%`)
  * 3D Horizon: Short MP=`55.09` (Vol: 5,200,000.00 USD, Dist: `+7.24%`) | Long MP=`51.17` (Vol: 2,900,000.00 USD, Dist: `--0.39%`)
  * 7D Horizon: Short MP=`55.09` (Vol: 8,900,000.00 USD, Dist: `+7.24%`) | Long MP=`51.17` (Vol: 2,900,000.00 USD, Dist: `--0.39%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

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
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.99K` | Last 24h: `209.74K` | Last 3d: `432.77K` | Last 7d: `624.53K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


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
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BEARISH (BELOW PIVOT)`** | SILVER (XAGUSD.pi) Metal Auction: ROTATI | `53.72` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 09:50:55 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:55 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:10:55 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.12` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.79` (Risk Distance: `0.3307` pts)
  * +2.5R Take Profit: `51.95`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `51.63` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `51.96` (Risk Distance: `0.3307` pts)
  * +2.5R Take Profit: `50.80`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`66.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
