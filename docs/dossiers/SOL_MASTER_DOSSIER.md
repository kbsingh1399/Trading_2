# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 02:42:47 IST` (`2026-10-29 21:12:47 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `95.08` | **Live Ask Quote**: `96.00` | **Mid Price**: `95.54`
- **Spread Points**: `92.00` | **Spread BPS**: `96.29 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `100.07` | VWAP Z-Score: `-3.15` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.8838` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `16.52` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `104.00` | Lower -3.00σ Band: `96.14`
  * Upper +2.51σ Band: `103.36` | Lower -2.51σ Band: `96.78`
  * Upper +2.01σ Band: `102.71` | Lower -2.01σ Band: `97.44`
  * Upper +2.00σ Band: `102.69` | Lower -2.00σ Band: `97.45`
  * Upper +1.28σ Band: `101.75` | Lower -1.28σ Band: `98.39`
  * Upper +1.00σ Band: `101.38` | Lower -1.00σ Band: `98.76`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`98.48` | EMA-20=`99.56` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`100.20` (Slope: `+0.0000`) | EMA-100=`100.49`
  * Institutional Anchors: EMA-144=`100.59` | EMA-200=`100.59` (Slope: `-0.1677`) | EMA-233=`100.60`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`94.56` | Weekly High=`103.63` | Weekly Low=`94.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `95.33` (Distance: `+0.35%`)
  * Point of Control (POC) = `95.04` (Distance: `+0.66%`)
  * Value Area Low (VAL) = `95.04` (Distance: `+0.66%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.54` | Weekly POC=`100.94` | Weekly VAL=`99.67`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`95.45` | Low=`95.04`
  * London Session (08:00-16:00 UTC): High=`95.92` | Low=`95.16`
  * New York Session (13:00-21:00 UTC): High=`96.11` | Low=`94.97`
  * Initial Balance (First Hour): IB High=`95.83` | IB Low=`95.25`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `95.16` - `95.92`
  * Optimal Trade Entry (OTE 0.705): `95.73`
  * Structural Invalidation Anchor (0.786): `96.30`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `96.70` | `96.79` | `96.04` | `96.10` | `249,876` | 24,089,939.92 USD | -2,653,827.76 USD | `-11.02%` | -130,050,073.13 USD | `+0.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `96.11` | `96.50` | `95.43` | `95.55` | `498,109` | 47,816,742.20 USD | -1,247,665.10 USD | `-2.61%` | -131,297,738.23 USD | `+0.18` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `95.54` | `95.64` | `95.34` | `95.61` | `55,551` | 5,302,154.09 USD | -1,336,842.34 USD | `-25.21%` | -132,634,580.57 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `99.39` | `99.57` | `96.21` | `96.70` | `1,970,996` | 192,431,903.91 USD | -26,903,885.44 USD | `-13.98%` | -115,244,658.33 USD | `-3.46` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `96.70` | `97.15` | `94.81` | `96.10` | `2,245,534` | 215,726,671.39 USD | -14,685,360.05 USD | `-6.81%` | -129,930,018.38 USD | `-1.46` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `96.11` | `96.50` | `95.34` | `95.39` | `542,844` | 52,085,586.01 USD | -2,968,608.02 USD | `-5.70%` | -132,898,626.40 USD | `+0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `100.57` | `100.61` | `99.76` | `99.78` | `679,393` | 68,026,040.28 USD | -1,354,724.67 USD | `-1.99%` | -71,717,987.73 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `99.78` | `99.90` | `94.81` | `96.10` | `5,935,409` | 578,463,305.23 USD | -52,522,739.54 USD | `-9.08%` | -124,240,727.27 USD | `-3.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `96.11` | `96.50` | `95.34` | `95.61` | `553,659` | 53,118,896.29 USD | -2,584,507.44 USD | `-4.87%` | -126,825,234.71 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -35,217,193.40 USD | `+0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -67,459,976.18 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.56` | `6,483,801` | 631,078,745.45 USD | -55,297,051.39 USD | `-8.76%` | -122,757,027.57 USD | `-1.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -29,365,912.19 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -33,659,266.07 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -35,217,193.40 USD | `+0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -67,459,976.18 USD | `-1.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.56` | `6,483,801` | 631,078,745.45 USD | -55,297,051.39 USD | `-8.76%` | -122,757,027.57 USD | `-1.59` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`95.54`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `95.52` | `92.3800` | 8,824.41 USD | 396,365.08 USD | `1 orders` | `-0.10%` | `-` |
| `BID` | `95.52` | `19.6200` | 1,874.14 USD | 398,239.22 USD | `1 orders` | `-0.10%` | `-` |
| `BID` | `95.53` | `519.7300` | 49,652.41 USD | 165,207.20 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `95.53` | `191.5400` | 18,298.58 USD | 183,505.78 USD | `2 orders` | `-0.09%` | `-` |
| `BID` | `95.53` | `26.5900` | 2,540.20 USD | 186,045.98 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `95.53` | `92.3800` | 8,825.15 USD | 194,871.13 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `95.53` | `30.0800` | 2,873.54 USD | 197,744.67 USD | `2 orders` | `-0.09%` | `-` |
| `BID` | `95.53` | `1.8300` | 174.82 USD | 197,919.49 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `95.53` | `53.1800` | 5,080.18 USD | 202,999.67 USD | `2 orders` | `-0.09%` | `-` |
| `BID` | `95.53` | `47.6100` | 4,548.04 USD | 207,547.71 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `95.53` | `1884.2300` | 179,992.95 USD | 387,540.66 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `95.54` | `325.6200` | 31,110.71 USD | 85,351.41 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `95.54` | `314.4000` | 30,037.15 USD | 115,388.56 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `95.54` | `1.7400` | 166.23 USD | 115,554.79 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `95.55` | `363.0100` | 34,687.06 USD | 49,785.43 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `95.55` | `0.5200` | 49.69 USD | 49,835.12 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `95.55` | `46.1100` | 4,405.58 USD | 54,240.70 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `95.57` | `104.6200` | 9,998.53 USD | 15,098.37 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `95.61` | `0.9400` | 89.88 USD | 89.88 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `95.61` | `52.4000` | 5,009.96 USD | 5,099.84 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `95.62` | `78.4500` | 7,501.39 USD | 12,591.14 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `95.62` | `53.2300` | 5,089.75 USD | 5,089.75 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `95.62` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 95.62` | `0.00%` | `-` |
| `ASK` | `95.63` | `228.8200` | 21,882.97 USD | 68,434.92 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `95.63` | `228.8200` | 21,882.74 USD | 46,551.95 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `95.63` | `0.8200` | 78.42 USD | 24,669.21 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `95.63` | `125.4800` | 11,999.65 USD | 24,590.79 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `95.64` | `209.9600` | 20,081.62 USD | 204,274.75 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `95.64` | `241.4000` | 23,088.46 USD | 184,193.12 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `95.64` | `1.2100` | 115.73 USD | 161,104.66 USD | `11 orders` | `+0.03%` | `-` |
| `ASK` | `95.64` | `441.6300` | 42,237.49 USD | 160,988.94 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `95.64` | `246.4500` | 23,570.23 USD | 118,751.44 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `95.64` | `50.8500` | 4,863.09 USD | 95,181.21 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `95.64` | `228.8200` | 21,883.20 USD | 90,318.12 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `95.65` | `69.2800` | 6,626.77 USD | 806,834.29 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `95.65` | `4536.4600` | 433,916.94 USD | 800,207.52 USD | `12 orders` | `+0.04%` | `-` |
| `ASK` | `95.65` | `1049.3800` | 100,373.20 USD | 366,290.58 USD | `27 orders` | `+0.04%` | `-` |
| `ASK` | `95.65` | `117.6000` | 11,248.32 USD | 265,917.39 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `95.65` | `117.6000` | 11,248.20 USD | 254,669.07 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `95.65` | `117.6000` | 11,248.09 USD | 243,420.86 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `95.65` | `291.6800` | 27,898.03 USD | 232,172.77 USD | `7 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15` | `0x5b5d...c060` | `SHORT` | 66,723,601.74 USD | `696,120.13` | `94.33` | `96.14` | `354.65` | -1,055,335.53 USD | `-1.58%` | `7X Cross` |
| `23` | `0x9c6a...a4ed` | `LONG` | 52,855,010.67 USD | `550,087.69` | `80.86` | `96.14` | `68.18` | 8,376,024.28 USD | `+15.85%` | `20X Cross` |
| `53` | `0xb83d...6e36` | `SHORT` | 24,868,687.02 USD | `259,300.02` | `91.42` | `96.14` | `686.17` | -1,163,554.00 USD | `-4.68%` | `5X Cross` |
| `80` | `0x3dc9...54b0` | `SHORT` | 21,155,438.27 USD | `220,000.19` | `105.90` | `96.14` | `172.92` | 2,143,669.01 USD | `+10.13%` | `20X Cross` |
| `101` | `0x9c89...600e` | `LONG` | 18,826,556.02 USD | `189,472.50` | `115.21` | `96.14` | `34.75` | -3,002,459.24 USD | `-15.95%` | `20X Cross` |
| `115` | `0x4a20...3c26` | `LONG` | 17,186,400.00 USD | `180,000.00` | `106.43` | `96.14` | `68.57` | -1,971,878.71 USD | `-11.47%` | `20X Cross` |
| `148` | `0xecb6...2b00` | `SHORT` | 13,853,914.81 USD | `144,451.55` | `102.63` | `96.14` | `283.73` | 971,187.72 USD | `+7.01%` | `20X Cross` |
| `181` | `0x7a5a...0394` | `SHORT` | 11,074,285.63 USD | `115,753.84` | `100.32` | `96.14` | `120.35` | 538,448.26 USD | `+4.86%` | `10X Cross` |
| `235` | `0xc63a...a3cd` | `LONG` | 9,589,000.00 USD | `100,000.00` | `112.22` | `96.14` | `0.000000` | -1,633,108.97 USD | `-17.03%` | `20X Cross` |
| `259` | `0xb581...6f4f` | `LONG` | 8,956,080.00 USD | `90,000.00` | `114.59` | `96.14` | `0.000000` | -1,357,212.29 USD | `-15.15%` | `3X Cross` |
| `294` | `0x645b...87b8` | `SHORT` | 8,010,089.44 USD | `83,523.26` | `103.90` | `96.14` | `351.47` | 668,221.53 USD | `+8.34%` | `20X Cross` |
| `309` | `0xdb3a...cf3b` | `LONG` | 7,842,873.86 USD | `81,851.78` | `106.04` | `96.14` | `44.76` | -836,873.00 USD | `-10.67%` | `4X Cross` |
| `317` | `0xe927...98ef` | `LONG` | 7,498,764.00 USD | `78,000.00` | `96.34` | `96.14` | `38.45` | -15,377.48 USD | `-0.21%` | `3X Cross` |
| `324` | `0x8ae4...3d60` | `LONG` | 7,177,584.17 USD | `72,180.05` | `111.72` | `96.14` | `3.73` | -886,576.07 USD | `-12.35%` | `10X Cross` |
| `327` | `0xca49...53c8` | `SHORT` | 7,072,395.22 USD | `73,943.45` | `110.70` | `96.14` | `297.75` | 1,113,227.04 USD | `+15.74%` | `20X Cross` |
| `336` | `0xa0b7...6165` | `SHORT` | 6,827,155.63 USD | `71,044.42` | `107.87` | `96.14` | `190.91` | 836,311.57 USD | `+12.25%` | `2X Cross` |
| `357` | `0xf517...c032` | `SHORT` | 6,530,176.70 USD | `67,778.53` | `84.64` | `96.14` | `222.98` | -793,145.53 USD | `-12.15%` | `20X Cross` |
| `468` | `0x7e23...5a5a` | `LONG` | 4,674,193.21 USD | `48,564.56` | `105.17` | `96.14` | `67.55` | -433,375.96 USD | `-9.27%` | `5X Isolated` |
| `545` | `0x7fda...17d1` | `SHORT` | 4,026,020.89 USD | `41,987.14` | `102.99` | `96.14` | `1110.47` | 298,263.49 USD | `+7.41%` | `20X Cross` |
| `588` | `0xf899...88db` | `SHORT` | 3,856,558.51 USD | `40,124.21` | `88.19` | `96.14` | `117.42` | -318,128.91 USD | `-8.25%` | `20X Cross` |
| `589` | `0x2e2b...2fab` | `LONG` | 3,849,880.00 USD | `40,000.00` | `119.55` | `96.14` | `57.90` | -932,155.64 USD | `-24.21%` | `10X Cross` |
| `610` | `0xfc66...ca06` | `SHORT` | 3,725,202.43 USD | `38,841.82` | `101.16` | `96.14` | `1031.16` | 203,951.73 USD | `+5.47%` | `20X Cross` |
| `634` | `0x27b8...12fc` | `LONG` | 3,585,586.39 USD | `36,085.73` | `110.86` | `96.14` | `15.98` | -414,758.86 USD | `-11.57%` | `10X Cross` |
| `635` | `0x9946...0852` | `SHORT` | 3,584,808.84 USD | `37,198.39` | `112.11` | `96.14` | `139.26` | 585,673.36 USD | `+16.34%` | `20X Cross` |
| `659` | `0x9c16...4a6f` | `SHORT` | 3,430,862.69 USD | `35,779.15` | `90.45` | `96.14` | `119.63` | -194,757.66 USD | `-5.68%` | `20X Cross` |
| `666` | `0x3440...32c5` | `SHORT` | 3,399,106.44 USD | `35,529.12` | `95.02` | `96.14` | `178.47` | -23,085.01 USD | `-0.68%` | `20X Cross` |
| `738` | `0x023a...2355` | `SHORT` | 3,085,335.31 USD | `32,188.97` | `101.45` | `96.14` | `343.68` | 180,135.34 USD | `+5.84%` | `20X Cross` |
| `739` | `0x96a7...79df` | `LONG` | 3,076,416.00 USD | `32,000.00` | `74.39` | `96.14` | `0.000000` | 696,010.15 USD | `+22.62%` | `20X Cross` |
| `784` | `0xbe19...8bd1` | `SHORT` | 2,907,731.39 USD | `30,451.69` | `97.62` | `96.14` | `761.31` | 64,815.24 USD | `+2.23%` | `3X Cross` |
| `787` | `0x482b...cae4` | `SHORT` | 2,894,045.59 USD | `30,310.49` | `88.03` | `96.14` | `151.14` | -225,797.30 USD | `-7.80%` | `20X Cross` |
| `799` | `0x610b...b613` | `LONG` | 2,849,648.54 USD | `29,634.14` | `101.23` | `96.14` | `70.39` | -150,350.81 USD | `-5.28%` | `3X Isolated` |
| `812` | `0x45d2...4029` | `SHORT` | 2,791,591.14 USD | `29,220.00` | `93.28` | `96.14` | `1553.75` | -65,815.16 USD | `-2.36%` | `20X Cross` |
| `817` | `0xa61c...66b9` | `LONG` | 2,782,896.59 USD | `28,888.00` | `104.39` | `96.14` | `0.000000` | -232,667.53 USD | `-8.36%` | `5X Cross` |
| `853` | `0x458d...ab3b` | `LONG` | 2,632,742.01 USD | `27,385.03` | `117.17` | `96.14` | `81.07` | -575,920.50 USD | `-21.88%` | `3X Isolated` |
| `921` | `0x051c...693c` | `LONG` | 2,416,880.48 USD | `25,139.70` | `89.76` | `96.14` | `39.29` | 160,319.15 USD | `+6.63%` | `20X Cross` |
| `930` | `0xfc27...9d9d` | `SHORT` | 2,397,307.40 USD | `24,997.34` | `102.53` | `96.14` | `789.03` | 165,681.68 USD | `+6.91%` | `20X Cross` |
| `970` | `0x638f...f5f0` | `LONG` | 2,301,768.00 USD | `24,000.00` | `136.71` | `96.14` | `48.08` | -979,200.54 USD | `-42.54%` | `20X Cross` |
| `1019` | `0x7178...0854` | `LONG` | 2,166,947.02 USD | `22,545.24` | `110.94` | `96.14` | `37.49` | -334,197.46 USD | `-15.42%` | `10X Cross` |
| `1034` | `0x739c...cfb2` | `LONG` | 2,116,950.00 USD | `22,000.00` | `91.95` | `96.14` | `75.88` | 94,042.69 USD | `+4.44%` | `20X Cross` |
| `1054` | `0x69cc...14fd` | `SHORT` | 2,073,042.47 USD | `21,701.57` | `99.01` | `96.14` | `473.25` | 75,610.28 USD | `+3.65%` | `20X Cross` |
| `1131` | `0x7737...bf66` | `SHORT` | 1,959,560.46 USD | `20,384.06` | `102.94` | `96.14` | `941.74` | 138,781.44 USD | `+7.08%` | `10X Cross` |
| `1151` | `0x251f...6e5d` | `LONG` | 1,926,916.00 USD | `20,000.00` | `101.15` | `96.14` | `66.43` | -96,181.77 USD | `-4.99%` | `20X Cross` |
| `1153` | `0xea00...a918` | `LONG` | 1,925,401.89 USD | `20,022.69` | `66.09` | `96.14` | `0.000000` | 602,093.29 USD | `+31.27%` | `20X Cross` |
| `1155` | `0xdf60...d3c7` | `LONG` | 1,924,940.00 USD | `20,000.00` | `120.12` | `96.14` | `94.00` | -477,468.53 USD | `-24.80%` | `7X Isolated` |
| `1156` | `0x3fc5...c0c1` | `SHORT` | 1,924,500.00 USD | `20,000.00` | `98.28` | `96.14` | `204.78` | 41,059.84 USD | `+2.13%` | `20X Cross` |
| `1157` | `0xbfc7...80b4` | `SHORT` | 1,922,440.00 USD | `20,000.00` | `85.98` | `96.14` | `371.49` | -202,905.50 USD | `-10.55%` | `20X Cross` |
| `1175` | `0xb322...d51f` | `LONG` | 1,896,800.73 USD | `19,774.82` | `102.98` | `96.14` | `56.70` | -139,670.67 USD | `-7.36%` | `20X Cross` |
| `1180` | `0x936c...bb0f` | `SHORT` | 1,883,521.41 USD | `19,639.04` | `105.58` | `96.14` | `643.13` | 189,999.79 USD | `+10.09%` | `20X Cross` |
| `1188` | `0x7160...d47c` | `LONG` | 1,864,060.57 USD | `19,434.10` | `105.03` | `96.14` | `85.31` | -177,160.72 USD | `-9.50%` | `20X Cross` |
| `1228` | `0xe097...d0fe` | `LONG` | 1,821,739.91 USD | `18,995.75` | `109.71` | `96.14` | `0.000000` | -262,256.97 USD | `-14.40%` | `20X Cross` |
| `1297` | `0xe98b...8cd5` | `SHORT` | 1,693,506.86 USD | `17,622.89` | `187.95` | `96.14` | `262.13` | 1,618,713.86 USD | `+95.58%` | `20X Cross` |
| `1302` | `0xdf95...7d72` | `SHORT` | 1,683,025.58 USD | `17,549.34` | `104.65` | `96.14` | `2406.79` | 153,566.95 USD | `+9.12%` | `20X Cross` |
| `1348` | `0xee2b...d67e` | `LONG` | 1,634,131.95 USD | `16,963.19` | `119.86` | `96.14` | `31.80` | -399,139.69 USD | `-24.43%` | `4X Cross` |
| `1362` | `0x123d...3bff` | `LONG` | 1,618,044.51 USD | `16,920.55` | `89.54` | `96.14` | `0.000000` | 103,050.76 USD | `+6.37%` | `10X Cross` |
| `1462` | `0x73d7...8be1` | `LONG` | 1,502,761.99 USD | `15,668.95` | `106.60` | `96.14` | `78.55` | -167,578.97 USD | `-11.15%` | `20X Cross` |
| `1468` | `0xc74a...ab93` | `LONG` | 1,493,329.22 USD | `15,536.82` | `64.06` | `96.14` | `54.88` | 498,100.39 USD | `+33.36%` | `5X Isolated` |
| `1494` | `0x34e6...8d74` | `LONG` | 1,447,396.79 USD | `15,091.67` | `101.19` | `96.14` | `39.53` | -79,674.10 USD | `-5.50%` | `20X Cross` |
| `1500` | `0xc7d1...51af` | `SHORT` | 1,442,070.00 USD | `15,000.00` | `105.79` | `96.14` | `138.76` | 144,805.00 USD | `+10.04%` | `20X Cross` |
| `1502` | `0x5f10...d49d` | `LONG` | 1,440,555.00 USD | `15,000.00` | `96.35` | `96.14` | `69.75` | -4,746.16 USD | `-0.33%` | `20X Cross` |
| `1503` | `0xffb2...5ed6` | `LONG` | 1,440,295.68 USD | `14,504.05` | `117.89` | `96.14` | `88.50` | -269,609.04 USD | `-18.72%` | `20X Cross` |
| `1572` | `0x0d6a...ca57` | `LONG` | 1,367,034.90 USD | `14,206.65` | `110.41` | `96.14` | `91.60` | -201,555.46 USD | `-14.74%` | `5X Isolated` |
| `1605` | `0x7277...0b98` | `SHORT` | 1,328,931.19 USD | `13,837.70` | `101.18` | `96.14` | `204.84` | 71,188.57 USD | `+5.36%` | `20X Cross` |
| `1839` | `0x2482...0e55` | `LONG` | 1,095,555.86 USD | `11,363.98` | `122.03` | `96.14` | `91.54` | -291,146.07 USD | `-26.58%` | `20X Isolated` |
| `1875` | `0x45db...86eb` | `LONG` | 1,064,517.75 USD | `11,100.00` | `110.69` | `96.14` | `68.66` | -164,164.15 USD | `-15.42%` | `5X Cross` |
| `1908` | `0x1d04...7c43` | `LONG` | 1,038,977.70 USD | `10,811.76` | `111.55` | `96.14` | `26.18` | -167,083.79 USD | `-16.08%` | `6X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `102.17` | 373.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.37K USD at 102.1700 USD [API] | `2026-10-28 03:30:30` |
| `ANNOUNCEMENT` | `INFO` | `102.18` | 31,770.83 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 31.77K USD at 102.1800 USD [API] | `2026-10-28 03:30:59` |
| `ANNOUNCEMENT` | `INFO` | `102.12` | 20,005.31 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 20.01K USD at 102.1200 USD [API] | `2026-10-28 04:36:05` |
| `ANNOUNCEMENT` | `INFO` | `102.14` | 30,360.09 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 30.36K USD at 102.1400 USD [API] | `2026-10-28 04:50:01` |
| `ANNOUNCEMENT` | `INFO` | `101.87` | 43,903.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 43.90K USD at 101.8700 USD [API] | `2026-10-28 05:40:11` |
| `ANNOUNCEMENT` | `INFO` | `101.95` | 34,001.34 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 34.00K USD at 101.9500 USD [API] | `2026-10-28 07:20:26` |
| `ANNOUNCEMENT` | `INFO` | `102.46` | 55,307.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 55.31K USD at 102.4600 USD [API] | `2026-10-28 08:06:40` |
| `ANNOUNCEMENT` | `INFO` | `102.46` | 101,129.04 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 101.13K USD at 102.4600 USD [API] | `2026-10-28 08:06:40` |
| `ANNOUNCEMENT` | `INFO` | `102.46` | 44,406.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 44.41K USD at 102.4600 USD [API] | `2026-10-28 08:06:40` |
| `ANNOUNCEMENT` | `INFO` | `102.46` | 172,969.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 172.97K USD at 102.4600 USD [API] | `2026-10-28 08:06:40` |
| `ANNOUNCEMENT` | `INFO` | `102.55` | 28,979.60 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 28.98K USD at 102.5500 USD [API] | `2026-10-28 08:23:18` |
| `ANNOUNCEMENT` | `INFO` | `103.00` | 33,060.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 33.06K USD at 103.0000 USD [API] | `2026-10-28 08:27:56` |
| `ANNOUNCEMENT` | `INFO` | `102.99` | 129.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.13K USD at 102.9900 USD [API] | `2026-10-28 08:26:53` |
| `ANNOUNCEMENT` | `INFO` | `102.99` | 9,147.57 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 9.15K USD at 102.9900 USD [API] | `2026-10-28 08:26:53` |
| `ANNOUNCEMENT` | `INFO` | `102.99` | 306.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.31K USD at 102.9900 USD [API] | `2026-10-28 08:26:53` |
| `ANNOUNCEMENT` | `INFO` | `102.99` | 218.34 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.22K USD at 102.9900 USD [API] | `2026-10-28 08:26:53` |
| `ANNOUNCEMENT` | `INFO` | `102.99` | 41.20 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.04K USD at 102.9900 USD [API] | `2026-10-28 08:26:53` |
| `ANNOUNCEMENT` | `INFO` | `102.99` | 36,553.21 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 36.55K USD at 102.9900 USD [API] | `2026-10-28 08:26:53` |
| `ANNOUNCEMENT` | `INFO` | `102.62` | 30,038.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 30.04K USD at 102.6200 USD [API] | `2026-10-28 09:01:16` |
| `ANNOUNCEMENT` | `INFO` | `102.62` | 49,356.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 49.36K USD at 102.6200 USD [API] | `2026-10-28 09:01:16` |
| `ANNOUNCEMENT` | `INFO` | `102.83` | 1,565.07 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.57K USD at 102.8300 USD [API] | `2026-10-28 08:26:42` |
| `ANNOUNCEMENT` | `INFO` | `102.83` | 57.58 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.06K USD at 102.8300 USD [API] | `2026-10-28 08:26:42` |
| `ANNOUNCEMENT` | `INFO` | `102.83` | 101.80 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.10K USD at 102.8300 USD [API] | `2026-10-28 08:26:42` |
| `ANNOUNCEMENT` | `INFO` | `102.83` | 4,500.87 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.50K USD at 102.8300 USD [API] | `2026-10-28 08:26:42` |
| `ANNOUNCEMENT` | `INFO` | `102.28` | 488.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.49K USD at 102.2800 USD [API] | `2026-10-28 03:32:25` |
| `ANNOUNCEMENT` | `INFO` | `102.28` | 20.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 102.2800 USD [API] | `2026-10-28 03:32:25` |
| `ANNOUNCEMENT` | `INFO` | `103.01` | 57,678.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 57.68K USD at 103.0100 USD [API] | `2026-10-28 10:16:31` |
| `ANNOUNCEMENT` | `INFO` | `103.19` | 199,982.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 199.98K USD at 103.1900 USD [API] | `2026-10-28 10:29:11` |
| `ANNOUNCEMENT` | `INFO` | `102.82` | 31,110.25 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 31.11K USD at 102.8200 USD [API] | `2026-10-28 11:00:25` |
| `ANNOUNCEMENT` | `INFO` | `102.96` | 346.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.35K USD at 102.9600 USD [API] | `2026-10-28 08:26:56` |
| `ANNOUNCEMENT` | `INFO` | `102.83` | 24,313.13 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 24.31K USD at 102.8300 USD [API] | `2026-10-28 08:26:42` |
| `ANNOUNCEMENT` | `INFO` | `102.83` | 1,305.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.31K USD at 102.8300 USD [API] | `2026-10-28 08:26:42` |
| `ANNOUNCEMENT` | `INFO` | `99.14` | 781.19 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.78K USD at 99.1360 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.14` | 11,621.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 11.62K USD at 99.1360 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 4,116.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 4.12K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 198.30 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.20K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 9,568.97 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 9.57K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 209.21 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.21K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 464.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.46K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 47.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.05K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 169.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.17K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 194.33 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.19K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 780.31 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.78K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 350.99 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.35K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 11.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 2,577.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.58K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 11.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 25.78 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.03K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 11.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 120.96 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.12K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.15` | 98.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.10K USD at 99.1500 USD [API] | `2026-10-27 10:14:43` |
| `ANNOUNCEMENT` | `INFO` | `99.25` | 574.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.57K USD at 99.2530 USD [API] | `2026-10-27 10:12:02` |
| `ANNOUNCEMENT` | `INFO` | `99.25` | 388.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.39K USD at 99.2530 USD [API] | `2026-10-27 10:12:02` |
| `ANNOUNCEMENT` | `INFO` | `99.25` | 20,066.97 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 20.07K USD at 99.2530 USD [API] | `2026-10-27 10:12:02` |
| `ANNOUNCEMENT` | `INFO` | `99.26` | 11.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 99.2600 USD [API] | `2026-10-27 10:11:54` |
| `ANNOUNCEMENT` | `INFO` | `99.26` | 1,396.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.40K USD at 99.2600 USD [API] | `2026-10-27 10:11:54` |
| `ANNOUNCEMENT` | `INFO` | `99.26` | 7,503.06 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 7.50K USD at 99.2600 USD [API] | `2026-10-27 10:11:50` |
| `ANNOUNCEMENT` | `INFO` | `99.26` | 48.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.05K USD at 99.2600 USD [API] | `2026-10-27 10:11:50` |
| `ANNOUNCEMENT` | `INFO` | `102.88` | 37,092.36 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 37.09K USD at 102.8800 USD [API] | `2026-10-28 11:29:31` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.14` (Vol: 4,700,000.00 USD, Dist: `+2.21%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`104.08` (Vol: 4,800,000.00 USD, Dist: `+5.18%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`101.14` (Vol: 4,700,000.00 USD, Dist: `+2.20%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`104.05` (Vol: 6,100,000.00 USD, Dist: `+5.14%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.25` | 577.50 USD | 140,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,520.00 USD | 140,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.85` | 20,250.00 USD | 140,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 17,640.00 USD | 140,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.65` | 516.25 USD | 140,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.05` | 759,600.00 USD | 140,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 401.85 USD | 140,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,760.00 USD | 140,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 4,770.00 USD | 140,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.65` | 1,060.00 USD | 140,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,630.00 USD | 140,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.85` | 474.58 USD | 140,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 109.15 USD | 140,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.15` | 297.92 USD | 140,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.25` | 9,940.00 USD | 140,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 8,280.00 USD | 140,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.55` | 1,670.00 USD | 140,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 1,440.00 USD | 140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.25` | 1,160.00 USD | 140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,380.00 USD | 140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 122.55 USD | 140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.95` | 17,960.00 USD | 140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 1,750.00 USD | 139,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.15` | 1,160.00 USD | 139,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.45` | 1,500.00 USD | 139,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 147,310.00 USD | 139,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.75` | 192.31 USD | 139,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.95` | 394.21 USD | 139,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 272,090.00 USD | 139,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 139,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 2,400.00 USD | 139,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 106.64 USD | 139,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.65` | 37,670.00 USD | 139,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.75` | 10,090.00 USD | 139,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 2,930.00 USD | 139,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 136.24 USD | 139,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.45` | 476.89 USD | 139,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 102.60 USD | 139,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.75` | 2,280.00 USD | 139,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 268.34 USD | 139,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.15` | 149.87 USD | 139,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 332.30 USD | 139,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 82,350.00 USD | 139,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 13,780.00 USD | 139,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.65` | 168.66 USD | 139,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 412.18 USD | 139,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 3,490.00 USD | 139,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,200.00 USD | 139,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 113.80 USD | 139,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 184.72 USD | 139,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.65` | 253.84 USD | 139,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 9,810.00 USD | 139,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 424.41 USD | 139,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 3,050.00 USD | 139,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 26,210.00 USD | 139,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.25` | 63,520.00 USD | 139,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 44,020.00 USD | 139,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.45` | 2,710.00 USD | 139,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.65` | 7,440.00 USD | 139,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.85` | 4,890.00 USD | 139,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 5,940.00 USD | 139,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 7,170.00 USD | 139,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 47,340.00 USD | 139,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.35` | 738.72 USD | 139,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 889.01 USD | 139,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 233.86 USD | 139,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 34,710.00 USD | 139,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 278.33 USD | 139,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.75` | 3,860.00 USD | 139,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 1,070.00 USD | 139,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 541,970.00 USD | 139,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 101.28 USD | 138,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 373.58 USD | 138,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 477.34 USD | 138,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.55` | 5,420.00 USD | 138,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 718.21 USD | 138,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 5,240.00 USD | 138,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 1,920.00 USD | 138,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.35` | 3,900.00 USD | 138,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.45` | 222.78 USD | 138,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 2,890.00 USD | 138,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.85` | 17,710.00 USD | 138,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.95` | 210.83 USD | 138,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 973.83 USD | 138,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.35` | 46,170.00 USD | 138,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 4,210.00 USD | 138,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 486.14 USD | 138,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 1,800.00 USD | 138,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.85` | 14,520.00 USD | 138,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 6,620,000.00 USD | 138,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 2,150.00 USD | 131,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.25` | 20,240.00 USD | 131,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 2,120.00 USD | 131,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 50,220.00 USD | 131,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 222.63 USD | 131,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 5,610.00 USD | 131,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 531.41 USD | 131,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 315.38 USD | 131,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 4,410.00 USD | 131,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 2,410.00 USD | 131,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 2,340.00 USD | 131,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 50,050.00 USD | 131,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,660.00 USD | 131,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 250.09 USD | 131,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 837,560.00 USD | 131,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 7,830.00 USD | 130,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 21,280.00 USD | 130,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.45` | 304,940.00 USD | 130,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 2,520.00 USD | 130,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 2,430.00 USD | 130,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 4,300.00 USD | 130,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 2,950.00 USD | 130,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 191,750.00 USD | 130,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,970,000.00 USD | 130,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 67,730.00 USD | 126,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 736.64 USD | 126,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 126,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 883.39 USD | 126,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 51,140.00 USD | 126,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 16,420.00 USD | 126,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.25` | 462.76 USD | 126,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 117,240.00 USD | 126,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 2,040.00 USD | 126,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 1,560.00 USD | 126,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 445.20 USD | 126,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,270.00 USD | 126,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.95` | 2,750.00 USD | 126,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 17,850.00 USD | 126,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 8,700.00 USD | 126,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 2,200.00 USD | 126,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 105.72 USD | 126,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 240.27 USD | 126,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 9,800.00 USD | 126,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.75` | 6,750.00 USD | 126,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 2,770.00 USD | 126,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 465.19 USD | 126,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 4,380.00 USD | 126,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 13,250.00 USD | 126,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 2,170.00 USD | 126,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 418.46 USD | 126,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 130.88 USD | 126,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 126,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 7,210.00 USD | 126,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 1,440.00 USD | 126,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 4,290.00 USD | 126,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 213.61 USD | 126,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 2,790.00 USD | 126,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 308.85 USD | 126,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 2,410.00 USD | 126,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 4,250.00 USD | 126,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 57,740.00 USD | 126,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 3,330.00 USD | 125,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 18,840.00 USD | 125,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,020.00 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 163.31 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 213.01 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 106.31 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 242.16 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 11,220.00 USD | 125,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 104.64 USD | 125,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 41,590.00 USD | 125,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 5,980.00 USD | 125,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 6,790.00 USD | 125,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 17,870.00 USD | 125,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 410.78 USD | 125,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 1,790.00 USD | 125,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 2,630.00 USD | 125,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 120,590.00 USD | 125,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 179.70 USD | 125,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 8,090.00 USD | 125,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 10,470.00 USD | 125,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 10,020.00 USD | 125,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,840.00 USD | 125,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 319.09 USD | 125,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,450.00 USD | 125,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 458.50 USD | 125,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 26,180.00 USD | 125,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 742.33 USD | 125,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 46,250.00 USD | 125,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 3,590.00 USD | 125,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 522.76 USD | 125,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 14,810.00 USD | 125,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 5,050.00 USD | 125,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 140.55 USD | 125,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 2,330.00 USD | 125,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.05` | 10,550.00 USD | 125,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 3,520.00 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 3,050.00 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,630.00 USD | 125,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 3,480.00 USD | 125,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 1,190.00 USD | 125,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 14,080.00 USD | 125,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 5,740.00 USD | 125,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 1,160,000.00 USD | 125,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 5,280.00 USD | 124,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 13,820.00 USD | 124,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 3,310.00 USD | 124,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 8,450.00 USD | 124,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 453.38 USD | 124,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 13,000.00 USD | 124,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,250.00 USD | 124,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,120.00 USD | 124,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 4,150,000.00 USD | 124,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 10,790.00 USD | 120,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 733.34 USD | 120,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 5,320.00 USD | 120,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 8,310.00 USD | 120,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 1,600.00 USD | 120,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 6,990.00 USD | 120,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 6,210.00 USD | 120,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 14,670.00 USD | 120,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 8,560.00 USD | 120,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 1,890.00 USD | 120,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 11,670.00 USD | 120,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,170.00 USD | 120,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 2,910.00 USD | 120,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 337.33 USD | 120,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 12,190.00 USD | 120,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 19,710.00 USD | 120,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 3,850.00 USD | 120,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 2,680.00 USD | 120,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 59,700.00 USD | 120,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 10,820.00 USD | 119,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 360.48 USD | 119,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 7,210.00 USD | 119,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 22,760.00 USD | 119,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 302.15 USD | 119,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 26,370.00 USD | 119,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 45,490.00 USD | 119,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 478,640.00 USD | 119,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 98,310.00 USD | 119,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,690.00 USD | 119,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,320.00 USD | 119,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 4,600.00 USD | 119,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 879.59 USD | 119,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 1,460.00 USD | 119,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 4,270.00 USD | 119,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 27,610.00 USD | 119,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 9,530.00 USD | 119,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 3,890.00 USD | 119,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 5,120.00 USD | 119,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 27,710.00 USD | 119,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,050,000.00 USD | 119,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 3,260.00 USD | 118,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 34,550.00 USD | 118,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 44,800.00 USD | 118,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 916.88 USD | 118,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 118,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 19,810.00 USD | 118,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 59,050.00 USD | 118,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 3,360.00 USD | 117,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 15,030.00 USD | 117,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 11,500.00 USD | 117,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 3,980.00 USD | 117,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 753.04 USD | 117,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 64,870.00 USD | 117,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 3,510.00 USD | 117,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 17,320.00 USD | 117,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 958,960.00 USD | 117,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 259,570.00 USD | 116,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 26,930.00 USD | 116,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 739.01 USD | 116,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,010.00 USD | 116,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 12,110.00 USD | 116,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 5,970.00 USD | 116,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 15,130.00 USD | 116,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 7,060.00 USD | 116,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 85,360.00 USD | 116,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 4,090.00 USD | 116,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 1,180.00 USD | 116,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 7,310.00 USD | 116,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 36,190.00 USD | 116,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 17,970.00 USD | 116,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 7,880.00 USD | 116,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 16,640.00 USD | 116,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 90,120.00 USD | 116,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 1,130,000.00 USD | 116,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 15,090.00 USD | 115,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 122.80 USD | 115,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 24,680.00 USD | 115,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 4,410.00 USD | 115,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 5,380.00 USD | 115,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 1,380.00 USD | 115,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 9,580.00 USD | 115,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 25,070.00 USD | 115,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 924.25 USD | 115,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 2,320,000.00 USD | 115,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 65,310.00 USD | 112,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 29,860.00 USD | 112,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 16,610.00 USD | 112,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 4,710.00 USD | 112,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 127,240.00 USD | 112,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 9,870.00 USD | 112,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 17,330.00 USD | 112,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 2,970.00 USD | 112,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 418.17 USD | 112,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 195.64 USD | 112,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 6,130.00 USD | 112,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 48,160.00 USD | 112,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 17,200.00 USD | 112,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 11,490.00 USD | 112,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 13,850.00 USD | 112,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 28,430.00 USD | 112,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 9,240.00 USD | 112,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 68,160.00 USD | 112,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 4,680.00 USD | 112,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 12,090.00 USD | 112,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 74,960.00 USD | 112,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 37,240.00 USD | 112,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 54,140.00 USD | 112,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 35,270.00 USD | 112,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 2,340.00 USD | 112,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 2,090.00 USD | 112,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.45` | 557.35 USD | 112,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 2,760.00 USD | 112,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 8,400.00 USD | 112,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 7,040.00 USD | 112,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 28,700.00 USD | 112,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 78,670.00 USD | 112,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,230.00 USD | 111,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 683.66 USD | 111,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 125,590.00 USD | 111,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 23,340.00 USD | 111,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 13,520.00 USD | 111,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 121.87 USD | 111,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 39,450.00 USD | 111,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 16,580.00 USD | 111,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 5,780.00 USD | 111,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 3,980.00 USD | 111,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 66,840.00 USD | 111,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 25,350.00 USD | 111,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 3,850.00 USD | 111,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 31,770.00 USD | 111,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 20,410.00 USD | 111,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 3,250.00 USD | 111,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 7,620.00 USD | 111,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 4,830.00 USD | 111,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 31,310.00 USD | 111,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 65,480.00 USD | 111,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 15,420.00 USD | 111,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 81,940.00 USD | 111,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 14,620.00 USD | 111,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.35` | 14,240.00 USD | 111,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 43,420.00 USD | 111,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 6,000.00 USD | 111,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 8,840.00 USD | 111,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 8,560.00 USD | 111,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 46,170.00 USD | 111,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 39,740.00 USD | 111,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.05` | 384,300.00 USD | 111,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 14,550.00 USD | 110,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 875.16 USD | 110,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 6,300.00 USD | 110,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 1,400.00 USD | 110,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 1,740.00 USD | 110,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 5,660.00 USD | 110,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 6,290.00 USD | 110,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 13,530.00 USD | 110,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 18,550.00 USD | 110,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 7,960.00 USD | 110,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 17,210.00 USD | 110,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 8,740.00 USD | 110,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 58,380.00 USD | 110,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 56,580.00 USD | 110,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 56,660.00 USD | 110,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 16,870.00 USD | 110,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 367.90 USD | 110,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.15` | 4,420.00 USD | 110,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 25,970.00 USD | 110,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,460.00 USD | 110,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 1,490.00 USD | 110,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 45,890.00 USD | 110,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 14,310.00 USD | 110,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 5,010.00 USD | 110,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 1,340.00 USD | 110,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 1,050.00 USD | 110,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 33,390.00 USD | 110,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 2,510.00 USD | 110,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 1,360,000.00 USD | 110,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 2,900.00 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 37,840.00 USD | 109,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 3,340,000.00 USD | 108,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 125,880.00 USD | 105,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 3,160.00 USD | 105,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 13,570.00 USD | 105,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.95` | 11,870.00 USD | 105,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 170.13 USD | 105,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 105,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 12,330,000.00 USD | 67,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 4,860.00 USD | 55,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 21,590.00 USD | 55,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 41,980.00 USD | 55,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 779,380.00 USD | 55,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 60,650.00 USD | 54,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 3,240.00 USD | 54,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 57,300.00 USD | 54,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 3,570.00 USD | 54,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 11,350.00 USD | 54,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 9,450.00 USD | 54,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.35` | 1,210.00 USD | 54,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 15,690.00 USD | 54,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 11,110.00 USD | 54,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 5,490.00 USD | 54,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 20,550.00 USD | 54,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 1,070,000.00 USD | 54,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 9,180.00 USD | 53,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 1,550.00 USD | 53,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 40,220.00 USD | 53,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 73,520.00 USD | 53,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,130,000.00 USD | 53,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 114,610.00 USD | 51,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 161,340.00 USD | 51,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 98,950.00 USD | 51,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 13,570.00 USD | 50,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 23,480.00 USD | 50,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 249,420.00 USD | 50,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 32,670.00 USD | 50,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 64,890.00 USD | 50,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 8,380.00 USD | 50,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 351.76 USD | 50,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 17,590.00 USD | 50,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 47,190.00 USD | 50,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 11,910.00 USD | 50,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 29,930.00 USD | 50,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 40,080.00 USD | 50,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 12,430.00 USD | 50,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 11,420.00 USD | 50,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 158,970.00 USD | 50,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 41,150.00 USD | 50,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 507,050.00 USD | 50,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 5,140.00 USD | 49,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 12,640.00 USD | 49,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 7,030.00 USD | 49,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 24,880.00 USD | 49,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 24,660.00 USD | 49,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 8,140.00 USD | 49,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 6,710.00 USD | 49,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 94,110.00 USD | 49,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 39,050.00 USD | 49,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 12,760.00 USD | 49,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 22,160.00 USD | 49,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 22,620.00 USD | 49,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 102,150.00 USD | 49,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 65,320.00 USD | 49,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 11,750.00 USD | 49,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,280.00 USD | 49,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 25,370.00 USD | 49,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 6,390.00 USD | 49,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 46,240.00 USD | 49,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 36,220.00 USD | 49,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 14,530.00 USD | 49,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 2,000.00 USD | 49,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 1,570.00 USD | 49,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 37,430.00 USD | 49,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 130,140.00 USD | 48,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 17,870.00 USD | 48,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 46,460.00 USD | 48,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.15` | 6,180.00 USD | 48,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 16,870.00 USD | 48,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 37,330.00 USD | 48,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 3,370.00 USD | 48,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 32,450.00 USD | 48,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 1,680,000.00 USD | 48,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 1,720,000.00 USD | 47,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 15,170.00 USD | 45,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 14,860.00 USD | 45,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 10,650.00 USD | 45,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 7,890.00 USD | 45,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 9,000.00 USD | 45,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 39,070.00 USD | 45,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 1,090.00 USD | 45,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 26,470.00 USD | 45,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 3,990.00 USD | 45,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 37,790.00 USD | 45,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 302,800.00 USD | 45,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 29,880.00 USD | 44,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 27,740.00 USD | 44,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 78,560.00 USD | 44,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 23,850.00 USD | 44,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 4,390.00 USD | 44,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 22,240.00 USD | 44,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 8,270.00 USD | 44,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.65` | 217,510.00 USD | 44,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 357,790.00 USD | 44,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 30,120.00 USD | 44,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 21,290.00 USD | 44,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 17,080.00 USD | 43,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 66,520.00 USD | 43,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 23,450.00 USD | 43,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 1,290,000.00 USD | 43,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 34,110.00 USD | 42,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 521,930.00 USD | 42,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 4,010.00 USD | 42,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 68,860.00 USD | 42,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 4,860.00 USD | 41,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 2,260.00 USD | 41,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 2,820.00 USD | 41,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 619,090.00 USD | 41,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 143,470.00 USD | 41,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 29,540.00 USD | 41,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 15,890.00 USD | 41,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 330.93 USD | 41,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 28,820.00 USD | 41,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 989.70 USD | 41,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 21,470.00 USD | 41,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 3,760.00 USD | 41,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 23,880.00 USD | 41,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 73,460.00 USD | 41,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 180,870.00 USD | 40,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 2,870.00 USD | 40,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 5,580.00 USD | 40,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 4,710.00 USD | 40,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 3,200.00 USD | 40,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 36,100.00 USD | 40,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 3,550.00 USD | 40,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,240,000.00 USD | 40,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 43,680.00 USD | 38,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 38,330.00 USD | 38,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 82,790.00 USD | 38,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 783,730.00 USD | 38,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 22,300.00 USD | 37,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 27,160.00 USD | 37,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 64,950.00 USD | 37,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 41,470.00 USD | 37,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 14,790.00 USD | 37,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 127,690.00 USD | 37,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 799,480.00 USD | 37,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 19,230.00 USD | 36,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 27,660.00 USD | 36,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 212,490.00 USD | 36,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 32,090.00 USD | 36,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.65` | 103,500.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 40,220.00 USD | 36,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.85` | 19,850.00 USD | 36,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 46,200.00 USD | 36,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.05` | 14,570.00 USD | 35,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 25,050.00 USD | 35,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.25` | 15,690.00 USD | 35,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 59,090.00 USD | 35,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.45` | 91,070.00 USD | 35,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 24,000.00 USD | 35,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.65` | 71,200.00 USD | 35,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 77,950.00 USD | 35,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.85` | 220,850.00 USD | 35,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 32,020.00 USD | 35,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 169,520.00 USD | 35,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 80,010.00 USD | 35,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.25` | 50,560.00 USD | 35,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 34,210.00 USD | 35,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.45` | 83,650.00 USD | 35,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 11,030.00 USD | 34,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 60,340.00 USD | 34,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 1,690,000.00 USD | 34,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 11,870.00 USD | 33,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 125,170.00 USD | 33,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 83,020.00 USD | 33,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 1,730.00 USD | 32,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.25` | 561,670.00 USD | 32,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 33,390.00 USD | 32,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.45` | 26,990.00 USD | 32,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 10,720.00 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.65` | 64,670.00 USD | 32,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 9,040.00 USD | 32,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.85` | 38,890.00 USD | 32,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 33,670.00 USD | 32,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.00` | 40,660,000.00 USD | 40,660,000.00 USD | 0.00 USD | 0.00 USD | 205,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.05` | 1,290,000.00 USD | 32,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 135,160.00 USD | 30,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.20` | 40,460,000.00 USD | 40,460,000.00 USD | 12,120.00 USD | 85,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.25` | 102,400.00 USD | 30,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.30` | 62,530,000.00 USD | 62,530,000.00 USD | 0.00 USD | 149,300.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.35` | 323.81 USD | 30,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.45` | 44,940.00 USD | 30,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.50` | 62,380,000.00 USD | 62,380,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.55` | 48,900.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.60` | 40,360,000.00 USD | 40,360,000.00 USD | 0.00 USD | 306,270.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.65` | 155,550.00 USD | 30,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.75` | 24,170.00 USD | 30,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.80` | 40,050,000.00 USD | 40,050,000.00 USD | 0.00 USD | 66,610.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.85` | 56,980.00 USD | 30,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.90` | 62,370,000.00 USD | 62,370,000.00 USD | 207,900.00 USD | 138,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.95` | 79,240.00 USD | 30,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.00` | 39,980,000.00 USD | 39,980,000.00 USD | 150,240.00 USD | 112,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.05` | 246,250.00 USD | 30,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.15` | 260,410.00 USD | 29,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.20` | 39,720,000.00 USD | 39,720,000.00 USD | 0.00 USD | 0.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.25` | 21,370.00 USD | 29,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.35` | 189,640.00 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.45` | 531,360.00 USD | 29,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.55` | 220,040.00 USD | 28,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.65` | 460,370.00 USD | 28,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.70` | 62,030,000.00 USD | 62,030,000.00 USD | 0.00 USD | 0.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.75` | 1,220.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.85` | 9,490.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.95` | 9,640.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.05` | 39,460.00 USD | 28,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.15` | 18,880.00 USD | 28,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.25` | 83,470.00 USD | 28,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.35` | 49,150.00 USD | 28,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.45` | 79,830.00 USD | 28,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.55` | 242,790.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.60` | 39,710,000.00 USD | 39,710,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.65` | 27,500.00 USD | 27,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.70` | 62,020,000.00 USD | 62,020,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.75` | 130,590.00 USD | 27,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.80` | 39,710,000.00 USD | 39,710,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 23,370.00 USD | 27,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.90` | 61,800,000.00 USD | 61,800,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.95` | 259,400.00 USD | 27,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.00` | 38,810,000.00 USD | 38,810,000.00 USD | 8,600.00 USD | 2,360.00 USD | 217,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 52,590.00 USD | 27,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.10` | 61,780,000.00 USD | 61,780,000.00 USD | 350,210.00 USD | 291,000.00 USD | 576,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.15` | 15,510.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.20` | 38,580,000.00 USD | 38,580,000.00 USD | 166,240.00 USD | 99,310.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 41,380.00 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.30` | 60,560,000.00 USD | 60,560,000.00 USD | 14,870.00 USD | 7,630.00 USD | 3,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.35` | 18,740.00 USD | 27,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.40` | 38,320,000.00 USD | 38,320,000.00 USD | 12,630.00 USD | 93,010.00 USD | 265,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 52,650.00 USD | 27,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.50` | 60,530,000.00 USD | 60,530,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.55` | 25,560.00 USD | 27,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.60` | 37,950,000.00 USD | 37,950,000.00 USD | 557,950.00 USD | 163,120.00 USD | 317,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 16,210.00 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.70` | 59,740,000.00 USD | 59,740,000.00 USD | 780,700.00 USD | 190,280.00 USD | 450,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.75` | 68,900.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.80` | 36,910,000.00 USD | 36,910,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 56,790.00 USD | 27,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.90` | 58,320,000.00 USD | 58,320,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.95` | 150,160.00 USD | 26,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.00` | 35,800,000.00 USD | 35,800,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 310,590.00 USD | 26,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.10` | 56,520,000.00 USD | 56,520,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.15` | 28,210.00 USD | 26,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.20` | 34,450,000.00 USD | 34,450,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 52,860.00 USD | 26,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.30` | 54,150,000.00 USD | 54,150,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.35` | 31,850.00 USD | 26,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.40` | 33,120,000.00 USD | 33,120,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 9,870.00 USD | 26,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.50` | 52,070,000.00 USD | 52,070,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.55` | 23,760.00 USD | 26,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 31,770,000.00 USD | 31,770,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 79,210.00 USD | 26,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.70` | 49,390,000.00 USD | 49,390,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.75` | 64,910.00 USD | 26,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.80` | 30,630,000.00 USD | 30,630,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 111,640.00 USD | 26,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.90` | 46,940,000.00 USD | 46,940,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.95` | 267,140.00 USD | 26,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.00` | 30,420,000.00 USD | 30,420,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 439,360.00 USD | 25,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.10` | 44,560,000.00 USD | 44,560,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.15` | 278,840.00 USD | 25,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.20` | 30,230,000.00 USD | 30,230,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 21,060.00 USD | 25,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.30` | 42,650,000.00 USD | 42,650,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.35` | 152,860.00 USD | 25,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.40` | 30,200,000.00 USD | 30,200,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 34,870.00 USD | 24,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.50` | 40,150,000.00 USD | 40,150,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.55` | 2,450,000.00 USD | 24,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 30,030,000.00 USD | 30,030,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 45,140.00 USD | 22,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.70` | 37,230,000.00 USD | 37,230,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.75` | 361,750.00 USD | 22,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.80` | 29,900,000.00 USD | 29,900,000.00 USD | 250,490.00 USD | 103,030.00 USD | 525,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 27,090.00 USD | 22,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.90` | 35,600,000.00 USD | 35,600,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.95` | 145,240.00 USD | 22,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.00` | 29,030,000.00 USD | 29,030,000.00 USD | 40,010.00 USD | 288,020.00 USD | 88,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 15,920.00 USD | 21,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.10` | 33,190,000.00 USD | 33,190,000.00 USD | 494,450.00 USD | 947,560.00 USD | 258,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.15` | 299,200.00 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.20` | 28,610,000.00 USD | 28,610,000.00 USD | 106,580.00 USD | 171,510.00 USD | 60,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 107,850.00 USD | 21,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.30` | 31,490,000.00 USD | 31,490,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.35` | 194,290.00 USD | 21,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.40` | 28,270,000.00 USD | 28,270,000.00 USD | 149,180.00 USD | 845,850.00 USD | 991,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 107,230.00 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.50` | 29,130,000.00 USD | 29,130,000.00 USD | 259,870.00 USD | 570,240.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.55` | 317,480.00 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 26,280,000.00 USD | 26,280,000.00 USD | 380,700.00 USD | 222,110.00 USD | 56,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 218,230.00 USD | 20,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.70` | 27,370,000.00 USD | 27,370,000.00 USD | 671,470.00 USD | 168,780.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.75` | 608,070.00 USD | 20,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.80` | 25,620,000.00 USD | 25,620,000.00 USD | 26,180.00 USD | 402,380.00 USD | 97,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 484,570.00 USD | 20,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.90` | 26,460,000.00 USD | 26,460,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.95` | 21,840.00 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.00` | 25,100,000.00 USD | 25,100,000.00 USD | 0.00 USD | 0.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 47,480.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.10` | 26,400,000.00 USD | 26,400,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.15` | 139,650.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.25` | 451,130.00 USD | 19,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.30` | 26,000,000.00 USD | 26,000,000.00 USD | 55,470.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.35` | 153,040.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.45` | 528,000.00 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.50` | 25,890,000.00 USD | 25,890,000.00 USD | 101,820.00 USD | 215,050.00 USD | 11,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.55` | 719,190.00 USD | 18,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.60` | 25,090,000.00 USD | 25,090,000.00 USD | 0.00 USD | 0.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 145,100.00 USD | 17,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.70` | 25,570,000.00 USD | 25,570,000.00 USD | 270,240.00 USD | 262,300.00 USD | 115,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.75` | 80,060.00 USD | 17,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.80` | 24,060,000.00 USD | 24,060,000.00 USD | 42,130.00 USD | 427,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.85` | 36,460.00 USD | 17,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.90` | 24,920,000.00 USD | 24,920,000.00 USD | 168,420.00 USD | 101,680.00 USD | 111,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.95` | 2,220,000.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.00` | 23,590,000.00 USD | 23,590,000.00 USD | 60,590.00 USD | 86,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.05` | 203,240.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.10` | 24,540,000.00 USD | 24,540,000.00 USD | 233,120.00 USD | 999,200.00 USD | 342,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 35,200.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.20` | 23,450,000.00 USD | 23,450,000.00 USD | 0.00 USD | 691,260.00 USD | 702,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `94.25` | 36,060.00 USD | 36,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.30` | 22,960,000.00 USD | 22,960,000.00 USD | 10,610.00 USD | 0.00 USD | 711,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.35` | 90,750.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.40` | 22,050,000.00 USD | 22,050,000.00 USD | 33,670.00 USD | 1,120,000.00 USD | 15,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 1,070,000.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.50` | 22,240,000.00 USD | 22,240,000.00 USD | 245,400.00 USD | 698,220.00 USD | 140,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.55` | 201,770.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.60` | 20,880,000.00 USD | 20,880,000.00 USD | 772,520.00 USD | 320,240.00 USD | 2,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.65` | 12,840,000.00 USD | 13,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.70` | 21,150,000.00 USD | 21,150,000.00 USD | 1,600,000.00 USD | 238,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.75` | 93,270.00 USD | 553,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.80` | 17,710,000.00 USD | 17,710,000.00 USD | 762,670.00 USD | 2,150,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 40,310.00 USD | 460,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.90` | 19,320,000.00 USD | 19,320,000.00 USD | 1,100,000.00 USD | 2,230,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.95` | 233,250.00 USD | 420,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.00` | 13,760,000.00 USD | 13,760,000.00 USD | 519,290.00 USD | 717,410.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.05` | 621.63 USD | 187,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.10` | 15,980,000.00 USD | 15,980,000.00 USD | 141,070.00 USD | 226,060.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.15` | 13,980.00 USD | 186,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.20` | 12,510,000.00 USD | 12,510,000.00 USD | 34,680.00 USD | 3,270,000.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.25` | 13,750.00 USD | 172,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.30` | 14,280,000.00 USD | 14,280,000.00 USD | 499,140.00 USD | 321,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.35` | 31,760.00 USD | 158,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.40` | 7,800,000.00 USD | 7,800,000.00 USD | 263,100.00 USD | 224,710.00 USD | 11,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.45` | 3,410.00 USD | 127,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.50` | 13,460,000.00 USD | 13,460,000.00 USD | 1,200,000.00 USD | 1,580,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.55` | 44,880.00 USD | 123,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 7,300,000.00 USD | 7,300,000.00 USD | 2,570,000.00 USD | 8,020.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.70` | 10,680,000.00 USD | 10,680,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.75` | 2,510.00 USD | 78,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.80` | 4,710,000.00 USD | 4,710,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 7,800.00 USD | 76,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.90` | 6,620,000.00 USD | 6,620,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.95` | 1,200.00 USD | 68,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.00` | 2,960,000.00 USD | 2,960,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.05` | 67,240.00 USD | 67,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `96.10` | 4,490,000.00 USD | 4,490,000.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.15` | 8,070.00 USD | 44,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.20` | 1,350,000.00 USD | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.25` | 20,540.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `96.30` | 1,030,000.00 USD | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.35` | 28,630.00 USD | 93,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `96.40` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.40` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.45` | 1,970.00 USD | 95,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `96.50` | 58,320.00 USD | 58,320.00 USD | 0.00 USD | 58,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `96.50` | 116,630.00 USD | 116,630.00 USD | 0.00 USD | 58,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.55` | 64,410.00 USD | 159,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `96.60` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.65` | 6,280.00 USD | 165,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `96.70` | 377,010.00 USD | 377,010.00 USD | 181,530.00 USD | 78,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.80` | 10,930,000.00 USD | 10,930,000.00 USD | 53,180.00 USD | 859,230.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `96.90` | 5,500,000.00 USD | 5,500,000.00 USD | 360,820.00 USD | 1,590,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.95` | 2,540.00 USD | 168,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.00` | 13,240,000.00 USD | 13,240,000.00 USD | 1,310,000.00 USD | 522,440.00 USD | 474,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.10` | 10,290,000.00 USD | 10,290,000.00 USD | 306,680.00 USD | 118,320.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.15` | 8,870.00 USD | 177,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.20` | 18,840,000.00 USD | 18,840,000.00 USD | 379,310.00 USD | 3,490,000.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.25` | 3,880.00 USD | 181,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `97.30` | 25,270,000.00 USD | 25,270,000.00 USD | 6,280,000.00 USD | 4,520,000.00 USD | 4,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.40` | 23,680,000.00 USD | 23,680,000.00 USD | 845,630.00 USD | 1,490,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.45` | 26,710.00 USD | 207,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `97.50` | 43,790,000.00 USD | 43,790,000.00 USD | 7,020,000.00 USD | 5,750,000.00 USD | 5,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.55` | 129,410.00 USD | 337,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.60` | 37,290,000.00 USD | 37,290,000.00 USD | 5,300,000.00 USD | 1,610,000.00 USD | 6,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.65` | 150.38 USD | 337,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `97.70` | 60,750,000.00 USD | 60,750,000.00 USD | 7,740,000.00 USD | 3,900,000.00 USD | 5,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.75` | 9,530.00 USD | 347,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.80` | 47,110,000.00 USD | 47,110,000.00 USD | 5,310,000.00 USD | 548,540.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.85` | 5,760.00 USD | 352,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `97.90` | 91,020,000.00 USD | 91,020,000.00 USD | 11,920,000.00 USD | 8,420,000.00 USD | 9,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.95` | 145.95 USD | 352,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.00` | 58,370,000.00 USD | 58,370,000.00 USD | 6,080,000.00 USD | 777,550.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.05` | 5,090.00 USD | 358,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.10` | 119,350,000.00 USD | 119,350,000.00 USD | 9,820,000.00 USD | 7,490,000.00 USD | 11,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.15` | 4,170.00 USD | 362,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.20` | 68,070,000.00 USD | 68,070,000.00 USD | 4,150,000.00 USD | 2,830,000.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.25` | 3,370.00 USD | 365,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.30` | 127,980,000.00 USD | 127,980,000.00 USD | 43,030.00 USD | 4,510,000.00 USD | 4,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.40` | 77,700,000.00 USD | 77,700,000.00 USD | 2,560,000.00 USD | 310,490.00 USD | 6,760,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.45` | 30,920.00 USD | 396,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.50` | 129,260,000.00 USD | 129,260,000.00 USD | 1,040,000.00 USD | 238,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 103,500.00 USD | 500,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.60` | 78,560,000.00 USD | 78,560,000.00 USD | 52,360.00 USD | 804,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.65` | 7,240.00 USD | 507,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.75` | 21,990.00 USD | 529,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.80` | 78,580,000.00 USD | 78,580,000.00 USD | 0.00 USD | 7,070.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.85` | 47,060.00 USD | 576,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.95` | 367,580.00 USD | 943,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.00` | 78,890,000.00 USD | 78,890,000.00 USD | 0.00 USD | 305,090.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 77,860.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.15` | 7,810.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.20` | 82,480,000.00 USD | 82,480,000.00 USD | 0.00 USD | 0.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.25` | 1,440,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.30` | 129,280,000.00 USD | 129,280,000.00 USD | 0.00 USD | 0.00 USD | 19,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.35` | 70,900.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.40` | 85,830,000.00 USD | 85,830,000.00 USD | 2,840,000.00 USD | 0.00 USD | 513,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.45` | 33,870.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.50` | 131,520,000.00 USD | 131,520,000.00 USD | 2,240,000.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.55` | 228,670.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.60` | 96,080,000.00 USD | 96,080,000.00 USD | 1,370,000.00 USD | 4,730,000.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.65` | 56,710.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.70` | 133,530,000.00 USD | 133,530,000.00 USD | 0.00 USD | 2,000,000.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.75` | 12,030.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.80` | 106,250,000.00 USD | 106,250,000.00 USD | 2,250,000.00 USD | 2,620,000.00 USD | 5,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.90` | 140,690,000.00 USD | 140,690,000.00 USD | 2,860,000.00 USD | 1,110,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.00` | 111,730,000.00 USD | 111,730,000.00 USD | 2,080,000.00 USD | 1,770,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 446.22 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.10` | 144,080,000.00 USD | 144,080,000.00 USD | 48,160.00 USD | 477,660.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.15` | 5,900.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.20` | 112,580,000.00 USD | 112,580,000.00 USD | 16,830.00 USD | 832,940.00 USD | 243.12 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.25` | 13,960.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.30` | 146,930,000.00 USD | 146,930,000.00 USD | 883,050.00 USD | 855,480.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.35` | 19,540.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.40` | 116,200,000.00 USD | 116,200,000.00 USD | 349,430.00 USD | 629,010.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.50` | 153,870,000.00 USD | 153,870,000.00 USD | 2,500,000.00 USD | 128,740.00 USD | 4,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.60` | 125,530,000.00 USD | 125,530,000.00 USD | 1,990,000.00 USD | 1,180,000.00 USD | 6,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.70` | 155,230,000.00 USD | 155,230,000.00 USD | 133,340.00 USD | 1,230,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.75` | 12,140.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.80` | 129,610,000.00 USD | 129,610,000.00 USD | 1,500,000.00 USD | 1,490,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.85` | 10,250.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.90` | 167,060,000.00 USD | 167,060,000.00 USD | 3,450,000.00 USD | 3,210,000.00 USD | 5,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 19,560.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.00` | 140,470,000.00 USD | 140,470,000.00 USD | 7,780,000.00 USD | 2,250,000.00 USD | 834,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.05` | 8,440.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.10` | 176,260,000.00 USD | 176,260,000.00 USD | 2,930,000.00 USD | 3,930,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.15` | 438.99 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.20` | 156,290,000.00 USD | 156,290,000.00 USD | 5,170,000.00 USD | 6,570,000.00 USD | 4,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.30` | 194,270,000.00 USD | 194,270,000.00 USD | 7,310,000.00 USD | 3,160,000.00 USD | 7,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.40` | 164,900,000.00 USD | 164,900,000.00 USD | 3,390,000.00 USD | 1,950,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 876.53 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.50` | 208,800,000.00 USD | 208,800,000.00 USD | 2,950,000.00 USD | 0.00 USD | 11,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.55` | 814.43 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.60` | 184,440,000.00 USD | 184,440,000.00 USD | 5,190,000.00 USD | 2,550,000.00 USD | 11,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 1,820.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.70` | 218,140,000.00 USD | 218,140,000.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.75` | 59,180.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.80` | 191,520,000.00 USD | 191,520,000.00 USD | 483,810.00 USD | 381,190.00 USD | 6,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.90` | 226,150,000.00 USD | 226,150,000.00 USD | 3,710,000.00 USD | 503,680.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.00` | 195,910,000.00 USD | 195,910,000.00 USD | 2,230,000.00 USD | 873,740.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 4,690.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.10` | 230,790,000.00 USD | 230,790,000.00 USD | 1,470,000.00 USD | 0.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.20` | 202,750,000.00 USD | 202,750,000.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.30` | 236,840,000.00 USD | 236,840,000.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.40` | 207,320,000.00 USD | 207,320,000.00 USD | 1,430,000.00 USD | 579,100.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.50` | 240,490,000.00 USD | 240,490,000.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.55` | 8,080.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.60` | 209,970,000.00 USD | 209,970,000.00 USD | 978,360.00 USD | 625,050.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.70` | 241,270,000.00 USD | 241,270,000.00 USD | 766,460.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.75` | 182.90 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.80` | 214,430,000.00 USD | 214,430,000.00 USD | 1,430,000.00 USD | 1,920,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.85` | 9,640.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.90` | 262,550,000.00 USD | 262,550,000.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 3,080.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.00` | 219,690,000.00 USD | 219,690,000.00 USD | 3,120,000.00 USD | 1,640,000.00 USD | 498,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 4,520.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.10` | 268,760,000.00 USD | 268,760,000.00 USD | 4,750,000.00 USD | 114,550.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.15` | 323.89 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.20` | 223,420,000.00 USD | 223,420,000.00 USD | 585,300.00 USD | 1,320,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.30` | 286,330,000.00 USD | 286,330,000.00 USD | 17,020,000.00 USD | 133,780.00 USD | 417,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.35` | 517,280.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.40` | 230,450,000.00 USD | 230,450,000.00 USD | 3,460,000.00 USD | 1,900,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.50` | 308,740,000.00 USD | 308,740,000.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.55` | 8,500.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 243,190,000.00 USD | 243,190,000.00 USD | 4,260,000.00 USD | 1,580,000.00 USD | 6,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.70` | 320,960,000.00 USD | 320,960,000.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 29,780.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.80` | 252,600,000.00 USD | 252,600,000.00 USD | 3,210,000.00 USD | 2,770,000.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 38,270.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.90` | 338,990,000.00 USD | 338,990,000.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.00` | 262,160,000.00 USD | 262,160,000.00 USD | 3,550,000.00 USD | 2,790,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 545.22 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.10` | 367,720,000.00 USD | 367,720,000.00 USD | 11,570,000.00 USD | 8,150,000.00 USD | 9,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.15` | 10,270.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.20` | 267,970,000.00 USD | 267,970,000.00 USD | 2,080,000.00 USD | 1,900,000.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.25` | 37,460.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.30` | 389,100,000.00 USD | 389,100,000.00 USD | 7,320,000.00 USD | 6,370,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.35` | 1,540.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.40` | 274,960,000.00 USD | 274,960,000.00 USD | 3,060,000.00 USD | 1,930,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 12,140.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.50` | 401,100,000.00 USD | 401,100,000.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.55` | 895.99 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 280,360,000.00 USD | 280,360,000.00 USD | 1,660,000.00 USD | 1,070,000.00 USD | 2,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 630,930.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.70` | 421,100,000.00 USD | 421,100,000.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.75` | 849.52 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.80` | 285,370,000.00 USD | 285,370,000.00 USD | 1,460,000.00 USD | 972,490.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.85` | 7,560.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.90` | 441,710,000.00 USD | 441,710,000.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 412.45 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.00` | 287,300,000.00 USD | 287,300,000.00 USD | 708,730.00 USD | 483,120.00 USD | 746,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.10` | 455,390,000.00 USD | 455,390,000.00 USD | 5,580,000.00 USD | 5,260,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.20` | 288,560,000.00 USD | 288,560,000.00 USD | 237,100.00 USD | 4,110.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 7,140.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.30` | 461,090,000.00 USD | 461,090,000.00 USD | 2,740,000.00 USD | 2,540,000.00 USD | 428,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.35` | 110,930.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.40` | 288,730,000.00 USD | 288,730,000.00 USD | 84,970.00 USD | 88,270.00 USD | 769.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.50` | 480,610,000.00 USD | 480,610,000.00 USD | 5,600,000.00 USD | 6,170,000.00 USD | 7,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.55` | 4,370.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 289,310,000.00 USD | 289,310,000.00 USD | 178,510.00 USD | 263,160.00 USD | 135,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.65` | 108.82 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.70` | 494,770,000.00 USD | 494,770,000.00 USD | 4,560,000.00 USD | 4,340,000.00 USD | 5,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.80` | 290,060,000.00 USD | 290,060,000.00 USD | 132,310.00 USD | 591,910.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.85` | 10,550.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.90` | 504,720,000.00 USD | 504,720,000.00 USD | 3,720,000.00 USD | 1,880,000.00 USD | 4,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 2,740.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.00` | 291,180,000.00 USD | 291,180,000.00 USD | 377,210.00 USD | 523,130.00 USD | 226,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 103.93 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.10` | 517,870,000.00 USD | 517,870,000.00 USD | 6,580,000.00 USD | 3,600,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.15` | 3,250.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.20` | 292,510,000.00 USD | 292,510,000.00 USD | 616,110.00 USD | 345,000.00 USD | 367,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.30` | 528,540,000.00 USD | 528,540,000.00 USD | 4,780,000.00 USD | 3,220,000.00 USD | 2,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.40` | 293,370,000.00 USD | 293,370,000.00 USD | 288,180.00 USD | 356,490.00 USD | 207,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 696.18 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.50` | 534,130,000.00 USD | 534,130,000.00 USD | 1,700,000.00 USD | 2,010,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.60` | 295,480,000.00 USD | 295,480,000.00 USD | 803,010.00 USD | 365,650.00 USD | 949,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.65` | 548.18 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.70` | 543,260,000.00 USD | 543,260,000.00 USD | 2,280,000.00 USD | 2,670,000.00 USD | 4,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.80` | 297,090,000.00 USD | 297,090,000.00 USD | 565,520.00 USD | 117,240.00 USD | 924,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 542,740.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.90` | 549,040,000.00 USD | 549,040,000.00 USD | 1,190,000.00 USD | 1,120,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.95` | 291.97 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.00` | 297,760,000.00 USD | 297,760,000.00 USD | 199,140.00 USD | 184,400.00 USD | 288,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 12,400.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.10` | 552,440,000.00 USD | 552,440,000.00 USD | 1,630,000.00 USD | 508,540.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.15` | 35,540.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.20` | 298,010,000.00 USD | 298,010,000.00 USD | 0.00 USD | 0.00 USD | 242,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.30` | 552,600,000.00 USD | 552,600,000.00 USD | 0.00 USD | 156,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.35` | 212,780.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.45` | 120,310.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.50` | 553,580,000.00 USD | 553,580,000.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.55` | 2,640.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.65` | 1,560.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.70` | 554,550,000.00 USD | 554,550,000.00 USD | 523,660.00 USD | 10,400.00 USD | 432,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.75` | 5,840.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.85` | 392,910.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.90` | 554,720,000.00 USD | 554,720,000.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.10` | 555,840,000.00 USD | 555,840,000.00 USD | 496,690.00 USD | 612,160.00 USD | 7,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `108.20` | 298,010,000.00 USD | 298,010,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.30` | 558,130,000.00 USD | 558,130,000.00 USD | 980,650.00 USD | 697,770.00 USD | 612,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,690.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.40` | 298,040,000.00 USD | 298,040,000.00 USD | 29,460.00 USD | 1,950.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.45` | 108,940.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.50` | 559,580,000.00 USD | 559,580,000.00 USD | 883,300.00 USD | 336,620.00 USD | 230,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.55` | 117.23 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.60` | 298,910,000.00 USD | 298,910,000.00 USD | 275,520.00 USD | 173,760.00 USD | 413,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 64,720.00 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.70` | 561,820,000.00 USD | 561,820,000.00 USD | 578,660.00 USD | 655,690.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.75` | 6,370.00 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.80` | 299,130,000.00 USD | 299,130,000.00 USD | 8,600.00 USD | 2,360.00 USD | 217,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 3,230.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.90` | 563,870,000.00 USD | 563,870,000.00 USD | 646,020.00 USD | 644,300.00 USD | 754,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.95` | 955.49 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.00` | 299,400,000.00 USD | 299,400,000.00 USD | 166,240.00 USD | 99,310.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.05` | 121,510.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.10` | 564,950,000.00 USD | 564,950,000.00 USD | 434,330.00 USD | 185,250.00 USD | 464,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.15` | 22,380.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.20` | 299,770,000.00 USD | 299,770,000.00 USD | 12,630.00 USD | 93,010.00 USD | 265,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.25` | 1,170.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.30` | 566,120,000.00 USD | 566,120,000.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.35` | 4,600.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.40` | 299,910,000.00 USD | 299,910,000.00 USD | 123,410.00 USD | 7,590.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.45` | 103,160.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.50` | 566,360,000.00 USD | 566,360,000.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.55` | 567.47 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.60` | 300,810,000.00 USD | 300,810,000.00 USD | 434,540.00 USD | 155,520.00 USD | 313,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.65` | 53,730.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.70` | 567,540,000.00 USD | 567,540,000.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.80` | 301,920,000.00 USD | 301,920,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.85` | 1,020.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.90` | 569,340,000.00 USD | 569,340,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.95` | 794.94 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.00` | 303,270,000.00 USD | 303,270,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.10` | 571,710,000.00 USD | 571,710,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.15` | 194.97 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.20` | 304,600,000.00 USD | 304,600,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.25` | 218.29 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.30` | 573,790,000.00 USD | 573,790,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.35` | 143,230.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.40` | 305,950,000.00 USD | 305,950,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.45` | 16,940.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.50` | 574,270,000.00 USD | 574,270,000.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.55` | 203.41 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.60` | 306,410,000.00 USD | 306,410,000.00 USD | 110,850.00 USD | 104,840.00 USD | 240,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.70` | 576,470,000.00 USD | 576,470,000.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.75` | 3,330.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.80` | 307,090,000.00 USD | 307,090,000.00 USD | 159,320.00 USD | 287,810.00 USD | 237,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.85` | 103.09 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.90` | 578,920,000.00 USD | 578,920,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.95` | 660.15 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `111.00` | 307,300,000.00 USD | 307,300,000.00 USD | 106,320.00 USD | 101,660.00 USD | 319.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.10` | 581,300,000.00 USD | 581,300,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.30` | 583,210,000.00 USD | 583,210,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.35` | 259,330.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.50` | 585,710,000.00 USD | 585,710,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.65` | 3,070.00 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.70` | 586,860,000.00 USD | 586,860,000.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.75` | 339.72 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.90` | 588,630,000.00 USD | 588,630,000.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.95` | 2,020.00 USD | 6,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.05` | 626.36 USD | 6,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.10` | 590,260,000.00 USD | 590,260,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.30` | 592,670,000.00 USD | 592,670,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.50` | 593,980,000.00 USD | 593,980,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.55` | 844.13 USD | 6,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.70` | 594,500,000.00 USD | 594,500,000.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.75` | 110.50 USD | 6,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 3,540.00 USD | 6,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.90` | 595,990,000.00 USD | 595,990,000.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.05` | 406.98 USD | 6,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.10` | 597,390,000.00 USD | 597,390,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.15` | 9,560.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 24,630.00 USD | 6,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.30` | 597,660,000.00 USD | 597,660,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.45` | 102,110.00 USD | 6,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.50` | 597,720,000.00 USD | 597,720,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.65` | 3,220.00 USD | 6,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.70` | 598,110,000.00 USD | 598,110,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.90` | 598,170,000.00 USD | 598,170,000.00 USD | 52,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 6,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 33,960.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `114.10` | 598,220,000.00 USD | 598,220,000.00 USD | 3,370.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.15` | 1,960.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,150.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `114.30` | 598,540,000.00 USD | 598,540,000.00 USD | 101,820.00 USD | 211,850.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `114.40` | 598,870,000.00 USD | 598,870,000.00 USD | 132,060.00 USD | 82,030.00 USD | 113,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.45` | 160.23 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.55` | 431.85 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 7,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 1,100.00 USD | 7,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.25` | 18,240.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 893,930.00 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 46,710.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.95` | 460,240.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.15` | 180.03 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 14,050.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,780.00 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.75` | 31,740.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.95` | 633.87 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 24,630.00 USD | 9,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 4,710,000.00 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.45` | 809.23 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 2,130.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 12,060.00 USD | 13,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.35` | 828.45 USD | 13,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 30,970.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 1,110.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.85` | 950.80 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 240.88 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 85,100.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.45` | 115.87 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 174.54 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.65` | 6,170.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 261.06 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 10,790.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.05` | 94,210.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 4,150.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.35` | 145.62 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 1,940.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.05` | 15,300.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.25` | 414.68 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.35` | 3,230.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 5,940.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.65` | 16,580.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 12,780.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 111,000.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 169.79 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 2,200.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 90,040.00 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.85` | 896,320.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.95` | 3,900.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.05` | 13,490,000.00 USD | 28,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.15` | 126.84 USD | 28,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.25` | 182,940.00 USD | 28,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,330.00 USD | 28,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 3,250.00 USD | 28,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.55` | 3,430.00 USD | 28,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 28,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 17,600.00 USD | 28,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.45` | 3,080.00 USD | 28,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 28,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 5,330.00 USD | 28,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 14,160.00 USD | 28,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 3,760.00 USD | 28,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 1,930.00 USD | 28,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.85` | 6,200.00 USD | 28,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 2,030.00 USD | 28,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 28,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 470.54 USD | 28,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 305.77 USD | 28,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 30,830.00 USD | 28,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 1,710.00 USD | 28,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.95` | 9,460.00 USD | 28,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 2,030.00 USD | 28,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 16,190.00 USD | 28,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.55` | 2,260.00 USD | 28,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 28,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 43,470.00 USD | 29,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 29,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,200.00 USD | 29,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 4,850,000.00 USD | 33,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.55` | 3,140.00 USD | 33,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 4,300.00 USD | 34,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 34,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 40,920.00 USD | 34,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.95` | 697,060.00 USD | 34,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.05` | 47,810.00 USD | 34,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 41,090.00 USD | 34,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 56,180.00 USD | 34,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 36,480.00 USD | 34,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 13,670.00 USD | 34,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.95` | 42,200.00 USD | 34,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.25` | 145.88 USD | 34,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.55` | 3,020.00 USD | 34,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.65` | 1,310.00 USD | 35,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 503,820.00 USD | 35,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 35,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 35,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 2,410.00 USD | 35,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 6,790.00 USD | 35,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 5,820.00 USD | 35,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 325.09 USD | 35,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.35` | 4,630.00 USD | 35,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.45` | 8,530.00 USD | 35,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 196.17 USD | 35,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 740.19 USD | 35,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 49,280.00 USD | 35,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 96,780.00 USD | 35,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 8,440.00 USD | 35,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.35` | 3,640.00 USD | 35,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.45` | 209,480.00 USD | 35,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.55` | 186.97 USD | 35,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 35,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 503.65 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 142.09 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 11,590.00 USD | 36,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.55` | 48,390.00 USD | 36,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.65` | 1,350,000.00 USD | 37,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 37,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 504.37 USD | 37,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.35` | 589.03 USD | 37,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 37,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 37,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 37,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.35` | 317.28 USD | 37,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.65` | 306.96 USD | 37,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.75` | 14,810.00 USD | 37,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 1,270.00 USD | 37,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 86,640.00 USD | 37,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 12,480.00 USD | 37,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.35` | 155,690.00 USD | 37,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 207,340.00 USD | 37,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,080,000.00 USD | 40,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.05` | 2,750.00 USD | 40,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 2,230.00 USD | 40,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.25` | 492.94 USD | 40,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.35` | 253.62 USD | 40,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.45` | 5,190,000.00 USD | 45,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.65` | 622.84 USD | 45,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.85` | 770.57 USD | 45,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 116.24 USD | 45,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 71,960.00 USD | 45,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 7,330.00 USD | 45,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,940.00 USD | 45,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 335.70 USD | 45,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.15` | 1,070,000.00 USD | 46,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 210.61 USD | 46,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 268,700.00 USD | 46,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 236.39 USD | 46,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 18,490.00 USD | 46,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 103.48 USD | 46,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.15` | 131,260.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.25` | 112.38 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 151.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.65` | 847,490.00 USD | 47,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 368.30 USD | 47,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 2,980.00 USD | 47,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 22,260.00 USD | 47,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.75` | 143.75 USD | 47,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 47,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.15` | 13,330.00 USD | 47,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 1,240.00 USD | 47,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 2,250.00 USD | 47,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.35` | 5,110.00 USD | 47,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.65` | 85,880.00 USD | 47,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 5,850.00 USD | 47,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.95` | 820.24 USD | 47,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 88,760.00 USD | 47,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 2,770.00 USD | 47,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,330.00 USD | 47,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,860.00 USD | 48,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.75` | 2,110.00 USD | 48,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 861,660.00 USD | 49,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 1,120.00 USD | 49,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 49,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 49,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 78,420.00 USD | 49,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 6,420.00 USD | 49,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 237.72 USD | 49,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 300.14 USD | 49,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 444,550.00 USD | 49,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.25` | 444,750.00 USD | 50,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.35` | 5,640.00 USD | 50,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 163.29 USD | 50,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 344,780.00 USD | 50,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.65` | 377.57 USD | 50,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 92,000.00 USD | 50,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.95` | 1,460.00 USD | 50,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.05` | 1,380,000.00 USD | 52,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.45` | 1,130,000.00 USD | 53,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 53,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 53,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.85` | 17,290.00 USD | 53,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 178.44 USD | 53,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 9,340.00 USD | 53,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.45` | 46,810.00 USD | 53,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 2,540.00 USD | 53,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.35` | 4,540.00 USD | 53,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 53,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,920.00 USD | 53,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.15` | 4,610,000.00 USD | 57,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 3,000.00 USD | 57,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 286,550.00 USD | 58,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 3,150.00 USD | 58,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.55` | 423,220.00 USD | 58,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.65` | 233.55 USD | 58,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 58,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.95` | 18,970.00 USD | 58,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 1,060.00 USD | 58,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 58,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.55` | 119,720.00 USD | 58,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 52,040.00 USD | 58,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.05` | 292.69 USD | 58,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 362.25 USD | 58,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 58,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.35` | 308,700.00 USD | 59,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 59,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.75` | 43,600.00 USD | 59,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.85` | 1,240.00 USD | 59,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.95` | 27,160.00 USD | 59,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.25` | 1,240.00 USD | 59,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.35` | 155,350.00 USD | 59,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 233,590.00 USD | 59,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.85` | 325.73 USD | 59,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.95` | 7,800.00 USD | 59,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.15` | 21,660.00 USD | 59,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 3,320.00 USD | 59,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 1,770.00 USD | 59,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.55` | 2,000.00 USD | 59,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.85` | 113,870.00 USD | 59,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.95` | 296.64 USD | 59,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 49,270.00 USD | 59,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.25` | 190.27 USD | 59,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.45` | 101,740.00 USD | 59,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 59,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 92,600.00 USD | 60,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.85` | 119.97 USD | 60,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.95` | 312.74 USD | 60,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.65` | 84,520.00 USD | 60,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.75` | 125.41 USD | 60,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 82,370.00 USD | 60,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.35` | 3,080.00 USD | 60,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.55` | 39,920.00 USD | 60,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 2,080.00 USD | 60,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.75` | 2,090.00 USD | 60,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.85` | 300.52 USD | 60,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 684,060.00 USD | 60,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 2,200.00 USD | 60,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.65` | 782.37 USD | 60,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.75` | 1,630.00 USD | 60,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.85` | 164,050.00 USD | 61,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 61,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 20,430.00 USD | 61,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 410.34 USD | 61,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 144,940.00 USD | 61,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.15` | 119.99 USD | 61,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.55` | 325,100.00 USD | 61,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.95` | 666.47 USD | 61,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.45` | 177,370.00 USD | 61,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.55` | 2,550.00 USD | 61,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 61,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.45` | 17,820.00 USD | 61,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.75` | 207,840.00 USD | 62,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 62,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.55` | 72,840.00 USD | 62,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 62,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.65` | 833.25 USD | 62,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.15` | 27,060.00 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.55` | 3,460.00 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 1,890.00 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.95` | 122.60 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 62,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 62,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.35` | 130,080.00 USD | 62,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.75` | 16,130.00 USD | 62,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.35` | 153.32 USD | 62,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.55` | 325.75 USD | 62,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 62,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.55` | 300.21 USD | 62,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.65` | 42,930.00 USD | 62,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.75` | 2,720.00 USD | 62,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.35` | 38,100,000.00 USD | 100,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,730.00 USD | 100,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.25` | 693.00 USD | 100,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 100,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.75` | 1,280.00 USD | 100,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 100,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.05` | 104,430.00 USD | 100,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.15` | 23,910.00 USD | 101,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,010.00 USD | 101,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 101,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.55` | 110,740.00 USD | 101,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 101,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.35` | 508.52 USD | 101,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.55` | 140,440.00 USD | 101,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 263.62 USD | 101,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.85` | 1,020,000.00 USD | 102,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 102,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.85` | 24,930.00 USD | 102,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 90,750.00 USD | 102,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.25` | 6,330,000.00 USD | 109,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.45` | 356,900.00 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.55` | 267,820.00 USD | 109,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.75` | 770.41 USD | 109,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.35` | 473.48 USD | 109,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.55` | 116,010.00 USD | 109,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.65` | 1,350.00 USD | 109,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.75` | 154.59 USD | 109,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.45` | 2,080.00 USD | 109,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 3,970.00 USD | 109,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.75` | 146.41 USD | 109,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.15` | 126,810.00 USD | 110,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 18,410.00 USD | 110,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 110,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.85` | 618.03 USD | 110,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.45` | 64,210.00 USD | 110,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.15` | 7,630.00 USD | 110,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 3,070.00 USD | 110,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.15` | 251.80 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.55` | 983.42 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 137.38 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.75` | 247.05 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.45` | 2,310.00 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.35` | 232.31 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.75` | 2,110.00 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.05` | 19,290.00 USD | 110,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.45` | 282,600.00 USD | 110,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 9,980.00 USD | 110,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 110,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.05` | 5,360.00 USD | 110,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.15` | 10,850.00 USD | 110,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 456.09 USD | 110,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 110,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.05` | 380,100.00 USD | 111,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 1,330.00 USD | 111,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.25` | 117.95 USD | 111,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 124,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 322.48 USD | 124,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.25` | 140,840,000.00 USD | 0.00 USD | 577.50 USD | `-79.97%` | `30.00` |
| `Live` | `Long` | `19.45` | 140,840,000.00 USD | 0.00 USD | 2,520.00 USD | `-79.76%` | `129.70` |
| `Live` | `Long` | `19.85` | 140,840,000.00 USD | 0.00 USD | 20,250.00 USD | `-79.35%` | `1,020.00` |
| `Live` | `Long` | `20.55` | 140,820,000.00 USD | 0.00 USD | 17,640.00 USD | `-78.62%` | `858.31` |
| `Live` | `Long` | `20.65` | 140,800,000.00 USD | 0.00 USD | 516.25 USD | `-78.51%` | `25.00` |
| `Live` | `Long` | `21.05` | 140,800,000.00 USD | 0.00 USD | 759,600.00 USD | `-78.10%` | `36,085.73` |
| `Live` | `Long` | `21.15` | 140,040,000.00 USD | 0.00 USD | 401.85 USD | `-77.99%` | `19.00` |
| `Live` | `Long` | `21.35` | 140,040,000.00 USD | 0.00 USD | 1,760.00 USD | `-77.78%` | `82.56` |
| `Live` | `Long` | `21.45` | 140,040,000.00 USD | 0.00 USD | 4,770.00 USD | `-77.68%` | `222.54` |
| `Live` | `Long` | `21.65` | 140,030,000.00 USD | 0.00 USD | 1,060.00 USD | `-77.47%` | `48.84` |
| `Live` | `Long` | `21.75` | 140,030,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.37%` | `212.70` |
| `Live` | `Long` | `21.85` | 140,020,000.00 USD | 0.00 USD | 474.58 USD | `-77.26%` | `21.72` |
| `Live` | `Long` | `22.05` | 140,020,000.00 USD | 0.00 USD | 109.15 USD | `-77.06%` | `4.95` |
| `Live` | `Long` | `22.15` | 140,020,000.00 USD | 0.00 USD | 297.92 USD | `-76.95%` | `13.45` |
| `Live` | `Long` | `22.25` | 140,020,000.00 USD | 0.00 USD | 9,940.00 USD | `-76.85%` | `446.72` |
| `Live` | `Long` | `22.45` | 140,010,000.00 USD | 0.00 USD | 8,280.00 USD | `-76.64%` | `369.00` |
| `Live` | `Long` | `22.55` | 140,010,000.00 USD | 0.00 USD | 1,670.00 USD | `-76.54%` | `74.05` |
| `Live` | `Long` | `22.95` | 140,000,000.00 USD | 0.00 USD | 1,440.00 USD | `-76.12%` | `62.65` |
| `Live` | `Long` | `23.25` | 140,000,000.00 USD | 0.00 USD | 1,160.00 USD | `-75.81%` | `50.00` |
| `Live` | `Long` | `23.45` | 140,000,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.60%` | `58.86` |
| `Live` | `Long` | `23.75` | 140,000,000.00 USD | 0.00 USD | 122.55 USD | `-75.29%` | `5.16` |
| `Live` | `Long` | `23.95` | 140,000,000.00 USD | 0.00 USD | 17,960.00 USD | `-75.08%` | `750.00` |
| `Live` | `Long` | `24.05` | 139,980,000.00 USD | 0.00 USD | 1,750.00 USD | `-74.98%` | `72.56` |
| `Live` | `Long` | `24.15` | 139,980,000.00 USD | 0.00 USD | 1,160.00 USD | `-74.87%` | `48.08` |
| `Live` | `Long` | `24.45` | 139,980,000.00 USD | 0.00 USD | 1,500.00 USD | `-74.56%` | `61.19` |
| `Live` | `Long` | `24.65` | 139,980,000.00 USD | 0.00 USD | 147,310.00 USD | `-74.35%` | `5,975.88` |
| `Live` | `Long` | `24.75` | 139,830,000.00 USD | 0.00 USD | 192.31 USD | `-74.25%` | `7.77` |
| `Live` | `Long` | `24.95` | 139,830,000.00 USD | 0.00 USD | 394.21 USD | `-74.04%` | `15.80` |
| `Live` | `Long` | `25.05` | 139,830,000.00 USD | 0.00 USD | 272,090.00 USD | `-73.93%` | `10,861.76` |
| `Live` | `Long` | `25.15` | 139,560,000.00 USD | 0.00 USD | 2,010.00 USD | `-73.83%` | `80.00` |
| `Live` | `Long` | `25.35` | 139,560,000.00 USD | 0.00 USD | 2,400.00 USD | `-73.62%` | `94.84` |
| `Live` | `Long` | `25.45` | 139,550,000.00 USD | 0.00 USD | 106.64 USD | `-73.52%` | `4.19` |
| `Live` | `Long` | `25.65` | 139,550,000.00 USD | 0.00 USD | 37,670.00 USD | `-73.31%` | `1,468.70` |
| `Live` | `Long` | `25.75` | 139,520,000.00 USD | 0.00 USD | 10,090.00 USD | `-73.21%` | `391.91` |
| `Live` | `Long` | `25.95` | 139,510,000.00 USD | 0.00 USD | 2,930.00 USD | `-73.00%` | `113.00` |
| `Live` | `Long` | `26.25` | 139,500,000.00 USD | 0.00 USD | 136.24 USD | `-72.69%` | `5.19` |
| `Live` | `Long` | `26.45` | 139,500,000.00 USD | 0.00 USD | 476.89 USD | `-72.48%` | `18.03` |
| `Live` | `Long` | `26.65` | 139,500,000.00 USD | 0.00 USD | 102.60 USD | `-72.27%` | `3.85` |
| `Live` | `Long` | `26.75` | 139,500,000.00 USD | 0.00 USD | 2,280.00 USD | `-72.17%` | `85.17` |
| `Live` | `Long` | `27.05` | 139,500,000.00 USD | 0.00 USD | 268.34 USD | `-71.85%` | `9.92` |
| `Live` | `Long` | `27.15` | 139,500,000.00 USD | 0.00 USD | 149.87 USD | `-71.75%` | `5.52` |
| `Live` | `Long` | `27.35` | 139,500,000.00 USD | 0.00 USD | 332.30 USD | `-71.54%` | `12.15` |
| `Live` | `Long` | `27.45` | 139,500,000.00 USD | 0.00 USD | 82,350.00 USD | `-71.44%` | `3,000.00` |
| `Live` | `Long` | `27.55` | 139,420,000.00 USD | 0.00 USD | 13,780.00 USD | `-71.33%` | `500.00` |
| `Live` | `Long` | `27.65` | 139,400,000.00 USD | 0.00 USD | 168.66 USD | `-71.23%` | `6.10` |
| `Live` | `Long` | `27.85` | 139,400,000.00 USD | 0.00 USD | 412.18 USD | `-71.02%` | `14.80` |
| `Live` | `Long` | `28.05` | 139,400,000.00 USD | 0.00 USD | 3,490.00 USD | `-70.81%` | `124.36` |
| `Live` | `Long` | `28.35` | 139,400,000.00 USD | 0.00 USD | 6,200.00 USD | `-70.50%` | `218.55` |
| `Live` | `Long` | `28.45` | 139,390,000.00 USD | 0.00 USD | 113.80 USD | `-70.40%` | `4.00` |
| `Live` | `Long` | `28.55` | 139,390,000.00 USD | 0.00 USD | 184.72 USD | `-70.29%` | `6.47` |
| `Live` | `Long` | `28.65` | 139,390,000.00 USD | 0.00 USD | 253.84 USD | `-70.19%` | `8.86` |
| `Live` | `Long` | `28.85` | 139,390,000.00 USD | 0.00 USD | 9,810.00 USD | `-69.98%` | `340.00` |
| `Live` | `Long` | `28.95` | 139,380,000.00 USD | 0.00 USD | 424.41 USD | `-69.88%` | `14.66` |
| `Live` | `Long` | `29.05` | 139,380,000.00 USD | 0.00 USD | 3,050.00 USD | `-69.77%` | `104.94` |
| `Live` | `Long` | `29.15` | 139,380,000.00 USD | 0.00 USD | 26,210.00 USD | `-69.67%` | `899.18` |
| `Live` | `Long` | `29.25` | 139,350,000.00 USD | 0.00 USD | 63,520.00 USD | `-69.56%` | `2,171.59` |
| `Live` | `Long` | `29.35` | 139,290,000.00 USD | 0.00 USD | 44,020.00 USD | `-69.46%` | `1,500.00` |
| `Live` | `Long` | `29.45` | 139,240,000.00 USD | 0.00 USD | 2,710.00 USD | `-69.36%` | `91.87` |
| `Live` | `Long` | `29.65` | 139,240,000.00 USD | 0.00 USD | 7,440.00 USD | `-69.15%` | `251.00` |
| `Live` | `Long` | `29.85` | 139,230,000.00 USD | 0.00 USD | 4,890.00 USD | `-68.94%` | `163.78` |
| `Live` | `Long` | `29.95` | 139,230,000.00 USD | 0.00 USD | 5,940.00 USD | `-68.84%` | `198.28` |
| `Live` | `Long` | `30.05` | 139,220,000.00 USD | 0.00 USD | 7,170.00 USD | `-68.73%` | `238.70` |
| `Live` | `Long` | `30.15` | 139,220,000.00 USD | 0.00 USD | 47,340.00 USD | `-68.63%` | `1,570.00` |
| `Live` | `Long` | `30.35` | 139,170,000.00 USD | 0.00 USD | 738.72 USD | `-68.42%` | `24.34` |
| `Live` | `Long` | `30.55` | 139,170,000.00 USD | 0.00 USD | 889.01 USD | `-68.21%` | `29.10` |
| `Live` | `Long` | `30.65` | 139,170,000.00 USD | 0.00 USD | 233.86 USD | `-68.11%` | `7.63` |
| `Live` | `Long` | `30.95` | 139,170,000.00 USD | 0.00 USD | 34,710.00 USD | `-67.80%` | `1,121.64` |
| `Live` | `Long` | `31.45` | 139,130,000.00 USD | 0.00 USD | 278.33 USD | `-67.28%` | `8.85` |
| `Live` | `Long` | `31.75` | 139,130,000.00 USD | 0.00 USD | 3,860.00 USD | `-66.96%` | `121.53` |
| `Live` | `Long` | `31.85` | 139,130,000.00 USD | 0.00 USD | 1,070.00 USD | `-66.86%` | `33.68` |
| `Live` | `Long` | `31.95` | 139,130,000.00 USD | 0.00 USD | 541,970.00 USD | `-66.75%` | `16,963.19` |
| `Live` | `Long` | `32.05` | 138,590,000.00 USD | 0.00 USD | 101.28 USD | `-66.65%` | `3.16` |
| `Live` | `Long` | `32.15` | 138,590,000.00 USD | 0.00 USD | 373.58 USD | `-66.55%` | `11.62` |
| `Live` | `Long` | `32.45` | 138,580,000.00 USD | 0.00 USD | 477.34 USD | `-66.23%` | `14.71` |
| `Live` | `Long` | `32.55` | 138,580,000.00 USD | 0.00 USD | 5,420.00 USD | `-66.13%` | `166.40` |
| `Live` | `Long` | `32.75` | 138,580,000.00 USD | 0.00 USD | 718.21 USD | `-65.92%` | `21.93` |
| `Live` | `Long` | `32.85` | 138,580,000.00 USD | 0.00 USD | 5,240.00 USD | `-65.82%` | `159.61` |
| `Live` | `Long` | `33.15` | 138,570,000.00 USD | 0.00 USD | 1,920.00 USD | `-65.51%` | `57.97` |
| `Live` | `Long` | `33.35` | 138,570,000.00 USD | 0.00 USD | 3,900.00 USD | `-65.30%` | `116.90` |
| `Live` | `Long` | `33.45` | 138,570,000.00 USD | 0.00 USD | 222.78 USD | `-65.19%` | `6.66` |
| `Live` | `Long` | `33.75` | 138,570,000.00 USD | 0.00 USD | 2,890.00 USD | `-64.88%` | `85.76` |
| `Live` | `Long` | `33.85` | 138,560,000.00 USD | 0.00 USD | 17,710.00 USD | `-64.78%` | `523.23` |
| `Live` | `Long` | `33.95` | 138,550,000.00 USD | 0.00 USD | 210.83 USD | `-64.67%` | `6.21` |
| `Live` | `Long` | `34.05` | 138,550,000.00 USD | 0.00 USD | 973.83 USD | `-64.57%` | `28.60` |
| `Live` | `Long` | `34.35` | 138,550,000.00 USD | 0.00 USD | 46,170.00 USD | `-64.26%` | `1,344.19` |
| `Live` | `Long` | `34.45` | 138,500,000.00 USD | 0.00 USD | 4,210.00 USD | `-64.15%` | `122.11` |
| `Live` | `Long` | `34.65` | 138,490,000.00 USD | 0.00 USD | 486.14 USD | `-63.95%` | `14.03` |
| `Live` | `Long` | `34.75` | 138,490,000.00 USD | 0.00 USD | 1,800.00 USD | `-63.84%` | `51.88` |
| `Live` | `Long` | `34.85` | 138,490,000.00 USD | 0.00 USD | 14,520.00 USD | `-63.74%` | `416.67` |
| `Live` | `Long` | `34.95` | 138,480,000.00 USD | 0.00 USD | 6,620,000.00 USD | `-63.63%` | `189,500.44` |
| `Live` | `Long` | `35.15` | 131,850,000.00 USD | 0.00 USD | 2,150.00 USD | `-63.43%` | `61.21` |
| `Live` | `Long` | `35.25` | 131,850,000.00 USD | 0.00 USD | 20,240.00 USD | `-63.32%` | `574.13` |
| `Live` | `Long` | `35.45` | 131,830,000.00 USD | 0.00 USD | 2,120.00 USD | `-63.11%` | `59.91` |
| `Live` | `Long` | `35.75` | 131,830,000.00 USD | 0.00 USD | 50,220.00 USD | `-62.80%` | `1,404.69` |
| `Live` | `Long` | `35.85` | 131,780,000.00 USD | 0.00 USD | 222.63 USD | `-62.70%` | `6.21` |
| `Live` | `Long` | `35.95` | 131,780,000.00 USD | 0.00 USD | 5,610.00 USD | `-62.59%` | `156.13` |
| `Live` | `Long` | `36.15` | 131,770,000.00 USD | 0.00 USD | 531.41 USD | `-62.38%` | `14.70` |
| `Live` | `Long` | `36.25` | 131,770,000.00 USD | 0.00 USD | 315.38 USD | `-62.28%` | `8.70` |
| `Live` | `Long` | `36.35` | 131,770,000.00 USD | 0.00 USD | 4,410.00 USD | `-62.18%` | `121.32` |
| `Live` | `Long` | `36.45` | 131,770,000.00 USD | 0.00 USD | 2,410.00 USD | `-62.07%` | `66.24` |
| `Live` | `Long` | `36.75` | 131,770,000.00 USD | 0.00 USD | 2,340.00 USD | `-61.76%` | `63.63` |
| `Live` | `Long` | `36.85` | 131,760,000.00 USD | 0.00 USD | 50,050.00 USD | `-61.66%` | `1,358.08` |
| `Live` | `Long` | `36.95` | 131,710,000.00 USD | 0.00 USD | 1,660.00 USD | `-61.55%` | `45.00` |
| `Live` | `Long` | `37.05` | 131,710,000.00 USD | 0.00 USD | 250.09 USD | `-61.45%` | `6.75` |
| `Live` | `Long` | `37.15` | 131,710,000.00 USD | 0.00 USD | 837,560.00 USD | `-61.34%` | `22,545.24` |
| `Live` | `Long` | `37.25` | 130,870,000.00 USD | 0.00 USD | 7,830.00 USD | `-61.24%` | `210.07` |
| `Live` | `Long` | `37.35` | 130,870,000.00 USD | 0.00 USD | 21,280.00 USD | `-61.14%` | `569.75` |
| `Live` | `Long` | `37.45` | 130,850,000.00 USD | 0.00 USD | 304,940.00 USD | `-61.03%` | `8,142.56` |
| `Live` | `Long` | `37.55` | 130,540,000.00 USD | 0.00 USD | 2,520.00 USD | `-60.93%` | `67.00` |
| `Live` | `Long` | `37.65` | 130,540,000.00 USD | 0.00 USD | 2,430.00 USD | `-60.82%` | `64.52` |
| `Live` | `Long` | `37.95` | 130,540,000.00 USD | 0.00 USD | 4,300.00 USD | `-60.51%` | `113.43` |
| `Live` | `Long` | `38.05` | 130,530,000.00 USD | 0.00 USD | 2,950.00 USD | `-60.41%` | `77.54` |
| `Live` | `Long` | `38.35` | 130,530,000.00 USD | 0.00 USD | 191,750.00 USD | `-60.10%` | `5,000.00` |
| `Live` | `Long` | `38.45` | 130,340,000.00 USD | 0.00 USD | 3,970,000.00 USD | `-59.99%` | `103,150.43` |
| `Live` | `Long` | `38.65` | 126,370,000.00 USD | 0.00 USD | 67,730.00 USD | `-59.78%` | `1,752.38` |
| `Live` | `Long` | `38.75` | 126,300,000.00 USD | 0.00 USD | 736.64 USD | `-59.68%` | `19.01` |
| `Live` | `Long` | `38.85` | 126,300,000.00 USD | 0.00 USD | 4,270.00 USD | `-59.58%` | `109.96` |
| `Live` | `Long` | `38.95` | 126,300,000.00 USD | 0.00 USD | 883.39 USD | `-59.47%` | `22.68` |
| `Live` | `Long` | `39.05` | 126,300,000.00 USD | 0.00 USD | 51,140.00 USD | `-59.37%` | `1,309.69` |
| `Live` | `Long` | `39.15` | 126,250,000.00 USD | 0.00 USD | 16,420.00 USD | `-59.26%` | `419.48` |
| `Live` | `Long` | `39.25` | 126,230,000.00 USD | 0.00 USD | 462.76 USD | `-59.16%` | `11.79` |
| `Live` | `Long` | `39.35` | 126,230,000.00 USD | 0.00 USD | 117,240.00 USD | `-59.05%` | `2,979.30` |
| `Live` | `Long` | `39.45` | 126,110,000.00 USD | 0.00 USD | 2,040.00 USD | `-58.95%` | `51.61` |
| `Live` | `Long` | `39.65` | 126,110,000.00 USD | 0.00 USD | 1,560.00 USD | `-58.74%` | `39.31` |
| `Live` | `Long` | `39.75` | 126,110,000.00 USD | 0.00 USD | 445.20 USD | `-58.64%` | `11.20` |
| `Live` | `Long` | `39.85` | 126,110,000.00 USD | 0.00 USD | 1,270.00 USD | `-58.53%` | `31.86` |
| `Live` | `Long` | `39.95` | 126,110,000.00 USD | 0.00 USD | 2,750.00 USD | `-58.43%` | `68.81` |
| `Live` | `Long` | `40.05` | 126,100,000.00 USD | 0.00 USD | 17,850.00 USD | `-58.33%` | `445.61` |
| `Live` | `Long` | `40.15` | 126,090,000.00 USD | 0.00 USD | 8,700.00 USD | `-58.22%` | `216.59` |
| `Live` | `Long` | `40.25` | 126,080,000.00 USD | 0.00 USD | 2,200.00 USD | `-58.12%` | `54.63` |
| `Live` | `Long` | `40.35` | 126,080,000.00 USD | 0.00 USD | 105.72 USD | `-58.01%` | `2.62` |
| `Live` | `Long` | `40.45` | 126,070,000.00 USD | 0.00 USD | 240.27 USD | `-57.91%` | `5.94` |
| `Live` | `Long` | `40.55` | 126,070,000.00 USD | 0.00 USD | 9,800.00 USD | `-57.81%` | `241.72` |
| `Live` | `Long` | `40.75` | 126,060,000.00 USD | 0.00 USD | 6,750.00 USD | `-57.60%` | `165.73` |
| `Live` | `Long` | `40.85` | 126,060,000.00 USD | 0.00 USD | 2,770.00 USD | `-57.49%` | `67.92` |
| `Live` | `Long` | `40.95` | 126,060,000.00 USD | 0.00 USD | 465.19 USD | `-57.39%` | `11.36` |
| `Live` | `Long` | `41.05` | 126,050,000.00 USD | 0.00 USD | 4,380.00 USD | `-57.29%` | `106.66` |
| `Live` | `Long` | `41.15` | 126,050,000.00 USD | 0.00 USD | 13,250.00 USD | `-57.18%` | `322.09` |
| `Live` | `Long` | `41.25` | 126,040,000.00 USD | 0.00 USD | 2,170.00 USD | `-57.08%` | `52.60` |
| `Live` | `Long` | `41.35` | 126,040,000.00 USD | 0.00 USD | 418.46 USD | `-56.97%` | `10.12` |
| `Live` | `Long` | `41.55` | 126,030,000.00 USD | 0.00 USD | 130.88 USD | `-56.77%` | `3.15` |
| `Live` | `Long` | `41.65` | 126,030,000.00 USD | 0.00 USD | 770.11 USD | `-56.66%` | `18.49` |
| `Live` | `Long` | `41.75` | 126,030,000.00 USD | 0.00 USD | 7,210.00 USD | `-56.56%` | `172.67` |
| `Live` | `Long` | `41.85` | 126,030,000.00 USD | 0.00 USD | 1,440.00 USD | `-56.45%` | `34.39` |
| `Live` | `Long` | `41.95` | 126,030,000.00 USD | 0.00 USD | 4,290.00 USD | `-56.35%` | `102.38` |
| `Live` | `Long` | `42.05` | 126,020,000.00 USD | 0.00 USD | 213.61 USD | `-56.25%` | `5.08` |
| `Live` | `Long` | `42.15` | 126,020,000.00 USD | 0.00 USD | 2,790.00 USD | `-56.14%` | `66.27` |
| `Live` | `Long` | `42.25` | 126,020,000.00 USD | 0.00 USD | 308.85 USD | `-56.04%` | `7.31` |
| `Live` | `Long` | `42.35` | 126,020,000.00 USD | 0.00 USD | 2,410.00 USD | `-55.93%` | `56.86` |
| `Live` | `Long` | `42.45` | 126,020,000.00 USD | 0.00 USD | 4,250.00 USD | `-55.83%` | `100.00` |
| `Live` | `Long` | `42.85` | 126,010,000.00 USD | 0.00 USD | 57,740.00 USD | `-55.41%` | `1,347.39` |
| `Live` | `Long` | `43.05` | 125,950,000.00 USD | 0.00 USD | 3,330.00 USD | `-55.20%` | `77.46` |
| `Live` | `Long` | `43.15` | 125,950,000.00 USD | 0.00 USD | 18,840.00 USD | `-55.10%` | `436.55` |
| `Live` | `Long` | `43.35` | 125,930,000.00 USD | 0.00 USD | 5,020.00 USD | `-54.89%` | `115.81` |
| `Live` | `Long` | `43.55` | 125,930,000.00 USD | 0.00 USD | 163.31 USD | `-54.68%` | `3.75` |
| `Live` | `Long` | `43.65` | 125,930,000.00 USD | 0.00 USD | 213.01 USD | `-54.58%` | `4.88` |
| `Live` | `Long` | `43.75` | 125,930,000.00 USD | 0.00 USD | 106.31 USD | `-54.48%` | `2.43` |
| `Live` | `Long` | `43.95` | 125,930,000.00 USD | 0.00 USD | 242.16 USD | `-54.27%` | `5.51` |
| `Live` | `Long` | `44.05` | 125,930,000.00 USD | 0.00 USD | 11,220.00 USD | `-54.16%` | `254.69` |
| `Live` | `Long` | `44.15` | 125,910,000.00 USD | 0.00 USD | 104.64 USD | `-54.06%` | `2.37` |
| `Live` | `Long` | `44.25` | 125,910,000.00 USD | 0.00 USD | 41,590.00 USD | `-53.96%` | `939.80` |
| `Live` | `Long` | `44.35` | 125,870,000.00 USD | 0.00 USD | 5,980.00 USD | `-53.85%` | `134.92` |
| `Live` | `Long` | `44.45` | 125,870,000.00 USD | 0.00 USD | 6,790.00 USD | `-53.75%` | `152.74` |
| `Live` | `Long` | `44.55` | 125,860,000.00 USD | 0.00 USD | 17,870.00 USD | `-53.64%` | `401.03` |
| `Live` | `Long` | `44.65` | 125,840,000.00 USD | 0.00 USD | 410.78 USD | `-53.54%` | `9.20` |
| `Live` | `Long` | `44.75` | 125,840,000.00 USD | 0.00 USD | 1,790.00 USD | `-53.44%` | `39.98` |
| `Live` | `Long` | `44.85` | 125,840,000.00 USD | 0.00 USD | 2,630.00 USD | `-53.33%` | `58.71` |
| `Live` | `Long` | `44.95` | 125,840,000.00 USD | 0.00 USD | 120,590.00 USD | `-53.23%` | `2,682.84` |
| `Live` | `Long` | `45.15` | 125,720,000.00 USD | 0.00 USD | 179.70 USD | `-53.02%` | `3.98` |
| `Live` | `Long` | `45.25` | 125,720,000.00 USD | 0.00 USD | 8,090.00 USD | `-52.92%` | `178.70` |
| `Live` | `Long` | `45.35` | 125,710,000.00 USD | 0.00 USD | 10,470.00 USD | `-52.81%` | `230.90` |
| `Live` | `Long` | `45.45` | 125,700,000.00 USD | 0.00 USD | 10,020.00 USD | `-52.71%` | `220.51` |
| `Live` | `Long` | `45.55` | 125,690,000.00 USD | 0.00 USD | 7,840.00 USD | `-52.60%` | `172.03` |
| `Live` | `Long` | `45.65` | 125,680,000.00 USD | 0.00 USD | 319.09 USD | `-52.50%` | `6.99` |
| `Live` | `Long` | `45.75` | 125,680,000.00 USD | 0.00 USD | 9,450.00 USD | `-52.40%` | `206.46` |
| `Live` | `Long` | `45.85` | 125,670,000.00 USD | 0.00 USD | 458.50 USD | `-52.29%` | `10.00` |
| `Live` | `Long` | `45.95` | 125,670,000.00 USD | 0.00 USD | 26,180.00 USD | `-52.19%` | `569.85` |
| `Live` | `Long` | `46.05` | 125,640,000.00 USD | 0.00 USD | 742.33 USD | `-52.08%` | `16.12` |
| `Live` | `Long` | `46.25` | 125,640,000.00 USD | 0.00 USD | 46,250.00 USD | `-51.88%` | `1,000.00` |
| `Live` | `Long` | `46.45` | 125,600,000.00 USD | 0.00 USD | 3,590.00 USD | `-51.67%` | `77.33` |
| `Live` | `Long` | `46.55` | 125,590,000.00 USD | 0.00 USD | 522.76 USD | `-51.56%` | `11.23` |
| `Live` | `Long` | `46.65` | 125,590,000.00 USD | 0.00 USD | 14,810.00 USD | `-51.46%` | `317.39` |
| `Live` | `Long` | `46.75` | 125,580,000.00 USD | 0.00 USD | 5,050.00 USD | `-51.35%` | `108.00` |
| `Live` | `Long` | `46.85` | 125,570,000.00 USD | 0.00 USD | 140.55 USD | `-51.25%` | `3.00` |
| `Live` | `Long` | `46.95` | 125,570,000.00 USD | 0.00 USD | 2,330.00 USD | `-51.15%` | `49.63` |
| `Live` | `Long` | `47.05` | 125,570,000.00 USD | 0.00 USD | 10,550.00 USD | `-51.04%` | `224.24` |
| `Live` | `Long` | `47.15` | 125,560,000.00 USD | 0.00 USD | 3,520.00 USD | `-50.94%` | `74.62` |
| `Live` | `Long` | `47.25` | 125,560,000.00 USD | 0.00 USD | 3,050.00 USD | `-50.83%` | `64.59` |
| `Live` | `Long` | `47.55` | 125,550,000.00 USD | 0.00 USD | 1,630.00 USD | `-50.52%` | `34.23` |
| `Live` | `Long` | `47.65` | 125,550,000.00 USD | 0.00 USD | 3,480.00 USD | `-50.42%` | `73.02` |
| `Live` | `Long` | `47.75` | 125,550,000.00 USD | 0.00 USD | 1,190.00 USD | `-50.31%` | `24.99` |
| `Live` | `Long` | `48.05` | 125,550,000.00 USD | 0.00 USD | 14,080.00 USD | `-50.00%` | `292.97` |
| `Live` | `Long` | `48.15` | 125,530,000.00 USD | 0.00 USD | 5,740.00 USD | `-49.90%` | `119.29` |
| `Live` | `Long` | `48.25` | 125,530,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-49.79%` | `24,045.57` |
| `Live` | `Long` | `48.35` | 124,370,000.00 USD | 0.00 USD | 5,280.00 USD | `-49.69%` | `109.21` |
| `Live` | `Long` | `48.45` | 124,360,000.00 USD | 0.00 USD | 13,820.00 USD | `-49.59%` | `285.28` |
| `Live` | `Long` | `48.55` | 124,350,000.00 USD | 0.00 USD | 3,310.00 USD | `-49.48%` | `68.13` |
| `Live` | `Long` | `48.65` | 124,340,000.00 USD | 0.00 USD | 8,450.00 USD | `-49.38%` | `173.68` |
| `Live` | `Long` | `48.75` | 124,340,000.00 USD | 0.00 USD | 453.38 USD | `-49.27%` | `9.30` |
| `Live` | `Long` | `48.85` | 124,340,000.00 USD | 0.00 USD | 13,000.00 USD | `-49.17%` | `266.20` |
| `Live` | `Long` | `48.95` | 124,320,000.00 USD | 0.00 USD | 1,250.00 USD | `-49.07%` | `25.51` |
| `Live` | `Long` | `49.05` | 124,320,000.00 USD | 0.00 USD | 1,120.00 USD | `-48.96%` | `22.86` |
| `Live` | `Long` | `49.15` | 124,320,000.00 USD | 0.00 USD | 4,150,000.00 USD | `-48.86%` | `84,528.09` |
| `Live` | `Long` | `49.25` | 120,170,000.00 USD | 0.00 USD | 10,790.00 USD | `-48.75%` | `219.02` |
| `Live` | `Long` | `49.35` | 120,150,000.00 USD | 0.00 USD | 733.34 USD | `-48.65%` | `14.86` |
| `Live` | `Long` | `49.45` | 120,150,000.00 USD | 0.00 USD | 5,320.00 USD | `-48.55%` | `107.49` |
| `Live` | `Long` | `49.55` | 120,150,000.00 USD | 0.00 USD | 8,310.00 USD | `-48.44%` | `167.79` |
| `Live` | `Long` | `49.65` | 120,140,000.00 USD | 0.00 USD | 1,600.00 USD | `-48.34%` | `32.24` |
| `Live` | `Long` | `49.75` | 120,140,000.00 USD | 0.00 USD | 6,990.00 USD | `-48.23%` | `140.48` |
| `Live` | `Long` | `49.85` | 120,130,000.00 USD | 0.00 USD | 6,210.00 USD | `-48.13%` | `124.55` |
| `Live` | `Long` | `49.95` | 120,130,000.00 USD | 0.00 USD | 14,670.00 USD | `-48.03%` | `293.63` |
| `Live` | `Long` | `50.05` | 120,110,000.00 USD | 0.00 USD | 8,560.00 USD | `-47.92%` | `171.08` |
| `Live` | `Long` | `50.15` | 120,100,000.00 USD | 0.00 USD | 1,890.00 USD | `-47.82%` | `37.67` |
| `Live` | `Long` | `50.25` | 120,100,000.00 USD | 0.00 USD | 11,670.00 USD | `-47.71%` | `232.26` |
| `Live` | `Long` | `50.45` | 120,090,000.00 USD | 0.00 USD | 4,170.00 USD | `-47.50%` | `82.73` |
| `Live` | `Long` | `50.55` | 120,080,000.00 USD | 0.00 USD | 2,910.00 USD | `-47.40%` | `57.47` |
| `Live` | `Long` | `50.65` | 120,080,000.00 USD | 0.00 USD | 337.33 USD | `-47.30%` | `6.66` |
| `Live` | `Long` | `50.75` | 120,080,000.00 USD | 0.00 USD | 12,190.00 USD | `-47.19%` | `240.29` |
| `Live` | `Long` | `50.85` | 120,070,000.00 USD | 0.00 USD | 19,710.00 USD | `-47.09%` | `387.64` |
| `Live` | `Long` | `50.95` | 120,050,000.00 USD | 0.00 USD | 3,850.00 USD | `-46.98%` | `75.61` |
| `Live` | `Long` | `51.05` | 120,050,000.00 USD | 0.00 USD | 2,680.00 USD | `-46.88%` | `52.57` |
| `Live` | `Long` | `51.15` | 120,040,000.00 USD | 0.00 USD | 59,700.00 USD | `-46.78%` | `1,167.14` |
| `Live` | `Long` | `51.25` | 119,980,000.00 USD | 0.00 USD | 10,820.00 USD | `-46.67%` | `211.19` |
| `Live` | `Long` | `51.35` | 119,970,000.00 USD | 0.00 USD | 360.48 USD | `-46.57%` | `7.02` |
| `Live` | `Long` | `51.45` | 119,970,000.00 USD | 0.00 USD | 7,210.00 USD | `-46.46%` | `140.17` |
| `Live` | `Long` | `51.55` | 119,960,000.00 USD | 0.00 USD | 22,760.00 USD | `-46.36%` | `441.45` |
| `Live` | `Long` | `51.65` | 119,940,000.00 USD | 0.00 USD | 302.15 USD | `-46.26%` | `5.85` |
| `Live` | `Long` | `51.75` | 119,940,000.00 USD | 0.00 USD | 26,370.00 USD | `-46.15%` | `509.64` |
| `Live` | `Long` | `51.85` | 119,920,000.00 USD | 0.00 USD | 45,490.00 USD | `-46.05%` | `877.43` |
| `Live` | `Long` | `51.95` | 119,870,000.00 USD | 0.00 USD | 478,640.00 USD | `-45.94%` | `9,213.38` |
| `Live` | `Long` | `52.05` | 119,390,000.00 USD | 0.00 USD | 98,310.00 USD | `-45.84%` | `1,888.80` |
| `Live` | `Long` | `52.15` | 119,290,000.00 USD | 0.00 USD | 1,690.00 USD | `-45.74%` | `32.45` |
| `Live` | `Long` | `52.25` | 119,290,000.00 USD | 0.00 USD | 4,320.00 USD | `-45.63%` | `82.73` |
| `Live` | `Long` | `52.35` | 119,290,000.00 USD | 0.00 USD | 4,600.00 USD | `-45.53%` | `87.78` |
| `Live` | `Long` | `52.45` | 119,280,000.00 USD | 0.00 USD | 879.59 USD | `-45.42%` | `16.77` |
| `Live` | `Long` | `52.55` | 119,280,000.00 USD | 0.00 USD | 1,460.00 USD | `-45.32%` | `27.80` |
| `Live` | `Long` | `52.65` | 119,280,000.00 USD | 0.00 USD | 4,270.00 USD | `-45.22%` | `81.04` |
| `Live` | `Long` | `52.75` | 119,280,000.00 USD | 0.00 USD | 27,610.00 USD | `-45.11%` | `523.49` |
| `Live` | `Long` | `52.85` | 119,250,000.00 USD | 0.00 USD | 9,530.00 USD | `-45.01%` | `180.28` |
| `Live` | `Long` | `52.95` | 119,240,000.00 USD | 0.00 USD | 3,890.00 USD | `-44.90%` | `73.46` |
| `Live` | `Long` | `53.05` | 119,230,000.00 USD | 0.00 USD | 5,120.00 USD | `-44.80%` | `96.59` |
| `Live` | `Long` | `53.15` | 119,230,000.00 USD | 0.00 USD | 27,710.00 USD | `-44.70%` | `521.34` |
| `Live` | `Long` | `53.25` | 119,200,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-44.59%` | `19,713.72` |
| `Live` | `Long` | `53.35` | 118,150,000.00 USD | 0.00 USD | 3,260.00 USD | `-44.49%` | `61.16` |
| `Live` | `Long` | `53.45` | 118,150,000.00 USD | 0.00 USD | 34,550.00 USD | `-44.38%` | `646.33` |
| `Live` | `Long` | `53.55` | 118,110,000.00 USD | 0.00 USD | 44,800.00 USD | `-44.28%` | `836.54` |
| `Live` | `Long` | `53.65` | 118,070,000.00 USD | 0.00 USD | 916.88 USD | `-44.18%` | `17.09` |
| `Live` | `Long` | `53.75` | 118,070,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.07%` | `67.00` |
| `Live` | `Long` | `53.85` | 118,060,000.00 USD | 0.00 USD | 19,810.00 USD | `-43.97%` | `367.96` |
| `Live` | `Long` | `53.95` | 118,040,000.00 USD | 0.00 USD | 59,050.00 USD | `-43.86%` | `1,094.61` |
| `Live` | `Long` | `54.05` | 117,990,000.00 USD | 0.00 USD | 3,360.00 USD | `-43.76%` | `62.12` |
| `Live` | `Long` | `54.15` | 117,980,000.00 USD | 0.00 USD | 15,030.00 USD | `-43.65%` | `277.53` |
| `Live` | `Long` | `54.25` | 117,970,000.00 USD | 0.00 USD | 11,500.00 USD | `-43.55%` | `211.99` |
| `Live` | `Long` | `54.35` | 117,960,000.00 USD | 0.00 USD | 3,980.00 USD | `-43.45%` | `73.16` |
| `Live` | `Long` | `54.45` | 117,950,000.00 USD | 0.00 USD | 753.04 USD | `-43.34%` | `13.83` |
| `Live` | `Long` | `54.55` | 117,950,000.00 USD | 0.00 USD | 64,870.00 USD | `-43.24%` | `1,189.16` |
| `Live` | `Long` | `54.65` | 117,890,000.00 USD | 0.00 USD | 3,510.00 USD | `-43.13%` | `64.29` |
| `Live` | `Long` | `54.75` | 117,880,000.00 USD | 0.00 USD | 17,320.00 USD | `-43.03%` | `316.32` |
| `Live` | `Long` | `54.85` | 117,870,000.00 USD | 0.00 USD | 958,960.00 USD | `-42.93%` | `17,483.40` |
| `Live` | `Long` | `54.95` | 116,910,000.00 USD | 0.00 USD | 259,570.00 USD | `-42.82%` | `4,723.76` |
| `Live` | `Long` | `55.05` | 116,650,000.00 USD | 0.00 USD | 26,930.00 USD | `-42.72%` | `489.15` |
| `Live` | `Long` | `55.15` | 116,620,000.00 USD | 0.00 USD | 739.01 USD | `-42.61%` | `13.40` |
| `Live` | `Long` | `55.25` | 116,620,000.00 USD | 0.00 USD | 2,010.00 USD | `-42.51%` | `36.31` |
| `Live` | `Long` | `55.35` | 116,620,000.00 USD | 0.00 USD | 12,110.00 USD | `-42.41%` | `218.73` |
| `Live` | `Long` | `55.45` | 116,610,000.00 USD | 0.00 USD | 5,970.00 USD | `-42.30%` | `107.71` |
| `Live` | `Long` | `55.55` | 116,600,000.00 USD | 0.00 USD | 15,130.00 USD | `-42.20%` | `272.38` |
| `Live` | `Long` | `55.65` | 116,580,000.00 USD | 0.00 USD | 7,060.00 USD | `-42.09%` | `126.84` |
| `Live` | `Long` | `55.75` | 116,580,000.00 USD | 0.00 USD | 85,360.00 USD | `-41.99%` | `1,531.18` |
| `Live` | `Long` | `55.85` | 116,490,000.00 USD | 0.00 USD | 4,090.00 USD | `-41.89%` | `73.18` |
| `Live` | `Long` | `55.95` | 116,490,000.00 USD | 0.00 USD | 1,180.00 USD | `-41.78%` | `21.07` |
| `Live` | `Long` | `56.05` | 116,490,000.00 USD | 0.00 USD | 7,310.00 USD | `-41.68%` | `130.37` |
| `Live` | `Long` | `56.15` | 116,480,000.00 USD | 0.00 USD | 36,190.00 USD | `-41.57%` | `644.50` |
| `Live` | `Long` | `56.25` | 116,440,000.00 USD | 0.00 USD | 17,970.00 USD | `-41.47%` | `319.43` |
| `Live` | `Long` | `56.35` | 116,420,000.00 USD | 0.00 USD | 7,880.00 USD | `-41.37%` | `139.77` |
| `Live` | `Long` | `56.45` | 116,420,000.00 USD | 0.00 USD | 16,640.00 USD | `-41.26%` | `294.82` |
| `Live` | `Long` | `56.55` | 116,400,000.00 USD | 0.00 USD | 90,120.00 USD | `-41.16%` | `1,593.63` |
| `Live` | `Long` | `56.65` | 116,310,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-41.05%` | `19,921.14` |
| `Live` | `Long` | `56.75` | 115,180,000.00 USD | 0.00 USD | 15,090.00 USD | `-40.95%` | `265.87` |
| `Live` | `Long` | `56.85` | 115,170,000.00 USD | 0.00 USD | 122.80 USD | `-40.85%` | `2.16` |
| `Live` | `Long` | `56.95` | 115,170,000.00 USD | 0.00 USD | 24,680.00 USD | `-40.74%` | `433.32` |
| `Live` | `Long` | `57.05` | 115,140,000.00 USD | 0.00 USD | 4,410.00 USD | `-40.64%` | `77.22` |
| `Live` | `Long` | `57.15` | 115,140,000.00 USD | 0.00 USD | 5,380.00 USD | `-40.53%` | `94.22` |
| `Live` | `Long` | `57.25` | 115,130,000.00 USD | 0.00 USD | 1,380.00 USD | `-40.43%` | `24.12` |
| `Live` | `Long` | `57.35` | 115,130,000.00 USD | 0.00 USD | 9,580.00 USD | `-40.33%` | `167.07` |
| `Live` | `Long` | `57.45` | 115,120,000.00 USD | 0.00 USD | 25,070.00 USD | `-40.22%` | `436.35` |
| `Live` | `Long` | `57.55` | 115,100,000.00 USD | 0.00 USD | 924.25 USD | `-40.12%` | `16.06` |
| `Live` | `Long` | `57.65` | 115,100,000.00 USD | 0.00 USD | 2,320,000.00 USD | `-40.01%` | `40,247.63` |
| `Live` | `Long` | `57.75` | 112,770,000.00 USD | 0.00 USD | 65,310.00 USD | `-39.91%` | `1,130.87` |
| `Live` | `Long` | `57.85` | 112,710,000.00 USD | 0.00 USD | 29,860.00 USD | `-39.80%` | `516.17` |
| `Live` | `Long` | `57.95` | 112,680,000.00 USD | 0.00 USD | 16,610.00 USD | `-39.70%` | `286.68` |
| `Live` | `Long` | `58.05` | 112,660,000.00 USD | 0.00 USD | 4,710.00 USD | `-39.60%` | `81.10` |
| `Live` | `Long` | `58.15` | 112,660,000.00 USD | 0.00 USD | 127,240.00 USD | `-39.49%` | `2,188.13` |
| `Live` | `Long` | `58.25` | 112,530,000.00 USD | 0.00 USD | 9,870.00 USD | `-39.39%` | `169.44` |
| `Live` | `Long` | `58.35` | 112,520,000.00 USD | 0.00 USD | 17,330.00 USD | `-39.28%` | `296.96` |
| `Live` | `Long` | `58.55` | 112,500,000.00 USD | 0.00 USD | 2,970.00 USD | `-39.08%` | `50.81` |
| `Live` | `Long` | `58.65` | 112,500,000.00 USD | 0.00 USD | 418.17 USD | `-38.97%` | `7.13` |
| `Live` | `Long` | `58.75` | 112,500,000.00 USD | 0.00 USD | 195.64 USD | `-38.87%` | `3.33` |
| `Live` | `Long` | `58.85` | 112,500,000.00 USD | 0.00 USD | 6,130.00 USD | `-38.76%` | `104.08` |
| `Live` | `Long` | `58.95` | 112,490,000.00 USD | 0.00 USD | 48,160.00 USD | `-38.66%` | `816.89` |
| `Live` | `Long` | `59.05` | 112,450,000.00 USD | 0.00 USD | 17,200.00 USD | `-38.56%` | `291.25` |
| `Live` | `Long` | `59.15` | 112,430,000.00 USD | 0.00 USD | 11,490.00 USD | `-38.45%` | `194.31` |
| `Live` | `Long` | `59.25` | 112,420,000.00 USD | 0.00 USD | 13,850.00 USD | `-38.35%` | `233.81` |
| `Live` | `Long` | `59.35` | 112,400,000.00 USD | 0.00 USD | 28,430.00 USD | `-38.24%` | `479.02` |
| `Live` | `Long` | `59.45` | 112,380,000.00 USD | 0.00 USD | 9,240.00 USD | `-38.14%` | `155.46` |
| `Live` | `Long` | `59.55` | 112,370,000.00 USD | 0.00 USD | 68,160.00 USD | `-38.04%` | `1,144.57` |
| `Live` | `Long` | `59.65` | 112,300,000.00 USD | 0.00 USD | 4,680.00 USD | `-37.93%` | `78.52` |
| `Live` | `Long` | `59.75` | 112,290,000.00 USD | 0.00 USD | 12,090.00 USD | `-37.83%` | `202.31` |
| `Live` | `Long` | `59.85` | 112,280,000.00 USD | 0.00 USD | 74,960.00 USD | `-37.72%` | `1,252.48` |
| `Live` | `Long` | `59.95` | 112,210,000.00 USD | 0.00 USD | 37,240.00 USD | `-37.62%` | `621.17` |
| `Live` | `Long` | `60.05` | 112,170,000.00 USD | 0.00 USD | 54,140.00 USD | `-37.52%` | `901.63` |
| `Live` | `Long` | `60.15` | 112,110,000.00 USD | 0.00 USD | 35,270.00 USD | `-37.41%` | `586.42` |
| `Live` | `Long` | `60.25` | 112,080,000.00 USD | 0.00 USD | 2,340.00 USD | `-37.31%` | `38.84` |
| `Live` | `Long` | `60.35` | 112,080,000.00 USD | 0.00 USD | 2,090.00 USD | `-37.20%` | `34.55` |
| `Live` | `Long` | `60.45` | 112,070,000.00 USD | 0.00 USD | 557.35 USD | `-37.10%` | `9.22` |
| `Live` | `Long` | `60.55` | 112,070,000.00 USD | 0.00 USD | 2,760.00 USD | `-37.00%` | `45.51` |
| `Live` | `Long` | `60.65` | 112,070,000.00 USD | 0.00 USD | 8,400.00 USD | `-36.89%` | `138.52` |
| `Live` | `Long` | `60.75` | 112,060,000.00 USD | 0.00 USD | 7,040.00 USD | `-36.79%` | `115.88` |
| `Live` | `Long` | `60.85` | 112,060,000.00 USD | 0.00 USD | 28,700.00 USD | `-36.68%` | `471.62` |
| `Live` | `Long` | `60.95` | 112,030,000.00 USD | 0.00 USD | 78,670.00 USD | `-36.58%` | `1,290.73` |
| `Live` | `Long` | `61.05` | 111,950,000.00 USD | 0.00 USD | 4,230.00 USD | `-36.48%` | `69.34` |
| `Live` | `Long` | `61.15` | 111,940,000.00 USD | 0.00 USD | 683.66 USD | `-36.37%` | `11.18` |
| `Live` | `Long` | `61.25` | 111,940,000.00 USD | 0.00 USD | 125,590.00 USD | `-36.27%` | `2,050.52` |
| `Live` | `Long` | `61.35` | 111,820,000.00 USD | 0.00 USD | 23,340.00 USD | `-36.16%` | `380.39` |
| `Live` | `Long` | `61.45` | 111,790,000.00 USD | 0.00 USD | 13,520.00 USD | `-36.06%` | `219.94` |
| `Live` | `Long` | `61.55` | 111,780,000.00 USD | 0.00 USD | 121.87 USD | `-35.95%` | `1.98` |
| `Live` | `Long` | `61.65` | 111,780,000.00 USD | 0.00 USD | 39,450.00 USD | `-35.85%` | `639.98` |
| `Live` | `Long` | `61.75` | 111,740,000.00 USD | 0.00 USD | 16,580.00 USD | `-35.75%` | `268.54` |
| `Live` | `Long` | `61.85` | 111,730,000.00 USD | 0.00 USD | 5,780.00 USD | `-35.64%` | `93.47` |
| `Live` | `Long` | `61.95` | 111,720,000.00 USD | 0.00 USD | 3,980.00 USD | `-35.54%` | `64.17` |
| `Live` | `Long` | `62.05` | 111,720,000.00 USD | 0.00 USD | 66,840.00 USD | `-35.43%` | `1,077.17` |
| `Live` | `Long` | `62.15` | 111,650,000.00 USD | 0.00 USD | 25,350.00 USD | `-35.33%` | `407.88` |
| `Live` | `Long` | `62.25` | 111,620,000.00 USD | 0.00 USD | 3,850.00 USD | `-35.23%` | `61.90` |
| `Live` | `Long` | `62.35` | 111,620,000.00 USD | 0.00 USD | 31,770.00 USD | `-35.12%` | `509.49` |
| `Live` | `Long` | `62.45` | 111,590,000.00 USD | 0.00 USD | 20,410.00 USD | `-35.02%` | `326.90` |
| `Live` | `Long` | `62.55` | 111,570,000.00 USD | 0.00 USD | 3,250.00 USD | `-34.91%` | `51.93` |
| `Live` | `Long` | `62.65` | 111,560,000.00 USD | 0.00 USD | 7,620.00 USD | `-34.81%` | `121.60` |
| `Live` | `Long` | `62.75` | 111,560,000.00 USD | 0.00 USD | 4,830.00 USD | `-34.71%` | `76.97` |
| `Live` | `Long` | `62.85` | 111,550,000.00 USD | 0.00 USD | 31,310.00 USD | `-34.60%` | `498.17` |
| `Live` | `Long` | `62.95` | 111,520,000.00 USD | 0.00 USD | 65,480.00 USD | `-34.50%` | `1,040.25` |
| `Live` | `Long` | `63.05` | 111,450,000.00 USD | 0.00 USD | 15,420.00 USD | `-34.39%` | `244.49` |
| `Live` | `Long` | `63.15` | 111,440,000.00 USD | 0.00 USD | 81,940.00 USD | `-34.29%` | `1,297.50` |
| `Live` | `Long` | `63.25` | 111,360,000.00 USD | 0.00 USD | 14,620.00 USD | `-34.19%` | `231.15` |
| `Live` | `Long` | `63.35` | 111,340,000.00 USD | 0.00 USD | 14,240.00 USD | `-34.08%` | `224.73` |
| `Live` | `Long` | `63.45` | 111,330,000.00 USD | 0.00 USD | 43,420.00 USD | `-33.98%` | `684.37` |
| `Live` | `Long` | `63.55` | 111,290,000.00 USD | 0.00 USD | 6,000.00 USD | `-33.87%` | `94.40` |
| `Live` | `Long` | `63.65` | 111,280,000.00 USD | 0.00 USD | 8,840.00 USD | `-33.77%` | `138.96` |
| `Live` | `Long` | `63.75` | 111,270,000.00 USD | 0.00 USD | 8,560.00 USD | `-33.67%` | `134.23` |
| `Live` | `Long` | `63.85` | 111,260,000.00 USD | 0.00 USD | 46,170.00 USD | `-33.56%` | `723.08` |
| `Live` | `Long` | `63.95` | 111,220,000.00 USD | 0.00 USD | 39,740.00 USD | `-33.46%` | `621.40` |
| `Live` | `Long` | `64.05` | 111,180,000.00 USD | 0.00 USD | 384,300.00 USD | `-33.35%` | `6,000.00` |
| `Live` | `Long` | `64.25` | 110,790,000.00 USD | 0.00 USD | 14,550.00 USD | `-33.15%` | `226.43` |
| `Live` | `Long` | `64.35` | 110,780,000.00 USD | 0.00 USD | 875.16 USD | `-33.04%` | `13.60` |
| `Live` | `Long` | `64.45` | 110,780,000.00 USD | 0.00 USD | 6,300.00 USD | `-32.94%` | `97.79` |
| `Live` | `Long` | `64.55` | 110,770,000.00 USD | 0.00 USD | 1,400.00 USD | `-32.83%` | `21.68` |
| `Live` | `Long` | `64.65` | 110,770,000.00 USD | 0.00 USD | 1,740.00 USD | `-32.73%` | `26.99` |
| `Live` | `Long` | `64.85` | 110,770,000.00 USD | 0.00 USD | 5,660.00 USD | `-32.52%` | `87.32` |
| `Live` | `Long` | `64.95` | 110,760,000.00 USD | 0.00 USD | 6,290.00 USD | `-32.42%` | `96.79` |
| `Live` | `Long` | `65.05` | 110,750,000.00 USD | 0.00 USD | 13,530.00 USD | `-32.31%` | `208.00` |
| `Live` | `Long` | `65.15` | 110,740,000.00 USD | 0.00 USD | 18,550.00 USD | `-32.21%` | `284.71` |
| `Live` | `Long` | `65.25` | 110,720,000.00 USD | 0.00 USD | 7,960.00 USD | `-32.10%` | `121.97` |
| `Live` | `Long` | `65.35` | 110,710,000.00 USD | 0.00 USD | 17,210.00 USD | `-32.00%` | `263.29` |
| `Live` | `Long` | `65.55` | 110,700,000.00 USD | 0.00 USD | 8,740.00 USD | `-31.79%` | `133.26` |
| `Live` | `Long` | `65.65` | 110,690,000.00 USD | 0.00 USD | 58,380.00 USD | `-31.69%` | `889.27` |
| `Live` | `Long` | `65.75` | 110,630,000.00 USD | 0.00 USD | 56,580.00 USD | `-31.58%` | `860.58` |
| `Live` | `Long` | `65.85` | 110,570,000.00 USD | 0.00 USD | 56,660.00 USD | `-31.48%` | `860.47` |
| `Live` | `Long` | `65.95` | 110,520,000.00 USD | 0.00 USD | 16,870.00 USD | `-31.38%` | `255.85` |
| `Live` | `Long` | `66.05` | 110,500,000.00 USD | 0.00 USD | 367.90 USD | `-31.27%` | `5.57` |
| `Live` | `Long` | `66.15` | 110,500,000.00 USD | 0.00 USD | 4,420.00 USD | `-31.17%` | `66.86` |
| `Live` | `Long` | `66.25` | 110,500,000.00 USD | 0.00 USD | 25,970.00 USD | `-31.06%` | `391.98` |
| `Live` | `Long` | `66.35` | 110,470,000.00 USD | 0.00 USD | 1,460.00 USD | `-30.96%` | `22.02` |
| `Live` | `Long` | `66.45` | 110,470,000.00 USD | 0.00 USD | 1,490.00 USD | `-30.86%` | `22.42` |
| `Live` | `Long` | `66.55` | 110,470,000.00 USD | 0.00 USD | 45,890.00 USD | `-30.75%` | `689.53` |
| `Live` | `Long` | `66.65` | 110,420,000.00 USD | 0.00 USD | 14,310.00 USD | `-30.65%` | `214.66` |
| `Live` | `Long` | `66.75` | 110,410,000.00 USD | 0.00 USD | 5,010.00 USD | `-30.54%` | `75.00` |
| `Live` | `Long` | `66.85` | 110,400,000.00 USD | 0.00 USD | 1,340.00 USD | `-30.44%` | `20.08` |
| `Live` | `Long` | `66.95` | 110,400,000.00 USD | 0.00 USD | 1,050.00 USD | `-30.34%` | `15.72` |
| `Live` | `Long` | `67.05` | 110,400,000.00 USD | 0.00 USD | 33,390.00 USD | `-30.23%` | `497.96` |
| `Live` | `Long` | `67.15` | 110,370,000.00 USD | 0.00 USD | 2,510.00 USD | `-30.13%` | `37.39` |
| `Live` | `Long` | `67.25` | 110,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-30.02%` | `20,187.90` |
| `Live` | `Long` | `67.35` | 109,010,000.00 USD | 0.00 USD | 2,900.00 USD | `-29.92%` | `43.05` |
| `Live` | `Long` | `67.45` | 109,000,000.00 USD | 0.00 USD | 37,840.00 USD | `-29.82%` | `561.01` |
| `Live` | `Long` | `67.55` | 108,960,000.00 USD | 0.00 USD | 3,340,000.00 USD | `-29.71%` | `49,400.98` |
| `Live` | `Long` | `67.65` | 105,630,000.00 USD | 0.00 USD | 125,880.00 USD | `-29.61%` | `1,860.77` |
| `Live` | `Long` | `67.75` | 105,500,000.00 USD | 0.00 USD | 3,160.00 USD | `-29.50%` | `46.64` |
| `Live` | `Long` | `67.85` | 105,500,000.00 USD | 0.00 USD | 13,570.00 USD | `-29.40%` | `200.04` |
| `Live` | `Long` | `67.95` | 105,480,000.00 USD | 0.00 USD | 11,870.00 USD | `-29.30%` | `174.62` |
| `Live` | `Long` | `68.05` | 105,470,000.00 USD | 0.00 USD | 170.13 USD | `-29.19%` | `2.50` |
| `Live` | `Long` | `68.15` | 105,470,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-29.09%` | `550,133.95` |
| `Live` | `Long` | `68.25` | 67,980,000.00 USD | 0.00 USD | 12,330,000.00 USD | `-28.98%` | `180,599.93` |
| `Live` | `Long` | `68.35` | 55,660,000.00 USD | 0.00 USD | 4,860.00 USD | `-28.88%` | `71.12` |
| `Live` | `Long` | `68.45` | 55,650,000.00 USD | 0.00 USD | 21,590.00 USD | `-28.78%` | `315.40` |
| `Live` | `Long` | `68.55` | 55,630,000.00 USD | 0.00 USD | 41,980.00 USD | `-28.67%` | `612.42` |
| `Live` | `Long` | `68.65` | 55,590,000.00 USD | 0.00 USD | 779,380.00 USD | `-28.57%` | `11,352.89` |
| `Live` | `Long` | `68.75` | 54,810,000.00 USD | 0.00 USD | 60,650.00 USD | `-28.46%` | `882.24` |
| `Live` | `Long` | `68.85` | 54,750,000.00 USD | 0.00 USD | 3,240.00 USD | `-28.36%` | `47.11` |
| `Live` | `Long` | `68.95` | 54,740,000.00 USD | 0.00 USD | 57,300.00 USD | `-28.25%` | `831.03` |
| `Live` | `Long` | `69.05` | 54,690,000.00 USD | 0.00 USD | 3,570.00 USD | `-28.15%` | `51.69` |
| `Live` | `Long` | `69.15` | 54,680,000.00 USD | 0.00 USD | 11,350.00 USD | `-28.05%` | `164.13` |
| `Live` | `Long` | `69.25` | 54,670,000.00 USD | 0.00 USD | 9,450.00 USD | `-27.94%` | `136.45` |
| `Live` | `Long` | `69.35` | 54,660,000.00 USD | 0.00 USD | 1,210.00 USD | `-27.84%` | `17.43` |
| `Live` | `Long` | `69.45` | 54,660,000.00 USD | 0.00 USD | 15,690.00 USD | `-27.73%` | `225.86` |
| `Live` | `Long` | `69.55` | 54,650,000.00 USD | 0.00 USD | 11,110.00 USD | `-27.63%` | `159.68` |
| `Live` | `Long` | `69.65` | 54,630,000.00 USD | 0.00 USD | 5,490.00 USD | `-27.53%` | `78.77` |
| `Live` | `Long` | `69.75` | 54,630,000.00 USD | 0.00 USD | 20,550.00 USD | `-27.42%` | `294.69` |
| `Live` | `Long` | `69.85` | 54,610,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-27.32%` | `15,311.49` |
| `Live` | `Long` | `69.95` | 53,540,000.00 USD | 0.00 USD | 9,180.00 USD | `-27.21%` | `131.21` |
| `Live` | `Long` | `70.05` | 53,530,000.00 USD | 0.00 USD | 1,550.00 USD | `-27.11%` | `22.13` |
| `Live` | `Long` | `70.15` | 53,530,000.00 USD | 0.00 USD | 40,220.00 USD | `-27.01%` | `573.33` |
| `Live` | `Long` | `70.25` | 53,490,000.00 USD | 0.00 USD | 73,520.00 USD | `-26.90%` | `1,046.55` |
| `Live` | `Long` | `70.35` | 53,410,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-26.80%` | `30,328.17` |
| `Live` | `Long` | `70.45` | 51,280,000.00 USD | 0.00 USD | 114,610.00 USD | `-26.69%` | `1,626.86` |
| `Live` | `Long` | `70.55` | 51,170,000.00 USD | 0.00 USD | 161,340.00 USD | `-26.59%` | `2,286.90` |
| `Live` | `Long` | `70.65` | 51,000,000.00 USD | 0.00 USD | 98,950.00 USD | `-26.49%` | `1,400.56` |
| `Live` | `Long` | `70.75` | 50,910,000.00 USD | 0.00 USD | 13,570.00 USD | `-26.38%` | `191.80` |
| `Live` | `Long` | `70.85` | 50,890,000.00 USD | 0.00 USD | 23,480.00 USD | `-26.28%` | `331.42` |
| `Live` | `Long` | `70.95` | 50,870,000.00 USD | 0.00 USD | 249,420.00 USD | `-26.17%` | `3,515.39` |
| `Live` | `Long` | `71.05` | 50,620,000.00 USD | 0.00 USD | 32,670.00 USD | `-26.07%` | `459.78` |
| `Live` | `Long` | `71.15` | 50,590,000.00 USD | 0.00 USD | 64,890.00 USD | `-25.97%` | `912.05` |
| `Live` | `Long` | `71.25` | 50,520,000.00 USD | 0.00 USD | 8,380.00 USD | `-25.86%` | `117.62` |
| `Live` | `Long` | `71.35` | 50,510,000.00 USD | 0.00 USD | 351.76 USD | `-25.76%` | `4.93` |
| `Live` | `Long` | `71.45` | 50,510,000.00 USD | 0.00 USD | 17,590.00 USD | `-25.65%` | `246.20` |
| `Live` | `Long` | `71.55` | 50,500,000.00 USD | 0.00 USD | 47,190.00 USD | `-25.55%` | `659.55` |
| `Live` | `Long` | `71.65` | 50,450,000.00 USD | 0.00 USD | 11,910.00 USD | `-25.45%` | `166.19` |
| `Live` | `Long` | `71.75` | 50,440,000.00 USD | 0.00 USD | 29,930.00 USD | `-25.34%` | `417.10` |
| `Live` | `Long` | `71.85` | 50,410,000.00 USD | 0.00 USD | 40,080.00 USD | `-25.24%` | `557.79` |
| `Live` | `Long` | `71.95` | 50,370,000.00 USD | 0.00 USD | 12,430.00 USD | `-25.13%` | `172.81` |
| `Live` | `Long` | `72.05` | 50,350,000.00 USD | 0.00 USD | 11,420.00 USD | `-25.03%` | `158.54` |
| `Live` | `Long` | `72.15` | 50,340,000.00 USD | 0.00 USD | 158,970.00 USD | `-24.93%` | `2,203.39` |
| `Live` | `Long` | `72.25` | 50,180,000.00 USD | 0.00 USD | 41,150.00 USD | `-24.82%` | `569.59` |
| `Live` | `Long` | `72.35` | 50,140,000.00 USD | 0.00 USD | 507,050.00 USD | `-24.72%` | `7,008.30` |
| `Live` | `Long` | `72.45` | 49,630,000.00 USD | 0.00 USD | 5,140.00 USD | `-24.61%` | `70.89` |
| `Live` | `Long` | `72.55` | 49,630,000.00 USD | 0.00 USD | 12,640.00 USD | `-24.51%` | `174.19` |
| `Live` | `Long` | `72.65` | 49,620,000.00 USD | 0.00 USD | 7,030.00 USD | `-24.40%` | `96.83` |
| `Live` | `Long` | `72.75` | 49,610,000.00 USD | 0.00 USD | 24,880.00 USD | `-24.30%` | `342.03` |
| `Live` | `Long` | `72.85` | 49,590,000.00 USD | 0.00 USD | 24,660.00 USD | `-24.20%` | `338.52` |
| `Live` | `Long` | `72.95` | 49,560,000.00 USD | 0.00 USD | 8,140.00 USD | `-24.09%` | `111.64` |
| `Live` | `Long` | `73.05` | 49,550,000.00 USD | 0.00 USD | 6,710.00 USD | `-23.99%` | `91.92` |
| `Live` | `Long` | `73.15` | 49,550,000.00 USD | 0.00 USD | 94,110.00 USD | `-23.88%` | `1,286.52` |
| `Live` | `Long` | `73.25` | 49,450,000.00 USD | 0.00 USD | 39,050.00 USD | `-23.78%` | `533.09` |
| `Live` | `Long` | `73.35` | 49,410,000.00 USD | 0.00 USD | 12,760.00 USD | `-23.68%` | `173.95` |
| `Live` | `Long` | `73.45` | 49,400,000.00 USD | 0.00 USD | 22,160.00 USD | `-23.57%` | `301.68` |
| `Live` | `Long` | `73.55` | 49,380,000.00 USD | 0.00 USD | 22,620.00 USD | `-23.47%` | `307.59` |
| `Live` | `Long` | `73.65` | 49,360,000.00 USD | 0.00 USD | 102,150.00 USD | `-23.36%` | `1,386.92` |
| `Live` | `Long` | `73.75` | 49,250,000.00 USD | 0.00 USD | 65,320.00 USD | `-23.26%` | `885.75` |
| `Live` | `Long` | `73.85` | 49,190,000.00 USD | 0.00 USD | 11,750.00 USD | `-23.16%` | `159.12` |
| `Live` | `Long` | `73.95` | 49,180,000.00 USD | 0.00 USD | 40,280.00 USD | `-23.05%` | `544.63` |
| `Live` | `Long` | `74.05` | 49,140,000.00 USD | 0.00 USD | 25,370.00 USD | `-22.95%` | `342.62` |
| `Live` | `Long` | `74.15` | 49,110,000.00 USD | 0.00 USD | 6,390.00 USD | `-22.84%` | `86.21` |
| `Live` | `Long` | `74.25` | 49,100,000.00 USD | 0.00 USD | 46,240.00 USD | `-22.74%` | `622.80` |
| `Live` | `Long` | `74.35` | 49,060,000.00 USD | 0.00 USD | 36,220.00 USD | `-22.64%` | `487.18` |
| `Live` | `Long` | `74.45` | 49,020,000.00 USD | 0.00 USD | 14,530.00 USD | `-22.53%` | `195.10` |
| `Live` | `Long` | `74.55` | 49,010,000.00 USD | 0.00 USD | 2,000.00 USD | `-22.43%` | `26.83` |
| `Live` | `Long` | `74.65` | 49,000,000.00 USD | 0.00 USD | 1,570.00 USD | `-22.32%` | `21.00` |
| `Live` | `Long` | `74.75` | 49,000,000.00 USD | 0.00 USD | 37,430.00 USD | `-22.22%` | `500.69` |
| `Live` | `Long` | `74.85` | 48,970,000.00 USD | 0.00 USD | 130,140.00 USD | `-22.12%` | `1,738.65` |
| `Live` | `Long` | `74.95` | 48,840,000.00 USD | 0.00 USD | 17,870.00 USD | `-22.01%` | `238.41` |
| `Live` | `Long` | `75.05` | 48,820,000.00 USD | 0.00 USD | 46,460.00 USD | `-21.91%` | `619.12` |
| `Live` | `Long` | `75.15` | 48,770,000.00 USD | 0.00 USD | 6,180.00 USD | `-21.80%` | `82.23` |
| `Live` | `Long` | `75.25` | 48,770,000.00 USD | 0.00 USD | 16,870.00 USD | `-21.70%` | `224.21` |
| `Live` | `Long` | `75.35` | 48,750,000.00 USD | 0.00 USD | 37,330.00 USD | `-21.60%` | `495.43` |
| `Live` | `Long` | `75.45` | 48,710,000.00 USD | 0.00 USD | 3,370.00 USD | `-21.49%` | `44.65` |
| `Live` | `Long` | `75.55` | 48,710,000.00 USD | 0.00 USD | 32,450.00 USD | `-21.39%` | `429.56` |
| `Live` | `Long` | `75.65` | 48,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-21.28%` | `22,196.95` |
| `Live` | `Long` | `75.75` | 47,000,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-21.18%` | `22,665.48` |
| `Live` | `Long` | `75.85` | 45,280,000.00 USD | 0.00 USD | 15,170.00 USD | `-21.08%` | `200.02` |
| `Live` | `Long` | `75.95` | 45,260,000.00 USD | 0.00 USD | 14,860.00 USD | `-20.97%` | `195.72` |
| `Live` | `Long` | `76.05` | 45,250,000.00 USD | 0.00 USD | 10,650.00 USD | `-20.87%` | `140.10` |
| `Live` | `Long` | `76.15` | 45,240,000.00 USD | 0.00 USD | 7,890.00 USD | `-20.76%` | `103.56` |
| `Live` | `Long` | `76.25` | 45,230,000.00 USD | 0.00 USD | 9,000.00 USD | `-20.66%` | `118.08` |
| `Live` | `Long` | `76.35` | 45,220,000.00 USD | 0.00 USD | 39,070.00 USD | `-20.55%` | `511.74` |
| `Live` | `Long` | `76.45` | 45,180,000.00 USD | 0.00 USD | 1,090.00 USD | `-20.45%` | `14.30` |
| `Live` | `Long` | `76.55` | 45,180,000.00 USD | 0.00 USD | 26,470.00 USD | `-20.35%` | `345.84` |
| `Live` | `Long` | `76.65` | 45,150,000.00 USD | 0.00 USD | 3,990.00 USD | `-20.24%` | `52.03` |
| `Live` | `Long` | `76.75` | 45,150,000.00 USD | 0.00 USD | 37,790.00 USD | `-20.14%` | `492.42` |
| `Live` | `Long` | `76.85` | 45,110,000.00 USD | 0.00 USD | 302,800.00 USD | `-20.03%` | `3,940.10` |
| `Live` | `Long` | `76.95` | 44,810,000.00 USD | 0.00 USD | 29,880.00 USD | `-19.93%` | `388.24` |
| `Live` | `Long` | `77.05` | 44,780,000.00 USD | 0.00 USD | 27,740.00 USD | `-19.83%` | `360.04` |
| `Live` | `Long` | `77.15` | 44,750,000.00 USD | 0.00 USD | 78,560.00 USD | `-19.72%` | `1,018.23` |
| `Live` | `Long` | `77.25` | 44,670,000.00 USD | 0.00 USD | 23,850.00 USD | `-19.62%` | `308.75` |
| `Live` | `Long` | `77.35` | 44,650,000.00 USD | 0.00 USD | 4,390.00 USD | `-19.51%` | `56.80` |
| `Live` | `Long` | `77.45` | 44,650,000.00 USD | 0.00 USD | 22,240.00 USD | `-19.41%` | `287.18` |
| `Live` | `Long` | `77.55` | 44,620,000.00 USD | 0.00 USD | 8,270.00 USD | `-19.31%` | `106.58` |
| `Live` | `Long` | `77.65` | 44,620,000.00 USD | 0.00 USD | 217,510.00 USD | `-19.20%` | `2,801.21` |
| `Live` | `Long` | `77.75` | 44,400,000.00 USD | 0.00 USD | 357,790.00 USD | `-19.10%` | `4,601.80` |
| `Live` | `Long` | `77.85` | 44,040,000.00 USD | 0.00 USD | 30,120.00 USD | `-18.99%` | `386.89` |
| `Live` | `Long` | `77.95` | 44,010,000.00 USD | 0.00 USD | 21,290.00 USD | `-18.89%` | `273.13` |
| `Live` | `Long` | `78.05` | 43,990,000.00 USD | 0.00 USD | 17,080.00 USD | `-18.79%` | `218.87` |
| `Live` | `Long` | `78.15` | 43,970,000.00 USD | 0.00 USD | 66,520.00 USD | `-18.68%` | `851.19` |
| `Live` | `Long` | `78.25` | 43,900,000.00 USD | 0.00 USD | 23,450.00 USD | `-18.58%` | `299.71` |
| `Live` | `Long` | `78.35` | 43,880,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-18.47%` | `16,505.70` |
| `Live` | `Long` | `78.45` | 42,590,000.00 USD | 0.00 USD | 34,110.00 USD | `-18.37%` | `434.78` |
| `Live` | `Long` | `78.55` | 42,550,000.00 USD | 0.00 USD | 521,930.00 USD | `-18.27%` | `6,644.58` |
| `Live` | `Long` | `78.65` | 42,030,000.00 USD | 0.00 USD | 4,010.00 USD | `-18.16%` | `50.99` |
| `Live` | `Long` | `78.75` | 42,030,000.00 USD | 0.00 USD | 68,860.00 USD | `-18.06%` | `874.42` |
| `Live` | `Long` | `78.85` | 41,960,000.00 USD | 0.00 USD | 4,860.00 USD | `-17.95%` | `61.61` |
| `Live` | `Long` | `78.95` | 41,950,000.00 USD | 0.00 USD | 2,260.00 USD | `-17.85%` | `28.67` |
| `Live` | `Long` | `79.05` | 41,950,000.00 USD | 0.00 USD | 2,820.00 USD | `-17.75%` | `35.64` |
| `Live` | `Long` | `79.15` | 41,950,000.00 USD | 0.00 USD | 619,090.00 USD | `-17.64%` | `7,821.79` |
| `Live` | `Long` | `79.25` | 41,330,000.00 USD | 0.00 USD | 143,470.00 USD | `-17.54%` | `1,810.33` |
| `Live` | `Long` | `79.35` | 41,190,000.00 USD | 0.00 USD | 29,540.00 USD | `-17.43%` | `372.30` |
| `Live` | `Long` | `79.45` | 41,160,000.00 USD | 0.00 USD | 15,890.00 USD | `-17.33%` | `199.97` |
| `Live` | `Long` | `79.55` | 41,140,000.00 USD | 0.00 USD | 330.93 USD | `-17.23%` | `4.16` |
| `Live` | `Long` | `79.65` | 41,140,000.00 USD | 0.00 USD | 28,820.00 USD | `-17.12%` | `361.88` |
| `Live` | `Long` | `79.75` | 41,110,000.00 USD | 0.00 USD | 989.70 USD | `-17.02%` | `12.41` |
| `Live` | `Long` | `79.85` | 41,110,000.00 USD | 0.00 USD | 21,470.00 USD | `-16.91%` | `268.90` |
| `Live` | `Long` | `79.95` | 41,090,000.00 USD | 0.00 USD | 3,760.00 USD | `-16.81%` | `46.99` |
| `Live` | `Long` | `80.15` | 41,090,000.00 USD | 0.00 USD | 23,880.00 USD | `-16.60%` | `297.96` |
| `Live` | `Long` | `80.25` | 41,060,000.00 USD | 0.00 USD | 73,460.00 USD | `-16.50%` | `915.36` |
| `Live` | `Long` | `80.35` | 40,990,000.00 USD | 0.00 USD | 180,870.00 USD | `-16.39%` | `2,251.08` |
| `Live` | `Long` | `80.45` | 40,810,000.00 USD | 0.00 USD | 2,870.00 USD | `-16.29%` | `35.64` |
| `Live` | `Long` | `80.55` | 40,810,000.00 USD | 0.00 USD | 5,580.00 USD | `-16.18%` | `69.28` |
| `Live` | `Long` | `80.65` | 40,800,000.00 USD | 0.00 USD | 4,710.00 USD | `-16.08%` | `58.46` |
| `Live` | `Long` | `80.75` | 40,790,000.00 USD | 0.00 USD | 3,200.00 USD | `-15.98%` | `39.58` |
| `Live` | `Long` | `80.85` | 40,790,000.00 USD | 0.00 USD | 36,100.00 USD | `-15.87%` | `446.52` |
| `Live` | `Long` | `80.95` | 40,760,000.00 USD | 0.00 USD | 3,550.00 USD | `-15.77%` | `43.91` |
| `Live` | `Long` | `81.05` | 40,750,000.00 USD | 0.00 USD | 2,240,000.00 USD | `-15.66%` | `27,634.13` |
| `Live` | `Long` | `81.15` | 38,510,000.00 USD | 0.00 USD | 43,680.00 USD | `-15.56%` | `538.22` |
| `Live` | `Long` | `81.25` | 38,470,000.00 USD | 0.00 USD | 38,330.00 USD | `-15.46%` | `471.76` |
| `Live` | `Long` | `81.35` | 38,430,000.00 USD | 0.00 USD | 82,790.00 USD | `-15.35%` | `1,017.76` |
| `Live` | `Long` | `81.45` | 38,350,000.00 USD | 0.00 USD | 783,730.00 USD | `-15.25%` | `9,622.22` |
| `Live` | `Long` | `81.55` | 37,560,000.00 USD | 0.00 USD | 22,300.00 USD | `-15.14%` | `273.45` |
| `Live` | `Long` | `81.65` | 37,540,000.00 USD | 0.00 USD | 27,160.00 USD | `-15.04%` | `332.60` |
| `Live` | `Long` | `81.75` | 37,510,000.00 USD | 0.00 USD | 64,950.00 USD | `-14.94%` | `794.48` |
| `Live` | `Long` | `81.85` | 37,450,000.00 USD | 0.00 USD | 41,470.00 USD | `-14.83%` | `506.65` |
| `Live` | `Long` | `81.95` | 37,410,000.00 USD | 0.00 USD | 14,790.00 USD | `-14.73%` | `180.50` |
| `Live` | `Long` | `82.05` | 37,390,000.00 USD | 0.00 USD | 127,690.00 USD | `-14.62%` | `1,556.22` |
| `Live` | `Long` | `82.15` | 37,270,000.00 USD | 0.00 USD | 799,480.00 USD | `-14.52%` | `9,732.01` |
| `Live` | `Long` | `82.25` | 36,470,000.00 USD | 0.00 USD | 19,230.00 USD | `-14.42%` | `233.86` |
| `Live` | `Long` | `82.35` | 36,450,000.00 USD | 0.00 USD | 27,660.00 USD | `-14.31%` | `335.88` |
| `Live` | `Long` | `82.45` | 36,420,000.00 USD | 0.00 USD | 212,490.00 USD | `-14.21%` | `2,577.17` |
| `Live` | `Long` | `82.55` | 36,210,000.00 USD | 0.00 USD | 32,090.00 USD | `-14.10%` | `388.71` |
| `Live` | `Long` | `82.65` | 36,170,000.00 USD | 0.00 USD | 103,500.00 USD | `-14.00%` | `1,252.30` |
| `Live` | `Long` | `82.75` | 36,070,000.00 USD | 0.00 USD | 40,220.00 USD | `-13.90%` | `486.09` |
| `Live` | `Long` | `82.85` | 36,030,000.00 USD | 0.00 USD | 19,850.00 USD | `-13.79%` | `239.60` |
| `Live` | `Long` | `82.95` | 36,010,000.00 USD | 0.00 USD | 46,200.00 USD | `-13.69%` | `556.99` |
| `Live` | `Long` | `83.05` | 35,960,000.00 USD | 0.00 USD | 14,570.00 USD | `-13.58%` | `175.42` |
| `Live` | `Long` | `83.15` | 35,950,000.00 USD | 0.00 USD | 25,050.00 USD | `-13.48%` | `301.25` |
| `Live` | `Long` | `83.25` | 35,920,000.00 USD | 0.00 USD | 15,690.00 USD | `-13.38%` | `188.47` |
| `Live` | `Long` | `83.35` | 35,910,000.00 USD | 0.00 USD | 59,090.00 USD | `-13.27%` | `708.98` |
| `Live` | `Long` | `83.45` | 35,850,000.00 USD | 0.00 USD | 91,070.00 USD | `-13.17%` | `1,091.26` |
| `Live` | `Long` | `83.55` | 35,760,000.00 USD | 0.00 USD | 24,000.00 USD | `-13.06%` | `287.21` |
| `Live` | `Long` | `83.65` | 35,740,000.00 USD | 0.00 USD | 71,200.00 USD | `-12.96%` | `851.15` |
| `Live` | `Long` | `83.75` | 35,660,000.00 USD | 0.00 USD | 77,950.00 USD | `-12.85%` | `930.77` |
| `Live` | `Long` | `83.85` | 35,590,000.00 USD | 0.00 USD | 220,850.00 USD | `-12.75%` | `2,633.92` |
| `Live` | `Long` | `83.95` | 35,370,000.00 USD | 0.00 USD | 32,020.00 USD | `-12.65%` | `381.43` |
| `Live` | `Long` | `84.05` | 35,330,000.00 USD | 0.00 USD | 169,520.00 USD | `-12.54%` | `2,016.94` |
| `Live` | `Long` | `84.15` | 35,160,000.00 USD | 0.00 USD | 80,010.00 USD | `-12.44%` | `950.86` |
| `Live` | `Long` | `84.25` | 35,080,000.00 USD | 0.00 USD | 50,560.00 USD | `-12.33%` | `600.08` |
| `Live` | `Long` | `84.35` | 35,030,000.00 USD | 0.00 USD | 34,210.00 USD | `-12.23%` | `405.56` |
| `Live` | `Long` | `84.45` | 35,000,000.00 USD | 0.00 USD | 83,650.00 USD | `-12.13%` | `990.51` |
| `Live` | `Long` | `84.55` | 34,920,000.00 USD | 0.00 USD | 11,030.00 USD | `-12.02%` | `130.46` |
| `Live` | `Long` | `84.65` | 34,900,000.00 USD | 0.00 USD | 60,340.00 USD | `-11.92%` | `712.77` |
| `Live` | `Long` | `84.75` | 34,840,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-11.81%` | `19,914.51` |
| `Live` | `Long` | `84.85` | 33,160,000.00 USD | 0.00 USD | 11,870.00 USD | `-11.71%` | `139.84` |
| `Live` | `Long` | `84.95` | 33,140,000.00 USD | 0.00 USD | 125,170.00 USD | `-11.61%` | `1,473.46` |
| `Live` | `Long` | `85.05` | 33,020,000.00 USD | 0.00 USD | 83,020.00 USD | `-11.50%` | `976.13` |
| `Live` | `Long` | `85.15` | 32,940,000.00 USD | 0.00 USD | 1,730.00 USD | `-11.40%` | `20.29` |
| `Live` | `Long` | `85.25` | 32,930,000.00 USD | 0.00 USD | 561,670.00 USD | `-11.29%` | `6,588.50` |
| `Live` | `Long` | `85.35` | 32,370,000.00 USD | 0.00 USD | 33,390.00 USD | `-11.19%` | `391.16` |
| `Live` | `Long` | `85.45` | 32,340,000.00 USD | 0.00 USD | 26,990.00 USD | `-11.09%` | `315.84` |
| `Live` | `Long` | `85.55` | 32,310,000.00 USD | 0.00 USD | 10,720.00 USD | `-10.98%` | `125.29` |
| `Live` | `Long` | `85.65` | 32,300,000.00 USD | 0.00 USD | 64,670.00 USD | `-10.88%` | `755.04` |
| `Live` | `Long` | `85.75` | 32,240,000.00 USD | 0.00 USD | 9,040.00 USD | `-10.77%` | `105.43` |
| `Live` | `Long` | `85.85` | 32,230,000.00 USD | 0.00 USD | 38,890.00 USD | `-10.67%` | `453.02` |
| `Live` | `Long` | `85.95` | 32,190,000.00 USD | 0.00 USD | 33,670.00 USD | `-10.57%` | `391.69` |
| `Live` | `Long` | `86.05` | 32,160,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-10.46%` | `14,979.71` |
| `Live` | `Long` | `86.15` | 30,870,000.00 USD | 0.00 USD | 135,160.00 USD | `-10.36%` | `1,568.87` |
| `Live` | `Long` | `86.25` | 30,730,000.00 USD | 0.00 USD | 102,400.00 USD | `-10.25%` | `1,187.24` |
| `Live` | `Long` | `86.35` | 30,630,000.00 USD | 0.00 USD | 323.81 USD | `-10.15%` | `3.75` |
| `Live` | `Long` | `86.45` | 30,630,000.00 USD | 0.00 USD | 44,940.00 USD | `-10.05%` | `519.82` |
| `Live` | `Long` | `86.55` | 30,580,000.00 USD | 0.00 USD | 48,900.00 USD | `-9.94%` | `565.01` |
| `Live` | `Long` | `86.65` | 30,530,000.00 USD | 0.00 USD | 155,550.00 USD | `-9.84%` | `1,795.10` |
| `Live` | `Long` | `86.75` | 30,380,000.00 USD | 0.00 USD | 24,170.00 USD | `-9.73%` | `278.58` |
| `Live` | `Long` | `86.85` | 30,350,000.00 USD | 0.00 USD | 56,980.00 USD | `-9.63%` | `656.08` |
| `Live` | `Long` | `86.95` | 30,300,000.00 USD | 0.00 USD | 79,240.00 USD | `-9.53%` | `911.33` |
| `Live` | `Long` | `87.05` | 30,220,000.00 USD | 0.00 USD | 246,250.00 USD | `-9.42%` | `2,828.89` |
| `Live` | `Long` | `87.15` | 29,970,000.00 USD | 0.00 USD | 260,410.00 USD | `-9.32%` | `2,988.05` |
| `Live` | `Long` | `87.25` | 29,710,000.00 USD | 0.00 USD | 21,370.00 USD | `-9.21%` | `244.90` |
| `Live` | `Long` | `87.35` | 29,690,000.00 USD | 0.00 USD | 189,640.00 USD | `-9.11%` | `2,171.05` |
| `Live` | `Long` | `87.45` | 29,500,000.00 USD | 0.00 USD | 531,360.00 USD | `-9.00%` | `6,076.13` |
| `Live` | `Long` | `87.55` | 28,970,000.00 USD | 0.00 USD | 220,040.00 USD | `-8.90%` | `2,513.36` |
| `Live` | `Long` | `87.65` | 28,750,000.00 USD | 0.00 USD | 460,370.00 USD | `-8.80%` | `5,252.36` |
| `Live` | `Long` | `87.75` | 28,290,000.00 USD | 0.00 USD | 1,220.00 USD | `-8.69%` | `13.87` |
| `Live` | `Long` | `87.85` | 28,290,000.00 USD | 0.00 USD | 9,490.00 USD | `-8.59%` | `108.04` |
| `Live` | `Long` | `87.95` | 28,280,000.00 USD | 0.00 USD | 9,640.00 USD | `-8.48%` | `109.61` |
| `Live` | `Long` | `88.05` | 28,270,000.00 USD | 0.00 USD | 39,460.00 USD | `-8.38%` | `448.15` |
| `Live` | `Long` | `88.15` | 28,230,000.00 USD | 0.00 USD | 18,880.00 USD | `-8.28%` | `214.22` |
| `Live` | `Long` | `88.25` | 28,210,000.00 USD | 0.00 USD | 83,470.00 USD | `-8.17%` | `945.89` |
| `Live` | `Long` | `88.35` | 28,130,000.00 USD | 0.00 USD | 49,150.00 USD | `-8.07%` | `556.32` |
| `Live` | `Long` | `88.45` | 28,080,000.00 USD | 0.00 USD | 79,830.00 USD | `-7.96%` | `902.52` |
| `Live` | `Long` | `88.55` | 28,000,000.00 USD | 0.00 USD | 242,790.00 USD | `-7.86%` | `2,741.88` |
| `Live` | `Long` | `88.65` | 27,760,000.00 USD | 0.00 USD | 27,500.00 USD | `-7.76%` | `310.23` |
| `Live` | `Long` | `88.75` | 27,730,000.00 USD | 0.00 USD | 130,590.00 USD | `-7.65%` | `1,471.43` |
| `Live` | `Long` | `88.85` | 27,600,000.00 USD | 0.00 USD | 23,370.00 USD | `-7.55%` | `262.98` |
| `Live` | `Long` | `88.95` | 27,570,000.00 USD | 0.00 USD | 259,400.00 USD | `-7.44%` | `2,916.27` |
| `Live` | `Long` | `89.05` | 27,310,000.00 USD | 0.00 USD | 52,590.00 USD | `-7.34%` | `590.58` |
| `Live` | `Long` | `89.15` | 27,260,000.00 USD | 0.00 USD | 15,510.00 USD | `-7.24%` | `174.02` |
| `Live` | `Long` | `89.25` | 27,250,000.00 USD | 0.00 USD | 41,380.00 USD | `-7.13%` | `463.65` |
| `Live` | `Long` | `89.35` | 27,200,000.00 USD | 0.00 USD | 18,740.00 USD | `-7.03%` | `209.73` |
| `Live` | `Long` | `89.45` | 27,190,000.00 USD | 0.00 USD | 52,650.00 USD | `-6.92%` | `588.58` |
| `Live` | `Long` | `89.55` | 27,130,000.00 USD | 0.00 USD | 25,560.00 USD | `-6.82%` | `285.40` |
| `Live` | `Long` | `89.65` | 27,110,000.00 USD | 0.00 USD | 16,210.00 USD | `-6.72%` | `180.80` |
| `Live` | `Long` | `89.75` | 27,090,000.00 USD | 0.00 USD | 68,900.00 USD | `-6.61%` | `767.65` |
| `Live` | `Long` | `89.85` | 27,020,000.00 USD | 0.00 USD | 56,790.00 USD | `-6.51%` | `632.04` |
| `Live` | `Long` | `89.95` | 26,970,000.00 USD | 0.00 USD | 150,160.00 USD | `-6.40%` | `1,669.33` |
| `Live` | `Long` | `90.05` | 26,820,000.00 USD | 0.00 USD | 310,590.00 USD | `-6.30%` | `3,449.08` |
| `Live` | `Long` | `90.15` | 26,510,000.00 USD | 0.00 USD | 28,210.00 USD | `-6.20%` | `312.94` |
| `Live` | `Long` | `90.25` | 26,480,000.00 USD | 0.00 USD | 52,860.00 USD | `-6.09%` | `585.70` |
| `Live` | `Long` | `90.35` | 26,420,000.00 USD | 0.00 USD | 31,850.00 USD | `-5.99%` | `352.54` |
| `Live` | `Long` | `90.45` | 26,390,000.00 USD | 0.00 USD | 9,870.00 USD | `-5.88%` | `109.09` |
| `Live` | `Long` | `90.55` | 26,380,000.00 USD | 0.00 USD | 23,760.00 USD | `-5.78%` | `262.38` |
| `Live` | `Long` | `90.65` | 26,360,000.00 USD | 0.00 USD | 79,210.00 USD | `-5.68%` | `873.79` |
| `Live` | `Long` | `90.75` | 26,280,000.00 USD | 0.00 USD | 64,910.00 USD | `-5.57%` | `715.23` |
| `Live` | `Long` | `90.85` | 26,210,000.00 USD | 0.00 USD | 111,640.00 USD | `-5.47%` | `1,228.87` |
| `Live` | `Long` | `90.95` | 26,100,000.00 USD | 0.00 USD | 267,140.00 USD | `-5.36%` | `2,937.26` |
| `Live` | `Long` | `91.05` | 25,840,000.00 USD | 0.00 USD | 439,360.00 USD | `-5.26%` | `4,825.44` |
| `Live` | `Long` | `91.15` | 25,400,000.00 USD | 0.00 USD | 278,840.00 USD | `-5.15%` | `3,059.17` |
| `Live` | `Long` | `91.25` | 25,120,000.00 USD | 0.00 USD | 21,060.00 USD | `-5.05%` | `230.81` |
| `Live` | `Long` | `91.35` | 25,100,000.00 USD | 0.00 USD | 152,860.00 USD | `-4.95%` | `1,673.35` |
| `Live` | `Long` | `91.45` | 24,940,000.00 USD | 0.00 USD | 34,870.00 USD | `-4.84%` | `381.28` |
| `Live` | `Long` | `91.55` | 24,910,000.00 USD | 0.00 USD | 2,450,000.00 USD | `-4.74%` | `26,800.61` |
| `Live` | `Long` | `91.65` | 22,460,000.00 USD | 0.00 USD | 45,140.00 USD | `-4.63%` | `492.51` |
| `Live` | `Long` | `91.75` | 22,410,000.00 USD | 0.00 USD | 361,750.00 USD | `-4.53%` | `3,942.77` |
| `Live` | `Long` | `91.85` | 22,050,000.00 USD | 0.00 USD | 27,090.00 USD | `-4.43%` | `294.97` |
| `Live` | `Long` | `91.95` | 22,020,000.00 USD | 0.00 USD | 145,240.00 USD | `-4.32%` | `1,579.59` |
| `Live` | `Long` | `92.05` | 21,880,000.00 USD | 0.00 USD | 15,920.00 USD | `-4.22%` | `172.92` |
| `Live` | `Long` | `92.15` | 21,860,000.00 USD | 0.00 USD | 299,200.00 USD | `-4.11%` | `3,246.85` |
| `Live` | `Long` | `92.25` | 21,560,000.00 USD | 0.00 USD | 107,850.00 USD | `-4.01%` | `1,169.12` |
| `Live` | `Long` | `92.35` | 21,450,000.00 USD | 0.00 USD | 194,290.00 USD | `-3.91%` | `2,103.87` |
| `Live` | `Long` | `92.45` | 21,260,000.00 USD | 0.00 USD | 107,230.00 USD | `-3.80%` | `1,159.82` |
| `Live` | `Long` | `92.55` | 21,150,000.00 USD | 0.00 USD | 317,480.00 USD | `-3.70%` | `3,430.31` |
| `Live` | `Long` | `92.65` | 20,830,000.00 USD | 0.00 USD | 218,230.00 USD | `-3.59%` | `2,355.47` |
| `Live` | `Long` | `92.75` | 20,620,000.00 USD | 0.00 USD | 608,070.00 USD | `-3.49%` | `6,555.99` |
| `Live` | `Long` | `92.85` | 20,010,000.00 USD | 0.00 USD | 484,570.00 USD | `-3.39%` | `5,218.88` |
| `Live` | `Long` | `92.95` | 19,520,000.00 USD | 0.00 USD | 21,840.00 USD | `-3.28%` | `234.97` |
| `Live` | `Long` | `93.05` | 19,500,000.00 USD | 0.00 USD | 47,480.00 USD | `-3.18%` | `510.21` |
| `Live` | `Long` | `93.15` | 19,450,000.00 USD | 0.00 USD | 139,650.00 USD | `-3.07%` | `1,499.19` |
| `Live` | `Long` | `93.25` | 19,310,000.00 USD | 0.00 USD | 451,130.00 USD | `-2.97%` | `4,837.84` |
| `Live` | `Long` | `93.35` | 18,860,000.00 USD | 0.00 USD | 153,040.00 USD | `-2.87%` | `1,639.47` |
| `Live` | `Long` | `93.45` | 18,710,000.00 USD | 0.00 USD | 528,000.00 USD | `-2.76%` | `5,650.10` |
| `Live` | `Long` | `93.55` | 18,180,000.00 USD | 0.00 USD | 719,190.00 USD | `-2.66%` | `7,687.79` |
| `Live` | `Long` | `93.65` | 17,460,000.00 USD | 0.00 USD | 145,100.00 USD | `-2.55%` | `1,549.42` |
| `Live` | `Long` | `93.75` | 17,320,000.00 USD | 0.00 USD | 80,060.00 USD | `-2.45%` | `853.92` |
| `Live` | `Long` | `93.85` | 17,240,000.00 USD | 0.00 USD | 36,460.00 USD | `-2.35%` | `388.53` |
| `Live` | `Long` | `93.95` | 17,200,000.00 USD | 0.00 USD | 2,220,000.00 USD | `-2.24%` | `23,576.59` |
| `Live` | `Long` | `94.05` | 14,990,000.00 USD | 0.00 USD | 203,240.00 USD | `-2.14%` | `2,161.01` |
| `Live` | `Long` | `94.15` | 14,780,000.00 USD | 0.00 USD | 35,200.00 USD | `-2.03%` | `373.88` |
| `Live` | `Short` | `94.25` | 36,060.00 USD | 36,060.00 USD | 0.00 USD | `-1.93%` | `382.62` |
| `Live` | `Long` | `94.35` | 14,750,000.00 USD | 0.00 USD | 90,750.00 USD | `-1.83%` | `961.82` |
| `Live` | `Long` | `94.45` | 14,660,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-1.72%` | `11,279.12` |
| `Live` | `Long` | `94.55` | 13,590,000.00 USD | 0.00 USD | 201,770.00 USD | `-1.62%` | `2,133.98` |
| `Live` | `Long` | `94.65` | 13,390,000.00 USD | 0.00 USD | 12,840,000.00 USD | `-1.51%` | `135,613.62` |
| `Live` | `Long` | `94.75` | 553,990.00 USD | 0.00 USD | 93,270.00 USD | `-1.41%` | `984.40` |
| `Live` | `Long` | `94.85` | 460,710.00 USD | 0.00 USD | 40,310.00 USD | `-1.30%` | `424.97` |
| `Live` | `Long` | `94.95` | 420,410.00 USD | 0.00 USD | 233,250.00 USD | `-1.20%` | `2,456.55` |
| `Live` | `Long` | `95.05` | 187,160.00 USD | 0.00 USD | 621.63 USD | `-1.10%` | `6.54` |
| `Live` | `Long` | `95.15` | 186,530.00 USD | 0.00 USD | 13,980.00 USD | `-0.99%` | `146.96` |
| `Live` | `Long` | `95.25` | 172,550.00 USD | 0.00 USD | 13,750.00 USD | `-0.89%` | `144.33` |
| `Live` | `Long` | `95.35` | 158,800.00 USD | 0.00 USD | 31,760.00 USD | `-0.78%` | `333.12` |
| `Live` | `Long` | `95.45` | 127,040.00 USD | 0.00 USD | 3,410.00 USD | `-0.68%` | `35.68` |
| `Live` | `Long` | `95.55` | 123,630.00 USD | 0.00 USD | 44,880.00 USD | `-0.58%` | `469.74` |
| `Live` | `Long` | `95.75` | 78,750.00 USD | 0.00 USD | 2,510.00 USD | `-0.37%` | `26.17` |
| `Live` | `Long` | `95.85` | 76,250.00 USD | 0.00 USD | 7,800.00 USD | `-0.26%` | `81.38` |
| `Live` | `Long` | `95.95` | 68,440.00 USD | 0.00 USD | 1,200.00 USD | `-0.16%` | `12.52` |
| `Live` | `Long` | `96.05` | 67,240.00 USD | 0.00 USD | 67,240.00 USD | `-0.06%` | `700.09` |
| `Live` | `Short` | `96.15` | 44,130.00 USD | 8,070.00 USD | 0.00 USD | `+0.05%` | `83.92` |
| `Live` | `Short` | `96.25` | 64,670.00 USD | 20,540.00 USD | 0.00 USD | `+0.15%` | `213.39` |
| `Live` | `Short` | `96.35` | 93,300.00 USD | 28,630.00 USD | 0.00 USD | `+0.26%` | `297.15` |
| `Live` | `Short` | `96.45` | 95,270.00 USD | 1,970.00 USD | 0.00 USD | `+0.36%` | `20.47` |
| `Live` | `Short` | `96.55` | 159,690.00 USD | 64,410.00 USD | 0.00 USD | `+0.46%` | `667.15` |
| `Live` | `Short` | `96.65` | 165,970.00 USD | 6,280.00 USD | 0.00 USD | `+0.57%` | `64.95` |
| `Live` | `Short` | `96.95` | 168,510.00 USD | 2,540.00 USD | 0.00 USD | `+0.88%` | `26.20` |
| `Live` | `Short` | `97.15` | 177,370.00 USD | 8,870.00 USD | 0.00 USD | `+1.09%` | `91.30` |
| `Live` | `Short` | `97.25` | 181,250.00 USD | 3,880.00 USD | 0.00 USD | `+1.19%` | `39.86` |
| `Live` | `Short` | `97.45` | 207,960.00 USD | 26,710.00 USD | 0.00 USD | `+1.40%` | `274.08` |
| `Live` | `Short` | `97.55` | 337,380.00 USD | 129,410.00 USD | 0.00 USD | `+1.50%` | `1,326.65` |
| `Live` | `Short` | `97.65` | 337,530.00 USD | 150.38 USD | 0.00 USD | `+1.61%` | `1.54` |
| `Live` | `Short` | `97.75` | 347,060.00 USD | 9,530.00 USD | 0.00 USD | `+1.71%` | `97.49` |
| `Live` | `Short` | `97.85` | 352,810.00 USD | 5,760.00 USD | 0.00 USD | `+1.82%` | `58.86` |
| `Live` | `Short` | `97.95` | 352,960.00 USD | 145.95 USD | 0.00 USD | `+1.92%` | `1.49` |
| `Live` | `Short` | `98.05` | 358,050.00 USD | 5,090.00 USD | 0.00 USD | `+2.02%` | `51.87` |
| `Live` | `Short` | `98.15` | 362,220.00 USD | 4,170.00 USD | 0.00 USD | `+2.13%` | `42.48` |
| `Live` | `Short` | `98.25` | 365,590.00 USD | 3,370.00 USD | 0.00 USD | `+2.23%` | `34.31` |
| `Live` | `Short` | `98.45` | 396,510.00 USD | 30,920.00 USD | 0.00 USD | `+2.44%` | `314.10` |
| `Live` | `Short` | `98.55` | 500,010.00 USD | 103,500.00 USD | 0.00 USD | `+2.55%` | `1,050.27` |
| `Live` | `Short` | `98.65` | 507,250.00 USD | 7,240.00 USD | 0.00 USD | `+2.65%` | `73.38` |
| `Live` | `Short` | `98.75` | 529,250.00 USD | 21,990.00 USD | 0.00 USD | `+2.75%` | `222.72` |
| `Live` | `Short` | `98.85` | 576,310.00 USD | 47,060.00 USD | 0.00 USD | `+2.86%` | `476.11` |
| `Live` | `Short` | `98.95` | 943,890.00 USD | 367,580.00 USD | 0.00 USD | `+2.96%` | `3,714.84` |
| `Live` | `Short` | `99.05` | 1,020,000.00 USD | 77,860.00 USD | 0.00 USD | `+3.07%` | `786.07` |
| `Live` | `Short` | `99.15` | 1,030,000.00 USD | 7,810.00 USD | 0.00 USD | `+3.17%` | `78.77` |
| `Live` | `Short` | `99.25` | 2,470,000.00 USD | 1,440,000.00 USD | 0.00 USD | `+3.27%` | `14,512.93` |
| `Live` | `Short` | `99.35` | 2,540,000.00 USD | 70,900.00 USD | 0.00 USD | `+3.38%` | `713.65` |
| `Live` | `Short` | `99.45` | 2,570,000.00 USD | 33,870.00 USD | 0.00 USD | `+3.48%` | `340.58` |
| `Live` | `Short` | `99.55` | 2,800,000.00 USD | 228,670.00 USD | 0.00 USD | `+3.59%` | `2,297.08` |
| `Live` | `Short` | `99.65` | 2,860,000.00 USD | 56,710.00 USD | 0.00 USD | `+3.69%` | `569.13` |
| `Live` | `Short` | `99.75` | 2,870,000.00 USD | 12,030.00 USD | 0.00 USD | `+3.79%` | `120.61` |
| `Live` | `Short` | `100.05` | 2,870,000.00 USD | 446.22 USD | 0.00 USD | `+4.11%` | `4.46` |
| `Live` | `Short` | `100.15` | 2,880,000.00 USD | 5,900.00 USD | 0.00 USD | `+4.21%` | `58.91` |
| `Live` | `Short` | `100.25` | 2,890,000.00 USD | 13,960.00 USD | 0.00 USD | `+4.31%` | `139.21` |
| `Live` | `Short` | `100.35` | 2,910,000.00 USD | 19,540.00 USD | 0.00 USD | `+4.42%` | `194.72` |
| `Live` | `Short` | `100.75` | 2,920,000.00 USD | 12,140.00 USD | 0.00 USD | `+4.83%` | `120.47` |
| `Live` | `Short` | `100.85` | 2,930,000.00 USD | 10,250.00 USD | 0.00 USD | `+4.94%` | `101.66` |
| `Live` | `Short` | `100.95` | 2,950,000.00 USD | 19,560.00 USD | 0.00 USD | `+5.04%` | `193.78` |
| `Live` | `Short` | `101.05` | 2,960,000.00 USD | 8,440.00 USD | 0.00 USD | `+5.15%` | `83.53` |
| `Live` | `Short` | `101.15` | 2,960,000.00 USD | 438.99 USD | 0.00 USD | `+5.25%` | `4.34` |
| `Live` | `Short` | `101.45` | 2,960,000.00 USD | 876.53 USD | 0.00 USD | `+5.56%` | `8.64` |
| `Live` | `Short` | `101.55` | 2,960,000.00 USD | 814.43 USD | 0.00 USD | `+5.67%` | `8.02` |
| `Live` | `Short` | `101.65` | 2,970,000.00 USD | 1,820.00 USD | 0.00 USD | `+5.77%` | `17.95` |
| `Live` | `Short` | `101.75` | 3,030,000.00 USD | 59,180.00 USD | 0.00 USD | `+5.87%` | `581.63` |
| `Live` | `Short` | `102.05` | 3,030,000.00 USD | 4,690.00 USD | 0.00 USD | `+6.19%` | `45.92` |
| `Live` | `Short` | `102.55` | 3,040,000.00 USD | 8,080.00 USD | 0.00 USD | `+6.71%` | `78.75` |
| `Live` | `Short` | `102.75` | 3,040,000.00 USD | 182.90 USD | 0.00 USD | `+6.92%` | `1.78` |
| `Live` | `Short` | `102.85` | 3,050,000.00 USD | 9,640.00 USD | 0.00 USD | `+7.02%` | `93.72` |
| `Live` | `Short` | `102.95` | 3,050,000.00 USD | 3,080.00 USD | 0.00 USD | `+7.12%` | `29.92` |
| `Live` | `Short` | `103.05` | 3,060,000.00 USD | 4,520.00 USD | 0.00 USD | `+7.23%` | `43.84` |
| `Live` | `Short` | `103.15` | 3,060,000.00 USD | 323.89 USD | 0.00 USD | `+7.33%` | `3.14` |
| `Live` | `Short` | `103.35` | 3,570,000.00 USD | 517,280.00 USD | 0.00 USD | `+7.54%` | `5,005.13` |
| `Live` | `Short` | `103.55` | 3,580,000.00 USD | 8,500.00 USD | 0.00 USD | `+7.75%` | `82.05` |
| `Live` | `Short` | `103.75` | 3,610,000.00 USD | 29,780.00 USD | 0.00 USD | `+7.96%` | `286.99` |
| `Live` | `Short` | `103.85` | 3,650,000.00 USD | 38,270.00 USD | 0.00 USD | `+8.06%` | `368.50` |
| `Live` | `Short` | `104.05` | 3,650,000.00 USD | 545.22 USD | 0.00 USD | `+8.27%` | `5.24` |
| `Live` | `Short` | `104.15` | 3,660,000.00 USD | 10,270.00 USD | 0.00 USD | `+8.37%` | `98.59` |
| `Live` | `Short` | `104.25` | 3,700,000.00 USD | 37,460.00 USD | 0.00 USD | `+8.48%` | `359.31` |
| `Live` | `Short` | `104.35` | 3,700,000.00 USD | 1,540.00 USD | 0.00 USD | `+8.58%` | `14.79` |
| `Live` | `Short` | `104.45` | 3,710,000.00 USD | 12,140.00 USD | 0.00 USD | `+8.68%` | `116.19` |
| `Live` | `Short` | `104.55` | 3,710,000.00 USD | 895.99 USD | 0.00 USD | `+8.79%` | `8.57` |
| `Live` | `Short` | `104.65` | 4,340,000.00 USD | 630,930.00 USD | 0.00 USD | `+8.89%` | `6,028.99` |
| `Live` | `Short` | `104.75` | 4,340,000.00 USD | 849.52 USD | 0.00 USD | `+9.00%` | `8.11` |
| `Live` | `Short` | `104.85` | 4,350,000.00 USD | 7,560.00 USD | 0.00 USD | `+9.10%` | `72.14` |
| `Live` | `Short` | `104.95` | 4,350,000.00 USD | 412.45 USD | 0.00 USD | `+9.20%` | `3.93` |
| `Live` | `Short` | `105.25` | 4,360,000.00 USD | 7,140.00 USD | 0.00 USD | `+9.52%` | `67.86` |
| `Live` | `Short` | `105.35` | 4,470,000.00 USD | 110,930.00 USD | 0.00 USD | `+9.62%` | `1,052.98` |
| `Live` | `Short` | `105.55` | 4,470,000.00 USD | 4,370.00 USD | 0.00 USD | `+9.83%` | `41.37` |
| `Live` | `Short` | `105.65` | 4,480,000.00 USD | 108.82 USD | 0.00 USD | `+9.93%` | `1.03` |
| `Live` | `Short` | `105.85` | 4,490,000.00 USD | 10,550.00 USD | 0.00 USD | `+10.14%` | `99.68` |
| `Live` | `Short` | `105.95` | 4,490,000.00 USD | 2,740.00 USD | 0.00 USD | `+10.25%` | `25.88` |
| `Live` | `Short` | `106.05` | 4,490,000.00 USD | 103.93 USD | 0.00 USD | `+10.35%` | `0.98` |
| `Live` | `Short` | `106.15` | 4,490,000.00 USD | 3,250.00 USD | 0.00 USD | `+10.45%` | `30.65` |
| `Live` | `Short` | `106.45` | 4,490,000.00 USD | 696.18 USD | 0.00 USD | `+10.77%` | `6.54` |
| `Live` | `Short` | `106.65` | 4,490,000.00 USD | 548.18 USD | 0.00 USD | `+10.97%` | `5.14` |
| `Live` | `Short` | `106.85` | 5,040,000.00 USD | 542,740.00 USD | 0.00 USD | `+11.18%` | `5,079.50` |
| `Live` | `Short` | `106.95` | 5,040,000.00 USD | 291.97 USD | 0.00 USD | `+11.29%` | `2.73` |
| `Live` | `Short` | `107.05` | 5,050,000.00 USD | 12,400.00 USD | 0.00 USD | `+11.39%` | `115.88` |
| `Live` | `Short` | `107.15` | 5,080,000.00 USD | 35,540.00 USD | 0.00 USD | `+11.49%` | `331.65` |
| `Live` | `Short` | `107.35` | 5,300,000.00 USD | 212,780.00 USD | 0.00 USD | `+11.70%` | `1,982.14` |
| `Live` | `Short` | `107.45` | 5,420,000.00 USD | 120,310.00 USD | 0.00 USD | `+11.81%` | `1,119.71` |
| `Live` | `Short` | `107.55` | 5,420,000.00 USD | 2,640.00 USD | 0.00 USD | `+11.91%` | `24.55` |
| `Live` | `Short` | `107.65` | 5,420,000.00 USD | 1,560.00 USD | 0.00 USD | `+12.01%` | `14.49` |
| `Live` | `Short` | `107.75` | 5,430,000.00 USD | 5,840.00 USD | 0.00 USD | `+12.12%` | `54.18` |
| `Live` | `Short` | `107.85` | 5,820,000.00 USD | 392,910.00 USD | 0.00 USD | `+12.22%` | `3,643.14` |
| `Live` | `Short` | `108.05` | 5,820,000.00 USD | 1,080.00 USD | 0.00 USD | `+12.43%` | `10.04` |
| `Live` | `Short` | `108.35` | 5,820,000.00 USD | 3,690.00 USD | 0.00 USD | `+12.74%` | `34.03` |
| `Live` | `Short` | `108.45` | 5,930,000.00 USD | 108,940.00 USD | 0.00 USD | `+12.85%` | `1,004.52` |
| `Live` | `Short` | `108.55` | 5,930,000.00 USD | 117.23 USD | 0.00 USD | `+12.95%` | `1.08` |
| `Live` | `Short` | `108.65` | 6,000,000.00 USD | 64,720.00 USD | 0.00 USD | `+13.05%` | `595.69` |
| `Live` | `Short` | `108.75` | 6,000,000.00 USD | 6,370.00 USD | 0.00 USD | `+13.16%` | `58.57` |
| `Live` | `Short` | `108.85` | 6,010,000.00 USD | 3,230.00 USD | 0.00 USD | `+13.26%` | `29.68` |
| `Live` | `Short` | `108.95` | 6,010,000.00 USD | 955.49 USD | 0.00 USD | `+13.37%` | `8.77` |
| `Live` | `Short` | `109.05` | 6,130,000.00 USD | 121,510.00 USD | 0.00 USD | `+13.47%` | `1,114.24` |
| `Live` | `Short` | `109.15` | 6,150,000.00 USD | 22,380.00 USD | 0.00 USD | `+13.57%` | `205.03` |
| `Live` | `Short` | `109.25` | 6,150,000.00 USD | 1,170.00 USD | 0.00 USD | `+13.68%` | `10.74` |
| `Live` | `Short` | `109.35` | 6,160,000.00 USD | 4,600.00 USD | 0.00 USD | `+13.78%` | `42.08` |
| `Live` | `Short` | `109.45` | 6,260,000.00 USD | 103,160.00 USD | 0.00 USD | `+13.89%` | `942.51` |
| `Live` | `Short` | `109.55` | 6,260,000.00 USD | 567.47 USD | 0.00 USD | `+13.99%` | `5.18` |
| `Live` | `Short` | `109.65` | 6,320,000.00 USD | 53,730.00 USD | 0.00 USD | `+14.10%` | `489.97` |
| `Live` | `Short` | `109.85` | 6,320,000.00 USD | 1,020.00 USD | 0.00 USD | `+14.30%` | `9.29` |
| `Live` | `Short` | `109.95` | 6,320,000.00 USD | 794.94 USD | 0.00 USD | `+14.41%` | `7.23` |
| `Live` | `Short` | `110.15` | 6,320,000.00 USD | 194.97 USD | 0.00 USD | `+14.62%` | `1.77` |
| `Live` | `Short` | `110.25` | 6,320,000.00 USD | 218.29 USD | 0.00 USD | `+14.72%` | `1.98` |
| `Live` | `Short` | `110.35` | 6,460,000.00 USD | 143,230.00 USD | 0.00 USD | `+14.82%` | `1,297.94` |
| `Live` | `Short` | `110.45` | 6,480,000.00 USD | 16,940.00 USD | 0.00 USD | `+14.93%` | `153.41` |
| `Live` | `Short` | `110.55` | 6,480,000.00 USD | 203.41 USD | 0.00 USD | `+15.03%` | `1.84` |
| `Live` | `Short` | `110.75` | 6,480,000.00 USD | 3,330.00 USD | 0.00 USD | `+15.24%` | `30.10` |
| `Live` | `Short` | `110.85` | 6,480,000.00 USD | 103.09 USD | 0.00 USD | `+15.34%` | `0.93` |
| `Live` | `Short` | `110.95` | 6,480,000.00 USD | 660.15 USD | 0.00 USD | `+15.45%` | `5.95` |
| `Live` | `Short` | `111.15` | 6,480,000.00 USD | 1,710.00 USD | 0.00 USD | `+15.66%` | `15.37` |
| `Live` | `Short` | `111.35` | 6,740,000.00 USD | 259,330.00 USD | 0.00 USD | `+15.86%` | `2,329.00` |
| `Live` | `Short` | `111.45` | 6,740,000.00 USD | 841.45 USD | 0.00 USD | `+15.97%` | `7.55` |
| `Live` | `Short` | `111.65` | 6,750,000.00 USD | 3,070.00 USD | 0.00 USD | `+16.18%` | `27.53` |
| `Live` | `Short` | `111.75` | 6,750,000.00 USD | 339.72 USD | 0.00 USD | `+16.28%` | `3.04` |
| `Live` | `Short` | `111.85` | 6,760,000.00 USD | 15,880.00 USD | 0.00 USD | `+16.38%` | `141.95` |
| `Live` | `Short` | `111.95` | 6,770,000.00 USD | 2,020.00 USD | 0.00 USD | `+16.49%` | `18.04` |
| `Live` | `Short` | `112.05` | 6,770,000.00 USD | 626.36 USD | 0.00 USD | `+16.59%` | `5.59` |
| `Live` | `Short` | `112.55` | 6,770,000.00 USD | 844.13 USD | 0.00 USD | `+17.11%` | `7.50` |
| `Live` | `Short` | `112.75` | 6,770,000.00 USD | 110.50 USD | 0.00 USD | `+17.32%` | `0.98` |
| `Live` | `Short` | `112.85` | 6,770,000.00 USD | 3,540.00 USD | 0.00 USD | `+17.42%` | `31.34` |
| `Live` | `Short` | `113.05` | 6,770,000.00 USD | 406.98 USD | 0.00 USD | `+17.63%` | `3.60` |
| `Live` | `Short` | `113.15` | 6,780,000.00 USD | 9,560.00 USD | 0.00 USD | `+17.74%` | `84.51` |
| `Live` | `Short` | `113.25` | 6,810,000.00 USD | 24,630.00 USD | 0.00 USD | `+17.84%` | `217.48` |
| `Live` | `Short` | `113.45` | 6,910,000.00 USD | 102,110.00 USD | 0.00 USD | `+18.05%` | `900.00` |
| `Live` | `Short` | `113.65` | 6,910,000.00 USD | 3,220.00 USD | 0.00 USD | `+18.26%` | `28.37` |
| `Live` | `Short` | `113.95` | 6,930,000.00 USD | 21,840.00 USD | 0.00 USD | `+18.57%` | `191.69` |
| `Live` | `Short` | `114.05` | 6,970,000.00 USD | 33,960.00 USD | 0.00 USD | `+18.67%` | `297.79` |
| `Live` | `Short` | `114.15` | 6,970,000.00 USD | 1,960.00 USD | 0.00 USD | `+18.78%` | `17.21` |
| `Live` | `Short` | `114.25` | 6,970,000.00 USD | 2,150.00 USD | 0.00 USD | `+18.88%` | `18.80` |
| `Live` | `Short` | `114.45` | 6,970,000.00 USD | 160.23 USD | 0.00 USD | `+19.09%` | `1.40` |
| `Live` | `Short` | `114.55` | 6,970,000.00 USD | 431.85 USD | 0.00 USD | `+19.19%` | `3.77` |
| `Live` | `Short` | `115.05` | 7,540,000.00 USD | 569,550.00 USD | 0.00 USD | `+19.71%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 7,540,000.00 USD | 1,100.00 USD | 0.00 USD | `+19.82%` | `9.52` |
| `Live` | `Short` | `115.25` | 7,560,000.00 USD | 18,240.00 USD | 0.00 USD | `+19.92%` | `158.28` |
| `Live` | `Short` | `115.35` | 8,450,000.00 USD | 893,930.00 USD | 0.00 USD | `+20.03%` | `7,749.73` |
| `Live` | `Short` | `115.55` | 8,500,000.00 USD | 46,710.00 USD | 0.00 USD | `+20.23%` | `404.24` |
| `Live` | `Short` | `115.75` | 8,500,000.00 USD | 160.89 USD | 0.00 USD | `+20.44%` | `1.39` |
| `Live` | `Short` | `115.85` | 8,500,000.00 USD | 289.62 USD | 0.00 USD | `+20.55%` | `2.50` |
| `Live` | `Short` | `115.95` | 8,960,000.00 USD | 460,240.00 USD | 0.00 USD | `+20.65%` | `3,969.31` |
| `Live` | `Short` | `116.05` | 8,970,000.00 USD | 4,450.00 USD | 0.00 USD | `+20.75%` | `38.34` |
| `Live` | `Short` | `116.15` | 8,970,000.00 USD | 180.03 USD | 0.00 USD | `+20.86%` | `1.55` |
| `Live` | `Short` | `116.25` | 8,980,000.00 USD | 14,050.00 USD | 0.00 USD | `+20.96%` | `120.84` |
| `Live` | `Short` | `116.35` | 8,990,000.00 USD | 4,960.00 USD | 0.00 USD | `+21.07%` | `42.60` |
| `Live` | `Short` | `116.55` | 8,990,000.00 USD | 2,780.00 USD | 0.00 USD | `+21.27%` | `23.86` |
| `Live` | `Short` | `116.65` | 8,990,000.00 USD | 113.15 USD | 0.00 USD | `+21.38%` | `0.97` |
| `Live` | `Short` | `116.75` | 9,020,000.00 USD | 31,740.00 USD | 0.00 USD | `+21.48%` | `271.88` |
| `Live` | `Short` | `116.95` | 9,020,000.00 USD | 633.87 USD | 0.00 USD | `+21.69%` | `5.42` |
| `Live` | `Short` | `117.05` | 9,020,000.00 USD | 156.85 USD | 0.00 USD | `+21.80%` | `1.34` |
| `Live` | `Short` | `117.15` | 9,050,000.00 USD | 24,630.00 USD | 0.00 USD | `+21.90%` | `210.24` |
| `Live` | `Short` | `117.35` | 13,750,000.00 USD | 4,710,000.00 USD | 0.00 USD | `+22.11%` | `40,124.21` |
| `Live` | `Short` | `117.45` | 13,750,000.00 USD | 809.23 USD | 0.00 USD | `+22.21%` | `6.89` |
| `Live` | `Short` | `117.75` | 13,760,000.00 USD | 2,130.00 USD | 0.00 USD | `+22.52%` | `18.10` |
| `Live` | `Short` | `117.95` | 13,770,000.00 USD | 12,060.00 USD | 0.00 USD | `+22.73%` | `102.22` |
| `Live` | `Short` | `118.35` | 13,770,000.00 USD | 828.45 USD | 0.00 USD | `+23.15%` | `7.00` |
| `Live` | `Short` | `118.45` | 13,800,000.00 USD | 30,970.00 USD | 0.00 USD | `+23.25%` | `261.43` |
| `Live` | `Short` | `118.55` | 13,800,000.00 USD | 1,110.00 USD | 0.00 USD | `+23.36%` | `9.38` |
| `Live` | `Short` | `118.75` | 13,800,000.00 USD | 309.94 USD | 0.00 USD | `+23.56%` | `2.61` |
| `Live` | `Short` | `118.85` | 13,800,000.00 USD | 950.80 USD | 0.00 USD | `+23.67%` | `8.00` |
| `Live` | `Short` | `119.25` | 13,800,000.00 USD | 240.88 USD | 0.00 USD | `+24.08%` | `2.02` |
| `Live` | `Short` | `119.35` | 13,890,000.00 USD | 85,100.00 USD | 0.00 USD | `+24.19%` | `712.99` |
| `Live` | `Short` | `119.45` | 13,890,000.00 USD | 115.87 USD | 0.00 USD | `+24.29%` | `0.97` |
| `Live` | `Short` | `119.55` | 13,890,000.00 USD | 174.54 USD | 0.00 USD | `+24.40%` | `1.46` |
| `Live` | `Short` | `119.65` | 13,900,000.00 USD | 6,170.00 USD | 0.00 USD | `+24.50%` | `51.58` |
| `Live` | `Short` | `119.75` | 13,900,000.00 USD | 261.06 USD | 0.00 USD | `+24.60%` | `2.18` |
| `Live` | `Short` | `119.85` | 13,910,000.00 USD | 10,790.00 USD | 0.00 USD | `+24.71%` | `90.00` |
| `Live` | `Short` | `120.05` | 14,000,000.00 USD | 94,210.00 USD | 0.00 USD | `+24.92%` | `784.74` |
| `Live` | `Short` | `120.15` | 14,000,000.00 USD | 4,150.00 USD | 0.00 USD | `+25.02%` | `34.50` |
| `Live` | `Short` | `120.35` | 14,000,000.00 USD | 145.62 USD | 0.00 USD | `+25.23%` | `1.21` |
| `Live` | `Short` | `120.55` | 14,010,000.00 USD | 1,940.00 USD | 0.00 USD | `+25.44%` | `16.08` |
| `Live` | `Short` | `121.05` | 14,020,000.00 USD | 15,300.00 USD | 0.00 USD | `+25.96%` | `126.38` |
| `Live` | `Short` | `121.25` | 14,020,000.00 USD | 414.68 USD | 0.00 USD | `+26.17%` | `3.42` |
| `Live` | `Short` | `121.35` | 14,030,000.00 USD | 3,230.00 USD | 0.00 USD | `+26.27%` | `26.65` |
| `Live` | `Short` | `121.55` | 14,030,000.00 USD | 5,940.00 USD | 0.00 USD | `+26.48%` | `48.87` |
| `Live` | `Short` | `121.65` | 14,050,000.00 USD | 16,580.00 USD | 0.00 USD | `+26.58%` | `136.29` |
| `Live` | `Short` | `121.75` | 14,060,000.00 USD | 12,780.00 USD | 0.00 USD | `+26.69%` | `105.00` |
| `Live` | `Short` | `122.05` | 14,170,000.00 USD | 111,000.00 USD | 0.00 USD | `+27.00%` | `909.44` |
| `Live` | `Short` | `122.15` | 14,170,000.00 USD | 169.79 USD | 0.00 USD | `+27.10%` | `1.39` |
| `Live` | `Short` | `122.25` | 14,170,000.00 USD | 2,200.00 USD | 0.00 USD | `+27.21%` | `17.99` |
| `Live` | `Short` | `122.45` | 14,260,000.00 USD | 90,040.00 USD | 0.00 USD | `+27.41%` | `735.36` |
| `Live` | `Short` | `122.65` | 14,260,000.00 USD | 116.52 USD | 0.00 USD | `+27.62%` | `0.95` |
| `Live` | `Short` | `122.85` | 15,160,000.00 USD | 896,320.00 USD | 0.00 USD | `+27.83%` | `7,296.04` |
| `Live` | `Short` | `122.95` | 15,160,000.00 USD | 3,900.00 USD | 0.00 USD | `+27.93%` | `31.75` |
| `Live` | `Short` | `123.05` | 28,650,000.00 USD | 13,490,000.00 USD | 0.00 USD | `+28.04%` | `109,622.48` |
| `Live` | `Short` | `123.15` | 28,650,000.00 USD | 126.84 USD | 0.00 USD | `+28.14%` | `1.03` |
| `Live` | `Short` | `123.25` | 28,840,000.00 USD | 182,940.00 USD | 0.00 USD | `+28.25%` | `1,484.34` |
| `Live` | `Short` | `123.35` | 28,840,000.00 USD | 2,330.00 USD | 0.00 USD | `+28.35%` | `18.92` |
| `Live` | `Short` | `123.45` | 28,840,000.00 USD | 3,250.00 USD | 0.00 USD | `+28.45%` | `26.34` |
| `Live` | `Short` | `123.55` | 28,850,000.00 USD | 3,430.00 USD | 0.00 USD | `+28.56%` | `27.73` |
| `Live` | `Short` | `124.05` | 28,850,000.00 USD | 586.76 USD | 0.00 USD | `+29.08%` | `4.73` |
| `Live` | `Short` | `124.25` | 28,860,000.00 USD | 17,600.00 USD | 0.00 USD | `+29.29%` | `141.62` |
| `Live` | `Short` | `124.45` | 28,870,000.00 USD | 3,080.00 USD | 0.00 USD | `+29.50%` | `24.76` |
| `Live` | `Short` | `124.65` | 28,870,000.00 USD | 675.60 USD | 0.00 USD | `+29.70%` | `5.42` |
| `Live` | `Short` | `124.75` | 28,870,000.00 USD | 5,330.00 USD | 0.00 USD | `+29.81%` | `42.73` |
| `Live` | `Short` | `124.95` | 28,890,000.00 USD | 14,160.00 USD | 0.00 USD | `+30.02%` | `113.36` |
| `Live` | `Short` | `125.45` | 28,890,000.00 USD | 3,760.00 USD | 0.00 USD | `+30.54%` | `30.00` |
| `Live` | `Short` | `125.75` | 28,890,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.85%` | `15.31` |
| `Live` | `Short` | `125.85` | 28,900,000.00 USD | 6,200.00 USD | 0.00 USD | `+30.95%` | `49.29` |
| `Live` | `Short` | `125.95` | 28,900,000.00 USD | 2,030.00 USD | 0.00 USD | `+31.06%` | `16.08` |
| `Live` | `Short` | `126.05` | 28,900,000.00 USD | 810.50 USD | 0.00 USD | `+31.16%` | `6.43` |
| `Live` | `Short` | `126.15` | 28,900,000.00 USD | 470.54 USD | 0.00 USD | `+31.26%` | `3.73` |
| `Live` | `Short` | `126.35` | 28,900,000.00 USD | 305.77 USD | 0.00 USD | `+31.47%` | `2.42` |
| `Live` | `Short` | `126.65` | 28,930,000.00 USD | 30,830.00 USD | 0.00 USD | `+31.78%` | `243.46` |
| `Live` | `Short` | `126.85` | 28,940,000.00 USD | 1,710.00 USD | 0.00 USD | `+31.99%` | `13.48` |
| `Live` | `Short` | `126.95` | 28,940,000.00 USD | 9,460.00 USD | 0.00 USD | `+32.10%` | `74.51` |
| `Live` | `Short` | `127.05` | 28,950,000.00 USD | 2,030.00 USD | 0.00 USD | `+32.20%` | `16.01` |
| `Live` | `Short` | `127.35` | 28,960,000.00 USD | 16,190.00 USD | 0.00 USD | `+32.51%` | `127.13` |
| `Live` | `Short` | `127.55` | 28,970,000.00 USD | 2,260.00 USD | 0.00 USD | `+32.72%` | `17.70` |
| `Live` | `Short` | `127.65` | 28,970,000.00 USD | 4,840.00 USD | 0.00 USD | `+32.82%` | `37.89` |
| `Live` | `Short` | `127.85` | 29,010,000.00 USD | 43,470.00 USD | 0.00 USD | `+33.03%` | `340.04` |
| `Live` | `Short` | `127.95` | 29,020,000.00 USD | 10,510.00 USD | 0.00 USD | `+33.14%` | `82.13` |
| `Live` | `Short` | `128.05` | 29,140,000.00 USD | 116,200.00 USD | 0.00 USD | `+33.24%` | `907.49` |
| `Live` | `Short` | `128.35` | 33,990,000.00 USD | 4,850,000.00 USD | 0.00 USD | `+33.55%` | `37,780.67` |
| `Live` | `Short` | `128.55` | 33,990,000.00 USD | 3,140.00 USD | 0.00 USD | `+33.76%` | `24.41` |
| `Live` | `Short` | `128.65` | 34,000,000.00 USD | 4,300.00 USD | 0.00 USD | `+33.87%` | `33.46` |
| `Live` | `Short` | `128.75` | 34,020,000.00 USD | 18,730.00 USD | 0.00 USD | `+33.97%` | `145.45` |
| `Live` | `Short` | `128.85` | 34,060,000.00 USD | 40,920.00 USD | 0.00 USD | `+34.07%` | `317.60` |
| `Live` | `Short` | `128.95` | 34,750,000.00 USD | 697,060.00 USD | 0.00 USD | `+34.18%` | `5,405.66` |
| `Live` | `Short` | `129.05` | 34,800,000.00 USD | 47,810.00 USD | 0.00 USD | `+34.28%` | `370.50` |
| `Live` | `Short` | `129.25` | 34,840,000.00 USD | 41,090.00 USD | 0.00 USD | `+34.49%` | `317.93` |
| `Live` | `Short` | `129.55` | 34,900,000.00 USD | 56,180.00 USD | 0.00 USD | `+34.80%` | `433.68` |
| `Live` | `Short` | `129.75` | 34,930,000.00 USD | 36,480.00 USD | 0.00 USD | `+35.01%` | `281.19` |
| `Live` | `Short` | `129.85` | 34,950,000.00 USD | 13,670.00 USD | 0.00 USD | `+35.11%` | `105.25` |
| `Live` | `Short` | `129.95` | 34,990,000.00 USD | 42,200.00 USD | 0.00 USD | `+35.22%` | `324.75` |
| `Live` | `Short` | `130.25` | 34,990,000.00 USD | 145.88 USD | 0.00 USD | `+35.53%` | `1.12` |
| `Live` | `Short` | `130.55` | 34,990,000.00 USD | 3,020.00 USD | 0.00 USD | `+35.84%` | `23.10` |
| `Live` | `Short` | `130.65` | 35,000,000.00 USD | 1,310.00 USD | 0.00 USD | `+35.95%` | `10.00` |
| `Live` | `Short` | `130.85` | 35,500,000.00 USD | 503,820.00 USD | 0.00 USD | `+36.15%` | `3,850.39` |
| `Live` | `Short` | `130.95` | 35,500,000.00 USD | 2,070.00 USD | 0.00 USD | `+36.26%` | `15.84` |
| `Live` | `Short` | `131.05` | 35,500,000.00 USD | 188.71 USD | 0.00 USD | `+36.36%` | `1.44` |
| `Live` | `Short` | `131.25` | 35,500,000.00 USD | 2,410.00 USD | 0.00 USD | `+36.57%` | `18.38` |
| `Live` | `Short` | `131.45` | 35,510,000.00 USD | 6,790.00 USD | 0.00 USD | `+36.78%` | `51.67` |
| `Live` | `Short` | `131.85` | 35,520,000.00 USD | 5,820.00 USD | 0.00 USD | `+37.20%` | `44.14` |
| `Live` | `Short` | `132.15` | 35,520,000.00 USD | 325.09 USD | 0.00 USD | `+37.51%` | `2.46` |
| `Live` | `Short` | `132.35` | 35,520,000.00 USD | 4,630.00 USD | 0.00 USD | `+37.72%` | `35.00` |
| `Live` | `Short` | `132.45` | 35,530,000.00 USD | 8,530.00 USD | 0.00 USD | `+37.82%` | `64.37` |
| `Live` | `Short` | `132.55` | 35,530,000.00 USD | 196.17 USD | 0.00 USD | `+37.92%` | `1.48` |
| `Live` | `Short` | `132.65` | 35,530,000.00 USD | 740.19 USD | 0.00 USD | `+38.03%` | `5.58` |
| `Live` | `Short` | `132.85` | 35,580,000.00 USD | 49,280.00 USD | 0.00 USD | `+38.24%` | `370.98` |
| `Live` | `Short` | `133.05` | 35,680,000.00 USD | 96,780.00 USD | 0.00 USD | `+38.44%` | `727.40` |
| `Live` | `Short` | `133.15` | 35,690,000.00 USD | 8,440.00 USD | 0.00 USD | `+38.55%` | `63.42` |
| `Live` | `Short` | `133.35` | 35,690,000.00 USD | 3,640.00 USD | 0.00 USD | `+38.76%` | `27.29` |
| `Live` | `Short` | `133.45` | 35,900,000.00 USD | 209,480.00 USD | 0.00 USD | `+38.86%` | `1,569.69` |
| `Live` | `Short` | `133.55` | 35,900,000.00 USD | 186.97 USD | 0.00 USD | `+38.96%` | `1.40` |
| `Live` | `Short` | `133.65` | 35,900,000.00 USD | 156.37 USD | 0.00 USD | `+39.07%` | `1.17` |
| `Live` | `Short` | `133.75` | 36,050,000.00 USD | 151,200.00 USD | 0.00 USD | `+39.17%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 36,050,000.00 USD | 503.65 USD | 0.00 USD | `+39.38%` | `3.76` |
| `Live` | `Short` | `134.05` | 36,050,000.00 USD | 142.09 USD | 0.00 USD | `+39.48%` | `1.06` |
| `Live` | `Short` | `134.25` | 36,060,000.00 USD | 11,590.00 USD | 0.00 USD | `+39.69%` | `86.32` |
| `Live` | `Short` | `134.55` | 36,110,000.00 USD | 48,390.00 USD | 0.00 USD | `+40.00%` | `359.64` |
| `Live` | `Short` | `134.65` | 37,460,000.00 USD | 1,350,000.00 USD | 0.00 USD | `+40.11%` | `10,000.00` |
| `Live` | `Short` | `135.85` | 37,460,000.00 USD | 3,250.00 USD | 0.00 USD | `+41.36%` | `23.94` |
| `Live` | `Short` | `135.95` | 37,460,000.00 USD | 504.37 USD | 0.00 USD | `+41.46%` | `3.71` |
| `Live` | `Short` | `136.35` | 37,460,000.00 USD | 589.03 USD | 0.00 USD | `+41.88%` | `4.32` |
| `Live` | `Short` | `136.55` | 37,460,000.00 USD | 136.55 USD | 0.00 USD | `+42.09%` | `1.00` |
| `Live` | `Short` | `136.65` | 37,460,000.00 USD | 1,110.00 USD | 0.00 USD | `+42.19%` | `8.14` |
| `Live` | `Short` | `137.05` | 37,460,000.00 USD | 836.00 USD | 0.00 USD | `+42.61%` | `6.10` |
| `Live` | `Short` | `137.35` | 37,460,000.00 USD | 317.28 USD | 0.00 USD | `+42.92%` | `2.31` |
| `Live` | `Short` | `137.65` | 37,460,000.00 USD | 306.96 USD | 0.00 USD | `+43.23%` | `2.23` |
| `Live` | `Short` | `137.75` | 37,480,000.00 USD | 14,810.00 USD | 0.00 USD | `+43.33%` | `107.50` |
| `Live` | `Short` | `138.05` | 37,480,000.00 USD | 1,270.00 USD | 0.00 USD | `+43.65%` | `9.20` |
| `Live` | `Short` | `138.15` | 37,570,000.00 USD | 86,640.00 USD | 0.00 USD | `+43.75%` | `627.11` |
| `Live` | `Short` | `138.25` | 37,580,000.00 USD | 12,480.00 USD | 0.00 USD | `+43.85%` | `90.29` |
| `Live` | `Short` | `138.35` | 37,740,000.00 USD | 155,690.00 USD | 0.00 USD | `+43.96%` | `1,125.32` |
| `Live` | `Short` | `138.45` | 37,940,000.00 USD | 207,340.00 USD | 0.00 USD | `+44.06%` | `1,497.60` |
| `Live` | `Short` | `138.75` | 40,020,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+44.37%` | `15,001.76` |
| `Live` | `Short` | `139.05` | 40,030,000.00 USD | 2,750.00 USD | 0.00 USD | `+44.69%` | `19.81` |
| `Live` | `Short` | `139.15` | 40,030,000.00 USD | 2,230.00 USD | 0.00 USD | `+44.79%` | `15.99` |
| `Live` | `Short` | `139.25` | 40,030,000.00 USD | 492.94 USD | 0.00 USD | `+44.90%` | `3.54` |
| `Live` | `Short` | `139.35` | 40,030,000.00 USD | 253.62 USD | 0.00 USD | `+45.00%` | `1.82` |
| `Live` | `Short` | `139.45` | 45,220,000.00 USD | 5,190,000.00 USD | 0.00 USD | `+45.10%` | `37,198.39` |
| `Live` | `Short` | `139.65` | 45,220,000.00 USD | 622.84 USD | 0.00 USD | `+45.31%` | `4.46` |
| `Live` | `Short` | `139.85` | 45,220,000.00 USD | 770.57 USD | 0.00 USD | `+45.52%` | `5.51` |
| `Live` | `Short` | `140.05` | 45,220,000.00 USD | 116.24 USD | 0.00 USD | `+45.73%` | `0.83` |
| `Live` | `Short` | `140.45` | 45,290,000.00 USD | 71,960.00 USD | 0.00 USD | `+46.14%` | `512.33` |
| `Live` | `Short` | `140.55` | 45,300,000.00 USD | 7,330.00 USD | 0.00 USD | `+46.25%` | `52.16` |
| `Live` | `Short` | `140.95` | 45,300,000.00 USD | 1,940.00 USD | 0.00 USD | `+46.66%` | `13.73` |
| `Live` | `Short` | `141.05` | 45,300,000.00 USD | 335.70 USD | 0.00 USD | `+46.77%` | `2.38` |
| `Live` | `Short` | `141.15` | 46,370,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+46.87%` | `7,609.58` |
| `Live` | `Short` | `141.35` | 46,370,000.00 USD | 210.61 USD | 0.00 USD | `+47.08%` | `1.49` |
| `Live` | `Short` | `141.45` | 46,640,000.00 USD | 268,700.00 USD | 0.00 USD | `+47.18%` | `1,899.58` |
| `Live` | `Short` | `141.55` | 46,640,000.00 USD | 236.39 USD | 0.00 USD | `+47.29%` | `1.67` |
| `Live` | `Short` | `141.65` | 46,660,000.00 USD | 18,490.00 USD | 0.00 USD | `+47.39%` | `130.56` |
| `Live` | `Short` | `141.75` | 46,660,000.00 USD | 103.48 USD | 0.00 USD | `+47.50%` | `0.73` |
| `Live` | `Short` | `142.15` | 46,790,000.00 USD | 131,260.00 USD | 0.00 USD | `+47.91%` | `923.38` |
| `Live` | `Short` | `142.25` | 46,790,000.00 USD | 112.38 USD | 0.00 USD | `+48.02%` | `0.79` |
| `Live` | `Short` | `142.45` | 46,790,000.00 USD | 151.00 USD | 0.00 USD | `+48.22%` | `1.06` |
| `Live` | `Short` | `142.65` | 47,640,000.00 USD | 847,490.00 USD | 0.00 USD | `+48.43%` | `5,941.05` |
| `Live` | `Short` | `142.75` | 47,640,000.00 USD | 368.30 USD | 0.00 USD | `+48.54%` | `2.58` |
| `Live` | `Short` | `143.15` | 47,640,000.00 USD | 2,980.00 USD | 0.00 USD | `+48.95%` | `20.83` |
| `Live` | `Short` | `143.35` | 47,670,000.00 USD | 22,260.00 USD | 0.00 USD | `+49.16%` | `155.27` |
| `Live` | `Short` | `143.75` | 47,670,000.00 USD | 143.75 USD | 0.00 USD | `+49.58%` | `1.00` |
| `Live` | `Short` | `144.05` | 47,670,000.00 USD | 3,750.00 USD | 0.00 USD | `+49.89%` | `26.00` |
| `Live` | `Short` | `144.15` | 47,680,000.00 USD | 13,330.00 USD | 0.00 USD | `+49.99%` | `92.45` |
| `Live` | `Short` | `144.65` | 47,680,000.00 USD | 1,240.00 USD | 0.00 USD | `+50.51%` | `8.60` |
| `Live` | `Short` | `145.15` | 47,690,000.00 USD | 2,250.00 USD | 0.00 USD | `+51.03%` | `15.48` |
| `Live` | `Short` | `145.35` | 47,690,000.00 USD | 5,110.00 USD | 0.00 USD | `+51.24%` | `35.17` |
| `Live` | `Short` | `145.65` | 47,780,000.00 USD | 85,880.00 USD | 0.00 USD | `+51.55%` | `589.63` |
| `Live` | `Short` | `145.85` | 47,780,000.00 USD | 5,850.00 USD | 0.00 USD | `+51.76%` | `40.09` |
| `Live` | `Short` | `145.95` | 47,780,000.00 USD | 820.24 USD | 0.00 USD | `+51.87%` | `5.62` |
| `Live` | `Short` | `146.15` | 47,870,000.00 USD | 88,760.00 USD | 0.00 USD | `+52.07%` | `607.33` |
| `Live` | `Short` | `146.25` | 47,880,000.00 USD | 2,770.00 USD | 0.00 USD | `+52.18%` | `18.95` |
| `Live` | `Short` | `146.35` | 47,880,000.00 USD | 7,330.00 USD | 0.00 USD | `+52.28%` | `50.10` |
| `Live` | `Short` | `146.65` | 48,470,000.00 USD | 587,860.00 USD | 0.00 USD | `+52.60%` | `4,008.60` |
| `Live` | `Short` | `146.75` | 48,470,000.00 USD | 2,110.00 USD | 0.00 USD | `+52.70%` | `14.41` |
| `Live` | `Short` | `146.95` | 49,340,000.00 USD | 861,660.00 USD | 0.00 USD | `+52.91%` | `5,863.60` |
| `Live` | `Short` | `147.05` | 49,340,000.00 USD | 1,120.00 USD | 0.00 USD | `+53.01%` | `7.64` |
| `Live` | `Short` | `147.15` | 49,340,000.00 USD | 1,730.00 USD | 0.00 USD | `+53.12%` | `11.75` |
| `Live` | `Short` | `147.35` | 49,340,000.00 USD | 169.45 USD | 0.00 USD | `+53.32%` | `1.15` |
| `Live` | `Short` | `147.45` | 49,420,000.00 USD | 78,420.00 USD | 0.00 USD | `+53.43%` | `531.81` |
| `Live` | `Short` | `147.55` | 49,420,000.00 USD | 6,420.00 USD | 0.00 USD | `+53.53%` | `43.51` |
| `Live` | `Short` | `147.65` | 49,420,000.00 USD | 237.72 USD | 0.00 USD | `+53.64%` | `1.61` |
| `Live` | `Short` | `147.85` | 49,420,000.00 USD | 300.14 USD | 0.00 USD | `+53.84%` | `2.03` |
| `Live` | `Short` | `148.15` | 49,870,000.00 USD | 444,550.00 USD | 0.00 USD | `+54.16%` | `3,000.69` |
| `Live` | `Short` | `148.25` | 50,310,000.00 USD | 444,750.00 USD | 0.00 USD | `+54.26%` | `3,000.00` |
| `Live` | `Short` | `148.35` | 50,320,000.00 USD | 5,640.00 USD | 0.00 USD | `+54.36%` | `38.00` |
| `Live` | `Short` | `148.45` | 50,320,000.00 USD | 163.29 USD | 0.00 USD | `+54.47%` | `1.10` |
| `Live` | `Short` | `148.55` | 50,660,000.00 USD | 344,780.00 USD | 0.00 USD | `+54.57%` | `2,321.00` |
| `Live` | `Short` | `148.65` | 50,660,000.00 USD | 377.57 USD | 0.00 USD | `+54.68%` | `2.54` |
| `Live` | `Short` | `148.75` | 50,760,000.00 USD | 92,000.00 USD | 0.00 USD | `+54.78%` | `618.52` |
| `Live` | `Short` | `148.95` | 50,760,000.00 USD | 1,460.00 USD | 0.00 USD | `+54.99%` | `9.81` |
| `Live` | `Short` | `149.05` | 52,140,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+55.09%` | `9,289.83` |
| `Live` | `Short` | `149.45` | 53,270,000.00 USD | 1,130,000.00 USD | 0.00 USD | `+55.51%` | `7,550.71` |
| `Live` | `Short` | `149.55` | 53,270,000.00 USD | 116.65 USD | 0.00 USD | `+55.61%` | `0.78` |
| `Live` | `Short` | `149.65` | 53,290,000.00 USD | 16,030.00 USD | 0.00 USD | `+55.72%` | `107.15` |
| `Live` | `Short` | `149.85` | 53,300,000.00 USD | 17,290.00 USD | 0.00 USD | `+55.92%` | `115.35` |
| `Live` | `Short` | `149.95` | 53,300,000.00 USD | 178.44 USD | 0.00 USD | `+56.03%` | `1.19` |
| `Live` | `Short` | `150.05` | 53,310,000.00 USD | 9,340.00 USD | 0.00 USD | `+56.13%` | `62.26` |
| `Live` | `Short` | `150.45` | 53,360,000.00 USD | 46,810.00 USD | 0.00 USD | `+56.55%` | `311.16` |
| `Live` | `Short` | `151.15` | 53,360,000.00 USD | 2,540.00 USD | 0.00 USD | `+57.28%` | `16.81` |
| `Live` | `Short` | `151.35` | 53,370,000.00 USD | 4,540.00 USD | 0.00 USD | `+57.49%` | `30.00` |
| `Live` | `Short` | `151.45` | 53,380,000.00 USD | 8,830.00 USD | 0.00 USD | `+57.59%` | `58.32` |
| `Live` | `Short` | `151.95` | 53,380,000.00 USD | 1,920.00 USD | 0.00 USD | `+58.11%` | `12.64` |
| `Live` | `Short` | `152.15` | 57,990,000.00 USD | 4,610,000.00 USD | 0.00 USD | `+58.32%` | `30,312.60` |
| `Live` | `Short` | `152.25` | 57,990,000.00 USD | 3,000.00 USD | 0.00 USD | `+58.42%` | `19.69` |
| `Live` | `Short` | `152.35` | 58,280,000.00 USD | 286,550.00 USD | 0.00 USD | `+58.53%` | `1,880.87` |
| `Live` | `Short` | `152.45` | 58,280,000.00 USD | 3,150.00 USD | 0.00 USD | `+58.63%` | `20.65` |
| `Live` | `Short` | `152.55` | 58,710,000.00 USD | 423,220.00 USD | 0.00 USD | `+58.73%` | `2,774.28` |
| `Live` | `Short` | `152.65` | 58,710,000.00 USD | 233.55 USD | 0.00 USD | `+58.84%` | `1.53` |
| `Live` | `Short` | `152.75` | 58,710,000.00 USD | 1,570.00 USD | 0.00 USD | `+58.94%` | `10.30` |
| `Live` | `Short` | `152.95` | 58,730,000.00 USD | 18,970.00 USD | 0.00 USD | `+59.15%` | `124.05` |
| `Live` | `Short` | `153.05` | 58,730,000.00 USD | 1,060.00 USD | 0.00 USD | `+59.25%` | `6.95` |
| `Live` | `Short` | `153.35` | 58,730,000.00 USD | 2,300.00 USD | 0.00 USD | `+59.57%` | `15.00` |
| `Live` | `Short` | `153.55` | 58,850,000.00 USD | 119,720.00 USD | 0.00 USD | `+59.77%` | `779.71` |
| `Live` | `Short` | `153.65` | 58,900,000.00 USD | 52,040.00 USD | 0.00 USD | `+59.88%` | `338.66` |
| `Live` | `Short` | `154.05` | 58,900,000.00 USD | 292.69 USD | 0.00 USD | `+60.30%` | `1.90` |
| `Live` | `Short` | `154.15` | 58,900,000.00 USD | 362.25 USD | 0.00 USD | `+60.40%` | `2.35` |
| `Live` | `Short` | `154.25` | 58,910,000.00 USD | 2,340.00 USD | 0.00 USD | `+60.50%` | `15.20` |
| `Live` | `Short` | `154.35` | 59,210,000.00 USD | 308,700.00 USD | 0.00 USD | `+60.61%` | `2,000.00` |
| `Live` | `Short` | `154.45` | 59,220,000.00 USD | 4,240.00 USD | 0.00 USD | `+60.71%` | `27.45` |
| `Live` | `Short` | `154.75` | 59,260,000.00 USD | 43,600.00 USD | 0.00 USD | `+61.02%` | `281.77` |
| `Live` | `Short` | `154.85` | 59,260,000.00 USD | 1,240.00 USD | 0.00 USD | `+61.13%` | `8.00` |
| `Live` | `Short` | `154.95` | 59,290,000.00 USD | 27,160.00 USD | 0.00 USD | `+61.23%` | `175.30` |
| `Live` | `Short` | `155.25` | 59,290,000.00 USD | 1,240.00 USD | 0.00 USD | `+61.54%` | `8.00` |
| `Live` | `Short` | `155.35` | 59,450,000.00 USD | 155,350.00 USD | 0.00 USD | `+61.65%` | `1,000.00` |
| `Live` | `Short` | `155.55` | 59,680,000.00 USD | 233,590.00 USD | 0.00 USD | `+61.86%` | `1,501.72` |
| `Live` | `Short` | `155.85` | 59,680,000.00 USD | 325.73 USD | 0.00 USD | `+62.17%` | `2.09` |
| `Live` | `Short` | `155.95` | 59,690,000.00 USD | 7,800.00 USD | 0.00 USD | `+62.27%` | `50.00` |
| `Live` | `Short` | `156.15` | 59,710,000.00 USD | 21,660.00 USD | 0.00 USD | `+62.48%` | `138.74` |
| `Live` | `Short` | `156.35` | 59,710,000.00 USD | 3,320.00 USD | 0.00 USD | `+62.69%` | `21.26` |
| `Live` | `Short` | `156.45` | 59,720,000.00 USD | 1,770.00 USD | 0.00 USD | `+62.79%` | `11.29` |
| `Live` | `Short` | `156.55` | 59,720,000.00 USD | 2,000.00 USD | 0.00 USD | `+62.90%` | `12.80` |
| `Live` | `Short` | `156.85` | 59,830,000.00 USD | 113,870.00 USD | 0.00 USD | `+63.21%` | `726.01` |
| `Live` | `Short` | `156.95` | 59,830,000.00 USD | 296.64 USD | 0.00 USD | `+63.31%` | `1.89` |
| `Live` | `Short` | `157.15` | 59,880,000.00 USD | 49,270.00 USD | 0.00 USD | `+63.52%` | `313.50` |
| `Live` | `Short` | `157.25` | 59,880,000.00 USD | 190.27 USD | 0.00 USD | `+63.62%` | `1.21` |
| `Live` | `Short` | `157.45` | 59,980,000.00 USD | 101,740.00 USD | 0.00 USD | `+63.83%` | `646.20` |
| `Live` | `Short` | `157.65` | 59,980,000.00 USD | 654.25 USD | 0.00 USD | `+64.04%` | `4.15` |
| `Live` | `Short` | `157.75` | 60,080,000.00 USD | 92,600.00 USD | 0.00 USD | `+64.15%` | `587.00` |
| `Live` | `Short` | `157.85` | 60,080,000.00 USD | 119.97 USD | 0.00 USD | `+64.25%` | `0.76` |
| `Live` | `Short` | `157.95` | 60,080,000.00 USD | 312.74 USD | 0.00 USD | `+64.35%` | `1.98` |
| `Live` | `Short` | `158.65` | 60,160,000.00 USD | 84,520.00 USD | 0.00 USD | `+65.08%` | `532.74` |
| `Live` | `Short` | `158.75` | 60,160,000.00 USD | 125.41 USD | 0.00 USD | `+65.19%` | `0.79` |
| `Live` | `Short` | `159.05` | 60,240,000.00 USD | 82,370.00 USD | 0.00 USD | `+65.50%` | `517.89` |
| `Live` | `Short` | `159.35` | 60,250,000.00 USD | 3,080.00 USD | 0.00 USD | `+65.81%` | `19.33` |
| `Live` | `Short` | `159.55` | 60,290,000.00 USD | 39,920.00 USD | 0.00 USD | `+66.02%` | `250.18` |
| `Live` | `Short` | `159.65` | 60,290,000.00 USD | 2,080.00 USD | 0.00 USD | `+66.12%` | `13.01` |
| `Live` | `Short` | `159.75` | 60,290,000.00 USD | 2,090.00 USD | 0.00 USD | `+66.23%` | `13.10` |
| `Live` | `Short` | `159.85` | 60,290,000.00 USD | 300.52 USD | 0.00 USD | `+66.33%` | `1.88` |
| `Live` | `Short` | `160.15` | 60,970,000.00 USD | 684,060.00 USD | 0.00 USD | `+66.64%` | `4,271.34` |
| `Live` | `Short` | `160.35` | 60,980,000.00 USD | 2,200.00 USD | 0.00 USD | `+66.85%` | `13.73` |
| `Live` | `Short` | `160.65` | 60,980,000.00 USD | 782.37 USD | 0.00 USD | `+67.16%` | `4.87` |
| `Live` | `Short` | `160.75` | 60,980,000.00 USD | 1,630.00 USD | 0.00 USD | `+67.27%` | `10.17` |
| `Live` | `Short` | `160.85` | 61,140,000.00 USD | 164,050.00 USD | 0.00 USD | `+67.37%` | `1,019.89` |
| `Live` | `Short` | `161.05` | 61,150,000.00 USD | 2,240.00 USD | 0.00 USD | `+67.58%` | `13.93` |
| `Live` | `Short` | `161.35` | 61,170,000.00 USD | 20,430.00 USD | 0.00 USD | `+67.89%` | `126.60` |
| `Live` | `Short` | `161.55` | 61,170,000.00 USD | 410.34 USD | 0.00 USD | `+68.10%` | `2.54` |
| `Live` | `Short` | `161.95` | 61,310,000.00 USD | 144,940.00 USD | 0.00 USD | `+68.52%` | `894.95` |
| `Live` | `Short` | `162.15` | 61,310,000.00 USD | 119.99 USD | 0.00 USD | `+68.72%` | `0.74` |
| `Live` | `Short` | `162.55` | 61,640,000.00 USD | 325,100.00 USD | 0.00 USD | `+69.14%` | `2,000.00` |
| `Live` | `Short` | `162.95` | 61,640,000.00 USD | 666.47 USD | 0.00 USD | `+69.56%` | `4.09` |
| `Live` | `Short` | `163.45` | 61,810,000.00 USD | 177,370.00 USD | 0.00 USD | `+70.08%` | `1,085.16` |
| `Live` | `Short` | `163.55` | 61,820,000.00 USD | 2,550.00 USD | 0.00 USD | `+70.18%` | `15.62` |
| `Live` | `Short` | `163.85` | 61,820,000.00 USD | 786.48 USD | 0.00 USD | `+70.49%` | `4.80` |
| `Live` | `Short` | `164.45` | 61,840,000.00 USD | 17,820.00 USD | 0.00 USD | `+71.12%` | `108.36` |
| `Live` | `Short` | `164.75` | 62,040,000.00 USD | 207,840.00 USD | 0.00 USD | `+71.43%` | `1,261.56` |
| `Live` | `Short` | `165.15` | 62,040,000.00 USD | 198.18 USD | 0.00 USD | `+71.85%` | `1.20` |
| `Live` | `Short` | `165.55` | 62,120,000.00 USD | 72,840.00 USD | 0.00 USD | `+72.26%` | `440.00` |
| `Live` | `Short` | `166.25` | 62,130,000.00 USD | 14,070.00 USD | 0.00 USD | `+72.99%` | `84.61` |
| `Live` | `Short` | `166.65` | 62,130,000.00 USD | 833.25 USD | 0.00 USD | `+73.41%` | `5.00` |
| `Live` | `Short` | `167.15` | 62,160,000.00 USD | 27,060.00 USD | 0.00 USD | `+73.93%` | `161.92` |
| `Live` | `Short` | `167.55` | 62,160,000.00 USD | 3,460.00 USD | 0.00 USD | `+74.34%` | `20.63` |
| `Live` | `Short` | `167.65` | 62,160,000.00 USD | 115.68 USD | 0.00 USD | `+74.45%` | `0.69` |
| `Live` | `Short` | `167.75` | 62,160,000.00 USD | 1,890.00 USD | 0.00 USD | `+74.55%` | `11.27` |
| `Live` | `Short` | `167.95` | 62,160,000.00 USD | 122.60 USD | 0.00 USD | `+74.76%` | `0.73` |
| `Live` | `Short` | `168.35` | 62,180,000.00 USD | 19,740.00 USD | 0.00 USD | `+75.17%` | `117.24` |
| `Live` | `Short` | `168.65` | 62,510,000.00 USD | 325,850.00 USD | 0.00 USD | `+75.49%` | `1,932.10` |
| `Live` | `Short` | `169.35` | 62,640,000.00 USD | 130,080.00 USD | 0.00 USD | `+76.22%` | `768.11` |
| `Live` | `Short` | `169.75` | 62,660,000.00 USD | 16,130.00 USD | 0.00 USD | `+76.63%` | `95.00` |
| `Live` | `Short` | `170.35` | 62,660,000.00 USD | 153.32 USD | 0.00 USD | `+77.26%` | `0.90` |
| `Live` | `Short` | `170.55` | 62,660,000.00 USD | 325.75 USD | 0.00 USD | `+77.46%` | `1.91` |
| `Live` | `Short` | `171.45` | 62,660,000.00 USD | 111.44 USD | 0.00 USD | `+78.40%` | `0.65` |
| `Live` | `Short` | `171.55` | 62,660,000.00 USD | 300.21 USD | 0.00 USD | `+78.50%` | `1.75` |
| `Live` | `Short` | `171.65` | 62,700,000.00 USD | 42,930.00 USD | 0.00 USD | `+78.61%` | `250.10` |
| `Live` | `Short` | `171.75` | 62,700,000.00 USD | 2,720.00 USD | 0.00 USD | `+78.71%` | `15.84` |
| `Live` | `Short` | `172.35` | 100,800,000.00 USD | 38,100,000.00 USD | 0.00 USD | `+79.34%` | `221,061.98` |
| `Live` | `Short` | `172.45` | 100,850,000.00 USD | 51,730.00 USD | 0.00 USD | `+79.44%` | `300.00` |
| `Live` | `Short` | `173.25` | 100,860,000.00 USD | 693.00 USD | 0.00 USD | `+80.27%` | `4.00` |
| `Live` | `Short` | `173.45` | 100,870,000.00 USD | 16,540.00 USD | 0.00 USD | `+80.48%` | `95.36` |
| `Live` | `Short` | `173.75` | 100,870,000.00 USD | 1,280.00 USD | 0.00 USD | `+80.79%` | `7.37` |
| `Live` | `Short` | `173.85` | 100,870,000.00 USD | 695.40 USD | 0.00 USD | `+80.90%` | `4.00` |
| `Live` | `Short` | `174.05` | 100,980,000.00 USD | 104,430.00 USD | 0.00 USD | `+81.11%` | `600.00` |
| `Live` | `Short` | `174.15` | 101,000,000.00 USD | 23,910.00 USD | 0.00 USD | `+81.21%` | `137.27` |
| `Live` | `Short` | `174.25` | 101,250,000.00 USD | 245,010.00 USD | 0.00 USD | `+81.31%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 101,450,000.00 USD | 205,490.00 USD | 0.00 USD | `+81.42%` | `1,178.60` |
| `Live` | `Short` | `174.55` | 101,560,000.00 USD | 110,740.00 USD | 0.00 USD | `+81.63%` | `634.45` |
| `Live` | `Short` | `174.75` | 101,560,000.00 USD | 146.79 USD | 0.00 USD | `+81.83%` | `0.84` |
| `Live` | `Short` | `175.35` | 101,560,000.00 USD | 508.52 USD | 0.00 USD | `+82.46%` | `2.90` |
| `Live` | `Short` | `175.55` | 101,700,000.00 USD | 140,440.00 USD | 0.00 USD | `+82.67%` | `800.00` |
| `Live` | `Short` | `175.75` | 101,700,000.00 USD | 263.62 USD | 0.00 USD | `+82.87%` | `1.50` |
| `Live` | `Short` | `175.85` | 102,720,000.00 USD | 1,020,000.00 USD | 0.00 USD | `+82.98%` | `5,800.00` |
| `Live` | `Short` | `176.25` | 102,730,000.00 USD | 625.69 USD | 0.00 USD | `+83.40%` | `3.55` |
| `Live` | `Short` | `176.85` | 102,750,000.00 USD | 24,930.00 USD | 0.00 USD | `+84.02%` | `140.96` |
| `Live` | `Short` | `177.95` | 102,840,000.00 USD | 90,750.00 USD | 0.00 USD | `+85.16%` | `510.00` |
| `Live` | `Short` | `178.25` | 109,180,000.00 USD | 6,330,000.00 USD | 0.00 USD | `+85.48%` | `35,538.18` |
| `Live` | `Short` | `178.45` | 109,530,000.00 USD | 356,900.00 USD | 0.00 USD | `+85.68%` | `2,000.00` |
| `Live` | `Short` | `178.55` | 109,800,000.00 USD | 267,820.00 USD | 0.00 USD | `+85.79%` | `1,500.00` |
| `Live` | `Short` | `178.75` | 109,800,000.00 USD | 770.41 USD | 0.00 USD | `+86.00%` | `4.31` |
| `Live` | `Short` | `179.35` | 109,800,000.00 USD | 473.48 USD | 0.00 USD | `+86.62%` | `2.64` |
| `Live` | `Short` | `179.55` | 109,920,000.00 USD | 116,010.00 USD | 0.00 USD | `+86.83%` | `646.12` |
| `Live` | `Short` | `179.65` | 109,920,000.00 USD | 1,350.00 USD | 0.00 USD | `+86.93%` | `7.52` |
| `Live` | `Short` | `179.75` | 109,920,000.00 USD | 154.59 USD | 0.00 USD | `+87.04%` | `0.86` |
| `Live` | `Short` | `180.45` | 109,920,000.00 USD | 2,080.00 USD | 0.00 USD | `+87.77%` | `11.54` |
| `Live` | `Short` | `180.55` | 109,920,000.00 USD | 3,970.00 USD | 0.00 USD | `+87.87%` | `22.01` |
| `Live` | `Short` | `180.75` | 109,930,000.00 USD | 146.41 USD | 0.00 USD | `+88.08%` | `0.81` |
| `Live` | `Short` | `181.15` | 110,050,000.00 USD | 126,810.00 USD | 0.00 USD | `+88.49%` | `700.00` |
| `Live` | `Short` | `181.55` | 110,070,000.00 USD | 18,410.00 USD | 0.00 USD | `+88.91%` | `101.40` |
| `Live` | `Short` | `182.15` | 110,070,000.00 USD | 3,990.00 USD | 0.00 USD | `+89.53%` | `21.93` |
| `Live` | `Short` | `182.85` | 110,070,000.00 USD | 618.03 USD | 0.00 USD | `+90.26%` | `3.38` |
| `Live` | `Short` | `183.45` | 110,140,000.00 USD | 64,210.00 USD | 0.00 USD | `+90.89%` | `350.00` |
| `Live` | `Short` | `184.15` | 110,150,000.00 USD | 7,630.00 USD | 0.00 USD | `+91.62%` | `41.43` |
| `Live` | `Short` | `184.25` | 110,150,000.00 USD | 3,070.00 USD | 0.00 USD | `+91.72%` | `16.67` |
| `Live` | `Short` | `184.95` | 110,320,000.00 USD | 165,230.00 USD | 0.00 USD | `+92.45%` | `893.35` |
| `Live` | `Short` | `185.15` | 110,320,000.00 USD | 251.80 USD | 0.00 USD | `+92.66%` | `1.36` |
| `Live` | `Short` | `185.25` | 110,320,000.00 USD | 737.29 USD | 0.00 USD | `+92.76%` | `3.98` |
| `Live` | `Short` | `185.45` | 110,320,000.00 USD | 2,770.00 USD | 0.00 USD | `+92.97%` | `14.94` |
| `Live` | `Short` | `185.55` | 110,320,000.00 USD | 983.42 USD | 0.00 USD | `+93.07%` | `5.30` |
| `Live` | `Short` | `185.65` | 110,320,000.00 USD | 137.38 USD | 0.00 USD | `+93.18%` | `0.74` |
| `Live` | `Short` | `185.75` | 110,320,000.00 USD | 247.05 USD | 0.00 USD | `+93.28%` | `1.33` |
| `Live` | `Short` | `186.45` | 110,320,000.00 USD | 2,310.00 USD | 0.00 USD | `+94.01%` | `12.37` |
| `Live` | `Short` | `187.35` | 110,320,000.00 USD | 232.31 USD | 0.00 USD | `+94.95%` | `1.24` |
| `Live` | `Short` | `187.75` | 110,320,000.00 USD | 2,110.00 USD | 0.00 USD | `+95.36%` | `11.24` |
| `Live` | `Short` | `188.05` | 110,340,000.00 USD | 19,290.00 USD | 0.00 USD | `+95.67%` | `102.58` |
| `Live` | `Short` | `188.45` | 110,630,000.00 USD | 282,600.00 USD | 0.00 USD | `+96.09%` | `1,499.60` |
| `Live` | `Short` | `188.55` | 110,640,000.00 USD | 9,980.00 USD | 0.00 USD | `+96.19%` | `52.95` |
| `Live` | `Short` | `188.95` | 110,640,000.00 USD | 1,450.00 USD | 0.00 USD | `+96.61%` | `7.69` |
| `Live` | `Short` | `189.05` | 110,640,000.00 USD | 5,360.00 USD | 0.00 USD | `+96.71%` | `28.34` |
| `Live` | `Short` | `189.15` | 110,650,000.00 USD | 10,850.00 USD | 0.00 USD | `+96.82%` | `57.38` |
| `Live` | `Short` | `189.25` | 110,650,000.00 USD | 456.09 USD | 0.00 USD | `+96.92%` | `2.41` |
| `Live` | `Short` | `189.95` | 110,940,000.00 USD | 284,930.00 USD | 0.00 USD | `+97.65%` | `1,500.00` |
| `Live` | `Short` | `190.05` | 111,320,000.00 USD | 380,100.00 USD | 0.00 USD | `+97.75%` | `2,000.00` |
| `Live` | `Short` | `190.15` | 111,320,000.00 USD | 1,330.00 USD | 0.00 USD | `+97.86%` | `7.00` |
| `Live` | `Short` | `190.25` | 111,320,000.00 USD | 117.95 USD | 0.00 USD | `+97.96%` | `0.62` |
| `Live` | `Short` | `190.95` | 124,890,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+98.69%` | `71,044.42` |
| `Live` | `Short` | `191.95` | 124,890,000.00 USD | 322.48 USD | 0.00 USD | `+99.73%` | `1.68` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 8,130,000.00 USD | 0.00 USD | 13,590.00 USD | `-76.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 8,120,000.00 USD | 0.00 USD | 3,760.00 USD | `-73.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `26.15` | 8,110,000.00 USD | 0.00 USD | 103.82 USD | `-72.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 8,110,000.00 USD | 0.00 USD | 519.56 USD | `-68.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 8,110,000.00 USD | 0.00 USD | 499.56 USD | `-68.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 8,110,000.00 USD | 0.00 USD | 818.32 USD | `-65.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 8,110,000.00 USD | 0.00 USD | 1,340.00 USD | `-63.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 8,110,000.00 USD | 0.00 USD | 201.74 USD | `-60.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 8,110,000.00 USD | 0.00 USD | 150.30 USD | `-60.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.65` | 8,110,000.00 USD | 0.00 USD | 206.00 USD | `-59.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 8,110,000.00 USD | 0.00 USD | 208.14 USD | `-59.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 8,110,000.00 USD | 0.00 USD | 3,460.00 USD | `-58.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 8,110,000.00 USD | 0.00 USD | 157.01 USD | `-58.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 8,110,000.00 USD | 0.00 USD | 418.92 USD | `-58.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 8,110,000.00 USD | 0.00 USD | 170,530.00 USD | `-55.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 7,940,000.00 USD | 0.00 USD | 105.00 USD | `-54.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 7,940,000.00 USD | 0.00 USD | 63,450.00 USD | `-53.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 7,870,000.00 USD | 0.00 USD | 251.05 USD | `-51.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 7,870,000.00 USD | 0.00 USD | 143.25 USD | `-50.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 7,870,000.00 USD | 0.00 USD | 191.40 USD | `-50.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 7,870,000.00 USD | 0.00 USD | 103.35 USD | `-49.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 7,870,000.00 USD | 0.00 USD | 4,660.00 USD | `-47.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 7,870,000.00 USD | 0.00 USD | 107.03 USD | `-47.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 7,870,000.00 USD | 0.00 USD | 102.62 USD | `-47.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 7,870,000.00 USD | 0.00 USD | 134.28 USD | `-46.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 7,870,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 7,860,000.00 USD | 0.00 USD | 102.74 USD | `-45.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 7,860,000.00 USD | 0.00 USD | 126.12 USD | `-45.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 7,860,000.00 USD | 0.00 USD | 200.15 USD | `-44.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 7,860,000.00 USD | 0.00 USD | 24,450.00 USD | `-44.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 7,840,000.00 USD | 0.00 USD | 2,140.00 USD | `-44.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 7,840,000.00 USD | 0.00 USD | 641.57 USD | `-43.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 7,840,000.00 USD | 0.00 USD | 139.87 USD | `-42.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 7,830,000.00 USD | 0.00 USD | 209.19 USD | `-42.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 7,830,000.00 USD | 0.00 USD | 894.56 USD | `-41.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 7,830,000.00 USD | 0.00 USD | 4,930.00 USD | `-41.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 7,830,000.00 USD | 0.00 USD | 6,500.00 USD | `-40.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 7,820,000.00 USD | 0.00 USD | 158.48 USD | `-39.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 7,820,000.00 USD | 0.00 USD | 428.72 USD | `-39.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 7,820,000.00 USD | 0.00 USD | 236.20 USD | `-38.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 7,820,000.00 USD | 0.00 USD | 200.01 USD | `-38.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 7,820,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 7,820,000.00 USD | 0.00 USD | 9,040.00 USD | `-37.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 7,810,000.00 USD | 0.00 USD | 33,220.00 USD | `-37.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 7,780,000.00 USD | 0.00 USD | 488.63 USD | `-37.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 7,780,000.00 USD | 0.00 USD | 258.90 USD | `-37.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 7,780,000.00 USD | 0.00 USD | 6,200.00 USD | `-37.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 7,770,000.00 USD | 0.00 USD | 551.61 USD | `-37.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 7,770,000.00 USD | 0.00 USD | 18,360.00 USD | `-36.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 7,750,000.00 USD | 0.00 USD | 142.33 USD | `-36.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 7,750,000.00 USD | 0.00 USD | 100.78 USD | `-36.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 7,750,000.00 USD | 0.00 USD | 243.74 USD | `-35.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 7,750,000.00 USD | 0.00 USD | 4,640.00 USD | `-35.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 7,750,000.00 USD | 0.00 USD | 136.98 USD | `-34.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 7,750,000.00 USD | 0.00 USD | 12,950.00 USD | `-34.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 7,730,000.00 USD | 0.00 USD | 2,980.00 USD | `-33.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 7,730,000.00 USD | 0.00 USD | 222.55 USD | `-33.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 7,730,000.00 USD | 0.00 USD | 163.19 USD | `-33.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 7,730,000.00 USD | 0.00 USD | 129.70 USD | `-32.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 7,730,000.00 USD | 0.00 USD | 2,440.00 USD | `-32.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 7,730,000.00 USD | 0.00 USD | 2,190.00 USD | `-32.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 7,730,000.00 USD | 0.00 USD | 2,200.00 USD | `-31.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 7,720,000.00 USD | 0.00 USD | 9,140.00 USD | `-31.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 7,710,000.00 USD | 0.00 USD | 541.72 USD | `-30.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 7,710,000.00 USD | 0.00 USD | 335.25 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 7,710,000.00 USD | 0.00 USD | 268.60 USD | `-30.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.85` | 7,710,000.00 USD | 0.00 USD | 303.29 USD | `-29.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 7,710,000.00 USD | 0.00 USD | 18,940.00 USD | `-29.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 7,690,000.00 USD | 0.00 USD | 5,610.00 USD | `-28.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 7,690,000.00 USD | 0.00 USD | 359.04 USD | `-28.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 7,690,000.00 USD | 0.00 USD | 1,200.00 USD | `-28.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 7,690,000.00 USD | 0.00 USD | 20,210.00 USD | `-28.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 7,670,000.00 USD | 0.00 USD | 172.18 USD | `-28.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 7,670,000.00 USD | 0.00 USD | 668.96 USD | `-27.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 7,670,000.00 USD | 0.00 USD | 107.96 USD | `-27.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 7,670,000.00 USD | 0.00 USD | 42,360.00 USD | `-27.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 7,620,000.00 USD | 0.00 USD | 365.32 USD | `-27.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 7,620,000.00 USD | 0.00 USD | 1,510.00 USD | `-27.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 7,620,000.00 USD | 0.00 USD | 36,240.00 USD | `-27.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 7,580,000.00 USD | 0.00 USD | 5,270.00 USD | `-26.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 7,580,000.00 USD | 0.00 USD | 562.80 USD | `-26.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 7,580,000.00 USD | 0.00 USD | 681.51 USD | `-26.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 7,580,000.00 USD | 0.00 USD | 4,920.00 USD | `-26.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 7,570,000.00 USD | 0.00 USD | 2,790.00 USD | `-26.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 7,570,000.00 USD | 0.00 USD | 265.02 USD | `-26.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 7,570,000.00 USD | 0.00 USD | 32,390.00 USD | `-25.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 7,540,000.00 USD | 0.00 USD | 289.37 USD | `-25.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.55` | 7,540,000.00 USD | 0.00 USD | 1,170.00 USD | `-25.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 7,540,000.00 USD | 0.00 USD | 913.54 USD | `-25.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 7,540,000.00 USD | 0.00 USD | 5,900.00 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 7,530,000.00 USD | 0.00 USD | 19,560.00 USD | `-24.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 7,510,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 7,440,000.00 USD | 0.00 USD | 139.56 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 7,440,000.00 USD | 0.00 USD | 510.95 USD | `-22.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 7,440,000.00 USD | 0.00 USD | 1,660.00 USD | `-22.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 7,440,000.00 USD | 0.00 USD | 10,730.00 USD | `-22.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 7,430,000.00 USD | 0.00 USD | 331.00 USD | `-22.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 7,430,000.00 USD | 0.00 USD | 28,050.00 USD | `-22.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 7,400,000.00 USD | 0.00 USD | 19,030.00 USD | `-21.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 7,380,000.00 USD | 0.00 USD | 2,220.00 USD | `-21.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 7,380,000.00 USD | 0.00 USD | 277.98 USD | `-20.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 7,380,000.00 USD | 0.00 USD | 28,850.00 USD | `-20.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 7,350,000.00 USD | 0.00 USD | 254.34 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 7,350,000.00 USD | 0.00 USD | 486.47 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 7,350,000.00 USD | 0.00 USD | 4,340.00 USD | `-20.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 7,350,000.00 USD | 0.00 USD | 536.55 USD | `-20.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 7,350,000.00 USD | 0.00 USD | 251.74 USD | `-20.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.95` | 7,350,000.00 USD | 0.00 USD | 320.11 USD | `-19.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 7,350,000.00 USD | 0.00 USD | 18,220.00 USD | `-19.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 7,330,000.00 USD | 0.00 USD | 5,690.00 USD | `-19.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 7,320,000.00 USD | 0.00 USD | 155.12 USD | `-18.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 7,320,000.00 USD | 0.00 USD | 56,050.00 USD | `-18.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 7,270,000.00 USD | 0.00 USD | 494.69 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 7,270,000.00 USD | 0.00 USD | 18,590.00 USD | `-18.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 7,250,000.00 USD | 0.00 USD | 379.58 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 7,250,000.00 USD | 0.00 USD | 4,660.00 USD | `-17.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 7,240,000.00 USD | 0.00 USD | 381.50 USD | `-17.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 7,240,000.00 USD | 0.00 USD | 1,750.00 USD | `-17.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 7,240,000.00 USD | 0.00 USD | 5,850.00 USD | `-17.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 7,230,000.00 USD | 0.00 USD | 238.95 USD | `-17.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 7,230,000.00 USD | 0.00 USD | 808.29 USD | `-16.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 7,230,000.00 USD | 0.00 USD | 42,140.00 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 7,190,000.00 USD | 0.00 USD | 1,620.00 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 7,190,000.00 USD | 0.00 USD | 5,830.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 7,180,000.00 USD | 0.00 USD | 295.21 USD | `-15.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 7,180,000.00 USD | 0.00 USD | 160.03 USD | `-15.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 7,180,000.00 USD | 0.00 USD | 1,390.00 USD | `-14.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 7,180,000.00 USD | 0.00 USD | 71,590.00 USD | `-14.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 7,110,000.00 USD | 0.00 USD | 3,220.00 USD | `-14.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 7,110,000.00 USD | 0.00 USD | 684.31 USD | `-14.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 7,110,000.00 USD | 0.00 USD | 1,570.00 USD | `-14.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 7,100,000.00 USD | 0.00 USD | 2,480.00 USD | `-14.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 7,100,000.00 USD | 0.00 USD | 12,040.00 USD | `-13.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 7,090,000.00 USD | 0.00 USD | 6,040.00 USD | `-13.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 7,080,000.00 USD | 0.00 USD | 239.47 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 7,080,000.00 USD | 0.00 USD | 18,330.00 USD | `-13.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 7,070,000.00 USD | 0.00 USD | 45,830.00 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 7,020,000.00 USD | 0.00 USD | 421.09 USD | `-13.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 7,020,000.00 USD | 0.00 USD | 1,370.00 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 7,020,000.00 USD | 0.00 USD | 1,320.00 USD | `-12.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 7,020,000.00 USD | 0.00 USD | 426.47 USD | `-12.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 7,020,000.00 USD | 0.00 USD | 22,080.00 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 6,990,000.00 USD | 0.00 USD | 3,490.00 USD | `-12.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 6,990,000.00 USD | 0.00 USD | 2,690.00 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 6,990,000.00 USD | 0.00 USD | 165.52 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 6,990,000.00 USD | 0.00 USD | 169.95 USD | `-12.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 6,990,000.00 USD | 0.00 USD | 519.75 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 6,990,000.00 USD | 0.00 USD | 306.80 USD | `-11.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 6,990,000.00 USD | 0.00 USD | 1,350.00 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 6,990,000.00 USD | 0.00 USD | 165,510.00 USD | `-11.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 6,820,000.00 USD | 0.00 USD | 437.67 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 6,820,000.00 USD | 0.00 USD | 1,320.00 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 6,820,000.00 USD | 0.00 USD | 915.81 USD | `-11.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 6,820,000.00 USD | 0.00 USD | 120.48 USD | `-11.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 6,820,000.00 USD | 0.00 USD | 105.23 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 6,820,000.00 USD | 0.00 USD | 310.05 USD | `-10.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 6,820,000.00 USD | 0.00 USD | 142.34 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 6,820,000.00 USD | 0.00 USD | 1,370.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 6,810,000.00 USD | 0.00 USD | 604.23 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 6,810,000.00 USD | 0.00 USD | 5,710.00 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 6,810,000.00 USD | 0.00 USD | 2,210.00 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 6,810,000.00 USD | 0.00 USD | 538.20 USD | `-10.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 6,810,000.00 USD | 0.00 USD | 4,080.00 USD | `-10.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 6,800,000.00 USD | 0.00 USD | 2,540.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 6,800,000.00 USD | 0.00 USD | 417.17 USD | `-9.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 6,800,000.00 USD | 0.00 USD | 305.87 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 6,800,000.00 USD | 0.00 USD | 2,020.00 USD | `-9.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 6,800,000.00 USD | 0.00 USD | 788.60 USD | `-9.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 6,800,000.00 USD | 0.00 USD | 132.16 USD | `-9.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 6,800,000.00 USD | 0.00 USD | 499,320.00 USD | `-9.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 6,300,000.00 USD | 0.00 USD | 435.75 USD | `-9.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 6,300,000.00 USD | 0.00 USD | 8,200.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 6,290,000.00 USD | 0.00 USD | 436.75 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 6,290,000.00 USD | 0.00 USD | 730.21 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 6,290,000.00 USD | 0.00 USD | 316.93 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 6,290,000.00 USD | 0.00 USD | 2,880.00 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 6,280,000.00 USD | 0.00 USD | 177.66 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 6,280,000.00 USD | 0.00 USD | 83,740.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 6,200,000.00 USD | 0.00 USD | 1,050.00 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 6,200,000.00 USD | 0.00 USD | 8,860.00 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 6,190,000.00 USD | 0.00 USD | 29,150.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 6,160,000.00 USD | 0.00 USD | 1,010.00 USD | `-7.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 6,160,000.00 USD | 0.00 USD | 7,610.00 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 6,150,000.00 USD | 0.00 USD | 27,220.00 USD | `-7.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 6,120,000.00 USD | 0.00 USD | 53,250.00 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 6,070,000.00 USD | 0.00 USD | 95,650.00 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 5,980,000.00 USD | 0.00 USD | 141.43 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 5,980,000.00 USD | 0.00 USD | 9,280.00 USD | `-7.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 5,970,000.00 USD | 0.00 USD | 6,470.00 USD | `-7.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 5,960,000.00 USD | 0.00 USD | 960.33 USD | `-7.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 5,960,000.00 USD | 0.00 USD | 615.62 USD | `-7.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 5,960,000.00 USD | 0.00 USD | 10,360.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 5,950,000.00 USD | 0.00 USD | 348.35 USD | `-6.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 5,950,000.00 USD | 0.00 USD | 173.02 USD | `-6.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 5,950,000.00 USD | 0.00 USD | 105.01 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 5,950,000.00 USD | 0.00 USD | 20,850.00 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 5,930,000.00 USD | 0.00 USD | 15,250.00 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 5,910,000.00 USD | 0.00 USD | 692,860.00 USD | `-6.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 5,220,000.00 USD | 0.00 USD | 180.30 USD | `-6.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 5,220,000.00 USD | 0.00 USD | 13,600.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 5,200,000.00 USD | 0.00 USD | 5,610.00 USD | `-5.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 5,200,000.00 USD | 0.00 USD | 109,540.00 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 5,090,000.00 USD | 0.00 USD | 663.56 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 5,090,000.00 USD | 0.00 USD | 4,370.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 5,080,000.00 USD | 0.00 USD | 9,110.00 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 5,070,000.00 USD | 0.00 USD | 70,580.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 5,000,000.00 USD | 0.00 USD | 519.56 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 5,000,000.00 USD | 0.00 USD | 5,840.00 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 5,000,000.00 USD | 0.00 USD | 330.13 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 5,000,000.00 USD | 0.00 USD | 343,420.00 USD | `-4.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 4,650,000.00 USD | 0.00 USD | 27,950.00 USD | `-4.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 4,630,000.00 USD | 0.00 USD | 2,450.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 4,620,000.00 USD | 0.00 USD | 14,200.00 USD | `-4.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 4,610,000.00 USD | 0.00 USD | 19,310.00 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 4,590,000.00 USD | 0.00 USD | 30,500.00 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 4,560,000.00 USD | 0.00 USD | 1,470.00 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 4,560,000.00 USD | 0.00 USD | 139.30 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 4,560,000.00 USD | 0.00 USD | 7,570.00 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 4,550,000.00 USD | 0.00 USD | 129.43 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 4,550,000.00 USD | 0.00 USD | 2,540.00 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 4,550,000.00 USD | 0.00 USD | 791.23 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 4,550,000.00 USD | 0.00 USD | 2,510.00 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 4,540,000.00 USD | 0.00 USD | 28,600.00 USD | `-3.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 4,520,000.00 USD | 0.00 USD | 5,800.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 4,510,000.00 USD | 0.00 USD | 26,470.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 4,480,000.00 USD | 0.00 USD | 4,130.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 4,480,000.00 USD | 0.00 USD | 1,380.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 4,480,000.00 USD | 0.00 USD | 969.91 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 4,480,000.00 USD | 0.00 USD | 20,050.00 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 4,460,000.00 USD | 0.00 USD | 591,220.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 3,870,000.00 USD | 0.00 USD | 452,890.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 3,410,000.00 USD | 0.00 USD | 7,410.00 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 3,410,000.00 USD | 0.00 USD | 3,310.00 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 3,400,000.00 USD | 0.00 USD | 28,990.00 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 3,370,000.00 USD | 0.00 USD | 507,270.00 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 2,870,000.00 USD | 0.00 USD | 11,300.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 2,850,000.00 USD | 0.00 USD | 2,870.00 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 2,850,000.00 USD | 0.00 USD | 6,550.00 USD | `-1.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 2,850,000.00 USD | 0.00 USD | 39,300.00 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 2,810,000.00 USD | 0.00 USD | 140,020.00 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 2,670,000.00 USD | 0.00 USD | 62,800.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 2,600,000.00 USD | 0.00 USD | 77,160.00 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 2,530,000.00 USD | 0.00 USD | 1,960,000.00 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 561,670.00 USD | 0.00 USD | 9,700.00 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 551,970.00 USD | 0.00 USD | 93,350.00 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 458,620.00 USD | 0.00 USD | 5,740.00 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 452,880.00 USD | 0.00 USD | 101,170.00 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 351,720.00 USD | 0.00 USD | 37,500.00 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 314,220.00 USD | 0.00 USD | 202.35 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 314,010.00 USD | 0.00 USD | 15,400.00 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 298,610.00 USD | 0.00 USD | 691.55 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 297,920.00 USD | 0.00 USD | 11,060.00 USD | `-0.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 286,860.00 USD | 0.00 USD | 268,370.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 18,500.00 USD | 0.00 USD | 9,640.00 USD | `-0.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 8,860.00 USD | 0.00 USD | 8,860.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.15` | 884.58 USD | 884.58 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.25` | 1,080.00 USD | 199.24 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.35` | 7,570.00 USD | 6,480.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.45` | 8,050.00 USD | 487.07 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.55` | 15,960.00 USD | 7,910.00 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.65` | 16,300.00 USD | 341.17 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.75` | 43,900.00 USD | 27,600.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.85` | 46,420.00 USD | 2,520.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.95` | 47,950.00 USD | 1,530.00 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.05` | 60,940.00 USD | 12,990.00 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.15` | 78,630.00 USD | 17,690.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.25` | 105,340.00 USD | 26,700.00 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 117,500.00 USD | 12,170.00 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 119,360.00 USD | 1,860.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 126,420.00 USD | 7,060.00 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 151,130.00 USD | 24,710.00 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 151,530.00 USD | 391.00 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 183,870.00 USD | 32,350.00 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 205,700.00 USD | 21,830.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 298,020.00 USD | 92,320.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 365,540.00 USD | 67,520.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 367,130.00 USD | 1,590.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 407,340.00 USD | 40,210.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 457,450.00 USD | 50,110.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 552,850.00 USD | 95,400.00 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 568,740.00 USD | 15,890.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 604,590.00 USD | 35,850.00 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 605,250.00 USD | 666.25 USD | 0.00 USD | `+2.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 605,410.00 USD | 157.33 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 777,630.00 USD | 172,220.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 778,440.00 USD | 803.12 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 779,540.00 USD | 1,110.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 787,150.00 USD | 7,600.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 787,810.00 USD | 663.33 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 808,190.00 USD | 20,380.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 866,340.00 USD | 58,150.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 914,150.00 USD | 47,810.00 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 914,560.00 USD | 415.38 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 914,830.00 USD | 263.87 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 949,580.00 USD | 34,760.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 955,140.00 USD | 5,550.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 962,800.00 USD | 7,670.00 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 964,850.00 USD | 2,050.00 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 969,510.00 USD | 4,670.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 973,700.00 USD | 4,180.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 983,890.00 USD | 10,190.00 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 1,000,000.00 USD | 18,230.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 1,000,000.00 USD | 703.93 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 1,010,000.00 USD | 2,800.00 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 1,580,000.00 USD | 570,690.00 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 1,850,000.00 USD | 273,410.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 1,860,000.00 USD | 6,640.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 1,870,000.00 USD | 17,190.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 1,880,000.00 USD | 5,850.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 1,890,000.00 USD | 9,690.00 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 1,890,000.00 USD | 116.90 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 1,890,000.00 USD | 642.04 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 1,890,000.00 USD | 1,420.00 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 1,890,000.00 USD | 1,990.00 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,940,000.00 USD | 50,180.00 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 1,940,000.00 USD | 417.79 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 1,950,000.00 USD | 6,530.00 USD | 0.00 USD | `+6.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 2,570,000.00 USD | 616,660.00 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 2,570,000.00 USD | 4,360.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 2,600,000.00 USD | 28,660.00 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 2,610,000.00 USD | 9,410.00 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 2,610,000.00 USD | 1,810.00 USD | 0.00 USD | `+6.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 2,630,000.00 USD | 21,080.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 2,640,000.00 USD | 3,430.00 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 2,670,000.00 USD | 33,680.00 USD | 0.00 USD | `+7.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 2,840,000.00 USD | 166,600.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 2,940,000.00 USD | 103,250.00 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 2,950,000.00 USD | 8,090.00 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 2,950,000.00 USD | 3,760.00 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 2,950,000.00 USD | 2,650.00 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 2,960,000.00 USD | 2,660.00 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 2,960,000.00 USD | 464.80 USD | 0.00 USD | `+7.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 3,210,000.00 USD | 251,550.00 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 3,270,000.00 USD | 60,410.00 USD | 0.00 USD | `+8.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 3,520,000.00 USD | 250,650.00 USD | 0.00 USD | `+8.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 3,520,000.00 USD | 1,710.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 3,520,000.00 USD | 1,460.00 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 3,520,000.00 USD | 146.09 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 3,530,000.00 USD | 5,400.00 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 3,540,000.00 USD | 11,050.00 USD | 0.00 USD | `+8.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 3,560,000.00 USD | 21,730.00 USD | 0.00 USD | `+8.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 3,560,000.00 USD | 1,100.00 USD | 0.00 USD | `+9.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 3,570,000.00 USD | 5,900.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 3,590,000.00 USD | 25,930.00 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 3,650,000.00 USD | 56,300.00 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 3,680,000.00 USD | 27,500.00 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 3,680,000.00 USD | 1,210.00 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 3,680,000.00 USD | 1,110.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 3,680,000.00 USD | 1,680.00 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 3,690,000.00 USD | 3,620.00 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 3,690,000.00 USD | 235.60 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 3,700,000.00 USD | 10,860.00 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 3,710,000.00 USD | 11,960.00 USD | 0.00 USD | `+10.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 3,710,000.00 USD | 332.68 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 3,750,000.00 USD | 45,750.00 USD | 0.00 USD | `+10.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 3,760,000.00 USD | 9,170.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 3,760,000.00 USD | 935.00 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 3,850,000.00 USD | 82,160.00 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 3,870,000.00 USD | 26,280.00 USD | 0.00 USD | `+10.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 3,880,000.00 USD | 7,800.00 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 3,880,000.00 USD | 355.14 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 3,990,000.00 USD | 110,390.00 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 3,990,000.00 USD | 1,000.00 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 4,020,000.00 USD | 24,340.00 USD | 0.00 USD | `+11.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 4,030,000.00 USD | 15,880.00 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 4,030,000.00 USD | 1,200.00 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 4,050,000.00 USD | 20,190.00 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 4,050,000.00 USD | 212.55 USD | 0.00 USD | `+11.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 4,060,000.00 USD | 8,930.00 USD | 0.00 USD | `+11.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 4,130,000.00 USD | 65,130.00 USD | 0.00 USD | `+11.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 4,190,000.00 USD | 65,380.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 4,200,000.00 USD | 2,140.00 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 4,200,000.00 USD | 4,520.00 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 4,200,000.00 USD | 930.53 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 4,270,000.00 USD | 63,540.00 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 4,330,000.00 USD | 68,190.00 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.25` | 4,330,000.00 USD | 1,240.00 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 4,340,000.00 USD | 9,700.00 USD | 0.00 USD | `+12.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 4,350,000.00 USD | 3,920.00 USD | 0.00 USD | `+12.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 4,350,000.00 USD | 6,140.00 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 4,360,000.00 USD | 2,310.00 USD | 0.00 USD | `+13.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 4,360,000.00 USD | 2,120.00 USD | 0.00 USD | `+13.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 4,360,000.00 USD | 3,260.00 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 4,400,000.00 USD | 42,240.00 USD | 0.00 USD | `+13.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 4,430,000.00 USD | 21,010.00 USD | 0.00 USD | `+13.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 4,430,000.00 USD | 8,620.00 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 8,500,000.00 USD | 4,070,000.00 USD | 0.00 USD | `+13.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 8,550,000.00 USD | 44,780.00 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 8,570,000.00 USD | 18,790.00 USD | 0.00 USD | `+13.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 8,570,000.00 USD | 1,170.00 USD | 0.00 USD | `+13.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 8,570,000.00 USD | 5,300.00 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 8,580,000.00 USD | 4,370.00 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 8,580,000.00 USD | 1,210.00 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 8,580,000.00 USD | 357.34 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 9,180,000.00 USD | 596,990.00 USD | 0.00 USD | `+14.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 9,180,000.00 USD | 340.36 USD | 0.00 USD | `+14.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 9,180,000.00 USD | 6,610.00 USD | 0.00 USD | `+14.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 9,180,000.00 USD | 1,610.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 9,190,000.00 USD | 1,580.00 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 9,200,000.00 USD | 10,820.00 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 9,200,000.00 USD | 3,030.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 9,220,000.00 USD | 17,520.00 USD | 0.00 USD | `+15.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 9,450,000.00 USD | 227,610.00 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 9,450,000.00 USD | 799.56 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 9,450,000.00 USD | 1,300.00 USD | 0.00 USD | `+15.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 9,450,000.00 USD | 5,910.00 USD | 0.00 USD | `+15.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 9,450,000.00 USD | 842.56 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 9,460,000.00 USD | 3,440.00 USD | 0.00 USD | `+16.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 9,460,000.00 USD | 106.07 USD | 0.00 USD | `+16.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 9,470,000.00 USD | 13,510.00 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 9,470,000.00 USD | 2,100.00 USD | 0.00 USD | `+16.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.95` | 9,470,000.00 USD | 559.75 USD | 0.00 USD | `+16.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 9,490,000.00 USD | 17,410.00 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 9,540,000.00 USD | 49,680.00 USD | 0.00 USD | `+16.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 9,550,000.00 USD | 4,960.00 USD | 0.00 USD | `+16.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 9,550,000.00 USD | 4,920.00 USD | 0.00 USD | `+16.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 9,550,000.00 USD | 2,290.00 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 9,590,000.00 USD | 36,280.00 USD | 0.00 USD | `+17.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 9,590,000.00 USD | 1,690.00 USD | 0.00 USD | `+17.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 9,590,000.00 USD | 586.82 USD | 0.00 USD | `+17.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 9,670,000.00 USD | 81,750.00 USD | 0.00 USD | `+17.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.15` | 9,670,000.00 USD | 427.71 USD | 0.00 USD | `+17.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 9,670,000.00 USD | 349.94 USD | 0.00 USD | `+17.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 9,800,000.00 USD | 128,070.00 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 9,800,000.00 USD | 655.74 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 9,810,000.00 USD | 4,470.00 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 9,810,000.00 USD | 230.71 USD | 0.00 USD | `+18.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 9,810,000.00 USD | 257.07 USD | 0.00 USD | `+18.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 9,810,000.00 USD | 4,540.00 USD | 0.00 USD | `+18.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 9,810,000.00 USD | 1,970.00 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 9,830,000.00 USD | 11,410.00 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 9,830,000.00 USD | 584.96 USD | 0.00 USD | `+18.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 9,840,000.00 USD | 9,320.00 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 9,840,000.00 USD | 343.35 USD | 0.00 USD | `+19.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 9,840,000.00 USD | 5,150.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 9,850,000.00 USD | 11,800.00 USD | 0.00 USD | `+19.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 9,850,000.00 USD | 1,010.00 USD | 0.00 USD | `+19.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 9,860,000.00 USD | 1,380.00 USD | 0.00 USD | `+19.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 9,940,000.00 USD | 81,650.00 USD | 0.00 USD | `+19.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 9,940,000.00 USD | 139.57 USD | 0.00 USD | `+20.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 9,960,000.00 USD | 23,260.00 USD | 0.00 USD | `+20.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 9,960,000.00 USD | 2,210.00 USD | 0.00 USD | `+20.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 9,960,000.00 USD | 579.25 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 9,980,000.00 USD | 20,280.00 USD | 0.00 USD | `+20.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 9,990,000.00 USD | 1,730.00 USD | 0.00 USD | `+20.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 9,990,000.00 USD | 3,840.00 USD | 0.00 USD | `+20.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 9,990,000.00 USD | 4,160.00 USD | 0.00 USD | `+21.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 10,000,000.00 USD | 10,810.00 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 10,010,000.00 USD | 1,100.00 USD | 0.00 USD | `+21.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 10,010,000.00 USD | 3,580.00 USD | 0.00 USD | `+21.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 10,010,000.00 USD | 234.87 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 10,010,000.00 USD | 1,170.00 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 10,010,000.00 USD | 3,740.00 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 10,010,000.00 USD | 686.50 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 10,010,000.00 USD | 349.40 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 10,020,000.00 USD | 2,330.00 USD | 0.00 USD | `+22.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 10,120,000.00 USD | 98,960.00 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 10,220,000.00 USD | 105,720.00 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 10,230,000.00 USD | 5,920.00 USD | 0.00 USD | `+22.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 10,280,000.00 USD | 55,580.00 USD | 0.00 USD | `+22.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 10,350,000.00 USD | 69,920.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 10,370,000.00 USD | 13,120.00 USD | 0.00 USD | `+22.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 10,370,000.00 USD | 3,090.00 USD | 0.00 USD | `+23.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 10,380,000.00 USD | 12,610.00 USD | 0.00 USD | `+23.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 10,380,000.00 USD | 707.15 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 10,450,000.00 USD | 70,980.00 USD | 0.00 USD | `+23.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 10,450,000.00 USD | 593.25 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 10,450,000.00 USD | 403.75 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 10,470,000.00 USD | 15,940.00 USD | 0.00 USD | `+23.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 10,510,000.00 USD | 42,290.00 USD | 0.00 USD | `+23.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 10,570,000.00 USD | 54,610.00 USD | 0.00 USD | `+23.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 10,580,000.00 USD | 8,120.00 USD | 0.00 USD | `+23.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 10,580,000.00 USD | 2,050.00 USD | 0.00 USD | `+24.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 10,580,000.00 USD | 5,330.00 USD | 0.00 USD | `+24.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 10,590,000.00 USD | 3,580.00 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 10,590,000.00 USD | 615.00 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 10,710,000.00 USD | 125,500.00 USD | 0.00 USD | `+24.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 10,750,000.00 USD | 37,630.00 USD | 0.00 USD | `+24.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 10,750,000.00 USD | 458.21 USD | 0.00 USD | `+24.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 10,870,000.00 USD | 117,190.00 USD | 0.00 USD | `+24.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 10,870,000.00 USD | 414.52 USD | 0.00 USD | `+25.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 10,870,000.00 USD | 3,210.00 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 10,880,000.00 USD | 7,850.00 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 10,880,000.00 USD | 184.29 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 10,880,000.00 USD | 964.40 USD | 0.00 USD | `+25.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 10,880,000.00 USD | 191.83 USD | 0.00 USD | `+25.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 10,880,000.00 USD | 2,150.00 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 10,880,000.00 USD | 650.17 USD | 0.00 USD | `+25.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 10,900,000.00 USD | 20,950.00 USD | 0.00 USD | `+25.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 10,900,000.00 USD | 122.36 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 10,910,000.00 USD | 8,780.00 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 10,930,000.00 USD | 11,570.00 USD | 0.00 USD | `+26.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 10,930,000.00 USD | 8,460.00 USD | 0.00 USD | `+26.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 10,940,000.00 USD | 4,360.00 USD | 0.00 USD | `+26.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 10,940,000.00 USD | 2,450.00 USD | 0.00 USD | `+26.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 10,950,000.00 USD | 7,600.00 USD | 0.00 USD | `+26.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 10,960,000.00 USD | 12,910.00 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 11,160,000.00 USD | 195,460.00 USD | 0.00 USD | `+27.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 11,160,000.00 USD | 2,370.00 USD | 0.00 USD | `+27.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 11,390,000.00 USD | 235,280.00 USD | 0.00 USD | `+27.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 11,450,000.00 USD | 52,320.00 USD | 0.00 USD | `+27.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 11,450,000.00 USD | 4,880.00 USD | 0.00 USD | `+27.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 11,460,000.00 USD | 7,020.00 USD | 0.00 USD | `+27.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 11,470,000.00 USD | 11,000.00 USD | 0.00 USD | `+27.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 11,470,000.00 USD | 235.68 USD | 0.00 USD | `+27.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 11,470,000.00 USD | 3,780.00 USD | 0.00 USD | `+27.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 11,480,000.00 USD | 10,560.00 USD | 0.00 USD | `+27.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 12,490,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 12,490,000.00 USD | 252.46 USD | 0.00 USD | `+28.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 12,500,000.00 USD | 7,710.00 USD | 0.00 USD | `+28.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 12,500,000.00 USD | 6,790.00 USD | 0.00 USD | `+28.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 12,500,000.00 USD | 2,670.00 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 12,510,000.00 USD | 632.58 USD | 0.00 USD | `+28.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 12,520,000.00 USD | 11,600.00 USD | 0.00 USD | `+28.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 12,530,000.00 USD | 11,530.00 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 12,550,000.00 USD | 18,820.00 USD | 0.00 USD | `+28.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 12,620,000.00 USD | 68,330.00 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 12,620,000.00 USD | 1,320.00 USD | 0.00 USD | `+29.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 12,620,000.00 USD | 144.13 USD | 0.00 USD | `+29.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 12,620,000.00 USD | 4,110.00 USD | 0.00 USD | `+29.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 12,620,000.00 USD | 1,370.00 USD | 0.00 USD | `+29.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 12,630,000.00 USD | 7,330.00 USD | 0.00 USD | `+29.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 12,640,000.00 USD | 6,610.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 12,640,000.00 USD | 344.59 USD | 0.00 USD | `+29.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 12,650,000.00 USD | 11,310.00 USD | 0.00 USD | `+30.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 13,120,000.00 USD | 469,290.00 USD | 0.00 USD | `+30.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 13,120,000.00 USD | 178.96 USD | 0.00 USD | `+30.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 13,120,000.00 USD | 311.87 USD | 0.00 USD | `+30.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 13,120,000.00 USD | 1,310.00 USD | 0.00 USD | `+30.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 13,120,000.00 USD | 3,320.00 USD | 0.00 USD | `+30.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 13,140,000.00 USD | 16,280.00 USD | 0.00 USD | `+30.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 13,140,000.00 USD | 471.94 USD | 0.00 USD | `+30.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 13,140,000.00 USD | 209.08 USD | 0.00 USD | `+31.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 13,290,000.00 USD | 151,060.00 USD | 0.00 USD | `+31.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 13,300,000.00 USD | 12,800.00 USD | 0.00 USD | `+31.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 13,300,000.00 USD | 187.15 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 13,310,000.00 USD | 3,550.00 USD | 0.00 USD | `+31.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 13,310,000.00 USD | 6,100.00 USD | 0.00 USD | `+31.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 13,500,000.00 USD | 190,580.00 USD | 0.00 USD | `+32.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 13,500,000.00 USD | 534.87 USD | 0.00 USD | `+32.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 13,520,000.00 USD | 14,210.00 USD | 0.00 USD | `+32.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 13,520,000.00 USD | 5,000.00 USD | 0.00 USD | `+32.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 13,520,000.00 USD | 362.81 USD | 0.00 USD | `+32.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 13,580,000.00 USD | 60,770.00 USD | 0.00 USD | `+33.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 13,580,000.00 USD | 482.37 USD | 0.00 USD | `+33.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 13,630,000.00 USD | 48,740.00 USD | 0.00 USD | `+33.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 13,640,000.00 USD | 3,010.00 USD | 0.00 USD | `+33.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 13,640,000.00 USD | 191.09 USD | 0.00 USD | `+33.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.85` | 13,640,000.00 USD | 132.72 USD | 0.00 USD | `+34.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 13,650,000.00 USD | 12,600.00 USD | 0.00 USD | `+34.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 13,700,000.00 USD | 50,720.00 USD | 0.00 USD | `+34.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 13,720,000.00 USD | 15,330.00 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 13,720,000.00 USD | 401.29 USD | 0.00 USD | `+34.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 13,720,000.00 USD | 1,320.00 USD | 0.00 USD | `+34.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 13,720,000.00 USD | 152.99 USD | 0.00 USD | `+34.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 13,720,000.00 USD | 882.30 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 13,720,000.00 USD | 116.87 USD | 0.00 USD | `+35.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 13,740,000.00 USD | 22,410.00 USD | 0.00 USD | `+35.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 13,740,000.00 USD | 1,760.00 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 13,750,000.00 USD | 4,090.00 USD | 0.00 USD | `+35.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 13,750,000.00 USD | 192.06 USD | 0.00 USD | `+35.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 13,750,000.00 USD | 3,150.00 USD | 0.00 USD | `+36.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 13,750,000.00 USD | 2,620.00 USD | 0.00 USD | `+36.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 13,760,000.00 USD | 10,140.00 USD | 0.00 USD | `+36.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 13,770,000.00 USD | 6,000.00 USD | 0.00 USD | `+36.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 13,770,000.00 USD | 5,950.00 USD | 0.00 USD | `+36.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 13,780,000.00 USD | 6,160.00 USD | 0.00 USD | `+36.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 13,940,000.00 USD | 160,920.00 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 13,940,000.00 USD | 144.93 USD | 0.00 USD | `+37.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 13,960,000.00 USD | 19,520.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 13,960,000.00 USD | 397.95 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 13,970,000.00 USD | 9,310.00 USD | 0.00 USD | `+38.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 13,980,000.00 USD | 3,910.00 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 13,980,000.00 USD | 6,700.00 USD | 0.00 USD | `+38.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 13,980,000.00 USD | 509.96 USD | 0.00 USD | `+38.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 13,980,000.00 USD | 191.88 USD | 0.00 USD | `+38.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 13,980,000.00 USD | 237.36 USD | 0.00 USD | `+38.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 13,980,000.00 USD | 1,210.00 USD | 0.00 USD | `+38.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 13,980,000.00 USD | 192.46 USD | 0.00 USD | `+39.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 13,980,000.00 USD | 112.35 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 13,990,000.00 USD | 4,150.00 USD | 0.00 USD | `+39.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 14,040,000.00 USD | 54,080.00 USD | 0.00 USD | `+39.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 14,040,000.00 USD | 331.60 USD | 0.00 USD | `+39.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 14,240,000.00 USD | 195,540.00 USD | 0.00 USD | `+40.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 14,240,000.00 USD | 668.86 USD | 0.00 USD | `+40.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 14,300,000.00 USD | 57,060.00 USD | 0.00 USD | `+40.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 14,300,000.00 USD | 7,560.00 USD | 0.00 USD | `+41.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 14,310,000.00 USD | 1,890.00 USD | 0.00 USD | `+41.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 14,310,000.00 USD | 192.25 USD | 0.00 USD | `+41.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 14,310,000.00 USD | 465.29 USD | 0.00 USD | `+41.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 14,310,000.00 USD | 389.17 USD | 0.00 USD | `+42.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 14,310,000.00 USD | 826.57 USD | 0.00 USD | `+42.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 14,310,000.00 USD | 1,330.00 USD | 0.00 USD | `+42.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 14,310,000.00 USD | 2,910.00 USD | 0.00 USD | `+42.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 14,320,000.00 USD | 3,920.00 USD | 0.00 USD | `+42.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 14,340,000.00 USD | 26,260.00 USD | 0.00 USD | `+43.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 14,340,000.00 USD | 133.62 USD | 0.00 USD | `+43.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 14,360,000.00 USD | 18,910.00 USD | 0.00 USD | `+43.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 14,360,000.00 USD | 692.25 USD | 0.00 USD | `+44.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 14,360,000.00 USD | 406.24 USD | 0.00 USD | `+44.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 21,110,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+44.48%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 21,110,000.00 USD | 826.75 USD | 0.00 USD | `+44.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 23,310,000.00 USD | 2,200,000.00 USD | 0.00 USD | `+44.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 23,310,000.00 USD | 7,530.00 USD | 0.00 USD | `+45.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 23,410,000.00 USD | 94,590.00 USD | 0.00 USD | `+45.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 23,510,000.00 USD | 98,400.00 USD | 0.00 USD | `+46.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 23,510,000.00 USD | 990.88 USD | 0.00 USD | `+46.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 23,530,000.00 USD | 16,630.00 USD | 0.00 USD | `+46.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 23,530,000.00 USD | 6,190.00 USD | 0.00 USD | `+46.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 23,530,000.00 USD | 796.07 USD | 0.00 USD | `+47.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 23,530,000.00 USD | 826.73 USD | 0.00 USD | `+47.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 23,530,000.00 USD | 278.56 USD | 0.00 USD | `+48.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 23,880,000.00 USD | 346,420.00 USD | 0.00 USD | `+48.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 24,100,000.00 USD | 215,510.00 USD | 0.00 USD | `+48.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 24,100,000.00 USD | 528.96 USD | 0.00 USD | `+49.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 24,100,000.00 USD | 6,330.00 USD | 0.00 USD | `+49.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 24,100,000.00 USD | 415.44 USD | 0.00 USD | `+50.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 24,360,000.00 USD | 252,610.00 USD | 0.00 USD | `+50.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 24,360,000.00 USD | 7,260.00 USD | 0.00 USD | `+50.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 24,360,000.00 USD | 791.78 USD | 0.00 USD | `+50.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 24,380,000.00 USD | 17,900.00 USD | 0.00 USD | `+50.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 24,380,000.00 USD | 209.16 USD | 0.00 USD | `+51.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 24,380,000.00 USD | 698.64 USD | 0.00 USD | `+51.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 24,570,000.00 USD | 190,100.00 USD | 0.00 USD | `+51.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 24,580,000.00 USD | 3,300.00 USD | 0.00 USD | `+52.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 24,580,000.00 USD | 1,020.00 USD | 0.00 USD | `+52.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 24,580,000.00 USD | 1,500.00 USD | 0.00 USD | `+52.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 24,620,000.00 USD | 37,700.00 USD | 0.00 USD | `+53.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 24,620,000.00 USD | 844.89 USD | 0.00 USD | `+53.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 24,620,000.00 USD | 4,610.00 USD | 0.00 USD | `+53.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 24,620,000.00 USD | 3,100.00 USD | 0.00 USD | `+53.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 25,950,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+54.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 25,950,000.00 USD | 1,370.00 USD | 0.00 USD | `+54.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 25,950,000.00 USD | 773.95 USD | 0.00 USD | `+54.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 25,950,000.00 USD | 549.99 USD | 0.00 USD | `+55.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 26,460,000.00 USD | 510,120.00 USD | 0.00 USD | `+55.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 26,760,000.00 USD | 294,330.00 USD | 0.00 USD | `+56.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 26,760,000.00 USD | 1,200.00 USD | 0.00 USD | `+56.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 26,760,000.00 USD | 178.92 USD | 0.00 USD | `+56.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 26,760,000.00 USD | 1,360.00 USD | 0.00 USD | `+56.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 26,780,000.00 USD | 14,430.00 USD | 0.00 USD | `+57.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 26,780,000.00 USD | 2,000.00 USD | 0.00 USD | `+57.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 26,780,000.00 USD | 411.94 USD | 0.00 USD | `+57.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.95` | 26,790,000.00 USD | 10,230.00 USD | 0.00 USD | `+58.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.15` | 26,800,000.00 USD | 12,000.00 USD | 0.00 USD | `+58.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 26,810,000.00 USD | 10,620.00 USD | 0.00 USD | `+59.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 26,810,000.00 USD | 1,020.00 USD | 0.00 USD | `+59.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 26,820,000.00 USD | 12,000.00 USD | 0.00 USD | `+60.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 26,820,000.00 USD | 113.04 USD | 0.00 USD | `+61.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.95` | 26,820,000.00 USD | 156.50 USD | 0.00 USD | `+61.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 26,830,000.00 USD | 1,830.00 USD | 0.00 USD | `+61.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 26,840,000.00 USD | 16,970.00 USD | 0.00 USD | `+62.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 26,850,000.00 USD | 2,230.00 USD | 0.00 USD | `+62.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 26,850,000.00 USD | 6,480.00 USD | 0.00 USD | `+64.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 26,870,000.00 USD | 15,880.00 USD | 0.00 USD | `+65.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 26,870,000.00 USD | 692.30 USD | 0.00 USD | `+65.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 26,960,000.00 USD | 90,570.00 USD | 0.00 USD | `+66.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 26,960,000.00 USD | 281.84 USD | 0.00 USD | `+67.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 26,960,000.00 USD | 4,080.00 USD | 0.00 USD | `+69.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 27,050,000.00 USD | 82,530.00 USD | 0.00 USD | `+71.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 27,050,000.00 USD | 823.94 USD | 0.00 USD | `+72.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 27,050,000.00 USD | 211.39 USD | 0.00 USD | `+73.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 27,050,000.00 USD | 307.19 USD | 0.00 USD | `+73.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 27,050,000.00 USD | 593.03 USD | 0.00 USD | `+73.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 27,050,000.00 USD | 1,440.00 USD | 0.00 USD | `+74.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 27,050,000.00 USD | 5,550.00 USD | 0.00 USD | `+74.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 27,060,000.00 USD | 495.09 USD | 0.00 USD | `+76.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 27,060,000.00 USD | 912.63 USD | 0.00 USD | `+76.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 27,100,000.00 USD | 42,840.00 USD | 0.00 USD | `+76.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 27,100,000.00 USD | 686.20 USD | 0.00 USD | `+78.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 27,130,000.00 USD | 35,280.00 USD | 0.00 USD | `+79.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 27,140,000.00 USD | 703.60 USD | 0.00 USD | `+79.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 27,140,000.00 USD | 3,160.00 USD | 0.00 USD | `+80.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 27,190,000.00 USD | 52,520.00 USD | 0.00 USD | `+82.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 27,210,000.00 USD | 21,960.00 USD | 0.00 USD | `+82.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.55` | 27,210,000.00 USD | 1,450.00 USD | 0.00 USD | `+83.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 27,220,000.00 USD | 1,450.00 USD | 0.00 USD | `+84.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 27,220,000.00 USD | 1,840.00 USD | 0.00 USD | `+84.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.35` | 27,220,000.00 USD | 390.17 USD | 0.00 USD | `+84.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 27,220,000.00 USD | 2,990.00 USD | 0.00 USD | `+85.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 27,220,000.00 USD | 261.56 USD | 0.00 USD | `+86.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.85` | 27,220,000.00 USD | 109.71 USD | 0.00 USD | `+87.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 27,280,000.00 USD | 53,500.00 USD | 0.00 USD | `+87.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 27,280,000.00 USD | 2,480.00 USD | 0.00 USD | `+88.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 27,280,000.00 USD | 349.34 USD | 0.00 USD | `+89.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 27,300,000.00 USD | 19,620.00 USD | 0.00 USD | `+89.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 27,850,000.00 USD | 550,350.00 USD | 0.00 USD | `+90.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 27,880,000.00 USD | 29,420.00 USD | 0.00 USD | `+92.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 28,080,000.00 USD | 198,160.00 USD | 0.00 USD | `+94.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 28,220,000.00 USD | 141,190.00 USD | 0.00 USD | `+95.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 28,250,000.00 USD | 35,880.00 USD | 0.00 USD | `+97.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 28,250,000.00 USD | 744.27 USD | 0.00 USD | `+98.07%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `86.00` | 40,660,000.00 USD | 0.00 USD | 40,660,000.00 USD | 0.00 USD | 0.00 USD | 205,540.00 USD |
| `1D` | `86.20` | 40,460,000.00 USD | 0.00 USD | 40,460,000.00 USD | 12,120.00 USD | 85,490.00 USD | 0.00 USD |
| `7D` | `86.30` | 62,530,000.00 USD | 0.00 USD | 62,530,000.00 USD | 0.00 USD | 149,300.00 USD | 4,140.00 USD |
| `7D` | `86.50` | 62,380,000.00 USD | 0.00 USD | 62,380,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD |
| `1D` | `86.60` | 40,360,000.00 USD | 0.00 USD | 40,360,000.00 USD | 0.00 USD | 306,270.00 USD | 3,100.00 USD |
| `1D` | `86.80` | 40,050,000.00 USD | 0.00 USD | 40,050,000.00 USD | 0.00 USD | 66,610.00 USD | 4,330.00 USD |
| `7D` | `86.90` | 62,370,000.00 USD | 0.00 USD | 62,370,000.00 USD | 207,900.00 USD | 138,700.00 USD | 0.00 USD |
| `1D` | `87.00` | 39,980,000.00 USD | 0.00 USD | 39,980,000.00 USD | 150,240.00 USD | 112,850.00 USD | 0.00 USD |
| `1D` | `87.20` | 39,720,000.00 USD | 0.00 USD | 39,720,000.00 USD | 0.00 USD | 0.00 USD | 3,290.00 USD |
| `7D` | `87.70` | 62,030,000.00 USD | 0.00 USD | 62,030,000.00 USD | 0.00 USD | 0.00 USD | 3,820.00 USD |
| `1D` | `88.60` | 39,710,000.00 USD | 0.00 USD | 39,710,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD |
| `7D` | `88.70` | 62,020,000.00 USD | 0.00 USD | 62,020,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `88.80` | 39,710,000.00 USD | 0.00 USD | 39,710,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD |
| `7D` | `88.90` | 61,800,000.00 USD | 0.00 USD | 61,800,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD |
| `1D` | `89.00` | 38,810,000.00 USD | 0.00 USD | 38,810,000.00 USD | 8,600.00 USD | 2,360.00 USD | 217,430.00 USD |
| `7D` | `89.10` | 61,780,000.00 USD | 0.00 USD | 61,780,000.00 USD | 350,210.00 USD | 291,000.00 USD | 576,850.00 USD |
| `1D` | `89.20` | 38,580,000.00 USD | 0.00 USD | 38,580,000.00 USD | 166,240.00 USD | 99,310.00 USD | 1,410.00 USD |
| `7D` | `89.30` | 60,560,000.00 USD | 0.00 USD | 60,560,000.00 USD | 14,870.00 USD | 7,630.00 USD | 3,920.00 USD |
| `1D` | `89.40` | 38,320,000.00 USD | 0.00 USD | 38,320,000.00 USD | 12,630.00 USD | 93,010.00 USD | 265,240.00 USD |
| `7D` | `89.50` | 60,530,000.00 USD | 0.00 USD | 60,530,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD |
| `1D` | `89.60` | 37,950,000.00 USD | 0.00 USD | 37,950,000.00 USD | 557,950.00 USD | 163,120.00 USD | 317,090.00 USD |
| `7D` | `89.70` | 59,740,000.00 USD | 0.00 USD | 59,740,000.00 USD | 780,700.00 USD | 190,280.00 USD | 450,090.00 USD |
| `1D` | `89.80` | 36,910,000.00 USD | 0.00 USD | 36,910,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD |
| `7D` | `89.90` | 58,320,000.00 USD | 0.00 USD | 58,320,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD |
| `1D` | `90.00` | 35,800,000.00 USD | 0.00 USD | 35,800,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD |
| `7D` | `90.10` | 56,520,000.00 USD | 0.00 USD | 56,520,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD |
| `1D` | `90.20` | 34,450,000.00 USD | 0.00 USD | 34,450,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD |
| `7D` | `90.30` | 54,150,000.00 USD | 0.00 USD | 54,150,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `1D` | `90.40` | 33,120,000.00 USD | 0.00 USD | 33,120,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD |
| `7D` | `90.50` | 52,070,000.00 USD | 0.00 USD | 52,070,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD |
| `1D` | `90.60` | 31,770,000.00 USD | 0.00 USD | 31,770,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD |
| `7D` | `90.70` | 49,390,000.00 USD | 0.00 USD | 49,390,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `1D` | `90.80` | 30,630,000.00 USD | 0.00 USD | 30,630,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD |
| `7D` | `90.90` | 46,940,000.00 USD | 0.00 USD | 46,940,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `1D` | `91.00` | 30,420,000.00 USD | 0.00 USD | 30,420,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD |
| `7D` | `91.10` | 44,560,000.00 USD | 0.00 USD | 44,560,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `1D` | `91.20` | 30,230,000.00 USD | 0.00 USD | 30,230,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD |
| `7D` | `91.30` | 42,650,000.00 USD | 0.00 USD | 42,650,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `1D` | `91.40` | 30,200,000.00 USD | 0.00 USD | 30,200,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD |
| `7D` | `91.50` | 40,150,000.00 USD | 0.00 USD | 40,150,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD |
| `1D` | `91.60` | 30,030,000.00 USD | 0.00 USD | 30,030,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD |
| `7D` | `91.70` | 37,230,000.00 USD | 0.00 USD | 37,230,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `1D` | `91.80` | 29,900,000.00 USD | 0.00 USD | 29,900,000.00 USD | 250,490.00 USD | 103,030.00 USD | 525,270.00 USD |
| `7D` | `91.90` | 35,600,000.00 USD | 0.00 USD | 35,600,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `1D` | `92.00` | 29,030,000.00 USD | 0.00 USD | 29,030,000.00 USD | 40,010.00 USD | 288,020.00 USD | 88,220.00 USD |
| `7D` | `92.10` | 33,190,000.00 USD | 0.00 USD | 33,190,000.00 USD | 494,450.00 USD | 947,560.00 USD | 258,190.00 USD |
| `1D` | `92.20` | 28,610,000.00 USD | 0.00 USD | 28,610,000.00 USD | 106,580.00 USD | 171,510.00 USD | 60,710.00 USD |
| `7D` | `92.30` | 31,490,000.00 USD | 0.00 USD | 31,490,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,540,000.00 USD |
| `1D` | `92.40` | 28,270,000.00 USD | 0.00 USD | 28,270,000.00 USD | 149,180.00 USD | 845,850.00 USD | 991,720.00 USD |
| `7D` | `92.50` | 29,130,000.00 USD | 0.00 USD | 29,130,000.00 USD | 259,870.00 USD | 570,240.00 USD | 935,930.00 USD |
| `1D` | `92.60` | 26,280,000.00 USD | 0.00 USD | 26,280,000.00 USD | 380,700.00 USD | 222,110.00 USD | 56,520.00 USD |
| `7D` | `92.70` | 27,370,000.00 USD | 0.00 USD | 27,370,000.00 USD | 671,470.00 USD | 168,780.00 USD | 70,750.00 USD |
| `1D` | `92.80` | 25,620,000.00 USD | 0.00 USD | 25,620,000.00 USD | 26,180.00 USD | 402,380.00 USD | 97,110.00 USD |
| `7D` | `92.90` | 26,460,000.00 USD | 0.00 USD | 26,460,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD |
| `1D` | `93.00` | 25,100,000.00 USD | 0.00 USD | 25,100,000.00 USD | 0.00 USD | 0.00 USD | 8,220.00 USD |
| `7D` | `93.10` | 26,400,000.00 USD | 0.00 USD | 26,400,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `93.30` | 26,000,000.00 USD | 0.00 USD | 26,000,000.00 USD | 55,470.00 USD | 4,160.00 USD | 49,310.00 USD |
| `7D` | `93.50` | 25,890,000.00 USD | 0.00 USD | 25,890,000.00 USD | 101,820.00 USD | 215,050.00 USD | 11,790.00 USD |
| `1D` | `93.60` | 25,090,000.00 USD | 0.00 USD | 25,090,000.00 USD | 0.00 USD | 0.00 USD | 1,030,000.00 USD |
| `7D` | `93.70` | 25,570,000.00 USD | 0.00 USD | 25,570,000.00 USD | 270,240.00 USD | 262,300.00 USD | 115,880.00 USD |
| `1D` | `93.80` | 24,060,000.00 USD | 0.00 USD | 24,060,000.00 USD | 42,130.00 USD | 427,470.00 USD | 0.00 USD |
| `7D` | `93.90` | 24,920,000.00 USD | 0.00 USD | 24,920,000.00 USD | 168,420.00 USD | 101,680.00 USD | 111,350.00 USD |
| `1D` | `94.00` | 23,590,000.00 USD | 0.00 USD | 23,590,000.00 USD | 60,590.00 USD | 86,320.00 USD | 0.00 USD |
| `7D` | `94.10` | 24,540,000.00 USD | 0.00 USD | 24,540,000.00 USD | 233,120.00 USD | 999,200.00 USD | 342,970.00 USD |
| `1D` | `94.20` | 23,450,000.00 USD | 0.00 USD | 23,450,000.00 USD | 0.00 USD | 691,260.00 USD | 702,910.00 USD |
| `7D` | `94.30` | 22,960,000.00 USD | 0.00 USD | 22,960,000.00 USD | 10,610.00 USD | 0.00 USD | 711,670.00 USD |
| `1D` | `94.40` | 22,050,000.00 USD | 0.00 USD | 22,050,000.00 USD | 33,670.00 USD | 1,120,000.00 USD | 15,520.00 USD |
| `7D` | `94.50` | 22,240,000.00 USD | 0.00 USD | 22,240,000.00 USD | 245,400.00 USD | 698,220.00 USD | 140,220.00 USD |
| `1D` | `94.60` | 20,880,000.00 USD | 0.00 USD | 20,880,000.00 USD | 772,520.00 USD | 320,240.00 USD | 2,080,000.00 USD |
| `7D` | `94.70` | 21,150,000.00 USD | 0.00 USD | 21,150,000.00 USD | 1,600,000.00 USD | 238,650.00 USD | 0.00 USD |
| `1D` | `94.80` | 17,710,000.00 USD | 0.00 USD | 17,710,000.00 USD | 762,670.00 USD | 2,150,000.00 USD | 1,040,000.00 USD |
| `7D` | `94.90` | 19,320,000.00 USD | 0.00 USD | 19,320,000.00 USD | 1,100,000.00 USD | 2,230,000.00 USD | 0.00 USD |
| `1D` | `95.00` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 519,290.00 USD | 717,410.00 USD | 19,750.00 USD |
| `7D` | `95.10` | 15,980,000.00 USD | 0.00 USD | 15,980,000.00 USD | 141,070.00 USD | 226,060.00 USD | 1,330,000.00 USD |
| `1D` | `95.20` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 34,680.00 USD | 3,270,000.00 USD | 1,400,000.00 USD |
| `7D` | `95.30` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 499,140.00 USD | 321,080.00 USD | 0.00 USD |
| `1D` | `95.40` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 263,100.00 USD | 224,710.00 USD | 11,000.00 USD |
| `7D` | `95.50` | 13,460,000.00 USD | 0.00 USD | 13,460,000.00 USD | 1,200,000.00 USD | 1,580,000.00 USD | 0.00 USD |
| `1D` | `95.60` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 2,570,000.00 USD | 8,020.00 USD | 20,500.00 USD |
| `7D` | `95.70` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `95.80` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `95.90` | 6,620,000.00 USD | 0.00 USD | 6,620,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `96.00` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `96.10` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `96.20` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `96.30` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `96.40` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,580,000.00 USD |
| `1D` | `96.40` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,580,000.00 USD |
| `7D` | `96.50` | 58,320.00 USD | 58,320.00 USD | 0.00 USD | 0.00 USD | 58,320.00 USD | 0.00 USD |
| `7D` | `96.50` | 116,630.00 USD | 116,630.00 USD | 0.00 USD | 0.00 USD | 58,320.00 USD | 0.00 USD |
| `1D` | `96.60` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,050,000.00 USD |
| `7D` | `96.70` | 377,010.00 USD | 377,010.00 USD | 0.00 USD | 181,530.00 USD | 78,840.00 USD | 0.00 USD |
| `1D` | `96.80` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 53,180.00 USD | 859,230.00 USD | 1,800,000.00 USD |
| `7D` | `96.90` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 360,820.00 USD | 1,590,000.00 USD | 3,170,000.00 USD |
| `1D` | `97.00` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 1,310,000.00 USD | 522,440.00 USD | 474,940.00 USD |
| `7D` | `97.10` | 10,290,000.00 USD | 10,290,000.00 USD | 0.00 USD | 306,680.00 USD | 118,320.00 USD | 4,360,000.00 USD |
| `1D` | `97.20` | 18,840,000.00 USD | 18,840,000.00 USD | 0.00 USD | 379,310.00 USD | 3,490,000.00 USD | 1,730,000.00 USD |
| `7D` | `97.30` | 25,270,000.00 USD | 25,270,000.00 USD | 0.00 USD | 6,280,000.00 USD | 4,520,000.00 USD | 4,180,000.00 USD |
| `1D` | `97.40` | 23,680,000.00 USD | 23,680,000.00 USD | 0.00 USD | 845,630.00 USD | 1,490,000.00 USD | 2,500,000.00 USD |
| `7D` | `97.50` | 43,790,000.00 USD | 43,790,000.00 USD | 0.00 USD | 7,020,000.00 USD | 5,750,000.00 USD | 5,740,000.00 USD |
| `1D` | `97.60` | 37,290,000.00 USD | 37,290,000.00 USD | 0.00 USD | 5,300,000.00 USD | 1,610,000.00 USD | 6,700,000.00 USD |
| `7D` | `97.70` | 60,750,000.00 USD | 60,750,000.00 USD | 0.00 USD | 7,740,000.00 USD | 3,900,000.00 USD | 5,320,000.00 USD |
| `1D` | `97.80` | 47,110,000.00 USD | 47,110,000.00 USD | 0.00 USD | 5,310,000.00 USD | 548,540.00 USD | 3,960,000.00 USD |
| `7D` | `97.90` | 91,020,000.00 USD | 91,020,000.00 USD | 0.00 USD | 11,920,000.00 USD | 8,420,000.00 USD | 9,940,000.00 USD |
| `1D` | `98.00` | 58,370,000.00 USD | 58,370,000.00 USD | 0.00 USD | 6,080,000.00 USD | 777,550.00 USD | 4,400,000.00 USD |
| `7D` | `98.10` | 119,350,000.00 USD | 119,350,000.00 USD | 0.00 USD | 9,820,000.00 USD | 7,490,000.00 USD | 11,030,000.00 USD |
| `1D` | `98.20` | 68,070,000.00 USD | 68,070,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,830,000.00 USD | 2,720,000.00 USD |
| `7D` | `98.30` | 127,980,000.00 USD | 127,980,000.00 USD | 0.00 USD | 43,030.00 USD | 4,510,000.00 USD | 4,070,000.00 USD |
| `1D` | `98.40` | 77,700,000.00 USD | 77,700,000.00 USD | 0.00 USD | 2,560,000.00 USD | 310,490.00 USD | 6,760,000.00 USD |
| `7D` | `98.50` | 129,260,000.00 USD | 129,260,000.00 USD | 0.00 USD | 1,040,000.00 USD | 238,650.00 USD | 0.00 USD |
| `1D` | `98.60` | 78,560,000.00 USD | 78,560,000.00 USD | 0.00 USD | 52,360.00 USD | 804,770.00 USD | 0.00 USD |
| `1D` | `98.80` | 78,580,000.00 USD | 78,580,000.00 USD | 0.00 USD | 0.00 USD | 7,070.00 USD | 16,440.00 USD |
| `1D` | `99.00` | 78,890,000.00 USD | 78,890,000.00 USD | 0.00 USD | 0.00 USD | 305,090.00 USD | 1,180.00 USD |
| `1D` | `99.20` | 82,480,000.00 USD | 82,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,590,000.00 USD |
| `7D` | `99.30` | 129,280,000.00 USD | 129,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,100.00 USD |
| `1D` | `99.40` | 85,830,000.00 USD | 85,830,000.00 USD | 0.00 USD | 2,840,000.00 USD | 0.00 USD | 513,850.00 USD |
| `7D` | `99.50` | 131,520,000.00 USD | 131,520,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 6,720.00 USD |
| `1D` | `99.60` | 96,080,000.00 USD | 96,080,000.00 USD | 0.00 USD | 1,370,000.00 USD | 4,730,000.00 USD | 4,150,000.00 USD |
| `7D` | `99.70` | 133,530,000.00 USD | 133,530,000.00 USD | 0.00 USD | 0.00 USD | 2,000,000.00 USD | 12,550.00 USD |
| `1D` | `99.80` | 106,250,000.00 USD | 106,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 2,620,000.00 USD | 5,300,000.00 USD |
| `7D` | `99.90` | 140,690,000.00 USD | 140,690,000.00 USD | 0.00 USD | 2,860,000.00 USD | 1,110,000.00 USD | 3,190,000.00 USD |
| `1D` | `100.00` | 111,730,000.00 USD | 111,730,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,770,000.00 USD | 1,630,000.00 USD |
| `7D` | `100.10` | 144,080,000.00 USD | 144,080,000.00 USD | 0.00 USD | 48,160.00 USD | 477,660.00 USD | 2,870,000.00 USD |
| `1D` | `100.20` | 112,580,000.00 USD | 112,580,000.00 USD | 0.00 USD | 16,830.00 USD | 832,940.00 USD | 243.12 USD |
| `7D` | `100.30` | 146,930,000.00 USD | 146,930,000.00 USD | 0.00 USD | 883,050.00 USD | 855,480.00 USD | 1,110,000.00 USD |
| `1D` | `100.40` | 116,200,000.00 USD | 116,200,000.00 USD | 0.00 USD | 349,430.00 USD | 629,010.00 USD | 2,640,000.00 USD |
| `7D` | `100.50` | 153,870,000.00 USD | 153,870,000.00 USD | 0.00 USD | 2,500,000.00 USD | 128,740.00 USD | 4,310,000.00 USD |
| `1D` | `100.60` | 125,530,000.00 USD | 125,530,000.00 USD | 0.00 USD | 1,990,000.00 USD | 1,180,000.00 USD | 6,150,000.00 USD |
| `7D` | `100.70` | 155,230,000.00 USD | 155,230,000.00 USD | 0.00 USD | 133,340.00 USD | 1,230,000.00 USD | 0.00 USD |
| `1D` | `100.80` | 129,610,000.00 USD | 129,610,000.00 USD | 0.00 USD | 1,500,000.00 USD | 1,490,000.00 USD | 1,090,000.00 USD |
| `7D` | `100.90` | 167,060,000.00 USD | 167,060,000.00 USD | 0.00 USD | 3,450,000.00 USD | 3,210,000.00 USD | 5,170,000.00 USD |
| `1D` | `101.00` | 140,470,000.00 USD | 140,470,000.00 USD | 0.00 USD | 7,780,000.00 USD | 2,250,000.00 USD | 834,730.00 USD |
| `7D` | `101.10` | 176,260,000.00 USD | 176,260,000.00 USD | 0.00 USD | 2,930,000.00 USD | 3,930,000.00 USD | 2,340,000.00 USD |
| `1D` | `101.20` | 156,290,000.00 USD | 156,290,000.00 USD | 0.00 USD | 5,170,000.00 USD | 6,570,000.00 USD | 4,070,000.00 USD |
| `7D` | `101.30` | 194,270,000.00 USD | 194,270,000.00 USD | 0.00 USD | 7,310,000.00 USD | 3,160,000.00 USD | 7,540,000.00 USD |
| `1D` | `101.40` | 164,900,000.00 USD | 164,900,000.00 USD | 0.00 USD | 3,390,000.00 USD | 1,950,000.00 USD | 3,270,000.00 USD |
| `7D` | `101.50` | 208,800,000.00 USD | 208,800,000.00 USD | 0.00 USD | 2,950,000.00 USD | 0.00 USD | 11,580,000.00 USD |
| `1D` | `101.60` | 184,440,000.00 USD | 184,440,000.00 USD | 0.00 USD | 5,190,000.00 USD | 2,550,000.00 USD | 11,800,000.00 USD |
| `7D` | `101.70` | 218,140,000.00 USD | 218,140,000.00 USD | 0.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD |
| `1D` | `101.80` | 191,520,000.00 USD | 191,520,000.00 USD | 0.00 USD | 483,810.00 USD | 381,190.00 USD | 6,210,000.00 USD |
| `7D` | `101.90` | 226,150,000.00 USD | 226,150,000.00 USD | 0.00 USD | 3,710,000.00 USD | 503,680.00 USD | 3,790,000.00 USD |
| `1D` | `102.00` | 195,910,000.00 USD | 195,910,000.00 USD | 0.00 USD | 2,230,000.00 USD | 873,740.00 USD | 1,290,000.00 USD |
| `7D` | `102.10` | 230,790,000.00 USD | 230,790,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 3,180,000.00 USD |
| `1D` | `102.20` | 202,750,000.00 USD | 202,750,000.00 USD | 0.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD |
| `7D` | `102.30` | 236,840,000.00 USD | 236,840,000.00 USD | 0.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,540,000.00 USD |
| `1D` | `102.40` | 207,320,000.00 USD | 207,320,000.00 USD | 0.00 USD | 1,430,000.00 USD | 579,100.00 USD | 2,570,000.00 USD |
| `7D` | `102.50` | 240,490,000.00 USD | 240,490,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `102.60` | 209,970,000.00 USD | 209,970,000.00 USD | 0.00 USD | 978,360.00 USD | 625,050.00 USD | 1,040,000.00 USD |
| `7D` | `102.70` | 241,270,000.00 USD | 241,270,000.00 USD | 0.00 USD | 766,460.00 USD | 0.00 USD | 7,680.00 USD |
| `1D` | `102.80` | 214,430,000.00 USD | 214,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,920,000.00 USD | 1,100,000.00 USD |
| `7D` | `102.90` | 262,550,000.00 USD | 262,550,000.00 USD | 0.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD |
| `1D` | `103.00` | 219,690,000.00 USD | 219,690,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,640,000.00 USD | 498,100.00 USD |
| `7D` | `103.10` | 268,760,000.00 USD | 268,760,000.00 USD | 0.00 USD | 4,750,000.00 USD | 114,550.00 USD | 1,340,000.00 USD |
| `1D` | `103.20` | 223,420,000.00 USD | 223,420,000.00 USD | 0.00 USD | 585,300.00 USD | 1,320,000.00 USD | 1,830,000.00 USD |
| `7D` | `103.30` | 286,330,000.00 USD | 286,330,000.00 USD | 0.00 USD | 17,020,000.00 USD | 133,780.00 USD | 417,110.00 USD |
| `1D` | `103.40` | 230,450,000.00 USD | 230,450,000.00 USD | 0.00 USD | 3,460,000.00 USD | 1,900,000.00 USD | 1,660,000.00 USD |
| `7D` | `103.50` | 308,740,000.00 USD | 308,740,000.00 USD | 0.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD |
| `1D` | `103.60` | 243,190,000.00 USD | 243,190,000.00 USD | 0.00 USD | 4,260,000.00 USD | 1,580,000.00 USD | 6,910,000.00 USD |
| `7D` | `103.70` | 320,960,000.00 USD | 320,960,000.00 USD | 0.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD |
| `1D` | `103.80` | 252,600,000.00 USD | 252,600,000.00 USD | 0.00 USD | 3,210,000.00 USD | 2,770,000.00 USD | 3,430,000.00 USD |
| `7D` | `103.90` | 338,990,000.00 USD | 338,990,000.00 USD | 0.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD |
| `1D` | `104.00` | 262,160,000.00 USD | 262,160,000.00 USD | 0.00 USD | 3,550,000.00 USD | 2,790,000.00 USD | 3,220,000.00 USD |
| `7D` | `104.10` | 367,720,000.00 USD | 367,720,000.00 USD | 0.00 USD | 11,570,000.00 USD | 8,150,000.00 USD | 9,010,000.00 USD |
| `1D` | `104.20` | 267,970,000.00 USD | 267,970,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,900,000.00 USD | 1,840,000.00 USD |
| `7D` | `104.30` | 389,100,000.00 USD | 389,100,000.00 USD | 0.00 USD | 7,320,000.00 USD | 6,370,000.00 USD | 7,690,000.00 USD |
| `1D` | `104.40` | 274,960,000.00 USD | 274,960,000.00 USD | 0.00 USD | 3,060,000.00 USD | 1,930,000.00 USD | 2,000,000.00 USD |
| `7D` | `104.50` | 401,100,000.00 USD | 401,100,000.00 USD | 0.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD |
| `1D` | `104.60` | 280,360,000.00 USD | 280,360,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,070,000.00 USD | 2,670,000.00 USD |
| `7D` | `104.70` | 421,100,000.00 USD | 421,100,000.00 USD | 0.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD |
| `1D` | `104.80` | 285,370,000.00 USD | 285,370,000.00 USD | 0.00 USD | 1,460,000.00 USD | 972,490.00 USD | 2,580,000.00 USD |
| `7D` | `104.90` | 441,710,000.00 USD | 441,710,000.00 USD | 0.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD |
| `1D` | `105.00` | 287,300,000.00 USD | 287,300,000.00 USD | 0.00 USD | 708,730.00 USD | 483,120.00 USD | 746,730.00 USD |
| `7D` | `105.10` | 455,390,000.00 USD | 455,390,000.00 USD | 0.00 USD | 5,580,000.00 USD | 5,260,000.00 USD | 2,830,000.00 USD |
| `1D` | `105.20` | 288,560,000.00 USD | 288,560,000.00 USD | 0.00 USD | 237,100.00 USD | 4,110.00 USD | 1,020,000.00 USD |
| `7D` | `105.30` | 461,090,000.00 USD | 461,090,000.00 USD | 0.00 USD | 2,740,000.00 USD | 2,540,000.00 USD | 428,740.00 USD |
| `1D` | `105.40` | 288,730,000.00 USD | 288,730,000.00 USD | 0.00 USD | 84,970.00 USD | 88,270.00 USD | 769.33 USD |
| `7D` | `105.50` | 480,610,000.00 USD | 480,610,000.00 USD | 0.00 USD | 5,600,000.00 USD | 6,170,000.00 USD | 7,740,000.00 USD |
| `1D` | `105.60` | 289,310,000.00 USD | 289,310,000.00 USD | 0.00 USD | 178,510.00 USD | 263,160.00 USD | 135,560.00 USD |
| `7D` | `105.70` | 494,770,000.00 USD | 494,770,000.00 USD | 0.00 USD | 4,560,000.00 USD | 4,340,000.00 USD | 5,270,000.00 USD |
| `1D` | `105.80` | 290,060,000.00 USD | 290,060,000.00 USD | 0.00 USD | 132,310.00 USD | 591,910.00 USD | 22,350.00 USD |
| `7D` | `105.90` | 504,720,000.00 USD | 504,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 1,880,000.00 USD | 4,350,000.00 USD |
| `1D` | `106.00` | 291,180,000.00 USD | 291,180,000.00 USD | 0.00 USD | 377,210.00 USD | 523,130.00 USD | 226,180.00 USD |
| `7D` | `106.10` | 517,870,000.00 USD | 517,870,000.00 USD | 0.00 USD | 6,580,000.00 USD | 3,600,000.00 USD | 2,960,000.00 USD |
| `1D` | `106.20` | 292,510,000.00 USD | 292,510,000.00 USD | 0.00 USD | 616,110.00 USD | 345,000.00 USD | 367,190.00 USD |
| `7D` | `106.30` | 528,540,000.00 USD | 528,540,000.00 USD | 0.00 USD | 4,780,000.00 USD | 3,220,000.00 USD | 2,670,000.00 USD |
| `1D` | `106.40` | 293,370,000.00 USD | 293,370,000.00 USD | 0.00 USD | 288,180.00 USD | 356,490.00 USD | 207,870.00 USD |
| `7D` | `106.50` | 534,130,000.00 USD | 534,130,000.00 USD | 0.00 USD | 1,700,000.00 USD | 2,010,000.00 USD | 1,890,000.00 USD |
| `1D` | `106.60` | 295,480,000.00 USD | 295,480,000.00 USD | 0.00 USD | 803,010.00 USD | 365,650.00 USD | 949,940.00 USD |
| `7D` | `106.70` | 543,260,000.00 USD | 543,260,000.00 USD | 0.00 USD | 2,280,000.00 USD | 2,670,000.00 USD | 4,180,000.00 USD |
| `1D` | `106.80` | 297,090,000.00 USD | 297,090,000.00 USD | 0.00 USD | 565,520.00 USD | 117,240.00 USD | 924,150.00 USD |
| `7D` | `106.90` | 549,040,000.00 USD | 549,040,000.00 USD | 0.00 USD | 1,190,000.00 USD | 1,120,000.00 USD | 3,470,000.00 USD |
| `1D` | `107.00` | 297,760,000.00 USD | 297,760,000.00 USD | 0.00 USD | 199,140.00 USD | 184,400.00 USD | 288,270.00 USD |
| `7D` | `107.10` | 552,440,000.00 USD | 552,440,000.00 USD | 0.00 USD | 1,630,000.00 USD | 508,540.00 USD | 1,270,000.00 USD |
| `1D` | `107.20` | 298,010,000.00 USD | 298,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 242,780.00 USD |
| `7D` | `107.30` | 552,600,000.00 USD | 552,600,000.00 USD | 0.00 USD | 0.00 USD | 156,300.00 USD | 0.00 USD |
| `7D` | `107.50` | 553,580,000.00 USD | 553,580,000.00 USD | 0.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD |
| `7D` | `107.70` | 554,550,000.00 USD | 554,550,000.00 USD | 0.00 USD | 523,660.00 USD | 10,400.00 USD | 432,310.00 USD |
| `7D` | `107.90` | 554,720,000.00 USD | 554,720,000.00 USD | 0.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.10` | 555,840,000.00 USD | 555,840,000.00 USD | 0.00 USD | 496,690.00 USD | 612,160.00 USD | 7,940.00 USD |
| `1D` | `108.20` | 298,010,000.00 USD | 298,010,000.00 USD | 0.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD |
| `7D` | `108.30` | 558,130,000.00 USD | 558,130,000.00 USD | 0.00 USD | 980,650.00 USD | 697,770.00 USD | 612,150.00 USD |
| `1D` | `108.40` | 298,040,000.00 USD | 298,040,000.00 USD | 0.00 USD | 29,460.00 USD | 1,950.00 USD | 1,520.00 USD |
| `7D` | `108.50` | 559,580,000.00 USD | 559,580,000.00 USD | 0.00 USD | 883,300.00 USD | 336,620.00 USD | 230,290.00 USD |
| `1D` | `108.60` | 298,910,000.00 USD | 298,910,000.00 USD | 0.00 USD | 275,520.00 USD | 173,760.00 USD | 413,910.00 USD |
| `7D` | `108.70` | 561,820,000.00 USD | 561,820,000.00 USD | 0.00 USD | 578,660.00 USD | 655,690.00 USD | 1,010,000.00 USD |
| `1D` | `108.80` | 299,130,000.00 USD | 299,130,000.00 USD | 0.00 USD | 8,600.00 USD | 2,360.00 USD | 217,430.00 USD |
| `7D` | `108.90` | 563,870,000.00 USD | 563,870,000.00 USD | 0.00 USD | 646,020.00 USD | 644,300.00 USD | 754,740.00 USD |
| `1D` | `109.00` | 299,400,000.00 USD | 299,400,000.00 USD | 0.00 USD | 166,240.00 USD | 99,310.00 USD | 1,410.00 USD |
| `7D` | `109.10` | 564,950,000.00 USD | 564,950,000.00 USD | 0.00 USD | 434,330.00 USD | 185,250.00 USD | 464,140.00 USD |
| `1D` | `109.20` | 299,770,000.00 USD | 299,770,000.00 USD | 0.00 USD | 12,630.00 USD | 93,010.00 USD | 265,240.00 USD |
| `7D` | `109.30` | 566,120,000.00 USD | 566,120,000.00 USD | 0.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD |
| `1D` | `109.40` | 299,910,000.00 USD | 299,910,000.00 USD | 0.00 USD | 123,410.00 USD | 7,590.00 USD | 4,060.00 USD |
| `7D` | `109.50` | 566,360,000.00 USD | 566,360,000.00 USD | 0.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD |
| `1D` | `109.60` | 300,810,000.00 USD | 300,810,000.00 USD | 0.00 USD | 434,540.00 USD | 155,520.00 USD | 313,030.00 USD |
| `7D` | `109.70` | 567,540,000.00 USD | 567,540,000.00 USD | 0.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD |
| `1D` | `109.80` | 301,920,000.00 USD | 301,920,000.00 USD | 0.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD |
| `7D` | `109.90` | 569,340,000.00 USD | 569,340,000.00 USD | 0.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD |
| `1D` | `110.00` | 303,270,000.00 USD | 303,270,000.00 USD | 0.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD |
| `7D` | `110.10` | 571,710,000.00 USD | 571,710,000.00 USD | 0.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD |
| `1D` | `110.20` | 304,600,000.00 USD | 304,600,000.00 USD | 0.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD |
| `7D` | `110.30` | 573,790,000.00 USD | 573,790,000.00 USD | 0.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `1D` | `110.40` | 305,950,000.00 USD | 305,950,000.00 USD | 0.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD |
| `7D` | `110.50` | 574,270,000.00 USD | 574,270,000.00 USD | 0.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD |
| `1D` | `110.60` | 306,410,000.00 USD | 306,410,000.00 USD | 0.00 USD | 110,850.00 USD | 104,840.00 USD | 240,140.00 USD |
| `7D` | `110.70` | 576,470,000.00 USD | 576,470,000.00 USD | 0.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD |
| `1D` | `110.80` | 307,090,000.00 USD | 307,090,000.00 USD | 0.00 USD | 159,320.00 USD | 287,810.00 USD | 237,370.00 USD |
| `7D` | `110.90` | 578,920,000.00 USD | 578,920,000.00 USD | 0.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `1D` | `111.00` | 307,300,000.00 USD | 307,300,000.00 USD | 0.00 USD | 106,320.00 USD | 101,660.00 USD | 319.18 USD |
| `7D` | `111.10` | 581,300,000.00 USD | 581,300,000.00 USD | 0.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `7D` | `111.30` | 583,210,000.00 USD | 583,210,000.00 USD | 0.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `7D` | `111.50` | 585,710,000.00 USD | 585,710,000.00 USD | 0.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `7D` | `111.70` | 586,860,000.00 USD | 586,860,000.00 USD | 0.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD |
| `7D` | `111.90` | 588,630,000.00 USD | 588,630,000.00 USD | 0.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD |
| `7D` | `112.10` | 590,260,000.00 USD | 590,260,000.00 USD | 0.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `7D` | `112.30` | 592,670,000.00 USD | 592,670,000.00 USD | 0.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `7D` | `112.50` | 593,980,000.00 USD | 593,980,000.00 USD | 0.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD |
| `7D` | `112.70` | 594,500,000.00 USD | 594,500,000.00 USD | 0.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD |
| `7D` | `112.90` | 595,990,000.00 USD | 595,990,000.00 USD | 0.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD |
| `7D` | `113.10` | 597,390,000.00 USD | 597,390,000.00 USD | 0.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD |
| `7D` | `113.30` | 597,660,000.00 USD | 597,660,000.00 USD | 0.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD |
| `7D` | `113.50` | 597,720,000.00 USD | 597,720,000.00 USD | 0.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD |
| `7D` | `113.70` | 598,110,000.00 USD | 598,110,000.00 USD | 0.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `113.90` | 598,170,000.00 USD | 598,170,000.00 USD | 0.00 USD | 52,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `114.10` | 598,220,000.00 USD | 598,220,000.00 USD | 0.00 USD | 3,370.00 USD | 4,160.00 USD | 49,310.00 USD |
| `7D` | `114.30` | 598,540,000.00 USD | 598,540,000.00 USD | 0.00 USD | 101,820.00 USD | 211,850.00 USD | 1,290.00 USD |
| `7D` | `114.40` | 598,870,000.00 USD | 598,870,000.00 USD | 0.00 USD | 132,060.00 USD | 82,030.00 USD | 113,160.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.99B` | Total OI Tokens: `62,305,972.5 SOL`
  * 1h OI Change: `-2.74%` | 4h OI Change: `-4.97%` | 24h OI Change: `-5.97%`
  * Exchange Breakdown: Binance=`1.05B` | Bybit=`603.07M` | OKX=`347.78M` | Hyperliquid=`547.06M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `92.56K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0054%` | **USDT OKX** | `0.0092%` |
| **USDT Bybit** | `0.0001%` | **USDT KuCoin** | `0.0097%` |
| **USDT MEXC** | `0.0055%` | **USDT BingX** | `0.0092%` |
| **USDT Gate** | `-0.0001%` | **USDT Bitget** | `0.0070%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `52.93%` | `47.07%` | `1.12` | 170,940,000.00 USD |
| `15M` | `Binance` | `49.01%` | `50.99%` | `0.96` | 74,310,000.00 USD |
| `15M` | `OKX` | `52.2%` | `47.8%` | `1.09` | 22,390,000.00 USD |
| `15M` | `Bybit` | `52.8%` | `47.2%` | `1.12` | 24,380,000.00 USD |
| `15M` | `KuCoin` | `48.54%` | `51.46%` | `0.94` | 2,990,000.00 USD |
| `15M` | `Gate` | `49.18%` | `50.82%` | `0.97` | 3,290,000.00 USD |
| `15M` | `Bitget` | `53.59%` | `46.41%` | `1.15` | 7,890,000.00 USD |
| `15M` | `BingX` | `49.73%` | `50.27%` | `0.99` | 1,370,000.00 USD |
| `15M` | `MEXC` | `48.45%` | `51.55%` | `0.94` | 9,370,000.00 USD |
| `15M` | `Bitunix` | `47.95%` | `52.05%` | `0.92` | 6,090,000.00 USD |
| `15M` | `Hyperliquid` | `76.33%` | `23.67%` | `3.22` | 14,320,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `84.79%` | `15.21%` | `5.57` | 545,510.00 USD |
| `15M` | `Crypto.com` | `38.21%` | `61.79%` | `0.62` | 155,150.00 USD |
| `15M` | `WhiteBIT` | `80.11%` | `19.89%` | `4.03` | 768,760.00 USD |
| `15M` | `HTX` | `49.72%` | `50.28%` | `0.99` | 134,080.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `70.88%` | `29.12%` | `2.43` | 1,440,000.00 USD |
| `15M` | `Aster` | `58.43%` | `41.57%` | `1.41` | 1,250,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `69.04%` | `30.96%` | `2.23` | 265,250.00 USD |
| `15M` | `Whale Positions` | `49.01%` | `50.99%` | `0.96` | 74,310,000.00 USD |
| `15M` | `Global Accounts` | `52.93%` | `47.07%` | `1.12` | 170,940,000.00 USD |
| `1H` | `SOL` | `44.38%` | `55.62%` | `0.80` | 791,040,000.00 USD |
| `1H` | `Binance` | `44.17%` | `55.83%` | `0.79` | 307,580,000.00 USD |
| `1H` | `OKX` | `46.12%` | `53.88%` | `0.86` | 111,190,000.00 USD |
| `1H` | `Bybit` | `41.36%` | `58.64%` | `0.71` | 121,800,000.00 USD |
| `1H` | `KuCoin` | `46.72%` | `53.28%` | `0.88` | 13,610,000.00 USD |
| `1H` | `Gate` | `46.99%` | `53.01%` | `0.89` | 10,150,000.00 USD |
| `1H` | `Bitget` | `47.25%` | `52.75%` | `0.90` | 35,160,000.00 USD |
| `1H` | `BingX` | `38.96%` | `61.04%` | `0.64` | 10,530,000.00 USD |
| `1H` | `MEXC` | `42.35%` | `57.65%` | `0.73` | 70,180,000.00 USD |
| `1H` | `Bitunix` | `46.94%` | `53.06%` | `0.88` | 29,650,000.00 USD |
| `1H` | `Hyperliquid` | `42.78%` | `57.22%` | `0.75` | 55,520,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `42.86%` | `57.14%` | `0.75` | 3,710,000.00 USD |
| `1H` | `Crypto.com` | `48.65%` | `51.35%` | `0.95` | 1,440,000.00 USD |
| `1H` | `WhiteBIT` | `83.65%` | `16.35%` | `5.12` | 6,480,000.00 USD |
| `1H` | `HTX` | `47.59%` | `52.41%` | `0.91` | 466,150.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `49.22%` | `50.78%` | `0.97` | 4,180,000.00 USD |
| `1H` | `Aster` | `45.64%` | `54.36%` | `0.84` | 8,310,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.13%` | `50.87%` | `0.97` | 1,090,000.00 USD |
| `1H` | `Whale Positions` | `44.17%` | `55.83%` | `0.79` | 307,580,000.00 USD |
| `1H` | `Global Accounts` | `44.38%` | `55.62%` | `0.80` | 791,040,000.00 USD |
| `4H` | `SOL` | `43.56%` | `56.44%` | `0.77` | 1,250,000,000.00 USD |
| `4H` | `Binance` | `43.62%` | `56.38%` | `0.77` | 464,600,000.00 USD |
| `4H` | `OKX` | `43.83%` | `56.17%` | `0.78` | 163,610,000.00 USD |
| `4H` | `Bybit` | `40.62%` | `59.38%` | `0.68` | 186,410,000.00 USD |
| `4H` | `KuCoin` | `45.91%` | `54.09%` | `0.85` | 18,390,000.00 USD |
| `4H` | `Gate` | `46.51%` | `53.49%` | `0.87` | 30,490,000.00 USD |
| `4H` | `Bitget` | `42.92%` | `57.08%` | `0.75` | 68,080,000.00 USD |
| `4H` | `BingX` | `31.4%` | `68.6%` | `0.46` | 24,230,000.00 USD |
| `4H` | `MEXC` | `42.67%` | `57.33%` | `0.74` | 117,950,000.00 USD |
| `4H` | `Bitunix` | `46.2%` | `53.8%` | `0.86` | 56,820,000.00 USD |
| `4H` | `Hyperliquid` | `41.22%` | `58.78%` | `0.70` | 65,180,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.59%` | `51.41%` | `0.95` | 5,680,000.00 USD |
| `4H` | `Crypto.com` | `49.86%` | `50.14%` | `0.99` | 2,110,000.00 USD |
| `4H` | `WhiteBIT` | `69.72%` | `30.28%` | `2.30` | 27,300,000.00 USD |
| `4H` | `HTX` | `54.73%` | `45.27%` | `1.21` | 960,600.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `41.91%` | `58.09%` | `0.72` | 6,610,000.00 USD |
| `4H` | `Aster` | `45.36%` | `54.64%` | `0.83` | 13,710,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.29%` | `52.71%` | `0.90` | 1,650,000.00 USD |
| `4H` | `Whale Positions` | `43.62%` | `56.38%` | `0.77` | 464,600,000.00 USD |
| `4H` | `Global Accounts` | `43.56%` | `56.44%` | `0.77` | 1,250,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `100.66` | `100.58` | `100.66` | `100.78` | `100.34` | 9,618,082.62 USD | 5,517,082.05 USD | 4,101,000.56 USD | 1,416,081.49 USD | `+14.72%` | `9B / 2S` |
| `0:00 UTC` | `100.38` | `100.40` | `100.38` | `100.62` | `100.25` | 9,521,682.83 USD | 4,738,635.78 USD | 4,783,047.06 USD | -44,411.28 USD | `-0.47%` | `0B / 7S` |
| `5:00 UTC` | `100.31` | `100.27` | `100.31` | `100.43` | `100.16` | 10,974,925.19 USD | 4,852,550.33 USD | 6,122,374.86 USD | -1,269,824.53 USD | `-11.57%` | `4B / 3S` |
| `0:00 UTC` | `100.10` | `100.18` | `100.10` | `100.38` | `100.09` | 16,033,450.26 USD | 8,994,633.57 USD | 7,038,816.68 USD | 1,955,816.89 USD | `+12.20%` | `5B / 2S` |
| `5:00 UTC` | `100.00` | `99.98` | `100.00` | `100.22` | `99.77` | 31,495,982.01 USD | 14,749,838.13 USD | 16,746,143.88 USD | -1,996,305.75 USD | `-6.34%` | `7B / 6S` |
| `0:00 UTC` | `99.50` | `99.07` | `99.50` | `99.91` | `98.34` | 139,589,983.05 USD | 62,074,582.88 USD | 77,515,400.18 USD | -15,440,817.30 USD | `-11.06%` | `5B / 15S` |
| `5:00 UTC` | `99.28` | `99.16` | `99.28` | `99.43` | `98.87` | 30,714,746.87 USD | 17,611,035.06 USD | 13,103,711.81 USD | 4,507,323.25 USD | `+14.67%` | `6B / 1S` |
| `0:00 UTC` | `96.92` | `97.64` | `96.92` | `99.58` | `96.22` | 192,431,903.91 USD | 82,764,009.24 USD | 109,667,894.68 USD | -26,903,885.44 USD | `-13.98%` | `3B / 37S` |
| `5:00 UTC` | `96.70` | `96.08` | `96.70` | `97.16` | `94.82` | 215,726,671.39 USD | 100,520,655.67 USD | 115,206,015.72 USD | -14,685,360.05 USD | `-6.81%` | `2B / 14S` |
| `0:00 UTC` | `95.81` | `96.16` | `95.81` | `96.88` | `95.34` | 112,306,242.49 USD | 58,495,033.55 USD | 53,811,208.94 USD | 4,683,824.60 USD | `+4.17%` | `11B / 6S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 18:37` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `101.13` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 500K SOL` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `101.76` | 0.00 USD | 0.00 USD |
| `10-28 15:32` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.87` | 99,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `102.88` | 0.00 USD | 0.00 USD |
| `10-28 13:30` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.22` | 103,000.00 USD | 0.00 USD |
| `10-28 10:59` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `101.76` | 110,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -2,120,000.00 USD | -5,770,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -2,340,000.00 USD | -19,780,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -27,850,000.00 USD | -95,900,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -30,110,000.00 USD | -116,180,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -31,500,000.00 USD | -146,440,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -37,300,000.00 USD | -179,320,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -23,910,000.00 USD | -188,590,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -20,360,000.00 USD | -193,700,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -19,450,000.00 USD | -207,870,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,050,000.00 USD | -247,810,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 55,280,000.00 USD | -442,370,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 26,550,000.00 USD | -2,010,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-2.12M` | 15m=`-2.34M` | 1h=`-30.11M` | 24h=`-9.05M`
* Futures Capital Netflows: 5m=`-5.77M` | 15m=`-19.78M` | 1h=`-116.18M` | 24h=`-247.81M`
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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `95.04` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `92.60` (Risk Distance: `2.44` pts)
  * +2.5R Take Profit: `101.14`
  * Mathematical Lot Sizing: **`4.09 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `95.33` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `97.77` (Risk Distance: `2.44` pts)
  * +2.5R Take Profit: `89.23`
  * Mathematical Lot Sizing: **`4.09 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`96.30`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
