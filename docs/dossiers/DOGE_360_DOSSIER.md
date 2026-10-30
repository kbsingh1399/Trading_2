# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 14:29:40 IST` (`2026-10-30 08:59:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0743` | **Live Ask Quote**: `0.0764` | **Mid Price**: `0.0754`
- **Spread Points**: `21.00` | **Spread BPS**: `278.70 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `0.0737` | VWAP Z-Score: `+0.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000447` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.20` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0769` | Lower -3.00σ Band: `0.0705`
  * Upper +2.51σ Band: `0.0764` | Lower -2.51σ Band: `0.0710`
  * Upper +2.01σ Band: `0.0759` | Lower -2.01σ Band: `0.0715`
  * Upper +2.00σ Band: `0.0758` | Lower -2.00σ Band: `0.0716`
  * Upper +1.28σ Band: `0.0751` | Lower -1.28σ Band: `0.0723`
  * Upper +1.00σ Band: `0.0748` | Lower -1.00σ Band: `0.0726`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0747` | EMA-20=`0.0747` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0751` (Slope: `+0.0000`) | EMA-100=`0.0758`
  * Institutional Anchors: EMA-144=`0.0762` | EMA-200=`0.0765` (Slope: `-0.2686`) | EMA-233=`0.0766`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0756` (Distance: `-0.28%`)
  * Point of Control (POC) = `0.0749` (Distance: `+0.62%`)
  * Value Area Low (VAL) = `0.0736` (Distance: `+2.37%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0783` | Weekly POC=`0.0762` | Weekly VAL=`0.0747`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0756` | Low=`0.0742`
  * New York Session (13:00-21:00 UTC): High=`0.0758` | Low=`0.0749`
  * Initial Balance (First Hour): IB High=`0.0754` | IB Low=`0.0749`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0750` - `0.0757`
  * Optimal Trade Entry (OTE 0.705): `0.0755`
  * Structural Invalidation Anchor (0.786): `0.0760`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0758` | `0.0759` | `0.0757` | `0.0757` | `6,320,250` | 478,911.58 USD | -28,813.30 USD | `-6.02%` | -36,770,869.40 USD | `+0.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.0757` | `0.0758` | `0.0756` | `0.0757` | `7,857,936` | 594,936.69 USD | -63,020.80 USD | `-10.59%` | -36,833,890.21 USD | `+0.57` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.0757` | `0.0757` | `0.0756` | `0.0756` | `1,595,345` | 120,682.50 USD | -44,983.10 USD | `-37.27%` | -36,878,873.31 USD | `+0.61` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.0756` | `0.0759` | `0.0755` | `0.0759` | `82,682,111` | 6,252,708.50 USD | -1,451,638.46 USD | `-23.22%` | -36,318,700.86 USD | `-2.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0759` | `0.0761` | `0.0758` | `0.0758` | `46,301,408` | 3,515,276.40 USD | -423,355.24 USD | `-12.04%` | -36,742,056.10 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.0758` | `0.0759` | `0.0756` | `0.0756` | `16,735,807` | 1,267,258.58 USD | -105,726.44 USD | `-8.34%` | -36,847,782.54 USD | `+0.42` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0761` | `0.0768` | `0.0760` | `0.0764` | `146,510,025` | 11,190,544.13 USD | 113,754.53 USD | `+1.02%` | -32,260,134.26 USD | `+0.35` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0764` | `0.0765` | `0.0755` | `0.0756` | `201,594,432` | 15,303,841.53 USD | -2,746,811.49 USD | `-17.95%` | -35,006,945.75 USD | `-0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.0756` | `0.0761` | `0.0755` | `0.0756` | `145,719,326` | 11,035,243.48 USD | -1,980,720.14 USD | `-17.95%` | -36,987,665.90 USD | `-0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0761` | `0.0755` | `0.0756` | `144,953,642` | 10,977,370.16 USD | -2,026,655.28 USD | `-18.46%` | -33,725,863.99 USD | `+0.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | 1,581,082.63 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -21,458,643.59 USD | `-1.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -26,887,484.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0768` | `0.0755` | `0.0756` | `735,678,721` | 56,021,811.10 USD | -4,811,724.49 USD | `-8.59%` | -31,699,208.71 USD | `+0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0756` | `0.0761` | `0.0755` | `0.0756` | `144,953,642` | 10,977,370.16 USD | -2,026,655.28 USD | `-18.46%` | -33,725,863.99 USD | `+0.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.0754`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `0.0754` | `121247.0000` | 9,147.96 USD | 114,115.41 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0754` | `56266.0000` | 4,245.16 USD | 104,967.45 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0754` | `410225.0000` | 30,950.25 USD | 100,722.29 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `3454.0000` | 260.59 USD | 69,772.04 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `64564.0000` | 4,870.90 USD | 69,511.45 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `19881.0000` | 1,499.86 USD | 64,640.55 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `19881.0000` | 1,499.84 USD | 63,140.69 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `362263.0000` | 27,329.12 USD | 61,640.85 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `0.0754` | `19881.0000` | 1,499.80 USD | 34,311.73 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `179830.0000` | 13,566.02 USD | 32,811.92 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `64764.0000` | 4,885.60 USD | 19,245.91 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `35970.0000` | 2,713.43 USD | 14,360.31 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `19884.0000` | 1,499.95 USD | 11,646.87 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `95266.0000` | 7,186.30 USD | 10,146.92 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0754` | `39250.0000` | 2,960.63 USD | 2,960.63 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0754` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0754` | `402.0000` | 30.32 USD | 30.32 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0754` | `16992.0000` | 1,281.60 USD | 1,311.93 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0754` | `1340.0000` | 101.06 USD | 1,412.99 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0754` | `14526.0000` | 1,095.51 USD | 2,508.50 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0754` | `14526.0000` | 1,095.42 USD | 3,603.92 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0754` | `14526.0000` | 1,095.41 USD | 4,699.32 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0754` | `40313.0000` | 3,039.96 USD | 7,739.29 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0754` | `10895.0000` | 821.53 USD | 8,560.81 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0754` | `95266.0000` | 7,182.96 USD | 15,743.77 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0754` | `243483.0000` | 18,358.13 USD | 34,101.90 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.0754` | `37384.0000` | 2,818.64 USD | 36,920.55 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0754` | `1034.0000` | 77.96 USD | 36,998.50 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0754` | `34930.0000` | 2,633.44 USD | 39,631.95 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0754` | `66321.0000` | 4,999.94 USD | 44,631.89 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0754` | `48099.0000` | 3,626.04 USD | 48,257.93 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.0754` | `282909.0000` | 21,327.38 USD | 69,585.30 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `0.0754` | `14523.0000` | 1,094.82 USD | 70,680.12 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0754` | `22964.0000` | 1,731.10 USD | 72,411.22 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0754` | `4418.0000` | 333.03 USD | 72,744.25 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.0754` | `95681.0000` | 7,212.43 USD | 79,956.68 USD | `2 orders` | `-0.06%` | `-` |
| `ASK` | `0.0755` | `572089.0000` | 43,167.55 USD | 186,670.60 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `0.0755` | `79868.0000` | 6,026.36 USD | 143,503.05 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `25022.0000` | 1,887.98 USD | 137,476.69 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `18414.0000` | 1,389.37 USD | 135,588.71 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0755` | `266185.0000` | 20,083.92 USD | 134,199.34 USD | `3 orders` | `+0.03%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `310` | `0xb83d...6e36` | `SHORT` | 7,748,843.52 USD | `102,645,925.00` | `0.0946` | `0.0756` | `1.28` | 1,958,498.13 USD | `+25.27%` | `3X Cross` |
| `319` | `0xc63a...a3cd` | `LONG` | 7,545,600.00 USD | `100,000,000.00` | `0.0856` | `0.0756` | `0.000000` | -1,019,221.96 USD | `-13.51%` | `10X Cross` |
| `320` | `0x610b...b613` | `LONG` | 7,445,171.02 USD | `98,666,424.00` | `0.0872` | `0.0756` | `0.0605` | -1,155,010.88 USD | `-15.51%` | `5X Cross` |
| `615` | `0x5b5d...c060` | `SHORT` | 3,735,413.71 USD | `49,478,955.00` | `0.0946` | `0.0756` | `3.13` | 946,102.90 USD | `+25.33%` | `3X Cross` |
| `647` | `0xca49...53c8` | `SHORT` | 3,512,015.21 USD | `46,542,649.00` | `0.0929` | `0.0756` | `0.3938` | 814,029.47 USD | `+23.18%` | `10X Cross` |
| `659` | `0x45d2...4029` | `SHORT` | 3,425,392.96 USD | `45,426,000.00` | `0.0954` | `0.0756` | `0.9809` | 910,236.26 USD | `+26.57%` | `10X Cross` |
| `694` | `0xecb6...2b00` | `SHORT` | 3,266,792.24 USD | `43,271,637.00` | `0.0788` | `0.0756` | `0.7653` | 144,091.67 USD | `+4.41%` | `10X Cross` |
| `1201` | `0x458d...ab3b` | `LONG` | 1,845,254.69 USD | `24,454,063.00` | `0.1002` | `0.0756` | `0.0714` | -605,667.22 USD | `-32.82%` | `3X Isolated` |
| `1209` | `0xeadc...9d55` | `LONG` | 1,835,504.69 USD | `24,317,440.00` | `0.0926` | `0.0756` | `0.000000` | -416,089.89 USD | `-22.67%` | `10X Cross` |
| `1347` | `0xf48f...10fe` | `LONG` | 1,614,528.67 USD | `21,424,497.00` | `0.0968` | `0.0756` | `0.0480` | -459,775.94 USD | `-28.48%` | `4X Cross` |
| `1373` | `0x9946...0852` | `SHORT` | 1,572,650.32 USD | `20,845,267.00` | `0.0859` | `0.0756` | `0.1499` | 218,635.69 USD | `+13.90%` | `10X Cross` |
| `1585` | `0xcac1...26b3` | `SHORT` | 1,368,412.90 USD | `18,126,835.00` | `0.0943` | `0.0756` | `0.5416` | 341,046.30 USD | `+24.92%` | `10X Cross` |
| `1612` | `0x0d6a...ca57` | `LONG` | 1,329,880.78 USD | `17,626,455.00` | `0.0875` | `0.0756` | `0.0626` | -212,224.18 USD | `-15.96%` | `3X Isolated` |
| `1672` | `0x4808...a82c` | `LONG` | 1,270,373.34 USD | `16,828,143.00` | `0.0883` | `0.0756` | `0.0632` | -216,099.64 USD | `-17.01%` | `3X Cross` |
| `1681` | `0x9aa5...58af` | `SHORT` | 1,265,339.00 USD | `16,761,455.00` | `0.0907` | `0.0756` | `0.6231` | 254,396.89 USD | `+20.11%` | `10X Cross` |
| `1813` | `0x31ef...f715` | `LONG` | 1,149,233.04 USD | `15,230,102.00` | `0.0936` | `0.0756` | `0.0668` | -276,462.89 USD | `-24.06%` | `3X Isolated` |
| `1834` | `0xbfc7...80b4` | `SHORT` | 1,133,874.82 USD | `15,020,000.00` | `0.0920` | `0.0756` | `0.1771` | 248,524.47 USD | `+21.92%` | `10X Cross` |
| `1917` | `0x7cee...fc93` | `SHORT` | 1,057,946.77 USD | `14,013,468.00` | `0.0863` | `0.0756` | `0.2627` | 150,930.60 USD | `+14.27%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0783` | 7,766.99 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 7.77K USD at 0.0783 USD [API] | `2026-10-17 21:32:17` |
| `ANNOUNCEMENT` | `INFO` | `0.0783` | 234.78 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 0.23K USD at 0.0783 USD [API] | `2026-10-17 21:32:17` |
| `ANNOUNCEMENT` | `INFO` | `0.0783` | 234.79 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 0.23K USD at 0.0783 USD [API] | `2026-10-17 21:32:17` |
| `ANNOUNCEMENT` | `INFO` | `0.0783` | 7,881.34 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 7.88K USD at 0.0783 USD [API] | `2026-10-17 21:32:17` |
| `ANNOUNCEMENT` | `INFO` | `0.0782` | 5,001.16 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 5.00K USD at 0.0782 USD [API] | `2026-10-29 09:16:31` |
| `ANNOUNCEMENT` | `INFO` | `0.0783` | 5,002.89 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.00K USD at 0.0783 USD [API] | `2026-10-29 09:19:04` |
| `ANNOUNCEMENT` | `INFO` | `0.0782` | 6,305.19 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.31K USD at 0.0782 USD [API] | `2026-10-29 09:28:21` |
| `ANNOUNCEMENT` | `INFO` | `0.0781` | 10,286.97 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 10.29K USD at 0.0781 USD [API] | `2026-10-29 09:48:31` |
| `ANNOUNCEMENT` | `INFO` | `0.0780` | 5,273.56 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.27K USD at 0.0780 USD [API] | `2026-10-29 10:28:51` |
| `ANNOUNCEMENT` | `INFO` | `0.0784` | 5,209.28 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 5.21K USD at 0.0784 USD [API] | `2026-10-29 10:47:36` |
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 6,966.22 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 6.97K USD at 0.0786 USD [API] | `2026-10-29 11:01:48` |
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 6,257.77 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 6.26K USD at 0.0786 USD [API] | `2026-10-29 11:01:48` |
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 10,493.93 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.49K USD at 0.0786 USD [API] | `2026-10-29 11:01:48` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 42,624.00 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 42.62K USD at 0.0800 USD [API] | `2026-10-15 02:22:46` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 7,468.63 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.47K USD at 0.0791 USD [API] | `2026-10-29 13:15:02` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 7,925.53 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.93K USD at 0.0792 USD [API] | `2026-10-29 13:17:45` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 23,358.29 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 23.36K USD at 0.0791 USD [API] | `2026-10-29 13:24:17` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 5,177.50 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.18K USD at 0.0791 USD [API] | `2026-10-29 13:24:17` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.86%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--3.98%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.86%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--3.98%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.86%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--3.98%`)
  * 7D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+2.86%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--3.98%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0152` | 1,690.00 USD | 16,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0152` | 182.53 USD | 16,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 16,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 16,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0171` | 1,030.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0174` | 1,030.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0181` | 1,360.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0198` | 632.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 18,970.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0216` | 541.25 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0217` | 131.61 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0222` | 33,260.00 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0230` | 896.17 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 367.23 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0240` | 21,490.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0244` | 12,220.00 USD | 16,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0253` | 4,000.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0255` | 393.38 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0261` | 523.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0276` | 147.23 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0283` | 912.42 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0294` | 506.67 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0300` | 1,120.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0307` | 265.80 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0316` | 5,950.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0326` | 458.31 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0330` | 757.85 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 393.23 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0341` | 4,590.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0350` | 13,620.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0360` | 8,390.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0367` | 34,820.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0377` | 170.44 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0379` | 3,790.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 1,600.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0382` | 179.78 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0384` | 156.30 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 2,160.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 2,180.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0399` | 103.31 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0403` | 77,960.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 5,400.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 6,130.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0418` | 100.19 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 43,500.00 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 455.06 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 883.34 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 2,960.00 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0428` | 948.23 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 5,770.00 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 111,720.00 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 10,120.00 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0437` | 12,810.00 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 2,620.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 1,640.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 681.05 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 810.81 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 1,240.00 USD | 16,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 16,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 689.25 USD | 16,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 5,680.00 USD | 16,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 10,460.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0469` | 96,820.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0471` | 1,010,000.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 1,600.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 1,420.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 39,340.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0478` | 258.87 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0479` | 2,400.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 58,890.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 1,780.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 2,780.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 5,180.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 106.23 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,310.00 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 3,760.00 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 256.75 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 991.41 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 396.47 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 33,640.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 4,420.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 4,690.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 279,570.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,210.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,430.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 852.09 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 182,040.00 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 9,840.00 USD | 14,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 8,100.00 USD | 14,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 42,580.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 930.83 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 1,040.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 45,370.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 425.43 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 28,760.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 14,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 3,030.00 USD | 14,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 95,630.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 903.30 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 3,230.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 3,250.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0549` | 344.18 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 1,760.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0554` | 4,000.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 1,100.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 8,410.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 144.08 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 40,620.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 568.50 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 315.67 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 1,290.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 4,060.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,960.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 4,310.00 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 441.75 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 4,130.00 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 582.50 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 16,730.00 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 305.15 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 398.74 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 546.26 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,140.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,300.00 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 644.22 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 2,110.00 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 360,940.00 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 7,210.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 845.25 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 5,960,000.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 7,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 622.63 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 2,350.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 8,580.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 629.72 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 719.81 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,890.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 28,460.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 27,580.00 USD | 7,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 576.69 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 43,420.00 USD | 7,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 870.40 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 2,630.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,310,000.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 3,030.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 9,740.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,990.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 150.01 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 3,270.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 1,330.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 76,280.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 27,180.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 631.94 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0646` | 1,230.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0647` | 29,780,000.00 USD | 29,780,000.00 USD | 23,160.00 USD | 13,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0648` | 162,920.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 8,800.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0649` | 29,740,000.00 USD | 29,740,000.00 USD | 21,850.00 USD | 0.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 7,790.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0657` | 14,160.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0657` | 29,710,000.00 USD | 29,710,000.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 9,600.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0661` | 29,690,000.00 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0662` | 2,280.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0663` | 29,650,000.00 USD | 29,650,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0664` | 17,410.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,270.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0665` | 29,640,000.00 USD | 29,640,000.00 USD | 169,640.00 USD | 12,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0665` | 9,240.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 8,880.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,150,000.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0669` | 29,460,000.00 USD | 29,460,000.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0669` | 3,990.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,050.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 4,830.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 2,050.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0675` | 29,460,000.00 USD | 29,460,000.00 USD | 25,430.00 USD | 8,460.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0675` | 112,780.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 12,610.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0677` | 29,410,000.00 USD | 29,410,000.00 USD | 10,470.00 USD | 0.00 USD | 475.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 17,350,000.00 USD | 17,350,000.00 USD | 20,570.00 USD | 61,960.00 USD | 82,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 34,090.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 17,190,000.00 USD | 17,190,000.00 USD | 43,120.00 USD | 38,120.00 USD | 86.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0679` | 29,390,000.00 USD | 29,390,000.00 USD | 6,140.00 USD | 59,770.00 USD | 61,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 17,110,000.00 USD | 17,110,000.00 USD | 51,160.00 USD | 43,850.00 USD | 34,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 10,960.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 16,980,000.00 USD | 16,980,000.00 USD | 36,810.00 USD | 55,770.00 USD | 150,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0681` | 29,270,000.00 USD | 29,270,000.00 USD | 118,640.00 USD | 61,880.00 USD | 164,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0682` | 16,730,000.00 USD | 16,730,000.00 USD | 14,920.00 USD | 58,710.00 USD | 27,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 55,770.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 16,630,000.00 USD | 16,630,000.00 USD | 15,780.00 USD | 32,750.00 USD | 467.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0683` | 28,920,000.00 USD | 28,920,000.00 USD | 0.00 USD | 58,370.00 USD | 66,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0684` | 16,580,000.00 USD | 16,580,000.00 USD | 24,150.00 USD | 26,540.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 113,760.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 16,530,000.00 USD | 16,530,000.00 USD | 58,140.00 USD | 14,450.00 USD | 28,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0685` | 28,800,000.00 USD | 28,800,000.00 USD | 142,840.00 USD | 77,920.00 USD | 25,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 8,890.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 16,430,000.00 USD | 16,430,000.00 USD | 56,540.00 USD | 17,000.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 4,840.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 16,340,000.00 USD | 16,340,000.00 USD | 17,350.00 USD | 32,460.00 USD | 30,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0687` | 28,550,000.00 USD | 28,550,000.00 USD | 101,720.00 USD | 128,090.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 16,260,000.00 USD | 16,260,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 345.83 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0689` | 16,200,000.00 USD | 16,200,000.00 USD | 10,400.00 USD | 0.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0689` | 28,320,000.00 USD | 28,320,000.00 USD | 225,480.00 USD | 77,640.00 USD | 61,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0689` | 508,320.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0690` | 16,190,000.00 USD | 16,190,000.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0691` | 6,960.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 16,180,000.00 USD | 16,180,000.00 USD | 1,460.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0691` | 27,960,000.00 USD | 27,960,000.00 USD | 162,010.00 USD | 95,020.00 USD | 130,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 26,150.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 16,180,000.00 USD | 16,180,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 10,100.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0693` | 16,160,000.00 USD | 16,160,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0693` | 27,570,000.00 USD | 27,570,000.00 USD | 207,150.00 USD | 190,180.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0694` | 16,140,000.00 USD | 16,140,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0694` | 8,070.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 16,110,000.00 USD | 16,110,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0695` | 27,090,000.00 USD | 27,090,000.00 USD | 282,470.00 USD | 212,530.00 USD | 212,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 4,950.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 16,110,000.00 USD | 16,110,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0697` | 26,380,000.00 USD | 26,380,000.00 USD | 142,190.00 USD | 148,620.00 USD | 263,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 6,970.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 16,050,000.00 USD | 16,050,000.00 USD | 10,960.00 USD | 10,400.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 2,910.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 16,020,000.00 USD | 16,020,000.00 USD | 38,680.00 USD | 0.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0699` | 25,830,000.00 USD | 25,830,000.00 USD | 325,570.00 USD | 205,450.00 USD | 138,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 15,980,000.00 USD | 15,980,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 15,850,000.00 USD | 15,850,000.00 USD | 39,680.00 USD | 108,360.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0701` | 25,160,000.00 USD | 25,160,000.00 USD | 283,670.00 USD | 119,790.00 USD | 142,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 8,310.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 15,700,000.00 USD | 15,700,000.00 USD | 48,350.00 USD | 19,670.00 USD | 59.13 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 1,070.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 15,630,000.00 USD | 15,630,000.00 USD | 161,920.00 USD | 66,830.00 USD | 10,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0703` | 24,610,000.00 USD | 24,610,000.00 USD | 261,240.00 USD | 120,430.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 3,790.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 15,400,000.00 USD | 15,400,000.00 USD | 27,140.00 USD | 43,930.00 USD | 22,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 780.37 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 15,300,000.00 USD | 15,300,000.00 USD | 41,460.00 USD | 30,720.00 USD | 48,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0705` | 24,180,000.00 USD | 24,180,000.00 USD | 224,080.00 USD | 133,180.00 USD | 178,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 15,180,000.00 USD | 15,180,000.00 USD | 22,880.00 USD | 1,120.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 608.86 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 15,140,000.00 USD | 15,140,000.00 USD | 136,920.00 USD | 69,310.00 USD | 45,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0707` | 23,650,000.00 USD | 23,650,000.00 USD | 171,490.00 USD | 37,160.00 USD | 156,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 14,890,000.00 USD | 14,890,000.00 USD | 69,400.00 USD | 62,000.00 USD | 107,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0709` | 14,650,000.00 USD | 14,650,000.00 USD | 38,730.00 USD | 82,010.00 USD | 149,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0709` | 23,280,000.00 USD | 23,280,000.00 USD | 485,290.00 USD | 159,720.00 USD | 139,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 821.60 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 14,380,000.00 USD | 14,380,000.00 USD | 117,230.00 USD | 91,550.00 USD | 119,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 4,720.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 14,050,000.00 USD | 14,050,000.00 USD | 49,210.00 USD | 25,670.00 USD | 43,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0711` | 22,500,000.00 USD | 22,500,000.00 USD | 285,730.00 USD | 252,130.00 USD | 91,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,860.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 13,930,000.00 USD | 13,930,000.00 USD | 165,590.00 USD | 46,690.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 802.06 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 13,720,000.00 USD | 13,720,000.00 USD | 75,840.00 USD | 85,230.00 USD | 63,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0713` | 21,870,000.00 USD | 21,870,000.00 USD | 379,600.00 USD | 171,480.00 USD | 139,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 13,490,000.00 USD | 13,490,000.00 USD | 120,780.00 USD | 51,930.00 USD | 48,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 13,270.00 USD | 384,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 13,270,000.00 USD | 13,270,000.00 USD | 75,940.00 USD | 238,460.00 USD | 43,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0715` | 21,180,000.00 USD | 21,180,000.00 USD | 211,700.00 USD | 51,460.00 USD | 66,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 371,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 12,910,000.00 USD | 12,910,000.00 USD | 19,480.00 USD | 51,080.00 USD | 173.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 3,840.00 USD | 363,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 12,840,000.00 USD | 12,840,000.00 USD | 238,310.00 USD | 96,160.00 USD | 385.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0717` | 20,850,000.00 USD | 20,850,000.00 USD | 285,100.00 USD | 190,890.00 USD | 48,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 22,070.00 USD | 359,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 12,510,000.00 USD | 12,510,000.00 USD | 64,570.00 USD | 101,030.00 USD | 13,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 960.13 USD | 337,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 12,330,000.00 USD | 12,330,000.00 USD | 229,400.00 USD | 45,330.00 USD | 72,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0719` | 20,320,000.00 USD | 20,320,000.00 USD | 233,070.00 USD | 63,390.00 USD | 276,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 5,880.00 USD | 336,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 11,980,000.00 USD | 11,980,000.00 USD | 138,650.00 USD | 50,600.00 USD | 72,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 4,750.00 USD | 330,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 11,720,000.00 USD | 11,720,000.00 USD | 308,410.00 USD | 298,040.00 USD | 67,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0721` | 19,750,000.00 USD | 19,750,000.00 USD | 422,700.00 USD | 285,460.00 USD | 95,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 758.08 USD | 325,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 11,050,000.00 USD | 11,050,000.00 USD | 181,970.00 USD | 122,030.00 USD | 150,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 38,340.00 USD | 324,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 10,590,000.00 USD | 10,590,000.00 USD | 85,680.00 USD | 258,330.00 USD | 326,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0723` | 18,950,000.00 USD | 18,950,000.00 USD | 242,550.00 USD | 148,860.00 USD | 110,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 285,380.00 USD | 286,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 9,920,000.00 USD | 9,920,000.00 USD | 141,120.00 USD | 214,730.00 USD | 382,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 984.89 USD | 1,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 9,180,000.00 USD | 9,180,000.00 USD | 245,770.00 USD | 252,860.00 USD | 293,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0725` | 18,440,000.00 USD | 18,440,000.00 USD | 1,070,000.00 USD | 365,360.00 USD | 152,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 8,390,000.00 USD | 8,390,000.00 USD | 132,320.00 USD | 139,590.00 USD | 59,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 115.51 USD | 115.51 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 8,060,000.00 USD | 8,060,000.00 USD | 190,550.00 USD | 161,760.00 USD | 45,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0727` | 16,860,000.00 USD | 16,860,000.00 USD | 249,200.00 USD | 432,030.00 USD | 92,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 7,660,000.00 USD | 7,660,000.00 USD | 60,510.00 USD | 154,910.00 USD | 48,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 7,400,000.00 USD | 7,400,000.00 USD | 58,550.00 USD | 41,110.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0729` | 16,080,000.00 USD | 16,080,000.00 USD | 114,120.00 USD | 105,410.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 7,290,000.00 USD | 7,290,000.00 USD | 123,090.00 USD | 55,310.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 7,060,000.00 USD | 7,060,000.00 USD | 44,230.00 USD | 81,130.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0731` | 15,830,000.00 USD | 15,830,000.00 USD | 565,310.00 USD | 49,290.00 USD | 12,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 6,910,000.00 USD | 6,910,000.00 USD | 153,570.00 USD | 93,810.00 USD | 93,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 6,570,000.00 USD | 6,570,000.00 USD | 64,680.00 USD | 96,060.00 USD | 31,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0733` | 15,200,000.00 USD | 15,200,000.00 USD | 470,120.00 USD | 0.00 USD | 29,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 6,370,000.00 USD | 6,370,000.00 USD | 361,270.00 USD | 80,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 5,930,000.00 USD | 5,930,000.00 USD | 141,790.00 USD | 23,950.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0735` | 14,700,000.00 USD | 14,700,000.00 USD | 589,440.00 USD | 93,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 5,760,000.00 USD | 5,760,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 5,520,000.00 USD | 5,520,000.00 USD | 113,510.00 USD | 52,730.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0737` | 14,020,000.00 USD | 14,020,000.00 USD | 506,070.00 USD | 494,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 5,300,000.00 USD | 5,300,000.00 USD | 78,630.00 USD | 23,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 5,200,000.00 USD | 5,200,000.00 USD | 128,640.00 USD | 17,470.00 USD | 22,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0739` | 13,020,000.00 USD | 13,020,000.00 USD | 265,850.00 USD | 515,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 5,030,000.00 USD | 5,030,000.00 USD | 41,890.00 USD | 102,110.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,800,000.00 USD | 4,800,000.00 USD | 175,330.00 USD | 166,190.00 USD | 102,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0741` | 12,240,000.00 USD | 12,240,000.00 USD | 66,970.00 USD | 294,670.00 USD | 178,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 4,360,000.00 USD | 4,360,000.00 USD | 90,280.00 USD | 290,690.00 USD | 80,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,900,000.00 USD | 3,900,000.00 USD | 236,300.00 USD | 181,510.00 USD | 284,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0743` | 11,700,000.00 USD | 11,700,000.00 USD | 774,380.00 USD | 209,100.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,200,000.00 USD | 3,200,000.00 USD | 217,450.00 USD | 118,720.00 USD | 107,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 2,750,000.00 USD | 2,750,000.00 USD | 87,580.00 USD | 88,750.00 USD | 46,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0745` | 9,600,000.00 USD | 9,600,000.00 USD | 1,360,000.00 USD | 951,300.00 USD | 326,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,530,000.00 USD | 2,530,000.00 USD | 88,460.00 USD | 86,840.00 USD | 142,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 2,210,000.00 USD | 2,210,000.00 USD | 625,930.00 USD | 210,220.00 USD | 148,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0747` | 6,960,000.00 USD | 6,960,000.00 USD | 1,410,000.00 USD | 1,830,000.00 USD | 649,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,230,000.00 USD | 1,230,000.00 USD | 98,680.00 USD | 109,690.00 USD | 198,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 818,980.00 USD | 818,980.00 USD | 122,780.00 USD | 90,750.00 USD | 131,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0749` | 3,070,000.00 USD | 3,070,000.00 USD | 706,340.00 USD | 459,930.00 USD | 875,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 473,930.00 USD | 473,930.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 409,590.00 USD | 409,590.00 USD | 0.00 USD | 37,490.00 USD | 10,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0751` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 30,900.00 USD | 84,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 361,560.00 USD | 361,560.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 337,140.00 USD | 337,140.00 USD | 0.00 USD | 12,650.00 USD | 141,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0753` | 907,280.00 USD | 907,280.00 USD | 751,120.00 USD | 53,860.00 USD | 102,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0755` | 182,850.00 USD | 182,850.00 USD | 182,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0755` | 938,670.00 USD | 938,670.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0755` | 1,880,000.00 USD | 1,880,000.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0756` | 30,100.00 USD | 30,100.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0756` | 60,200.00 USD | 60,200.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0757` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 144,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0758` | 65,120.00 USD | 65,120.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0759` | 65,280.00 USD | 65,280.00 USD | 0.00 USD | 0.00 USD | 160.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0759` | 2,130,000.00 USD | 2,130,000.00 USD | 40,360.00 USD | 66,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 65,700.00 USD | 65,700.00 USD | 0.00 USD | 0.00 USD | 420.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0762` | 65,870.00 USD | 65,870.00 USD | 0.00 USD | 0.00 USD | 168.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 80,690.00 USD | 80,690.00 USD | 0.00 USD | 14,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 428,850.00 USD | 428,850.00 USD | 211,600.00 USD | 37,120.00 USD | 99,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0765` | 3,400,000.00 USD | 3,400,000.00 USD | 772,480.00 USD | 496,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 1,540,000.00 USD | 1,540,000.00 USD | 586,470.00 USD | 522,700.00 USD | 291.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 2,210,000.00 USD | 2,210,000.00 USD | 188,080.00 USD | 328,450.00 USD | 159,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0767` | 4,670,000.00 USD | 4,670,000.00 USD | 1,180,000.00 USD | 90,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 3,130,000.00 USD | 3,130,000.00 USD | 224,320.00 USD | 93,770.00 USD | 594,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 4,180,000.00 USD | 4,180,000.00 USD | 305,260.00 USD | 438,740.00 USD | 310,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0769` | 5,940,000.00 USD | 5,940,000.00 USD | 760,570.00 USD | 84,300.00 USD | 429,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 5,310,000.00 USD | 5,310,000.00 USD | 396,020.00 USD | 281,820.00 USD | 450,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 6,400,000.00 USD | 6,400,000.00 USD | 398,660.00 USD | 441,880.00 USD | 251,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0771` | 8,430,000.00 USD | 8,430,000.00 USD | 888,600.00 USD | 798,440.00 USD | 794,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 7,980,000.00 USD | 7,980,000.00 USD | 480,450.00 USD | 327,770.00 USD | 765,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 8,780,000.00 USD | 8,780,000.00 USD | 190,960.00 USD | 368,960.00 USD | 243,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0773` | 8,910,000.00 USD | 8,910,000.00 USD | 69,030.00 USD | 347,590.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 9,180,000.00 USD | 9,180,000.00 USD | 118,800.00 USD | 246,740.00 USD | 36,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 373.31 USD | 373.31 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0775` | 9,710,000.00 USD | 9,710,000.00 USD | 288,570.00 USD | 180,890.00 USD | 61,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0775` | 10,060,000.00 USD | 10,060,000.00 USD | 779,670.00 USD | 375,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 614.26 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 10,350,000.00 USD | 10,350,000.00 USD | 284,830.00 USD | 214,460.00 USD | 142,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 11,260,000.00 USD | 11,260,000.00 USD | 401,010.00 USD | 342,630.00 USD | 163,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0777` | 10,620,000.00 USD | 10,620,000.00 USD | 265,980.00 USD | 286,560.00 USD | 693.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 12,120,000.00 USD | 12,120,000.00 USD | 116,640.00 USD | 340,450.00 USD | 401,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 12,880,000.00 USD | 12,880,000.00 USD | 345,840.00 USD | 210,420.00 USD | 205,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0779` | 11,630,000.00 USD | 11,630,000.00 USD | 270,450.00 USD | 301,690.00 USD | 438,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 13,210,000.00 USD | 13,210,000.00 USD | 212,580.00 USD | 78,920.00 USD | 39,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 13,580,000.00 USD | 13,580,000.00 USD | 151,030.00 USD | 193,800.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0781` | 11,960,000.00 USD | 11,960,000.00 USD | 186,410.00 USD | 142,450.00 USD | 4,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 13,810,000.00 USD | 13,810,000.00 USD | 70,430.00 USD | 84,580.00 USD | 79,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 14,250,000.00 USD | 14,250,000.00 USD | 48,890.00 USD | 214,890.00 USD | 177,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0783` | 12,450,000.00 USD | 12,450,000.00 USD | 15,350.00 USD | 285,880.00 USD | 193,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 14,770,000.00 USD | 14,770,000.00 USD | 353,240.00 USD | 110,170.00 USD | 50,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 15,240,000.00 USD | 15,240,000.00 USD | 208,550.00 USD | 161,570.00 USD | 102,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0785` | 13,070,000.00 USD | 13,070,000.00 USD | 197,420.00 USD | 141,600.00 USD | 278,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0785` | 9,220.00 USD | 9,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0786` | 16,080,000.00 USD | 16,080,000.00 USD | 330,770.00 USD | 209,740.00 USD | 296,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 17,310,000.00 USD | 17,310,000.00 USD | 379,110.00 USD | 464,730.00 USD | 386,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0787` | 14,670,000.00 USD | 14,670,000.00 USD | 437,500.00 USD | 346,050.00 USD | 812,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 9,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 17,860,000.00 USD | 17,860,000.00 USD | 168,080.00 USD | 262,350.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 18,510,000.00 USD | 18,510,000.00 USD | 312,410.00 USD | 233,260.00 USD | 102,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0789` | 15,480,000.00 USD | 15,480,000.00 USD | 301,760.00 USD | 259,180.00 USD | 249,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 18,780,000.00 USD | 18,780,000.00 USD | 153,960.00 USD | 87,240.00 USD | 27,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 19,240,000.00 USD | 19,240,000.00 USD | 199,650.00 USD | 133,580.00 USD | 125,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0791` | 16,040,000.00 USD | 16,040,000.00 USD | 476,430.00 USD | 81,300.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 19,590,000.00 USD | 19,590,000.00 USD | 224,560.00 USD | 57,840.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0793` | 19,600,000.00 USD | 19,600,000.00 USD | 5,950.00 USD | 0.00 USD | 289.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0793` | 16,380,000.00 USD | 16,380,000.00 USD | 27,550.00 USD | 61,220.00 USD | 246,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0794` | 19,950,000.00 USD | 19,950,000.00 USD | 158,580.00 USD | 96,210.00 USD | 100,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 104.72 USD | 10,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0795` | 20,200,000.00 USD | 20,200,000.00 USD | 92,560.00 USD | 45,380.00 USD | 103,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0795` | 17,050,000.00 USD | 17,050,000.00 USD | 206,900.00 USD | 0.00 USD | 469,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 20,410,000.00 USD | 20,410,000.00 USD | 199,280.00 USD | 12,890.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0796` | 326.09 USD | 10,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0797` | 20,770,000.00 USD | 20,770,000.00 USD | 206,810.00 USD | 89,760.00 USD | 65,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0797` | 18,020,000.00 USD | 18,020,000.00 USD | 640,790.00 USD | 203,560.00 USD | 119,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 20,940,000.00 USD | 20,940,000.00 USD | 58,670.00 USD | 110,930.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 21,340,000.00 USD | 21,340,000.00 USD | 99,030.00 USD | 191,860.00 USD | 107,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0799` | 18,790,000.00 USD | 18,790,000.00 USD | 561,590.00 USD | 130,870.00 USD | 78,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 21,500,000.00 USD | 21,500,000.00 USD | 48,550.00 USD | 9,760.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 21,520,000.00 USD | 21,520,000.00 USD | 25,740.00 USD | 0.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0801` | 18,980,000.00 USD | 18,980,000.00 USD | 85,040.00 USD | 0.00 USD | 104,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 21,550,000.00 USD | 21,550,000.00 USD | 25,490.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0803` | 314.26 USD | 10,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0803` | 21,660,000.00 USD | 21,660,000.00 USD | 21,230.00 USD | 43,340.00 USD | 41,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0803` | 19,020,000.00 USD | 19,020,000.00 USD | 42,220.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 21,670,000.00 USD | 21,670,000.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0804` | 826.14 USD | 11,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0805` | 21,840,000.00 USD | 21,840,000.00 USD | 89,620.00 USD | 37,230.00 USD | 41,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0805` | 19,350,000.00 USD | 19,350,000.00 USD | 228,320.00 USD | 43,910.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 22,100,000.00 USD | 22,100,000.00 USD | 28,730.00 USD | 21,040.00 USD | 215,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 22,510,000.00 USD | 22,510,000.00 USD | 228,350.00 USD | 143,670.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0807` | 20,790,000.00 USD | 20,790,000.00 USD | 217,720.00 USD | 934,840.00 USD | 294,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 23,160,000.00 USD | 23,160,000.00 USD | 150,860.00 USD | 116,140.00 USD | 382,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 23,500,000.00 USD | 23,500,000.00 USD | 109,380.00 USD | 220,760.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0809` | 22,570,000.00 USD | 22,570,000.00 USD | 9,880.00 USD | 1,760,000.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 23,950,000.00 USD | 23,950,000.00 USD | 192,870.00 USD | 127,690.00 USD | 132,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 24,210,000.00 USD | 24,210,000.00 USD | 100,060.00 USD | 145,810.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0811` | 23,430,000.00 USD | 23,430,000.00 USD | 131,030.00 USD | 730,620.00 USD | 1,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 24,500,000.00 USD | 24,500,000.00 USD | 138,630.00 USD | 102,020.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 24,680,000.00 USD | 24,680,000.00 USD | 45,000.00 USD | 30,430.00 USD | 109,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0813` | 24,500,000.00 USD | 24,500,000.00 USD | 517,320.00 USD | 548,390.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 25,020,000.00 USD | 25,020,000.00 USD | 43,650.00 USD | 108,690.00 USD | 184,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 25,140,000.00 USD | 25,140,000.00 USD | 20,890.00 USD | 6,740.00 USD | 94,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0815` | 26,110,000.00 USD | 26,110,000.00 USD | 671,840.00 USD | 643,990.00 USD | 300,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 25,840,000.00 USD | 25,840,000.00 USD | 323,740.00 USD | 194,310.00 USD | 179,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 26,390,000.00 USD | 26,390,000.00 USD | 280,410.00 USD | 134,560.00 USD | 130,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0817` | 28,680,000.00 USD | 28,680,000.00 USD | 1,200,000.00 USD | 745,850.00 USD | 614,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0818` | 27,050,000.00 USD | 27,050,000.00 USD | 234,840.00 USD | 161,260.00 USD | 267,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 11,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 27,650,000.00 USD | 27,650,000.00 USD | 158,800.00 USD | 312,480.00 USD | 128,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0819` | 30,790,000.00 USD | 30,790,000.00 USD | 672,340.00 USD | 512,490.00 USD | 929,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 28,190,000.00 USD | 28,190,000.00 USD | 52,420.00 USD | 172,050.00 USD | 319,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 28,480,000.00 USD | 28,480,000.00 USD | 151,670.00 USD | 48,110.00 USD | 85,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0821` | 33,150,000.00 USD | 33,150,000.00 USD | 1,210,000.00 USD | 760,670.00 USD | 390,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 29,040,000.00 USD | 29,040,000.00 USD | 249,310.00 USD | 151,600.00 USD | 156,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 29,380,000.00 USD | 29,380,000.00 USD | 267,050.00 USD | 72,540.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0823` | 34,920,000.00 USD | 34,920,000.00 USD | 884,810.00 USD | 520,900.00 USD | 366,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 29,950,000.00 USD | 29,950,000.00 USD | 168,680.00 USD | 204,930.00 USD | 190,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 30,200,000.00 USD | 30,200,000.00 USD | 102,430.00 USD | 125,690.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0825` | 36,500,000.00 USD | 36,500,000.00 USD | 761,460.00 USD | 514,320.00 USD | 307,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 30,630,000.00 USD | 30,630,000.00 USD | 131,950.00 USD | 125,260.00 USD | 170,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 30,720,000.00 USD | 30,720,000.00 USD | 13,110.00 USD | 62,110.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0827` | 37,650,000.00 USD | 37,650,000.00 USD | 658,340.00 USD | 220,660.00 USD | 271,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 31,050,000.00 USD | 31,050,000.00 USD | 187,960.00 USD | 75,940.00 USD | 66,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0828` | 120.96 USD | 12,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0829` | 31,310,000.00 USD | 31,310,000.00 USD | 168,550.00 USD | 88,230.00 USD | 326.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0829` | 38,690,000.00 USD | 38,690,000.00 USD | 645,990.00 USD | 177,740.00 USD | 214,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 31,440,000.00 USD | 31,440,000.00 USD | 54,060.00 USD | 37,820.00 USD | 43,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 31,520,000.00 USD | 31,520,000.00 USD | 22,160.00 USD | 16,920.00 USD | 37,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0831` | 39,590,000.00 USD | 39,590,000.00 USD | 452,190.00 USD | 160,720.00 USD | 288,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 15,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 31,900,000.00 USD | 31,900,000.00 USD | 185,880.00 USD | 93,160.00 USD | 100,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 500.17 USD | 15,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0833` | 32,320,000.00 USD | 32,320,000.00 USD | 130,200.00 USD | 111,030.00 USD | 181,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0833` | 40,810,000.00 USD | 40,810,000.00 USD | 524,880.00 USD | 414,820.00 USD | 276,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 32,710,000.00 USD | 32,710,000.00 USD | 128,050.00 USD | 118,950.00 USD | 144,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 33,070,000.00 USD | 33,070,000.00 USD | 109,250.00 USD | 188,990.00 USD | 64,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0835` | 41,970,000.00 USD | 41,970,000.00 USD | 365,460.00 USD | 261,800.00 USD | 536,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 33,340,000.00 USD | 33,340,000.00 USD | 44,050.00 USD | 74,690.00 USD | 147,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 16,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 33,570,000.00 USD | 33,570,000.00 USD | 130,410.00 USD | 32,170.00 USD | 62,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0837` | 42,770,000.00 USD | 42,770,000.00 USD | 453,970.00 USD | 227,430.00 USD | 115,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 17,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 33,870,000.00 USD | 33,870,000.00 USD | 180,800.00 USD | 85,610.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 34,000,000.00 USD | 34,000,000.00 USD | 60,660.00 USD | 32,460.00 USD | 29,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0839` | 43,250,000.00 USD | 43,250,000.00 USD | 321,350.00 USD | 128,090.00 USD | 36,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0840` | 34,080,000.00 USD | 34,080,000.00 USD | 28,070.00 USD | 24,900.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0841` | 34,100,000.00 USD | 34,100,000.00 USD | 9,490.00 USD | 2,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0841` | 43,520,000.00 USD | 43,520,000.00 USD | 205,170.00 USD | 0.00 USD | 64,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0842` | 34,140,000.00 USD | 34,140,000.00 USD | 0.00 USD | 0.00 USD | 46,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 264.21 USD | 18,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0843` | 44,020,000.00 USD | 44,020,000.00 USD | 337,540.00 USD | 77,640.00 USD | 85,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0845` | 44,490,000.00 USD | 44,490,000.00 USD | 234,950.00 USD | 95,020.00 USD | 138,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0847` | 45,000,000.00 USD | 45,000,000.00 USD | 244,090.00 USD | 190,180.00 USD | 77,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 426.71 USD | 18,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0849` | 45,730,000.00 USD | 45,730,000.00 USD | 310,690.00 USD | 205,870.00 USD | 208,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 46,060,000.00 USD | 46,060,000.00 USD | 87,360.00 USD | 53,240.00 USD | 186,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 18,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,250.00 USD | 22,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0868` | 155.98 USD | 23,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0871` | 138.58 USD | 23,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 23,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 24,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 24,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 24,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0905` | 6,760.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 1,310.00 USD | 32,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 4,940.00 USD | 37,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 37,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 805.37 USD | 38,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0938` | 4,220.00 USD | 42,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0940` | 914.70 USD | 43,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0944` | 39,700.00 USD | 83,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0946` | 192.61 USD | 83,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 24,460.00 USD | 108,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 48,290.00 USD | 156,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 157,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0970` | 365.68 USD | 157,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 121.23 USD | 157,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 158,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1003` | 1,420.00 USD | 159,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1012` | 2,960.00 USD | 162,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 170,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 173,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 173,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 179,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1062` | 3,290.00 USD | 182,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 183,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 186,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1095` | 1,880.00 USD | 188,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 188,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1137` | 147.86 USD | 189,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1152` | 147.05 USD | 189,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1211` | 874.58 USD | 190,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 637.53 USD | 190,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1231` | 118.84 USD | 190,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 190,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 191,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 193,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 193,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1328` | 45,470.00 USD | 238,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 239,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1368` | 1,160.00 USD | 240,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 240,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1424` | 23,090.00 USD | 263,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1426` | 1,800.00 USD | 265,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 267,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 2,030.00 USD | 269,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1442` | 45,670.00 USD | 315,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 316,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1446` | 144.55 USD | 317,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1452` | 1,920.00 USD | 318,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1457` | 1,270.00 USD | 320,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,110.00 USD | 328,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1490` | 3,110,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1494` | 24,030.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0152` | 16,720,000.00 USD | 0.00 USD | 1,690.00 USD | `-79.96%` | `111,254.00` |
| `Live` | `Long` | `0.0152` | 16,720,000.00 USD | 0.00 USD | 182.53 USD | `-79.83%` | `11,969.00` |
| `Live` | `Long` | `0.0160` | 16,720,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.77%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,720,000.00 USD | 0.00 USD | 407.02 USD | `-78.24%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,720,000.00 USD | 0.00 USD | 5,290.00 USD | `-78.11%` | `319,394.00` |
| `Live` | `Long` | `0.0171` | 16,710,000.00 USD | 0.00 USD | 1,030.00 USD | `-77.31%` | `60,000.00` |
| `Live` | `Long` | `0.0174` | 16,710,000.00 USD | 0.00 USD | 1,030.00 USD | `-77.05%` | `59,317.00` |
| `Live` | `Long` | `0.0181` | 16,710,000.00 USD | 0.00 USD | 1,360.00 USD | `-75.99%` | `75,012.00` |
| `Live` | `Long` | `0.0198` | 16,710,000.00 USD | 0.00 USD | 632.00 USD | `-73.87%` | `32,000.00` |
| `Live` | `Long` | `0.0215` | 16,710,000.00 USD | 0.00 USD | 18,970.00 USD | `-71.49%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,690,000.00 USD | 0.00 USD | 541.25 USD | `-71.36%` | `25,000.00` |
| `Live` | `Long` | `0.0217` | 16,690,000.00 USD | 0.00 USD | 131.61 USD | `-71.23%` | `6,051.00` |
| `Live` | `Long` | `0.0222` | 16,690,000.00 USD | 0.00 USD | 33,260.00 USD | `-70.57%` | `1,495,055.00` |
| `Live` | `Long` | `0.0230` | 16,660,000.00 USD | 0.00 USD | 896.17 USD | `-69.64%` | `39,049.00` |
| `Live` | `Long` | `0.0232` | 16,660,000.00 USD | 0.00 USD | 367.23 USD | `-69.24%` | `15,795.00` |
| `Live` | `Long` | `0.0240` | 16,660,000.00 USD | 0.00 USD | 21,490.00 USD | `-68.18%` | `893,720.00` |
| `Live` | `Long` | `0.0244` | 16,630,000.00 USD | 0.00 USD | 12,220.00 USD | `-67.65%` | `500,000.00` |
| `Live` | `Long` | `0.0253` | 16,620,000.00 USD | 0.00 USD | 4,000.00 USD | `-66.60%` | `158,606.00` |
| `Live` | `Long` | `0.0255` | 16,620,000.00 USD | 0.00 USD | 393.38 USD | `-66.33%` | `15,457.00` |
| `Live` | `Long` | `0.0261` | 16,620,000.00 USD | 0.00 USD | 523.00 USD | `-65.41%` | `20,000.00` |
| `Live` | `Long` | `0.0276` | 16,620,000.00 USD | 0.00 USD | 147.23 USD | `-63.55%` | `5,344.00` |
| `Live` | `Long` | `0.0279` | 16,620,000.00 USD | 0.00 USD | 1,730.00 USD | `-63.02%` | `61,775.00` |
| `Live` | `Long` | `0.0283` | 16,610,000.00 USD | 0.00 USD | 912.42 USD | `-62.63%` | `32,298.00` |
| `Live` | `Long` | `0.0294` | 16,610,000.00 USD | 0.00 USD | 506.67 USD | `-61.17%` | `17,263.00` |
| `Live` | `Long` | `0.0300` | 16,610,000.00 USD | 0.00 USD | 1,120.00 USD | `-60.38%` | `37,344.00` |
| `Live` | `Long` | `0.0306` | 16,610,000.00 USD | 0.00 USD | 137.41 USD | `-59.59%` | `4,498.00` |
| `Live` | `Long` | `0.0307` | 16,610,000.00 USD | 0.00 USD | 265.80 USD | `-59.32%` | `8,644.00` |
| `Live` | `Long` | `0.0316` | 16,610,000.00 USD | 0.00 USD | 5,950.00 USD | `-58.13%` | `187,979.00` |
| `Live` | `Long` | `0.0326` | 16,610,000.00 USD | 0.00 USD | 458.31 USD | `-56.81%` | `14,037.00` |
| `Live` | `Long` | `0.0330` | 16,610,000.00 USD | 0.00 USD | 757.85 USD | `-56.41%` | `23,000.00` |
| `Live` | `Long` | `0.0336` | 16,600,000.00 USD | 0.00 USD | 393.23 USD | `-55.48%` | `11,686.00` |
| `Live` | `Long` | `0.0341` | 16,600,000.00 USD | 0.00 USD | 4,590.00 USD | `-54.82%` | `134,443.00` |
| `Live` | `Long` | `0.0350` | 16,600,000.00 USD | 0.00 USD | 13,620.00 USD | `-53.76%` | `389,633.00` |
| `Live` | `Long` | `0.0358` | 16,590,000.00 USD | 0.00 USD | 214.53 USD | `-52.57%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,590,000.00 USD | 0.00 USD | 8,390.00 USD | `-52.44%` | `233,408.00` |
| `Live` | `Long` | `0.0367` | 16,580,000.00 USD | 0.00 USD | 34,820.00 USD | `-51.52%` | `950,000.00` |
| `Live` | `Long` | `0.0377` | 16,540,000.00 USD | 0.00 USD | 170.44 USD | `-50.06%` | `4,515.00` |
| `Live` | `Long` | `0.0379` | 16,540,000.00 USD | 0.00 USD | 3,790.00 USD | `-49.93%` | `100,000.00` |
| `Live` | `Long` | `0.0381` | 16,540,000.00 USD | 0.00 USD | 1,600.00 USD | `-49.66%` | `41,929.00` |
| `Live` | `Long` | `0.0382` | 16,540,000.00 USD | 0.00 USD | 179.78 USD | `-49.40%` | `4,700.00` |
| `Live` | `Long` | `0.0384` | 16,540,000.00 USD | 0.00 USD | 156.30 USD | `-49.13%` | `4,065.00` |
| `Live` | `Long` | `0.0386` | 16,540,000.00 USD | 0.00 USD | 2,160.00 USD | `-49.00%` | `56,008.00` |
| `Live` | `Long` | `0.0393` | 16,530,000.00 USD | 0.00 USD | 2,180.00 USD | `-48.08%` | `55,633.00` |
| `Live` | `Long` | `0.0399` | 16,530,000.00 USD | 0.00 USD | 103.31 USD | `-47.15%` | `2,586.00` |
| `Live` | `Long` | `0.0403` | 16,530,000.00 USD | 0.00 USD | 77,960.00 USD | `-46.62%` | `1,932,139.00` |
| `Live` | `Long` | `0.0404` | 16,450,000.00 USD | 0.00 USD | 115.12 USD | `-46.49%` | `2,846.00` |
| `Live` | `Long` | `0.0408` | 16,450,000.00 USD | 0.00 USD | 5,400.00 USD | `-46.09%` | `132,595.00` |
| `Live` | `Long` | `0.0415` | 16,450,000.00 USD | 0.00 USD | 6,130.00 USD | `-45.17%` | `147,817.00` |
| `Live` | `Long` | `0.0415` | 16,440,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.03%` | `24,809.00` |
| `Live` | `Long` | `0.0418` | 16,440,000.00 USD | 0.00 USD | 100.19 USD | `-44.64%` | `2,394.00` |
| `Live` | `Long` | `0.0420` | 16,440,000.00 USD | 0.00 USD | 43,500.00 USD | `-44.50%` | `1,036,909.00` |
| `Live` | `Long` | `0.0423` | 16,400,000.00 USD | 0.00 USD | 1,670.00 USD | `-44.11%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,400,000.00 USD | 0.00 USD | 267.52 USD | `-43.97%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,400,000.00 USD | 0.00 USD | 455.06 USD | `-43.84%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,400,000.00 USD | 0.00 USD | 883.34 USD | `-43.71%` | `20,760.00` |
| `Live` | `Long` | `0.0427` | 16,390,000.00 USD | 0.00 USD | 2,960.00 USD | `-43.58%` | `69,502.00` |
| `Live` | `Long` | `0.0428` | 16,390,000.00 USD | 0.00 USD | 948.23 USD | `-43.31%` | `22,129.00` |
| `Live` | `Long` | `0.0430` | 16,390,000.00 USD | 0.00 USD | 5,770.00 USD | `-43.18%` | `134,259.00` |
| `Live` | `Long` | `0.0432` | 16,390,000.00 USD | 0.00 USD | 111,720.00 USD | `-42.92%` | `2,589,112.00` |
| `Live` | `Long` | `0.0432` | 16,270,000.00 USD | 0.00 USD | 10,120.00 USD | `-42.78%` | `233,977.00` |
| `Live` | `Long` | `0.0433` | 16,260,000.00 USD | 0.00 USD | 2,450.00 USD | `-42.65%` | `56,456.00` |
| `Live` | `Long` | `0.0437` | 16,260,000.00 USD | 0.00 USD | 12,810.00 USD | `-42.26%` | `293,424.00` |
| `Live` | `Long` | `0.0439` | 16,250,000.00 USD | 0.00 USD | 2,620.00 USD | `-41.99%` | `59,668.00` |
| `Live` | `Long` | `0.0440` | 16,250,000.00 USD | 0.00 USD | 750.58 USD | `-41.86%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,240,000.00 USD | 0.00 USD | 1,060.00 USD | `-41.73%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 16,240,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.33%` | `2,287,370.00` |
| `Live` | `Long` | `0.0445` | 16,140,000.00 USD | 0.00 USD | 1,640.00 USD | `-41.20%` | `36,976.00` |
| `Live` | `Long` | `0.0447` | 16,140,000.00 USD | 0.00 USD | 444.76 USD | `-40.93%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 16,140,000.00 USD | 0.00 USD | 681.05 USD | `-40.80%` | `15,219.00` |
| `Live` | `Long` | `0.0449` | 16,140,000.00 USD | 0.00 USD | 810.81 USD | `-40.54%` | `18,038.00` |
| `Live` | `Long` | `0.0454` | 16,140,000.00 USD | 0.00 USD | 2,170.00 USD | `-39.87%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 16,140,000.00 USD | 0.00 USD | 32,650.00 USD | `-39.74%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 16,100,000.00 USD | 0.00 USD | 1,240.00 USD | `-39.61%` | `27,061.00` |
| `Live` | `Long` | `0.0457` | 16,100,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.48%` | `119,571.00` |
| `Live` | `Long` | `0.0459` | 16,100,000.00 USD | 0.00 USD | 689.25 USD | `-39.21%` | `15,000.00` |
| `Live` | `Long` | `0.0461` | 16,100,000.00 USD | 0.00 USD | 5,680.00 USD | `-39.08%` | `123,396.00` |
| `Live` | `Long` | `0.0461` | 16,090,000.00 USD | 0.00 USD | 114.36 USD | `-38.95%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 16,090,000.00 USD | 0.00 USD | 362.87 USD | `-38.68%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 16,090,000.00 USD | 0.00 USD | 16,780.00 USD | `-38.55%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 16,070,000.00 USD | 0.00 USD | 10,460.00 USD | `-38.42%` | `224,650.00` |
| `Live` | `Long` | `0.0466` | 16,060,000.00 USD | 0.00 USD | 109.49 USD | `-38.29%` | `2,347.00` |
| `Live` | `Long` | `0.0469` | 16,060,000.00 USD | 0.00 USD | 96,820.00 USD | `-38.02%` | `2,066,606.00` |
| `Live` | `Long` | `0.0471` | 15,970,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-37.62%` | `21,424,497.00` |
| `Live` | `Long` | `0.0473` | 14,960,000.00 USD | 0.00 USD | 1,600.00 USD | `-37.49%` | `33,899.00` |
| `Live` | `Long` | `0.0474` | 14,950,000.00 USD | 0.00 USD | 1,420.00 USD | `-37.36%` | `29,884.00` |
| `Live` | `Long` | `0.0474` | 14,950,000.00 USD | 0.00 USD | 39,340.00 USD | `-37.23%` | `829,067.00` |
| `Live` | `Long` | `0.0476` | 14,910,000.00 USD | 0.00 USD | 105.02 USD | `-36.96%` | `2,204.00` |
| `Live` | `Long` | `0.0478` | 14,910,000.00 USD | 0.00 USD | 258.87 USD | `-36.70%` | `5,410.00` |
| `Live` | `Long` | `0.0479` | 14,910,000.00 USD | 0.00 USD | 2,400.00 USD | `-36.57%` | `50,080.00` |
| `Live` | `Long` | `0.0481` | 14,910,000.00 USD | 0.00 USD | 58,890.00 USD | `-36.30%` | `1,223,127.00` |
| `Live` | `Long` | `0.0483` | 14,850,000.00 USD | 0.00 USD | 1,780.00 USD | `-36.04%` | `36,742.00` |
| `Live` | `Long` | `0.0485` | 14,850,000.00 USD | 0.00 USD | 2,780.00 USD | `-35.91%` | `57,433.00` |
| `Live` | `Long` | `0.0488` | 14,850,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.38%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,850,000.00 USD | 0.00 USD | 5,470.00 USD | `-35.24%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,840,000.00 USD | 0.00 USD | 1,080.00 USD | `-35.11%` | `21,989.00` |
| `Live` | `Long` | `0.0495` | 14,840,000.00 USD | 0.00 USD | 5,180.00 USD | `-34.58%` | `104,808.00` |
| `Live` | `Long` | `0.0498` | 14,830,000.00 USD | 0.00 USD | 253.82 USD | `-34.19%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,830,000.00 USD | 0.00 USD | 501.50 USD | `-33.79%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,830,000.00 USD | 0.00 USD | 106.23 USD | `-33.52%` | `2,114.00` |
| `Live` | `Long` | `0.0503` | 14,830,000.00 USD | 0.00 USD | 5,310.00 USD | `-33.39%` | `105,458.00` |
| `Live` | `Long` | `0.0505` | 14,830,000.00 USD | 0.00 USD | 334.89 USD | `-33.26%` | `6,638.00` |
| `Live` | `Long` | `0.0505` | 14,830,000.00 USD | 0.00 USD | 3,760.00 USD | `-33.13%` | `74,309.00` |
| `Live` | `Long` | `0.0507` | 14,820,000.00 USD | 0.00 USD | 1,040.00 USD | `-32.99%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,820,000.00 USD | 0.00 USD | 5,350.00 USD | `-32.86%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,820,000.00 USD | 0.00 USD | 535.43 USD | `-32.60%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,820,000.00 USD | 0.00 USD | 566.65 USD | `-32.47%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,820,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.33%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,810,000.00 USD | 0.00 USD | 1,490.00 USD | `-32.20%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 14,800,000.00 USD | 0.00 USD | 256.75 USD | `-32.07%` | `5,000.00` |
| `Live` | `Long` | `0.0515` | 14,800,000.00 USD | 0.00 USD | 991.41 USD | `-31.80%` | `19,232.00` |
| `Live` | `Long` | `0.0517` | 14,800,000.00 USD | 0.00 USD | 396.47 USD | `-31.67%` | `7,676.00` |
| `Live` | `Long` | `0.0519` | 14,800,000.00 USD | 0.00 USD | 33,640.00 USD | `-31.41%` | `648,741.00` |
| `Live` | `Long` | `0.0520` | 14,770,000.00 USD | 0.00 USD | 277.72 USD | `-31.27%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,770,000.00 USD | 0.00 USD | 4,420.00 USD | `-31.14%` | `84,852.00` |
| `Live` | `Long` | `0.0522` | 14,760,000.00 USD | 0.00 USD | 4,690.00 USD | `-31.01%` | `90,000.00` |
| `Live` | `Long` | `0.0522` | 14,760,000.00 USD | 0.00 USD | 279,570.00 USD | `-30.88%` | `5,350,591.00` |
| `Live` | `Long` | `0.0524` | 14,480,000.00 USD | 0.00 USD | 1,210.00 USD | `-30.75%` | `23,207.00` |
| `Live` | `Long` | `0.0524` | 14,480,000.00 USD | 0.00 USD | 1,170.00 USD | `-30.61%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,480,000.00 USD | 0.00 USD | 5,430.00 USD | `-30.48%` | `103,246.00` |
| `Live` | `Long` | `0.0527` | 14,470,000.00 USD | 0.00 USD | 852.09 USD | `-30.35%` | `16,184.00` |
| `Live` | `Long` | `0.0527` | 14,470,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.22%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,470,000.00 USD | 0.00 USD | 673.52 USD | `-30.08%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,470,000.00 USD | 0.00 USD | 182,040.00 USD | `-29.95%` | `3,437,948.00` |
| `Live` | `Long` | `0.0532` | 14,290,000.00 USD | 0.00 USD | 9,840.00 USD | `-29.69%` | `185,175.00` |
| `Live` | `Long` | `0.0532` | 14,280,000.00 USD | 0.00 USD | 8,100.00 USD | `-29.56%` | `152,035.00` |
| `Live` | `Long` | `0.0534` | 14,270,000.00 USD | 0.00 USD | 42,580.00 USD | `-29.42%` | `798,082.00` |
| `Live` | `Long` | `0.0534` | 14,230,000.00 USD | 0.00 USD | 930.83 USD | `-29.29%` | `17,415.00` |
| `Live` | `Long` | `0.0536` | 14,220,000.00 USD | 0.00 USD | 1,040.00 USD | `-29.16%` | `19,489.00` |
| `Live` | `Long` | `0.0537` | 14,220,000.00 USD | 0.00 USD | 45,370.00 USD | `-29.03%` | `845,726.00` |
| `Live` | `Long` | `0.0537` | 14,180,000.00 USD | 0.00 USD | 425.43 USD | `-28.89%` | `7,915.00` |
| `Live` | `Long` | `0.0539` | 14,180,000.00 USD | 0.00 USD | 28,760.00 USD | `-28.63%` | `533,005.00` |
| `Live` | `Long` | `0.0541` | 14,150,000.00 USD | 0.00 USD | 2,290.00 USD | `-28.50%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 14,150,000.00 USD | 0.00 USD | 3,030.00 USD | `-28.36%` | `55,906.00` |
| `Live` | `Long` | `0.0542` | 14,140,000.00 USD | 0.00 USD | 95,630.00 USD | `-28.23%` | `1,762,722.00` |
| `Live` | `Long` | `0.0544` | 14,050,000.00 USD | 0.00 USD | 903.30 USD | `-28.10%` | `16,620.00` |
| `Live` | `Long` | `0.0546` | 14,050,000.00 USD | 0.00 USD | 3,230.00 USD | `-27.70%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 14,040,000.00 USD | 0.00 USD | 3,250.00 USD | `-27.57%` | `59,376.00` |
| `Live` | `Long` | `0.0549` | 14,040,000.00 USD | 0.00 USD | 344.18 USD | `-27.44%` | `6,275.00` |
| `Live` | `Long` | `0.0551` | 14,040,000.00 USD | 0.00 USD | 1,760.00 USD | `-27.04%` | `31,888.00` |
| `Live` | `Long` | `0.0554` | 14,040,000.00 USD | 0.00 USD | 4,000.00 USD | `-26.64%` | `72,076.00` |
| `Live` | `Long` | `0.0556` | 14,030,000.00 USD | 0.00 USD | 1,100.00 USD | `-26.51%` | `19,864.00` |
| `Live` | `Long` | `0.0561` | 14,030,000.00 USD | 0.00 USD | 8,410.00 USD | `-25.85%` | `150,077.00` |
| `Live` | `Long` | `0.0561` | 14,030,000.00 USD | 0.00 USD | 144.08 USD | `-25.72%` | `2,566.00` |
| `Live` | `Long` | `0.0563` | 14,030,000.00 USD | 0.00 USD | 40,620.00 USD | `-25.59%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,980,000.00 USD | 0.00 USD | 351.85 USD | `-25.45%` | `6,244.00` |
| `Live` | `Long` | `0.0568` | 13,980,000.00 USD | 0.00 USD | 568.50 USD | `-24.79%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,980,000.00 USD | 0.00 USD | 315.67 USD | `-24.66%` | `5,543.00` |
| `Live` | `Long` | `0.0570` | 13,980,000.00 USD | 0.00 USD | 8,350.00 USD | `-24.53%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,970,000.00 USD | 0.00 USD | 1,290.00 USD | `-24.40%` | `22,573.00` |
| `Live` | `Long` | `0.0573` | 13,970,000.00 USD | 0.00 USD | 4,060.00 USD | `-24.13%` | `70,727.00` |
| `Live` | `Long` | `0.0575` | 13,970,000.00 USD | 0.00 USD | 3,960.00 USD | `-23.87%` | `68,830.00` |
| `Live` | `Long` | `0.0576` | 13,970,000.00 USD | 0.00 USD | 10,600.00 USD | `-23.73%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,950,000.00 USD | 0.00 USD | 14,210.00 USD | `-23.60%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,940,000.00 USD | 0.00 USD | 4,310.00 USD | `-23.47%` | `74,438.00` |
| `Live` | `Long` | `0.0580` | 13,940,000.00 USD | 0.00 USD | 441.75 USD | `-23.34%` | `7,623.00` |
| `Live` | `Long` | `0.0580` | 13,940,000.00 USD | 0.00 USD | 4,130.00 USD | `-23.21%` | `71,200.00` |
| `Live` | `Long` | `0.0582` | 13,930,000.00 USD | 0.00 USD | 447.17 USD | `-23.07%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,930,000.00 USD | 0.00 USD | 582.50 USD | `-22.94%` | `10,000.00` |
| `Live` | `Long` | `0.0583` | 13,930,000.00 USD | 0.00 USD | 16,730.00 USD | `-22.81%` | `286,750.00` |
| `Live` | `Long` | `0.0585` | 13,910,000.00 USD | 0.00 USD | 172.78 USD | `-22.54%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,910,000.00 USD | 0.00 USD | 305.15 USD | `-22.28%` | `5,194.00` |
| `Live` | `Long` | `0.0590` | 13,910,000.00 USD | 0.00 USD | 398.74 USD | `-22.01%` | `6,764.00` |
| `Live` | `Long` | `0.0592` | 13,910,000.00 USD | 0.00 USD | 26,980.00 USD | `-21.75%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,890,000.00 USD | 0.00 USD | 546.26 USD | `-21.49%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,890,000.00 USD | 0.00 USD | 4,140.00 USD | `-21.35%` | `69,573.00` |
| `Live` | `Long` | `0.0595` | 13,880,000.00 USD | 0.00 USD | 3,300.00 USD | `-21.22%` | `55,392.00` |
| `Live` | `Long` | `0.0597` | 13,880,000.00 USD | 0.00 USD | 644.22 USD | `-20.96%` | `10,782.00` |
| `Live` | `Long` | `0.0599` | 13,880,000.00 USD | 0.00 USD | 2,110.00 USD | `-20.82%` | `35,297.00` |
| `Live` | `Long` | `0.0600` | 13,880,000.00 USD | 0.00 USD | 360,940.00 USD | `-20.69%` | `6,020,720.00` |
| `Live` | `Long` | `0.0600` | 13,510,000.00 USD | 0.00 USD | 7,210.00 USD | `-20.56%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 13,510,000.00 USD | 0.00 USD | 8,490.00 USD | `-20.43%` | `141,093.00` |
| `Live` | `Long` | `0.0602` | 13,500,000.00 USD | 0.00 USD | 845.25 USD | `-20.29%` | `14,029.00` |
| `Live` | `Long` | `0.0604` | 13,500,000.00 USD | 0.00 USD | 5,960,000.00 USD | `-20.16%` | `98,707,875.00` |
| `Live` | `Long` | `0.0605` | 7,540,000.00 USD | 0.00 USD | 32,090.00 USD | `-19.90%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,510,000.00 USD | 0.00 USD | 622.63 USD | `-19.77%` | `10,266.00` |
| `Live` | `Long` | `0.0609` | 7,510,000.00 USD | 0.00 USD | 2,350.00 USD | `-19.50%` | `38,583.00` |
| `Live` | `Long` | `0.0609` | 7,510,000.00 USD | 0.00 USD | 8,580.00 USD | `-19.37%` | `140,725.00` |
| `Live` | `Long` | `0.0612` | 7,500,000.00 USD | 0.00 USD | 629.72 USD | `-19.10%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 7,500,000.00 USD | 0.00 USD | 719.81 USD | `-18.97%` | `11,752.00` |
| `Live` | `Long` | `0.0614` | 7,500,000.00 USD | 0.00 USD | 655.16 USD | `-18.84%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,500,000.00 USD | 0.00 USD | 1,890.00 USD | `-18.57%` | `30,770.00` |
| `Live` | `Long` | `0.0617` | 7,490,000.00 USD | 0.00 USD | 28,460.00 USD | `-18.44%` | `461,598.00` |
| `Live` | `Long` | `0.0617` | 7,470,000.00 USD | 0.00 USD | 158.08 USD | `-18.31%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,460,000.00 USD | 0.00 USD | 27,580.00 USD | `-17.91%` | `444,421.00` |
| `Live` | `Long` | `0.0621` | 7,440,000.00 USD | 0.00 USD | 576.69 USD | `-17.78%` | `9,279.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 1,900.00 USD | `-17.52%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,430,000.00 USD | 0.00 USD | 43,420.00 USD | `-17.38%` | `695,308.00` |
| `Live` | `Long` | `0.0625` | 7,390,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-17.25%` | `17,636,448.00` |
| `Live` | `Long` | `0.0626` | 6,290,000.00 USD | 0.00 USD | 870.40 USD | `-17.12%` | `13,893.00` |
| `Live` | `Long` | `0.0628` | 6,290,000.00 USD | 0.00 USD | 461.78 USD | `-16.99%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,290,000.00 USD | 0.00 USD | 6,400.00 USD | `-16.86%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,280,000.00 USD | 0.00 USD | 2,630.00 USD | `-16.59%` | `41,730.00` |
| `Live` | `Long` | `0.0631` | 6,280,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-16.46%` | `20,783,139.00` |
| `Live` | `Long` | `0.0633` | 4,970,000.00 USD | 0.00 USD | 3,030.00 USD | `-16.33%` | `47,852.00` |
| `Live` | `Long` | `0.0634` | 4,960,000.00 USD | 0.00 USD | 12,660.00 USD | `-16.19%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-16.06%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 280.95 USD | `-15.93%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 4,950,000.00 USD | 0.00 USD | 633.38 USD | `-15.80%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 4,950,000.00 USD | 0.00 USD | 9,740.00 USD | `-15.66%` | `152,837.00` |
| `Live` | `Long` | `0.0639` | 4,940,000.00 USD | 0.00 USD | 23,220.00 USD | `-15.53%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 1,990.00 USD | `-15.40%` | `31,194.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 150.01 USD | `-15.27%` | `2,342.00` |
| `Live` | `Long` | `0.0641` | 4,910,000.00 USD | 0.00 USD | 3,270.00 USD | `-15.14%` | `50,913.00` |
| `Live` | `Long` | `0.0643` | 4,910,000.00 USD | 0.00 USD | 1,330.00 USD | `-15.00%` | `20,766.00` |
| `Live` | `Long` | `0.0644` | 4,910,000.00 USD | 0.00 USD | 76,280.00 USD | `-14.87%` | `1,185,416.00` |
| `Live` | `Long` | `0.0644` | 4,830,000.00 USD | 0.00 USD | 27,180.00 USD | `-14.74%` | `421,717.00` |
| `Live` | `Long` | `0.0645` | 4,800,000.00 USD | 0.00 USD | 631.94 USD | `-14.61%` | `9,790.00` |
| `Live` | `Long` | `0.0646` | 4,800,000.00 USD | 0.00 USD | 1,230.00 USD | `-14.47%` | `19,086.00` |
| `Live` | `Long` | `0.0648` | 4,800,000.00 USD | 0.00 USD | 162,920.00 USD | `-14.34%` | `2,516,210.00` |
| `Live` | `Long` | `0.0649` | 4,640,000.00 USD | 0.00 USD | 8,800.00 USD | `-14.21%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,630,000.00 USD | 0.00 USD | 21,910.00 USD | `-14.08%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 4,610,000.00 USD | 0.00 USD | 2,380.00 USD | `-13.81%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,610,000.00 USD | 0.00 USD | 13,770.00 USD | `-13.68%` | `210,965.00` |
| `Live` | `Long` | `0.0655` | 4,590,000.00 USD | 0.00 USD | 7,790.00 USD | `-13.28%` | `118,852.00` |
| `Live` | `Long` | `0.0657` | 4,580,000.00 USD | 0.00 USD | 14,160.00 USD | `-13.15%` | `215,665.00` |
| `Live` | `Long` | `0.0658` | 4,570,000.00 USD | 0.00 USD | 66,820.00 USD | `-13.02%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,500,000.00 USD | 0.00 USD | 14,600.00 USD | `-12.89%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,490,000.00 USD | 0.00 USD | 9,600.00 USD | `-12.75%` | `145,525.00` |
| `Live` | `Long` | `0.0662` | 4,480,000.00 USD | 0.00 USD | 2,280.00 USD | `-12.49%` | `34,474.00` |
| `Live` | `Long` | `0.0663` | 4,480,000.00 USD | 0.00 USD | 1,630.00 USD | `-12.36%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,480,000.00 USD | 0.00 USD | 17,410.00 USD | `-12.23%` | `262,335.00` |
| `Live` | `Long` | `0.0664` | 4,460,000.00 USD | 0.00 USD | 1,270.00 USD | `-12.09%` | `19,149.00` |
| `Live` | `Long` | `0.0665` | 4,460,000.00 USD | 0.00 USD | 9,240.00 USD | `-11.96%` | `138,864.00` |
| `Live` | `Long` | `0.0667` | 4,450,000.00 USD | 0.00 USD | 34,860.00 USD | `-11.83%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,410,000.00 USD | 0.00 USD | 8,880.00 USD | `-11.70%` | `133,009.00` |
| `Live` | `Long` | `0.0669` | 4,400,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-11.56%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,260,000.00 USD | 0.00 USD | 3,990.00 USD | `-11.43%` | `59,653.00` |
| `Live` | `Long` | `0.0670` | 3,250,000.00 USD | 0.00 USD | 9,050.00 USD | `-11.30%` | `134,979.00` |
| `Live` | `Long` | `0.0673` | 3,240,000.00 USD | 0.00 USD | 9,220.00 USD | `-11.03%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,240,000.00 USD | 0.00 USD | 4,830.00 USD | `-10.90%` | `71,711.00` |
| `Live` | `Long` | `0.0674` | 3,230,000.00 USD | 0.00 USD | 2,050.00 USD | `-10.77%` | `30,427.00` |
| `Live` | `Long` | `0.0675` | 3,230,000.00 USD | 0.00 USD | 112,780.00 USD | `-10.64%` | `1,669,510.00` |
| `Live` | `Long` | `0.0677` | 3,120,000.00 USD | 0.00 USD | 12,610.00 USD | `-10.51%` | `186,370.00` |
| `Live` | `Long` | `0.0678` | 3,100,000.00 USD | 0.00 USD | 4,290.00 USD | `-10.37%` | `63,374.00` |
| `Live` | `Long` | `0.0678` | 3,100,000.00 USD | 0.00 USD | 34,090.00 USD | `-10.24%` | `502,486.00` |
| `Live` | `Long` | `0.0679` | 3,060,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.11%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,050,000.00 USD | 0.00 USD | 10,960.00 USD | `-9.98%` | `161,086.00` |
| `Live` | `Long` | `0.0683` | 3,040,000.00 USD | 0.00 USD | 55,770.00 USD | `-9.71%` | `817,124.00` |
| `Live` | `Long` | `0.0684` | 2,980,000.00 USD | 0.00 USD | 113,760.00 USD | `-9.45%` | `1,661,946.00` |
| `Live` | `Long` | `0.0685` | 2,870,000.00 USD | 0.00 USD | 8,890.00 USD | `-9.31%` | `129,646.00` |
| `Live` | `Long` | `0.0687` | 2,860,000.00 USD | 0.00 USD | 4,840.00 USD | `-9.18%` | `70,447.00` |
| `Live` | `Long` | `0.0688` | 2,850,000.00 USD | 0.00 USD | 16,210.00 USD | `-9.05%` | `235,726.00` |
| `Live` | `Long` | `0.0688` | 2,840,000.00 USD | 0.00 USD | 345.83 USD | `-8.92%` | `5,023.00` |
| `Live` | `Long` | `0.0689` | 2,840,000.00 USD | 0.00 USD | 508,320.00 USD | `-8.79%` | `7,372,312.00` |
| `Live` | `Long` | `0.0691` | 2,330,000.00 USD | 0.00 USD | 6,960.00 USD | `-8.65%` | `100,756.00` |
| `Live` | `Long` | `0.0692` | 2,320,000.00 USD | 0.00 USD | 26,150.00 USD | `-8.52%` | `378,182.00` |
| `Live` | `Long` | `0.0693` | 2,300,000.00 USD | 0.00 USD | 10,100.00 USD | `-8.39%` | `145,853.00` |
| `Live` | `Long` | `0.0693` | 2,290,000.00 USD | 0.00 USD | 2,020.00 USD | `-8.26%` | `29,107.00` |
| `Live` | `Long` | `0.0694` | 2,280,000.00 USD | 0.00 USD | 8,070.00 USD | `-8.12%` | `116,243.00` |
| `Live` | `Long` | `0.0697` | 2,280,000.00 USD | 0.00 USD | 4,950.00 USD | `-7.86%` | `71,115.00` |
| `Live` | `Long` | `0.0698` | 2,270,000.00 USD | 0.00 USD | 6,970.00 USD | `-7.73%` | `99,923.00` |
| `Live` | `Long` | `0.0698` | 2,260,000.00 USD | 0.00 USD | 2,910.00 USD | `-7.59%` | `41,684.00` |
| `Live` | `Long` | `0.0699` | 2,260,000.00 USD | 0.00 USD | 1,310.00 USD | `-7.46%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,260,000.00 USD | 0.00 USD | 9,620.00 USD | `-7.33%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,250,000.00 USD | 0.00 USD | 8,310.00 USD | `-7.20%` | `118,427.00` |
| `Live` | `Long` | `0.0703` | 2,240,000.00 USD | 0.00 USD | 1,070.00 USD | `-7.07%` | `15,205.00` |
| `Live` | `Long` | `0.0703` | 2,240,000.00 USD | 0.00 USD | 3,790.00 USD | `-6.93%` | `53,920.00` |
| `Live` | `Long` | `0.0704` | 2,240,000.00 USD | 0.00 USD | 780.37 USD | `-6.80%` | `11,077.00` |
| `Live` | `Long` | `0.0707` | 2,240,000.00 USD | 0.00 USD | 608.86 USD | `-6.54%` | `8,618.00` |
| `Live` | `Long` | `0.0707` | 2,240,000.00 USD | 0.00 USD | 94,410.00 USD | `-6.40%` | `1,334,448.00` |
| `Live` | `Long` | `0.0709` | 2,140,000.00 USD | 0.00 USD | 821.60 USD | `-6.14%` | `11,580.00` |
| `Live` | `Long` | `0.0711` | 2,140,000.00 USD | 0.00 USD | 4,720.00 USD | `-6.01%` | `66,436.00` |
| `Live` | `Long` | `0.0712` | 2,140,000.00 USD | 0.00 USD | 1,860.00 USD | `-5.88%` | `26,118.00` |
| `Live` | `Long` | `0.0712` | 2,130,000.00 USD | 0.00 USD | 802.06 USD | `-5.74%` | `11,257.00` |
| `Live` | `Long` | `0.0713` | 2,130,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-5.61%` | `24,500,580.00` |
| `Live` | `Long` | `0.0714` | 384,450.00 USD | 0.00 USD | 13,270.00 USD | `-5.48%` | `185,735.00` |
| `Live` | `Long` | `0.0716` | 371,180.00 USD | 0.00 USD | 8,120.00 USD | `-5.35%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 363,060.00 USD | 0.00 USD | 3,840.00 USD | `-5.21%` | `53,537.00` |
| `Live` | `Long` | `0.0717` | 359,230.00 USD | 0.00 USD | 22,070.00 USD | `-5.08%` | `307,537.00` |
| `Live` | `Long` | `0.0718` | 337,160.00 USD | 0.00 USD | 960.13 USD | `-4.95%` | `13,363.00` |
| `Live` | `Long` | `0.0720` | 336,200.00 USD | 0.00 USD | 5,880.00 USD | `-4.82%` | `81,672.00` |
| `Live` | `Long` | `0.0721` | 330,320.00 USD | 0.00 USD | 4,750.00 USD | `-4.68%` | `65,881.00` |
| `Live` | `Long` | `0.0722` | 325,580.00 USD | 0.00 USD | 758.08 USD | `-4.55%` | `10,507.00` |
| `Live` | `Long` | `0.0722` | 324,820.00 USD | 0.00 USD | 38,340.00 USD | `-4.42%` | `530,618.00` |
| `Live` | `Long` | `0.0723` | 286,480.00 USD | 0.00 USD | 285,380.00 USD | `-4.29%` | `3,944,458.00` |
| `Live` | `Long` | `0.0725` | 1,100.00 USD | 0.00 USD | 984.89 USD | `-4.16%` | `13,594.00` |
| `Live` | `Long` | `0.0727` | 115.51 USD | 0.00 USD | 115.51 USD | `-3.89%` | `1,590.00` |
| `Live` | `Short` | `0.0775` | 373.31 USD | 373.31 USD | 0.00 USD | `+2.46%` | `4,820.00` |
| `Live` | `Short` | `0.0775` | 614.26 USD | 240.95 USD | 0.00 USD | `+2.59%` | `3,107.00` |
| `Live` | `Short` | `0.0785` | 9,840.00 USD | 9,220.00 USD | 0.00 USD | `+3.91%` | `117,432.00` |
| `Live` | `Short` | `0.0788` | 9,950.00 USD | 113.24 USD | 0.00 USD | `+4.18%` | `1,438.00` |
| `Live` | `Short` | `0.0795` | 10,060.00 USD | 104.72 USD | 0.00 USD | `+5.11%` | `1,318.00` |
| `Live` | `Short` | `0.0796` | 10,380.00 USD | 326.09 USD | 0.00 USD | `+5.37%` | `4,094.00` |
| `Live` | `Short` | `0.0803` | 10,700.00 USD | 314.26 USD | 0.00 USD | `+6.16%` | `3,916.00` |
| `Live` | `Short` | `0.0804` | 11,520.00 USD | 826.14 USD | 0.00 USD | `+6.43%` | `10,269.00` |
| `Live` | `Short` | `0.0819` | 11,900.00 USD | 380.85 USD | 0.00 USD | `+8.28%` | `4,653.00` |
| `Live` | `Short` | `0.0828` | 12,020.00 USD | 120.96 USD | 0.00 USD | `+9.60%` | `1,460.00` |
| `Live` | `Short` | `0.0832` | 15,480.00 USD | 3,450.00 USD | 0.00 USD | `+10.00%` | `41,543.00` |
| `Live` | `Short` | `0.0833` | 15,980.00 USD | 500.17 USD | 0.00 USD | `+10.13%` | `6,008.00` |
| `Live` | `Short` | `0.0837` | 16,270.00 USD | 293.44 USD | 0.00 USD | `+10.66%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 17,840.00 USD | 1,570.00 USD | 0.00 USD | `+10.79%` | `18,767.00` |
| `Live` | `Short` | `0.0843` | 18,110.00 USD | 264.21 USD | 0.00 USD | `+11.46%` | `3,136.00` |
| `Live` | `Short` | `0.0848` | 18,540.00 USD | 426.71 USD | 0.00 USD | `+12.25%` | `5,029.00` |
| `Live` | `Short` | `0.0858` | 18,650.00 USD | 115.30 USD | 0.00 USD | `+13.57%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 22,900.00 USD | 4,250.00 USD | 0.00 USD | `+13.70%` | `49,397.00` |
| `Live` | `Short` | `0.0868` | 23,050.00 USD | 155.98 USD | 0.00 USD | `+14.89%` | `1,796.00` |
| `Live` | `Short` | `0.0871` | 23,190.00 USD | 138.58 USD | 0.00 USD | `+15.16%` | `1,592.00` |
| `Live` | `Short` | `0.0881` | 23,660.00 USD | 465.17 USD | 0.00 USD | `+16.48%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 24,070.00 USD | 411.53 USD | 0.00 USD | `+17.41%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 24,490.00 USD | 418.80 USD | 0.00 USD | `+17.81%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 24,770.00 USD | 285.70 USD | 0.00 USD | `+18.33%` | `3,194.00` |
| `Live` | `Short` | `0.0905` | 31,540.00 USD | 6,760.00 USD | 0.00 USD | `+19.66%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 32,840.00 USD | 1,310.00 USD | 0.00 USD | `+19.92%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 37,780.00 USD | 4,940.00 USD | 0.00 USD | `+20.58%` | `54,197.00` |
| `Live` | `Short` | `0.0921` | 37,960.00 USD | 171.49 USD | 0.00 USD | `+21.77%` | `1,863.00` |
| `Live` | `Short` | `0.0931` | 38,760.00 USD | 805.37 USD | 0.00 USD | `+23.23%` | `8,646.00` |
| `Live` | `Short` | `0.0938` | 42,980.00 USD | 4,220.00 USD | 0.00 USD | `+24.02%` | `45,000.00` |
| `Live` | `Short` | `0.0940` | 43,890.00 USD | 914.70 USD | 0.00 USD | `+24.29%` | `9,736.00` |
| `Live` | `Short` | `0.0944` | 83,600.00 USD | 39,700.00 USD | 0.00 USD | `+24.82%` | `420,808.00` |
| `Live` | `Short` | `0.0946` | 83,790.00 USD | 192.61 USD | 0.00 USD | `+25.21%` | `2,035.00` |
| `Live` | `Short` | `0.0950` | 108,250.00 USD | 24,460.00 USD | 0.00 USD | `+25.61%` | `257,659.00` |
| `Live` | `Short` | `0.0950` | 156,540.00 USD | 48,290.00 USD | 0.00 USD | `+25.74%` | `508,009.00` |
| `Live` | `Short` | `0.0961` | 157,150.00 USD | 609.59 USD | 0.00 USD | `+27.20%` | `6,340.00` |
| `Live` | `Short` | `0.0970` | 157,520.00 USD | 365.68 USD | 0.00 USD | `+28.39%` | `3,768.00` |
| `Live` | `Short` | `0.0974` | 157,640.00 USD | 121.23 USD | 0.00 USD | `+28.92%` | `1,244.00` |
| `Live` | `Short` | `0.0983` | 158,110.00 USD | 477.50 USD | 0.00 USD | `+29.98%` | `4,860.00` |
| `Live` | `Short` | `0.1003` | 159,530.00 USD | 1,420.00 USD | 0.00 USD | `+32.75%` | `14,104.00` |
| `Live` | `Short` | `0.1012` | 162,490.00 USD | 2,960.00 USD | 0.00 USD | `+33.81%` | `29,217.00` |
| `Live` | `Short` | `0.1014` | 170,110.00 USD | 7,630.00 USD | 0.00 USD | `+34.21%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 173,080.00 USD | 2,970.00 USD | 0.00 USD | `+34.47%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 173,570.00 USD | 492.85 USD | 0.00 USD | `+34.74%` | `4,839.00` |
| `Live` | `Short` | `0.1061` | 179,680.00 USD | 6,110.00 USD | 0.00 USD | `+40.43%` | `57,554.00` |
| `Live` | `Short` | `0.1062` | 182,980.00 USD | 3,290.00 USD | 0.00 USD | `+40.56%` | `31,000.00` |
| `Live` | `Short` | `0.1076` | 183,590.00 USD | 616.19 USD | 0.00 USD | `+42.41%` | `5,724.00` |
| `Live` | `Short` | `0.1085` | 186,830.00 USD | 3,240.00 USD | 0.00 USD | `+43.60%` | `29,849.00` |
| `Live` | `Short` | `0.1095` | 188,720.00 USD | 1,880.00 USD | 0.00 USD | `+44.92%` | `17,184.00` |
| `Live` | `Short` | `0.1127` | 188,930.00 USD | 214.15 USD | 0.00 USD | `+49.03%` | `1,901.00` |
| `Live` | `Short` | `0.1137` | 189,080.00 USD | 147.86 USD | 0.00 USD | `+50.35%` | `1,301.00` |
| `Live` | `Short` | `0.1152` | 189,220.00 USD | 147.05 USD | 0.00 USD | `+52.33%` | `1,277.00` |
| `Live` | `Short` | `0.1211` | 190,100.00 USD | 874.58 USD | 0.00 USD | `+60.27%` | `7,219.00` |
| `Live` | `Short` | `0.1222` | 190,740.00 USD | 637.53 USD | 0.00 USD | `+61.73%` | `5,215.00` |
| `Live` | `Short` | `0.1231` | 190,860.00 USD | 118.84 USD | 0.00 USD | `+62.92%` | `965.00` |
| `Live` | `Short` | `0.1270` | 190,960.00 USD | 108.80 USD | 0.00 USD | `+67.94%` | `857.00` |
| `Live` | `Short` | `0.1296` | 191,140.00 USD | 171.66 USD | 0.00 USD | `+71.52%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 193,280.00 USD | 2,140.00 USD | 0.00 USD | `+73.50%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 193,380.00 USD | 102.97 USD | 0.00 USD | `+74.43%` | `781.00` |
| `Live` | `Short` | `0.1328` | 238,840.00 USD | 45,470.00 USD | 0.00 USD | `+75.75%` | `342,231.00` |
| `Live` | `Short` | `0.1338` | 239,050.00 USD | 205.31 USD | 0.00 USD | `+76.94%` | `1,535.00` |
| `Live` | `Short` | `0.1368` | 240,200.00 USD | 1,160.00 USD | 0.00 USD | `+80.91%` | `8,450.00` |
| `Live` | `Short` | `0.1404` | 240,870.00 USD | 663.63 USD | 0.00 USD | `+85.80%` | `4,725.00` |
| `Live` | `Short` | `0.1424` | 263,950.00 USD | 23,090.00 USD | 0.00 USD | `+88.32%` | `162,180.00` |
| `Live` | `Short` | `0.1426` | 265,760.00 USD | 1,800.00 USD | 0.00 USD | `+88.58%` | `12,652.00` |
| `Live` | `Short` | `0.1432` | 267,620.00 USD | 1,860.00 USD | 0.00 USD | `+89.51%` | `13,010.00` |
| `Live` | `Short` | `0.1441` | 269,650.00 USD | 2,030.00 USD | 0.00 USD | `+90.57%` | `14,103.00` |
| `Live` | `Short` | `0.1442` | 315,330.00 USD | 45,670.00 USD | 0.00 USD | `+90.70%` | `316,845.00` |
| `Live` | `Short` | `0.1444` | 316,870.00 USD | 1,540.00 USD | 0.00 USD | `+90.96%` | `10,691.00` |
| `Live` | `Short` | `0.1446` | 317,010.00 USD | 144.55 USD | 0.00 USD | `+91.23%` | `1,000.00` |
| `Live` | `Short` | `0.1452` | 318,940.00 USD | 1,920.00 USD | 0.00 USD | `+92.02%` | `13,240.00` |
| `Live` | `Short` | `0.1457` | 320,200.00 USD | 1,270.00 USD | 0.00 USD | `+92.68%` | `8,712.00` |
| `Live` | `Short` | `0.1479` | 328,320.00 USD | 8,110.00 USD | 0.00 USD | `+95.59%` | `54,875.00` |
| `Live` | `Short` | `0.1490` | 3,440,000.00 USD | 3,110,000.00 USD | 0.00 USD | `+97.18%` | `20,845,267.00` |
| `Live` | `Short` | `0.1494` | 3,460,000.00 USD | 24,030.00 USD | 0.00 USD | `+97.71%` | `160,802.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 740,540.00 USD | 0.00 USD | 375.42 USD | `-65.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 740,170.00 USD | 0.00 USD | 409.59 USD | `-47.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 739,760.00 USD | 0.00 USD | 132.68 USD | `-46.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 739,630.00 USD | 0.00 USD | 788.27 USD | `-44.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 738,840.00 USD | 0.00 USD | 527.05 USD | `-44.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 738,310.00 USD | 0.00 USD | 286.87 USD | `-40.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 738,020.00 USD | 0.00 USD | 252.42 USD | `-38.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 737,770.00 USD | 0.00 USD | 468.67 USD | `-37.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 737,300.00 USD | 0.00 USD | 5,160.00 USD | `-35.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 732,140.00 USD | 0.00 USD | 920.48 USD | `-34.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 731,220.00 USD | 0.00 USD | 236.01 USD | `-33.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 730,990.00 USD | 0.00 USD | 175.41 USD | `-32.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 730,810.00 USD | 0.00 USD | 242.96 USD | `-31.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 730,570.00 USD | 0.00 USD | 2,670.00 USD | `-28.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 727,890.00 USD | 0.00 USD | 1,370.00 USD | `-26.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 726,520.00 USD | 0.00 USD | 437.58 USD | `-25.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 726,090.00 USD | 0.00 USD | 183.30 USD | `-22.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 725,900.00 USD | 0.00 USD | 752.54 USD | `-22.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 725,150.00 USD | 0.00 USD | 984.67 USD | `-21.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 724,160.00 USD | 0.00 USD | 668.84 USD | `-20.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 723,500.00 USD | 0.00 USD | 273.90 USD | `-20.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 723,220.00 USD | 0.00 USD | 8,800.00 USD | `-19.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 714,420.00 USD | 0.00 USD | 838.79 USD | `-19.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 713,590.00 USD | 0.00 USD | 218.94 USD | `-19.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 713,370.00 USD | 0.00 USD | 504.26 USD | `-18.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 712,860.00 USD | 0.00 USD | 2,280.00 USD | `-17.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 710,580.00 USD | 0.00 USD | 118.27 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 710,460.00 USD | 0.00 USD | 1,280.00 USD | `-17.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 709,190.00 USD | 0.00 USD | 1,820.00 USD | `-16.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 707,360.00 USD | 0.00 USD | 1,340.00 USD | `-15.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 706,030.00 USD | 0.00 USD | 386.70 USD | `-15.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 705,640.00 USD | 0.00 USD | 644.50 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 705,000.00 USD | 0.00 USD | 11,270.00 USD | `-13.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 693,730.00 USD | 0.00 USD | 362.24 USD | `-13.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 693,360.00 USD | 0.00 USD | 3,140.00 USD | `-13.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 690,220.00 USD | 0.00 USD | 1,100.00 USD | `-13.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 689,130.00 USD | 0.00 USD | 1,200.00 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 687,930.00 USD | 0.00 USD | 996.31 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 686,930.00 USD | 0.00 USD | 909.85 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 686,020.00 USD | 0.00 USD | 115.57 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 685,910.00 USD | 0.00 USD | 33,620.00 USD | `-11.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 652,280.00 USD | 0.00 USD | 12,860.00 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 639,420.00 USD | 0.00 USD | 1,540.00 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 637,880.00 USD | 0.00 USD | 108.08 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 637,770.00 USD | 0.00 USD | 19,540.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 618,230.00 USD | 0.00 USD | 1,430.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 616,800.00 USD | 0.00 USD | 8,540.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 608,260.00 USD | 0.00 USD | 8,580.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 599,690.00 USD | 0.00 USD | 4,970.00 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 594,720.00 USD | 0.00 USD | 3,100.00 USD | `-9.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 591,620.00 USD | 0.00 USD | 160.31 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 591,460.00 USD | 0.00 USD | 38,710.00 USD | `-8.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 552,750.00 USD | 0.00 USD | 21,140.00 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 531,620.00 USD | 0.00 USD | 3,190.00 USD | `-8.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 528,430.00 USD | 0.00 USD | 176.08 USD | `-8.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 528,250.00 USD | 0.00 USD | 142.09 USD | `-8.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 528,110.00 USD | 0.00 USD | 925.29 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 527,180.00 USD | 0.00 USD | 797.80 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 526,390.00 USD | 0.00 USD | 68,440.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 457,950.00 USD | 0.00 USD | 141.77 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 457,800.00 USD | 0.00 USD | 895.27 USD | `-7.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 456,910.00 USD | 0.00 USD | 523.23 USD | `-6.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 456,390.00 USD | 0.00 USD | 468.88 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 455,920.00 USD | 0.00 USD | 235.12 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 455,680.00 USD | 0.00 USD | 1,090.00 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 454,600.00 USD | 0.00 USD | 71,660.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0711` | 382,930.00 USD | 0.00 USD | 729.61 USD | `-6.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 382,210.00 USD | 0.00 USD | 647.04 USD | `-5.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 381,560.00 USD | 0.00 USD | 20,180.00 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 361,380.00 USD | 0.00 USD | 608.76 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 360,770.00 USD | 0.00 USD | 16,880.00 USD | `-5.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 343,890.00 USD | 0.00 USD | 110.12 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 343,780.00 USD | 0.00 USD | 1,880.00 USD | `-5.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 341,900.00 USD | 0.00 USD | 17,760.00 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 324,140.00 USD | 0.00 USD | 13,550.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 310,590.00 USD | 0.00 USD | 551.98 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 310,040.00 USD | 0.00 USD | 138,380.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 171,660.00 USD | 0.00 USD | 1,690.00 USD | `-4.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 169,970.00 USD | 0.00 USD | 34,460.00 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 135,510.00 USD | 0.00 USD | 2,030.00 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 133,480.00 USD | 0.00 USD | 2,340.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 131,140.00 USD | 0.00 USD | 2,540.00 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 128,600.00 USD | 0.00 USD | 4,030.00 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 124,570.00 USD | 0.00 USD | 2,090.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 122,480.00 USD | 0.00 USD | 1,950.00 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 120,530.00 USD | 0.00 USD | 535.16 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 119,990.00 USD | 0.00 USD | 227.92 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 119,760.00 USD | 0.00 USD | 397.76 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 119,360.00 USD | 0.00 USD | 398.00 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 118,970.00 USD | 0.00 USD | 797.39 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 118,170.00 USD | 0.00 USD | 59,430.00 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 58,740.00 USD | 0.00 USD | 1,640.00 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 57,090.00 USD | 0.00 USD | 189.57 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 56,900.00 USD | 0.00 USD | 1,480.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 55,430.00 USD | 0.00 USD | 2,900.00 USD | `-1.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 52,530.00 USD | 0.00 USD | 415.62 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 52,110.00 USD | 0.00 USD | 16,520.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 35,600.00 USD | 0.00 USD | 3,170.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 32,420.00 USD | 0.00 USD | 375.86 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 32,050.00 USD | 0.00 USD | 537.68 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 31,510.00 USD | 0.00 USD | 140.04 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 31,370.00 USD | 0.00 USD | 1,490.00 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 29,880.00 USD | 0.00 USD | 3,450.00 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 26,430.00 USD | 0.00 USD | 16,670.00 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 9,750.00 USD | 0.00 USD | 406.95 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0754` | 9,350.00 USD | 0.00 USD | 1,700.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 7,650.00 USD | 0.00 USD | 151.35 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 7,490.00 USD | 0.00 USD | 7,490.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 150.85 USD | 150.85 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0757` | 1,370.00 USD | 1,210.00 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0759` | 1,870.00 USD | 504.10 USD | 0.00 USD | `+0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0760` | 2,270.00 USD | 398.13 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 2,480.00 USD | 216.21 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 22,720.00 USD | 20,230.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 23,530.00 USD | 814.81 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 27,310.00 USD | 3,770.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 27,420.00 USD | 109.63 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 28,660.00 USD | 1,250.00 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 28,850.00 USD | 183.50 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 29,360.00 USD | 515.15 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 30,320.00 USD | 955.71 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 31,130.00 USD | 816.05 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 31,850.00 USD | 715.18 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 34,180.00 USD | 2,330.00 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 34,420.00 USD | 240.02 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 38,550.00 USD | 4,140.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 38,960.00 USD | 407.23 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 39,280.00 USD | 321.13 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 40,770.00 USD | 1,490.00 USD | 0.00 USD | `+2.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 43,020.00 USD | 2,240.00 USD | 0.00 USD | `+2.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 43,350.00 USD | 329.23 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 43,500.00 USD | 155.43 USD | 0.00 USD | `+3.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 43,690.00 USD | 186.07 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 46,610.00 USD | 2,920.00 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 47,590.00 USD | 975.23 USD | 0.00 USD | `+3.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 48,000.00 USD | 413.84 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 48,160.00 USD | 157.14 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 48,290.00 USD | 130.71 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 89,900.00 USD | 41,610.00 USD | 0.00 USD | `+4.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 90,040.00 USD | 141.44 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 90,810.00 USD | 773.68 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 91,500.00 USD | 687.81 USD | 0.00 USD | `+4.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 96,920.00 USD | 5,420.00 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 98,030.00 USD | 1,110.00 USD | 0.00 USD | `+4.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 103,400.00 USD | 5,370.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 112,730.00 USD | 9,330.00 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 113,040.00 USD | 312.56 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 113,500.00 USD | 455.34 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 113,620.00 USD | 125.45 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 113,860.00 USD | 230.40 USD | 0.00 USD | `+5.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 114,170.00 USD | 319.16 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 115,180.00 USD | 1,010.00 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 137,930.00 USD | 22,750.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 138,330.00 USD | 400.91 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 138,530.00 USD | 200.46 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 138,790.00 USD | 259.13 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 139,500.00 USD | 707.08 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 148,510.00 USD | 9,010.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 245,290.00 USD | 96,780.00 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 246,090.00 USD | 807.50 USD | 0.00 USD | `+6.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 246,350.00 USD | 257.18 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 246,780.00 USD | 424.74 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 246,880.00 USD | 101.80 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 248,260.00 USD | 1,380.00 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 250,290.00 USD | 2,030.00 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 251,720.00 USD | 1,430.00 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 251,850.00 USD | 129.67 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 252,870.00 USD | 1,020.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 253,120.00 USD | 256.05 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 254,150.00 USD | 1,030.00 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 257,170.00 USD | 3,020.00 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 257,500.00 USD | 327.80 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 257,960.00 USD | 457.92 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 258,650.00 USD | 691.29 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 259,450.00 USD | 800.79 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 259,960.00 USD | 512.05 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 260,460.00 USD | 495.36 USD | 0.00 USD | `+9.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 260,850.00 USD | 389.31 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 261,000.00 USD | 154.58 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 261,300.00 USD | 303.56 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 261,420.00 USD | 112.89 USD | 0.00 USD | `+9.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 261,800.00 USD | 381.45 USD | 0.00 USD | `+9.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 261,950.00 USD | 155.82 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 306,340.00 USD | 44,390.00 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 306,650.00 USD | 309.23 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 307,910.00 USD | 1,260.00 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 309,150.00 USD | 1,240.00 USD | 0.00 USD | `+10.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,050,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+10.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,060,000.00 USD | 3,150.00 USD | 0.00 USD | `+10.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,060,000.00 USD | 1,470.00 USD | 0.00 USD | `+11.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,060,000.00 USD | 107.71 USD | 0.00 USD | `+11.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,060,000.00 USD | 2,690.00 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,060,000.00 USD | 529.92 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,060,000.00 USD | 219.07 USD | 0.00 USD | `+11.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,060,000.00 USD | 242.84 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,070,000.00 USD | 10,140.00 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,070,000.00 USD | 876.11 USD | 0.00 USD | `+12.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,080,000.00 USD | 812.54 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,080,000.00 USD | 126.76 USD | 0.00 USD | `+13.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,080,000.00 USD | 307.41 USD | 0.00 USD | `+13.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,080,000.00 USD | 614.09 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,080,000.00 USD | 859.50 USD | 0.00 USD | `+13.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,080,000.00 USD | 2,020.00 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,120,000.00 USD | 43,760.00 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,120,000.00 USD | 123.94 USD | 0.00 USD | `+14.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 2,120,000.00 USD | 271.53 USD | 0.00 USD | `+14.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,120,000.00 USD | 1,660.00 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,130,000.00 USD | 1,840.00 USD | 0.00 USD | `+15.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,130,000.00 USD | 2,760.00 USD | 0.00 USD | `+15.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,130,000.00 USD | 117.71 USD | 0.00 USD | `+15.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,130,000.00 USD | 111.61 USD | 0.00 USD | `+16.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,130,000.00 USD | 571.18 USD | 0.00 USD | `+16.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,130,000.00 USD | 375.94 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,130,000.00 USD | 627.55 USD | 0.00 USD | `+16.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,130,000.00 USD | 211.04 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,130,000.00 USD | 108.36 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,130,000.00 USD | 543.32 USD | 0.00 USD | `+17.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,130,000.00 USD | 1,820.00 USD | 0.00 USD | `+17.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,140,000.00 USD | 2,080.00 USD | 0.00 USD | `+17.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,150,000.00 USD | 17,680.00 USD | 0.00 USD | `+18.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,160,000.00 USD | 1,370.00 USD | 0.00 USD | `+18.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,160,000.00 USD | 5,630.00 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,160,000.00 USD | 1,090.00 USD | 0.00 USD | `+19.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,160,000.00 USD | 224.86 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,180,000.00 USD | 20,540.00 USD | 0.00 USD | `+19.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,180,000.00 USD | 114.93 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,180,000.00 USD | 679.12 USD | 0.00 USD | `+20.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,180,000.00 USD | 173.36 USD | 0.00 USD | `+20.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,190,000.00 USD | 1,810.00 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,190,000.00 USD | 1,530.00 USD | 0.00 USD | `+21.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,190,000.00 USD | 2,280.00 USD | 0.00 USD | `+21.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,190,000.00 USD | 541.32 USD | 0.00 USD | `+22.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,330,000.00 USD | 137,500.00 USD | 0.00 USD | `+22.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,330,000.00 USD | 691.07 USD | 0.00 USD | `+22.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,330,000.00 USD | 6,250.00 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,350,000.00 USD | 13,480.00 USD | 0.00 USD | `+22.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,350,000.00 USD | 734.82 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,350,000.00 USD | 1,230.00 USD | 0.00 USD | `+23.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,350,000.00 USD | 105.00 USD | 0.00 USD | `+23.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,350,000.00 USD | 184.09 USD | 0.00 USD | `+23.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,350,000.00 USD | 1,120.00 USD | 0.00 USD | `+24.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,350,000.00 USD | 1,860.00 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,350,000.00 USD | 1,070.00 USD | 0.00 USD | `+24.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,350,000.00 USD | 512.15 USD | 0.00 USD | `+24.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,360,000.00 USD | 6,620.00 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,360,000.00 USD | 404.96 USD | 0.00 USD | `+25.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,360,000.00 USD | 129.85 USD | 0.00 USD | `+26.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,370,000.00 USD | 3,740.00 USD | 0.00 USD | `+26.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,370,000.00 USD | 409.17 USD | 0.00 USD | `+27.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,370,000.00 USD | 203.74 USD | 0.00 USD | `+27.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,370,000.00 USD | 2,800.00 USD | 0.00 USD | `+28.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,370,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,370,000.00 USD | 694.56 USD | 0.00 USD | `+29.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,370,000.00 USD | 940.91 USD | 0.00 USD | `+30.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,370,000.00 USD | 2,980.00 USD | 0.00 USD | `+30.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,370,000.00 USD | 104.99 USD | 0.00 USD | `+31.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,380,000.00 USD | 1,930.00 USD | 0.00 USD | `+31.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,380,000.00 USD | 1,490.00 USD | 0.00 USD | `+31.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,380,000.00 USD | 1,090.00 USD | 0.00 USD | `+31.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,380,000.00 USD | 438.96 USD | 0.00 USD | `+31.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,380,000.00 USD | 973.76 USD | 0.00 USD | `+31.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,390,000.00 USD | 10,000.00 USD | 0.00 USD | `+32.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,390,000.00 USD | 175.59 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,390,000.00 USD | 2,060.00 USD | 0.00 USD | `+32.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,390,000.00 USD | 482.89 USD | 0.00 USD | `+33.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,390,000.00 USD | 201.90 USD | 0.00 USD | `+33.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,390,000.00 USD | 489.46 USD | 0.00 USD | `+33.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,390,000.00 USD | 103.68 USD | 0.00 USD | `+34.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,400,000.00 USD | 2,590.00 USD | 0.00 USD | `+34.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,400,000.00 USD | 3,810.00 USD | 0.00 USD | `+34.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,410,000.00 USD | 11,200.00 USD | 0.00 USD | `+35.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,420,000.00 USD | 4,330.00 USD | 0.00 USD | `+35.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,420,000.00 USD | 205.50 USD | 0.00 USD | `+35.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,420,000.00 USD | 3,490.00 USD | 0.00 USD | `+36.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,420,000.00 USD | 1,300.00 USD | 0.00 USD | `+36.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,420,000.00 USD | 207.50 USD | 0.00 USD | `+37.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,420,000.00 USD | 813.88 USD | 0.00 USD | `+37.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,450,000.00 USD | 23,160.00 USD | 0.00 USD | `+38.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,450,000.00 USD | 781.51 USD | 0.00 USD | `+38.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,450,000.00 USD | 209.30 USD | 0.00 USD | `+38.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,450,000.00 USD | 1,440.00 USD | 0.00 USD | `+38.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,450,000.00 USD | 5,140.00 USD | 0.00 USD | `+38.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,450,000.00 USD | 585.32 USD | 0.00 USD | `+39.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,450,000.00 USD | 210.90 USD | 0.00 USD | `+39.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,460,000.00 USD | 1,850.00 USD | 0.00 USD | `+39.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,460,000.00 USD | 105.75 USD | 0.00 USD | `+39.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,460,000.00 USD | 3,220.00 USD | 0.00 USD | `+40.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,460,000.00 USD | 1,600.00 USD | 0.00 USD | `+40.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,460,000.00 USD | 212.90 USD | 0.00 USD | `+40.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,460,000.00 USD | 472.63 USD | 0.00 USD | `+41.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,460,000.00 USD | 214.50 USD | 0.00 USD | `+41.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,460,000.00 USD | 1,040.00 USD | 0.00 USD | `+42.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,460,000.00 USD | 136.12 USD | 0.00 USD | `+42.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,460,000.00 USD | 216.10 USD | 0.00 USD | `+42.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,460,000.00 USD | 1,010.00 USD | 0.00 USD | `+43.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,460,000.00 USD | 217.90 USD | 0.00 USD | `+44.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,460,000.00 USD | 219.70 USD | 0.00 USD | `+45.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,470,000.00 USD | 7,780.00 USD | 0.00 USD | `+45.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,470,000.00 USD | 154.22 USD | 0.00 USD | `+46.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,470,000.00 USD | 221.30 USD | 0.00 USD | `+46.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,470,000.00 USD | 1,050.00 USD | 0.00 USD | `+46.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,500,000.00 USD | 24,190.00 USD | 0.00 USD | `+46.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,500,000.00 USD | 223.10 USD | 0.00 USD | `+47.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,500,000.00 USD | 224.70 USD | 0.00 USD | `+48.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,500,000.00 USD | 226.30 USD | 0.00 USD | `+49.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,500,000.00 USD | 950.34 USD | 0.00 USD | `+50.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,500,000.00 USD | 229.50 USD | 0.00 USD | `+51.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,500,000.00 USD | 771.08 USD | 0.00 USD | `+52.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,500,000.00 USD | 942.95 USD | 0.00 USD | `+52.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,500,000.00 USD | 230.90 USD | 0.00 USD | `+52.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,500,000.00 USD | 288.18 USD | 0.00 USD | `+52.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,500,000.00 USD | 619.10 USD | 0.00 USD | `+53.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,500,000.00 USD | 1,250.00 USD | 0.00 USD | `+53.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,500,000.00 USD | 1,050.00 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,500,000.00 USD | 232.30 USD | 0.00 USD | `+53.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,510,000.00 USD | 1,600.00 USD | 0.00 USD | `+54.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+54.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,510,000.00 USD | 3,730.00 USD | 0.00 USD | `+55.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,510,000.00 USD | 676.22 USD | 0.00 USD | `+55.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,510,000.00 USD | 648.25 USD | 0.00 USD | `+56.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,510,000.00 USD | 1,510.00 USD | 0.00 USD | `+56.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,510,000.00 USD | 448.52 USD | 0.00 USD | `+56.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,510,000.00 USD | 124.58 USD | 0.00 USD | `+56.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,520,000.00 USD | 1,050.00 USD | 0.00 USD | `+57.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,520,000.00 USD | 691.80 USD | 0.00 USD | `+58.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,630,000.00 USD | 117,860.00 USD | 0.00 USD | `+58.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,630,000.00 USD | 143.22 USD | 0.00 USD | `+59.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,640,000.00 USD | 1,380.00 USD | 0.00 USD | `+60.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,640,000.00 USD | 2,270.00 USD | 0.00 USD | `+61.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,640,000.00 USD | 871.99 USD | 0.00 USD | `+61.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,670,000.00 USD | 29,610.00 USD | 0.00 USD | `+67.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,670,000.00 USD | 400.21 USD | 0.00 USD | `+68.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,670,000.00 USD | 2,360.00 USD | 0.00 USD | `+74.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,680,000.00 USD | 4,160.00 USD | 0.00 USD | `+79.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,680,000.00 USD | 114.70 USD | 0.00 USD | `+80.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,680,000.00 USD | 278.50 USD | 0.00 USD | `+85.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,680,000.00 USD | 1,160.00 USD | 0.00 USD | `+87.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,680,000.00 USD | 173.57 USD | 0.00 USD | `+88.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,680,000.00 USD | 380.09 USD | 0.00 USD | `+88.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,690,000.00 USD | 17,150.00 USD | 0.00 USD | `+88.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,700,000.00 USD | 1,440.00 USD | 0.00 USD | `+90.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,700,000.00 USD | 433.35 USD | 0.00 USD | `+91.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,700,000.00 USD | 452.26 USD | 0.00 USD | `+92.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,700,000.00 USD | 3,640.00 USD | 0.00 USD | `+94.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,760,000.00 USD | 55,720.00 USD | 0.00 USD | `+95.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,760,000.00 USD | 2,120.00 USD | 0.00 USD | `+96.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,780,000.00 USD | 19,850.00 USD | 0.00 USD | `+98.37%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0647` | 29,780,000.00 USD | 0.00 USD | 29,780,000.00 USD | 23,160.00 USD | 13,720.00 USD | 0.00 USD |
| `7D` | `0.0649` | 29,740,000.00 USD | 0.00 USD | 29,740,000.00 USD | 21,850.00 USD | 0.00 USD | 15,770.00 USD |
| `7D` | `0.0657` | 29,710,000.00 USD | 0.00 USD | 29,710,000.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0661` | 29,690,000.00 USD | 0.00 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 40,620.00 USD |
| `7D` | `0.0663` | 29,650,000.00 USD | 0.00 USD | 29,650,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD |
| `7D` | `0.0665` | 29,640,000.00 USD | 0.00 USD | 29,640,000.00 USD | 169,640.00 USD | 12,840.00 USD | 0.00 USD |
| `7D` | `0.0669` | 29,460,000.00 USD | 0.00 USD | 29,460,000.00 USD | 0.00 USD | 0.00 USD | 1,590.00 USD |
| `7D` | `0.0675` | 29,460,000.00 USD | 0.00 USD | 29,460,000.00 USD | 25,430.00 USD | 8,460.00 USD | 19,470.00 USD |
| `7D` | `0.0677` | 29,410,000.00 USD | 0.00 USD | 29,410,000.00 USD | 10,470.00 USD | 0.00 USD | 475.18 USD |
| `1D` | `0.0678` | 17,350,000.00 USD | 0.00 USD | 17,350,000.00 USD | 20,570.00 USD | 61,960.00 USD | 82,960.00 USD |
| `1D` | `0.0679` | 17,190,000.00 USD | 0.00 USD | 17,190,000.00 USD | 43,120.00 USD | 38,120.00 USD | 86.69 USD |
| `7D` | `0.0679` | 29,390,000.00 USD | 0.00 USD | 29,390,000.00 USD | 6,140.00 USD | 59,770.00 USD | 61,020.00 USD |
| `1D` | `0.0680` | 17,110,000.00 USD | 0.00 USD | 17,110,000.00 USD | 51,160.00 USD | 43,850.00 USD | 34,330.00 USD |
| `1D` | `0.0681` | 16,980,000.00 USD | 0.00 USD | 16,980,000.00 USD | 36,810.00 USD | 55,770.00 USD | 150,410.00 USD |
| `7D` | `0.0681` | 29,270,000.00 USD | 0.00 USD | 29,270,000.00 USD | 118,640.00 USD | 61,880.00 USD | 164,800.00 USD |
| `1D` | `0.0682` | 16,730,000.00 USD | 0.00 USD | 16,730,000.00 USD | 14,920.00 USD | 58,710.00 USD | 27,060.00 USD |
| `1D` | `0.0683` | 16,630,000.00 USD | 0.00 USD | 16,630,000.00 USD | 15,780.00 USD | 32,750.00 USD | 467.62 USD |
| `7D` | `0.0683` | 28,920,000.00 USD | 0.00 USD | 28,920,000.00 USD | 0.00 USD | 58,370.00 USD | 66,930.00 USD |
| `1D` | `0.0684` | 16,580,000.00 USD | 0.00 USD | 16,580,000.00 USD | 24,150.00 USD | 26,540.00 USD | 3,380.00 USD |
| `1D` | `0.0685` | 16,530,000.00 USD | 0.00 USD | 16,530,000.00 USD | 58,140.00 USD | 14,450.00 USD | 28,590.00 USD |
| `7D` | `0.0685` | 28,800,000.00 USD | 0.00 USD | 28,800,000.00 USD | 142,840.00 USD | 77,920.00 USD | 25,380.00 USD |
| `1D` | `0.0686` | 16,430,000.00 USD | 0.00 USD | 16,430,000.00 USD | 56,540.00 USD | 17,000.00 USD | 17,280.00 USD |
| `1D` | `0.0687` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 17,350.00 USD | 32,460.00 USD | 30,030.00 USD |
| `7D` | `0.0687` | 28,550,000.00 USD | 0.00 USD | 28,550,000.00 USD | 101,720.00 USD | 128,090.00 USD | 1,010.00 USD |
| `1D` | `0.0688` | 16,260,000.00 USD | 0.00 USD | 16,260,000.00 USD | 16,500.00 USD | 9,410.00 USD | 34,370.00 USD |
| `1D` | `0.0689` | 16,200,000.00 USD | 0.00 USD | 16,200,000.00 USD | 10,400.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `0.0689` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 225,480.00 USD | 77,640.00 USD | 61,090.00 USD |
| `1D` | `0.0690` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD |
| `1D` | `0.0691` | 16,180,000.00 USD | 0.00 USD | 16,180,000.00 USD | 1,460.00 USD | 0.00 USD | 1,540.00 USD |
| `7D` | `0.0691` | 27,960,000.00 USD | 0.00 USD | 27,960,000.00 USD | 162,010.00 USD | 95,020.00 USD | 130,900.00 USD |
| `1D` | `0.0692` | 16,180,000.00 USD | 0.00 USD | 16,180,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0693` | 16,160,000.00 USD | 0.00 USD | 16,160,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0693` | 27,570,000.00 USD | 0.00 USD | 27,570,000.00 USD | 207,150.00 USD | 190,180.00 USD | 80,200.00 USD |
| `1D` | `0.0694` | 16,140,000.00 USD | 0.00 USD | 16,140,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0695` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0695` | 27,090,000.00 USD | 0.00 USD | 27,090,000.00 USD | 282,470.00 USD | 212,530.00 USD | 212,560.00 USD |
| `1D` | `0.0697` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD |
| `7D` | `0.0697` | 26,380,000.00 USD | 0.00 USD | 26,380,000.00 USD | 142,190.00 USD | 148,620.00 USD | 263,500.00 USD |
| `1D` | `0.0698` | 16,050,000.00 USD | 0.00 USD | 16,050,000.00 USD | 10,960.00 USD | 10,400.00 USD | 9,890.00 USD |
| `1D` | `0.0699` | 16,020,000.00 USD | 0.00 USD | 16,020,000.00 USD | 38,680.00 USD | 0.00 USD | 2,360.00 USD |
| `7D` | `0.0699` | 25,830,000.00 USD | 0.00 USD | 25,830,000.00 USD | 325,570.00 USD | 205,450.00 USD | 138,220.00 USD |
| `1D` | `0.0700` | 15,980,000.00 USD | 0.00 USD | 15,980,000.00 USD | 93,910.00 USD | 4,920.00 USD | 23,890.00 USD |
| `1D` | `0.0701` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 39,680.00 USD | 108,360.00 USD | 1,900.00 USD |
| `7D` | `0.0701` | 25,160,000.00 USD | 0.00 USD | 25,160,000.00 USD | 283,670.00 USD | 119,790.00 USD | 142,750.00 USD |
| `1D` | `0.0702` | 15,700,000.00 USD | 0.00 USD | 15,700,000.00 USD | 48,350.00 USD | 19,670.00 USD | 59.13 USD |
| `1D` | `0.0703` | 15,630,000.00 USD | 0.00 USD | 15,630,000.00 USD | 161,920.00 USD | 66,830.00 USD | 10,830.00 USD |
| `7D` | `0.0703` | 24,610,000.00 USD | 0.00 USD | 24,610,000.00 USD | 261,240.00 USD | 120,430.00 USD | 50,710.00 USD |
| `1D` | `0.0704` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 27,140.00 USD | 43,930.00 USD | 22,360.00 USD |
| `1D` | `0.0705` | 15,300,000.00 USD | 0.00 USD | 15,300,000.00 USD | 41,460.00 USD | 30,720.00 USD | 48,520.00 USD |
| `7D` | `0.0705` | 24,180,000.00 USD | 0.00 USD | 24,180,000.00 USD | 224,080.00 USD | 133,180.00 USD | 178,570.00 USD |
| `1D` | `0.0706` | 15,180,000.00 USD | 0.00 USD | 15,180,000.00 USD | 22,880.00 USD | 1,120.00 USD | 15,630.00 USD |
| `1D` | `0.0707` | 15,140,000.00 USD | 0.00 USD | 15,140,000.00 USD | 136,920.00 USD | 69,310.00 USD | 45,730.00 USD |
| `7D` | `0.0707` | 23,650,000.00 USD | 0.00 USD | 23,650,000.00 USD | 171,490.00 USD | 37,160.00 USD | 156,120.00 USD |
| `1D` | `0.0708` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 69,400.00 USD | 62,000.00 USD | 107,390.00 USD |
| `1D` | `0.0709` | 14,650,000.00 USD | 0.00 USD | 14,650,000.00 USD | 38,730.00 USD | 82,010.00 USD | 149,320.00 USD |
| `7D` | `0.0709` | 23,280,000.00 USD | 0.00 USD | 23,280,000.00 USD | 485,290.00 USD | 159,720.00 USD | 139,080.00 USD |
| `1D` | `0.0710` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 117,230.00 USD | 91,550.00 USD | 119,960.00 USD |
| `1D` | `0.0711` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 49,210.00 USD | 25,670.00 USD | 43,530.00 USD |
| `7D` | `0.0711` | 22,500,000.00 USD | 0.00 USD | 22,500,000.00 USD | 285,730.00 USD | 252,130.00 USD | 91,190.00 USD |
| `1D` | `0.0712` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 165,590.00 USD | 46,690.00 USD | 4,000.00 USD |
| `1D` | `0.0713` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 75,840.00 USD | 85,230.00 USD | 63,930.00 USD |
| `7D` | `0.0713` | 21,870,000.00 USD | 0.00 USD | 21,870,000.00 USD | 379,600.00 USD | 171,480.00 USD | 139,950.00 USD |
| `1D` | `0.0714` | 13,490,000.00 USD | 0.00 USD | 13,490,000.00 USD | 120,780.00 USD | 51,930.00 USD | 48,070.00 USD |
| `1D` | `0.0715` | 13,270,000.00 USD | 0.00 USD | 13,270,000.00 USD | 75,940.00 USD | 238,460.00 USD | 43,090.00 USD |
| `7D` | `0.0715` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 211,700.00 USD | 51,460.00 USD | 66,820.00 USD |
| `1D` | `0.0716` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 19,480.00 USD | 51,080.00 USD | 173.38 USD |
| `1D` | `0.0717` | 12,840,000.00 USD | 0.00 USD | 12,840,000.00 USD | 238,310.00 USD | 96,160.00 USD | 385.38 USD |
| `7D` | `0.0717` | 20,850,000.00 USD | 0.00 USD | 20,850,000.00 USD | 285,100.00 USD | 190,890.00 USD | 48,380.00 USD |
| `1D` | `0.0718` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 64,570.00 USD | 101,030.00 USD | 13,040.00 USD |
| `1D` | `0.0719` | 12,330,000.00 USD | 0.00 USD | 12,330,000.00 USD | 229,400.00 USD | 45,330.00 USD | 72,220.00 USD |
| `7D` | `0.0719` | 20,320,000.00 USD | 0.00 USD | 20,320,000.00 USD | 233,070.00 USD | 63,390.00 USD | 276,250.00 USD |
| `1D` | `0.0720` | 11,980,000.00 USD | 0.00 USD | 11,980,000.00 USD | 138,650.00 USD | 50,600.00 USD | 72,110.00 USD |
| `1D` | `0.0721` | 11,720,000.00 USD | 0.00 USD | 11,720,000.00 USD | 308,410.00 USD | 298,040.00 USD | 67,520.00 USD |
| `7D` | `0.0721` | 19,750,000.00 USD | 0.00 USD | 19,750,000.00 USD | 422,700.00 USD | 285,460.00 USD | 95,670.00 USD |
| `1D` | `0.0722` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 181,970.00 USD | 122,030.00 USD | 150,560.00 USD |
| `1D` | `0.0723` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 85,680.00 USD | 258,330.00 USD | 326,730.00 USD |
| `7D` | `0.0723` | 18,950,000.00 USD | 0.00 USD | 18,950,000.00 USD | 242,550.00 USD | 148,860.00 USD | 110,740.00 USD |
| `1D` | `0.0724` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 141,120.00 USD | 214,730.00 USD | 382,240.00 USD |
| `1D` | `0.0725` | 9,180,000.00 USD | 0.00 USD | 9,180,000.00 USD | 245,770.00 USD | 252,860.00 USD | 293,390.00 USD |
| `7D` | `0.0725` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 1,070,000.00 USD | 365,360.00 USD | 152,800.00 USD |
| `1D` | `0.0726` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 132,320.00 USD | 139,590.00 USD | 59,700.00 USD |
| `1D` | `0.0727` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 190,550.00 USD | 161,760.00 USD | 45,560.00 USD |
| `7D` | `0.0727` | 16,860,000.00 USD | 0.00 USD | 16,860,000.00 USD | 249,200.00 USD | 432,030.00 USD | 92,170.00 USD |
| `1D` | `0.0728` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 60,510.00 USD | 154,910.00 USD | 48,430.00 USD |
| `1D` | `0.0729` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 58,550.00 USD | 41,110.00 USD | 9,760.00 USD |
| `7D` | `0.0729` | 16,080,000.00 USD | 0.00 USD | 16,080,000.00 USD | 114,120.00 USD | 105,410.00 USD | 37,020.00 USD |
| `1D` | `0.0730` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 123,090.00 USD | 55,310.00 USD | 51,030.00 USD |
| `1D` | `0.0731` | 7,060,000.00 USD | 0.00 USD | 7,060,000.00 USD | 44,230.00 USD | 81,130.00 USD | 28,420.00 USD |
| `7D` | `0.0731` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 565,310.00 USD | 49,290.00 USD | 12,800.00 USD |
| `1D` | `0.0732` | 6,910,000.00 USD | 0.00 USD | 6,910,000.00 USD | 153,570.00 USD | 93,810.00 USD | 93,610.00 USD |
| `1D` | `0.0733` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 64,680.00 USD | 96,060.00 USD | 31,580.00 USD |
| `7D` | `0.0733` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 470,120.00 USD | 0.00 USD | 29,970.00 USD |
| `1D` | `0.0734` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 361,270.00 USD | 80,330.00 USD | 0.00 USD |
| `1D` | `0.0735` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 141,790.00 USD | 23,950.00 USD | 5,270.00 USD |
| `7D` | `0.0735` | 14,700,000.00 USD | 0.00 USD | 14,700,000.00 USD | 589,440.00 USD | 93,670.00 USD | 0.00 USD |
| `1D` | `0.0736` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD |
| `1D` | `0.0737` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 113,510.00 USD | 52,730.00 USD | 49,860.00 USD |
| `7D` | `0.0737` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 506,070.00 USD | 494,020.00 USD | 0.00 USD |
| `1D` | `0.0738` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 78,630.00 USD | 23,440.00 USD | 0.00 USD |
| `1D` | `0.0739` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 128,640.00 USD | 17,470.00 USD | 22,490.00 USD |
| `7D` | `0.0739` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 265,850.00 USD | 515,020.00 USD | 0.00 USD |
| `1D` | `0.0740` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 41,890.00 USD | 102,110.00 USD | 81,230.00 USD |
| `1D` | `0.0741` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 175,330.00 USD | 166,190.00 USD | 102,820.00 USD |
| `7D` | `0.0741` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 66,970.00 USD | 294,670.00 USD | 178,730.00 USD |
| `1D` | `0.0742` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 90,280.00 USD | 290,690.00 USD | 80,900.00 USD |
| `1D` | `0.0743` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 236,300.00 USD | 181,510.00 USD | 284,730.00 USD |
| `7D` | `0.0743` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 774,380.00 USD | 209,100.00 USD | 1,120,000.00 USD |
| `1D` | `0.0744` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 217,450.00 USD | 118,720.00 USD | 107,270.00 USD |
| `1D` | `0.0745` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 87,580.00 USD | 88,750.00 USD | 46,710.00 USD |
| `7D` | `0.0745` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 1,360,000.00 USD | 951,300.00 USD | 326,000.00 USD |
| `1D` | `0.0746` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 88,460.00 USD | 86,840.00 USD | 142,590.00 USD |
| `1D` | `0.0747` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 625,930.00 USD | 210,220.00 USD | 148,860.00 USD |
| `7D` | `0.0747` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 1,410,000.00 USD | 1,830,000.00 USD | 649,410.00 USD |
| `1D` | `0.0748` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 98,680.00 USD | 109,690.00 USD | 198,860.00 USD |
| `1D` | `0.0749` | 818,980.00 USD | 0.00 USD | 818,980.00 USD | 122,780.00 USD | 90,750.00 USD | 131,510.00 USD |
| `7D` | `0.0749` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 706,340.00 USD | 459,930.00 USD | 875,850.00 USD |
| `1D` | `0.0750` | 473,930.00 USD | 0.00 USD | 473,930.00 USD | 38,560.00 USD | 25,780.00 USD | 0.00 USD |
| `1D` | `0.0751` | 409,590.00 USD | 0.00 USD | 409,590.00 USD | 0.00 USD | 37,490.00 USD | 10,540.00 USD |
| `7D` | `0.0751` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 30,900.00 USD | 84,880.00 USD |
| `1D` | `0.0752` | 361,560.00 USD | 0.00 USD | 361,560.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD |
| `1D` | `0.0753` | 337,140.00 USD | 0.00 USD | 337,140.00 USD | 0.00 USD | 12,650.00 USD | 141,640.00 USD |
| `7D` | `0.0753` | 907,280.00 USD | 0.00 USD | 907,280.00 USD | 751,120.00 USD | 53,860.00 USD | 102,300.00 USD |
| `1D` | `0.0755` | 182,850.00 USD | 0.00 USD | 182,850.00 USD | 182,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0755` | 938,670.00 USD | 938,670.00 USD | 0.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD |
| `7D` | `0.0755` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 792,920.00 USD | 0.00 USD | 145,750.00 USD |
| `1D` | `0.0756` | 30,100.00 USD | 30,100.00 USD | 0.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD |
| `1D` | `0.0756` | 60,200.00 USD | 60,200.00 USD | 0.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD |
| `7D` | `0.0757` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 144,530.00 USD | 0.00 USD |
| `1D` | `0.0758` | 65,120.00 USD | 65,120.00 USD | 0.00 USD | 0.00 USD | 4,920.00 USD | 0.00 USD |
| `1D` | `0.0759` | 65,280.00 USD | 65,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 160.56 USD |
| `7D` | `0.0759` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 40,360.00 USD | 66,300.00 USD | 0.00 USD |
| `1D` | `0.0761` | 65,700.00 USD | 65,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 420.80 USD |
| `1D` | `0.0762` | 65,870.00 USD | 65,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 168.86 USD |
| `1D` | `0.0764` | 80,690.00 USD | 80,690.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | 0.00 USD |
| `1D` | `0.0765` | 428,850.00 USD | 428,850.00 USD | 0.00 USD | 211,600.00 USD | 37,120.00 USD | 99,440.00 USD |
| `7D` | `0.0765` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 772,480.00 USD | 496,590.00 USD | 0.00 USD |
| `1D` | `0.0766` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 586,470.00 USD | 522,700.00 USD | 291.50 USD |
| `1D` | `0.0767` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 188,080.00 USD | 328,450.00 USD | 159,130.00 USD |
| `7D` | `0.0767` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 1,180,000.00 USD | 90,730.00 USD | 0.00 USD |
| `1D` | `0.0768` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 224,320.00 USD | 93,770.00 USD | 594,750.00 USD |
| `1D` | `0.0769` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 305,260.00 USD | 438,740.00 USD | 310,120.00 USD |
| `7D` | `0.0769` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 760,570.00 USD | 84,300.00 USD | 429,490.00 USD |
| `1D` | `0.0770` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 396,020.00 USD | 281,820.00 USD | 450,850.00 USD |
| `1D` | `0.0771` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 398,660.00 USD | 441,880.00 USD | 251,890.00 USD |
| `7D` | `0.0771` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 888,600.00 USD | 798,440.00 USD | 794,320.00 USD |
| `1D` | `0.0772` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 480,450.00 USD | 327,770.00 USD | 765,720.00 USD |
| `1D` | `0.0773` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 190,960.00 USD | 368,960.00 USD | 243,950.00 USD |
| `7D` | `0.0773` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 69,030.00 USD | 347,590.00 USD | 64,060.00 USD |
| `1D` | `0.0774` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 118,800.00 USD | 246,740.00 USD | 36,420.00 USD |
| `1D` | `0.0775` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 288,570.00 USD | 180,890.00 USD | 61,000.00 USD |
| `7D` | `0.0775` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 779,670.00 USD | 375,100.00 USD | 0.00 USD |
| `1D` | `0.0776` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 284,830.00 USD | 214,460.00 USD | 142,590.00 USD |
| `1D` | `0.0777` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 401,010.00 USD | 342,630.00 USD | 163,070.00 USD |
| `7D` | `0.0777` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 265,980.00 USD | 286,560.00 USD | 693.20 USD |
| `1D` | `0.0778` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 116,640.00 USD | 340,450.00 USD | 401,410.00 USD |
| `1D` | `0.0779` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 345,840.00 USD | 210,420.00 USD | 205,560.00 USD |
| `7D` | `0.0779` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 270,450.00 USD | 301,690.00 USD | 438,670.00 USD |
| `1D` | `0.0780` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 212,580.00 USD | 78,920.00 USD | 39,560.00 USD |
| `1D` | `0.0781` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 151,030.00 USD | 193,800.00 USD | 19,450.00 USD |
| `7D` | `0.0781` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 186,410.00 USD | 142,450.00 USD | 4,370.00 USD |
| `1D` | `0.0782` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 70,430.00 USD | 84,580.00 USD | 79,320.00 USD |
| `1D` | `0.0783` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 48,890.00 USD | 214,890.00 USD | 177,310.00 USD |
| `7D` | `0.0783` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 15,350.00 USD | 285,880.00 USD | 193,490.00 USD |
| `1D` | `0.0784` | 14,770,000.00 USD | 14,770,000.00 USD | 0.00 USD | 353,240.00 USD | 110,170.00 USD | 50,700.00 USD |
| `1D` | `0.0785` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 208,550.00 USD | 161,570.00 USD | 102,810.00 USD |
| `7D` | `0.0785` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 197,420.00 USD | 141,600.00 USD | 278,250.00 USD |
| `1D` | `0.0786` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 330,770.00 USD | 209,740.00 USD | 296,610.00 USD |
| `1D` | `0.0787` | 17,310,000.00 USD | 17,310,000.00 USD | 0.00 USD | 379,110.00 USD | 464,730.00 USD | 386,460.00 USD |
| `7D` | `0.0787` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 437,500.00 USD | 346,050.00 USD | 812,710.00 USD |
| `1D` | `0.0788` | 17,860,000.00 USD | 17,860,000.00 USD | 0.00 USD | 168,080.00 USD | 262,350.00 USD | 123,650.00 USD |
| `1D` | `0.0789` | 18,510,000.00 USD | 18,510,000.00 USD | 0.00 USD | 312,410.00 USD | 233,260.00 USD | 102,060.00 USD |
| `7D` | `0.0789` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 301,760.00 USD | 259,180.00 USD | 249,350.00 USD |
| `1D` | `0.0790` | 18,780,000.00 USD | 18,780,000.00 USD | 0.00 USD | 153,960.00 USD | 87,240.00 USD | 27,520.00 USD |
| `1D` | `0.0791` | 19,240,000.00 USD | 19,240,000.00 USD | 0.00 USD | 199,650.00 USD | 133,580.00 USD | 125,070.00 USD |
| `7D` | `0.0791` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 476,430.00 USD | 81,300.00 USD | 5,350.00 USD |
| `1D` | `0.0792` | 19,590,000.00 USD | 19,590,000.00 USD | 0.00 USD | 224,560.00 USD | 57,840.00 USD | 74,710.00 USD |
| `1D` | `0.0793` | 19,600,000.00 USD | 19,600,000.00 USD | 0.00 USD | 5,950.00 USD | 0.00 USD | 289.58 USD |
| `7D` | `0.0793` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 27,550.00 USD | 61,220.00 USD | 246,330.00 USD |
| `1D` | `0.0794` | 19,950,000.00 USD | 19,950,000.00 USD | 0.00 USD | 158,580.00 USD | 96,210.00 USD | 100,830.00 USD |
| `1D` | `0.0795` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 92,560.00 USD | 45,380.00 USD | 103,710.00 USD |
| `7D` | `0.0795` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 206,900.00 USD | 0.00 USD | 469,960.00 USD |
| `1D` | `0.0796` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 199,280.00 USD | 12,890.00 USD | 1,890.00 USD |
| `1D` | `0.0797` | 20,770,000.00 USD | 20,770,000.00 USD | 0.00 USD | 206,810.00 USD | 89,760.00 USD | 65,390.00 USD |
| `7D` | `0.0797` | 18,020,000.00 USD | 18,020,000.00 USD | 0.00 USD | 640,790.00 USD | 203,560.00 USD | 119,170.00 USD |
| `1D` | `0.0798` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 58,670.00 USD | 110,930.00 USD | 2,870.00 USD |
| `1D` | `0.0799` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 99,030.00 USD | 191,860.00 USD | 107,080.00 USD |
| `7D` | `0.0799` | 18,790,000.00 USD | 18,790,000.00 USD | 0.00 USD | 561,590.00 USD | 130,870.00 USD | 78,050.00 USD |
| `1D` | `0.0800` | 21,500,000.00 USD | 21,500,000.00 USD | 0.00 USD | 48,550.00 USD | 9,760.00 USD | 95,080.00 USD |
| `1D` | `0.0801` | 21,520,000.00 USD | 21,520,000.00 USD | 0.00 USD | 25,740.00 USD | 0.00 USD | 1,490.00 USD |
| `7D` | `0.0801` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 85,040.00 USD | 0.00 USD | 104,840.00 USD |
| `1D` | `0.0802` | 21,550,000.00 USD | 21,550,000.00 USD | 0.00 USD | 25,490.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `0.0803` | 21,660,000.00 USD | 21,660,000.00 USD | 0.00 USD | 21,230.00 USD | 43,340.00 USD | 41,200.00 USD |
| `7D` | `0.0803` | 19,020,000.00 USD | 19,020,000.00 USD | 0.00 USD | 42,220.00 USD | 0.00 USD | 1,480.00 USD |
| `1D` | `0.0804` | 21,670,000.00 USD | 21,670,000.00 USD | 0.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 21,840,000.00 USD | 21,840,000.00 USD | 0.00 USD | 89,620.00 USD | 37,230.00 USD | 41,240.00 USD |
| `7D` | `0.0805` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 228,320.00 USD | 43,910.00 USD | 53,390.00 USD |
| `1D` | `0.0806` | 22,100,000.00 USD | 22,100,000.00 USD | 0.00 USD | 28,730.00 USD | 21,040.00 USD | 215,520.00 USD |
| `1D` | `0.0807` | 22,510,000.00 USD | 22,510,000.00 USD | 0.00 USD | 228,350.00 USD | 143,670.00 USD | 30,480.00 USD |
| `7D` | `0.0807` | 20,790,000.00 USD | 20,790,000.00 USD | 0.00 USD | 217,720.00 USD | 934,840.00 USD | 294,860.00 USD |
| `1D` | `0.0808` | 23,160,000.00 USD | 23,160,000.00 USD | 0.00 USD | 150,860.00 USD | 116,140.00 USD | 382,880.00 USD |
| `1D` | `0.0809` | 23,500,000.00 USD | 23,500,000.00 USD | 0.00 USD | 109,380.00 USD | 220,760.00 USD | 12,790.00 USD |
| `7D` | `0.0809` | 22,570,000.00 USD | 22,570,000.00 USD | 0.00 USD | 9,880.00 USD | 1,760,000.00 USD | 1,700.00 USD |
| `1D` | `0.0810` | 23,950,000.00 USD | 23,950,000.00 USD | 0.00 USD | 192,870.00 USD | 127,690.00 USD | 132,730.00 USD |
| `1D` | `0.0811` | 24,210,000.00 USD | 24,210,000.00 USD | 0.00 USD | 100,060.00 USD | 145,810.00 USD | 11,510.00 USD |
| `7D` | `0.0811` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 131,030.00 USD | 730,620.00 USD | 1,610.00 USD |
| `1D` | `0.0812` | 24,500,000.00 USD | 24,500,000.00 USD | 0.00 USD | 138,630.00 USD | 102,020.00 USD | 49,540.00 USD |
| `1D` | `0.0813` | 24,680,000.00 USD | 24,680,000.00 USD | 0.00 USD | 45,000.00 USD | 30,430.00 USD | 109,260.00 USD |
| `7D` | `0.0813` | 24,500,000.00 USD | 24,500,000.00 USD | 0.00 USD | 517,320.00 USD | 548,390.00 USD | 2,470.00 USD |
| `1D` | `0.0814` | 25,020,000.00 USD | 25,020,000.00 USD | 0.00 USD | 43,650.00 USD | 108,690.00 USD | 184,100.00 USD |
| `1D` | `0.0815` | 25,140,000.00 USD | 25,140,000.00 USD | 0.00 USD | 20,890.00 USD | 6,740.00 USD | 94,490.00 USD |
| `7D` | `0.0815` | 26,110,000.00 USD | 26,110,000.00 USD | 0.00 USD | 671,840.00 USD | 643,990.00 USD | 300,370.00 USD |
| `1D` | `0.0816` | 25,840,000.00 USD | 25,840,000.00 USD | 0.00 USD | 323,740.00 USD | 194,310.00 USD | 179,480.00 USD |
| `1D` | `0.0817` | 26,390,000.00 USD | 26,390,000.00 USD | 0.00 USD | 280,410.00 USD | 134,560.00 USD | 130,180.00 USD |
| `7D` | `0.0817` | 28,680,000.00 USD | 28,680,000.00 USD | 0.00 USD | 1,200,000.00 USD | 745,850.00 USD | 614,910.00 USD |
| `1D` | `0.0818` | 27,050,000.00 USD | 27,050,000.00 USD | 0.00 USD | 234,840.00 USD | 161,260.00 USD | 267,850.00 USD |
| `1D` | `0.0819` | 27,650,000.00 USD | 27,650,000.00 USD | 0.00 USD | 158,800.00 USD | 312,480.00 USD | 128,570.00 USD |
| `7D` | `0.0819` | 30,790,000.00 USD | 30,790,000.00 USD | 0.00 USD | 672,340.00 USD | 512,490.00 USD | 929,000.00 USD |
| `1D` | `0.0820` | 28,190,000.00 USD | 28,190,000.00 USD | 0.00 USD | 52,420.00 USD | 172,050.00 USD | 319,880.00 USD |
| `1D` | `0.0821` | 28,480,000.00 USD | 28,480,000.00 USD | 0.00 USD | 151,670.00 USD | 48,110.00 USD | 85,260.00 USD |
| `7D` | `0.0821` | 33,150,000.00 USD | 33,150,000.00 USD | 0.00 USD | 1,210,000.00 USD | 760,670.00 USD | 390,320.00 USD |
| `1D` | `0.0822` | 29,040,000.00 USD | 29,040,000.00 USD | 0.00 USD | 249,310.00 USD | 151,600.00 USD | 156,380.00 USD |
| `1D` | `0.0823` | 29,380,000.00 USD | 29,380,000.00 USD | 0.00 USD | 267,050.00 USD | 72,540.00 USD | 8,520.00 USD |
| `7D` | `0.0823` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 884,810.00 USD | 520,900.00 USD | 366,690.00 USD |
| `1D` | `0.0824` | 29,950,000.00 USD | 29,950,000.00 USD | 0.00 USD | 168,680.00 USD | 204,930.00 USD | 190,880.00 USD |
| `1D` | `0.0825` | 30,200,000.00 USD | 30,200,000.00 USD | 0.00 USD | 102,430.00 USD | 125,690.00 USD | 22,000.00 USD |
| `7D` | `0.0825` | 36,500,000.00 USD | 36,500,000.00 USD | 0.00 USD | 761,460.00 USD | 514,320.00 USD | 307,380.00 USD |
| `1D` | `0.0826` | 30,630,000.00 USD | 30,630,000.00 USD | 0.00 USD | 131,950.00 USD | 125,260.00 USD | 170,210.00 USD |
| `1D` | `0.0827` | 30,720,000.00 USD | 30,720,000.00 USD | 0.00 USD | 13,110.00 USD | 62,110.00 USD | 16,660.00 USD |
| `7D` | `0.0827` | 37,650,000.00 USD | 37,650,000.00 USD | 0.00 USD | 658,340.00 USD | 220,660.00 USD | 271,680.00 USD |
| `1D` | `0.0828` | 31,050,000.00 USD | 31,050,000.00 USD | 0.00 USD | 187,960.00 USD | 75,940.00 USD | 66,460.00 USD |
| `1D` | `0.0829` | 31,310,000.00 USD | 31,310,000.00 USD | 0.00 USD | 168,550.00 USD | 88,230.00 USD | 326.19 USD |
| `7D` | `0.0829` | 38,690,000.00 USD | 38,690,000.00 USD | 0.00 USD | 645,990.00 USD | 177,740.00 USD | 214,060.00 USD |
| `1D` | `0.0830` | 31,440,000.00 USD | 31,440,000.00 USD | 0.00 USD | 54,060.00 USD | 37,820.00 USD | 43,280.00 USD |
| `1D` | `0.0831` | 31,520,000.00 USD | 31,520,000.00 USD | 0.00 USD | 22,160.00 USD | 16,920.00 USD | 37,650.00 USD |
| `7D` | `0.0831` | 39,590,000.00 USD | 39,590,000.00 USD | 0.00 USD | 452,190.00 USD | 160,720.00 USD | 288,260.00 USD |
| `1D` | `0.0832` | 31,900,000.00 USD | 31,900,000.00 USD | 0.00 USD | 185,880.00 USD | 93,160.00 USD | 100,760.00 USD |
| `1D` | `0.0833` | 32,320,000.00 USD | 32,320,000.00 USD | 0.00 USD | 130,200.00 USD | 111,030.00 USD | 181,790.00 USD |
| `7D` | `0.0833` | 40,810,000.00 USD | 40,810,000.00 USD | 0.00 USD | 524,880.00 USD | 414,820.00 USD | 276,510.00 USD |
| `1D` | `0.0834` | 32,710,000.00 USD | 32,710,000.00 USD | 0.00 USD | 128,050.00 USD | 118,950.00 USD | 144,310.00 USD |
| `1D` | `0.0835` | 33,070,000.00 USD | 33,070,000.00 USD | 0.00 USD | 109,250.00 USD | 188,990.00 USD | 64,580.00 USD |
| `7D` | `0.0835` | 41,970,000.00 USD | 41,970,000.00 USD | 0.00 USD | 365,460.00 USD | 261,800.00 USD | 536,330.00 USD |
| `1D` | `0.0836` | 33,340,000.00 USD | 33,340,000.00 USD | 0.00 USD | 44,050.00 USD | 74,690.00 USD | 147,470.00 USD |
| `1D` | `0.0837` | 33,570,000.00 USD | 33,570,000.00 USD | 0.00 USD | 130,410.00 USD | 32,170.00 USD | 62,550.00 USD |
| `7D` | `0.0837` | 42,770,000.00 USD | 42,770,000.00 USD | 0.00 USD | 453,970.00 USD | 227,430.00 USD | 115,210.00 USD |
| `1D` | `0.0838` | 33,870,000.00 USD | 33,870,000.00 USD | 0.00 USD | 180,800.00 USD | 85,610.00 USD | 42,800.00 USD |
| `1D` | `0.0839` | 34,000,000.00 USD | 34,000,000.00 USD | 0.00 USD | 60,660.00 USD | 32,460.00 USD | 29,490.00 USD |
| `7D` | `0.0839` | 43,250,000.00 USD | 43,250,000.00 USD | 0.00 USD | 321,350.00 USD | 128,090.00 USD | 36,900.00 USD |
| `1D` | `0.0840` | 34,080,000.00 USD | 34,080,000.00 USD | 0.00 USD | 28,070.00 USD | 24,900.00 USD | 34,370.00 USD |
| `1D` | `0.0841` | 34,100,000.00 USD | 34,100,000.00 USD | 0.00 USD | 9,490.00 USD | 2,010.00 USD | 0.00 USD |
| `7D` | `0.0841` | 43,520,000.00 USD | 43,520,000.00 USD | 0.00 USD | 205,170.00 USD | 0.00 USD | 64,950.00 USD |
| `1D` | `0.0842` | 34,140,000.00 USD | 34,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46,530.00 USD |
| `7D` | `0.0843` | 44,020,000.00 USD | 44,020,000.00 USD | 0.00 USD | 337,540.00 USD | 77,640.00 USD | 85,070.00 USD |
| `7D` | `0.0845` | 44,490,000.00 USD | 44,490,000.00 USD | 0.00 USD | 234,950.00 USD | 95,020.00 USD | 138,940.00 USD |
| `7D` | `0.0847` | 45,000,000.00 USD | 45,000,000.00 USD | 0.00 USD | 244,090.00 USD | 190,180.00 USD | 77,700.00 USD |
| `7D` | `0.0849` | 45,730,000.00 USD | 45,730,000.00 USD | 0.00 USD | 310,690.00 USD | 205,870.00 USD | 208,400.00 USD |
| `7D` | `0.0850` | 46,060,000.00 USD | 46,060,000.00 USD | 0.00 USD | 87,360.00 USD | 53,240.00 USD | 186,300.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.06B` | Total OI Tokens: `13,988,150,165.9 DOGE`
  * 1h OI Change: `+0.49%` | 4h OI Change: `+0.04%` | 24h OI Change: `-5.05%`
  * Exchange Breakdown: Binance=`240.46M` | Bybit=`106.74M` | OKX=`111.05M` | Hyperliquid=`75.98M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `27.53K` | Last 24h: `49.48K` | Last 3d: `238.63K` | Last 7d: `304.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0007%` |
| **USDT Bybit** | `0.0065%` | **USDT KuCoin** | `0.0078%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0004%` | **USDT Bitget** | `0.0025%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `37.65%` | `62.35%` | `0.60` | 10,100,000.00 USD |
| `15M` | `Binance` | `37.43%` | `62.57%` | `0.60` | 3,580,000.00 USD |
| `15M` | `OKX` | `34.49%` | `65.51%` | `0.53` | 2,060,000.00 USD |
| `15M` | `Bybit` | `44%` | `56%` | `0.79` | 793,910.00 USD |
| `15M` | `KuCoin` | `23.33%` | `76.67%` | `0.30` | 70,430.00 USD |
| `15M` | `Gate` | `46.93%` | `53.07%` | `0.88` | 1,620,000.00 USD |
| `15M` | `Bitget` | `35.82%` | `64.18%` | `0.56` | 230,780.00 USD |
| `15M` | `BingX` | `35.01%` | `64.99%` | `0.54` | 180,340.00 USD |
| `15M` | `MEXC` | `42.39%` | `57.61%` | `0.74` | 430,230.00 USD |
| `15M` | `Bitunix` | `31.05%` | `68.95%` | `0.45` | 220,970.00 USD |
| `15M` | `Hyperliquid` | `55.82%` | `44.18%` | `1.26` | 50,400.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `36.14%` | `63.86%` | `0.57` | 63,980.00 USD |
| `15M` | `Crypto.com` | `33.19%` | `66.81%` | `0.50` | 13,990.00 USD |
| `15M` | `WhiteBIT` | `17.22%` | `82.78%` | `0.21` | 593,870.00 USD |
| `15M` | `HTX` | `53.49%` | `46.51%` | `1.15` | 50,010.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `22.8%` | `77.2%` | `0.30` | 86,830.00 USD |
| `15M` | `Aster` | `45.02%` | `54.98%` | `0.82` | 41,750.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 1,240.00 USD |
| `15M` | `Whale Positions` | `37.43%` | `62.57%` | `0.60` | 3,580,000.00 USD |
| `15M` | `Global Accounts` | `37.65%` | `62.35%` | `0.60` | 10,100,000.00 USD |
| `1H` | `DOGE` | `42.01%` | `57.99%` | `0.72` | 45,350,000.00 USD |
| `1H` | `Binance` | `41.76%` | `58.24%` | `0.72` | 16,880,000.00 USD |
| `1H` | `OKX` | `41.25%` | `58.75%` | `0.70` | 8,390,000.00 USD |
| `1H` | `Bybit` | `36.26%` | `63.74%` | `0.57` | 4,100,000.00 USD |
| `1H` | `KuCoin` | `44.08%` | `55.92%` | `0.79` | 395,280.00 USD |
| `1H` | `Gate` | `46.89%` | `53.11%` | `0.88` | 8,210,000.00 USD |
| `1H` | `Bitget` | `44.15%` | `55.85%` | `0.79` | 782,120.00 USD |
| `1H` | `BingX` | `30.13%` | `69.87%` | `0.43` | 682,720.00 USD |
| `1H` | `MEXC` | `46.48%` | `53.52%` | `0.87` | 1,950,000.00 USD |
| `1H` | `Bitunix` | `38.35%` | `61.65%` | `0.62` | 1,030,000.00 USD |
| `1H` | `Hyperliquid` | `69.24%` | `30.76%` | `2.25` | 601,770.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `56.75%` | `43.25%` | `1.31` | 331,900.00 USD |
| `1H` | `Crypto.com` | `24.67%` | `75.33%` | `0.33` | 60,620.00 USD |
| `1H` | `WhiteBIT` | `22.22%` | `77.78%` | `0.29` | 1,310,000.00 USD |
| `1H` | `HTX` | `51.78%` | `48.22%` | `1.07` | 162,340.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.64%` | `58.36%` | `0.71` | 205,150.00 USD |
| `1H` | `Aster` | `37.65%` | `62.35%` | `0.60` | 247,220.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `89.85%` | `10.15%` | `8.85` | 4,530.00 USD |
| `1H` | `Whale Positions` | `41.76%` | `58.24%` | `0.72` | 16,880,000.00 USD |
| `1H` | `Global Accounts` | `42.01%` | `57.99%` | `0.72` | 45,350,000.00 USD |
| `4H` | `DOGE` | `45.81%` | `54.19%` | `0.85` | 165,430,000.00 USD |
| `4H` | `Binance` | `45.81%` | `54.19%` | `0.85` | 62,700,000.00 USD |
| `4H` | `OKX` | `46.67%` | `53.33%` | `0.88` | 33,660,000.00 USD |
| `4H` | `Bybit` | `42.98%` | `57.02%` | `0.75` | 10,770,000.00 USD |
| `4H` | `KuCoin` | `45.31%` | `54.69%` | `0.83` | 1,060,000.00 USD |
| `4H` | `Gate` | `46.86%` | `53.14%` | `0.88` | 27,320,000.00 USD |
| `4H` | `Bitget` | `40.96%` | `59.04%` | `0.69` | 3,370,000.00 USD |
| `4H` | `BingX` | `35.68%` | `64.32%` | `0.55` | 2,860,000.00 USD |
| `4H` | `MEXC` | `47.39%` | `52.61%` | `0.90` | 11,800,000.00 USD |
| `4H` | `Bitunix` | `49.63%` | `50.37%` | `0.99` | 4,370,000.00 USD |
| `4H` | `Hyperliquid` | `56.71%` | `43.29%` | `1.31` | 1,160,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.62%` | `49.38%` | `1.03` | 1,160,000.00 USD |
| `4H` | `Crypto.com` | `35.58%` | `64.42%` | `0.55` | 190,420.00 USD |
| `4H` | `WhiteBIT` | `25.95%` | `74.05%` | `0.35` | 2,650,000.00 USD |
| `4H` | `HTX` | `62.64%` | `37.36%` | `1.68` | 1,250,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `41.79%` | `58.21%` | `0.72` | 207,230.00 USD |
| `4H` | `Aster` | `45.15%` | `54.85%` | `0.82` | 886,240.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `57.65%` | `42.35%` | `1.36` | 22,520.00 USD |
| `4H` | `Whale Positions` | `45.81%` | `54.19%` | `0.85` | 62,700,000.00 USD |
| `4H` | `Global Accounts` | `45.81%` | `54.19%` | `0.85` | 165,430,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.0765` | `0.0766` | `0.0765` | `0.0768` | `0.0764` | 2,886,151.65 USD | 1,339,966.04 USD | 1,546,185.61 USD | -206,219.57 USD | `-7.15%` | `9B / 10S` |
| `5:00 UTC` | `0.0764` | `0.0763` | `0.0764` | `0.0765` | `0.0762` | 2,912,003.24 USD | 1,404,159.00 USD | 1,507,844.23 USD | -103,685.23 USD | `-3.56%` | `5B / 8S` |
| `0:00 UTC` | `0.0762` | `0.0763` | `0.0762` | `0.0765` | `0.0761` | 2,910,679.71 USD | 1,025,736.40 USD | 1,884,943.31 USD | -859,206.91 USD | `-29.52%` | `0B / 13S` |
| `5:00 UTC` | `0.0762` | `0.0762` | `0.0762` | `0.0763` | `0.0760` | 2,543,107.52 USD | 868,277.41 USD | 1,674,830.11 USD | -806,552.70 USD | `-31.72%` | `2B / 3S` |
| `0:00 UTC` | `0.0759` | `0.0758` | `0.0759` | `0.0763` | `0.0755` | 6,345,196.06 USD | 2,713,125.81 USD | 3,632,070.25 USD | -918,944.44 USD | `-14.48%` | `8B / 18S` |
| `5:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0758` | `0.0755` | 3,504,858.24 USD | 1,671,375.40 USD | 1,833,482.84 USD | -162,107.45 USD | `-4.63%` | `6B / 5S` |
| `0:00 UTC` | `0.0756` | `0.0756` | `0.0756` | `0.0759` | `0.0755` | 6,252,708.50 USD | 2,400,535.02 USD | 3,852,173.48 USD | -1,451,638.46 USD | `-23.22%` | `9B / 7S` |
| `5:00 UTC` | `0.0758` | `0.0759` | `0.0758` | `0.0761` | `0.0758` | 3,515,276.40 USD | 1,545,960.58 USD | 1,969,315.82 USD | -423,355.24 USD | `-12.04%` | `4B / 6S` |
| `0:00 UTC` | `0.0757` | `0.0757` | `0.0757` | `0.0759` | `0.0755` | 2,056,025.64 USD | 709,276.38 USD | 1,346,749.25 USD | -637,472.87 USD | `-31.01%` | `2B / 13S` |
| `5:00 UTC` | `0.0754` | `0.0755` | `0.0754` | `0.0757` | `0.0753` | 2,805,117.52 USD | 1,373,657.36 USD | 1,431,460.16 USD | -57,802.80 USD | `-2.06%` | `8B / 2S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:51` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0795` | 0.00 USD | 0.00 USD |
| `10-28 20:12` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0790` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0785` | 0.00 USD | 0.00 USD |
| `10-28 19:47` | `Volume 100M DOGE` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0785` | 0.00 USD | 0.00 USD |
| `10-28 19:19` | `Volume 100M DOGE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.0786` | 17,000,000.00 USD | 0.00 USD |
| `10-28 17:27` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0799` | 0.00 USD | 0.00 USD |
| `10-28 16:36` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0800` | 0.00 USD | 0.00 USD |
| `10-28 16:07` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0803` | 0.00 USD | 0.00 USD |
| `10-28 15:16` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0806` | 0.00 USD | 0.00 USD |
| `10-28 15:13` | `Volume 100M DOGE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0806` | 0.00 USD | 0.00 USD |
| `10-28 13:51` | `Volume 100M DOGE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0804` | 0.00 USD | 0.00 USD |
| `10-28 13:31` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0802` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 100M DOGE` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0797` | 0.00 USD | 0.00 USD |
| `10-28 07:56` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0793` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0795` | 0.00 USD | 0.00 USD |
| `10-28 07:07` | `Range 0.0002` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.0794` | 74,000,000.00 USD | 0.00 USD |
| `10-28 06:32` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0790` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 1,280.00 USD | -113,150.00 USD | **`DISTRIBUTION`** |
| `15m` | -225,350.00 USD | -1,820,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -450,730.00 USD | -2,840,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 412,610.00 USD | -5,670,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -168,350.00 USD | -10,250,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 175,480.00 USD | -9,220,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 1,390,000.00 USD | -7,290,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 3,660,000.00 USD | -30,980,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,010,000.00 USD | -26,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -17,020,000.00 USD | -66,480,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -61,660,000.00 USD | -198,460,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -283,510,000.00 USD | -807,030,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.28K` | 15m=`-225.35K` | 1h=`+412.61K` | 24h=`-17.02M`
* Futures Capital Netflows: 5m=`-113.15K` | 15m=`-1.82M` | 1h=`-5.67M` | 24h=`-66.48M`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0736` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0699` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0841`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0756` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0792` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0651`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0760`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
