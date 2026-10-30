# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 11:44:30 IST` (`2026-10-30 06:14:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0752` | **Live Ask Quote**: `0.0773` | **Mid Price**: `0.0762`
- **Spread Points**: `21.00` | **Spread BPS**: `275.41 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0734` | VWAP Z-Score: `+1.52` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000520` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.03` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0764` | Lower -3.00σ Band: `0.0704`
  * Upper +2.51σ Band: `0.0759` | Lower -2.51σ Band: `0.0709`
  * Upper +2.01σ Band: `0.0754` | Lower -2.01σ Band: `0.0714`
  * Upper +2.00σ Band: `0.0754` | Lower -2.00σ Band: `0.0714`
  * Upper +1.28σ Band: `0.0747` | Lower -1.28σ Band: `0.0721`
  * Upper +1.00σ Band: `0.0744` | Lower -1.00σ Band: `0.0724`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0749` | EMA-20=`0.0746` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0752` (Slope: `+0.0000`) | EMA-100=`0.0760`
  * Institutional Anchors: EMA-144=`0.0764` | EMA-200=`0.0766` (Slope: `-0.2992`) | EMA-233=`0.0768`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0757` (Distance: `+0.70%`)
  * Point of Control (POC) = `0.0749` (Distance: `+1.82%`)
  * Value Area Low (VAL) = `0.0733` (Distance: `+4.00%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0783` | Weekly POC=`0.0762` | Weekly VAL=`0.0748`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0754` | Low=`0.0749`
  * New York Session (13:00-21:00 UTC): High=`0.0767` | Low=`0.0758`
  * Initial Balance (First Hour): IB High=`0.0754` | IB Low=`0.0749`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0759` - `0.0766`
  * Optimal Trade Entry (OTE 0.705): `0.0764`
  * Structural Invalidation Anchor (0.786): `0.0769`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0761` | `0.0762` | `0.0760` | `0.0761` | `19,808,243` | 1,508,221.43 USD | 19,411.04 USD | `+1.29%` | -33,830,387.62 USD | `+0.22` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.0761` | `0.0763` | `0.0761` | `0.0762` | `8,366,626` | 637,404.84 USD | 64,916.18 USD | `+10.18%` | -33,765,471.44 USD | `+0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.0762` | `0.0764` | `0.0762` | `0.0764` | `10,359,903` | 790,298.31 USD | 212,772.85 USD | `+26.92%` | -33,552,698.59 USD | `+1.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0764` | `0.0766` | `0.0763` | `0.0764` | `33,619,692` | 2,569,719.99 USD | 71,103.82 USD | `+2.77%` | -33,250,284.47 USD | `+0.05` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.0764` | `0.0765` | `0.0761` | `0.0761` | `37,877,086` | 2,887,550.28 USD | -599,514.19 USD | `-20.76%` | -33,849,798.67 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.0761` | `0.0764` | `0.0760` | `0.0764` | `38,492,799` | 2,932,718.26 USD | 293,893.76 USD | `+10.02%` | -33,555,904.91 USD | `+0.45` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.0760` | `0.0764` | `0.0756` | `0.0761` | `219,497,371` | 16,694,978.29 USD | -1,885,253.58 USD | `-11.29%` | -33,632,818.63 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0761` | `0.0766` | `0.0761` | `0.0761` | `168,076,893` | 12,832,447.15 USD | -293,413.94 USD | `-2.29%` | -33,926,232.57 USD | `+0.28` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.0761` | `0.0764` | `0.0760` | `0.0764` | `38,536,120` | 2,936,027.55 USD | 297,203.05 USD | `+10.12%` | -33,629,029.52 USD | `+0.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -24,481,648.11 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -29,910,488.74 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0766` | `0.0756` | `0.0764` | `426,067,063` | 32,460,143.71 USD | -1,884,773.76 USD | `-5.81%` | -31,795,262.51 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | 1,565,746.91 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -1,441,921.89 USD | `-0.70` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -24,481,648.11 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0761` | `0.0722` | `0.0760` | `2,066,208,508` | 153,107,709.84 USD | -5,428,840.63 USD | `-3.55%` | -29,910,488.74 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0760` | `0.0766` | `0.0756` | `0.0764` | `426,067,063` | 32,460,143.71 USD | -1,884,773.76 USD | `-5.81%` | -31,795,262.51 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.0762`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.0763` | `3000.0000` | 229.05 USD | 3,310.45 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0763` | `52915.0000` | 4,039.80 USD | 7,350.25 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0763` | `147175.0000` | 11,235.93 USD | 18,586.18 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0763` | `60466.0000` | 4,616.16 USD | 23,202.33 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `0.0763` | `406461.0000` | 31,030.05 USD | 54,232.38 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0763` | `39540.0000` | 3,018.33 USD | 57,250.70 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `0.0763` | `91700.0000` | 6,999.83 USD | 64,250.53 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0763` | `39744.0000` | 3,033.78 USD | 67,284.31 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0763` | `15399.0000` | 1,175.44 USD | 68,459.75 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0763` | `594735.0000` | 45,396.72 USD | 113,856.46 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0763` | `15398.0000` | 1,175.31 USD | 115,031.78 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0763` | `50922.0000` | 3,886.72 USD | 118,918.50 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0763` | `140469.0000` | 10,720.88 USD | 129,639.38 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `0.0763` | `59172.0000` | 4,516.01 USD | 134,155.38 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.0763` | `15399.0000` | 1,175.24 USD | 135,330.62 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0763` | `72740.0000` | 5,551.37 USD | 140,881.99 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.0763` | `147228.0000` | 11,236.00 USD | 152,117.99 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0763` | `24650.0000` | 1,881.16 USD | 153,999.15 USD | `2 orders` | `-0.07%` | `-` |
| `ASK` | `0.0764` | `3888.0000` | 297.05 USD | 159,719.67 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0764` | `55081.0000` | 4,208.24 USD | 159,422.62 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0764` | `190975.0000` | 14,590.49 USD | 155,214.38 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `0.0764` | `15399.0000` | 1,176.42 USD | 140,623.89 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0764` | `2666.0000` | 203.67 USD | 139,447.46 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0764` | `472203.0000` | 36,072.53 USD | 139,243.80 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0764` | `11549.0000` | 882.24 USD | 103,171.27 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0764` | `71634.0000` | 5,472.05 USD | 102,289.03 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0764` | `424892.0000` | 32,456.65 USD | 96,816.98 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0764` | `169818.0000` | 12,971.89 USD | 64,360.33 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `0.0764` | `35034.0000` | 2,676.07 USD | 51,388.44 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0764` | `128421.0000` | 9,809.18 USD | 48,712.37 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0764` | `218301.0000` | 16,674.27 USD | 38,903.19 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `0.0764` | `48305.0000` | 3,689.54 USD | 22,228.92 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0764` | `35037.0000` | 2,676.09 USD | 18,539.38 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0764` | `81979.0000` | 6,261.39 USD | 15,863.29 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0764` | `1034.0000` | 78.97 USD | 9,601.90 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0764` | `15399.0000` | 1,176.07 USD | 9,522.93 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0764` | `32384.0000` | 2,473.17 USD | 8,346.86 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `0.0764` | `76914.0000` | 5,873.69 USD | 5,873.69 USD | `8 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0764` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0764` | `24345.0000` | 1,859.13 USD | 1,859.13 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0764` | `16008.0000` | 1,222.27 USD | 3,081.41 USD | `1 orders` | `-0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `303` | `0xb83d...6e36` | `SHORT` | 7,812,586.64 USD | `102,645,925.00` | `0.0946` | `0.0761` | `1.31` | 1,894,755.01 USD | `+24.25%` | `3X Cross` |
| `310` | `0xc63a...a3cd` | `LONG` | 7,609,700.00 USD | `100,000,000.00` | `0.0856` | `0.0761` | `0.000000` | -955,121.96 USD | `-12.55%` | `10X Cross` |
| `311` | `0x610b...b613` | `LONG` | 7,510,586.86 USD | `98,666,424.00` | `0.0872` | `0.0761` | `0.0600` | -1,089,595.04 USD | `-14.51%` | `5X Cross` |
| `602` | `0x5b5d...c060` | `SHORT` | 3,768,812.00 USD | `49,478,955.00` | `0.0946` | `0.0761` | `3.20` | 912,704.60 USD | `+24.22%` | `3X Cross` |
| `634` | `0xca49...53c8` | `SHORT` | 3,541,755.96 USD | `46,542,649.00` | `0.0929` | `0.0761` | `0.3868` | 784,288.72 USD | `+22.14%` | `10X Cross` |
| `650` | `0x45d2...4029` | `SHORT` | 3,456,555.19 USD | `45,426,000.00` | `0.0954` | `0.0761` | `0.9575` | 879,074.03 USD | `+25.43%` | `10X Cross` |
| `688` | `0xecb6...2b00` | `SHORT` | 3,277,274.25 USD | `43,037,088.00` | `0.0789` | `0.0761` | `0.7207` | 117,162.96 USD | `+3.58%` | `10X Cross` |
| `1185` | `0x458d...ab3b` | `LONG` | 1,861,369.91 USD | `24,454,063.00` | `0.1002` | `0.0761` | `0.0714` | -589,551.99 USD | `-31.67%` | `3X Isolated` |
| `1204` | `0xeadc...9d55` | `LONG` | 1,852,259.40 USD | `24,317,440.00` | `0.0926` | `0.0761` | `0.000000` | -399,335.17 USD | `-21.56%` | `10X Cross` |
| `1334` | `0xf48f...10fe` | `LONG` | 1,630,661.32 USD | `21,424,497.00` | `0.0968` | `0.0761` | `0.0448` | -443,643.29 USD | `-27.21%` | `4X Cross` |
| `1416` | `0x9946...0852` | `SHORT` | 1,526,214.20 USD | `20,059,331.00` | `0.0863` | `0.0761` | `0.1513` | 205,071.87 USD | `+13.44%` | `10X Cross` |
| `1554` | `0xcac1...26b3` | `SHORT` | 1,379,198.37 USD | `18,126,835.00` | `0.0943` | `0.0761` | `0.5453` | 330,260.83 USD | `+23.95%` | `10X Cross` |
| `1560` | `0x9aa5...58af` | `SHORT` | 1,370,110.50 USD | `18,004,790.00` | `0.0907` | `0.0761` | `0.5732` | 262,356.70 USD | `+19.15%` | `10X Cross` |
| `1588` | `0x0d6a...ca57` | `LONG` | 1,341,602.37 USD | `17,626,455.00` | `0.0875` | `0.0761` | `0.0626` | -200,502.59 USD | `-14.95%` | `3X Isolated` |
| `1644` | `0x4808...a82c` | `LONG` | 1,281,126.53 USD | `16,828,143.00` | `0.0883` | `0.0761` | `0.0632` | -205,346.45 USD | `-16.03%` | `3X Cross` |
| `1775` | `0x31ef...f715` | `LONG` | 1,159,589.51 USD | `15,230,102.00` | `0.0936` | `0.0761` | `0.0668` | -266,106.42 USD | `-22.95%` | `3X Isolated` |
| `1796` | `0xbfc7...80b4` | `SHORT` | 1,143,472.60 USD | `15,020,000.00` | `0.0920` | `0.0761` | `0.1776` | 238,926.69 USD | `+20.89%` | `10X Cross` |
| `1885` | `0x7cee...fc93` | `SHORT` | 1,066,999.47 USD | `14,013,468.00` | `0.0863` | `0.0761` | `0.2656` | 141,877.90 USD | `+13.30%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0775` | 7,049.87 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 7.05K USD at 0.0775 USD [API] | `2026-10-29 04:08:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0781` | 10,726.88 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.73K USD at 0.0781 USD [API] | `2026-10-29 04:41:36` |
| `ANNOUNCEMENT` | `INFO` | `0.0789` | 5,299.40 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 5.30K USD at 0.0789 USD [API] | `2026-10-29 05:13:28` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+1.49%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--5.26%`)
  * 48H Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+1.49%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--5.26%`)
  * 3D Horizon: Short MP=`0.0776` (Vol: 1,100,000.00 USD, Dist: `+1.49%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--5.26%`)
  * 7D Horizon: Short MP=`0.0818` (Vol: 1,100,000.00 USD, Dist: `+6.96%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--5.26%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0152` | 1,700.00 USD | 16,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0154` | 1,150.00 USD | 16,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0168` | 993.56 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0184` | 111.04 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0186` | 596.80 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0188` | 102.39 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0213` | 335.64 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 18,970.00 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0216` | 675.61 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0230` | 20,510.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0242` | 780.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0244` | 954.75 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0250` | 3,970.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0253` | 3,870.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0255` | 902.38 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0255` | 50,820.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0261` | 972.81 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0262` | 140.28 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0283` | 487.68 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0307` | 265.80 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0309` | 434.45 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0312` | 5,870.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0323` | 741.75 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 393.23 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 4,540.00 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0340` | 138.01 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0347` | 13,500.00 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 3,530.00 USD | 16,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0360` | 8,390.00 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0362` | 34,440.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0365` | 19,200.00 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0367` | 723.91 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0372` | 1,760.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0374` | 169.09 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0379` | 178.36 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 1,600.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0382` | 204.60 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0384` | 301.87 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 2,180.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0399` | 4,990.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0403` | 56,710.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 41,800.00 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 558.80 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0411` | 4,750.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0418` | 923.89 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 455.06 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 883.34 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 38,970.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0428` | 115,570.00 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 924,470.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 10,120.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0437` | 751.83 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 2,620.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,180.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 2,250.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0442` | 1,140.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0442` | 1,190.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 15,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 92,730.00 USD | 15,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 810.81 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 11,010.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0462` | 13,410.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 14,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 14,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0467` | 2,340.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 1,600.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 1,420.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 58,890.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 261.03 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 1,780.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 4,610.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,380.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0493` | 246.25 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0493` | 4,780.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 655.79 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 40,280.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0502` | 26,180.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 14,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,880.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 309.15 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 6,570.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 4,950.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 4,420.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 275,090.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 25,040.00 USD | 14,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 6,280.00 USD | 14,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 4,520.00 USD | 14,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 3,340.00 USD | 14,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 182,040.00 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 9,840.00 USD | 14,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 8,100.00 USD | 14,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 42,580.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 930.83 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 2,070.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 337.91 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 3,030.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 3,230.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 892.81 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0549` | 3,960.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 1,760.00 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 464.34 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 8,410.00 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 144.08 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 40,620.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 568.50 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 315.67 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 814.04 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 6,380.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 7,630.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,940.00 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 441.75 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 582.50 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 16,730.00 USD | 13,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 5,840.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 358.03 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 305.15 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 1,230.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 30,340.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 546.26 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,140.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,300.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 5,890,000.00 USD | 13,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 2,510.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 8,560.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 24,120.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 830.97 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 1,510.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,470.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 622.63 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,220.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 717.73 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 5,110.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0611` | 359,500.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 629.72 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 2,670.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 11,100.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 345.86 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 194.66 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 43,420.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 1,250.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 2,430.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,310,000.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 3,260.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 4,770.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 5,600.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,990.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 748.55 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 3,270.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 733.80 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 76,280.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 27,310.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 631.94 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 163,150.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 8,800.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 7,790.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0657` | 14,160.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 9,600.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 12,560.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 17,410.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 4,070.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 9,150.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,150,000.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,180.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,050.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 15,370.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 112,780.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 12,610.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 68,070.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 15,450,000.00 USD | 15,450,000.00 USD | 49,820.00 USD | 47,880.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 15,340,000.00 USD | 15,340,000.00 USD | 17,070.00 USD | 27,520.00 USD | 139,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0682` | 49,480.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 15,160,000.00 USD | 15,160,000.00 USD | 2,550.00 USD | 33,950.00 USD | 20,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 15,100,000.00 USD | 15,100,000.00 USD | 15,780.00 USD | 26,860.00 USD | 467.62 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0684` | 15,060,000.00 USD | 15,060,000.00 USD | 24,150.00 USD | 15,070.00 USD | 899.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 80,430.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 15,020,000.00 USD | 15,020,000.00 USD | 58,140.00 USD | 13,720.00 USD | 22,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 13,120.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 14,920,000.00 USD | 14,920,000.00 USD | 45,490.00 USD | 8,860.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 595.81 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 14,850,000.00 USD | 14,850,000.00 USD | 9,250.00 USD | 24,710.00 USD | 29,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 14,790,000.00 USD | 14,790,000.00 USD | 6,710.00 USD | 4,630.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 1,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0689` | 14,750,000.00 USD | 14,750,000.00 USD | 9,350.00 USD | 0.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0690` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0691` | 6,960.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 14,730,000.00 USD | 14,730,000.00 USD | 1,460.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 14,730,000.00 USD | 14,730,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,970.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0693` | 14,710,000.00 USD | 14,710,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0694` | 14,690,000.00 USD | 14,690,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,980.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 14,660,000.00 USD | 14,660,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 14,660,000.00 USD | 14,660,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 6,680.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 14,600,000.00 USD | 14,600,000.00 USD | 14,010.00 USD | 10,800.00 USD | 9,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 2,910.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 14,560,000.00 USD | 14,560,000.00 USD | 83,570.00 USD | 27,620.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 14,420,000.00 USD | 14,420,000.00 USD | 141,150.00 USD | 21,100.00 USD | 37,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 14,220,000.00 USD | 14,220,000.00 USD | 51,480.00 USD | 115,140.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 11,430.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 14,040,000.00 USD | 14,040,000.00 USD | 87,840.00 USD | 36,120.00 USD | 59.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 1,070.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 13,910,000.00 USD | 13,910,000.00 USD | 175,640.00 USD | 66,830.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 4,360.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 13,650,000.00 USD | 13,650,000.00 USD | 24,140.00 USD | 45,140.00 USD | 22,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 13,560,000.00 USD | 13,560,000.00 USD | 40,970.00 USD | 30,720.00 USD | 55,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 13,430,000.00 USD | 13,430,000.00 USD | 21,850.00 USD | 1,120.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 423.90 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 13,400,000.00 USD | 13,400,000.00 USD | 140,160.00 USD | 69,310.00 USD | 45,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 13,140,000.00 USD | 13,140,000.00 USD | 69,400.00 USD | 62,000.00 USD | 107,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0708` | 428.57 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0709` | 12,900,000.00 USD | 12,900,000.00 USD | 36,870.00 USD | 82,010.00 USD | 148,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 821.60 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 12,630,000.00 USD | 12,630,000.00 USD | 117,230.00 USD | 91,550.00 USD | 119,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 4,720.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 12,300,000.00 USD | 12,300,000.00 USD | 46,900.00 USD | 25,670.00 USD | 43,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 1,860.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 12,190,000.00 USD | 12,190,000.00 USD | 159,040.00 USD | 46,690.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 802.06 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 11,980,000.00 USD | 11,980,000.00 USD | 70,910.00 USD | 85,230.00 USD | 63,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 11,760,000.00 USD | 11,760,000.00 USD | 118,420.00 USD | 51,930.00 USD | 48,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 5,410.00 USD | 398,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 11,540,000.00 USD | 11,540,000.00 USD | 73,470.00 USD | 238,460.00 USD | 43,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 392,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 11,190,000.00 USD | 11,190,000.00 USD | 19,480.00 USD | 51,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,170.00 USD | 384,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 11,120,000.00 USD | 11,120,000.00 USD | 232,360.00 USD | 96,160.00 USD | 137.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 22,270.00 USD | 383,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 10,790,000.00 USD | 10,790,000.00 USD | 55,690.00 USD | 101,030.00 USD | 13,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 1,600.00 USD | 361,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 10,620,000.00 USD | 10,620,000.00 USD | 226,040.00 USD | 45,330.00 USD | 72,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 359,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 10,270,000.00 USD | 10,270,000.00 USD | 135,290.00 USD | 50,600.00 USD | 72,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 12,310.00 USD | 357,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 10,020,000.00 USD | 10,020,000.00 USD | 308,410.00 USD | 298,040.00 USD | 67,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 22,360.00 USD | 345,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 9,340,000.00 USD | 9,340,000.00 USD | 179,490.00 USD | 119,590.00 USD | 149,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 322,260.00 USD | 322,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 8,890,000.00 USD | 8,890,000.00 USD | 82,600.00 USD | 258,330.00 USD | 326,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 626.77 USD | 626.77 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 8,230,000.00 USD | 8,230,000.00 USD | 111,400.00 USD | 206,000.00 USD | 370,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0725` | 7,540,000.00 USD | 7,540,000.00 USD | 234,040.00 USD | 201,810.00 USD | 268,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 6,830,000.00 USD | 6,830,000.00 USD | 29,310.00 USD | 90,560.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0727` | 120.82 USD | 120.82 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 6,700,000.00 USD | 6,700,000.00 USD | 138,060.00 USD | 83,300.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 6,470,000.00 USD | 6,470,000.00 USD | 27,890.00 USD | 84,500.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 6,320,000.00 USD | 6,320,000.00 USD | 42,630.00 USD | 26,380.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 6,250,000.00 USD | 6,250,000.00 USD | 105,290.00 USD | 26,630.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 6,070,000.00 USD | 6,070,000.00 USD | 35,610.00 USD | 68,840.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 5,950,000.00 USD | 5,950,000.00 USD | 65,770.00 USD | 40,460.00 USD | 80,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 5,760,000.00 USD | 5,760,000.00 USD | 36,920.00 USD | 69,930.00 USD | 28,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 5,630,000.00 USD | 5,630,000.00 USD | 339,370.00 USD | 67,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 5,220,000.00 USD | 5,220,000.00 USD | 141,790.00 USD | 23,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 5,060,000.00 USD | 5,060,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 4,810,000.00 USD | 4,810,000.00 USD | 113,510.00 USD | 47,850.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 4,600,000.00 USD | 4,600,000.00 USD | 83,080.00 USD | 23,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 4,490,000.00 USD | 4,490,000.00 USD | 54,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 4,440,000.00 USD | 4,440,000.00 USD | 54,250.00 USD | 0.00 USD | 34,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 68,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 133,790.00 USD | 24,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 4,120,000.00 USD | 4,120,000.00 USD | 174,420.00 USD | 40,680.00 USD | 245,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,660,000.00 USD | 3,660,000.00 USD | 185,610.00 USD | 89,270.00 USD | 107,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 3,280,000.00 USD | 3,280,000.00 USD | 54,460.00 USD | 32,770.00 USD | 34,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 3,160,000.00 USD | 3,160,000.00 USD | 71,220.00 USD | 64,390.00 USD | 189,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 2,830,000.00 USD | 2,830,000.00 USD | 643,140.00 USD | 225,930.00 USD | 178,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,790,000.00 USD | 1,790,000.00 USD | 130,110.00 USD | 43,650.00 USD | 233,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 1,380,000.00 USD | 1,380,000.00 USD | 73,840.00 USD | 38,480.00 USD | 125,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 37,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0752` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 12,650.00 USD | 141,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0754` | 926,030.00 USD | 926,030.00 USD | 0.00 USD | 103,430.00 USD | 278,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0755` | 544,220.00 USD | 544,220.00 USD | 182,850.00 USD | 180,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0756` | 181,360.00 USD | 181,360.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0757` | 151,260.00 USD | 151,260.00 USD | 130,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0758` | 20,690.00 USD | 20,690.00 USD | 15,180.00 USD | 4,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0759` | 581.36 USD | 581.36 USD | 0.00 USD | 0.00 USD | 160.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0761` | 420.80 USD | 420.80 USD | 0.00 USD | 0.00 USD | 420.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0762` | 168.86 USD | 168.86 USD | 0.00 USD | 0.00 USD | 168.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0762` | 337.72 USD | 337.72 USD | 0.00 USD | 0.00 USD | 168.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0763` | 51,500.00 USD | 51,500.00 USD | 4,000.00 USD | 47,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 83,840.00 USD | 83,840.00 USD | 17,520.00 USD | 14,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 666,050.00 USD | 666,050.00 USD | 233,890.00 USD | 248,870.00 USD | 99,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 1,820,000.00 USD | 1,820,000.00 USD | 586,470.00 USD | 522,700.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 2,560,000.00 USD | 2,560,000.00 USD | 246,530.00 USD | 337,770.00 USD | 159,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 3,470,000.00 USD | 3,470,000.00 USD | 224,320.00 USD | 93,770.00 USD | 594,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 4,440,000.00 USD | 4,440,000.00 USD | 259,990.00 USD | 421,270.00 USD | 287,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 5,420,000.00 USD | 5,420,000.00 USD | 396,020.00 USD | 179,710.00 USD | 403,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 6,140,000.00 USD | 6,140,000.00 USD | 223,340.00 USD | 343,810.00 USD | 149,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 7,410,000.00 USD | 7,410,000.00 USD | 390,170.00 USD | 170,860.00 USD | 709,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 7,970,000.00 USD | 7,970,000.00 USD | 129,080.00 USD | 228,140.00 USD | 204,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 8,310,000.00 USD | 8,310,000.00 USD | 86,950.00 USD | 217,280.00 USD | 36,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0775` | 8,740,000.00 USD | 8,740,000.00 USD | 255,450.00 USD | 123,530.00 USD | 48,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 361.76 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 9,310,000.00 USD | 9,310,000.00 USD | 267,580.00 USD | 189,880.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 10,030,000.00 USD | 10,030,000.00 USD | 276,300.00 USD | 301,970.00 USD | 145,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 10,790,000.00 USD | 10,790,000.00 USD | 88,720.00 USD | 274,410.00 USD | 395,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 11,440,000.00 USD | 11,440,000.00 USD | 296,890.00 USD | 158,150.00 USD | 199,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0780` | 3,490.00 USD | 3,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0780` | 11,710,000.00 USD | 11,710,000.00 USD | 174,020.00 USD | 53,140.00 USD | 39,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 12,070,000.00 USD | 12,070,000.00 USD | 151,030.00 USD | 193,800.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 12,300,000.00 USD | 12,300,000.00 USD | 70,430.00 USD | 82,140.00 USD | 79,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 12,740,000.00 USD | 12,740,000.00 USD | 45,800.00 USD | 214,890.00 USD | 177,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 13,190,000.00 USD | 13,190,000.00 USD | 316,220.00 USD | 101,430.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 13,590,000.00 USD | 13,590,000.00 USD | 205,570.00 USD | 110,520.00 USD | 78,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 14,230,000.00 USD | 14,230,000.00 USD | 234,330.00 USD | 160,700.00 USD | 245,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 15,300,000.00 USD | 15,300,000.00 USD | 329,770.00 USD | 386,280.00 USD | 358,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 3,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 15,730,000.00 USD | 15,730,000.00 USD | 135,470.00 USD | 191,940.00 USD | 104,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 16,350,000.00 USD | 16,350,000.00 USD | 296,490.00 USD | 218,540.00 USD | 102,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 16,570,000.00 USD | 16,570,000.00 USD | 136,170.00 USD | 58,560.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 16,990,000.00 USD | 16,990,000.00 USD | 188,560.00 USD | 121,290.00 USD | 110,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 17,250,000.00 USD | 17,250,000.00 USD | 158,350.00 USD | 37,510.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0793` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 41.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0794` | 17,540,000.00 USD | 17,540,000.00 USD | 128,100.00 USD | 63,190.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 104.72 USD | 4,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0795` | 17,720,000.00 USD | 17,720,000.00 USD | 61,440.00 USD | 19,240.00 USD | 100,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 17,910,000.00 USD | 17,910,000.00 USD | 174,010.00 USD | 0.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 18,320,000.00 USD | 18,320,000.00 USD | 206,810.00 USD | 89,760.00 USD | 115,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 18,490,000.00 USD | 18,490,000.00 USD | 56,190.00 USD | 110,930.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 18,980,000.00 USD | 18,980,000.00 USD | 157,480.00 USD | 193,600.00 USD | 142,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 19,130,000.00 USD | 19,130,000.00 USD | 45,460.00 USD | 9,760.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0801` | 19,150,000.00 USD | 19,150,000.00 USD | 17,000.00 USD | 0.00 USD | 617.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 19,170,000.00 USD | 19,170,000.00 USD | 18,910.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 19,270,000.00 USD | 19,270,000.00 USD | 16,230.00 USD | 43,340.00 USD | 41,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 19,290,000.00 USD | 19,290,000.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0805` | 19,460,000.00 USD | 19,460,000.00 USD | 89,620.00 USD | 37,230.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 19,720,000.00 USD | 19,720,000.00 USD | 24,270.00 USD | 21,040.00 USD | 215,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 20,110,000.00 USD | 20,110,000.00 USD | 221,690.00 USD | 145,040.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 20,990,000.00 USD | 20,990,000.00 USD | 297,680.00 USD | 118,270.00 USD | 458,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 21,530,000.00 USD | 21,530,000.00 USD | 252,300.00 USD | 275,640.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 22,070,000.00 USD | 22,070,000.00 USD | 252,220.00 USD | 157,180.00 USD | 132,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 22,410,000.00 USD | 22,410,000.00 USD | 98,200.00 USD | 229,260.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 22,730,000.00 USD | 22,730,000.00 USD | 138,630.00 USD | 102,020.00 USD | 77,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 22,920,000.00 USD | 22,920,000.00 USD | 47,380.00 USD | 33,440.00 USD | 109,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 23,270,000.00 USD | 23,270,000.00 USD | 39,620.00 USD | 109,560.00 USD | 200,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0814` | 118.92 USD | 4,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0815` | 23,400,000.00 USD | 23,400,000.00 USD | 33,530.00 USD | 6,740.00 USD | 94,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 24,120,000.00 USD | 24,120,000.00 USD | 340,210.00 USD | 194,310.00 USD | 179,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 24,670,000.00 USD | 24,670,000.00 USD | 284,640.00 USD | 134,560.00 USD | 130,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0818` | 25,340,000.00 USD | 25,340,000.00 USD | 247,200.00 USD | 161,260.00 USD | 268,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 4,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 25,940,000.00 USD | 25,940,000.00 USD | 161,320.00 USD | 312,480.00 USD | 128,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 26,490,000.00 USD | 26,490,000.00 USD | 52,420.00 USD | 172,050.00 USD | 319,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 26,780,000.00 USD | 26,780,000.00 USD | 156,680.00 USD | 48,110.00 USD | 85,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 27,340,000.00 USD | 27,340,000.00 USD | 252,350.00 USD | 151,600.00 USD | 156,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 27,690,000.00 USD | 27,690,000.00 USD | 270,020.00 USD | 72,540.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 28,260,000.00 USD | 28,260,000.00 USD | 168,680.00 USD | 204,930.00 USD | 190,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 28,510,000.00 USD | 28,510,000.00 USD | 102,430.00 USD | 125,690.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 28,930,000.00 USD | 28,930,000.00 USD | 131,950.00 USD | 125,260.00 USD | 170,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 29,020,000.00 USD | 29,020,000.00 USD | 13,110.00 USD | 62,110.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 29,360,000.00 USD | 29,360,000.00 USD | 197,110.00 USD | 75,940.00 USD | 66,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 29,610,000.00 USD | 29,610,000.00 USD | 157,080.00 USD | 88,230.00 USD | 361.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 29,750,000.00 USD | 29,750,000.00 USD | 57,230.00 USD | 37,820.00 USD | 43,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 29,810,000.00 USD | 29,810,000.00 USD | 31,420.00 USD | 0.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 8,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 30,120,000.00 USD | 30,120,000.00 USD | 154,910.00 USD | 75,990.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 500.17 USD | 8,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0833` | 30,490,000.00 USD | 30,490,000.00 USD | 110,470.00 USD | 82,770.00 USD | 170,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 30,840,000.00 USD | 30,840,000.00 USD | 119,430.00 USD | 94,190.00 USD | 138,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 31,200,000.00 USD | 31,200,000.00 USD | 111,520.00 USD | 183,090.00 USD | 64,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 31,450,000.00 USD | 31,450,000.00 USD | 44,050.00 USD | 63,220.00 USD | 144,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 8,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 31,670,000.00 USD | 31,670,000.00 USD | 132,640.00 USD | 31,430.00 USD | 56,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 10,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 31,960,000.00 USD | 31,960,000.00 USD | 169,750.00 USD | 77,480.00 USD | 39,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 32,060,000.00 USD | 32,060,000.00 USD | 52,570.00 USD | 24,710.00 USD | 30,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0840` | 32,140,000.00 USD | 32,140,000.00 USD | 18,280.00 USD | 20,110.00 USD | 34,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0841` | 32,150,000.00 USD | 32,150,000.00 USD | 9,490.00 USD | 2,010.00 USD | 608.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0842` | 32,220,000.00 USD | 32,220,000.00 USD | 22,710.00 USD | 0.00 USD | 46,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 264.21 USD | 10,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0843` | 32,250,000.00 USD | 32,250,000.00 USD | 33,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 32,310,000.00 USD | 32,310,000.00 USD | 59,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 426.71 USD | 11,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 11,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,450.00 USD | 15,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0868` | 155.98 USD | 15,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0871` | 138.58 USD | 15,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 16,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 16,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 17,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 17,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0905` | 6,760.00 USD | 24,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 1,310.00 USD | 25,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 4,940.00 USD | 30,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 30,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 5,000.00 USD | 35,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0934` | 249.24 USD | 35,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0940` | 915.67 USD | 36,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0944` | 39,700.00 USD | 76,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0945` | 192.21 USD | 76,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0946` | 47,330.00 USD | 124,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 24,460.00 USD | 148,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 761.26 USD | 149,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 149,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0964` | 2,820.00 USD | 152,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 121.23 USD | 152,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 153,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0984` | 1,190.00 USD | 154,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 162,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 165,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 165,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 171,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1062` | 3,290.00 USD | 175,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 175,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 178,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1095` | 1,940.00 USD | 180,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 181,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1137` | 147.86 USD | 181,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1158` | 131.49 USD | 181,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1202` | 116.04 USD | 181,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 637.53 USD | 182,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1229` | 2,330.00 USD | 184,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1252` | 1,330.00 USD | 185,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1253` | 904.18 USD | 186,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 186,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 186,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 189,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 189,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1330` | 34,350.00 USD | 223,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 223,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1341` | 45,880.00 USD | 269,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1364` | 136.31 USD | 269,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 270,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1407` | 22,830.00 USD | 293,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 3,760.00 USD | 296,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 196.63 USD | 297,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 15,300.00 USD | 312,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1446` | 144.55 USD | 312,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1451` | 1,820.00 USD | 314,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1461` | 23,490.00 USD | 337,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,180.00 USD | 346,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1484` | 2,980,000.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1489` | 483.17 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1494` | 448.05 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1497` | 2,100.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1507` | 56,440.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1512` | 1,320.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0152` | 16,570,000.00 USD | 0.00 USD | 1,700.00 USD | `-80.01%` | `111,254.00` |
| `Live` | `Long` | `0.0154` | 16,570,000.00 USD | 0.00 USD | 1,150.00 USD | `-79.88%` | `75,012.00` |
| `Live` | `Long` | `0.0160` | 16,570,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.96%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,560,000.00 USD | 0.00 USD | 407.02 USD | `-78.44%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,560,000.00 USD | 0.00 USD | 5,290.00 USD | `-78.31%` | `319,394.00` |
| `Live` | `Long` | `0.0168` | 16,560,000.00 USD | 0.00 USD | 993.56 USD | `-78.05%` | `59,317.00` |
| `Live` | `Long` | `0.0184` | 16,560,000.00 USD | 0.00 USD | 111.04 USD | `-75.95%` | `6,051.00` |
| `Live` | `Long` | `0.0186` | 16,560,000.00 USD | 0.00 USD | 596.80 USD | `-75.55%` | `32,000.00` |
| `Live` | `Long` | `0.0188` | 16,560,000.00 USD | 0.00 USD | 102.39 USD | `-75.29%` | `5,432.00` |
| `Live` | `Long` | `0.0213` | 16,560,000.00 USD | 0.00 USD | 335.64 USD | `-72.15%` | `15,795.00` |
| `Live` | `Long` | `0.0215` | 16,560,000.00 USD | 0.00 USD | 18,970.00 USD | `-71.75%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,540,000.00 USD | 0.00 USD | 675.61 USD | `-71.62%` | `31,206.00` |
| `Live` | `Long` | `0.0230` | 16,540,000.00 USD | 0.00 USD | 20,510.00 USD | `-69.92%` | `893,720.00` |
| `Live` | `Long` | `0.0242` | 16,520,000.00 USD | 0.00 USD | 780.00 USD | `-68.35%` | `32,298.00` |
| `Live` | `Long` | `0.0244` | 16,510,000.00 USD | 0.00 USD | 954.75 USD | `-67.95%` | `39,049.00` |
| `Live` | `Long` | `0.0250` | 16,510,000.00 USD | 0.00 USD | 3,970.00 USD | `-67.17%` | `158,606.00` |
| `Live` | `Long` | `0.0253` | 16,510,000.00 USD | 0.00 USD | 3,870.00 USD | `-66.90%` | `153,201.00` |
| `Live` | `Long` | `0.0255` | 16,510,000.00 USD | 0.00 USD | 902.38 USD | `-66.64%` | `35,457.00` |
| `Live` | `Long` | `0.0255` | 16,510,000.00 USD | 0.00 USD | 50,820.00 USD | `-66.51%` | `1,988,849.00` |
| `Live` | `Long` | `0.0261` | 16,450,000.00 USD | 0.00 USD | 972.81 USD | `-65.86%` | `37,344.00` |
| `Live` | `Long` | `0.0262` | 16,450,000.00 USD | 0.00 USD | 140.28 USD | `-65.59%` | `5,344.00` |
| `Live` | `Long` | `0.0279` | 16,450,000.00 USD | 0.00 USD | 1,730.00 USD | `-63.36%` | `61,775.00` |
| `Live` | `Long` | `0.0283` | 16,450,000.00 USD | 0.00 USD | 487.68 USD | `-62.97%` | `17,263.00` |
| `Live` | `Long` | `0.0306` | 16,450,000.00 USD | 0.00 USD | 137.41 USD | `-59.96%` | `4,498.00` |
| `Live` | `Long` | `0.0307` | 16,450,000.00 USD | 0.00 USD | 265.80 USD | `-59.69%` | `8,644.00` |
| `Live` | `Long` | `0.0309` | 16,450,000.00 USD | 0.00 USD | 434.45 USD | `-59.43%` | `14,037.00` |
| `Live` | `Long` | `0.0312` | 16,450,000.00 USD | 0.00 USD | 5,870.00 USD | `-59.04%` | `187,979.00` |
| `Live` | `Long` | `0.0323` | 16,440,000.00 USD | 0.00 USD | 741.75 USD | `-57.73%` | `23,000.00` |
| `Live` | `Long` | `0.0336` | 16,440,000.00 USD | 0.00 USD | 393.23 USD | `-55.89%` | `11,686.00` |
| `Live` | `Long` | `0.0338` | 16,440,000.00 USD | 0.00 USD | 4,540.00 USD | `-55.76%` | `134,443.00` |
| `Live` | `Long` | `0.0340` | 16,440,000.00 USD | 0.00 USD | 138.01 USD | `-55.50%` | `4,065.00` |
| `Live` | `Long` | `0.0347` | 16,440,000.00 USD | 0.00 USD | 13,500.00 USD | `-54.58%` | `389,633.00` |
| `Live` | `Long` | `0.0352` | 16,430,000.00 USD | 0.00 USD | 3,530.00 USD | `-53.80%` | `100,000.00` |
| `Live` | `Long` | `0.0358` | 16,420,000.00 USD | 0.00 USD | 214.53 USD | `-53.01%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,420,000.00 USD | 0.00 USD | 8,390.00 USD | `-52.88%` | `233,408.00` |
| `Live` | `Long` | `0.0362` | 16,410,000.00 USD | 0.00 USD | 34,440.00 USD | `-52.49%` | `950,000.00` |
| `Live` | `Long` | `0.0365` | 16,380,000.00 USD | 0.00 USD | 19,200.00 USD | `-52.22%` | `526,651.00` |
| `Live` | `Long` | `0.0367` | 16,360,000.00 USD | 0.00 USD | 723.91 USD | `-51.96%` | `19,752.00` |
| `Live` | `Long` | `0.0372` | 16,360,000.00 USD | 0.00 USD | 1,760.00 USD | `-51.31%` | `47,501.00` |
| `Live` | `Long` | `0.0374` | 16,360,000.00 USD | 0.00 USD | 169.09 USD | `-50.91%` | `4,515.00` |
| `Live` | `Long` | `0.0379` | 16,360,000.00 USD | 0.00 USD | 178.36 USD | `-50.26%` | `4,700.00` |
| `Live` | `Long` | `0.0381` | 16,360,000.00 USD | 0.00 USD | 1,600.00 USD | `-50.13%` | `41,929.00` |
| `Live` | `Long` | `0.0382` | 16,350,000.00 USD | 0.00 USD | 204.60 USD | `-49.86%` | `5,349.00` |
| `Live` | `Long` | `0.0384` | 16,350,000.00 USD | 0.00 USD | 301.87 USD | `-49.60%` | `7,851.00` |
| `Live` | `Long` | `0.0386` | 16,350,000.00 USD | 0.00 USD | 121.74 USD | `-49.47%` | `3,158.00` |
| `Live` | `Long` | `0.0393` | 16,350,000.00 USD | 0.00 USD | 2,180.00 USD | `-48.55%` | `55,633.00` |
| `Live` | `Long` | `0.0399` | 16,350,000.00 USD | 0.00 USD | 4,990.00 USD | `-47.64%` | `124,892.00` |
| `Live` | `Long` | `0.0403` | 16,350,000.00 USD | 0.00 USD | 56,710.00 USD | `-47.11%` | `1,405,488.00` |
| `Live` | `Long` | `0.0404` | 16,290,000.00 USD | 0.00 USD | 41,800.00 USD | `-46.98%` | `1,033,413.00` |
| `Live` | `Long` | `0.0408` | 16,250,000.00 USD | 0.00 USD | 558.80 USD | `-46.59%` | `13,713.00` |
| `Live` | `Long` | `0.0411` | 16,250,000.00 USD | 0.00 USD | 4,750.00 USD | `-46.19%` | `115,774.00` |
| `Live` | `Long` | `0.0415` | 16,240,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.54%` | `24,809.00` |
| `Live` | `Long` | `0.0418` | 16,240,000.00 USD | 0.00 USD | 923.89 USD | `-45.28%` | `22,129.00` |
| `Live` | `Long` | `0.0420` | 16,240,000.00 USD | 0.00 USD | 266.05 USD | `-45.01%` | `6,342.00` |
| `Live` | `Long` | `0.0423` | 16,240,000.00 USD | 0.00 USD | 1,670.00 USD | `-44.62%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,240,000.00 USD | 0.00 USD | 267.52 USD | `-44.49%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,240,000.00 USD | 0.00 USD | 455.06 USD | `-44.36%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,240,000.00 USD | 0.00 USD | 883.34 USD | `-44.23%` | `20,760.00` |
| `Live` | `Long` | `0.0427` | 16,240,000.00 USD | 0.00 USD | 38,970.00 USD | `-44.10%` | `913,827.00` |
| `Live` | `Long` | `0.0428` | 16,200,000.00 USD | 0.00 USD | 115,570.00 USD | `-43.97%` | `2,703,371.00` |
| `Live` | `Long` | `0.0430` | 16,080,000.00 USD | 0.00 USD | 859.00 USD | `-43.70%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 16,080,000.00 USD | 0.00 USD | 924,470.00 USD | `-43.44%` | `21,424,497.00` |
| `Live` | `Long` | `0.0432` | 15,160,000.00 USD | 0.00 USD | 10,120.00 USD | `-43.31%` | `233,977.00` |
| `Live` | `Long` | `0.0433` | 15,150,000.00 USD | 0.00 USD | 2,450.00 USD | `-43.18%` | `56,456.00` |
| `Live` | `Long` | `0.0437` | 15,150,000.00 USD | 0.00 USD | 751.83 USD | `-42.79%` | `17,224.00` |
| `Live` | `Long` | `0.0439` | 15,140,000.00 USD | 0.00 USD | 2,620.00 USD | `-42.52%` | `59,668.00` |
| `Live` | `Long` | `0.0440` | 15,140,000.00 USD | 0.00 USD | 1,180.00 USD | `-42.39%` | `26,741.00` |
| `Live` | `Long` | `0.0440` | 15,140,000.00 USD | 0.00 USD | 2,250.00 USD | `-42.26%` | `51,134.00` |
| `Live` | `Long` | `0.0442` | 15,140,000.00 USD | 0.00 USD | 1,140.00 USD | `-42.13%` | `25,729.00` |
| `Live` | `Long` | `0.0442` | 15,140,000.00 USD | 0.00 USD | 1,190.00 USD | `-42.00%` | `26,900.00` |
| `Live` | `Long` | `0.0444` | 15,140,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.87%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 15,030,000.00 USD | 0.00 USD | 444.76 USD | `-41.48%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 15,030,000.00 USD | 0.00 USD | 92,730.00 USD | `-41.34%` | `2,072,162.00` |
| `Live` | `Long` | `0.0449` | 14,940,000.00 USD | 0.00 USD | 810.81 USD | `-41.08%` | `18,038.00` |
| `Live` | `Long` | `0.0454` | 14,940,000.00 USD | 0.00 USD | 2,170.00 USD | `-40.43%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 14,940,000.00 USD | 0.00 USD | 32,650.00 USD | `-40.30%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 14,910,000.00 USD | 0.00 USD | 5,470.00 USD | `-40.03%` | `119,571.00` |
| `Live` | `Long` | `0.0459` | 14,900,000.00 USD | 0.00 USD | 11,010.00 USD | `-39.77%` | `239,650.00` |
| `Live` | `Long` | `0.0461` | 14,890,000.00 USD | 0.00 USD | 4,500.00 USD | `-39.64%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 14,880,000.00 USD | 0.00 USD | 114.36 USD | `-39.51%` | `2,478.00` |
| `Live` | `Long` | `0.0462` | 14,880,000.00 USD | 0.00 USD | 13,410.00 USD | `-39.38%` | `290,000.00` |
| `Live` | `Long` | `0.0464` | 14,870,000.00 USD | 0.00 USD | 362.87 USD | `-39.25%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 14,870,000.00 USD | 0.00 USD | 16,780.00 USD | `-39.12%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 14,850,000.00 USD | 0.00 USD | 109.49 USD | `-38.85%` | `2,347.00` |
| `Live` | `Long` | `0.0467` | 14,850,000.00 USD | 0.00 USD | 2,340.00 USD | `-38.72%` | `50,080.00` |
| `Live` | `Long` | `0.0473` | 14,850,000.00 USD | 0.00 USD | 1,600.00 USD | `-38.07%` | `33,899.00` |
| `Live` | `Long` | `0.0474` | 14,850,000.00 USD | 0.00 USD | 1,420.00 USD | `-37.94%` | `29,884.00` |
| `Live` | `Long` | `0.0476` | 14,850,000.00 USD | 0.00 USD | 105.02 USD | `-37.54%` | `2,204.00` |
| `Live` | `Long` | `0.0481` | 14,850,000.00 USD | 0.00 USD | 58,890.00 USD | `-36.89%` | `1,223,127.00` |
| `Live` | `Long` | `0.0483` | 14,790,000.00 USD | 0.00 USD | 261.03 USD | `-36.76%` | `5,410.00` |
| `Live` | `Long` | `0.0483` | 14,790,000.00 USD | 0.00 USD | 1,780.00 USD | `-36.63%` | `36,742.00` |
| `Live` | `Long` | `0.0485` | 14,790,000.00 USD | 0.00 USD | 1,480.00 USD | `-36.49%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 14,790,000.00 USD | 0.00 USD | 4,610.00 USD | `-35.97%` | `94,321.00` |
| `Live` | `Long` | `0.0490` | 14,780,000.00 USD | 0.00 USD | 5,470.00 USD | `-35.84%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,780,000.00 USD | 0.00 USD | 1,380.00 USD | `-35.71%` | `28,086.00` |
| `Live` | `Long` | `0.0493` | 14,770,000.00 USD | 0.00 USD | 246.25 USD | `-35.45%` | `5,000.00` |
| `Live` | `Long` | `0.0493` | 14,770,000.00 USD | 0.00 USD | 4,780.00 USD | `-35.32%` | `96,957.00` |
| `Live` | `Long` | `0.0495` | 14,770,000.00 USD | 0.00 USD | 655.79 USD | `-35.05%` | `13,235.00` |
| `Live` | `Long` | `0.0498` | 14,770,000.00 USD | 0.00 USD | 253.82 USD | `-34.79%` | `5,102.00` |
| `Live` | `Long` | `0.0498` | 14,770,000.00 USD | 0.00 USD | 40,280.00 USD | `-34.66%` | `808,039.00` |
| `Live` | `Long` | `0.0500` | 14,730,000.00 USD | 0.00 USD | 501.50 USD | `-34.40%` | `10,020.00` |
| `Live` | `Long` | `0.0502` | 14,730,000.00 USD | 0.00 USD | 26,180.00 USD | `-34.27%` | `521,978.00` |
| `Live` | `Long` | `0.0503` | 14,700,000.00 USD | 0.00 USD | 5,410.00 USD | `-34.14%` | `107,572.00` |
| `Live` | `Long` | `0.0505` | 14,700,000.00 USD | 0.00 USD | 334.89 USD | `-33.87%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,700,000.00 USD | 0.00 USD | 1,040.00 USD | `-33.61%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,700,000.00 USD | 0.00 USD | 5,350.00 USD | `-33.48%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,690,000.00 USD | 0.00 USD | 535.43 USD | `-33.22%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,690,000.00 USD | 0.00 USD | 566.65 USD | `-33.09%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,690,000.00 USD | 0.00 USD | 11,000.00 USD | `-32.96%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,680,000.00 USD | 0.00 USD | 1,880.00 USD | `-32.82%` | `36,681.00` |
| `Live` | `Long` | `0.0515` | 14,680,000.00 USD | 0.00 USD | 309.15 USD | `-32.43%` | `5,997.00` |
| `Live` | `Long` | `0.0519` | 14,680,000.00 USD | 0.00 USD | 6,570.00 USD | `-32.04%` | `126,763.00` |
| `Live` | `Long` | `0.0520` | 14,670,000.00 USD | 0.00 USD | 4,950.00 USD | `-31.91%` | `95,346.00` |
| `Live` | `Long` | `0.0520` | 14,660,000.00 USD | 0.00 USD | 4,420.00 USD | `-31.78%` | `84,852.00` |
| `Live` | `Long` | `0.0522` | 14,660,000.00 USD | 0.00 USD | 275,090.00 USD | `-31.51%` | `5,264,820.00` |
| `Live` | `Long` | `0.0524` | 14,380,000.00 USD | 0.00 USD | 25,040.00 USD | `-31.25%` | `477,425.00` |
| `Live` | `Long` | `0.0525` | 14,360,000.00 USD | 0.00 USD | 6,280.00 USD | `-31.12%` | `119,430.00` |
| `Live` | `Long` | `0.0527` | 14,350,000.00 USD | 0.00 USD | 4,520.00 USD | `-30.99%` | `85,771.00` |
| `Live` | `Long` | `0.0527` | 14,350,000.00 USD | 0.00 USD | 3,340.00 USD | `-30.86%` | `63,242.00` |
| `Live` | `Long` | `0.0529` | 14,350,000.00 USD | 0.00 USD | 673.52 USD | `-30.73%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,340,000.00 USD | 0.00 USD | 182,040.00 USD | `-30.60%` | `3,437,948.00` |
| `Live` | `Long` | `0.0532` | 14,160,000.00 USD | 0.00 USD | 9,840.00 USD | `-30.33%` | `185,175.00` |
| `Live` | `Long` | `0.0532` | 14,150,000.00 USD | 0.00 USD | 8,100.00 USD | `-30.20%` | `152,035.00` |
| `Live` | `Long` | `0.0534` | 14,140,000.00 USD | 0.00 USD | 42,580.00 USD | `-30.07%` | `798,082.00` |
| `Live` | `Long` | `0.0534` | 14,100,000.00 USD | 0.00 USD | 930.83 USD | `-29.94%` | `17,415.00` |
| `Live` | `Long` | `0.0536` | 14,100,000.00 USD | 0.00 USD | 942.48 USD | `-29.81%` | `17,600.00` |
| `Live` | `Long` | `0.0537` | 14,100,000.00 USD | 0.00 USD | 2,070.00 USD | `-29.68%` | `38,584.00` |
| `Live` | `Long` | `0.0539` | 14,100,000.00 USD | 0.00 USD | 337.91 USD | `-29.42%` | `6,275.00` |
| `Live` | `Long` | `0.0539` | 14,100,000.00 USD | 0.00 USD | 5,290.00 USD | `-29.29%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 14,090,000.00 USD | 0.00 USD | 2,290.00 USD | `-29.15%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 14,090,000.00 USD | 0.00 USD | 3,030.00 USD | `-29.02%` | `55,906.00` |
| `Live` | `Long` | `0.0542` | 14,090,000.00 USD | 0.00 USD | 96,530.00 USD | `-28.89%` | `1,779,342.00` |
| `Live` | `Long` | `0.0546` | 13,990,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.37%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 13,990,000.00 USD | 0.00 USD | 892.81 USD | `-28.24%` | `16,307.00` |
| `Live` | `Long` | `0.0549` | 13,990,000.00 USD | 0.00 USD | 3,960.00 USD | `-27.98%` | `72,076.00` |
| `Live` | `Long` | `0.0551` | 13,980,000.00 USD | 0.00 USD | 1,760.00 USD | `-27.71%` | `31,888.00` |
| `Live` | `Long` | `0.0556` | 13,980,000.00 USD | 0.00 USD | 907.02 USD | `-27.19%` | `16,328.00` |
| `Live` | `Long` | `0.0558` | 13,980,000.00 USD | 0.00 USD | 464.34 USD | `-26.93%` | `8,329.00` |
| `Live` | `Long` | `0.0561` | 13,980,000.00 USD | 0.00 USD | 8,410.00 USD | `-26.53%` | `150,077.00` |
| `Live` | `Long` | `0.0561` | 13,970,000.00 USD | 0.00 USD | 144.08 USD | `-26.40%` | `2,566.00` |
| `Live` | `Long` | `0.0563` | 13,970,000.00 USD | 0.00 USD | 40,620.00 USD | `-26.27%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,930,000.00 USD | 0.00 USD | 351.85 USD | `-26.14%` | `6,244.00` |
| `Live` | `Long` | `0.0568` | 13,930,000.00 USD | 0.00 USD | 568.50 USD | `-25.48%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,930,000.00 USD | 0.00 USD | 315.67 USD | `-25.35%` | `5,543.00` |
| `Live` | `Long` | `0.0570` | 13,930,000.00 USD | 0.00 USD | 8,350.00 USD | `-25.22%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,920,000.00 USD | 0.00 USD | 814.04 USD | `-25.09%` | `14,244.00` |
| `Live` | `Long` | `0.0573` | 13,920,000.00 USD | 0.00 USD | 6,380.00 USD | `-24.83%` | `111,318.00` |
| `Live` | `Long` | `0.0575` | 13,910,000.00 USD | 0.00 USD | 7,630.00 USD | `-24.57%` | `132,603.00` |
| `Live` | `Long` | `0.0576` | 13,910,000.00 USD | 0.00 USD | 10,600.00 USD | `-24.44%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,900,000.00 USD | 0.00 USD | 14,210.00 USD | `-24.30%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 13,880,000.00 USD | 0.00 USD | 3,940.00 USD | `-24.17%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,880,000.00 USD | 0.00 USD | 441.75 USD | `-24.04%` | `7,623.00` |
| `Live` | `Long` | `0.0580` | 13,880,000.00 USD | 0.00 USD | 431.14 USD | `-23.91%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,880,000.00 USD | 0.00 USD | 447.17 USD | `-23.78%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,880,000.00 USD | 0.00 USD | 582.50 USD | `-23.65%` | `10,000.00` |
| `Live` | `Long` | `0.0583` | 13,880,000.00 USD | 0.00 USD | 16,730.00 USD | `-23.52%` | `286,750.00` |
| `Live` | `Long` | `0.0585` | 13,860,000.00 USD | 0.00 USD | 5,840.00 USD | `-23.39%` | `100,000.00` |
| `Live` | `Long` | `0.0585` | 13,850,000.00 USD | 0.00 USD | 358.03 USD | `-23.26%` | `6,115.00` |
| `Live` | `Long` | `0.0587` | 13,850,000.00 USD | 0.00 USD | 305.15 USD | `-22.99%` | `5,194.00` |
| `Live` | `Long` | `0.0590` | 13,850,000.00 USD | 0.00 USD | 212.22 USD | `-22.73%` | `3,600.00` |
| `Live` | `Long` | `0.0590` | 13,850,000.00 USD | 0.00 USD | 1,230.00 USD | `-22.60%` | `20,913.00` |
| `Live` | `Long` | `0.0592` | 13,850,000.00 USD | 0.00 USD | 30,340.00 USD | `-22.47%` | `512,956.00` |
| `Live` | `Long` | `0.0593` | 13,820,000.00 USD | 0.00 USD | 546.26 USD | `-22.21%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,820,000.00 USD | 0.00 USD | 4,140.00 USD | `-22.08%` | `69,573.00` |
| `Live` | `Long` | `0.0595` | 13,820,000.00 USD | 0.00 USD | 3,300.00 USD | `-21.95%` | `55,392.00` |
| `Live` | `Long` | `0.0597` | 13,810,000.00 USD | 0.00 USD | 5,890,000.00 USD | `-21.81%` | `98,666,424.00` |
| `Live` | `Long` | `0.0599` | 7,930,000.00 USD | 0.00 USD | 2,510.00 USD | `-21.55%` | `42,005.00` |
| `Live` | `Long` | `0.0600` | 7,920,000.00 USD | 0.00 USD | 8,560.00 USD | `-21.42%` | `142,849.00` |
| `Live` | `Long` | `0.0600` | 7,920,000.00 USD | 0.00 USD | 24,120.00 USD | `-21.29%` | `401,658.00` |
| `Live` | `Long` | `0.0602` | 7,890,000.00 USD | 0.00 USD | 8,490.00 USD | `-21.16%` | `141,093.00` |
| `Live` | `Long` | `0.0602` | 7,880,000.00 USD | 0.00 USD | 830.97 USD | `-21.03%` | `13,792.00` |
| `Live` | `Long` | `0.0604` | 7,880,000.00 USD | 0.00 USD | 1,510.00 USD | `-20.90%` | `25,043.00` |
| `Live` | `Long` | `0.0605` | 7,880,000.00 USD | 0.00 USD | 32,470.00 USD | `-20.63%` | `536,332.00` |
| `Live` | `Long` | `0.0607` | 7,850,000.00 USD | 0.00 USD | 622.63 USD | `-20.50%` | `10,266.00` |
| `Live` | `Long` | `0.0607` | 7,850,000.00 USD | 0.00 USD | 1,220.00 USD | `-20.37%` | `20,080.00` |
| `Live` | `Long` | `0.0609` | 7,850,000.00 USD | 0.00 USD | 717.73 USD | `-20.24%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 7,850,000.00 USD | 0.00 USD | 5,110.00 USD | `-20.11%` | `83,914.00` |
| `Live` | `Long` | `0.0611` | 7,840,000.00 USD | 0.00 USD | 359,500.00 USD | `-19.98%` | `5,888,653.00` |
| `Live` | `Long` | `0.0612` | 7,480,000.00 USD | 0.00 USD | 629.72 USD | `-19.85%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 7,480,000.00 USD | 0.00 USD | 298.17 USD | `-19.72%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,480,000.00 USD | 0.00 USD | 655.16 USD | `-19.59%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,480,000.00 USD | 0.00 USD | 2,670.00 USD | `-19.32%` | `43,404.00` |
| `Live` | `Long` | `0.0617` | 7,480,000.00 USD | 0.00 USD | 11,100.00 USD | `-19.19%` | `180,028.00` |
| `Live` | `Long` | `0.0617` | 7,470,000.00 USD | 0.00 USD | 158.08 USD | `-19.06%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,470,000.00 USD | 0.00 USD | 26,790.00 USD | `-18.67%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,440,000.00 USD | 0.00 USD | 345.86 USD | `-18.54%` | `5,565.00` |
| `Live` | `Long` | `0.0622` | 7,440,000.00 USD | 0.00 USD | 194.66 USD | `-18.41%` | `3,127.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.28%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 43,420.00 USD | `-18.14%` | `695,308.00` |
| `Live` | `Long` | `0.0625` | 7,390,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-18.01%` | `17,630,450.00` |
| `Live` | `Long` | `0.0626` | 6,290,000.00 USD | 0.00 USD | 1,250.00 USD | `-17.88%` | `19,891.00` |
| `Live` | `Long` | `0.0628` | 6,290,000.00 USD | 0.00 USD | 461.78 USD | `-17.75%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,290,000.00 USD | 0.00 USD | 6,400.00 USD | `-17.62%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,280,000.00 USD | 0.00 USD | 2,430.00 USD | `-17.36%` | `38,603.00` |
| `Live` | `Long` | `0.0631` | 6,280,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-17.23%` | `20,783,139.00` |
| `Live` | `Long` | `0.0633` | 4,970,000.00 USD | 0.00 USD | 3,260.00 USD | `-17.10%` | `51,566.00` |
| `Live` | `Long` | `0.0634` | 4,960,000.00 USD | 0.00 USD | 12,660.00 USD | `-16.96%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 1,690.00 USD | `-16.83%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 4,950,000.00 USD | 0.00 USD | 280.95 USD | `-16.70%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 4,950,000.00 USD | 0.00 USD | 4,770.00 USD | `-16.57%` | `74,997.00` |
| `Live` | `Long` | `0.0638` | 4,940,000.00 USD | 0.00 USD | 5,600.00 USD | `-16.44%` | `87,791.00` |
| `Live` | `Long` | `0.0639` | 4,940,000.00 USD | 0.00 USD | 23,220.00 USD | `-16.31%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 4,920,000.00 USD | 0.00 USD | 1,990.00 USD | `-16.18%` | `31,194.00` |
| `Live` | `Long` | `0.0640` | 4,910,000.00 USD | 0.00 USD | 748.55 USD | `-16.05%` | `11,687.00` |
| `Live` | `Long` | `0.0641` | 4,910,000.00 USD | 0.00 USD | 3,270.00 USD | `-15.92%` | `50,913.00` |
| `Live` | `Long` | `0.0643` | 4,910,000.00 USD | 0.00 USD | 733.80 USD | `-15.79%` | `11,421.00` |
| `Live` | `Long` | `0.0644` | 4,910,000.00 USD | 0.00 USD | 76,280.00 USD | `-15.65%` | `1,185,416.00` |
| `Live` | `Long` | `0.0644` | 4,830,000.00 USD | 0.00 USD | 27,310.00 USD | `-15.52%` | `423,677.00` |
| `Live` | `Long` | `0.0645` | 4,810,000.00 USD | 0.00 USD | 631.94 USD | `-15.39%` | `9,790.00` |
| `Live` | `Long` | `0.0648` | 4,800,000.00 USD | 0.00 USD | 163,150.00 USD | `-15.13%` | `2,519,746.00` |
| `Live` | `Long` | `0.0649` | 4,640,000.00 USD | 0.00 USD | 8,800.00 USD | `-15.00%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,630,000.00 USD | 0.00 USD | 21,910.00 USD | `-14.87%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 4,610,000.00 USD | 0.00 USD | 2,380.00 USD | `-14.61%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,610,000.00 USD | 0.00 USD | 13,770.00 USD | `-14.47%` | `210,965.00` |
| `Live` | `Long` | `0.0655` | 4,590,000.00 USD | 0.00 USD | 7,790.00 USD | `-14.08%` | `118,852.00` |
| `Live` | `Long` | `0.0657` | 4,590,000.00 USD | 0.00 USD | 14,160.00 USD | `-13.95%` | `215,665.00` |
| `Live` | `Long` | `0.0658` | 4,570,000.00 USD | 0.00 USD | 66,820.00 USD | `-13.82%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,510,000.00 USD | 0.00 USD | 14,600.00 USD | `-13.69%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,490,000.00 USD | 0.00 USD | 9,600.00 USD | `-13.56%` | `145,525.00` |
| `Live` | `Long` | `0.0662` | 4,480,000.00 USD | 0.00 USD | 12,560.00 USD | `-13.29%` | `189,817.00` |
| `Live` | `Long` | `0.0663` | 4,470,000.00 USD | 0.00 USD | 1,630.00 USD | `-13.16%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,470,000.00 USD | 0.00 USD | 17,410.00 USD | `-13.03%` | `262,335.00` |
| `Live` | `Long` | `0.0664` | 4,450,000.00 USD | 0.00 USD | 4,070.00 USD | `-12.90%` | `61,232.00` |
| `Live` | `Long` | `0.0667` | 4,450,000.00 USD | 0.00 USD | 34,860.00 USD | `-12.64%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,410,000.00 USD | 0.00 USD | 9,150.00 USD | `-12.51%` | `137,075.00` |
| `Live` | `Long` | `0.0669` | 4,400,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-12.38%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,260,000.00 USD | 0.00 USD | 1,180.00 USD | `-12.25%` | `17,570.00` |
| `Live` | `Long` | `0.0670` | 3,250,000.00 USD | 0.00 USD | 9,050.00 USD | `-12.12%` | `134,979.00` |
| `Live` | `Long` | `0.0673` | 3,250,000.00 USD | 0.00 USD | 9,220.00 USD | `-11.85%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,240,000.00 USD | 0.00 USD | 15,370.00 USD | `-11.72%` | `228,139.00` |
| `Live` | `Long` | `0.0674` | 3,220,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.59%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,220,000.00 USD | 0.00 USD | 112,780.00 USD | `-11.46%` | `1,669,510.00` |
| `Live` | `Long` | `0.0677` | 3,110,000.00 USD | 0.00 USD | 12,610.00 USD | `-11.33%` | `186,370.00` |
| `Live` | `Long` | `0.0678` | 3,090,000.00 USD | 0.00 USD | 4,290.00 USD | `-11.20%` | `63,374.00` |
| `Live` | `Long` | `0.0678` | 3,090,000.00 USD | 0.00 USD | 68,070.00 USD | `-11.07%` | `1,003,212.00` |
| `Live` | `Long` | `0.0679` | 3,020,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.94%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,000,000.00 USD | 0.00 USD | 212.72 USD | `-10.80%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,000,000.00 USD | 0.00 USD | 49,480.00 USD | `-10.67%` | `726,014.00` |
| `Live` | `Long` | `0.0683` | 2,960,000.00 USD | 0.00 USD | 6,220.00 USD | `-10.54%` | `91,110.00` |
| `Live` | `Long` | `0.0684` | 2,950,000.00 USD | 0.00 USD | 80,430.00 USD | `-10.28%` | `1,174,961.00` |
| `Live` | `Long` | `0.0685` | 2,870,000.00 USD | 0.00 USD | 13,120.00 USD | `-10.15%` | `191,414.00` |
| `Live` | `Long` | `0.0687` | 2,860,000.00 USD | 0.00 USD | 595.81 USD | `-10.02%` | `8,679.00` |
| `Live` | `Long` | `0.0688` | 2,850,000.00 USD | 0.00 USD | 16,210.00 USD | `-9.89%` | `235,726.00` |
| `Live` | `Long` | `0.0688` | 2,840,000.00 USD | 0.00 USD | 1,000.00 USD | `-9.76%` | `14,570.00` |
| `Live` | `Long` | `0.0689` | 2,840,000.00 USD | 0.00 USD | 507,660.00 USD | `-9.62%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,330,000.00 USD | 0.00 USD | 6,960.00 USD | `-9.49%` | `100,756.00` |
| `Live` | `Long` | `0.0692` | 2,320,000.00 USD | 0.00 USD | 13,510.00 USD | `-9.36%` | `195,385.00` |
| `Live` | `Long` | `0.0693` | 2,310,000.00 USD | 0.00 USD | 9,970.00 USD | `-9.23%` | `144,028.00` |
| `Live` | `Long` | `0.0693` | 2,300,000.00 USD | 0.00 USD | 2,020.00 USD | `-9.10%` | `29,107.00` |
| `Live` | `Long` | `0.0694` | 2,300,000.00 USD | 0.00 USD | 4,980.00 USD | `-8.97%` | `71,770.00` |
| `Live` | `Long` | `0.0697` | 2,290,000.00 USD | 0.00 USD | 5,240.00 USD | `-8.71%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,290,000.00 USD | 0.00 USD | 6,680.00 USD | `-8.58%` | `95,809.00` |
| `Live` | `Long` | `0.0698` | 2,280,000.00 USD | 0.00 USD | 2,910.00 USD | `-8.45%` | `41,684.00` |
| `Live` | `Long` | `0.0699` | 2,280,000.00 USD | 0.00 USD | 1,310.00 USD | `-8.31%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,280,000.00 USD | 0.00 USD | 9,620.00 USD | `-8.18%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,270,000.00 USD | 0.00 USD | 11,430.00 USD | `-8.05%` | `162,900.00` |
| `Live` | `Long` | `0.0703` | 2,260,000.00 USD | 0.00 USD | 1,070.00 USD | `-7.92%` | `15,205.00` |
| `Live` | `Long` | `0.0703` | 2,250,000.00 USD | 0.00 USD | 4,360.00 USD | `-7.79%` | `61,923.00` |
| `Live` | `Long` | `0.0704` | 2,250,000.00 USD | 0.00 USD | 216.56 USD | `-7.66%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 423.90 USD | `-7.40%` | `6,000.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 94,410.00 USD | `-7.27%` | `1,334,448.00` |
| `Live` | `Long` | `0.0708` | 2,150,000.00 USD | 0.00 USD | 428.57 USD | `-7.13%` | `6,049.00` |
| `Live` | `Long` | `0.0709` | 2,150,000.00 USD | 0.00 USD | 821.60 USD | `-7.00%` | `11,580.00` |
| `Live` | `Long` | `0.0711` | 2,150,000.00 USD | 0.00 USD | 4,720.00 USD | `-6.87%` | `66,436.00` |
| `Live` | `Long` | `0.0712` | 2,150,000.00 USD | 0.00 USD | 1,860.00 USD | `-6.74%` | `26,118.00` |
| `Live` | `Long` | `0.0712` | 2,150,000.00 USD | 0.00 USD | 802.06 USD | `-6.61%` | `11,257.00` |
| `Live` | `Long` | `0.0713` | 2,150,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-6.48%` | `24,500,580.00` |
| `Live` | `Long` | `0.0714` | 398,010.00 USD | 0.00 USD | 5,410.00 USD | `-6.35%` | `75,723.00` |
| `Live` | `Long` | `0.0716` | 392,600.00 USD | 0.00 USD | 8,120.00 USD | `-6.22%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 384,480.00 USD | 0.00 USD | 1,170.00 USD | `-6.09%` | `16,291.00` |
| `Live` | `Long` | `0.0717` | 383,310.00 USD | 0.00 USD | 22,270.00 USD | `-5.95%` | `310,316.00` |
| `Live` | `Long` | `0.0718` | 361,050.00 USD | 0.00 USD | 1,600.00 USD | `-5.82%` | `22,299.00` |
| `Live` | `Long` | `0.0720` | 359,450.00 USD | 0.00 USD | 1,900.00 USD | `-5.69%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 357,550.00 USD | 0.00 USD | 12,310.00 USD | `-5.56%` | `170,786.00` |
| `Live` | `Long` | `0.0722` | 345,250.00 USD | 0.00 USD | 22,360.00 USD | `-5.43%` | `309,869.00` |
| `Live` | `Long` | `0.0722` | 322,890.00 USD | 0.00 USD | 322,260.00 USD | `-5.30%` | `4,460,378.00` |
| `Live` | `Long` | `0.0723` | 626.77 USD | 0.00 USD | 626.77 USD | `-5.17%` | `8,663.00` |
| `Live` | `Short` | `0.0727` | 120.82 USD | 120.82 USD | 0.00 USD | `-4.78%` | `1,663.00` |
| `Live` | `Short` | `0.0775` | 361.76 USD | 240.95 USD | 0.00 USD | `+1.65%` | `3,107.00` |
| `Live` | `Short` | `0.0780` | 3,850.00 USD | 3,490.00 USD | 0.00 USD | `+2.17%` | `44,723.00` |
| `Live` | `Short` | `0.0788` | 3,960.00 USD | 113.24 USD | 0.00 USD | `+3.22%` | `1,438.00` |
| `Live` | `Short` | `0.0795` | 4,070.00 USD | 104.72 USD | 0.00 USD | `+4.14%` | `1,318.00` |
| `Live` | `Short` | `0.0814` | 4,180.00 USD | 118.92 USD | 0.00 USD | `+6.76%` | `1,460.00` |
| `Live` | `Short` | `0.0819` | 4,570.00 USD | 380.85 USD | 0.00 USD | `+7.28%` | `4,653.00` |
| `Live` | `Short` | `0.0832` | 8,020.00 USD | 3,450.00 USD | 0.00 USD | `+8.99%` | `41,543.00` |
| `Live` | `Short` | `0.0833` | 8,520.00 USD | 500.17 USD | 0.00 USD | `+9.12%` | `6,008.00` |
| `Live` | `Short` | `0.0837` | 8,810.00 USD | 293.44 USD | 0.00 USD | `+9.64%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 10,390.00 USD | 1,570.00 USD | 0.00 USD | `+9.77%` | `18,767.00` |
| `Live` | `Short` | `0.0843` | 10,650.00 USD | 264.21 USD | 0.00 USD | `+10.43%` | `3,136.00` |
| `Live` | `Short` | `0.0848` | 11,080.00 USD | 426.71 USD | 0.00 USD | `+11.22%` | `5,029.00` |
| `Live` | `Short` | `0.0858` | 11,190.00 USD | 115.30 USD | 0.00 USD | `+12.53%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 15,640.00 USD | 4,450.00 USD | 0.00 USD | `+12.66%` | `51,791.00` |
| `Live` | `Short` | `0.0868` | 15,800.00 USD | 155.98 USD | 0.00 USD | `+13.84%` | `1,796.00` |
| `Live` | `Short` | `0.0871` | 15,940.00 USD | 138.58 USD | 0.00 USD | `+14.10%` | `1,592.00` |
| `Live` | `Short` | `0.0881` | 16,400.00 USD | 465.17 USD | 0.00 USD | `+15.41%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 16,810.00 USD | 411.53 USD | 0.00 USD | `+16.33%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 17,230.00 USD | 418.80 USD | 0.00 USD | `+16.72%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 17,520.00 USD | 285.70 USD | 0.00 USD | `+17.25%` | `3,194.00` |
| `Live` | `Short` | `0.0905` | 24,280.00 USD | 6,760.00 USD | 0.00 USD | `+18.56%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 25,590.00 USD | 1,310.00 USD | 0.00 USD | `+18.82%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 30,530.00 USD | 4,940.00 USD | 0.00 USD | `+19.47%` | `54,197.00` |
| `Live` | `Short` | `0.0921` | 30,700.00 USD | 171.49 USD | 0.00 USD | `+20.65%` | `1,863.00` |
| `Live` | `Short` | `0.0931` | 35,700.00 USD | 5,000.00 USD | 0.00 USD | `+22.10%` | `53,646.00` |
| `Live` | `Short` | `0.0934` | 35,950.00 USD | 249.24 USD | 0.00 USD | `+22.36%` | `2,670.00` |
| `Live` | `Short` | `0.0940` | 36,860.00 USD | 915.67 USD | 0.00 USD | `+23.27%` | `9,736.00` |
| `Live` | `Short` | `0.0944` | 76,570.00 USD | 39,700.00 USD | 0.00 USD | `+23.67%` | `420,808.00` |
| `Live` | `Short` | `0.0945` | 76,760.00 USD | 192.21 USD | 0.00 USD | `+23.80%` | `2,035.00` |
| `Live` | `Short` | `0.0946` | 124,080.00 USD | 47,330.00 USD | 0.00 USD | `+24.06%` | `500,000.00` |
| `Live` | `Short` | `0.0950` | 148,550.00 USD | 24,460.00 USD | 0.00 USD | `+24.45%` | `257,659.00` |
| `Live` | `Short` | `0.0950` | 149,310.00 USD | 761.26 USD | 0.00 USD | `+24.59%` | `8,009.00` |
| `Live` | `Short` | `0.0961` | 149,920.00 USD | 609.59 USD | 0.00 USD | `+26.03%` | `6,340.00` |
| `Live` | `Short` | `0.0964` | 152,730.00 USD | 2,820.00 USD | 0.00 USD | `+26.29%` | `29,217.00` |
| `Live` | `Short` | `0.0974` | 152,860.00 USD | 121.23 USD | 0.00 USD | `+27.73%` | `1,244.00` |
| `Live` | `Short` | `0.0983` | 153,330.00 USD | 477.50 USD | 0.00 USD | `+28.78%` | `4,860.00` |
| `Live` | `Short` | `0.0984` | 154,520.00 USD | 1,190.00 USD | 0.00 USD | `+29.04%` | `12,089.00` |
| `Live` | `Short` | `0.1014` | 162,150.00 USD | 7,630.00 USD | 0.00 USD | `+32.97%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 165,120.00 USD | 2,970.00 USD | 0.00 USD | `+33.24%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 165,610.00 USD | 492.85 USD | 0.00 USD | `+33.50%` | `4,839.00` |
| `Live` | `Short` | `0.1061` | 171,720.00 USD | 6,110.00 USD | 0.00 USD | `+39.13%` | `57,554.00` |
| `Live` | `Short` | `0.1062` | 175,020.00 USD | 3,290.00 USD | 0.00 USD | `+39.27%` | `31,000.00` |
| `Live` | `Short` | `0.1076` | 175,630.00 USD | 616.19 USD | 0.00 USD | `+41.10%` | `5,724.00` |
| `Live` | `Short` | `0.1085` | 178,870.00 USD | 3,240.00 USD | 0.00 USD | `+42.28%` | `29,849.00` |
| `Live` | `Short` | `0.1095` | 180,810.00 USD | 1,940.00 USD | 0.00 USD | `+43.59%` | `17,721.00` |
| `Live` | `Short` | `0.1127` | 181,030.00 USD | 214.15 USD | 0.00 USD | `+47.65%` | `1,901.00` |
| `Live` | `Short` | `0.1137` | 181,170.00 USD | 147.86 USD | 0.00 USD | `+48.97%` | `1,301.00` |
| `Live` | `Short` | `0.1158` | 181,310.00 USD | 131.49 USD | 0.00 USD | `+51.85%` | `1,135.00` |
| `Live` | `Short` | `0.1202` | 181,420.00 USD | 116.04 USD | 0.00 USD | `+57.62%` | `965.00` |
| `Live` | `Short` | `0.1222` | 182,060.00 USD | 637.53 USD | 0.00 USD | `+60.24%` | `5,215.00` |
| `Live` | `Short` | `0.1229` | 184,390.00 USD | 2,330.00 USD | 0.00 USD | `+61.02%` | `18,935.00` |
| `Live` | `Short` | `0.1252` | 185,720.00 USD | 1,330.00 USD | 0.00 USD | `+64.04%` | `10,652.00` |
| `Live` | `Short` | `0.1253` | 186,620.00 USD | 904.18 USD | 0.00 USD | `+64.17%` | `7,219.00` |
| `Live` | `Short` | `0.1270` | 186,730.00 USD | 108.80 USD | 0.00 USD | `+66.40%` | `857.00` |
| `Live` | `Short` | `0.1296` | 186,900.00 USD | 171.66 USD | 0.00 USD | `+69.94%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 189,040.00 USD | 2,140.00 USD | 0.00 USD | `+71.90%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 189,150.00 USD | 102.97 USD | 0.00 USD | `+72.82%` | `781.00` |
| `Live` | `Short` | `0.1330` | 223,490.00 USD | 34,350.00 USD | 0.00 USD | `+74.26%` | `258,360.00` |
| `Live` | `Short` | `0.1338` | 223,700.00 USD | 205.31 USD | 0.00 USD | `+75.31%` | `1,535.00` |
| `Live` | `Short` | `0.1341` | 269,580.00 USD | 45,880.00 USD | 0.00 USD | `+75.70%` | `342,231.00` |
| `Live` | `Short` | `0.1364` | 269,710.00 USD | 136.31 USD | 0.00 USD | `+78.85%` | `999.00` |
| `Live` | `Short` | `0.1404` | 270,380.00 USD | 663.63 USD | 0.00 USD | `+84.09%` | `4,725.00` |
| `Live` | `Short` | `0.1407` | 293,200.00 USD | 22,830.00 USD | 0.00 USD | `+84.49%` | `162,180.00` |
| `Live` | `Short` | `0.1432` | 296,960.00 USD | 3,760.00 USD | 0.00 USD | `+87.76%` | `26,250.00` |
| `Live` | `Short` | `0.1441` | 297,160.00 USD | 196.63 USD | 0.00 USD | `+88.81%` | `1,365.00` |
| `Live` | `Short` | `0.1444` | 312,460.00 USD | 15,300.00 USD | 0.00 USD | `+89.20%` | `106,016.00` |
| `Live` | `Short` | `0.1446` | 312,610.00 USD | 144.55 USD | 0.00 USD | `+89.47%` | `1,000.00` |
| `Live` | `Short` | `0.1451` | 314,430.00 USD | 1,820.00 USD | 0.00 USD | `+90.12%` | `12,559.00` |
| `Live` | `Short` | `0.1461` | 337,910.00 USD | 23,490.00 USD | 0.00 USD | `+91.43%` | `160,802.00` |
| `Live` | `Short` | `0.1479` | 346,090.00 USD | 8,180.00 USD | 0.00 USD | `+93.79%` | `55,317.00` |
| `Live` | `Short` | `0.1484` | 3,320,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+94.58%` | `20,059,331.00` |
| `Live` | `Short` | `0.1489` | 3,320,000.00 USD | 483.17 USD | 0.00 USD | `+95.10%` | `3,246.00` |
| `Live` | `Short` | `0.1494` | 3,320,000.00 USD | 448.05 USD | 0.00 USD | `+95.76%` | `3,000.00` |
| `Live` | `Short` | `0.1497` | 3,330,000.00 USD | 2,100.00 USD | 0.00 USD | `+96.15%` | `14,000.00` |
| `Live` | `Short` | `0.1507` | 3,380,000.00 USD | 56,440.00 USD | 0.00 USD | `+97.59%` | `374,415.00` |
| `Live` | `Short` | `0.1512` | 3,380,000.00 USD | 1,320.00 USD | 0.00 USD | `+98.25%` | `8,712.00` |
| `Live` | `Short` | `0.1525` | 3,380,000.00 USD | 267.55 USD | 0.00 USD | `+99.82%` | `1,755.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 744,380.00 USD | 0.00 USD | 375.42 USD | `-66.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 744,010.00 USD | 0.00 USD | 409.59 USD | `-47.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 743,600.00 USD | 0.00 USD | 132.68 USD | `-46.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 743,460.00 USD | 0.00 USD | 788.27 USD | `-45.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 742,680.00 USD | 0.00 USD | 527.05 USD | `-45.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 742,150.00 USD | 0.00 USD | 286.87 USD | `-41.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 741,860.00 USD | 0.00 USD | 252.42 USD | `-39.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 741,610.00 USD | 0.00 USD | 468.67 USD | `-38.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 741,140.00 USD | 0.00 USD | 5,160.00 USD | `-35.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 735,980.00 USD | 0.00 USD | 920.48 USD | `-35.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 735,060.00 USD | 0.00 USD | 236.01 USD | `-34.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 734,830.00 USD | 0.00 USD | 175.41 USD | `-32.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 734,650.00 USD | 0.00 USD | 242.96 USD | `-32.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 734,410.00 USD | 0.00 USD | 2,670.00 USD | `-29.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 731,730.00 USD | 0.00 USD | 1,370.00 USD | `-27.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 730,360.00 USD | 0.00 USD | 437.58 USD | `-26.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 729,920.00 USD | 0.00 USD | 183.30 USD | `-23.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 729,740.00 USD | 0.00 USD | 752.54 USD | `-23.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 728,990.00 USD | 0.00 USD | 9,830.00 USD | `-22.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 719,160.00 USD | 0.00 USD | 1,050.00 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 718,110.00 USD | 0.00 USD | 668.84 USD | `-21.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 717,440.00 USD | 0.00 USD | 273.90 USD | `-21.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 717,170.00 USD | 0.00 USD | 8,800.00 USD | `-20.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 708,370.00 USD | 0.00 USD | 419.39 USD | `-20.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 707,950.00 USD | 0.00 USD | 218.94 USD | `-20.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 707,730.00 USD | 0.00 USD | 504.26 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 707,230.00 USD | 0.00 USD | 2,280.00 USD | `-18.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 704,950.00 USD | 0.00 USD | 118.27 USD | `-18.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 704,830.00 USD | 0.00 USD | 1,280.00 USD | `-18.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 703,550.00 USD | 0.00 USD | 1,820.00 USD | `-17.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 701,730.00 USD | 0.00 USD | 1,340.00 USD | `-16.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 700,390.00 USD | 0.00 USD | 386.70 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 700,000.00 USD | 0.00 USD | 644.50 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 699,360.00 USD | 0.00 USD | 19,520.00 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 679,840.00 USD | 0.00 USD | 362.24 USD | `-14.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 679,480.00 USD | 0.00 USD | 3,140.00 USD | `-14.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 676,340.00 USD | 0.00 USD | 1,100.00 USD | `-13.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 675,250.00 USD | 0.00 USD | 1,200.00 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 674,050.00 USD | 0.00 USD | 996.31 USD | `-13.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 673,050.00 USD | 0.00 USD | 909.85 USD | `-12.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 672,140.00 USD | 0.00 USD | 115.57 USD | `-11.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 672,020.00 USD | 0.00 USD | 33,620.00 USD | `-11.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 638,400.00 USD | 0.00 USD | 12,860.00 USD | `-11.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 625,540.00 USD | 0.00 USD | 1,540.00 USD | `-11.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 624,000.00 USD | 0.00 USD | 108.08 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 623,890.00 USD | 0.00 USD | 19,540.00 USD | `-11.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 604,350.00 USD | 0.00 USD | 1,430.00 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 602,910.00 USD | 0.00 USD | 8,540.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 594,380.00 USD | 0.00 USD | 8,580.00 USD | `-10.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 585,800.00 USD | 0.00 USD | 4,970.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 580,830.00 USD | 0.00 USD | 3,100.00 USD | `-10.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 577,740.00 USD | 0.00 USD | 160.31 USD | `-10.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 577,580.00 USD | 0.00 USD | 38,710.00 USD | `-9.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 538,870.00 USD | 0.00 USD | 27,690.00 USD | `-9.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 511,180.00 USD | 0.00 USD | 3,190.00 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 507,990.00 USD | 0.00 USD | 176.08 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 507,810.00 USD | 0.00 USD | 142.09 USD | `-8.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 507,670.00 USD | 0.00 USD | 925.29 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 506,740.00 USD | 0.00 USD | 797.80 USD | `-8.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 505,950.00 USD | 0.00 USD | 68,440.00 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 437,510.00 USD | 0.00 USD | 141.77 USD | `-8.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 437,370.00 USD | 0.00 USD | 895.27 USD | `-7.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 436,470.00 USD | 0.00 USD | 523.23 USD | `-7.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 435,950.00 USD | 0.00 USD | 468.88 USD | `-7.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 435,480.00 USD | 0.00 USD | 235.12 USD | `-7.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 435,240.00 USD | 0.00 USD | 1,090.00 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 434,160.00 USD | 0.00 USD | 71,660.00 USD | `-7.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0711` | 362,490.00 USD | 0.00 USD | 729.61 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 361,770.00 USD | 0.00 USD | 355.75 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 361,410.00 USD | 0.00 USD | 20,180.00 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 341,230.00 USD | 0.00 USD | 608.76 USD | `-6.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 340,620.00 USD | 0.00 USD | 16,880.00 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 323,740.00 USD | 0.00 USD | 110.12 USD | `-6.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 323,630.00 USD | 0.00 USD | 1,880.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 321,750.00 USD | 0.00 USD | 18,420.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 303,330.00 USD | 0.00 USD | 13,550.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 289,780.00 USD | 0.00 USD | 551.98 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 289,220.00 USD | 0.00 USD | 138,380.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 150,840.00 USD | 0.00 USD | 849.15 USD | `-5.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 149,990.00 USD | 0.00 USD | 34,460.00 USD | `-5.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 115,530.00 USD | 0.00 USD | 2,030.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 113,500.00 USD | 0.00 USD | 1,950.00 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 111,550.00 USD | 0.00 USD | 2,540.00 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 109,010.00 USD | 0.00 USD | 4,110.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 104,900.00 USD | 0.00 USD | 2,090.00 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 102,810.00 USD | 0.00 USD | 1,950.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 100,850.00 USD | 0.00 USD | 535.16 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 100,320.00 USD | 0.00 USD | 227.92 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 100,090.00 USD | 0.00 USD | 397.76 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 99,690.00 USD | 0.00 USD | 398.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 99,300.00 USD | 0.00 USD | 797.39 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 98,500.00 USD | 0.00 USD | 59,430.00 USD | `-3.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 39,060.00 USD | 0.00 USD | 1,640.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 37,420.00 USD | 0.00 USD | 189.57 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 37,230.00 USD | 0.00 USD | 1,480.00 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 35,760.00 USD | 0.00 USD | 2,900.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 32,860.00 USD | 0.00 USD | 415.62 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 32,440.00 USD | 0.00 USD | 16,520.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 15,930.00 USD | 0.00 USD | 3,170.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 12,750.00 USD | 0.00 USD | 375.86 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 12,380.00 USD | 0.00 USD | 399.17 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 11,980.00 USD | 0.00 USD | 140.04 USD | `-1.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 11,840.00 USD | 0.00 USD | 1,490.00 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 10,340.00 USD | 0.00 USD | 3,450.00 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 6,890.00 USD | 0.00 USD | 736.17 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 6,160.00 USD | 0.00 USD | 406.95 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0754` | 5,750.00 USD | 0.00 USD | 221.00 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 5,530.00 USD | 0.00 USD | 757.44 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 4,770.00 USD | 0.00 USD | 408.57 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 4,360.00 USD | 0.00 USD | 408.81 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 3,950.00 USD | 0.00 USD | 1,210.00 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 2,740.00 USD | 0.00 USD | 504.10 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 2,240.00 USD | 0.00 USD | 398.13 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 1,840.00 USD | 0.00 USD | 216.21 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 1,620.00 USD | 0.00 USD | 806.81 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0762` | 814.81 USD | 0.00 USD | 814.81 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 3,770.00 USD | 3,770.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 3,880.00 USD | 109.63 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 5,130.00 USD | 1,250.00 USD | 0.00 USD | `+0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 5,310.00 USD | 183.50 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 6,160.00 USD | 843.94 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 6,910.00 USD | 754.59 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 7,730.00 USD | 816.05 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 8,600.00 USD | 870.90 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 8,700.00 USD | 100.37 USD | 0.00 USD | `+1.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 8,940.00 USD | 240.02 USD | 0.00 USD | `+1.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 12,870.00 USD | 3,930.00 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 13,280.00 USD | 407.23 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 13,600.00 USD | 321.13 USD | 0.00 USD | `+1.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 15,090.00 USD | 1,490.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 17,340.00 USD | 2,240.00 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 17,670.00 USD | 329.23 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 17,820.00 USD | 155.43 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 18,010.00 USD | 186.07 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 21,090.00 USD | 3,080.00 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 22,060.00 USD | 975.23 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 26,430.00 USD | 4,370.00 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 26,590.00 USD | 157.14 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 26,720.00 USD | 130.71 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 68,330.00 USD | 41,610.00 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 68,470.00 USD | 141.44 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 69,240.00 USD | 773.68 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 69,930.00 USD | 687.81 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 75,510.00 USD | 5,580.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 76,330.00 USD | 812.79 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 81,590.00 USD | 5,270.00 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 90,610.00 USD | 9,020.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 90,920.00 USD | 312.56 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 91,380.00 USD | 455.34 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 91,500.00 USD | 125.45 USD | 0.00 USD | `+4.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 91,730.00 USD | 230.40 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 92,050.00 USD | 319.16 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 93,060.00 USD | 1,010.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 115,810.00 USD | 22,750.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 116,210.00 USD | 400.91 USD | 0.00 USD | `+5.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 116,410.00 USD | 200.46 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 116,670.00 USD | 259.13 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 117,380.00 USD | 707.08 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 126,380.00 USD | 9,010.00 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 223,160.00 USD | 96,780.00 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 223,970.00 USD | 807.50 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 224,230.00 USD | 257.18 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 224,650.00 USD | 424.74 USD | 0.00 USD | `+6.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 224,760.00 USD | 101.80 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 226,140.00 USD | 1,380.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 228,170.00 USD | 2,030.00 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 229,600.00 USD | 1,430.00 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 229,730.00 USD | 129.67 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 230,750.00 USD | 1,020.00 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 231,000.00 USD | 256.05 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 232,030.00 USD | 1,030.00 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 235,050.00 USD | 3,020.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 235,380.00 USD | 327.80 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 235,840.00 USD | 457.92 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 236,530.00 USD | 691.29 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 237,330.00 USD | 800.79 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 237,840.00 USD | 512.05 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 238,330.00 USD | 495.36 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 238,720.00 USD | 389.31 USD | 0.00 USD | `+8.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 238,880.00 USD | 154.58 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 239,180.00 USD | 303.56 USD | 0.00 USD | `+8.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 239,300.00 USD | 112.89 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 239,680.00 USD | 381.45 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 239,830.00 USD | 155.82 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 284,220.00 USD | 44,390.00 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 284,530.00 USD | 309.23 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 285,790.00 USD | 1,260.00 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 285,890.00 USD | 107.03 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,970,000.00 USD | 1,680,000.00 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,970,000.00 USD | 3,150.00 USD | 0.00 USD | `+9.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 1,970,000.00 USD | 1,470.00 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 1,970,000.00 USD | 107.71 USD | 0.00 USD | `+10.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 1,970,000.00 USD | 2,690.00 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 1,970,000.00 USD | 529.92 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 1,970,000.00 USD | 219.07 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,970,000.00 USD | 242.84 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 1,980,000.00 USD | 10,140.00 USD | 0.00 USD | `+11.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 1,990,000.00 USD | 876.11 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 1,990,000.00 USD | 812.54 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 1,990,000.00 USD | 126.76 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,990,000.00 USD | 307.41 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,990,000.00 USD | 614.09 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 1,990,000.00 USD | 859.50 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,990,000.00 USD | 2,020.00 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,030,000.00 USD | 43,760.00 USD | 0.00 USD | `+13.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,030,000.00 USD | 123.94 USD | 0.00 USD | `+13.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 2,030,000.00 USD | 271.53 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,040,000.00 USD | 1,550.00 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,040,000.00 USD | 1,840.00 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,040,000.00 USD | 2,760.00 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,040,000.00 USD | 117.71 USD | 0.00 USD | `+14.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,040,000.00 USD | 111.61 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,040,000.00 USD | 571.18 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,040,000.00 USD | 375.94 USD | 0.00 USD | `+15.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,040,000.00 USD | 627.55 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,040,000.00 USD | 211.04 USD | 0.00 USD | `+15.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,040,000.00 USD | 108.36 USD | 0.00 USD | `+16.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,040,000.00 USD | 543.32 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,040,000.00 USD | 1,820.00 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,050,000.00 USD | 2,080.00 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,060,000.00 USD | 17,680.00 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,070,000.00 USD | 1,370.00 USD | 0.00 USD | `+17.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,070,000.00 USD | 5,630.00 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,070,000.00 USD | 1,090.00 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,070,000.00 USD | 224.86 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,090,000.00 USD | 20,540.00 USD | 0.00 USD | `+18.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,090,000.00 USD | 114.93 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,090,000.00 USD | 679.12 USD | 0.00 USD | `+19.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,090,000.00 USD | 173.36 USD | 0.00 USD | `+19.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,100,000.00 USD | 1,810.00 USD | 0.00 USD | `+20.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,100,000.00 USD | 1,630.00 USD | 0.00 USD | `+20.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,100,000.00 USD | 2,280.00 USD | 0.00 USD | `+20.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,100,000.00 USD | 541.32 USD | 0.00 USD | `+20.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,240,000.00 USD | 137,500.00 USD | 0.00 USD | `+21.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,240,000.00 USD | 691.07 USD | 0.00 USD | `+21.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,250,000.00 USD | 6,250.00 USD | 0.00 USD | `+21.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,260,000.00 USD | 13,480.00 USD | 0.00 USD | `+21.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,260,000.00 USD | 734.82 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,260,000.00 USD | 1,230.00 USD | 0.00 USD | `+22.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,260,000.00 USD | 105.00 USD | 0.00 USD | `+22.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,260,000.00 USD | 184.09 USD | 0.00 USD | `+22.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,260,000.00 USD | 1,120.00 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,260,000.00 USD | 1,860.00 USD | 0.00 USD | `+23.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,260,000.00 USD | 1,070.00 USD | 0.00 USD | `+23.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,270,000.00 USD | 512.15 USD | 0.00 USD | `+23.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,270,000.00 USD | 6,620.00 USD | 0.00 USD | `+23.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,270,000.00 USD | 404.96 USD | 0.00 USD | `+24.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,270,000.00 USD | 129.85 USD | 0.00 USD | `+25.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,280,000.00 USD | 3,740.00 USD | 0.00 USD | `+25.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,280,000.00 USD | 409.17 USD | 0.00 USD | `+25.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,280,000.00 USD | 203.74 USD | 0.00 USD | `+26.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,280,000.00 USD | 2,800.00 USD | 0.00 USD | `+27.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,280,000.00 USD | 1,320.00 USD | 0.00 USD | `+27.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,280,000.00 USD | 694.56 USD | 0.00 USD | `+27.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,280,000.00 USD | 940.91 USD | 0.00 USD | `+28.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,290,000.00 USD | 2,980.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,290,000.00 USD | 104.99 USD | 0.00 USD | `+29.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,290,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,290,000.00 USD | 1,490.00 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,290,000.00 USD | 1,090.00 USD | 0.00 USD | `+30.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,290,000.00 USD | 438.96 USD | 0.00 USD | `+30.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,290,000.00 USD | 973.76 USD | 0.00 USD | `+30.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,300,000.00 USD | 10,000.00 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,300,000.00 USD | 175.59 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,300,000.00 USD | 2,060.00 USD | 0.00 USD | `+31.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,300,000.00 USD | 482.89 USD | 0.00 USD | `+32.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,300,000.00 USD | 201.90 USD | 0.00 USD | `+32.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,310,000.00 USD | 489.46 USD | 0.00 USD | `+32.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,310,000.00 USD | 103.68 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,310,000.00 USD | 2,590.00 USD | 0.00 USD | `+33.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,310,000.00 USD | 3,810.00 USD | 0.00 USD | `+33.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,320,000.00 USD | 11,200.00 USD | 0.00 USD | `+33.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,330,000.00 USD | 4,330.00 USD | 0.00 USD | `+33.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,330,000.00 USD | 205.50 USD | 0.00 USD | `+34.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,330,000.00 USD | 3,490.00 USD | 0.00 USD | `+34.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,330,000.00 USD | 1,300.00 USD | 0.00 USD | `+35.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,330,000.00 USD | 207.50 USD | 0.00 USD | `+35.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,330,000.00 USD | 813.88 USD | 0.00 USD | `+36.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,360,000.00 USD | 23,160.00 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,360,000.00 USD | 781.51 USD | 0.00 USD | `+37.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,360,000.00 USD | 209.30 USD | 0.00 USD | `+37.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,360,000.00 USD | 1,440.00 USD | 0.00 USD | `+37.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,360,000.00 USD | 5,140.00 USD | 0.00 USD | `+37.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,360,000.00 USD | 585.32 USD | 0.00 USD | `+38.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,360,000.00 USD | 210.90 USD | 0.00 USD | `+38.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,370,000.00 USD | 1,850.00 USD | 0.00 USD | `+38.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,370,000.00 USD | 105.75 USD | 0.00 USD | `+38.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,370,000.00 USD | 3,220.00 USD | 0.00 USD | `+38.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,370,000.00 USD | 1,600.00 USD | 0.00 USD | `+39.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,370,000.00 USD | 212.90 USD | 0.00 USD | `+39.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,370,000.00 USD | 472.63 USD | 0.00 USD | `+40.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,370,000.00 USD | 214.50 USD | 0.00 USD | `+40.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,370,000.00 USD | 1,040.00 USD | 0.00 USD | `+41.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,370,000.00 USD | 136.12 USD | 0.00 USD | `+41.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,370,000.00 USD | 216.10 USD | 0.00 USD | `+41.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,370,000.00 USD | 1,010.00 USD | 0.00 USD | `+42.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,370,000.00 USD | 217.90 USD | 0.00 USD | `+42.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,380,000.00 USD | 219.70 USD | 0.00 USD | `+43.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,380,000.00 USD | 7,780.00 USD | 0.00 USD | `+44.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,380,000.00 USD | 154.22 USD | 0.00 USD | `+44.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,380,000.00 USD | 221.30 USD | 0.00 USD | `+45.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,380,000.00 USD | 1,050.00 USD | 0.00 USD | `+45.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,410,000.00 USD | 24,190.00 USD | 0.00 USD | `+45.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,410,000.00 USD | 223.10 USD | 0.00 USD | `+46.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,410,000.00 USD | 224.70 USD | 0.00 USD | `+47.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,410,000.00 USD | 226.30 USD | 0.00 USD | `+48.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,410,000.00 USD | 950.34 USD | 0.00 USD | `+49.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,410,000.00 USD | 229.50 USD | 0.00 USD | `+50.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,410,000.00 USD | 771.08 USD | 0.00 USD | `+50.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,410,000.00 USD | 942.95 USD | 0.00 USD | `+50.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,410,000.00 USD | 230.90 USD | 0.00 USD | `+51.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,410,000.00 USD | 288.18 USD | 0.00 USD | `+51.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,410,000.00 USD | 619.10 USD | 0.00 USD | `+51.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,410,000.00 USD | 1,250.00 USD | 0.00 USD | `+51.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,420,000.00 USD | 1,050.00 USD | 0.00 USD | `+52.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,420,000.00 USD | 232.30 USD | 0.00 USD | `+52.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,420,000.00 USD | 1,600.00 USD | 0.00 USD | `+53.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,420,000.00 USD | 1,050.00 USD | 0.00 USD | `+53.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,420,000.00 USD | 3,730.00 USD | 0.00 USD | `+53.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,420,000.00 USD | 676.22 USD | 0.00 USD | `+54.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,420,000.00 USD | 648.25 USD | 0.00 USD | `+54.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,430,000.00 USD | 1,510.00 USD | 0.00 USD | `+54.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,430,000.00 USD | 448.52 USD | 0.00 USD | `+54.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,430,000.00 USD | 124.58 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,430,000.00 USD | 1,050.00 USD | 0.00 USD | `+56.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,430,000.00 USD | 691.80 USD | 0.00 USD | `+56.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,550,000.00 USD | 117,860.00 USD | 0.00 USD | `+57.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,550,000.00 USD | 143.22 USD | 0.00 USD | `+57.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,550,000.00 USD | 1,380.00 USD | 0.00 USD | `+58.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,550,000.00 USD | 2,270.00 USD | 0.00 USD | `+59.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,550,000.00 USD | 871.99 USD | 0.00 USD | `+60.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,580,000.00 USD | 29,610.00 USD | 0.00 USD | `+66.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,580,000.00 USD | 400.21 USD | 0.00 USD | `+66.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,590,000.00 USD | 13,850.00 USD | 0.00 USD | `+72.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,600,000.00 USD | 2,360.00 USD | 0.00 USD | `+73.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,600,000.00 USD | 4,160.00 USD | 0.00 USD | `+77.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,600,000.00 USD | 114.70 USD | 0.00 USD | `+78.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,600,000.00 USD | 278.50 USD | 0.00 USD | `+83.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,600,000.00 USD | 1,160.00 USD | 0.00 USD | `+85.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,600,000.00 USD | 173.57 USD | 0.00 USD | `+86.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,600,000.00 USD | 380.09 USD | 0.00 USD | `+86.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,620,000.00 USD | 17,150.00 USD | 0.00 USD | `+86.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,620,000.00 USD | 1,440.00 USD | 0.00 USD | `+88.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,620,000.00 USD | 433.35 USD | 0.00 USD | `+89.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,620,000.00 USD | 452.26 USD | 0.00 USD | `+91.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,630,000.00 USD | 3,640.00 USD | 0.00 USD | `+92.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,680,000.00 USD | 55,720.00 USD | 0.00 USD | `+93.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,680,000.00 USD | 2,120.00 USD | 0.00 USD | `+94.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,700,000.00 USD | 19,850.00 USD | 0.00 USD | `+96.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1514` | 2,700,000.00 USD | 1,620.00 USD | 0.00 USD | `+98.38%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.0680` | 15,450,000.00 USD | 0.00 USD | 15,450,000.00 USD | 49,820.00 USD | 47,880.00 USD | 6,870.00 USD |
| `1D` | `0.0681` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 17,070.00 USD | 27,520.00 USD | 139,180.00 USD |
| `1D` | `0.0682` | 15,160,000.00 USD | 0.00 USD | 15,160,000.00 USD | 2,550.00 USD | 33,950.00 USD | 20,750.00 USD |
| `1D` | `0.0683` | 15,100,000.00 USD | 0.00 USD | 15,100,000.00 USD | 15,780.00 USD | 26,860.00 USD | 467.62 USD |
| `1D` | `0.0684` | 15,060,000.00 USD | 0.00 USD | 15,060,000.00 USD | 24,150.00 USD | 15,070.00 USD | 899.29 USD |
| `1D` | `0.0685` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 58,140.00 USD | 13,720.00 USD | 22,890.00 USD |
| `1D` | `0.0686` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 45,490.00 USD | 8,860.00 USD | 13,680.00 USD |
| `1D` | `0.0687` | 14,850,000.00 USD | 0.00 USD | 14,850,000.00 USD | 9,250.00 USD | 24,710.00 USD | 29,590.00 USD |
| `1D` | `0.0688` | 14,790,000.00 USD | 0.00 USD | 14,790,000.00 USD | 6,710.00 USD | 4,630.00 USD | 34,370.00 USD |
| `1D` | `0.0689` | 14,750,000.00 USD | 0.00 USD | 14,750,000.00 USD | 9,350.00 USD | 0.00 USD | 1,130.00 USD |
| `1D` | `0.0690` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 1,520.00 USD |
| `1D` | `0.0691` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 1,460.00 USD | 0.00 USD | 1,540.00 USD |
| `1D` | `0.0692` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0693` | 14,710,000.00 USD | 0.00 USD | 14,710,000.00 USD | 18,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0694` | 14,690,000.00 USD | 0.00 USD | 14,690,000.00 USD | 27,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0695` | 14,660,000.00 USD | 0.00 USD | 14,660,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `1D` | `0.0697` | 14,660,000.00 USD | 0.00 USD | 14,660,000.00 USD | 31,720.00 USD | 13,590.00 USD | 16,440.00 USD |
| `1D` | `0.0698` | 14,600,000.00 USD | 0.00 USD | 14,600,000.00 USD | 14,010.00 USD | 10,800.00 USD | 9,960.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0699` | 14,560,000.00 USD | 0.00 USD | 14,560,000.00 USD | 83,570.00 USD | 27,620.00 USD | 32,760.00 USD |
| `1D` | `0.0700` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 141,150.00 USD | 21,100.00 USD | 37,530.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0701` | 14,220,000.00 USD | 0.00 USD | 14,220,000.00 USD | 51,480.00 USD | 115,140.00 USD | 14,560.00 USD |
| `1D` | `0.0702` | 14,040,000.00 USD | 0.00 USD | 14,040,000.00 USD | 87,840.00 USD | 36,120.00 USD | 59.13 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0703` | 13,910,000.00 USD | 0.00 USD | 13,910,000.00 USD | 175,640.00 USD | 66,830.00 USD | 18,580.00 USD |
| `1D` | `0.0704` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 24,140.00 USD | 45,140.00 USD | 22,200.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0705` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 40,970.00 USD | 30,720.00 USD | 55,500.00 USD |
| `1D` | `0.0706` | 13,430,000.00 USD | 0.00 USD | 13,430,000.00 USD | 21,850.00 USD | 1,120.00 USD | 15,630.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0707` | 13,400,000.00 USD | 0.00 USD | 13,400,000.00 USD | 140,160.00 USD | 69,310.00 USD | 45,730.00 USD |
| `1D` | `0.0708` | 13,140,000.00 USD | 0.00 USD | 13,140,000.00 USD | 69,400.00 USD | 62,000.00 USD | 107,390.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0709` | 12,900,000.00 USD | 0.00 USD | 12,900,000.00 USD | 36,870.00 USD | 82,010.00 USD | 148,720.00 USD |
| `1D` | `0.0710` | 12,630,000.00 USD | 0.00 USD | 12,630,000.00 USD | 117,230.00 USD | 91,550.00 USD | 119,960.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 12,300,000.00 USD | 0.00 USD | 12,300,000.00 USD | 46,900.00 USD | 25,670.00 USD | 43,530.00 USD |
| `1D` | `0.0712` | 12,190,000.00 USD | 0.00 USD | 12,190,000.00 USD | 159,040.00 USD | 46,690.00 USD | 3,350.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 11,980,000.00 USD | 0.00 USD | 11,980,000.00 USD | 70,910.00 USD | 85,230.00 USD | 63,930.00 USD |
| `1D` | `0.0714` | 11,760,000.00 USD | 0.00 USD | 11,760,000.00 USD | 118,420.00 USD | 51,930.00 USD | 48,070.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 73,470.00 USD | 238,460.00 USD | 43,090.00 USD |
| `1D` | `0.0716` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 19,480.00 USD | 51,080.00 USD | 0.00 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 11,120,000.00 USD | 0.00 USD | 11,120,000.00 USD | 232,360.00 USD | 96,160.00 USD | 137.40 USD |
| `1D` | `0.0718` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 55,690.00 USD | 101,030.00 USD | 13,040.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 10,620,000.00 USD | 0.00 USD | 10,620,000.00 USD | 226,040.00 USD | 45,330.00 USD | 72,220.00 USD |
| `1D` | `0.0720` | 10,270,000.00 USD | 0.00 USD | 10,270,000.00 USD | 135,290.00 USD | 50,600.00 USD | 72,110.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 308,410.00 USD | 298,040.00 USD | 67,520.00 USD |
| `1D` | `0.0722` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 179,490.00 USD | 119,590.00 USD | 149,770.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 82,600.00 USD | 258,330.00 USD | 326,730.00 USD |
| `1D` | `0.0724` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 111,400.00 USD | 206,000.00 USD | 370,890.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 234,040.00 USD | 201,810.00 USD | 268,780.00 USD |
| `1D` | `0.0726` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 29,310.00 USD | 90,560.00 USD | 8,290.00 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 138,060.00 USD | 83,300.00 USD | 17,610.00 USD |
| `1D` | `0.0728` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 27,890.00 USD | 84,500.00 USD | 28,810.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 42,630.00 USD | 26,380.00 USD | 9,760.00 USD |
| `1D` | `0.0730` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 105,290.00 USD | 26,630.00 USD | 44,470.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 35,610.00 USD | 68,840.00 USD | 14,170.00 USD |
| `1D` | `0.0732` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 65,770.00 USD | 40,460.00 USD | 80,640.00 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 36,920.00 USD | 69,930.00 USD | 28,340.00 USD |
| `1D` | `0.0734` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 339,370.00 USD | 67,440.00 USD | 0.00 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 141,790.00 USD | 23,950.00 USD | 0.00 USD |
| `1D` | `0.0736` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 37,590.00 USD | 189,640.00 USD | 16,660.00 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 113,510.00 USD | 47,850.00 USD | 49,860.00 USD |
| `1D` | `0.0738` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 83,080.00 USD | 23,440.00 USD | 0.00 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 54,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0740` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 54,250.00 USD | 0.00 USD | 34,130.00 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 0.00 USD | 68,120.00 USD | 0.00 USD |
| `1D` | `0.0742` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 133,790.00 USD | 24,700.00 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 174,420.00 USD | 40,680.00 USD | 245,490.00 USD |
| `1D` | `0.0744` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 185,610.00 USD | 89,270.00 USD | 107,270.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 54,460.00 USD | 32,770.00 USD | 34,320.00 USD |
| `1D` | `0.0746` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 71,220.00 USD | 64,390.00 USD | 189,880.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 643,140.00 USD | 225,930.00 USD | 178,650.00 USD |
| `1D` | `0.0748` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 130,110.00 USD | 43,650.00 USD | 233,550.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 73,840.00 USD | 38,480.00 USD | 125,020.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 37,490.00 USD | 0.00 USD |
| `1D` | `0.0752` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 24,430.00 USD | 0.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 0.00 USD | 12,650.00 USD | 141,640.00 USD |
| `1D` | `0.0754` | 926,030.00 USD | 0.00 USD | 926,030.00 USD | 0.00 USD | 103,430.00 USD | 278,380.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0755` | 544,220.00 USD | 0.00 USD | 544,220.00 USD | 182,850.00 USD | 180,020.00 USD | 0.00 USD |
| `1D` | `0.0756` | 181,360.00 USD | 0.00 USD | 181,360.00 USD | 0.00 USD | 30,100.00 USD | 0.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 151,260.00 USD | 0.00 USD | 151,260.00 USD | 130,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0758` | 20,690.00 USD | 0.00 USD | 20,690.00 USD | 15,180.00 USD | 4,920.00 USD | 0.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 581.36 USD | 0.00 USD | 581.36 USD | 0.00 USD | 0.00 USD | 160.56 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 420.80 USD | 0.00 USD | 420.80 USD | 0.00 USD | 0.00 USD | 420.80 USD |
| `1D` | `0.0762` | 168.86 USD | 168.86 USD | 0.00 USD | 0.00 USD | 0.00 USD | 168.86 USD |
| `1D` | `0.0762` | 337.72 USD | 337.72 USD | 0.00 USD | 0.00 USD | 0.00 USD | 168.86 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 51,500.00 USD | 51,500.00 USD | 0.00 USD | 4,000.00 USD | 47,160.00 USD | 0.00 USD |
| `1D` | `0.0764` | 83,840.00 USD | 83,840.00 USD | 0.00 USD | 17,520.00 USD | 14,830.00 USD | 0.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 666,050.00 USD | 666,050.00 USD | 0.00 USD | 233,890.00 USD | 248,870.00 USD | 99,440.00 USD |
| `1D` | `0.0766` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 586,470.00 USD | 522,700.00 USD | 40,340.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 246,530.00 USD | 337,770.00 USD | 159,130.00 USD |
| `1D` | `0.0768` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 224,320.00 USD | 93,770.00 USD | 594,750.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 259,990.00 USD | 421,270.00 USD | 287,630.00 USD |
| `1D` | `0.0770` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 396,020.00 USD | 179,710.00 USD | 403,750.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 223,340.00 USD | 343,810.00 USD | 149,070.00 USD |
| `1D` | `0.0772` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 390,170.00 USD | 170,860.00 USD | 709,530.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 129,080.00 USD | 228,140.00 USD | 204,700.00 USD |
| `1D` | `0.0774` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 86,950.00 USD | 217,280.00 USD | 36,420.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 255,450.00 USD | 123,530.00 USD | 48,600.00 USD |
| `1D` | `0.0776` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 267,580.00 USD | 189,880.00 USD | 114,090.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 276,300.00 USD | 301,970.00 USD | 145,080.00 USD |
| `1D` | `0.0778` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 88,720.00 USD | 274,410.00 USD | 395,660.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 296,890.00 USD | 158,150.00 USD | 199,070.00 USD |
| `1D` | `0.0780` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 174,020.00 USD | 53,140.00 USD | 39,560.00 USD |
| `1D` | `0.0781` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 151,030.00 USD | 193,800.00 USD | 8,910.00 USD |
| `1D` | `0.0782` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 70,430.00 USD | 82,140.00 USD | 79,320.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 45,800.00 USD | 214,890.00 USD | 177,310.00 USD |
| `1D` | `0.0784` | 13,190,000.00 USD | 13,190,000.00 USD | 0.00 USD | 316,220.00 USD | 101,430.00 USD | 39,240.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 205,570.00 USD | 110,520.00 USD | 78,950.00 USD |
| `1D` | `0.0786` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 234,330.00 USD | 160,700.00 USD | 245,200.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 329,770.00 USD | 386,280.00 USD | 358,360.00 USD |
| `1D` | `0.0788` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 135,470.00 USD | 191,940.00 USD | 104,030.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 16,350,000.00 USD | 16,350,000.00 USD | 0.00 USD | 296,490.00 USD | 218,540.00 USD | 102,060.00 USD |
| `1D` | `0.0790` | 16,570,000.00 USD | 16,570,000.00 USD | 0.00 USD | 136,170.00 USD | 58,560.00 USD | 20,930.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 188,560.00 USD | 121,290.00 USD | 110,820.00 USD |
| `1D` | `0.0792` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 158,350.00 USD | 37,510.00 USD | 65,540.00 USD |
| `1D` | `0.0793` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 41.60 USD |
| `1D` | `0.0794` | 17,540,000.00 USD | 17,540,000.00 USD | 0.00 USD | 128,100.00 USD | 63,190.00 USD | 96,870.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0795` | 17,720,000.00 USD | 17,720,000.00 USD | 0.00 USD | 61,440.00 USD | 19,240.00 USD | 100,470.00 USD |
| `1D` | `0.0796` | 17,910,000.00 USD | 17,910,000.00 USD | 0.00 USD | 174,010.00 USD | 0.00 USD | 18,140.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 18,320,000.00 USD | 18,320,000.00 USD | 0.00 USD | 206,810.00 USD | 89,760.00 USD | 115,620.00 USD |
| `1D` | `0.0798` | 18,490,000.00 USD | 18,490,000.00 USD | 0.00 USD | 56,190.00 USD | 110,930.00 USD | 2,080.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 157,480.00 USD | 193,600.00 USD | 142,000.00 USD |
| `1D` | `0.0800` | 19,130,000.00 USD | 19,130,000.00 USD | 0.00 USD | 45,460.00 USD | 9,760.00 USD | 95,080.00 USD |
| `1D` | `0.0801` | 19,150,000.00 USD | 19,150,000.00 USD | 0.00 USD | 17,000.00 USD | 0.00 USD | 617.52 USD |
| `1D` | `0.0802` | 19,170,000.00 USD | 19,170,000.00 USD | 0.00 USD | 18,910.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `0.0803` | 19,270,000.00 USD | 19,270,000.00 USD | 0.00 USD | 16,230.00 USD | 43,340.00 USD | 41,200.00 USD |
| `1D` | `0.0804` | 19,290,000.00 USD | 19,290,000.00 USD | 0.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 19,460,000.00 USD | 19,460,000.00 USD | 0.00 USD | 89,620.00 USD | 37,230.00 USD | 41,110.00 USD |
| `1D` | `0.0806` | 19,720,000.00 USD | 19,720,000.00 USD | 0.00 USD | 24,270.00 USD | 21,040.00 USD | 215,330.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 221,690.00 USD | 145,040.00 USD | 30,480.00 USD |
| `1D` | `0.0808` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 297,680.00 USD | 118,270.00 USD | 458,880.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 21,530,000.00 USD | 21,530,000.00 USD | 0.00 USD | 252,300.00 USD | 275,640.00 USD | 12,790.00 USD |
| `1D` | `0.0810` | 22,070,000.00 USD | 22,070,000.00 USD | 0.00 USD | 252,220.00 USD | 157,180.00 USD | 132,930.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 22,410,000.00 USD | 22,410,000.00 USD | 0.00 USD | 98,200.00 USD | 229,260.00 USD | 10,910.00 USD |
| `1D` | `0.0812` | 22,730,000.00 USD | 22,730,000.00 USD | 0.00 USD | 138,630.00 USD | 102,020.00 USD | 77,290.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 22,920,000.00 USD | 22,920,000.00 USD | 0.00 USD | 47,380.00 USD | 33,440.00 USD | 109,320.00 USD |
| `1D` | `0.0814` | 23,270,000.00 USD | 23,270,000.00 USD | 0.00 USD | 39,620.00 USD | 109,560.00 USD | 200,910.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 23,400,000.00 USD | 23,400,000.00 USD | 0.00 USD | 33,530.00 USD | 6,740.00 USD | 94,640.00 USD |
| `1D` | `0.0816` | 24,120,000.00 USD | 24,120,000.00 USD | 0.00 USD | 340,210.00 USD | 194,310.00 USD | 179,640.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 24,670,000.00 USD | 24,670,000.00 USD | 0.00 USD | 284,640.00 USD | 134,560.00 USD | 130,180.00 USD |
| `1D` | `0.0818` | 25,340,000.00 USD | 25,340,000.00 USD | 0.00 USD | 247,200.00 USD | 161,260.00 USD | 268,040.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 25,940,000.00 USD | 25,940,000.00 USD | 0.00 USD | 161,320.00 USD | 312,480.00 USD | 128,570.00 USD |
| `1D` | `0.0820` | 26,490,000.00 USD | 26,490,000.00 USD | 0.00 USD | 52,420.00 USD | 172,050.00 USD | 319,880.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 26,780,000.00 USD | 26,780,000.00 USD | 0.00 USD | 156,680.00 USD | 48,110.00 USD | 85,310.00 USD |
| `1D` | `0.0822` | 27,340,000.00 USD | 27,340,000.00 USD | 0.00 USD | 252,350.00 USD | 151,600.00 USD | 156,380.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 27,690,000.00 USD | 27,690,000.00 USD | 0.00 USD | 270,020.00 USD | 72,540.00 USD | 8,520.00 USD |
| `1D` | `0.0824` | 28,260,000.00 USD | 28,260,000.00 USD | 0.00 USD | 168,680.00 USD | 204,930.00 USD | 190,880.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 28,510,000.00 USD | 28,510,000.00 USD | 0.00 USD | 102,430.00 USD | 125,690.00 USD | 22,000.00 USD |
| `1D` | `0.0826` | 28,930,000.00 USD | 28,930,000.00 USD | 0.00 USD | 131,950.00 USD | 125,260.00 USD | 170,210.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 29,020,000.00 USD | 29,020,000.00 USD | 0.00 USD | 13,110.00 USD | 62,110.00 USD | 16,660.00 USD |
| `1D` | `0.0828` | 29,360,000.00 USD | 29,360,000.00 USD | 0.00 USD | 197,110.00 USD | 75,940.00 USD | 66,570.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 29,610,000.00 USD | 29,610,000.00 USD | 0.00 USD | 157,080.00 USD | 88,230.00 USD | 361.06 USD |
| `1D` | `0.0830` | 29,750,000.00 USD | 29,750,000.00 USD | 0.00 USD | 57,230.00 USD | 37,820.00 USD | 43,280.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 29,810,000.00 USD | 29,810,000.00 USD | 0.00 USD | 31,420.00 USD | 0.00 USD | 30,900.00 USD |
| `1D` | `0.0832` | 30,120,000.00 USD | 30,120,000.00 USD | 0.00 USD | 154,910.00 USD | 75,990.00 USD | 80,200.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 30,490,000.00 USD | 30,490,000.00 USD | 0.00 USD | 110,470.00 USD | 82,770.00 USD | 170,550.00 USD |
| `1D` | `0.0834` | 30,840,000.00 USD | 30,840,000.00 USD | 0.00 USD | 119,430.00 USD | 94,190.00 USD | 138,030.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 31,200,000.00 USD | 31,200,000.00 USD | 0.00 USD | 111,520.00 USD | 183,090.00 USD | 64,580.00 USD |
| `1D` | `0.0836` | 31,450,000.00 USD | 31,450,000.00 USD | 0.00 USD | 44,050.00 USD | 63,220.00 USD | 144,990.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 31,670,000.00 USD | 31,670,000.00 USD | 0.00 USD | 132,640.00 USD | 31,430.00 USD | 56,850.00 USD |
| `1D` | `0.0838` | 31,960,000.00 USD | 31,960,000.00 USD | 0.00 USD | 169,750.00 USD | 77,480.00 USD | 39,200.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 32,060,000.00 USD | 32,060,000.00 USD | 0.00 USD | 52,570.00 USD | 24,710.00 USD | 30,110.00 USD |
| `1D` | `0.0840` | 32,140,000.00 USD | 32,140,000.00 USD | 0.00 USD | 18,280.00 USD | 20,110.00 USD | 34,960.00 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0841` | 32,150,000.00 USD | 32,150,000.00 USD | 0.00 USD | 9,490.00 USD | 2,010.00 USD | 608.34 USD |
| `1D` | `0.0842` | 32,220,000.00 USD | 32,220,000.00 USD | 0.00 USD | 22,710.00 USD | 0.00 USD | 46,530.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 32,250,000.00 USD | 32,250,000.00 USD | 0.00 USD | 33,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0844` | 32,310,000.00 USD | 32,310,000.00 USD | 0.00 USD | 59,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `7D` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `7D` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `7D` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD |
| `7D` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 0.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD |
| `7D` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 0.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD |
| `7D` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD |
| `7D` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD |
| `7D` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 0.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `7D` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 0.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD |
| `7D` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD |
| `7D` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 0.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD |
| `7D` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 0.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD |
| `7D` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD |
| `7D` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD |
| `7D` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 0.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD |
| `7D` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 0.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD |
| `7D` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 0.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD |
| `7D` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 0.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD |
| `7D` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 0.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD |
| `7D` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 0.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD |
| `7D` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 0.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 0.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD |
| `7D` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 0.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD |
| `7D` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 0.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.06B` | Total OI Tokens: `13,945,205,674.4 DOGE`
  * 1h OI Change: `+0.42%` | 4h OI Change: `+3.66%` | 24h OI Change: `-4.79%`
  * Exchange Breakdown: Binance=`243.62M` | Bybit=`106.89M` | OKX=`109.92M` | Hyperliquid=`76.77M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `15.41K` | Last 24h: `35.55K` | Last 3d: `229.21K` | Last 7d: `310.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0037%` |
| **USDT Bybit** | `-0.0027%` | **USDT KuCoin** | `0.0016%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0006%` | **USDT Bitget** | `0.0029%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `36.76%` | `63.24%` | `0.58` | 113,290,000.00 USD |
| `15M` | `Binance` | `40.12%` | `59.88%` | `0.67` | 31,480,000.00 USD |
| `15M` | `OKX` | `31.82%` | `68.18%` | `0.47` | 22,320,000.00 USD |
| `15M` | `Bybit` | `36.64%` | `63.36%` | `0.58` | 13,330,000.00 USD |
| `15M` | `KuCoin` | `37.44%` | `62.56%` | `0.60` | 479,630.00 USD |
| `15M` | `Gate` | `51.7%` | `48.3%` | `1.07` | 7,820,000.00 USD |
| `15M` | `Bitget` | `25.49%` | `74.51%` | `0.34` | 6,790,000.00 USD |
| `15M` | `BingX` | `34.53%` | `65.47%` | `0.53` | 3,210,000.00 USD |
| `15M` | `MEXC` | `27.33%` | `72.67%` | `0.38` | 10,800,000.00 USD |
| `15M` | `Bitunix` | `44.22%` | `55.78%` | `0.79` | 7,150,000.00 USD |
| `15M` | `Hyperliquid` | `49.34%` | `50.66%` | `0.97` | 3,690,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `35.94%` | `64.06%` | `0.56` | 606,610.00 USD |
| `15M` | `Crypto.com` | `49.9%` | `50.1%` | `1.00` | 128,320.00 USD |
| `15M` | `WhiteBIT` | `99.91%` | `0.09%` | `1110.11` | 794,450.00 USD |
| `15M` | `HTX` | `39.33%` | `60.67%` | `0.65` | 90,110.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `26.71%` | `73.29%` | `0.36` | 924,490.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `18.37%` | `81.63%` | `0.23` | 3,660,000.00 USD |
| `15M` | `Whale Positions` | `40.12%` | `59.88%` | `0.67` | 31,480,000.00 USD |
| `15M` | `Global Accounts` | `36.76%` | `63.24%` | `0.58` | 113,290,000.00 USD |
| `1H` | `DOGE` | `46.47%` | `53.53%` | `0.87` | 342,790,000.00 USD |
| `1H` | `Binance` | `46.01%` | `53.99%` | `0.85` | 97,410,000.00 USD |
| `1H` | `OKX` | `46.5%` | `53.5%` | `0.87` | 69,620,000.00 USD |
| `1H` | `Bybit` | `42.38%` | `57.62%` | `0.74` | 48,260,000.00 USD |
| `1H` | `KuCoin` | `48.09%` | `51.91%` | `0.93` | 1,570,000.00 USD |
| `1H` | `Gate` | `53.58%` | `46.42%` | `1.15` | 23,480,000.00 USD |
| `1H` | `Bitget` | `43.92%` | `56.08%` | `0.78` | 15,100,000.00 USD |
| `1H` | `BingX` | `49.23%` | `50.77%` | `0.97` | 14,240,000.00 USD |
| `1H` | `MEXC` | `36.98%` | `63.02%` | `0.59` | 24,170,000.00 USD |
| `1H` | `Bitunix` | `46.96%` | `53.04%` | `0.89` | 20,160,000.00 USD |
| `1H` | `Hyperliquid` | `57.59%` | `42.41%` | `1.36` | 14,650,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.15%` | `50.85%` | `0.97` | 1,530,000.00 USD |
| `1H` | `Crypto.com` | `52.12%` | `47.88%` | `1.09` | 454,050.00 USD |
| `1H` | `WhiteBIT` | `99.51%` | `0.49%` | `203.08` | 3,500,000.00 USD |
| `1H` | `HTX` | `59.15%` | `40.85%` | `1.45` | 602,540.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `44.89%` | `55.11%` | `0.81` | 2,340,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `34.18%` | `65.82%` | `0.52` | 5,710,000.00 USD |
| `1H` | `Whale Positions` | `46.01%` | `53.99%` | `0.85` | 97,410,000.00 USD |
| `1H` | `Global Accounts` | `46.47%` | `53.53%` | `0.87` | 342,790,000.00 USD |
| `4H` | `DOGE` | `51.94%` | `48.06%` | `1.08` | 1,350,000,000.00 USD |
| `4H` | `Binance` | `52.34%` | `47.66%` | `1.10` | 424,750,000.00 USD |
| `4H` | `OKX` | `54.66%` | `45.34%` | `1.21` | 271,030,000.00 USD |
| `4H` | `Bybit` | `51.5%` | `48.5%` | `1.06` | 141,190,000.00 USD |
| `4H` | `KuCoin` | `54.9%` | `45.1%` | `1.22` | 9,980,000.00 USD |
| `4H` | `Gate` | `53.65%` | `46.35%` | `1.16` | 85,090,000.00 USD |
| `4H` | `Bitget` | `52.25%` | `47.75%` | `1.09` | 51,900,000.00 USD |
| `4H` | `BingX` | `48.44%` | `51.56%` | `0.94` | 52,190,000.00 USD |
| `4H` | `MEXC` | `42.14%` | `57.86%` | `0.73` | 108,840,000.00 USD |
| `4H` | `Bitunix` | `49.59%` | `50.41%` | `0.98` | 78,780,000.00 USD |
| `4H` | `Hyperliquid` | `50.88%` | `49.12%` | `1.04` | 64,410,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.17%` | `49.83%` | `1.01` | 9,640,000.00 USD |
| `4H` | `Crypto.com` | `54.53%` | `45.47%` | `1.20` | 2,070,000.00 USD |
| `4H` | `WhiteBIT` | `86.83%` | `13.17%` | `6.59` | 13,470,000.00 USD |
| `4H` | `HTX` | `60.03%` | `39.97%` | `1.50` | 2,660,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `37.22%` | `62.78%` | `0.59` | 442,060.00 USD |
| `4H` | `Aster` | `53.75%` | `46.25%` | `1.16` | 12,690,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.44%` | `49.56%` | `1.02` | 15,900,000.00 USD |
| `4H` | `Whale Positions` | `52.34%` | `47.66%` | `1.10` | 424,750,000.00 USD |
| `4H` | `Global Accounts` | `51.94%` | `48.06%` | `1.08` | 1,350,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0761` | `0.0760` | `0.0761` | `0.0761` | `0.0758` | 4,745,125.96 USD | 2,439,783.51 USD | 2,305,342.45 USD | 134,441.06 USD | `+2.83%` | `2B / 3S` |
| `0:00 UTC` | `0.0759` | `0.0758` | `0.0759` | `0.0761` | `0.0756` | 6,291,103.20 USD | 2,334,096.16 USD | 3,957,007.04 USD | -1,622,910.88 USD | `-25.80%` | `4B / 13S` |
| `5:00 UTC` | `0.0761` | `0.0761` | `0.0761` | `0.0763` | `0.0759` | 2,882,835.87 USD | 1,316,913.19 USD | 1,565,922.69 USD | -249,009.50 USD | `-8.64%` | `1B / 8S` |
| `0:00 UTC` | `0.0763` | `0.0763` | `0.0763` | `0.0764` | `0.0761` | 3,656,750.71 USD | 1,701,724.26 USD | 1,955,026.45 USD | -253,302.19 USD | `-6.93%` | `3B / 3S` |
| `5:00 UTC` | `0.0762` | `0.0762` | `0.0762` | `0.0764` | `0.0761` | 3,864,288.50 USD | 2,052,128.75 USD | 1,812,159.75 USD | 239,969.00 USD | `+6.21%` | `3B / 3S` |
| `0:00 UTC` | `0.0765` | `0.0763` | `0.0765` | `0.0765` | `0.0761` | 4,863,943.78 USD | 2,443,195.66 USD | 2,420,748.13 USD | 22,447.53 USD | `+0.46%` | `5B / 3S` |
| `5:00 UTC` | `0.0764` | `0.0764` | `0.0764` | `0.0765` | `0.0763` | 2,511,233.10 USD | 1,361,891.00 USD | 1,149,342.10 USD | 212,548.89 USD | `+8.46%` | `5B / 0S` |
| `0:00 UTC` | `0.0764` | `0.0764` | `0.0764` | `0.0766` | `0.0763` | 2,569,719.99 USD | 1,320,411.91 USD | 1,249,308.08 USD | 71,103.82 USD | `+2.77%` | `1B / 5S` |
| `5:00 UTC` | `0.0761` | `0.0762` | `0.0761` | `0.0765` | `0.0761` | 2,887,550.28 USD | 1,144,018.04 USD | 1,743,532.24 USD | -599,514.19 USD | `-20.76%` | `1B / 15S` |
| `0:00 UTC` | `0.0762` | `0.0762` | `0.0762` | `0.0763` | `0.0760` | 2,139,726.27 USD | 1,113,517.24 USD | 1,026,209.03 USD | 87,308.21 USD | `+4.08%` | `4B / 1S` |

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
| `5m` | -54,850.00 USD | 384,040.00 USD | **`ACCUMULATION`** |
| `15m` | -172,300.00 USD | -890,780.00 USD | **`DISTRIBUTION`** |
| `30m` | -417,490.00 USD | -1,270,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -476,910.00 USD | -775,480.00 USD | **`DISTRIBUTION`** |
| `2h` | 1,290,000.00 USD | -476,540.00 USD | **`ACCUMULATION`** |
| `4h` | 3,700,000.00 USD | 5,100,000.00 USD | **`ACCUMULATION`** |
| `6h` | -4,720,000.00 USD | -16,650,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -7,160,000.00 USD | -28,240,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -18,290,000.00 USD | -53,960,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -17,920,000.00 USD | -60,780,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -58,860,000.00 USD | -188,130,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -284,170,000.00 USD | -798,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-54.85K` | 15m=`-172.30K` | 1h=`-476.91K` | 24h=`-17.92M`
* Futures Capital Netflows: 5m=`+384.04K` | 15m=`-890.78K` | 1h=`-775.48K` | 24h=`-60.78M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0733` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0695` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0838`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0757` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0795` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0652`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0769`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
