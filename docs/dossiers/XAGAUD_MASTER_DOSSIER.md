# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGAUD
**Canonical Key**: `XAGAUD` | **Broker Instrument**: `XAGAUD.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-30 10:25:43 IST` (`2026-10-30 04:55:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `51.33` | **Live Ask Quote**: `51.37` | **Mid Price**: `51.35`
- **Spread Points**: `36.00` | **Spread BPS**: `7.01 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `51.46` | VWAP Z-Score: `-1.05` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2424` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.81` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.07` | Lower -3.00σ Band: `50.85`
  * Upper +2.51σ Band: `51.97` | Lower -2.51σ Band: `50.95`
  * Upper +2.01σ Band: `51.87` | Lower -2.01σ Band: `51.05`
  * Upper +2.00σ Band: `51.87` | Lower -2.00σ Band: `51.05`
  * Upper +1.28σ Band: `51.72` | Lower -1.28σ Band: `51.20`
  * Upper +1.00σ Band: `51.66` | Lower -1.00σ Band: `51.26`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`51.35` | EMA-20=`51.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.85` (Slope: `+0.0000`) | EMA-100=`52.28`
  * Institutional Anchors: EMA-144=`52.55` | EMA-200=`52.79` (Slope: `-0.3396`) | EMA-233=`52.95`
- **Range Boundaries**: 24H High=`53.50` | 24H Low=`51.08` | Weekly High=`54.61` | Weekly Low=`51.08`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `51.63` (Distance: `-0.51%`)
  * Point of Control (POC) = `51.39` (Distance: `-0.05%`)
  * Value Area Low (VAL) = `51.14` (Distance: `+0.44%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.53` | Weekly POC=`53.89` | Weekly VAL=`52.81`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.55` | Low=`51.14`
  * New York Session (13:00-21:00 UTC): High=`51.66` | Low=`51.04`
  * Initial Balance (First Hour): IB High=`51.50` | IB Low=`51.19`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `51.14` - `51.55`
  * Optimal Trade Entry (OTE 0.705): `51.45`
  * Structural Invalidation Anchor (0.786): `51.76`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `51.47` | `51.48` | `51.27` | `51.38` | `2,667` | 137,038.46 USD | -20,654.12 USD | `-15.07%` | -867,340.67 USD | `-0.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `51.38` | `51.50` | `51.31` | `51.37` | `2,990` | 153,608.26 USD | -28,952.34 USD | `-18.85%` | -896,293.01 USD | `-0.32` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `51.37` | `51.49` | `51.19` | `51.26` | `3,941` | 201,995.96 USD | -99,974.35 USD | `-49.49%` | -996,267.36 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.26` | `51.58` | `51.15` | `51.47` | `8,843` | 455,158.05 USD | 224,945.01 USD | `+49.42%` | -2,190,114.49 USD | `+2.02` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `51.47` | `51.50` | `51.19` | `51.26` | `9,598` | 491,945.49 USD | -321,286.88 USD | `-65.31%` | -2,511,401.37 USD | `-2.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `51.26` | `51.63` | `51.10` | `51.55` | `6,872` | 354,224.11 USD | 217,547.07 USD | `+61.42%` | -2,293,854.30 USD | `+1.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `4h` | `51.78` | `51.80` | `51.08` | `51.34` | `77,060` | 3,956,260.40 USD | -1,742,181.24 USD | `-44.04%` | -6,520,387.16 USD | `-0.80` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `51.39` | `63.4200` | 3,259.34 USD | 173,902.87 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.39` | `4174.3100` | 214,526.14 USD | 388,429.01 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `51.39` | `34.3900` | 1,767.34 USD | 390,196.35 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `51.39` | `171.8200` | 8,829.83 USD | 399,026.18 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `51.39` | `3893.2900` | 200,072.28 USD | 599,098.46 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.39` | `39.7800` | 2,044.21 USD | 601,142.67 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `51.39` | `6008.1200` | 308,739.26 USD | 909,881.94 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `51.40` | `38.3300` | 1,970.32 USD | 13,420.15 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `51.40` | `0.2000` | 10.28 USD | 13,430.43 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `51.40` | `1666.2100` | 85,646.53 USD | 99,076.96 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `51.40` | `271.3500` | 13,947.66 USD | 113,024.62 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `51.40` | `18.1900` | 934.97 USD | 113,959.58 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `51.40` | `81.6200` | 4,195.19 USD | 118,154.77 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `51.40` | `549.3900` | 28,237.55 USD | 146,392.32 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `51.40` | `164.0200` | 8,430.14 USD | 154,822.45 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `51.40` | `154.5700` | 7,944.28 USD | 162,766.73 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `51.40` | `153.2600` | 7,876.80 USD | 170,643.53 USD | `2 orders` | `-0.03%` | `-` |
| `ASK` | `51.41` | `1470.3500` | 75,598.05 USD | 130,696.42 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.41` | `151.2900` | 7,778.42 USD | 55,098.37 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `51.41` | `121.5000` | 6,246.68 USD | 47,319.95 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `51.41` | `62.8300` | 3,230.22 USD | 41,073.27 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.41` | `700.2800` | 36,002.10 USD | 37,843.05 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `51.41` | `35.8100` | 1,840.96 USD | 1,840.96 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `51.41` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 51.41` | `0.00%` | `-` |
| `BID` | `51.41` | `16.0600` | 825.61 USD | 825.61 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `51.41` | `143.2500` | 7,364.05 USD | 8,189.67 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `51.41` | `63.4200` | 3,260.17 USD | 11,449.83 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `51.42` | `79.7200` | 4,099.60 USD | 641,518.25 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `51.42` | `5866.3400` | 301,670.67 USD | 637,418.65 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `51.42` | `3141.9200` | 161,566.95 USD | 335,747.98 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `51.42` | `347.4700` | 17,867.60 USD | 174,181.03 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `51.42` | `79.4600` | 4,085.91 USD | 156,313.43 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.42` | `191.1000` | 9,826.36 USD | 152,227.52 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `51.42` | `17.8200` | 916.29 USD | 142,401.15 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.42` | `141.6700` | 7,284.39 USD | 141,484.87 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `51.42` | `63.4100` | 3,260.35 USD | 134,200.48 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `51.42` | `4.7400` | 243.71 USD | 130,940.13 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `51.43` | `468.7500` | 24,107.34 USD | 689,137.00 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `51.43` | `136.2300` | 7,006.04 USD | 665,029.66 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `51.43` | `193.0200` | 9,926.44 USD | 658,023.62 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `51.43` | `127.9300` | 6,578.93 USD | 648,097.18 USD | `2 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

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
  * Execution Entry: `51.14` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.80` (Risk Distance: `0.3449` pts)
  * +2.5R Take Profit: `52.00`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `51.63` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `51.97` (Risk Distance: `0.3449` pts)
  * +2.5R Take Profit: `50.77`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`51.76`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
