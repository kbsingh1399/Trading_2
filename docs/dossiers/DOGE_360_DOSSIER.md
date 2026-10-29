# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 02:39:45 IST` (`2026-10-29 21:09:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0739` | **Live Ask Quote**: `0.0760` | **Mid Price**: `0.0749`
- **Spread Points**: `21.00` | **Spread BPS**: `280.19 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0774` | VWAP Z-Score: `-2.51` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.000729` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `17.36` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0813` | Lower -3.00σ Band: `0.0735`
  * Upper +2.51σ Band: `0.0806` | Lower -2.51σ Band: `0.0741`
  * Upper +2.01σ Band: `0.0800` | Lower -2.01σ Band: `0.0747`
  * Upper +2.00σ Band: `0.0800` | Lower -2.00σ Band: `0.0748`
  * Upper +1.28σ Band: `0.0790` | Lower -1.28σ Band: `0.0757`
  * Upper +1.00σ Band: `0.0787` | Lower -1.00σ Band: `0.0761`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0766` | EMA-20=`0.0774` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0778` (Slope: `+0.0000`) | EMA-100=`0.0778`
  * Institutional Anchors: EMA-144=`0.0777` | EMA-200=`0.0776` (Slope: `-0.0468`) | EMA-233=`0.0775`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0733` | Weekly High=`0.0803` | Weekly Low=`0.0733`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0740` (Distance: `+1.54%`)
  * Point of Control (POC) = `0.0738` (Distance: `+1.83%`)
  * Value Area Low (VAL) = `0.0738` (Distance: `+1.83%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0782` | Weekly POC=`0.0761` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0741` | Low=`0.0738`
  * London Session (08:00-16:00 UTC): High=`0.0752` | Low=`0.0747`
  * New York Session (13:00-21:00 UTC): High=`0.0754` | Low=`0.0745`
  * Initial Balance (First Hour): IB High=`0.0752` | IB Low=`0.0747`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0747` - `0.0752`
  * Optimal Trade Entry (OTE 0.705): `0.0751`
  * Structural Invalidation Anchor (0.786): `0.0755`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0757` | `0.0758` | `0.0751` | `0.0753` | `108,869,011` | 8,214,896.07 USD | -990,783.63 USD | `-12.06%` | -31,912,998.57 USD | `-0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.0753` | `0.0757` | `0.0750` | `0.0750` | `187,881,278` | 14,152,693.49 USD | 255,566.63 USD | `+1.81%` | -31,657,431.94 USD | `+0.58` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.0750` | `0.0752` | `0.0749` | `0.0752` | `13,969,263` | 1,047,666.28 USD | -144,090.10 USD | `-13.75%` | -31,801,522.04 USD | `+0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.0784` | `0.0785` | `0.0752` | `0.0756` | `728,358,892` | 55,822,204.41 USD | -10,033,903.33 USD | `-17.97%` | -25,764,708.11 USD | `-3.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.0756` | `0.0761` | `0.0742` | `0.0753` | `803,424,264` | 60,549,155.39 USD | -6,174,284.35 USD | `-10.20%` | -31,938,992.46 USD | `-1.96` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.0753` | `0.0757` | `0.0749` | `0.0752` | `201,850,541` | 15,200,359.77 USD | 111,476.53 USD | `+0.73%` | -31,827,515.93 USD | `+0.49` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.0793` | `0.0795` | `0.0790` | `0.0793` | `99,331,512` | 7,872,201.47 USD | -219,088.96 USD | `-2.78%` | -13,221,722.80 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0792` | `0.0793` | `0.0742` | `0.0753` | `1,891,844,576` | 144,606,422.97 USD | -19,167,046.23 USD | `-13.25%` | -32,388,769.03 USD | `-4.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0753` | `0.0757` | `0.0749` | `0.0751` | `199,676,468` | 15,037,073.46 USD | 52,746.30 USD | `+0.35%` | -32,336,022.73 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0751` | `2,094,017,000` | 159,830,972.76 USD | -19,077,213.06 USD | `-11.94%` | -31,902,638.57 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -11,383,503.61 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -14,406,508.13 USD | `+1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0751` | `2,094,017,000` | 159,830,972.76 USD | -19,077,213.06 USD | `-11.94%` | -31,902,638.57 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.0749`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.0752` | `4983.0000` | 374.94 USD | 374.94 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0752` | `4983.0000` | 374.93 USD | 749.87 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0752` | `4983.0000` | 374.93 USD | 1,124.79 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0752` | `4984.0000` | 375.00 USD | 1,499.79 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0752` | `99854.0000` | 7,512.92 USD | 9,012.70 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `0.0752` | `17913.0000` | 1,347.61 USD | 10,360.32 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0752` | `151543.0000` | 11,399.97 USD | 21,760.29 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0752` | `151545.0000` | 11,399.97 USD | 33,160.26 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0752` | `189491.0000` | 14,254.27 USD | 47,414.53 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `0.0752` | `208162.0000` | 15,658.57 USD | 63,073.10 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `0.0752` | `48087.0000` | 3,617.15 USD | 66,690.26 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0752` | `17919.0000` | 1,347.78 USD | 68,038.03 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0752` | `303874.0000` | 22,854.67 USD | 90,892.70 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `0.0752` | `11200.0000` | 842.35 USD | 91,735.05 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0752` | `11200.0000` | 842.34 USD | 92,577.39 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0752` | `11200.0000` | 842.33 USD | 93,419.72 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0752` | `11376.0000` | 855.55 USD | 94,275.28 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `0.0752` | `27142.0000` | 2,041.24 USD | 96,316.52 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `0.0752` | `278535.0000` | 20,946.95 USD | 117,263.47 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `0.0752` | `17919.0000` | 1,347.56 USD | 118,611.03 USD | `1 orders` | `-0.08%` | `-` |
| `ASK` | `0.0753` | `14268.0000` | 1,074.98 USD | 132,189.34 USD | `1 orders` | `+0.11%` | `-` |
| `ASK` | `0.0753` | `32464.0000` | 2,445.81 USD | 131,114.36 USD | `2 orders` | `+0.10%` | `-` |
| `ASK` | `0.0753` | `92932.0000` | 7,001.31 USD | 128,668.55 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `0.0753` | `266067.0000` | 20,044.69 USD | 121,667.24 USD | `2 orders` | `+0.10%` | `-` |
| `ASK` | `0.0753` | `560926.0000` | 42,254.56 USD | 101,622.55 USD | `2 orders` | `+0.09%` | `-` |
| `ASK` | `0.0753` | `2300.0000` | 173.26 USD | 59,367.99 USD | `2 orders` | `+0.09%` | `-` |
| `ASK` | `0.0753` | `62449.0000` | 4,704.16 USD | 59,194.74 USD | `2 orders` | `+0.09%` | `-` |
| `ASK` | `0.0753` | `133458.0000` | 10,052.99 USD | 54,490.58 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `0.0753` | `48087.0000` | 3,622.15 USD | 44,437.59 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `0.0753` | `3888.0000` | 292.84 USD | 40,815.43 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `0.0753` | `69334.0000` | 5,221.96 USD | 40,522.59 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `0.0753` | `2322.0000` | 174.88 USD | 35,300.64 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `0.0753` | `15942.0000` | 1,200.64 USD | 35,125.75 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `0.0753` | `18368.0000` | 1,383.33 USD | 33,925.11 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `0.0753` | `2656.0000` | 200.03 USD | 32,541.78 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `0.0753` | `410831.0000` | 30,938.45 USD | 32,341.76 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `0.0753` | `1037.0000` | 78.08 USD | 1,403.31 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `0.0753` | `16035.0000` | 1,207.26 USD | 1,325.22 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0753` | `664.0000` | 49.99 USD | 117.97 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0753` | `903.0000` | 67.98 USD | 67.98 USD | `1 orders` | `+0.02%` | `-` |
| `MID_SPREAD` | `0.0753` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `312` | `0xb83d...6e36` | `SHORT` | 7,733,959.87 USD | `102,645,925.00` | `0.0946` | `0.0755` | `1.49` | 1,973,381.79 USD | `+25.52%` | `3X Cross` |
| `316` | `0xc63a...a3cd` | `LONG` | 7,538,000.00 USD | `100,000,000.00` | `0.0856` | `0.0755` | `0.000000` | -1,026,821.96 USD | `-13.62%` | `10X Cross` |
| `318` | `0x610b...b613` | `LONG` | 7,447,144.35 USD | `98,666,424.00` | `0.0872` | `0.0755` | `0.0605` | -1,153,037.55 USD | `-15.48%` | `5X Cross` |
| `609` | `0x5b5d...c060` | `SHORT` | 3,728,981.44 USD | `49,478,955.00` | `0.0946` | `0.0755` | `3.56` | 952,535.16 USD | `+25.54%` | `3X Cross` |
| `648` | `0xca49...53c8` | `SHORT` | 3,491,396.81 USD | `46,542,649.00` | `0.0929` | `0.0755` | `0.3885` | 834,647.87 USD | `+23.91%` | `10X Cross` |
| `663` | `0x45d2...4029` | `SHORT` | 3,407,495.11 USD | `45,426,000.00` | `0.0954` | `0.0755` | `0.9656` | 928,134.11 USD | `+27.24%` | `10X Cross` |
| `814` | `0xecb6...2b00` | `SHORT` | 2,787,954.73 USD | `37,002,027.00` | `0.0796` | `0.0755` | `0.7797` | 155,565.55 USD | `+5.58%` | `10X Cross` |
| `1207` | `0x458d...ab3b` | `LONG` | 1,844,569.97 USD | `24,454,063.00` | `0.1002` | `0.0755` | `0.0714` | -606,351.93 USD | `-32.87%` | `3X Isolated` |
| `1221` | `0xeadc...9d55` | `LONG` | 1,832,319.10 USD | `24,317,440.00` | `0.0926` | `0.0755` | `0.000000` | -419,275.47 USD | `-22.88%` | `10X Cross` |
| `1260` | `0x9aa5...58af` | `SHORT` | 1,771,021.18 USD | `23,500,500.00` | `0.0907` | `0.0755` | `0.4572` | 359,733.77 USD | `+20.31%` | `10X Cross` |
| `1357` | `0xf48f...10fe` | `LONG` | 1,620,870.32 USD | `21,424,497.00` | `0.0968` | `0.0755` | `0.0488` | -453,434.29 USD | `-27.97%` | `4X Cross` |
| `1388` | `0x9946...0852` | `SHORT` | 1,581,371.84 USD | `20,910,149.00` | `0.0871` | `0.0755` | `0.1501` | 239,183.55 USD | `+15.13%` | `10X Cross` |
| `1568` | `0xcac1...26b3` | `SHORT` | 1,370,207.46 USD | `18,126,835.00` | `0.0943` | `0.0755` | `0.5347` | 339,251.74 USD | `+24.76%` | `10X Cross` |
| `1601` | `0x0d6a...ca57` | `LONG` | 1,331,396.65 USD | `17,626,455.00` | `0.0875` | `0.0755` | `0.0626` | -210,708.31 USD | `-15.83%` | `3X Isolated` |
| `1661` | `0x4808...a82c` | `LONG` | 1,268,185.68 USD | `16,828,143.00` | `0.0883` | `0.0755` | `0.0632` | -218,287.30 USD | `-17.21%` | `3X Cross` |
| `1776` | `0x31ef...f715` | `LONG` | 1,148,806.59 USD | `15,230,102.00` | `0.0936` | `0.0755` | `0.0668` | -276,889.34 USD | `-24.10%` | `3X Isolated` |
| `1795` | `0xbfc7...80b4` | `SHORT` | 1,132,447.92 USD | `15,020,000.00` | `0.0920` | `0.0755` | `0.4333` | 249,951.37 USD | `+22.07%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 1,353.48 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 1.35K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 1,353.46 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 1.35K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 737.72 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.74K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 794.60 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.79K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 9,333.65 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 9.33K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 552.07 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.55K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 3,532.42 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 3.53K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 83.19 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.08K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 1,278.32 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 1.28K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 11.44 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 0.01K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0794` | 2,003.47 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 2.00K USD at 0.0794 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0794` | 7,000.96 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 7.00K USD at 0.0794 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0794` | 1,650.77 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 1.65K USD at 0.0794 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0794` | 2,503.76 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Short: 2.50K USD at 0.0794 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0794` | 27,033.60 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 27.03K USD at 0.0794 USD [API] | `2026-10-28 02:19:16` |
| `ANNOUNCEMENT` | `INFO` | `0.0794` | 11,660.64 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 11.66K USD at 0.0794 USD [API] | `2026-10-28 02:19:16` |
| `ANNOUNCEMENT` | `INFO` | `0.0793` | 6,166.72 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.17K USD at 0.0793 USD [API] | `2026-10-28 02:21:39` |
| `ANNOUNCEMENT` | `INFO` | `0.0794` | 13,014.78 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 13.01K USD at 0.0794 USD [API] | `2026-10-28 04:23:16` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 11,667.39 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 11.67K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 9,333.65 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 9.33K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0794` | 7,000.96 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 7.00K USD at 0.0794 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0797` | 10,341.94 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.34K USD at 0.0797 USD [API] | `2026-10-28 04:39:47` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 6,283.05 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.28K USD at 0.0800 USD [API] | `2026-10-28 07:48:18` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 9,007.07 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 9.01K USD at 0.0800 USD [API] | `2026-10-28 07:48:18` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 30,942.20 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 30.94K USD at 0.0800 USD [API] | `2026-10-28 07:48:18` |
| `ANNOUNCEMENT` | `INFO` | `0.0795` | 20,119.11 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 20.12K USD at 0.0795 USD [API] | `2026-10-28 02:17:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 11,431.20 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 11.43K USD at 0.0800 USD [API] | `2026-10-28 08:09:54` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 22,856.88 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 22.86K USD at 0.0800 USD [API] | `2026-10-28 08:16:14` |
| `ANNOUNCEMENT` | `INFO` | `0.0799` | 12,017.09 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 12.02K USD at 0.0799 USD [API] | `2026-10-28 08:16:40` |
| `ANNOUNCEMENT` | `INFO` | `0.0803` | 6,227.79 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.23K USD at 0.0803 USD [API] | `2026-10-28 08:46:39` |
| `ANNOUNCEMENT` | `INFO` | `0.0802` | 10,058.02 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.06K USD at 0.0802 USD [API] | `2026-10-28 08:58:22` |
| `ANNOUNCEMENT` | `INFO` | `0.0802` | 8,154.92 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 8.15K USD at 0.0802 USD [API] | `2026-10-28 09:11:32` |
| `ANNOUNCEMENT` | `INFO` | `0.0802` | 7,280.26 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.28K USD at 0.0802 USD [API] | `2026-10-28 09:10:39` |
| `ANNOUNCEMENT` | `INFO` | `0.0802` | 5,295.64 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.30K USD at 0.0802 USD [API] | `2026-10-28 09:12:52` |
| `ANNOUNCEMENT` | `INFO` | `0.0802` | 12,709.06 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 12.71K USD at 0.0802 USD [API] | `2026-10-28 09:13:01` |
| `ANNOUNCEMENT` | `INFO` | `0.0803` | 5,264.32 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.26K USD at 0.0803 USD [API] | `2026-10-28 09:18:08` |
| `ANNOUNCEMENT` | `INFO` | `0.0803` | 9,503.03 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 9.50K USD at 0.0803 USD [API] | `2026-10-28 09:21:23` |
| `ANNOUNCEMENT` | `INFO` | `0.0803` | 9,558.52 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.56K USD at 0.0803 USD [API] | `2026-10-28 09:32:39` |
| `ANNOUNCEMENT` | `INFO` | `0.0806` | 1,434.64 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 1.43K USD at 0.0806 USD [API] | `2026-10-28 09:47:34` |
| `ANNOUNCEMENT` | `INFO` | `0.0806` | 3,303.87 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 3.30K USD at 0.0806 USD [API] | `2026-10-28 09:47:34` |
| `ANNOUNCEMENT` | `INFO` | `0.0804` | 6,864.44 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.86K USD at 0.0804 USD [API] | `2026-10-28 10:20:56` |
| `ANNOUNCEMENT` | `INFO` | `0.0804` | 9,204.64 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 9.20K USD at 0.0804 USD [API] | `2026-10-28 10:20:56` |
| `ANNOUNCEMENT` | `INFO` | `0.0804` | 10,228.93 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 10.23K USD at 0.0804 USD [API] | `2026-10-28 10:20:56` |
| `ANNOUNCEMENT` | `INFO` | `0.0937` | 457.22 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 0.46K USD at 0.0937 USD [API] | `2026-09-28 03:33:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0937` | 16,999.98 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 17.00K USD at 0.0937 USD [API] | `2026-09-28 03:33:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0937` | 1,845.57 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 1.85K USD at 0.0937 USD [API] | `2026-09-28 03:33:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0937` | 1,421.78 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 1.42K USD at 0.0937 USD [API] | `2026-09-28 03:33:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0937` | 16,999.97 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 17.00K USD at 0.0937 USD [API] | `2026-09-28 03:33:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0937` | 16,999.97 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 17.00K USD at 0.0937 USD [API] | `2026-09-28 03:33:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0937` | 947.89 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 0.95K USD at 0.0937 USD [API] | `2026-09-28 03:33:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0937` | 16,999.97 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 17.00K USD at 0.0937 USD [API] | `2026-09-28 03:33:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0937` | 16,766.39 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 16.77K USD at 0.0937 USD [API] | `2026-09-28 03:33:00` |
| `ANNOUNCEMENT` | `INFO` | `0.0802` | 18,045.74 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 18.05K USD at 0.0802 USD [API] | `2026-10-28 11:08:16` |
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 9,101.23 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 9.10K USD at 0.0800 USD [API] | `2026-10-28 11:15:21` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0826` (Vol: 395,700.00 USD, Dist: `+5.32%`) | Long MP=`0.0767` (Vol: 519,500.00 USD, Dist: `--2.24%`)
  * 48H Horizon: Short MP=`0.0821` (Vol: 478,200.00 USD, Dist: `+4.71%`) | Long MP=`0.0774` (Vol: 691,800.00 USD, Dist: `--1.36%`)
  * 3D Horizon: Short MP=`0.0823` (Vol: 539,400.00 USD, Dist: `+4.91%`) | Long MP=`0.0765` (Vol: 660,700.00 USD, Dist: `--2.43%`)
  * 7D Horizon: Short MP=`0.0821` (Vol: 746,800.00 USD, Dist: `+4.72%`) | Long MP=`0.0762` (Vol: 988,700.00 USD, Dist: `--2.83%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0152` | 231.77 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0162` | 184.97 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0182` | 115.60 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0187` | 323.68 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0192` | 16,860.00 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0203` | 125.67 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0210` | 295.48 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 429.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0222` | 1,680.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 345.98 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0238` | 4,960.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0239` | 620.21 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0242` | 11,860.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0262` | 140.28 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0266` | 457.30 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0270` | 6,050.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0272` | 1,060.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0272` | 603.02 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0276` | 2,200.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0284` | 3,850.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0288` | 2,180.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0299` | 162.15 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0301` | 2,360.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0303` | 4,080.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0331` | 149.22 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0333` | 199.13 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 3,290.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0345` | 740,220.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0350` | 50,680.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 4,310.00 USD | 15,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0365` | 194.97 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0372` | 28,950.00 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0374` | 3,370.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0376` | 3,800.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 246.45 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0391` | 1,010.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 101,840.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 1,070.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0398` | 2,710.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0406` | 11,450.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0411` | 1,030.00 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 252.72 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 4,590.00 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0421` | 59,650.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 88,980.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 3,190.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,010.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 3,620.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 6,430.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 2,490.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 402.70 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 2,360.00 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 14,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0471` | 15,280.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 3,010.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 593.13 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 56,440.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,500.00 USD | 14,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,280.00 USD | 14,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 18,690.00 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 323.28 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0502` | 384.95 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 1,330.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 314.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 385.13 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 662.73 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 1,200.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 297.41 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 3,990.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 275,090.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 14,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,640.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 395.09 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,360.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 181,690.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 61,750.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 336.86 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 314,750.00 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 291.27 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 13,510.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 237.95 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 3,230.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 892.81 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0549` | 770.89 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 1,610.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 101.07 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 772.62 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 40,620.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 1,010.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 567.50 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 1,040.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 825.82 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 7,260.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 13,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,940.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 10,530.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 116.82 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 392.08 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 5,780,000.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 9,120.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 889.30 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,660.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,650.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 2,110.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 2,830.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 11,540.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 1,280.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 2,160.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,990.00 USD | 7,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 17,630.00 USD | 7,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 2,220.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0611` | 11,810.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 913.21 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,400.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 13,830.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 1,820.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 3,470.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 168.28 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 10,410.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 233.80 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 3,080.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,060,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 32,880.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 8,670.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,360.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 633.29 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,150.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 2,170.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 23,050.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0646` | 3,520.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 87,470.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 9,910.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0650` | 885.98 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 34,430.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 6,530.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 5,340.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0657` | 22,620.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 71,100.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 11,990.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 339.48 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 27,600.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,030.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 66,830.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 4,860.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,020,000.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 389.18 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,180.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0672` | 899.27 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 196.64 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 96,530.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0674` | 8,600,000.00 USD | 8,600,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0674` | 2,070.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 310.73 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0676` | 8,590,000.00 USD | 8,590,000.00 USD | 45,230.00 USD | 30,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0677` | 8,210.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 5,100.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 8,520,000.00 USD | 8,520,000.00 USD | 3,200.00 USD | 0.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 55,180.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0679` | 20,030.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0682` | 4,720.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 8,480,000.00 USD | 8,480,000.00 USD | 2,550.00 USD | 33,950.00 USD | 134,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 1,290.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0684` | 6,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 4,690.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0687` | 1,410.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 69,020.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 517.48 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 86,650.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0692` | 8,350.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 8,280,000.00 USD | 8,280,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 52,390.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 96,110.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0696` | 15,100.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0696` | 8,280,000.00 USD | 8,280,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,420.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 8,280,000.00 USD | 8,280,000.00 USD | 39,980.00 USD | 38,520.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,630.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0699` | 9,500.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 8,160,000.00 USD | 8,160,000.00 USD | 142,320.00 USD | 78,270.00 USD | 57,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 7,880,000.00 USD | 7,880,000.00 USD | 106,420.00 USD | 54,820.00 USD | 27,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 2,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 7,700,000.00 USD | 7,700,000.00 USD | 132,460.00 USD | 55,620.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0706` | 93,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0706` | 7,450,000.00 USD | 7,450,000.00 USD | 71,470.00 USD | 54,000.00 USD | 59,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 536.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 7,260,000.00 USD | 7,260,000.00 USD | 79,650.00 USD | 38,000.00 USD | 49,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0710` | 7,090,000.00 USD | 7,090,000.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0712` | 6,970,000.00 USD | 6,970,000.00 USD | 79,710.00 USD | 21,060.00 USD | 45,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 389.38 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 6,820,000.00 USD | 6,820,000.00 USD | 67,420.00 USD | 100,220.00 USD | 71,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 2,220.00 USD | 762,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0716` | 10,330.00 USD | 760,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 6,580,000.00 USD | 6,580,000.00 USD | 55,590.00 USD | 40,440.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 560.88 USD | 750,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,520.00 USD | 749,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 6,450,000.00 USD | 6,450,000.00 USD | 83,040.00 USD | 44,590.00 USD | 54,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 10,850.00 USD | 748,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0720` | 778.93 USD | 737,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 6,260,000.00 USD | 6,260,000.00 USD | 77,220.00 USD | 32,390.00 USD | 42,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 23,870.00 USD | 736,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 6,110,000.00 USD | 6,110,000.00 USD | 175,160.00 USD | 97,110.00 USD | 34,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 5,720.00 USD | 712,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0723` | 6,110.00 USD | 706,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 5,810,000.00 USD | 5,810,000.00 USD | 74,530.00 USD | 172,100.00 USD | 123,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 598.51 USD | 700,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 700,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 5,440,000.00 USD | 5,440,000.00 USD | 88,190.00 USD | 22,980.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 948.37 USD | 700,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0727` | 3,170.00 USD | 699,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 5,300,000.00 USD | 5,300,000.00 USD | 223,190.00 USD | 85,670.00 USD | 387,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 646.11 USD | 695,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0730` | 72,950.00 USD | 695,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 4,600,000.00 USD | 4,600,000.00 USD | 39,900.00 USD | 0.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,300.00 USD | 622,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 612,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 4,550,000.00 USD | 4,550,000.00 USD | 90,450.00 USD | 0.00 USD | 100.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 5,410.00 USD | 610,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0734` | 4,450,000.00 USD | 4,450,000.00 USD | 23,950.00 USD | 0.00 USD | 70,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,000.00 USD | 604,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,060.00 USD | 597,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 4,360,000.00 USD | 4,360,000.00 USD | 262,120.00 USD | 151,300.00 USD | 299.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 593,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,390.00 USD | 588,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 3,950,000.00 USD | 3,950,000.00 USD | 83,700.00 USD | 0.00 USD | 637.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 5,430.00 USD | 577,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0740` | 13,770.00 USD | 572,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 3,860,000.00 USD | 3,860,000.00 USD | 67,420.00 USD | 161,430.00 USD | 78,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 455,270.00 USD | 558,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0741` | 777.39 USD | 103,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 3,550,000.00 USD | 3,550,000.00 USD | 323,330.00 USD | 0.00 USD | 666,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 1,280.00 USD | 102,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0743` | 2,140.00 USD | 101,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 2,560,000.00 USD | 2,560,000.00 USD | 138,520.00 USD | 257,350.00 USD | 183,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,040.00 USD | 99,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,420.00 USD | 97,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0746` | 1,990,000.00 USD | 1,990,000.00 USD | 232,670.00 USD | 232,630.00 USD | 150,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,050.00 USD | 95,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0747` | 359.77 USD | 94,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,370,000.00 USD | 1,370,000.00 USD | 391,880.00 USD | 181,940.00 USD | 161,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0750` | 8,550.00 USD | 94,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0750` | 634,080.00 USD | 634,080.00 USD | 203,330.00 USD | 0.00 USD | 269,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 13,430.00 USD | 85,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0751` | 1,480.00 USD | 72,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0752` | 161,700.00 USD | 161,700.00 USD | 0.00 USD | 0.00 USD | 161,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0752` | 11,190.00 USD | 70,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0755` | 4,060.00 USD | 59,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0756` | 977.84 USD | 55,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 516.61 USD | 54,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0757` | 3,270.00 USD | 53,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0759` | 5,070.00 USD | 50,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0760` | 32,080.00 USD | 45,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0760` | 883.41 USD | 883.41 USD | 0.00 USD | 0.00 USD | 883.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,260.00 USD | 13,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0761` | 623.52 USD | 12,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0762` | 1,310,000.00 USD | 1,310,000.00 USD | 604,660.00 USD | 706,100.00 USD | 691.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0762` | 181.93 USD | 11,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0764` | 11,510.00 USD | 11,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0764` | 2,570,000.00 USD | 2,570,000.00 USD | 756,300.00 USD | 505,620.00 USD | 250.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 4,590,000.00 USD | 4,590,000.00 USD | 1,320,000.00 USD | 690,020.00 USD | 912.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 5,870,000.00 USD | 5,870,000.00 USD | 609,920.00 USD | 433,980.00 USD | 236,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 7,210,000.00 USD | 7,210,000.00 USD | 489,490.00 USD | 448,120.00 USD | 402,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 8,860,000.00 USD | 8,860,000.00 USD | 502,750.00 USD | 260,570.00 USD | 892,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 9,200,000.00 USD | 9,200,000.00 USD | 65,160.00 USD | 169,730.00 USD | 102,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0776` | 9,220,000.00 USD | 9,220,000.00 USD | 7,430.00 USD | 12,000.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 9,800,000.00 USD | 9,800,000.00 USD | 16,790.00 USD | 347,140.00 USD | 213,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 117,930.00 USD | 141,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 10,230,000.00 USD | 10,230,000.00 USD | 113,060.00 USD | 61,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0784` | 10,630,000.00 USD | 10,630,000.00 USD | 273,810.00 USD | 86,850.00 USD | 42,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 11,520,000.00 USD | 11,520,000.00 USD | 356,780.00 USD | 227,550.00 USD | 298,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0788` | 12,770,000.00 USD | 12,770,000.00 USD | 374,310.00 USD | 488,720.00 USD | 386,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 13,200,000.00 USD | 13,200,000.00 USD | 234,900.00 USD | 113,150.00 USD | 82,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 13,340,000.00 USD | 13,340,000.00 USD | 48,420.00 USD | 45,770.00 USD | 52,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0794` | 13,420,000.00 USD | 13,420,000.00 USD | 75,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 13,660,000.00 USD | 13,660,000.00 USD | 149,220.00 USD | 0.00 USD | 88,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 14,370,000.00 USD | 14,370,000.00 USD | 220,340.00 USD | 250,960.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 14,990,000.00 USD | 14,990,000.00 USD | 178,150.00 USD | 156,700.00 USD | 290,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 15,060,000.00 USD | 15,060,000.00 USD | 11,880.00 USD | 10,910.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 15,460,000.00 USD | 15,460,000.00 USD | 84,020.00 USD | 58,270.00 USD | 256,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 16,990,000.00 USD | 16,990,000.00 USD | 634,220.00 USD | 339,110.00 USD | 564,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 18,430,000.00 USD | 18,430,000.00 USD | 771,010.00 USD | 517,160.00 USD | 144,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 19,110,000.00 USD | 19,110,000.00 USD | 202,360.00 USD | 340,900.00 USD | 135,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0814` | 1,060.00 USD | 1,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0814` | 19,800,000.00 USD | 19,800,000.00 USD | 74,410.00 USD | 108,600.00 USD | 515,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 21,160,000.00 USD | 21,160,000.00 USD | 675,530.00 USD | 335,640.00 USD | 348,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 710.08 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 22,530,000.00 USD | 22,530,000.00 USD | 613,810.00 USD | 315,240.00 USD | 438,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 24,110,000.00 USD | 24,110,000.00 USD | 349,970.00 USD | 624,350.00 USD | 604,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 25,160,000.00 USD | 25,160,000.00 USD | 472,760.00 USD | 248,830.00 USD | 327,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 26,090,000.00 USD | 26,090,000.00 USD | 422,760.00 USD | 301,930.00 USD | 207,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 26,790,000.00 USD | 26,790,000.00 USD | 278,370.00 USD | 206,840.00 USD | 217,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 27,170,000.00 USD | 27,170,000.00 USD | 278,450.00 USD | 84,280.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0828` | 263.55 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0829` | 651.07 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0830` | 27,950,000.00 USD | 27,950,000.00 USD | 396,370.00 USD | 209,720.00 USD | 178,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 11,330.00 USD | 14,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 28,500,000.00 USD | 28,500,000.00 USD | 320,350.00 USD | 100,300.00 USD | 128,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 150.95 USD | 14,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0834` | 29,240,000.00 USD | 29,240,000.00 USD | 289,210.00 USD | 162,910.00 USD | 282,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0835` | 13,550.00 USD | 27,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0836` | 29,930,000.00 USD | 29,930,000.00 USD | 156,630.00 USD | 258,910.00 USD | 274,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 28,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 29,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 30,310,000.00 USD | 30,310,000.00 USD | 238,020.00 USD | 86,330.00 USD | 59,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 104.69 USD | 29,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0840` | 30,440,000.00 USD | 30,440,000.00 USD | 89,110.00 USD | 15,480.00 USD | 29,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0840` | 4,710.00 USD | 34,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0842` | 30,560,000.00 USD | 30,560,000.00 USD | 62,170.00 USD | 2,010.00 USD | 47,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 104.72 USD | 34,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0844` | 30,670,000.00 USD | 30,670,000.00 USD | 116,360.00 USD | 0.00 USD | 825.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 30,780,000.00 USD | 30,780,000.00 USD | 90,570.00 USD | 16,670.00 USD | 264.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 213.74 USD | 34,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0848` | 30,800,000.00 USD | 30,800,000.00 USD | 22,580.00 USD | 0.00 USD | 284.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0850` | 30,830,000.00 USD | 30,830,000.00 USD | 23,830.00 USD | 0.00 USD | 448.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0851` | 214.75 USD | 34,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0852` | 30,900,000.00 USD | 30,900,000.00 USD | 35,100.00 USD | 24,590.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0854` | 30,980,000.00 USD | 30,980,000.00 USD | 40,150.00 USD | 13,930.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0856` | 31,280,000.00 USD | 31,280,000.00 USD | 167,910.00 USD | 78,270.00 USD | 56,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0858` | 31,490,000.00 USD | 31,490,000.00 USD | 123,990.00 USD | 54,820.00 USD | 27,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 35,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 135.37 USD | 35,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0860` | 31,730,000.00 USD | 31,730,000.00 USD | 130,590.00 USD | 55,620.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 216.58 USD | 35,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0862` | 31,900,000.00 USD | 31,900,000.00 USD | 54,010.00 USD | 54,000.00 USD | 57,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 2,340.00 USD | 37,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0864` | 31,950,000.00 USD | 31,950,000.00 USD | 22,510.00 USD | 20,050.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0866` | 32,070,000.00 USD | 32,070,000.00 USD | 57,180.00 USD | 17,950.00 USD | 44,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0868` | 32,200,000.00 USD | 32,200,000.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0870` | 32,330,000.00 USD | 32,330,000.00 USD | 68,060.00 USD | 21,060.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0872` | 32,570,000.00 USD | 32,570,000.00 USD | 67,420.00 USD | 100,220.00 USD | 71,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0874` | 32,630,000.00 USD | 32,630,000.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0876` | 32,690,000.00 USD | 32,690,000.00 USD | 30,130.00 USD | 31,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0877` | 9,630.00 USD | 47,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0878` | 32,840,000.00 USD | 32,840,000.00 USD | 50,320.00 USD | 44,590.00 USD | 54,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0880` | 32,950,000.00 USD | 32,950,000.00 USD | 50,910.00 USD | 17,330.00 USD | 38,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 47,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 48,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0891` | 106.09 USD | 48,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 49,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0896` | 3,460.00 USD | 52,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0900` | 226.85 USD | 52,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0905` | 361.53 USD | 53,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 882.57 USD | 54,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0909` | 4,090.00 USD | 58,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0910` | 114.23 USD | 58,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 743.15 USD | 58,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0912` | 4,040.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0914` | 171.19 USD | 63,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0917` | 344.43 USD | 63,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 63,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0924` | 187.93 USD | 63,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0935` | 3,300.00 USD | 67,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0949` | 573.84 USD | 67,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 13,800.00 USD | 81,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0951` | 114,180.00 USD | 195,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0959` | 747.55 USD | 196,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 197,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0963` | 48,120.00 USD | 245,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0979` | 39,190.00 USD | 284,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 284,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0984` | 10,510.00 USD | 295,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1002` | 1,290.00 USD | 296,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1012` | 1,010.00 USD | 297,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1013` | 177.90 USD | 297,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 305,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 308,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 308,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1041` | 1,020.00 USD | 309,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 316,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1072` | 3,210.00 USD | 319,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,370.00 USD | 322,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1114` | 1,500.00 USD | 324,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1121` | 2,290.00 USD | 326,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 326,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 326,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1187` | 106.19 USD | 326,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1215` | 353.91 USD | 327,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 328,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1265` | 379.65 USD | 328,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 328,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1278` | 1,540.00 USD | 330,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 330,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 332,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 332,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1323` | 2,770,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1384` | 2,210.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1389` | 1,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1411` | 1,800.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1419` | 23,020.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1437` | 678.93 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,320.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1480` | 391.74 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1510` | 56,520.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 2,010.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 267.55 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1527` | 195.39 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1527` | 194.45 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1563` | 340.06 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 4,830.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 980.15 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0158` | 16,520,000.00 USD | 0.00 USD | 1,510.00 USD | `-79.07%` | `95,954.00` |
| `Live` | `Long` | `0.0160` | 16,520,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.68%` | `244,573.00` |
| `Live` | `Long` | `0.0163` | 16,510,000.00 USD | 0.00 USD | 4,060.00 USD | `-78.41%` | `250,000.00` |
| `Live` | `Long` | `0.0164` | 16,510,000.00 USD | 0.00 USD | 407.02 USD | `-78.14%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,510,000.00 USD | 0.00 USD | 5,290.00 USD | `-78.01%` | `319,394.00` |
| `Live` | `Long` | `0.0176` | 16,500,000.00 USD | 0.00 USD | 1,930.00 USD | `-76.55%` | `109,191.00` |
| `Live` | `Long` | `0.0192` | 16,500,000.00 USD | 0.00 USD | 22,220.00 USD | `-74.56%` | `1,160,480.00` |
| `Live` | `Long` | `0.0193` | 16,480,000.00 USD | 0.00 USD | 1,450.00 USD | `-74.29%` | `75,012.00` |
| `Live` | `Long` | `0.0203` | 16,480,000.00 USD | 0.00 USD | 110.00 USD | `-73.10%` | `5,432.00` |
| `Live` | `Long` | `0.0209` | 16,480,000.00 USD | 0.00 USD | 31,040.00 USD | `-72.30%` | `1,488,849.00` |
| `Live` | `Long` | `0.0210` | 16,450,000.00 USD | 0.00 USD | 127.37 USD | `-72.03%` | `6,051.00` |
| `Live` | `Long` | `0.0214` | 16,450,000.00 USD | 0.00 USD | 337.22 USD | `-71.63%` | `15,795.00` |
| `Live` | `Long` | `0.0219` | 16,450,000.00 USD | 0.00 USD | 3,350.00 USD | `-70.97%` | `153,201.00` |
| `Live` | `Long` | `0.0225` | 16,440,000.00 USD | 0.00 USD | 268.70 USD | `-70.17%` | `11,969.00` |
| `Live` | `Long` | `0.0231` | 16,440,000.00 USD | 0.00 USD | 20,600.00 USD | `-69.38%` | `893,720.00` |
| `Live` | `Long` | `0.0232` | 16,420,000.00 USD | 0.00 USD | 143.67 USD | `-69.24%` | `6,206.00` |
| `Live` | `Long` | `0.0232` | 16,420,000.00 USD | 0.00 USD | 345.98 USD | `-69.11%` | `14,881.00` |
| `Live` | `Long` | `0.0233` | 16,420,000.00 USD | 0.00 USD | 747.20 USD | `-68.98%` | `32,000.00` |
| `Live` | `Long` | `0.0234` | 16,420,000.00 USD | 0.00 USD | 915.70 USD | `-68.84%` | `39,049.00` |
| `Live` | `Long` | `0.0261` | 16,420,000.00 USD | 0.00 USD | 449.70 USD | `-65.39%` | `17,263.00` |
| `Live` | `Long` | `0.0267` | 16,420,000.00 USD | 0.00 USD | 13,320.00 USD | `-64.59%` | `500,000.00` |
| `Live` | `Long` | `0.0267` | 16,410,000.00 USD | 0.00 USD | 535.00 USD | `-64.46%` | `20,000.00` |
| `Live` | `Long` | `0.0272` | 16,410,000.00 USD | 0.00 USD | 2,670.00 USD | `-63.93%` | `98,319.00` |
| `Live` | `Long` | `0.0276` | 16,400,000.00 USD | 0.00 USD | 889.81 USD | `-63.40%` | `32,298.00` |
| `Live` | `Long` | `0.0278` | 16,400,000.00 USD | 0.00 USD | 317.82 USD | `-63.13%` | `11,453.00` |
| `Live` | `Long` | `0.0279` | 16,400,000.00 USD | 0.00 USD | 1,730.00 USD | `-62.87%` | `61,775.00` |
| `Live` | `Long` | `0.0284` | 16,400,000.00 USD | 0.00 USD | 13,970.00 USD | `-62.20%` | `491,018.00` |
| `Live` | `Long` | `0.0305` | 16,390,000.00 USD | 0.00 USD | 153.38 USD | `-59.54%` | `5,037.00` |
| `Live` | `Long` | `0.0306` | 16,390,000.00 USD | 0.00 USD | 137.41 USD | `-59.41%` | `4,498.00` |
| `Live` | `Long` | `0.0312` | 16,390,000.00 USD | 0.00 USD | 141.48 USD | `-58.61%` | `4,542.00` |
| `Live` | `Long` | `0.0330` | 16,390,000.00 USD | 0.00 USD | 6,190.00 USD | `-56.22%` | `187,979.00` |
| `Live` | `Long` | `0.0338` | 16,380,000.00 USD | 0.00 USD | 1,690.00 USD | `-55.16%` | `50,000.00` |
| `Live` | `Long` | `0.0348` | 16,380,000.00 USD | 0.00 USD | 5,170.00 USD | `-53.70%` | `148,480.00` |
| `Live` | `Long` | `0.0358` | 16,370,000.00 USD | 0.00 USD | 214.53 USD | `-52.37%` | `5,984.00` |
| `Live` | `Long` | `0.0369` | 16,370,000.00 USD | 0.00 USD | 463.46 USD | `-50.91%` | `12,543.00` |
| `Live` | `Long` | `0.0370` | 16,370,000.00 USD | 0.00 USD | 35,200.00 USD | `-50.77%` | `950,000.00` |
| `Live` | `Long` | `0.0379` | 16,340,000.00 USD | 0.00 USD | 1,800.00 USD | `-49.71%` | `47,501.00` |
| `Live` | `Long` | `0.0381` | 16,340,000.00 USD | 0.00 USD | 246.45 USD | `-49.45%` | `6,477.00` |
| `Live` | `Long` | `0.0382` | 16,330,000.00 USD | 0.00 USD | 172.70 USD | `-49.18%` | `4,515.00` |
| `Live` | `Long` | `0.0386` | 16,330,000.00 USD | 0.00 USD | 4,020.00 USD | `-48.78%` | `104,284.00` |
| `Live` | `Long` | `0.0387` | 16,330,000.00 USD | 0.00 USD | 857.50 USD | `-48.52%` | `22,129.00` |
| `Live` | `Long` | `0.0389` | 16,330,000.00 USD | 0.00 USD | 208.34 USD | `-48.25%` | `5,349.00` |
| `Live` | `Long` | `0.0391` | 16,330,000.00 USD | 0.00 USD | 400.78 USD | `-47.98%` | `10,237.00` |
| `Live` | `Long` | `0.0393` | 16,330,000.00 USD | 0.00 USD | 221.10 USD | `-47.85%` | `5,633.00` |
| `Live` | `Long` | `0.0394` | 16,330,000.00 USD | 0.00 USD | 4,810.00 USD | `-47.72%` | `122,306.00` |
| `Live` | `Long` | `0.0396` | 16,320,000.00 USD | 0.00 USD | 135.76 USD | `-47.32%` | `3,424.00` |
| `Live` | `Long` | `0.0404` | 16,320,000.00 USD | 0.00 USD | 115.12 USD | `-46.26%` | `2,846.00` |
| `Live` | `Long` | `0.0408` | 16,320,000.00 USD | 0.00 USD | 419.28 USD | `-45.86%` | `10,289.00` |
| `Live` | `Long` | `0.0410` | 16,320,000.00 USD | 0.00 USD | 705.32 USD | `-45.59%` | `17,224.00` |
| `Live` | `Long` | `0.0415` | 16,320,000.00 USD | 0.00 USD | 1,030.00 USD | `-44.80%` | `24,809.00` |
| `Live` | `Long` | `0.0416` | 16,320,000.00 USD | 0.00 USD | 58,540.00 USD | `-44.66%` | `1,405,488.00` |
| `Live` | `Long` | `0.0420` | 16,260,000.00 USD | 0.00 USD | 266.05 USD | `-44.26%` | `6,342.00` |
| `Live` | `Long` | `0.0423` | 16,260,000.00 USD | 0.00 USD | 1,670.00 USD | `-43.87%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,260,000.00 USD | 0.00 USD | 493.84 USD | `-43.73%` | `11,661.00` |
| `Live` | `Long` | `0.0425` | 16,260,000.00 USD | 0.00 USD | 455.06 USD | `-43.60%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,260,000.00 USD | 0.00 USD | 1,010.00 USD | `-43.47%` | `23,716.00` |
| `Live` | `Long` | `0.0427` | 16,260,000.00 USD | 0.00 USD | 3,620.00 USD | `-43.33%` | `84,760.00` |
| `Live` | `Long` | `0.0430` | 16,260,000.00 USD | 0.00 USD | 859.00 USD | `-42.94%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 16,250,000.00 USD | 0.00 USD | 6,430.00 USD | `-42.54%` | `148,704.00` |
| `Live` | `Long` | `0.0433` | 16,250,000.00 USD | 0.00 USD | 6,780.00 USD | `-42.40%` | `156,456.00` |
| `Live` | `Long` | `0.0437` | 16,240,000.00 USD | 0.00 USD | 116,590.00 USD | `-41.87%` | `2,664,805.00` |
| `Live` | `Long` | `0.0439` | 16,130,000.00 USD | 0.00 USD | 1,610.00 USD | `-41.74%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 16,120,000.00 USD | 0.00 USD | 750.58 USD | `-41.61%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,120,000.00 USD | 0.00 USD | 1,060.00 USD | `-41.47%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 16,120,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.08%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 16,020,000.00 USD | 0.00 USD | 444.76 USD | `-40.68%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 16,020,000.00 USD | 0.00 USD | 248.63 USD | `-40.54%` | `5,556.00` |
| `Live` | `Long` | `0.0454` | 16,020,000.00 USD | 0.00 USD | 2,170.00 USD | `-39.61%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 16,020,000.00 USD | 0.00 USD | 32,650.00 USD | `-39.48%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 15,980,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.22%` | `119,571.00` |
| `Live` | `Long` | `0.0461` | 15,980,000.00 USD | 0.00 USD | 4,500.00 USD | `-38.82%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 15,970,000.00 USD | 0.00 USD | 114.36 USD | `-38.68%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 15,970,000.00 USD | 0.00 USD | 362.87 USD | `-38.42%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 15,970,000.00 USD | 0.00 USD | 16,780.00 USD | `-38.29%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 15,960,000.00 USD | 0.00 USD | 1,710.00 USD | `-38.15%` | `36,724.00` |
| `Live` | `Long` | `0.0466` | 15,960,000.00 USD | 0.00 USD | 109.49 USD | `-38.02%` | `2,347.00` |
| `Live` | `Long` | `0.0471` | 15,960,000.00 USD | 0.00 USD | 1,210.00 USD | `-37.49%` | `25,729.00` |
| `Live` | `Long` | `0.0473` | 15,950,000.00 USD | 0.00 USD | 1,600.00 USD | `-37.22%` | `33,899.00` |
| `Live` | `Long` | `0.0474` | 15,950,000.00 USD | 0.00 USD | 1,420.00 USD | `-37.09%` | `29,884.00` |
| `Live` | `Long` | `0.0474` | 15,950,000.00 USD | 0.00 USD | 593.13 USD | `-36.96%` | `12,500.00` |
| `Live` | `Long` | `0.0476` | 15,950,000.00 USD | 0.00 USD | 2,010.00 USD | `-36.69%` | `42,211.00` |
| `Live` | `Long` | `0.0481` | 15,950,000.00 USD | 0.00 USD | 59,060.00 USD | `-36.03%` | `1,226,627.00` |
| `Live` | `Long` | `0.0483` | 15,890,000.00 USD | 0.00 USD | 2,410.00 USD | `-35.76%` | `49,758.00` |
| `Live` | `Long` | `0.0485` | 15,890,000.00 USD | 0.00 USD | 1,480.00 USD | `-35.63%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 15,890,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.10%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 15,880,000.00 USD | 0.00 USD | 11,270.00 USD | `-34.96%` | `230,133.00` |
| `Live` | `Long` | `0.0491` | 15,870,000.00 USD | 0.00 USD | 1,080.00 USD | `-34.83%` | `21,989.00` |
| `Live` | `Long` | `0.0491` | 15,870,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-34.70%` | `21,649,147.00` |
| `Live` | `Long` | `0.0495` | 14,810,000.00 USD | 0.00 USD | 18,690.00 USD | `-34.17%` | `377,099.00` |
| `Live` | `Long` | `0.0498` | 14,790,000.00 USD | 0.00 USD | 253.82 USD | `-33.90%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,790,000.00 USD | 0.00 USD | 501.50 USD | `-33.50%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,790,000.00 USD | 0.00 USD | 5,410.00 USD | `-33.24%` | `107,572.00` |
| `Live` | `Long` | `0.0503` | 14,780,000.00 USD | 0.00 USD | 5,650.00 USD | `-33.10%` | `112,151.00` |
| `Live` | `Long` | `0.0505` | 14,780,000.00 USD | 0.00 USD | 334.89 USD | `-32.97%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,780,000.00 USD | 0.00 USD | 1,040.00 USD | `-32.71%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,780,000.00 USD | 0.00 USD | 19,640.00 USD | `-32.57%` | `386,933.00` |
| `Live` | `Long` | `0.0510` | 14,760,000.00 USD | 0.00 USD | 2,730.00 USD | `-32.31%` | `53,578.00` |
| `Live` | `Long` | `0.0510` | 14,750,000.00 USD | 0.00 USD | 566.65 USD | `-32.17%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,750,000.00 USD | 0.00 USD | 12,190.00 USD | `-32.04%` | `238,328.00` |
| `Live` | `Long` | `0.0512` | 14,740,000.00 USD | 0.00 USD | 2,160.00 USD | `-31.91%` | `42,240.00` |
| `Live` | `Long` | `0.0513` | 14,740,000.00 USD | 0.00 USD | 385.13 USD | `-31.78%` | `7,500.00` |
| `Live` | `Long` | `0.0515` | 14,740,000.00 USD | 0.00 USD | 309.15 USD | `-31.51%` | `5,997.00` |
| `Live` | `Long` | `0.0520` | 14,740,000.00 USD | 0.00 USD | 277.72 USD | `-30.98%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,740,000.00 USD | 0.00 USD | 8,670.00 USD | `-30.85%` | `166,663.00` |
| `Live` | `Long` | `0.0522` | 14,730,000.00 USD | 0.00 USD | 315,650.00 USD | `-30.58%` | `6,041,244.00` |
| `Live` | `Long` | `0.0524` | 14,410,000.00 USD | 0.00 USD | 1,170.00 USD | `-30.31%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,410,000.00 USD | 0.00 USD | 5,640.00 USD | `-30.18%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 14,410,000.00 USD | 0.00 USD | 395.09 USD | `-30.05%` | `7,504.00` |
| `Live` | `Long` | `0.0527` | 14,410,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.92%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,400,000.00 USD | 0.00 USD | 673.52 USD | `-29.78%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,400,000.00 USD | 0.00 USD | 182,630.00 USD | `-29.65%` | `3,449,122.00` |
| `Live` | `Long` | `0.0532` | 14,220,000.00 USD | 0.00 USD | 9,240.00 USD | `-29.38%` | `173,844.00` |
| `Live` | `Long` | `0.0534` | 14,210,000.00 USD | 0.00 USD | 325.27 USD | `-29.12%` | `6,097.00` |
| `Live` | `Long` | `0.0534` | 14,210,000.00 USD | 0.00 USD | 314,750.00 USD | `-28.99%` | `5,888,653.00` |
| `Live` | `Long` | `0.0536` | 13,900,000.00 USD | 0.00 USD | 942.48 USD | `-28.85%` | `17,600.00` |
| `Live` | `Long` | `0.0537` | 13,900,000.00 USD | 0.00 USD | 111,250.00 USD | `-28.59%` | `2,069,770.00` |
| `Live` | `Long` | `0.0539` | 13,780,000.00 USD | 0.00 USD | 5,290.00 USD | `-28.32%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 13,780,000.00 USD | 0.00 USD | 2,550.00 USD | `-28.19%` | `47,142.00` |
| `Live` | `Long` | `0.0541` | 13,780,000.00 USD | 0.00 USD | 13,510.00 USD | `-28.06%` | `249,542.00` |
| `Live` | `Long` | `0.0542` | 13,760,000.00 USD | 0.00 USD | 150,780.00 USD | `-27.92%` | `2,779,342.00` |
| `Live` | `Long` | `0.0544` | 13,610,000.00 USD | 0.00 USD | 237.95 USD | `-27.66%` | `4,370.00` |
| `Live` | `Long` | `0.0546` | 13,610,000.00 USD | 0.00 USD | 3,230.00 USD | `-27.39%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 13,610,000.00 USD | 0.00 USD | 892.81 USD | `-27.26%` | `16,307.00` |
| `Live` | `Long` | `0.0556` | 13,610,000.00 USD | 0.00 USD | 907.02 USD | `-26.20%` | `16,328.00` |
| `Live` | `Long` | `0.0558` | 13,610,000.00 USD | 0.00 USD | 1,500.00 USD | `-25.93%` | `26,900.00` |
| `Live` | `Long` | `0.0559` | 13,610,000.00 USD | 0.00 USD | 1,440.00 USD | `-25.66%` | `25,791.00` |
| `Live` | `Long` | `0.0561` | 13,600,000.00 USD | 0.00 USD | 144.08 USD | `-25.40%` | `2,566.00` |
| `Live` | `Long` | `0.0563` | 13,600,000.00 USD | 0.00 USD | 40,620.00 USD | `-25.27%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,560,000.00 USD | 0.00 USD | 351.85 USD | `-25.13%` | `6,244.00` |
| `Live` | `Long` | `0.0566` | 13,560,000.00 USD | 0.00 USD | 131.48 USD | `-24.87%` | `2,325.00` |
| `Live` | `Long` | `0.0568` | 13,560,000.00 USD | 0.00 USD | 568.50 USD | `-24.47%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,560,000.00 USD | 0.00 USD | 667.34 USD | `-24.34%` | `11,718.00` |
| `Live` | `Long` | `0.0570` | 13,560,000.00 USD | 0.00 USD | 8,350.00 USD | `-24.20%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,550,000.00 USD | 0.00 USD | 644.99 USD | `-24.07%` | `11,286.00` |
| `Live` | `Long` | `0.0573` | 13,550,000.00 USD | 0.00 USD | 329.02 USD | `-23.94%` | `5,747.00` |
| `Live` | `Long` | `0.0573` | 13,550,000.00 USD | 0.00 USD | 3,910.00 USD | `-23.80%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,550,000.00 USD | 0.00 USD | 3,590.00 USD | `-23.54%` | `62,330.00` |
| `Live` | `Long` | `0.0576` | 13,540,000.00 USD | 0.00 USD | 10,600.00 USD | `-23.40%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,530,000.00 USD | 0.00 USD | 17,090.00 USD | `-23.27%` | `295,980.00` |
| `Live` | `Long` | `0.0578` | 13,520,000.00 USD | 0.00 USD | 3,940.00 USD | `-23.14%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,510,000.00 USD | 0.00 USD | 431.14 USD | `-22.87%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,510,000.00 USD | 0.00 USD | 447.17 USD | `-22.74%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,510,000.00 USD | 0.00 USD | 485.94 USD | `-22.47%` | `8,328.00` |
| `Live` | `Long` | `0.0585` | 13,510,000.00 USD | 0.00 USD | 172.78 USD | `-22.21%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,510,000.00 USD | 0.00 USD | 9,120.00 USD | `-21.94%` | `155,271.00` |
| `Live` | `Long` | `0.0590` | 13,500,000.00 USD | 0.00 USD | 212.22 USD | `-21.68%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 13,500,000.00 USD | 0.00 USD | 26,980.00 USD | `-21.41%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,480,000.00 USD | 0.00 USD | 889.30 USD | `-21.15%` | `14,984.00` |
| `Live` | `Long` | `0.0595` | 13,470,000.00 USD | 0.00 USD | 4,040.00 USD | `-21.01%` | `67,874.00` |
| `Live` | `Long` | `0.0595` | 13,470,000.00 USD | 0.00 USD | 2,650.00 USD | `-20.88%` | `44,458.00` |
| `Live` | `Long` | `0.0599` | 13,470,000.00 USD | 0.00 USD | 5,750.00 USD | `-20.48%` | `96,079.00` |
| `Live` | `Long` | `0.0600` | 13,460,000.00 USD | 0.00 USD | 2,830.00 USD | `-20.35%` | `47,268.00` |
| `Live` | `Long` | `0.0600` | 13,460,000.00 USD | 0.00 USD | 7,210.00 USD | `-20.22%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 13,450,000.00 USD | 0.00 USD | 8,490.00 USD | `-20.08%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 13,440,000.00 USD | 0.00 USD | 5,960,000.00 USD | `-19.82%` | `98,689,541.00` |
| `Live` | `Long` | `0.0604` | 7,490,000.00 USD | 0.00 USD | 1,970.00 USD | `-19.68%` | `32,592.00` |
| `Live` | `Long` | `0.0605` | 7,490,000.00 USD | 0.00 USD | 32,090.00 USD | `-19.55%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,450,000.00 USD | 0.00 USD | 1,220.00 USD | `-19.29%` | `20,080.00` |
| `Live` | `Long` | `0.0609` | 7,450,000.00 USD | 0.00 USD | 717.73 USD | `-19.15%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 7,450,000.00 USD | 0.00 USD | 2,220.00 USD | `-19.02%` | `36,478.00` |
| `Live` | `Long` | `0.0612` | 7,450,000.00 USD | 0.00 USD | 913.21 USD | `-18.75%` | `14,934.00` |
| `Live` | `Long` | `0.0612` | 7,450,000.00 USD | 0.00 USD | 1,320.00 USD | `-18.62%` | `21,534.00` |
| `Live` | `Long` | `0.0614` | 7,450,000.00 USD | 0.00 USD | 655.16 USD | `-18.49%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,450,000.00 USD | 0.00 USD | 2,330.00 USD | `-18.22%` | `37,794.00` |
| `Live` | `Long` | `0.0617` | 7,440,000.00 USD | 0.00 USD | 59,700.00 USD | `-18.09%` | `968,374.00` |
| `Live` | `Long` | `0.0617` | 7,380,000.00 USD | 0.00 USD | 158.08 USD | `-17.96%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,380,000.00 USD | 0.00 USD | 26,790.00 USD | `-17.56%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,360,000.00 USD | 0.00 USD | 1,740.00 USD | `-17.43%` | `27,935.00` |
| `Live` | `Long` | `0.0622` | 7,360,000.00 USD | 0.00 USD | 428.53 USD | `-17.29%` | `6,884.00` |
| `Live` | `Long` | `0.0624` | 7,360,000.00 USD | 0.00 USD | 2,270.00 USD | `-17.16%` | `36,431.00` |
| `Live` | `Long` | `0.0624` | 7,350,000.00 USD | 0.00 USD | 3,660.00 USD | `-17.03%` | `58,632.00` |
| `Live` | `Long` | `0.0625` | 7,350,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-16.89%` | `18,274,137.00` |
| `Live` | `Long` | `0.0626` | 6,210,000.00 USD | 0.00 USD | 168.28 USD | `-16.76%` | `2,686.00` |
| `Live` | `Long` | `0.0628` | 6,210,000.00 USD | 0.00 USD | 694.83 USD | `-16.63%` | `11,073.00` |
| `Live` | `Long` | `0.0629` | 6,210,000.00 USD | 0.00 USD | 6,830.00 USD | `-16.50%` | `108,608.00` |
| `Live` | `Long` | `0.0630` | 6,200,000.00 USD | 0.00 USD | 3,080.00 USD | `-16.23%` | `48,869.00` |
| `Live` | `Long` | `0.0631` | 6,200,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-16.10%` | `16,926,907.00` |
| `Live` | `Long` | `0.0633` | 5,130,000.00 USD | 0.00 USD | 5,770.00 USD | `-15.96%` | `91,237.00` |
| `Live` | `Long` | `0.0634` | 5,120,000.00 USD | 0.00 USD | 16,700.00 USD | `-15.83%` | `263,544.00` |
| `Live` | `Long` | `0.0635` | 5,100,000.00 USD | 0.00 USD | 1,690.00 USD | `-15.70%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 5,100,000.00 USD | 0.00 USD | 280.95 USD | `-15.57%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 5,100,000.00 USD | 0.00 USD | 633.38 USD | `-15.43%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 5,100,000.00 USD | 0.00 USD | 2,150.00 USD | `-15.30%` | `33,786.00` |
| `Live` | `Long` | `0.0639` | 5,100,000.00 USD | 0.00 USD | 23,220.00 USD | `-15.17%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 5,080,000.00 USD | 0.00 USD | 1,770.00 USD | `-15.03%` | `27,679.00` |
| `Live` | `Long` | `0.0641` | 5,070,000.00 USD | 0.00 USD | 633.29 USD | `-14.77%` | `9,872.00` |
| `Live` | `Long` | `0.0643` | 5,070,000.00 USD | 0.00 USD | 9,150.00 USD | `-14.64%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 5,060,000.00 USD | 0.00 USD | 2,170.00 USD | `-14.50%` | `33,693.00` |
| `Live` | `Long` | `0.0644` | 5,060,000.00 USD | 0.00 USD | 23,050.00 USD | `-14.37%` | `357,682.00` |
| `Live` | `Long` | `0.0645` | 5,040,000.00 USD | 0.00 USD | 603.22 USD | `-14.24%` | `9,345.00` |
| `Live` | `Long` | `0.0646` | 5,040,000.00 USD | 0.00 USD | 3,520.00 USD | `-14.10%` | `54,442.00` |
| `Live` | `Long` | `0.0648` | 5,040,000.00 USD | 0.00 USD | 86,870.00 USD | `-13.97%` | `1,341,590.00` |
| `Live` | `Long` | `0.0649` | 4,950,000.00 USD | 0.00 USD | 9,910.00 USD | `-13.84%` | `152,854.00` |
| `Live` | `Long` | `0.0649` | 4,940,000.00 USD | 0.00 USD | 21,910.00 USD | `-13.71%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 4,920,000.00 USD | 0.00 USD | 2,380.00 USD | `-13.44%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,910,000.00 USD | 0.00 USD | 13,770.00 USD | `-13.31%` | `210,965.00` |
| `Live` | `Long` | `0.0654` | 4,900,000.00 USD | 0.00 USD | 6,530.00 USD | `-13.17%` | `100,000.00` |
| `Live` | `Long` | `0.0655` | 4,890,000.00 USD | 0.00 USD | 5,340.00 USD | `-12.91%` | `81,453.00` |
| `Live` | `Long` | `0.0658` | 4,890,000.00 USD | 0.00 USD | 66,820.00 USD | `-12.64%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,820,000.00 USD | 0.00 USD | 14,600.00 USD | `-12.51%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,810,000.00 USD | 0.00 USD | 11,990.00 USD | `-12.38%` | `181,801.00` |
| `Live` | `Long` | `0.0662` | 4,800,000.00 USD | 0.00 USD | 776.93 USD | `-12.11%` | `11,745.00` |
| `Live` | `Long` | `0.0663` | 4,790,000.00 USD | 0.00 USD | 2,450.00 USD | `-11.98%` | `36,920.00` |
| `Live` | `Long` | `0.0664` | 4,790,000.00 USD | 0.00 USD | 27,600.00 USD | `-11.85%` | `415,904.00` |
| `Live` | `Long` | `0.0664` | 4,760,000.00 USD | 0.00 USD | 1,030.00 USD | `-11.71%` | `15,449.00` |
| `Live` | `Long` | `0.0665` | 4,760,000.00 USD | 0.00 USD | 66,550.00 USD | `-11.58%` | `1,000,000.00` |
| `Live` | `Long` | `0.0667` | 4,700,000.00 USD | 0.00 USD | 34,860.00 USD | `-11.45%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-11.31%` | `19,836.00` |
| `Live` | `Long` | `0.0669` | 4,660,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-11.18%` | `15,230,102.00` |
| `Live` | `Long` | `0.0669` | 3,640,000.00 USD | 0.00 USD | 389.18 USD | `-11.05%` | `5,813.00` |
| `Live` | `Long` | `0.0670` | 3,640,000.00 USD | 0.00 USD | 13,530.00 USD | `-10.92%` | `201,862.00` |
| `Live` | `Long` | `0.0672` | 3,630,000.00 USD | 0.00 USD | 899.27 USD | `-10.78%` | `13,392.00` |
| `Live` | `Long` | `0.0673` | 3,630,000.00 USD | 0.00 USD | 33,870.00 USD | `-10.65%` | `503,650.00` |
| `Live` | `Long` | `0.0673` | 3,590,000.00 USD | 0.00 USD | 96,190.00 USD | `-10.52%` | `1,428,139.00` |
| `Live` | `Long` | `0.0674` | 3,500,000.00 USD | 0.00 USD | 3,300.00 USD | `-10.38%` | `48,918.00` |
| `Live` | `Long` | `0.0675` | 3,490,000.00 USD | 0.00 USD | 310.73 USD | `-10.25%` | `4,600.00` |
| `Live` | `Long` | `0.0677` | 3,490,000.00 USD | 0.00 USD | 8,210.00 USD | `-10.12%` | `121,370.00` |
| `Live` | `Long` | `0.0678` | 3,490,000.00 USD | 0.00 USD | 140,600.00 USD | `-9.99%` | `2,075,221.00` |
| `Live` | `Long` | `0.0678` | 3,350,000.00 USD | 0.00 USD | 55,180.00 USD | `-9.85%` | `813,258.00` |
| `Live` | `Long` | `0.0679` | 3,290,000.00 USD | 0.00 USD | 20,030.00 USD | `-9.72%` | `294,729.00` |
| `Live` | `Long` | `0.0680` | 3,270,000.00 USD | 0.00 USD | 212.72 USD | `-9.59%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,270,000.00 USD | 0.00 USD | 1,680.00 USD | `-9.45%` | `24,721.00` |
| `Live` | `Long` | `0.0683` | 3,270,000.00 USD | 0.00 USD | 55,650.00 USD | `-9.32%` | `815,403.00` |
| `Live` | `Long` | `0.0683` | 3,210,000.00 USD | 0.00 USD | 1,290.00 USD | `-9.19%` | `18,879.00` |
| `Live` | `Long` | `0.0684` | 3,210,000.00 USD | 0.00 USD | 6,000.00 USD | `-9.06%` | `87,593.00` |
| `Live` | `Long` | `0.0685` | 3,210,000.00 USD | 0.00 USD | 4,690.00 USD | `-8.92%` | `68,414.00` |
| `Live` | `Long` | `0.0687` | 3,200,000.00 USD | 0.00 USD | 595.81 USD | `-8.79%` | `8,679.00` |
| `Live` | `Long` | `0.0688` | 3,200,000.00 USD | 0.00 USD | 69,020.00 USD | `-8.66%` | `1,003,929.00` |
| `Live` | `Long` | `0.0688` | 3,130,000.00 USD | 0.00 USD | 1,170.00 USD | `-8.52%` | `17,063.00` |
| `Live` | `Long` | `0.0689` | 3,130,000.00 USD | 0.00 USD | 507,660.00 USD | `-8.39%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,620,000.00 USD | 0.00 USD | 3,670.00 USD | `-8.26%` | `53,108.00` |
| `Live` | `Long` | `0.0692` | 2,620,000.00 USD | 0.00 USD | 8,350.00 USD | `-8.13%` | `120,766.00` |
| `Live` | `Long` | `0.0693` | 2,610,000.00 USD | 0.00 USD | 2,160.00 USD | `-7.86%` | `31,211.00` |
| `Live` | `Long` | `0.0694` | 2,610,000.00 USD | 0.00 USD | 4,840.00 USD | `-7.73%` | `69,669.00` |
| `Live` | `Long` | `0.0696` | 2,600,000.00 USD | 0.00 USD | 14,930.00 USD | `-7.59%` | `214,659.00` |
| `Live` | `Long` | `0.0697` | 2,590,000.00 USD | 0.00 USD | 8,340.00 USD | `-7.46%` | `119,702.00` |
| `Live` | `Long` | `0.0698` | 2,580,000.00 USD | 0.00 USD | 3,420.00 USD | `-7.33%` | `49,047.00` |
| `Live` | `Long` | `0.0698` | 2,580,000.00 USD | 0.00 USD | 25,750.00 USD | `-7.20%` | `368,644.00` |
| `Live` | `Long` | `0.0699` | 2,550,000.00 USD | 0.00 USD | 1,310.00 USD | `-7.06%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,550,000.00 USD | 0.00 USD | 264.58 USD | `-6.93%` | `3,777.00` |
| `Live` | `Long` | `0.0702` | 2,550,000.00 USD | 0.00 USD | 1,590.00 USD | `-6.80%` | `22,683.00` |
| `Live` | `Long` | `0.0703` | 2,550,000.00 USD | 0.00 USD | 791.79 USD | `-6.66%` | `11,271.00` |
| `Live` | `Long` | `0.0703` | 2,550,000.00 USD | 0.00 USD | 5,060.00 USD | `-6.53%` | `71,876.00` |
| `Live` | `Long` | `0.0704` | 2,540,000.00 USD | 0.00 USD | 216.56 USD | `-6.40%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,540,000.00 USD | 0.00 USD | 94,410.00 USD | `-6.00%` | `1,334,448.00` |
| `Live` | `Long` | `0.0708` | 2,450,000.00 USD | 0.00 USD | 9,150.00 USD | `-5.87%` | `129,200.00` |
| `Live` | `Long` | `0.0711` | 2,440,000.00 USD | 0.00 USD | 8,840.00 USD | `-5.60%` | `124,379.00` |
| `Live` | `Long` | `0.0712` | 2,430,000.00 USD | 0.00 USD | 389.38 USD | `-5.34%` | `5,465.00` |
| `Live` | `Long` | `0.0713` | 2,430,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-5.20%` | `24,460,119.00` |
| `Live` | `Long` | `0.0714` | 683,410.00 USD | 0.00 USD | 2,370.00 USD | `-5.07%` | `33,195.00` |
| `Live` | `Long` | `0.0716` | 681,040.00 USD | 0.00 USD | 8,120.00 USD | `-4.94%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 672,930.00 USD | 0.00 USD | 1,150.00 USD | `-4.80%` | `16,036.00` |
| `Live` | `Long` | `0.0717` | 671,780.00 USD | 0.00 USD | 2,700.00 USD | `-4.67%` | `37,666.00` |
| `Live` | `Long` | `0.0718` | 669,080.00 USD | 0.00 USD | 960.13 USD | `-4.54%` | `13,363.00` |
| `Live` | `Long` | `0.0720` | 668,120.00 USD | 0.00 USD | 778.93 USD | `-4.41%` | `10,826.00` |
| `Live` | `Long` | `0.0721` | 667,340.00 USD | 0.00 USD | 24,050.00 USD | `-4.27%` | `333,835.00` |
| `Live` | `Long` | `0.0722` | 643,280.00 USD | 0.00 USD | 5,720.00 USD | `-4.01%` | `79,141.00` |
| `Live` | `Long` | `0.0723` | 637,570.00 USD | 0.00 USD | 10,980.00 USD | `-3.87%` | `151,780.00` |
| `Live` | `Long` | `0.0725` | 626,580.00 USD | 0.00 USD | 5,290.00 USD | `-3.74%` | `73,027.00` |
| `Live` | `Long` | `0.0726` | 621,290.00 USD | 0.00 USD | 260.74 USD | `-3.61%` | `3,594.00` |
| `Live` | `Long` | `0.0727` | 621,030.00 USD | 0.00 USD | 948.37 USD | `-3.48%` | `13,054.00` |
| `Live` | `Long` | `0.0727` | 620,080.00 USD | 0.00 USD | 452.21 USD | `-3.34%` | `6,216.00` |
| `Live` | `Long` | `0.0728` | 619,630.00 USD | 0.00 USD | 646.11 USD | `-3.21%` | `8,869.00` |
| `Live` | `Long` | `0.0730` | 618,990.00 USD | 0.00 USD | 72,950.00 USD | `-3.08%` | `1,000,000.00` |
| `Live` | `Long` | `0.0731` | 546,040.00 USD | 0.00 USD | 10,040.00 USD | `-2.94%` | `137,397.00` |
| `Live` | `Long` | `0.0732` | 536,000.00 USD | 0.00 USD | 1,930.00 USD | `-2.81%` | `26,339.00` |
| `Live` | `Long` | `0.0732` | 534,070.00 USD | 0.00 USD | 29,280.00 USD | `-2.68%` | `399,671.00` |
| `Live` | `Long` | `0.0735` | 504,800.00 USD | 0.00 USD | 3,930.00 USD | `-2.41%` | `53,459.00` |
| `Live` | `Long` | `0.0736` | 500,870.00 USD | 0.00 USD | 4,060.00 USD | `-2.28%` | `55,170.00` |
| `Live` | `Long` | `0.0736` | 496,810.00 USD | 0.00 USD | 5,490.00 USD | `-2.15%` | `74,588.00` |
| `Live` | `Long` | `0.0737` | 491,320.00 USD | 0.00 USD | 10,740.00 USD | `-2.01%` | `145,658.00` |
| `Live` | `Long` | `0.0738` | 480,580.00 USD | 0.00 USD | 1,740.00 USD | `-1.88%` | `23,523.00` |
| `Live` | `Long` | `0.0740` | 478,840.00 USD | 0.00 USD | 19,840.00 USD | `-1.75%` | `268,267.00` |
| `Live` | `Long` | `0.0741` | 459,000.00 USD | 0.00 USD | 455,080.00 USD | `-1.62%` | `6,145,600.00` |
| `Live` | `Long` | `0.0741` | 3,920.00 USD | 0.00 USD | 641.77 USD | `-1.48%` | `8,655.00` |
| `Live` | `Long` | `0.0742` | 3,280.00 USD | 0.00 USD | 1,280.00 USD | `-1.35%` | `17,202.00` |
| `Live` | `Long` | `0.0743` | 2,000.00 USD | 0.00 USD | 1,180.00 USD | `-1.22%` | `15,867.00` |
| `Live` | `Long` | `0.0745` | 821.27 USD | 0.00 USD | 176.30 USD | `-1.08%` | `2,368.00` |
| `Live` | `Long` | `0.0746` | 644.98 USD | 0.00 USD | 644.98 USD | `-0.82%` | `8,640.00` |
| `Live` | `Short` | `0.0760` | 10,740.00 USD | 10,740.00 USD | 0.00 USD | `+0.91%` | `141,386.00` |
| `Live` | `Short` | `0.0761` | 15,970.00 USD | 5,230.00 USD | 0.00 USD | `+1.17%` | `68,638.00` |
| `Live` | `Short` | `0.0784` | 16,160.00 USD | 192.04 USD | 0.00 USD | `+4.10%` | `2,451.00` |
| `Live` | `Short` | `0.0785` | 26,690.00 USD | 10,530.00 USD | 0.00 USD | `+4.23%` | `134,228.00` |
| `Live` | `Short` | `0.0791` | 26,840.00 USD | 150.07 USD | 0.00 USD | `+5.16%` | `1,896.00` |
| `Live` | `Short` | `0.0795` | 27,920.00 USD | 1,080.00 USD | 0.00 USD | `+5.56%` | `13,564.00` |
| `Live` | `Short` | `0.0798` | 33,240.00 USD | 5,330.00 USD | 0.00 USD | `+5.96%` | `66,784.00` |
| `Live` | `Short` | `0.0799` | 35,220.00 USD | 1,970.00 USD | 0.00 USD | `+6.22%` | `24,701.00` |
| `Live` | `Short` | `0.0800` | 38,660.00 USD | 3,450.00 USD | 0.00 USD | `+6.36%` | `43,037.00` |
| `Live` | `Short` | `0.0818` | 38,900.00 USD | 241.90 USD | 0.00 USD | `+8.61%` | `2,959.00` |
| `Live` | `Short` | `0.0824` | 39,440.00 USD | 532.64 USD | 0.00 USD | `+9.41%` | `6,468.00` |
| `Live` | `Short` | `0.0832` | 42,890.00 USD | 3,450.00 USD | 0.00 USD | `+10.47%` | `41,543.00` |
| `Live` | `Short` | `0.0837` | 43,180.00 USD | 293.44 USD | 0.00 USD | `+11.14%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 44,760.00 USD | 1,570.00 USD | 0.00 USD | `+11.27%` | `18,767.00` |
| `Live` | `Short` | `0.0843` | 44,860.00 USD | 104.72 USD | 0.00 USD | `+11.94%` | `1,243.00` |
| `Live` | `Short` | `0.0848` | 45,580.00 USD | 723.94 USD | 0.00 USD | `+12.73%` | `8,532.00` |
| `Live` | `Short` | `0.0858` | 45,700.00 USD | 115.30 USD | 0.00 USD | `+14.06%` | `1,343.00` |
| `Live` | `Short` | `0.0862` | 48,040.00 USD | 2,340.00 USD | 0.00 USD | `+14.59%` | `27,165.00` |
| `Live` | `Short` | `0.0881` | 48,510.00 USD | 465.17 USD | 0.00 USD | `+16.99%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 48,920.00 USD | 411.53 USD | 0.00 USD | `+17.92%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 49,340.00 USD | 418.80 USD | 0.00 USD | `+18.31%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 50,570.00 USD | 1,230.00 USD | 0.00 USD | `+18.85%` | `13,799.00` |
| `Live` | `Short` | `0.0911` | 51,310.00 USD | 743.15 USD | 0.00 USD | `+21.10%` | `8,153.00` |
| `Live` | `Short` | `0.0912` | 55,360.00 USD | 4,040.00 USD | 0.00 USD | `+21.24%` | `44,324.00` |
| `Live` | `Short` | `0.0914` | 55,530.00 USD | 171.19 USD | 0.00 USD | `+21.37%` | `1,874.00` |
| `Live` | `Short` | `0.0921` | 55,700.00 USD | 171.49 USD | 0.00 USD | `+22.30%` | `1,863.00` |
| `Live` | `Short` | `0.0950` | 69,500.00 USD | 13,800.00 USD | 0.00 USD | `+26.15%` | `145,305.00` |
| `Live` | `Short` | `0.0953` | 117,120.00 USD | 47,620.00 USD | 0.00 USD | `+26.55%` | `500,000.00` |
| `Live` | `Short` | `0.0954` | 118,050.00 USD | 928.33 USD | 0.00 USD | `+26.68%` | `9,736.00` |
| `Live` | `Short` | `0.0959` | 118,250.00 USD | 195.05 USD | 0.00 USD | `+27.35%` | `2,035.00` |
| `Live` | `Short` | `0.0961` | 118,860.00 USD | 609.59 USD | 0.00 USD | `+27.75%` | `6,340.00` |
| `Live` | `Short` | `0.0978` | 120,730.00 USD | 1,880.00 USD | 0.00 USD | `+29.87%` | `19,213.00` |
| `Live` | `Short` | `0.0979` | 159,930.00 USD | 39,190.00 USD | 0.00 USD | `+30.01%` | `400,522.00` |
| `Live` | `Short` | `0.0983` | 160,400.00 USD | 477.50 USD | 0.00 USD | `+30.54%` | `4,860.00` |
| `Live` | `Short` | `0.0984` | 164,830.00 USD | 4,430.00 USD | 0.00 USD | `+30.67%` | `45,000.00` |
| `Live` | `Short` | `0.0984` | 175,340.00 USD | 10,510.00 USD | 0.00 USD | `+30.80%` | `106,785.00` |
| `Live` | `Short` | `0.1014` | 182,970.00 USD | 7,630.00 USD | 0.00 USD | `+34.79%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 185,940.00 USD | 2,970.00 USD | 0.00 USD | `+35.05%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 186,430.00 USD | 492.85 USD | 0.00 USD | `+35.32%` | `4,839.00` |
| `Live` | `Short` | `0.1032` | 187,760.00 USD | 1,330.00 USD | 0.00 USD | `+37.18%` | `12,841.00` |
| `Live` | `Short` | `0.1048` | 190,220.00 USD | 2,460.00 USD | 0.00 USD | `+39.31%` | `23,466.00` |
| `Live` | `Short` | `0.1061` | 196,330.00 USD | 6,110.00 USD | 0.00 USD | `+41.03%` | `57,554.00` |
| `Live` | `Short` | `0.1070` | 200,470.00 USD | 4,150.00 USD | 0.00 USD | `+42.10%` | `38,791.00` |
| `Live` | `Short` | `0.1085` | 203,710.00 USD | 3,240.00 USD | 0.00 USD | `+44.22%` | `29,849.00` |
| `Live` | `Short` | `0.1120` | 205,580.00 USD | 1,870.00 USD | 0.00 USD | `+48.87%` | `16,647.00` |
| `Live` | `Short` | `0.1127` | 205,790.00 USD | 214.15 USD | 0.00 USD | `+49.67%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 205,940.00 USD | 142.88 USD | 0.00 USD | `+50.07%` | `1,265.00` |
| `Live` | `Short` | `0.1132` | 209,330.00 USD | 3,390.00 USD | 0.00 USD | `+50.33%` | `29,960.00` |
| `Live` | `Short` | `0.1139` | 212,860.00 USD | 3,530.00 USD | 0.00 USD | `+51.26%` | `31,000.00` |
| `Live` | `Short` | `0.1187` | 212,960.00 USD | 106.19 USD | 0.00 USD | `+57.64%` | `895.00` |
| `Live` | `Short` | `0.1222` | 213,760.00 USD | 796.83 USD | 0.00 USD | `+62.42%` | `6,518.00` |
| `Live` | `Short` | `0.1237` | 214,650.00 USD | 893.35 USD | 0.00 USD | `+64.42%` | `7,219.00` |
| `Live` | `Short` | `0.1270` | 214,760.00 USD | 108.80 USD | 0.00 USD | `+68.67%` | `857.00` |
| `Live` | `Short` | `0.1296` | 214,930.00 USD | 171.66 USD | 0.00 USD | `+72.26%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 218,280.00 USD | 3,340.00 USD | 0.00 USD | `+74.25%` | `25,486.00` |
| `Live` | `Short` | `0.1318` | 218,380.00 USD | 102.97 USD | 0.00 USD | `+75.18%` | `781.00` |
| `Live` | `Short` | `0.1338` | 218,580.00 USD | 205.31 USD | 0.00 USD | `+77.70%` | `1,535.00` |
| `Live` | `Short` | `0.1353` | 253,530.00 USD | 34,940.00 USD | 0.00 USD | `+79.70%` | `258,360.00` |
| `Live` | `Short` | `0.1373` | 275,790.00 USD | 22,260.00 USD | 0.00 USD | `+82.35%` | `162,180.00` |
| `Live` | `Short` | `0.1376` | 277,850.00 USD | 2,060.00 USD | 0.00 USD | `+82.75%` | `15,003.00` |
| `Live` | `Short` | `0.1388` | 278,270.00 USD | 416.25 USD | 0.00 USD | `+84.35%` | `3,000.00` |
| `Live` | `Short` | `0.1404` | 278,930.00 USD | 663.63 USD | 0.00 USD | `+86.60%` | `4,725.00` |
| `Live` | `Short` | `0.1411` | 280,730.00 USD | 1,800.00 USD | 0.00 USD | `+87.53%` | `12,780.00` |
| `Live` | `Short` | `0.1432` | 282,600.00 USD | 1,860.00 USD | 0.00 USD | `+90.32%` | `13,010.00` |
| `Live` | `Short` | `0.1444` | 284,140.00 USD | 1,540.00 USD | 0.00 USD | `+91.79%` | `10,691.00` |
| `Live` | `Short` | `0.1479` | 292,440.00 USD | 8,300.00 USD | 0.00 USD | `+96.44%` | `56,144.00` |
| `Live` | `Short` | `0.1497` | 294,420.00 USD | 1,980.00 USD | 0.00 USD | `+98.96%` | `13,240.00` |
| `Live` | `Short` | `0.1502` | 3,440,000.00 USD | 3,140,000.00 USD | 0.00 USD | `+99.63%` | `20,910,149.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 460,870.00 USD | 0.00 USD | 375.42 USD | `-65.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 460,500.00 USD | 0.00 USD | 409.59 USD | `-46.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 460,090.00 USD | 0.00 USD | 132.68 USD | `-45.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 459,960.00 USD | 0.00 USD | 788.27 USD | `-44.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 459,170.00 USD | 0.00 USD | 527.05 USD | `-44.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 458,640.00 USD | 0.00 USD | 286.87 USD | `-40.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 458,350.00 USD | 0.00 USD | 252.42 USD | `-38.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 458,100.00 USD | 0.00 USD | 468.67 USD | `-37.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 457,630.00 USD | 0.00 USD | 5,160.00 USD | `-34.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 452,470.00 USD | 0.00 USD | 920.48 USD | `-34.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 451,550.00 USD | 0.00 USD | 1,730.00 USD | `-33.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 449,820.00 USD | 0.00 USD | 175.41 USD | `-31.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 449,650.00 USD | 0.00 USD | 2,670.00 USD | `-28.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 446,970.00 USD | 0.00 USD | 1,370.00 USD | `-26.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 445,600.00 USD | 0.00 USD | 437.58 USD | `-25.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 445,160.00 USD | 0.00 USD | 752.54 USD | `-22.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 444,410.00 USD | 0.00 USD | 9,830.00 USD | `-21.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 434,580.00 USD | 0.00 USD | 984.67 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 433,590.00 USD | 0.00 USD | 668.84 USD | `-20.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 432,920.00 USD | 0.00 USD | 134.12 USD | `-19.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 432,790.00 USD | 0.00 USD | 8,800.00 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 423,990.00 USD | 0.00 USD | 504.26 USD | `-17.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 423,490.00 USD | 0.00 USD | 2,280.00 USD | `-17.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 421,210.00 USD | 0.00 USD | 1,280.00 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 419,930.00 USD | 0.00 USD | 920.18 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 419,010.00 USD | 0.00 USD | 370.79 USD | `-14.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 418,640.00 USD | 0.00 USD | 1,130.00 USD | `-13.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 417,510.00 USD | 0.00 USD | 362.24 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 417,150.00 USD | 0.00 USD | 3,140.00 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 414,010.00 USD | 0.00 USD | 1,100.00 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 412,910.00 USD | 0.00 USD | 1,200.00 USD | `-12.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 411,710.00 USD | 0.00 USD | 996.31 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 410,720.00 USD | 0.00 USD | 632.88 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 410,080.00 USD | 0.00 USD | 115.57 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 409,970.00 USD | 0.00 USD | 33,620.00 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 376,340.00 USD | 0.00 USD | 12,860.00 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 363,480.00 USD | 0.00 USD | 1,260.00 USD | `-10.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 362,220.00 USD | 0.00 USD | 108.08 USD | `-10.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 362,110.00 USD | 0.00 USD | 2,960.00 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 359,150.00 USD | 0.00 USD | 1,430.00 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 357,720.00 USD | 0.00 USD | 7,990.00 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 349,730.00 USD | 0.00 USD | 8,580.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 341,150.00 USD | 0.00 USD | 606.47 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 340,550.00 USD | 0.00 USD | 38,710.00 USD | `-8.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 301,840.00 USD | 0.00 USD | 660.06 USD | `-8.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 301,180.00 USD | 0.00 USD | 102.34 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 301,080.00 USD | 0.00 USD | 218.87 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 300,860.00 USD | 0.00 USD | 144.59 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 300,720.00 USD | 0.00 USD | 925.29 USD | `-7.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 299,790.00 USD | 0.00 USD | 697.50 USD | `-7.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 299,090.00 USD | 0.00 USD | 16,840.00 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 282,250.00 USD | 0.00 USD | 1,800.00 USD | `-6.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 280,450.00 USD | 0.00 USD | 523.23 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 279,930.00 USD | 0.00 USD | 235.12 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 279,690.00 USD | 0.00 USD | 204.40 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 279,490.00 USD | 0.00 USD | 107,570.00 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 171,920.00 USD | 0.00 USD | 12,930.00 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 158,990.00 USD | 0.00 USD | 20,070.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 138,920.00 USD | 0.00 USD | 608.76 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 138,310.00 USD | 0.00 USD | 16,880.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 121,430.00 USD | 0.00 USD | 1,670.00 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 119,760.00 USD | 0.00 USD | 4,710.00 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 115,050.00 USD | 0.00 USD | 8,570.00 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 106,480.00 USD | 0.00 USD | 413.42 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 106,070.00 USD | 0.00 USD | 881.82 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 105,190.00 USD | 0.00 USD | 1,330.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 103,850.00 USD | 0.00 USD | 621.12 USD | `-3.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 103,230.00 USD | 0.00 USD | 1,430.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 101,800.00 USD | 0.00 USD | 29,060.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 72,730.00 USD | 0.00 USD | 1,610.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 71,120.00 USD | 0.00 USD | 2,090.00 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 69,030.00 USD | 0.00 USD | 23,870.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 45,160.00 USD | 0.00 USD | 28,640.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 16,520.00 USD | 0.00 USD | 2,910.00 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 13,610.00 USD | 0.00 USD | 115.12 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 13,500.00 USD | 0.00 USD | 4,680.00 USD | `-1.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 8,820.00 USD | 0.00 USD | 1,220.00 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 7,600.00 USD | 0.00 USD | 2,900.00 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 4,710.00 USD | 0.00 USD | 107.66 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 4,600.00 USD | 0.00 USD | 744.50 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 3,850.00 USD | 0.00 USD | 1,410.00 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 2,440.00 USD | 0.00 USD | 375.86 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 2,070.00 USD | 0.00 USD | 193.90 USD | `-0.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 1,870.00 USD | 0.00 USD | 140.04 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 1,730.00 USD | 0.00 USD | 397.83 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 1,330.00 USD | 0.00 USD | 199.48 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 1,130.00 USD | 0.00 USD | 736.17 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 398.60 USD | 0.00 USD | 398.60 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 192.73 USD | 192.73 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 550.86 USD | 358.13 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0757` | 5,430.00 USD | 4,880.00 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0759` | 5,630.00 USD | 193.49 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0760` | 7,900.00 USD | 2,280.00 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 11,040.00 USD | 3,130.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 11,840.00 USD | 806.81 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 12,200.00 USD | 359.60 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 12,540.00 USD | 335.56 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 13,800.00 USD | 1,260.00 USD | 0.00 USD | `+1.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 14,010.00 USD | 203.47 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 17,550.00 USD | 3,540.00 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 17,740.00 USD | 192.95 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 18,040.00 USD | 297.49 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 18,850.00 USD | 816.05 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 34,250.00 USD | 15,400.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 38,230.00 USD | 3,980.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 42,130.00 USD | 3,900.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 45,950.00 USD | 3,820.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 46,170.00 USD | 215.00 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 46,770.00 USD | 604.81 USD | 0.00 USD | `+3.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 48,260.00 USD | 1,490.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 90,070.00 USD | 41,810.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 131,510.00 USD | 41,440.00 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 134,520.00 USD | 3,000.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 136,520.00 USD | 2,010.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 137,870.00 USD | 1,350.00 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 138,090.00 USD | 222.46 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 142,460.00 USD | 4,370.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 143,030.00 USD | 573.31 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 158,820.00 USD | 15,790.00 USD | 0.00 USD | `+4.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 159,320.00 USD | 495.57 USD | 0.00 USD | `+4.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 162,350.00 USD | 3,030.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 162,650.00 USD | 303.73 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 164,220.00 USD | 1,560.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 166,580.00 USD | 2,360.00 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 171,170.00 USD | 4,600.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 173,430.00 USD | 2,260.00 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 174,440.00 USD | 1,010.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 174,590.00 USD | 148.25 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 175,150.00 USD | 556.77 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 175,280.00 USD | 125.45 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 175,510.00 USD | 230.40 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 175,820.00 USD | 319.16 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 176,940.00 USD | 1,120.00 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 199,480.00 USD | 22,540.00 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 199,880.00 USD | 400.91 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 200,080.00 USD | 200.46 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 200,340.00 USD | 259.13 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 201,050.00 USD | 707.08 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 203,310.00 USD | 2,260.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 300,090.00 USD | 96,780.00 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 300,900.00 USD | 807.50 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 301,160.00 USD | 257.18 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 301,580.00 USD | 424.74 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 301,680.00 USD | 101.80 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 303,070.00 USD | 1,380.00 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 303,330.00 USD | 264.63 USD | 0.00 USD | `+7.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 304,770.00 USD | 1,430.00 USD | 0.00 USD | `+8.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 305,260.00 USD | 492.77 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 306,280.00 USD | 1,020.00 USD | 0.00 USD | `+8.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 308,840.00 USD | 2,560.00 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 309,860.00 USD | 1,030.00 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 312,470.00 USD | 2,610.00 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 312,800.00 USD | 327.80 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 313,410.00 USD | 607.58 USD | 0.00 USD | `+9.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 320,290.00 USD | 6,880.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 321,090.00 USD | 800.79 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 321,610.00 USD | 512.05 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 321,850.00 USD | 240.26 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 322,240.00 USD | 389.31 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 322,940.00 USD | 706.02 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 323,250.00 USD | 303.56 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 323,360.00 USD | 112.89 USD | 0.00 USD | `+10.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 323,740.00 USD | 381.45 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 323,900.00 USD | 155.82 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 325,330.00 USD | 1,430.00 USD | 0.00 USD | `+10.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 325,470.00 USD | 138.69 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 326,730.00 USD | 1,260.00 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 326,940.00 USD | 210.88 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,080,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,080,000.00 USD | 3,150.00 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,080,000.00 USD | 341.34 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,080,000.00 USD | 107.71 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,080,000.00 USD | 2,690.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,090,000.00 USD | 1,330.00 USD | 0.00 USD | `+12.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,090,000.00 USD | 219.07 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,090,000.00 USD | 326.97 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,090,000.00 USD | 242.84 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,100,000.00 USD | 10,140.00 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0851` | 2,100,000.00 USD | 152.92 USD | 0.00 USD | `+13.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,100,000.00 USD | 876.11 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,100,000.00 USD | 205.59 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,100,000.00 USD | 126.76 USD | 0.00 USD | `+13.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,100,000.00 USD | 307.41 USD | 0.00 USD | `+13.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,100,000.00 USD | 614.09 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,100,000.00 USD | 644.62 USD | 0.00 USD | `+14.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0861` | 2,100,000.00 USD | 180.45 USD | 0.00 USD | `+14.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,100,000.00 USD | 2,020.00 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,150,000.00 USD | 43,760.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,150,000.00 USD | 1,080.00 USD | 0.00 USD | `+14.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,150,000.00 USD | 384.06 USD | 0.00 USD | `+15.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,150,000.00 USD | 1,840.00 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,150,000.00 USD | 2,760.00 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,150,000.00 USD | 117.71 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,150,000.00 USD | 111.61 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,150,000.00 USD | 571.18 USD | 0.00 USD | `+16.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,150,000.00 USD | 375.94 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,150,000.00 USD | 627.55 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,150,000.00 USD | 211.04 USD | 0.00 USD | `+17.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,150,000.00 USD | 108.36 USD | 0.00 USD | `+17.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,150,000.00 USD | 543.32 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,160,000.00 USD | 1,820.00 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,160,000.00 USD | 2,080.00 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,180,000.00 USD | 17,680.00 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,180,000.00 USD | 1,640.00 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0896` | 2,180,000.00 USD | 1,640.00 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,180,000.00 USD | 5,010.00 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,190,000.00 USD | 1,090.00 USD | 0.00 USD | `+19.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,190,000.00 USD | 224.86 USD | 0.00 USD | `+20.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,210,000.00 USD | 20,540.00 USD | 0.00 USD | `+20.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,210,000.00 USD | 114.93 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,210,000.00 USD | 679.12 USD | 0.00 USD | `+20.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,210,000.00 USD | 173.36 USD | 0.00 USD | `+20.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,210,000.00 USD | 1,810.00 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,210,000.00 USD | 1,530.00 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,210,000.00 USD | 2,170.00 USD | 0.00 USD | `+22.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,210,000.00 USD | 541.32 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,350,000.00 USD | 137,500.00 USD | 0.00 USD | `+22.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,350,000.00 USD | 691.07 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,360,000.00 USD | 6,250.00 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,370,000.00 USD | 13,480.00 USD | 0.00 USD | `+23.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,370,000.00 USD | 734.82 USD | 0.00 USD | `+23.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,370,000.00 USD | 1,230.00 USD | 0.00 USD | `+23.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,370,000.00 USD | 184.09 USD | 0.00 USD | `+24.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,370,000.00 USD | 1,120.00 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,380,000.00 USD | 1,860.00 USD | 0.00 USD | `+24.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,380,000.00 USD | 512.15 USD | 0.00 USD | `+25.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,380,000.00 USD | 6,620.00 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,380,000.00 USD | 404.96 USD | 0.00 USD | `+25.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,380,000.00 USD | 129.85 USD | 0.00 USD | `+26.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,390,000.00 USD | 3,740.00 USD | 0.00 USD | `+27.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0959` | 2,390,000.00 USD | 2,400.00 USD | 0.00 USD | `+27.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,390,000.00 USD | 409.17 USD | 0.00 USD | `+27.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,390,000.00 USD | 203.74 USD | 0.00 USD | `+28.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,390,000.00 USD | 2,800.00 USD | 0.00 USD | `+29.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,390,000.00 USD | 1,320.00 USD | 0.00 USD | `+29.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,400,000.00 USD | 694.56 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,400,000.00 USD | 940.91 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,400,000.00 USD | 2,980.00 USD | 0.00 USD | `+31.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,400,000.00 USD | 104.99 USD | 0.00 USD | `+31.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,400,000.00 USD | 1,930.00 USD | 0.00 USD | `+31.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,400,000.00 USD | 1,490.00 USD | 0.00 USD | `+32.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,400,000.00 USD | 1,090.00 USD | 0.00 USD | `+32.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,400,000.00 USD | 438.96 USD | 0.00 USD | `+32.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,410,000.00 USD | 973.76 USD | 0.00 USD | `+32.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,520,000.00 USD | 111,100.00 USD | 0.00 USD | `+32.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,520,000.00 USD | 175.59 USD | 0.00 USD | `+32.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,520,000.00 USD | 482.89 USD | 0.00 USD | `+33.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,520,000.00 USD | 201.90 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,520,000.00 USD | 489.46 USD | 0.00 USD | `+34.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,520,000.00 USD | 103.68 USD | 0.00 USD | `+34.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,520,000.00 USD | 203.70 USD | 0.00 USD | `+35.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,520,000.00 USD | 3,810.00 USD | 0.00 USD | `+35.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,530,000.00 USD | 11,200.00 USD | 0.00 USD | `+35.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,540,000.00 USD | 4,330.00 USD | 0.00 USD | `+35.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,540,000.00 USD | 205.50 USD | 0.00 USD | `+36.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,540,000.00 USD | 3,490.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,540,000.00 USD | 1,300.00 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,540,000.00 USD | 207.50 USD | 0.00 USD | `+37.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,540,000.00 USD | 813.88 USD | 0.00 USD | `+38.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,570,000.00 USD | 23,160.00 USD | 0.00 USD | `+38.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,570,000.00 USD | 781.51 USD | 0.00 USD | `+38.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,570,000.00 USD | 209.30 USD | 0.00 USD | `+39.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,570,000.00 USD | 1,440.00 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,570,000.00 USD | 5,140.00 USD | 0.00 USD | `+39.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,570,000.00 USD | 585.32 USD | 0.00 USD | `+39.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,570,000.00 USD | 210.90 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,580,000.00 USD | 1,850.00 USD | 0.00 USD | `+40.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,580,000.00 USD | 105.75 USD | 0.00 USD | `+40.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,580,000.00 USD | 3,220.00 USD | 0.00 USD | `+40.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,580,000.00 USD | 1,600.00 USD | 0.00 USD | `+41.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,580,000.00 USD | 212.90 USD | 0.00 USD | `+41.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,580,000.00 USD | 472.63 USD | 0.00 USD | `+42.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,580,000.00 USD | 214.50 USD | 0.00 USD | `+42.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,580,000.00 USD | 1,040.00 USD | 0.00 USD | `+43.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,580,000.00 USD | 136.12 USD | 0.00 USD | `+43.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,580,000.00 USD | 216.10 USD | 0.00 USD | `+43.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,620,000.00 USD | 40,920.00 USD | 0.00 USD | `+44.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,630,000.00 USD | 217.90 USD | 0.00 USD | `+44.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,630,000.00 USD | 219.70 USD | 0.00 USD | `+45.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,630,000.00 USD | 7,920.00 USD | 0.00 USD | `+46.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,630,000.00 USD | 154.22 USD | 0.00 USD | `+46.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,630,000.00 USD | 221.30 USD | 0.00 USD | `+47.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,630,000.00 USD | 1,050.00 USD | 0.00 USD | `+47.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,660,000.00 USD | 24,440.00 USD | 0.00 USD | `+47.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,660,000.00 USD | 223.10 USD | 0.00 USD | `+48.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,660,000.00 USD | 2,120.00 USD | 0.00 USD | `+49.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,660,000.00 USD | 226.30 USD | 0.00 USD | `+50.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,660,000.00 USD | 351.57 USD | 0.00 USD | `+51.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,660,000.00 USD | 950.34 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,660,000.00 USD | 229.50 USD | 0.00 USD | `+52.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,660,000.00 USD | 771.08 USD | 0.00 USD | `+52.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,660,000.00 USD | 230.90 USD | 0.00 USD | `+53.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,660,000.00 USD | 288.18 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,670,000.00 USD | 619.10 USD | 0.00 USD | `+53.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,670,000.00 USD | 1,250.00 USD | 0.00 USD | `+54.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,670,000.00 USD | 1,050.00 USD | 0.00 USD | `+54.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,670,000.00 USD | 232.30 USD | 0.00 USD | `+54.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,670,000.00 USD | 1,600.00 USD | 0.00 USD | `+55.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,670,000.00 USD | 1,050.00 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,670,000.00 USD | 3,730.00 USD | 0.00 USD | `+55.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,670,000.00 USD | 676.22 USD | 0.00 USD | `+56.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,680,000.00 USD | 648.25 USD | 0.00 USD | `+56.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,680,000.00 USD | 1,510.00 USD | 0.00 USD | `+56.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,680,000.00 USD | 448.52 USD | 0.00 USD | `+57.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1186` | 2,680,000.00 USD | 136.93 USD | 0.00 USD | `+57.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,680,000.00 USD | 124.58 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,680,000.00 USD | 1,050.00 USD | 0.00 USD | `+58.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,680,000.00 USD | 691.80 USD | 0.00 USD | `+59.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,800,000.00 USD | 117,860.00 USD | 0.00 USD | `+59.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,800,000.00 USD | 143.22 USD | 0.00 USD | `+59.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1207` | 2,800,000.00 USD | 803.95 USD | 0.00 USD | `+60.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,800,000.00 USD | 1,380.00 USD | 0.00 USD | `+60.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,800,000.00 USD | 2,270.00 USD | 0.00 USD | `+62.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,800,000.00 USD | 871.99 USD | 0.00 USD | `+62.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,830,000.00 USD | 24,560.00 USD | 0.00 USD | `+68.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,830,000.00 USD | 400.21 USD | 0.00 USD | `+68.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,840,000.00 USD | 13,850.00 USD | 0.00 USD | `+75.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,840,000.00 USD | 2,360.00 USD | 0.00 USD | `+75.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,850,000.00 USD | 4,160.00 USD | 0.00 USD | `+80.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,850,000.00 USD | 235.54 USD | 0.00 USD | `+85.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,850,000.00 USD | 1,160.00 USD | 0.00 USD | `+87.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,850,000.00 USD | 173.57 USD | 0.00 USD | `+88.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,850,000.00 USD | 380.09 USD | 0.00 USD | `+89.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,870,000.00 USD | 17,150.00 USD | 0.00 USD | `+89.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,870,000.00 USD | 433.35 USD | 0.00 USD | `+91.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,870,000.00 USD | 3,640.00 USD | 0.00 USD | `+95.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,930,000.00 USD | 55,720.00 USD | 0.00 USD | `+96.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,930,000.00 USD | 2,120.00 USD | 0.00 USD | `+96.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,950,000.00 USD | 18,810.00 USD | 0.00 USD | `+99.23%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.0674` | 9,270,000.00 USD | 0.00 USD | 9,270,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0676` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 45,230.00 USD | 30,260.00 USD | 0.00 USD |
| `1D` | `0.0678` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 3,200.00 USD | 39,890.00 USD | 58,170.00 USD |
| `1D` | `0.0680` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD |
| `1D` | `0.0682` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 2,550.00 USD | 33,950.00 USD | 134,240.00 USD |
| `1D` | `0.0688` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD |
| `1D` | `0.0692` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0696` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `1D` | `0.0698` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 39,980.00 USD | 38,520.00 USD | 36,010.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0700` | 8,740,000.00 USD | 0.00 USD | 8,740,000.00 USD | 142,320.00 USD | 78,270.00 USD | 57,790.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0702` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 114,140.00 USD | 54,820.00 USD | 27,690.00 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0704` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 132,460.00 USD | 55,620.00 USD | 61,970.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0706` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 71,470.00 USD | 54,000.00 USD | 59,120.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0708` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 79,650.00 USD | 38,000.00 USD | 49,380.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0710` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0712` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 79,710.00 USD | 21,060.00 USD | 45,140.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0714` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 77,730.00 USD | 100,220.00 USD | 71,010.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0716` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 55,590.00 USD | 40,440.00 USD | 38,710.00 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0718` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 83,040.00 USD | 44,590.00 USD | 54,340.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0720` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 77,220.00 USD | 32,390.00 USD | 42,780.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0722` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 176,450.00 USD | 97,110.00 USD | 34,100.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0724` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 74,530.00 USD | 264,070.00 USD | 266,050.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0726` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 88,190.00 USD | 22,980.00 USD | 23,840.00 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0728` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 223,190.00 USD | 85,670.00 USD | 387,260.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0730` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 39,900.00 USD | 0.00 USD | 18,940.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0732` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 90,450.00 USD | 0.00 USD | 100.25 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0734` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 23,950.00 USD | 0.00 USD | 70,160.00 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0736` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 262,120.00 USD | 151,300.00 USD | 299.76 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0738` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 83,700.00 USD | 199,460.00 USD | 285,000.00 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0740` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 67,420.00 USD | 161,430.00 USD | 78,750.00 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0742` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 323,330.00 USD | 0.00 USD | 666,950.00 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0744` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 138,520.00 USD | 257,350.00 USD | 183,260.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0746` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 232,670.00 USD | 232,630.00 USD | 150,360.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0748` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 391,880.00 USD | 181,940.00 USD | 161,700.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0750` | 472,380.00 USD | 0.00 USD | 472,380.00 USD | 203,330.00 USD | 0.00 USD | 269,050.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0760` | 883.41 USD | 883.41 USD | 0.00 USD | 0.00 USD | 0.00 USD | 883.41 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0762` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 604,660.00 USD | 706,100.00 USD | 590.17 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0764` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 756,300.00 USD | 505,620.00 USD | 0.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0766` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 1,320,000.00 USD | 690,020.00 USD | 912.09 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0768` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 609,920.00 USD | 633,440.00 USD | 521,110.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0770` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 484,760.00 USD | 448,120.00 USD | 402,900.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0772` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 502,750.00 USD | 241,160.00 USD | 878,520.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0774` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 65,160.00 USD | 169,730.00 USD | 102,410.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0776` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 7,430.00 USD | 12,000.00 USD | 355.85 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0778` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 16,790.00 USD | 347,140.00 USD | 213,010.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0780` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 0.00 USD | 117,930.00 USD | 141,980.00 USD |
| `1D` | `0.0782` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 118,220.00 USD | 61,820.00 USD | 0.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0784` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 273,810.00 USD | 186,580.00 USD | 184,660.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0786` | 12,210,000.00 USD | 12,210,000.00 USD | 0.00 USD | 356,780.00 USD | 227,550.00 USD | 298,550.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0788` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 374,310.00 USD | 488,720.00 USD | 386,640.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0790` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 245,210.00 USD | 113,150.00 USD | 82,210.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0792` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 48,420.00 USD | 45,770.00 USD | 52,050.00 USD |
| `1D` | `0.0794` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 75,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0796` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 149,220.00 USD | 0.00 USD | 88,390.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0798` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 220,340.00 USD | 250,960.00 USD | 241,210.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0800` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 178,150.00 USD | 156,700.00 USD | 290,300.00 USD |
| `1D` | `0.0802` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 7,730.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `0.0804` | 15,770,000.00 USD | 15,770,000.00 USD | 0.00 USD | 11,880.00 USD | 10,910.00 USD | 38,610.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0806` | 16,170,000.00 USD | 16,170,000.00 USD | 0.00 USD | 84,020.00 USD | 58,270.00 USD | 256,410.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0808` | 17,700,000.00 USD | 17,700,000.00 USD | 0.00 USD | 634,220.00 USD | 339,110.00 USD | 564,550.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0810` | 19,140,000.00 USD | 19,140,000.00 USD | 0.00 USD | 771,010.00 USD | 517,160.00 USD | 144,580.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0812` | 19,820,000.00 USD | 19,820,000.00 USD | 0.00 USD | 202,360.00 USD | 340,900.00 USD | 135,390.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0814` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 74,410.00 USD | 108,600.00 USD | 515,840.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0816` | 21,870,000.00 USD | 21,870,000.00 USD | 0.00 USD | 675,530.00 USD | 335,640.00 USD | 348,800.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0818` | 23,240,000.00 USD | 23,240,000.00 USD | 0.00 USD | 613,810.00 USD | 315,240.00 USD | 438,420.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0820` | 24,750,000.00 USD | 24,750,000.00 USD | 0.00 USD | 349,970.00 USD | 585,520.00 USD | 576,570.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0822` | 25,800,000.00 USD | 25,800,000.00 USD | 0.00 USD | 472,760.00 USD | 248,830.00 USD | 327,420.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0824` | 26,730,000.00 USD | 26,730,000.00 USD | 0.00 USD | 422,760.00 USD | 301,930.00 USD | 207,110.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0826` | 27,440,000.00 USD | 27,440,000.00 USD | 0.00 USD | 278,370.00 USD | 206,840.00 USD | 217,880.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0828` | 27,910,000.00 USD | 27,910,000.00 USD | 0.00 USD | 278,450.00 USD | 124,170.00 USD | 66,080.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0830` | 28,690,000.00 USD | 28,690,000.00 USD | 0.00 USD | 396,370.00 USD | 209,720.00 USD | 178,180.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0832` | 29,240,000.00 USD | 29,240,000.00 USD | 0.00 USD | 320,350.00 USD | 100,300.00 USD | 128,700.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0834` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 279,570.00 USD | 162,910.00 USD | 282,900.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0836` | 30,620,000.00 USD | 30,620,000.00 USD | 0.00 USD | 156,630.00 USD | 239,500.00 USD | 260,040.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0838` | 31,010,000.00 USD | 31,010,000.00 USD | 0.00 USD | 238,020.00 USD | 86,330.00 USD | 59,580.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0840` | 31,140,000.00 USD | 31,140,000.00 USD | 0.00 USD | 89,110.00 USD | 15,480.00 USD | 29,290.00 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0842` | 31,240,000.00 USD | 31,240,000.00 USD | 0.00 USD | 54,450.00 USD | 2,010.00 USD | 47,720.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0844` | 31,360,000.00 USD | 31,360,000.00 USD | 0.00 USD | 116,360.00 USD | 0.00 USD | 574.90 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0846` | 31,470,000.00 USD | 31,470,000.00 USD | 0.00 USD | 90,570.00 USD | 16,670.00 USD | 264.82 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0848` | 31,490,000.00 USD | 31,490,000.00 USD | 0.00 USD | 22,580.00 USD | 0.00 USD | 284.68 USD |
| `7D` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `1D` | `0.0850` | 31,520,000.00 USD | 31,520,000.00 USD | 0.00 USD | 23,830.00 USD | 0.00 USD | 448.19 USD |
| `7D` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `1D` | `0.0852` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 35,100.00 USD | 24,590.00 USD | 17,300.00 USD |
| `7D` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD |
| `1D` | `0.0854` | 31,670,000.00 USD | 31,670,000.00 USD | 0.00 USD | 40,150.00 USD | 13,930.00 USD | 20,220.00 USD |
| `7D` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 0.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD |
| `1D` | `0.0856` | 31,960,000.00 USD | 31,960,000.00 USD | 0.00 USD | 162,130.00 USD | 78,270.00 USD | 56,120.00 USD |
| `7D` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 0.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD |
| `1D` | `0.0858` | 32,170,000.00 USD | 32,170,000.00 USD | 0.00 USD | 123,990.00 USD | 54,820.00 USD | 27,690.00 USD |
| `7D` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD |
| `1D` | `0.0860` | 32,420,000.00 USD | 32,420,000.00 USD | 0.00 USD | 130,590.00 USD | 55,620.00 USD | 60,210.00 USD |
| `7D` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0862` | 32,580,000.00 USD | 32,580,000.00 USD | 0.00 USD | 54,010.00 USD | 54,000.00 USD | 57,860.00 USD |
| `7D` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 0.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0864` | 32,630,000.00 USD | 32,630,000.00 USD | 0.00 USD | 22,510.00 USD | 20,050.00 USD | 5,370.00 USD |
| `7D` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 0.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD |
| `1D` | `0.0866` | 32,750,000.00 USD | 32,750,000.00 USD | 0.00 USD | 57,180.00 USD | 17,950.00 USD | 44,690.00 USD |
| `7D` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD |
| `1D` | `0.0868` | 32,880,000.00 USD | 32,880,000.00 USD | 0.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD |
| `7D` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 0.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD |
| `1D` | `0.0870` | 33,010,000.00 USD | 33,010,000.00 USD | 0.00 USD | 68,060.00 USD | 21,060.00 USD | 42,320.00 USD |
| `7D` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 0.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0872` | 33,250,000.00 USD | 33,250,000.00 USD | 0.00 USD | 67,420.00 USD | 100,220.00 USD | 71,010.00 USD |
| `7D` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD |
| `1D` | `0.0874` | 33,310,000.00 USD | 33,310,000.00 USD | 0.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD |
| `7D` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD |
| `1D` | `0.0876` | 33,370,000.00 USD | 33,370,000.00 USD | 0.00 USD | 30,130.00 USD | 31,610.00 USD | 0.00 USD |
| `7D` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 0.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD |
| `1D` | `0.0878` | 33,520,000.00 USD | 33,520,000.00 USD | 0.00 USD | 50,320.00 USD | 44,590.00 USD | 54,340.00 USD |
| `7D` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 0.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD |
| `1D` | `0.0880` | 33,630,000.00 USD | 33,630,000.00 USD | 0.00 USD | 50,910.00 USD | 17,330.00 USD | 38,970.00 USD |
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
  * Total Open Interest: `1.07B` | Total OI Tokens: `14,111,035,849.2 DOGE`
  * 1h OI Change: `-2.89%` | 4h OI Change: `-5.28%` | 24h OI Change: `-7.36%`
  * Exchange Breakdown: Binance=`253.46M` | Bybit=`106.77M` | OKX=`109.02M` | Hyperliquid=`75.89M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `28.49K` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0020%` | **USDT KuCoin** | `0.0077%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0003%` | **USDT Bitget** | `0.0053%` |
| **CoinM Binance** | `0.0066%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `49.97%` | `50.03%` | `1.00` | 88,220,000.00 USD |
| `15M` | `Binance` | `48.12%` | `51.88%` | `0.93` | 41,540,000.00 USD |
| `15M` | `OKX` | `51%` | `49%` | `1.04` | 16,690,000.00 USD |
| `15M` | `Bybit` | `57.4%` | `42.6%` | `1.35` | 10,150,000.00 USD |
| `15M` | `KuCoin` | `48.93%` | `51.07%` | `0.96` | 1,200,000.00 USD |
| `15M` | `Gate` | `49.5%` | `50.5%` | `0.98` | 6,370,000.00 USD |
| `15M` | `Bitget` | `47.62%` | `52.38%` | `0.91` | 1,680,000.00 USD |
| `15M` | `BingX` | `58.75%` | `41.25%` | `1.42` | 513,170.00 USD |
| `15M` | `MEXC` | `57.09%` | `42.91%` | `1.33` | 4,070,000.00 USD |
| `15M` | `Bitunix` | `44.55%` | `55.45%` | `0.80` | 2,060,000.00 USD |
| `15M` | `Hyperliquid` | `47.04%` | `52.96%` | `0.89` | 961,830.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `41.79%` | `58.21%` | `0.72` | 189,090.00 USD |
| `15M` | `Crypto.com` | `50.77%` | `49.23%` | `1.03` | 113,100.00 USD |
| `15M` | `WhiteBIT` | `26.51%` | `73.49%` | `0.36` | 813,980.00 USD |
| `15M` | `HTX` | `32.95%` | `67.05%` | `0.49` | 314,230.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `54.93%` | `45.07%` | `1.22` | 363,590.00 USD |
| `15M` | `Aster` | `46.03%` | `53.97%` | `0.85` | 1,150,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `72.32%` | `27.68%` | `2.61` | 47,550.00 USD |
| `15M` | `Whale Positions` | `48.12%` | `51.88%` | `0.93` | 41,540,000.00 USD |
| `15M` | `Global Accounts` | `49.97%` | `50.03%` | `1.00` | 88,220,000.00 USD |
| `1H` | `DOGE` | `45.16%` | `54.84%` | `0.82` | 1,360,000,000.00 USD |
| `1H` | `Binance` | `44.6%` | `55.4%` | `0.81` | 799,270,000.00 USD |
| `1H` | `OKX` | `46.99%` | `53.01%` | `0.89` | 89,930,000.00 USD |
| `1H` | `Bybit` | `43.82%` | `56.18%` | `0.78` | 146,650,000.00 USD |
| `1H` | `KuCoin` | `42.93%` | `57.07%` | `0.75` | 9,140,000.00 USD |
| `1H` | `Gate` | `48.52%` | `51.48%` | `0.94` | 29,390,000.00 USD |
| `1H` | `Bitget` | `35.22%` | `64.78%` | `0.54` | 39,810,000.00 USD |
| `1H` | `BingX` | `55.2%` | `44.8%` | `1.23` | 11,770,000.00 USD |
| `1H` | `MEXC` | `50.79%` | `49.21%` | `1.03` | 19,450,000.00 USD |
| `1H` | `Bitunix` | `44.63%` | `55.37%` | `0.81` | 31,230,000.00 USD |
| `1H` | `Hyperliquid` | `49.44%` | `50.56%` | `0.98` | 122,200,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.07%` | `45.93%` | `1.18` | 8,700,000.00 USD |
| `1H` | `Crypto.com` | `50.14%` | `49.86%` | `1.01` | 0.00 USD |
| `1H` | `WhiteBIT` | `19.36%` | `80.64%` | `0.24` | 2,370,000.00 USD |
| `1H` | `HTX` | `31.97%` | `68.03%` | `0.47` | 1,640,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.08%` | `57.92%` | `0.73` | 3,110,000.00 USD |
| `1H` | `Aster` | `50.48%` | `49.52%` | `1.02` | 26,860,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.8%` | `45.2%` | `1.21` | 15,380,000.00 USD |
| `1H` | `Whale Positions` | `44.6%` | `55.4%` | `0.81` | 799,270,000.00 USD |
| `1H` | `Global Accounts` | `45.16%` | `54.84%` | `0.82` | 1,360,000,000.00 USD |
| `4H` | `DOGE` | `47.60%` | `52.40%` | `0.91` | 1,590,000,000.00 USD |
| `4H` | `Binance` | `47.81%` | `52.19%` | `0.92` | 939,940,000.00 USD |
| `4H` | `OKX` | `47.4%` | `52.6%` | `0.90` | 102,230,000.00 USD |
| `4H` | `Bybit` | `48.25%` | `51.75%` | `0.93` | 169,110,000.00 USD |
| `4H` | `KuCoin` | `45.27%` | `54.73%` | `0.83` | 10,820,000.00 USD |
| `4H` | `Gate` | `49.29%` | `50.71%` | `0.97` | 38,020,000.00 USD |
| `4H` | `Bitget` | `45.67%` | `54.33%` | `0.84` | 46,030,000.00 USD |
| `4H` | `BingX` | `44.62%` | `55.38%` | `0.81` | 18,880,000.00 USD |
| `4H` | `MEXC` | `48.61%` | `51.39%` | `0.95` | 22,250,000.00 USD |
| `4H` | `Bitunix` | `48.56%` | `51.44%` | `0.94` | 37,810,000.00 USD |
| `4H` | `Hyperliquid` | `45.19%` | `54.81%` | `0.82` | 134,440,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.68%` | `49.32%` | `1.03` | 11,320,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `55.44%` | `44.56%` | `1.24` | 3,120,000.00 USD |
| `4H` | `HTX` | `41.29%` | `58.71%` | `0.70` | 2,400,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `36.39%` | `63.61%` | `0.57` | 3,540,000.00 USD |
| `4H` | `Aster` | `47.54%` | `52.46%` | `0.91` | 30,460,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.49%` | `47.51%` | `1.10` | 17,090,000.00 USD |
| `4H` | `Whale Positions` | `47.81%` | `52.19%` | `0.92` | 939,940,000.00 USD |
| `4H` | `Global Accounts` | `47.60%` | `52.40%` | `0.91` | 1,590,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0793` | `0.0793` | `0.0793` | `0.0795` | `0.0790` | 3,072,363.78 USD | 1,995,905.48 USD | 1,076,458.30 USD | 919,447.18 USD | `+29.93%` | `17B / 6S` |
| `0:00 UTC` | `0.0792` | `0.0792` | `0.0792` | `0.0793` | `0.0791` | 2,162,354.33 USD | 812,153.86 USD | 1,350,200.47 USD | -538,046.61 USD | `-24.88%` | `2B / 9S` |
| `5:00 UTC` | `0.0791` | `0.0791` | `0.0791` | `0.0792` | `0.0790` | 1,623,560.28 USD | 710,933.62 USD | 912,626.66 USD | -201,693.05 USD | `-12.42%` | `1B / 6S` |
| `0:00 UTC` | `0.0794` | `0.0794` | `0.0794` | `0.0795` | `0.0791` | 2,224,641.24 USD | 1,501,047.07 USD | 723,594.17 USD | 777,452.89 USD | `+34.95%` | `11B / 0S` |
| `5:00 UTC` | `0.0793` | `0.0793` | `0.0793` | `0.0795` | `0.0792` | 1,861,645.62 USD | 802,421.72 USD | 1,059,223.91 USD | -256,802.19 USD | `-13.79%` | `3B / 2S` |
| `0:00 UTC` | `0.0785` | `0.0784` | `0.0785` | `0.0793` | `0.0779` | 23,632,878.19 USD | 10,124,152.20 USD | 13,508,725.98 USD | -3,384,573.78 USD | `-14.32%` | `7B / 41S` |
| `5:00 UTC` | `0.0785` | `0.0785` | `0.0785` | `0.0786` | `0.0783` | 4,602,184.99 USD | 2,513,950.11 USD | 2,088,234.88 USD | 425,715.23 USD | `+9.25%` | `2B / 3S` |
| `0:00 UTC` | `0.0760` | `0.0766` | `0.0760` | `0.0786` | `0.0752` | 55,822,204.41 USD | 22,894,150.54 USD | 32,928,053.87 USD | -10,033,903.33 USD | `-17.97%` | `2B / 33S` |
| `5:00 UTC` | `0.0757` | `0.0754` | `0.0757` | `0.0762` | `0.0742` | 60,549,155.39 USD | 27,187,435.52 USD | 33,361,719.87 USD | -6,174,284.35 USD | `-10.20%` | `1B / 21S` |
| `0:00 UTC` | `0.0753` | `0.0754` | `0.0753` | `0.0757` | `0.0750` | 9,207,650.43 USD | 4,949,590.02 USD | 4,258,060.40 USD | 691,529.62 USD | `+7.51%` | `9B / 2S` |

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
| `5m` | -83,290.00 USD | 529,620.00 USD | **`ACCUMULATION`** |
| `15m` | 1,300,000.00 USD | -4,370,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -5,720,000.00 USD | -33,110,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -7,550,000.00 USD | -33,710,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -9,680,000.00 USD | -37,510,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -11,660,000.00 USD | -38,890,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -11,850,000.00 USD | -38,830,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -11,450,000.00 USD | -34,930,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,380,000.00 USD | -40,790,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -13,450,000.00 USD | -55,690,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -49,750,000.00 USD | -164,940,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -277,080,000.00 USD | -784,980,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-83.29K` | 15m=`+1.30M` | 1h=`-7.55M` | 24h=`-13.45M`
* Futures Capital Netflows: 5m=`+529.62K` | 15m=`-4.37M` | 1h=`-33.71M` | 24h=`-55.69M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0738` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0698` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0843`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0740` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0780` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0635`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0755`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
