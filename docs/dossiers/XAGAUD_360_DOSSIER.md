# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGAUD
**Canonical Key**: `XAGAUD` | **Broker Instrument**: `XAGAUD.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-30 10:22:41 IST` (`2026-10-30 04:52:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `51.27` | **Live Ask Quote**: `51.30` | **Mid Price**: `51.28`
- **Spread Points**: `36.00` | **Spread BPS**: `7.02 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `51.28` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `51.64` | Lower -3.00σ Band: `50.93`
  * Upper +2.51σ Band: `51.57` | Lower -2.51σ Band: `51.00`
  * Upper +2.01σ Band: `51.50` | Lower -2.01σ Band: `51.07`
  * Upper +2.00σ Band: `51.49` | Lower -2.00σ Band: `51.08`
  * Upper +1.28σ Band: `51.43` | Lower -1.28σ Band: `51.14`
  * Upper +1.00σ Band: `51.39` | Lower -1.00σ Band: `51.18`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`51.28` | EMA-20=`51.28` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.28` (Slope: `+0.0000`) | EMA-100=`51.28`
  * Institutional Anchors: EMA-144=`51.28` | EMA-200=`51.28` (Slope: `+0.0000`) | EMA-233=`51.28`
- **Range Boundaries**: 24H High=`51.80` | 24H Low=`50.77` | Weekly High=`52.31` | Weekly Low=`50.26`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `51.63` (Distance: `-0.67%`)
  * Point of Control (POC) = `51.39` (Distance: `-0.22%`)
  * Value Area Low (VAL) = `51.13` (Distance: `+0.29%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.53` | Weekly POC=`53.89` | Weekly VAL=`52.81`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.49` | Low=`51.08`
  * New York Session (13:00-21:00 UTC): High=`51.59` | Low=`50.98`
  * Initial Balance (First Hour): IB High=`51.44` | IB Low=`51.13`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `51.08` - `51.49`
  * Optimal Trade Entry (OTE 0.705): `51.39`
  * Structural Invalidation Anchor (0.786): `51.69`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `51.47` | `51.48` | `51.27` | `51.38` | `2,667` | 137,038.46 USD | -20,654.12 USD | `-15.07%` | -867,340.67 USD | `-0.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `51.38` | `51.50` | `51.31` | `51.37` | `2,990` | 153,608.26 USD | -28,952.34 USD | `-18.85%` | -896,293.01 USD | `-0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `51.37` | `51.49` | `51.19` | `51.26` | `3,941` | 201,995.96 USD | -99,974.35 USD | `-49.49%` | -996,267.36 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.78` | `51.80` | `51.09` | `51.26` | `11,936` | 611,803.55 USD | -389,526.48 USD | `-63.67%` | -2,249,910.06 USD | `-3.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.26` | `51.58` | `51.15` | `51.47` | `8,843` | 455,158.05 USD | 224,945.01 USD | `+49.42%` | -2,024,965.05 USD | `+2.02` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `51.47` | `51.50` | `51.19` | `51.26` | `9,598` | 491,945.49 USD | -321,286.88 USD | `-65.31%` | -2,346,251.92 USD | `-2.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `51.96` | `52.01` | `51.81` | `51.92` | `6,169` | 320,319.16 USD | -7,812.66 USD | `-2.44%` | -1,854,423.11 USD | `+0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `51.92` | `52.06` | `51.73` | `51.78` | `13,804` | 714,757.32 USD | -415,480.10 USD | `-58.13%` | -2,269,903.21 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `51.78` | `51.80` | `51.09` | `51.55` | `37,249` | 1,920,036.95 USD | -43,513.59 USD | `-2.27%` | -2,313,416.79 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -3,777,102.90 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -4,778,205.92 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.27` | `75,650` | 3,878,272.90 USD | -2,304,909.76 USD | `-59.43%` | -7,083,115.68 USD | `-1.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -3,330,572.26 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -2,783,791.99 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -3,777,102.90 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -4,778,205.92 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.27` | `75,650` | 3,878,272.90 USD | -2,304,909.76 USD | `-59.43%` | -7,083,115.68 USD | `-1.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `51.29` | `409.3300` | 20,995.76 USD | 657,796.44 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `51.30` | `202.8000` | 10,404.65 USD | 144,583.74 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `51.30` | `409.3100` | 20,999.24 USD | 165,582.98 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.30` | `114.5800` | 5,878.30 USD | 171,461.28 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `51.30` | `84.5200` | 4,336.05 USD | 175,797.32 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.30` | `129.5300` | 6,645.02 USD | 182,442.34 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `51.30` | `3898.5200` | 199,994.08 USD | 382,436.42 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.30` | `91.3000` | 4,683.60 USD | 387,120.02 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `51.30` | `3878.1300` | 198,936.43 USD | 586,056.45 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `51.30` | `131.0600` | 6,722.85 USD | 592,779.30 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.30` | `858.2000` | 44,021.37 USD | 636,800.67 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `51.31` | `169.9000` | 8,718.08 USD | 24,970.31 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `51.31` | `22.0900` | 1,133.48 USD | 26,103.79 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `51.31` | `0.2000` | 10.26 USD | 26,114.05 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `51.31` | `256.8400` | 13,178.20 USD | 39,292.25 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `51.31` | `220.9200` | 11,334.96 USD | 50,627.22 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `51.31` | `1585.6500` | 81,354.94 USD | 131,982.16 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `51.31` | `42.8200` | 2,196.92 USD | 134,179.08 USD | `2 orders` | `-0.02%` | `-` |
| `ASK` | `51.32` | `186.9000` | 9,592.46 USD | 101,501.32 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.32` | `56.5800` | 2,903.86 USD | 91,908.86 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.32` | `67.7500` | 3,477.07 USD | 89,005.01 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.32` | `103.9800` | 5,336.36 USD | 85,527.94 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `51.32` | `0.2000` | 10.26 USD | 80,191.58 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `51.32` | `1562.4100` | 80,181.32 USD | 80,181.32 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `51.32` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 51.32` | `0.00%` | `-` |
| `BID` | `51.32` | `133.6400` | 6,858.14 USD | 6,858.14 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `51.32` | `183.0600` | 9,394.09 USD | 16,252.23 USD | `3 orders` | `-0.00%` | `-` |
| `ASK` | `51.33` | `11350.7600` | 582,679.91 USD | 948,923.87 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `51.33` | `1153.9500` | 59,235.72 USD | 366,243.96 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `51.33` | `161.7400` | 8,302.28 USD | 307,008.24 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `51.33` | `109.0200` | 5,596.00 USD | 298,705.97 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `51.33` | `113.7600` | 5,839.19 USD | 293,109.97 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `51.33` | `311.0400` | 15,965.06 USD | 287,270.78 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `51.33` | `34.9300` | 1,792.85 USD | 271,305.72 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.33` | `3273.4200` | 168,011.55 USD | 269,512.87 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `51.34` | `463.6400` | 23,803.28 USD | 1,087,388.80 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `51.34` | `728.7700` | 37,414.32 USD | 1,063,585.52 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `51.34` | `220.1000` | 11,299.49 USD | 1,026,171.20 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.34` | `67.9200` | 3,486.81 USD | 1,014,871.70 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `51.34` | `700.5800` | 35,964.97 USD | 1,011,384.90 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `51.34` | `516.1400` | 26,496.05 USD | 975,419.92 USD | `2 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:14:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,763,271.00 USD | `346,127.65` | `58.90` | `51.32` | `530.02` | 2,623,089.09 USD | `+14.77%` | `5X Cross` |
| `124` | `0x4692...164f` | `SHORT` | 15,936,954.37 USD | `310,540.81` | `52.91` | `51.32` | `253.02` | 494,724.12 USD | `+3.10%` | `5X Cross` |
| `206` | `0xacb6...efbd` | `SHORT` | 10,321,156.83 USD | `201,133.33` | `59.63` | `51.32` | `76.89` | 1,671,500.29 USD | `+16.19%` | `6X Cross` |
| `240` | `0xc26c...b8f4` | `LONG` | 9,312,702.20 USD | `181,463.41` | `55.43` | `51.32` | `0.000000` | -746,052.88 USD | `-8.01%` | `2X Cross` |
| `288` | `0x49e9...e1d0` | `SHORT` | 8,205,432.15 USD | `159,887.61` | `55.44` | `51.32` | `102.37` | 658,323.57 USD | `+8.02%` | `4X Cross` |
| `354` | `0x645b...87b8` | `LONG` | 6,566,713.21 USD | `127,956.22` | `56.57` | `51.32` | `0.000000` | -671,729.35 USD | `-10.23%` | `3X Cross` |
| `358` | `0xd8c5...99b0` | `SHORT` | 6,483,123.41 USD | `126,320.04` | `61.98` | `51.32` | `199.05` | 1,346,214.43 USD | `+20.76%` | `3X Cross` |
| `390` | `0xe9ff...5903` | `SHORT` | 5,798,167.85 USD | `112,996.08` | `60.07` | `51.32` | `178.25` | 989,782.95 USD | `+17.07%` | `5X Cross` |
| `618` | `0x9aa5...58af` | `LONG` | 3,656,212.83 USD | `71,243.43` | `61.59` | `51.32` | `0.000000` | -731,944.70 USD | `-20.02%` | `20X Cross` |
| `662` | `0x354b...6425` | `SHORT` | 3,400,384.17 USD | `66,258.46` | `51.37` | `51.32` | `211.79` | 3,241.92 USD | `+0.10%` | `10X Cross` |
| `750` | `0x2056...8396` | `LONG` | 3,079,200.00 USD | `60,000.00` | `66.92` | `51.32` | `21.35` | -936,127.14 USD | `-30.40%` | `10X Cross` |
| `887` | `0x0242...ffa1` | `SHORT` | 2,561,723.50 USD | `49,916.67` | `56.48` | `51.32` | `312.99` | 257,408.36 USD | `+10.05%` | `10X Cross` |
| `892` | `0x960b...f0fc` | `LONG` | 2,538,182.51 USD | `49,457.96` | `55.82` | `51.32` | `0.000000` | -222,754.52 USD | `-8.78%` | `25X Cross` |
| `975` | `0x8b9d...7b28` | `LONG` | 2,300,833.54 USD | `44,823.47` | `58.35` | `51.32` | `0.000000` | -314,615.01 USD | `-13.67%` | `10X Cross` |
| `1054` | `0x5647...e7de` | `LONG` | 2,066,048.12 USD | `40,262.07` | `57.38` | `51.32` | `0.000000` | -244,189.48 USD | `-11.82%` | `20X Cross` |
| `1062` | `0xa2ce...3126` | `LONG` | 2,052,520.00 USD | `40,000.00` | `74.30` | `51.32` | `0.000000` | -919,535.49 USD | `-44.80%` | `20X Cross` |
| `1098` | `0xb078...de15` | `SHORT` | 2,001,480.51 USD | `39,000.01` | `52.58` | `51.32` | `202.63` | 49,038.44 USD | `+2.45%` | `8X Cross` |
| `1351` | `0xce97...7e78` | `LONG` | 1,611,640.97 USD | `31,406.82` | `51.51` | `51.32` | `0.000000` | -6,229.01 USD | `-0.39%` | `5X Cross` |
| `1430` | `0x5a88...d997` | `LONG` | 1,539,690.00 USD | `30,000.00` | `59.50` | `51.32` | `38.57` | -245,197.59 USD | `-15.93%` | `25X Cross` |
| `1431` | `0x3678...b209` | `LONG` | 1,539,630.00 USD | `30,000.00` | `57.15` | `51.32` | `0.000000` | -174,870.00 USD | `-11.36%` | `20X Cross` |
| `1650` | `0x7ea9...fc7f` | `LONG` | 1,282,825.00 USD | `25,000.00` | `53.60` | `51.32` | `35.05` | -57,179.05 USD | `-4.46%` | `25X Cross` |
| `1753` | `0x24fb...ed0f` | `LONG` | 1,185,982.09 USD | `23,110.00` | `51.37` | `51.32` | `0.000000` | -1,195.24 USD | `-0.10%` | `20X Cross` |
| `1795` | `0xf517...c032` | `LONG` | 1,160,519.22 USD | `22,627.50` | `66.29` | `51.32` | `0.000000` | -339,475.88 USD | `-29.25%` | `20X Cross` |
| `1924` | `0xcc9f...d218` | `LONG` | 1,053,014.59 USD | `20,520.60` | `52.63` | `51.32` | `26.86` | -26,893.46 USD | `-2.55%` | `2X Isolated` |

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
  * Current Rate: `9.41K` | Last 24h: `209.74K` | Last 3d: `432.77K` | Last 7d: `624.53K`
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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.13` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `49.88` (Risk Distance: `1.25` pts)
  * +2.5R Take Profit: `54.27`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `51.63` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.88` (Risk Distance: `1.25` pts)
  * +2.5R Take Profit: `48.49`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.06 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`51.69`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
