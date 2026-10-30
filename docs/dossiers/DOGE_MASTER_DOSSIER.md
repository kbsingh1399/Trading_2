# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 09:13:07 IST` (`2026-10-30 03:43:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0746` | **Live Ask Quote**: `0.0767` | **Mid Price**: `0.0756`
- **Spread Points**: `21.00` | **Spread BPS**: `277.59 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0730` | VWAP Z-Score: `+1.95` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000726` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.58` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0749` | Lower -3.00σ Band: `0.0711`
  * Upper +2.51σ Band: `0.0745` | Lower -2.51σ Band: `0.0714`
  * Upper +2.01σ Band: `0.0742` | Lower -2.01σ Band: `0.0717`
  * Upper +2.00σ Band: `0.0742` | Lower -2.00σ Band: `0.0717`
  * Upper +1.28σ Band: `0.0738` | Lower -1.28σ Band: `0.0722`
  * Upper +1.00σ Band: `0.0736` | Lower -1.00σ Band: `0.0723`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0737` | EMA-20=`0.0740` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0753` (Slope: `+0.0000`) | EMA-100=`0.0762`
  * Institutional Anchors: EMA-144=`0.0766` | EMA-200=`0.0768` (Slope: `-0.5593`) | EMA-233=`0.0769`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0710` | Weekly High=`0.0803` | Weekly Low=`0.0710`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0757` (Distance: `-0.09%`)
  * Point of Control (POC) = `0.0749` (Distance: `+1.02%`)
  * Value Area Low (VAL) = `0.0731` (Distance: `+3.45%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0788` | Weekly POC=`0.0762` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0758` | Low=`0.0710`
  * London Session (08:00-16:00 UTC): High=`0.0760` | Low=`0.0753`
  * New York Session (13:00-21:00 UTC): High=`0.0761` | Low=`0.0752`
  * Initial Balance (First Hour): IB High=`0.0759` | IB Low=`0.0754`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0753` - `0.0760`
  * Optimal Trade Entry (OTE 0.705): `0.0758`
  * Structural Invalidation Anchor (0.786): `0.0763`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0749` | `0.0750` | `0.0748` | `0.0750` | `15,958,775` | 1,195,328.78 USD | 222,375.88 USD | `+18.60%` | -36,342,204.37 USD | `+0.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.0750` | `0.0752` | `0.0749` | `0.0750` | `32,630,142` | 2,449,522.05 USD | 833,697.22 USD | `+34.04%` | -35,508,507.15 USD | `+1.37` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.0750` | `0.0752` | `0.0750` | `0.0752` | `16,508,921` | 1,240,275.33 USD | 299,584.02 USD | `+24.15%` | -35,208,923.13 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0749` | `0.0752` | `0.0748` | `0.0752` | `92,161,761` | 6,915,504.04 USD | 902,399.44 USD | `+13.05%` | -36,205,185.25 USD | `+0.54` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.0752` | `0.0752` | `0.0748` | `0.0750` | `57,193,825` | 4,286,041.88 USD | -88,263.30 USD | `-2.06%` | -36,293,448.55 USD | `+0.18` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.0750` | `0.0752` | `0.0749` | `0.0752` | `49,139,063` | 3,689,797.37 USD | 1,133,281.24 USD | `+30.71%` | -35,160,167.31 USD | `+0.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0743` | `0.0746` | `0.0733` | `0.0740` | `386,101,231` | 28,593,595.00 USD | -713,201.79 USD | `-2.49%` | -37,137,890.46 USD | `+0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0740` | `0.0752` | `0.0736` | `0.0750` | `319,578,594` | 23,850,098.79 USD | 1,220,777.97 USD | `+5.12%` | -35,917,112.48 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.0750` | `0.0752` | `0.0749` | `0.0752` | `49,139,063` | 3,689,797.37 USD | 1,133,281.24 USD | `+30.71%` | -34,783,831.24 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -5,801,361.26 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -28,841,087.48 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0755` | `0.0722` | `0.0752` | `1,881,064,939` | 139,098,728.92 USD | -5,942,743.77 USD | `-4.27%` | -34,783,831.24 USD | `-0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -7,382,443.88 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -2,793,692.45 USD | `+1.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -5,801,361.26 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0752` | `3,701,409,962` | 282,061,435.08 USD | -23,039,726.22 USD | `-8.17%` | -28,841,087.48 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0752` | `0.0755` | `0.0722` | `0.0752` | `1,881,064,939` | 139,098,728.92 USD | -5,942,743.77 USD | `-4.27%` | -34,783,831.24 USD | `-0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.0756`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.0757` | `92400.0000` | 6,999.12 USD | 19,262.32 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0757` | `148560.0000` | 11,252.97 USD | 30,515.30 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0757` | `425572.0000` | 32,234.95 USD | 62,750.25 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `0.0757` | `17049.0000` | 1,291.33 USD | 64,041.57 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0757` | `451114.0000` | 34,167.37 USD | 98,208.95 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0757` | `79498.0000` | 6,020.86 USD | 104,229.81 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.0757` | `148585.0000` | 11,252.94 USD | 115,482.74 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0757` | `16893.0000` | 1,279.36 USD | 116,762.10 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0757` | `16858.0000` | 1,276.69 USD | 118,038.79 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0757` | `57071.0000` | 4,321.87 USD | 122,360.66 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `0.0757` | `73978.0000` | 5,602.13 USD | 127,962.80 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0757` | `3673.0000` | 278.14 USD | 128,240.93 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0757` | `19825.0000` | 1,501.23 USD | 129,742.16 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0757` | `205950.0000` | 15,595.15 USD | 145,337.32 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `0.0757` | `16875.0000` | 1,277.81 USD | 146,615.12 USD | `1 orders` | `-0.07%` | `-` |
| `ASK` | `0.0758` | `5584.0000` | 423.35 USD | 93,163.79 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `0.0758` | `50368.0000` | 3,818.50 USD | 92,740.44 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `45465.0000` | 3,446.75 USD | 88,921.94 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `16876.0000` | 1,279.35 USD | 85,475.20 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `21926.0000` | 1,662.17 USD | 84,195.85 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `143273.0000` | 10,860.95 USD | 82,533.68 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `3000.0000` | 227.41 USD | 71,672.73 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0758` | `36150.0000` | 2,740.31 USD | 71,445.31 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `16876.0000` | 1,279.23 USD | 68,705.00 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `16876.0000` | 1,279.20 USD | 67,425.76 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `5052.0000` | 382.94 USD | 66,146.56 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0758` | `103354.0000` | 7,833.82 USD | 65,763.62 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `67200.0000` | 5,093.42 USD | 57,929.80 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `67200.0000` | 5,093.36 USD | 52,836.38 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `210498.0000` | 15,954.27 USD | 47,743.02 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `67060.0000` | 5,082.61 USD | 31,788.75 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `92269.0000` | 6,993.16 USD | 26,706.14 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `69869.0000` | 5,295.37 USD | 19,712.98 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `0.0758` | `75791.0000` | 5,744.12 USD | 14,417.61 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `0.0758` | `114444.0000` | 8,673.48 USD | 8,673.48 USD | `7 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `0.0758` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0758` | `107545.0000` | 8,148.47 USD | 8,148.47 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0758` | `16892.0000` | 1,279.79 USD | 9,428.26 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0758` | `16892.0000` | 1,279.69 USD | 10,707.95 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `3639.0000` | 275.68 USD | 10,983.62 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0758` | `16892.0000` | 1,279.59 USD | 12,263.21 USD | `1 orders` | `-0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:07:15 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `302` | `0xb83d...6e36` | `SHORT` | 7,776,044.69 USD | `102,645,925.00` | `0.0946` | `0.0758` | `1.34` | 1,931,296.96 USD | `+24.84%` | `3X Cross` |
| `308` | `0xc63a...a3cd` | `LONG` | 7,574,900.00 USD | `100,000,000.00` | `0.0856` | `0.0758` | `0.000000` | -989,921.96 USD | `-13.07%` | `10X Cross` |
| `312` | `0x610b...b613` | `LONG` | 7,472,501.62 USD | `98,666,424.00` | `0.0872` | `0.0758` | `0.0607` | -1,127,680.28 USD | `-15.09%` | `5X Cross` |
| `597` | `0x5b5d...c060` | `SHORT` | 3,748,674.07 USD | `49,478,955.00` | `0.0946` | `0.0758` | `3.28` | 932,842.54 USD | `+24.88%` | `3X Cross` |
| `625` | `0xca49...53c8` | `SHORT` | 3,525,791.83 USD | `46,542,649.00` | `0.0929` | `0.0758` | `0.3963` | 800,252.85 USD | `+22.70%` | `10X Cross` |
| `641` | `0x45d2...4029` | `SHORT` | 3,442,836.54 USD | `45,426,000.00` | `0.0954` | `0.0758` | `0.9784` | 892,792.68 USD | `+25.93%` | `10X Cross` |
| `699` | `0xecb6...2b00` | `SHORT` | 3,180,861.52 USD | `41,954,463.00` | `0.0789` | `0.0758` | `0.7175` | 131,340.03 USD | `+4.13%` | `10X Cross` |
| `1185` | `0x458d...ab3b` | `LONG` | 1,854,131.51 USD | `24,454,063.00` | `0.1002` | `0.0758` | `0.0714` | -596,790.39 USD | `-32.19%` | `3X Isolated` |
| `1198` | `0xeadc...9d55` | `LONG` | 1,843,772.62 USD | `24,317,440.00` | `0.0926` | `0.0758` | `0.000000` | -407,821.96 USD | `-22.12%` | `10X Cross` |
| `1328` | `0xf48f...10fe` | `LONG` | 1,623,976.87 USD | `21,424,497.00` | `0.0968` | `0.0758` | `0.0457` | -450,327.73 USD | `-27.73%` | `4X Cross` |
| `1516` | `0x9946...0852` | `SHORT` | 1,420,900.00 USD | `18,738,955.00` | `0.0871` | `0.0758` | `0.1629` | 210,619.00 USD | `+14.82%` | `10X Cross` |
| `1541` | `0x9aa5...58af` | `SHORT` | 1,398,611.65 USD | `18,444,771.00` | `0.0907` | `0.0758` | `0.5636` | 273,747.97 USD | `+19.57%` | `10X Cross` |
| `1561` | `0xcac1...26b3` | `SHORT` | 1,374,014.09 USD | `18,126,835.00` | `0.0943` | `0.0758` | `0.5520` | 335,445.11 USD | `+24.41%` | `10X Cross` |
| `1592` | `0x0d6a...ca57` | `LONG` | 1,335,115.83 USD | `17,626,455.00` | `0.0875` | `0.0758` | `0.0626` | -206,989.12 USD | `-15.50%` | `3X Isolated` |
| `1654` | `0x4808...a82c` | `LONG` | 1,275,926.63 USD | `16,828,143.00` | `0.0883` | `0.0758` | `0.0631` | -210,546.35 USD | `-16.50%` | `3X Cross` |
| `1795` | `0x31ef...f715` | `LONG` | 1,154,761.56 USD | `15,230,102.00` | `0.0936` | `0.0758` | `0.0668` | -270,934.37 USD | `-23.46%` | `3X Isolated` |
| `1812` | `0xbfc7...80b4` | `SHORT` | 1,138,035.36 USD | `15,020,000.00` | `0.0920` | `0.0758` | `0.1888` | 244,363.93 USD | `+21.47%` | `10X Cross` |
| `1899` | `0x7cee...fc93` | `SHORT` | 1,062,459.10 USD | `14,013,468.00` | `0.0863` | `0.0758` | `0.2693` | 146,418.26 USD | `+13.78%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0800` | 8,202.51 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 8.20K USD at 0.0800 USD [API] | `2026-10-28 22:02:56` |
| `ANNOUNCEMENT` | `INFO` | `0.0801` | 12,172.83 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 12.17K USD at 0.0801 USD [API] | `2026-10-28 22:02:23` |
| `ANNOUNCEMENT` | `INFO` | `0.0799` | 8,348.29 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 8.35K USD at 0.0799 USD [API] | `2026-10-28 22:51:05` |
| `ANNOUNCEMENT` | `INFO` | `0.0798` | 5,249.24 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 5.25K USD at 0.0798 USD [API] | `2026-10-28 23:08:15` |
| `ANNOUNCEMENT` | `INFO` | `0.0799` | 7,598.95 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.60K USD at 0.0799 USD [API] | `2026-10-29 00:28:51` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.07%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.07%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.07%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.0725` (Vol: 1,600,000.00 USD, Dist: `--4.07%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0155` | 1,390.00 USD | 16,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0185` | 1,090.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0193` | 1,860.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0194` | 1,170.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0197` | 628.80 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0199` | 4,990.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0208` | 810.27 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0214` | 10,680.00 USD | 16,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0215` | 18,970.00 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0216` | 541.25 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0243` | 225.11 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0244` | 369.37 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0246` | 152.98 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0256` | 4,070.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0262` | 1,970.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0276` | 3,070.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0282` | 563.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0284` | 152.04 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0294` | 463.58 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0307` | 27,480.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0309` | 684.83 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0321` | 3,510.00 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0333` | 573.99 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0336` | 393.23 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0340` | 780.85 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0350` | 13,620.00 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 1,140.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0352` | 421.91 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0355` | 6,680.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0360` | 5,520.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0367` | 221.77 USD | 16,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0367` | 4,940.00 USD | 16,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0369` | 1,250.00 USD | 16,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 1,600.00 USD | 16,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 36,740.00 USD | 16,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0389` | 546.74 USD | 16,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 2,370.00 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0394` | 211.02 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 178.57 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0399` | 103.31 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0406` | 75,870.00 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 1,910.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 267.52 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 455.06 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 883.34 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 8,830.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 10,120.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 4,960.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 216,270.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 13,010.00 USD | 16,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0449` | 810.81 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0452` | 5,240.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,370.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 6,480.00 USD | 16,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0459` | 689.25 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0467` | 451.75 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0469` | 4,700.00 USD | 16,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 3,180.00 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 925.74 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0479` | 71,390.00 USD | 16,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 56,440.00 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,330.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 42,370.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 104,040.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 267.52 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 52,340.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0502` | 120.06 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 10,280.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 1,360.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 1,090,000.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 2,680.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 308.55 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0517` | 1,190.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 7,510.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 5,350.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 315,250.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 2,230.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 10,260.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 182,740.00 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 12,030.00 USD | 14,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 8,420.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 1,890.00 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 1,590.00 USD | 14,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 14,430.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 3,290.00 USD | 14,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 28,620.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 2,840.00 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 1,420.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 188.07 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0551` | 1,760.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 6,290.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 8,410.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 38,870.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 1,820.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 178.61 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 749.76 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 567.50 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 315.67 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 814.04 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 359.24 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,960.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 14,210.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 6,430.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 441.75 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 582.50 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 347,440.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 19,490.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 5,280.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 305.15 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 546.26 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,520.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,940.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0597` | 25,990.00 USD | 13,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 4,560.00 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 1,130.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 7,210.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 830.97 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 548.46 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 622.63 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,220.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 717.73 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 6,160.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 629.72 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,890.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 11,100.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 6,090,000.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0619` | 17,440.00 USD | 7,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 345.86 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 43,420.00 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 870.40 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 8,460.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 2,430.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,310,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 3,030.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,660.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 905.97 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 4,770.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 5,600.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 2,100.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 150.01 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 17,700.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,390.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 76,280.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 27,180.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 631.94 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 162,920.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 8,800.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 4,720.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 7,790.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 9,600.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0660` | 2,510.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 2,280.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 17,410.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,270.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 7,620.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,150,000.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,180.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 9,190.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 9,220.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 15,370.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 1,780.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 11,450.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 14,030.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 4,290.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 11,770,000.00 USD | 11,770,000.00 USD | 3,200.00 USD | 39,890.00 USD | 58,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 34,560.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0679` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0679` | 16,630.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 11,640,000.00 USD | 11,640,000.00 USD | 4,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0681` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 134,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0682` | 117.29 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 11,500,000.00 USD | 11,500,000.00 USD | 2,550.00 USD | 33,950.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0683` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 20,340.00 USD | 723.57 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 49,510.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0684` | 11,430,000.00 USD | 11,430,000.00 USD | 24,150.00 USD | 15,070.00 USD | 584.27 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 80,430.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0685` | 11,390,000.00 USD | 11,390,000.00 USD | 41,510.00 USD | 12,720.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0685` | 13,120.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0686` | 11,320,000.00 USD | 11,320,000.00 USD | 41,080.00 USD | 1,410.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0687` | 595.81 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0687` | 11,260,000.00 USD | 11,260,000.00 USD | 3,150.00 USD | 16,550.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 16,210.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 870.75 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 10,310.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0691` | 11,200,000.00 USD | 11,200,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0692` | 13,510.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 9,970.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,020.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,980.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0695` | 11,200,000.00 USD | 11,200,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0697` | 11,200,000.00 USD | 11,200,000.00 USD | 14,390.00 USD | 24,590.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 4,720.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 11,140,000.00 USD | 11,140,000.00 USD | 25,600.00 USD | 13,930.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 38,610.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0699` | 11,080,000.00 USD | 11,080,000.00 USD | 53,800.00 USD | 45,460.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 10,950,000.00 USD | 10,950,000.00 USD | 88,520.00 USD | 32,810.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 9,620.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0701` | 10,810,000.00 USD | 10,810,000.00 USD | 35,400.00 USD | 18,030.00 USD | 29,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0702` | 8,310.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 10,720,000.00 USD | 10,720,000.00 USD | 78,740.00 USD | 36,780.00 USD | 164.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 1,070.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0703` | 10,610,000.00 USD | 10,610,000.00 USD | 87,540.00 USD | 31,470.00 USD | 41,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 4,360.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 10,450,000.00 USD | 10,450,000.00 USD | 44,920.00 USD | 24,150.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0705` | 10,360,000.00 USD | 10,360,000.00 USD | 41,490.00 USD | 24,910.00 USD | 32,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0706` | 10,260,000.00 USD | 10,260,000.00 USD | 36,930.00 USD | 29,080.00 USD | 26,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 423.90 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0707` | 10,170,000.00 USD | 10,170,000.00 USD | 54,240.00 USD | 21,680.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 536.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 10,070,000.00 USD | 10,070,000.00 USD | 25,410.00 USD | 16,310.00 USD | 27,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0708` | 94,010.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0709` | 10,000,000.00 USD | 10,000,000.00 USD | 36,740.00 USD | 37,120.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0709` | 821.60 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 9,910,000.00 USD | 9,910,000.00 USD | 21,430.00 USD | 9,300.00 USD | 34,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 9,660.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 9,840,000.00 USD | 9,840,000.00 USD | 27,890.00 USD | 8,560.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 2,160.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 9,770,000.00 USD | 9,770,000.00 USD | 56,550.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 802.06 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 9,700,000.00 USD | 9,700,000.00 USD | 35,120.00 USD | 58,130.00 USD | 67,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 9,540,000.00 USD | 9,540,000.00 USD | 42,610.00 USD | 42,090.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 213.78 USD | 391,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 9,440,000.00 USD | 9,440,000.00 USD | 34,440.00 USD | 8,830.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 391,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 9,360,000.00 USD | 9,360,000.00 USD | 24,840.00 USD | 31,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,170.00 USD | 383,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 9,300,000.00 USD | 9,300,000.00 USD | 10,910.00 USD | 7,710.00 USD | 21,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 22,270.00 USD | 382,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 9,260,000.00 USD | 9,260,000.00 USD | 67,080.00 USD | 31,390.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 1,070.00 USD | 360,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 9,130,000.00 USD | 9,130,000.00 USD | 10,150.00 USD | 0.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 1,900.00 USD | 359,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 9,120,000.00 USD | 9,120,000.00 USD | 31,160.00 USD | 29,440.00 USD | 32,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 12,160.00 USD | 357,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 9,030,000.00 USD | 9,030,000.00 USD | 136,510.00 USD | 76,220.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 22,360.00 USD | 345,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 8,800,000.00 USD | 8,800,000.00 USD | 43,930.00 USD | 15,630.00 USD | 22,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 322,050.00 USD | 322,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 8,720,000.00 USD | 8,720,000.00 USD | 54,790.00 USD | 162,040.00 USD | 153,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 626.77 USD | 626.77 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 8,350,000.00 USD | 8,350,000.00 USD | 27,830.00 USD | 87,980.00 USD | 92,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0725` | 8,140,000.00 USD | 8,140,000.00 USD | 54,140.00 USD | 22,980.00 USD | 23,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0726` | 8,040,000.00 USD | 8,040,000.00 USD | 51,960.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0727` | 7,980,000.00 USD | 7,980,000.00 USD | 168,660.00 USD | 0.00 USD | 345,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0728` | 7,470,000.00 USD | 7,470,000.00 USD | 66,510.00 USD | 85,670.00 USD | 75,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0729` | 7,240,000.00 USD | 7,240,000.00 USD | 19,510.00 USD | 82,260.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0730` | 7,110,000.00 USD | 7,110,000.00 USD | 112,200.00 USD | 54,520.00 USD | 1,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0731` | 6,940,000.00 USD | 6,940,000.00 USD | 152,870.00 USD | 49,300.00 USD | 43,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0732` | 6,700,000.00 USD | 6,700,000.00 USD | 154,930.00 USD | 60,240.00 USD | 81,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0733` | 6,400,000.00 USD | 6,400,000.00 USD | 15,550.00 USD | 0.00 USD | 71,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 6,310,000.00 USD | 6,310,000.00 USD | 43,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0735` | 6,270,000.00 USD | 6,270,000.00 USD | 33,390.00 USD | 31,100.00 USD | 299.76 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0736` | 6,200,000.00 USD | 6,200,000.00 USD | 234,720.00 USD | 123,630.00 USD | 1.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0737` | 5,850,000.00 USD | 5,850,000.00 USD | 51,890.00 USD | 42,510.00 USD | 636.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0738` | 5,750,000.00 USD | 5,750,000.00 USD | 31,820.00 USD | 199,460.00 USD | 284,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0739` | 5,230,000.00 USD | 5,230,000.00 USD | 33,680.00 USD | 161,430.00 USD | 78,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0740` | 4,960,000.00 USD | 4,960,000.00 USD | 33,740.00 USD | 0.00 USD | 267.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0741` | 4,930,000.00 USD | 4,930,000.00 USD | 36,980.00 USD | 0.00 USD | 560.08 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0742` | 4,890,000.00 USD | 4,890,000.00 USD | 286,340.00 USD | 0.00 USD | 684,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0743` | 3,920,000.00 USD | 3,920,000.00 USD | 118,640.00 USD | 234,470.00 USD | 190,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0744` | 3,380,000.00 USD | 3,380,000.00 USD | 19,880.00 USD | 187,400.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0745` | 3,110,000.00 USD | 3,110,000.00 USD | 199,850.00 USD | 166,270.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0746` | 2,720,000.00 USD | 2,720,000.00 USD | 371,240.00 USD | 274,020.00 USD | 211,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0747` | 1,860,000.00 USD | 1,860,000.00 USD | 466,980.00 USD | 159,330.00 USD | 131,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0748` | 1,100,000.00 USD | 1,100,000.00 USD | 130,290.00 USD | 143,100.00 USD | 194,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 635,760.00 USD | 635,760.00 USD | 203,330.00 USD | 0.00 USD | 149,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 282,960.00 USD | 282,960.00 USD | 69,890.00 USD | 0.00 USD | 120,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0751` | 92,290.00 USD | 92,290.00 USD | 0.00 USD | 6,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0753` | 85,440.00 USD | 85,440.00 USD | 0.00 USD | 85,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0760` | 424.91 USD | 424.91 USD | 0.00 USD | 0.00 USD | 424.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 412.85 USD | 412.85 USD | 0.00 USD | 0.00 USD | 412.85 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0761` | 825.70 USD | 825.70 USD | 0.00 USD | 0.00 USD | 412.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0763` | 14,210.00 USD | 14,210.00 USD | 0.00 USD | 13,220.00 USD | 168.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0764` | 340,180.00 USD | 340,180.00 USD | 0.00 USD | 325,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0765` | 598,420.00 USD | 598,420.00 USD | 0.00 USD | 257,590.00 USD | 656.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 1,710,000.00 USD | 1,710,000.00 USD | 745,930.00 USD | 360,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0767` | 2,060,000.00 USD | 2,060,000.00 USD | 169,980.00 USD | 188,260.00 USD | 502.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 2,930,000.00 USD | 2,930,000.00 USD | 351,760.00 USD | 0.00 USD | 514,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0769` | 3,600,000.00 USD | 3,600,000.00 USD | 181,440.00 USD | 341,350.00 USD | 148,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 4,220,000.00 USD | 4,220,000.00 USD | 272,760.00 USD | 93,300.00 USD | 253,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0771` | 4,880,000.00 USD | 4,880,000.00 USD | 216,410.00 USD | 232,340.00 USD | 212,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 5,850,000.00 USD | 5,850,000.00 USD | 286,340.00 USD | 0.00 USD | 685,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0773` | 6,240,000.00 USD | 6,240,000.00 USD | 65,160.00 USD | 169,730.00 USD | 149,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 164,510.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 3,830.00 USD | 3,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0775` | 6,690,000.00 USD | 6,690,000.00 USD | 155,740.00 USD | 109,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0775` | 240.95 USD | 4,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0776` | 7,070,000.00 USD | 7,070,000.00 USD | 190,100.00 USD | 110,600.00 USD | 86,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0777` | 7,620,000.00 USD | 7,620,000.00 USD | 205,390.00 USD | 264,690.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 8,140,000.00 USD | 8,140,000.00 USD | 16,790.00 USD | 202,930.00 USD | 295,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0779` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 85,950.00 USD | 140,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 8,470,000.00 USD | 8,470,000.00 USD | 69,890.00 USD | 31,980.00 USD | 253.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0781` | 8,650,000.00 USD | 8,650,000.00 USD | 113,060.00 USD | 68,670.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 8,660,000.00 USD | 8,660,000.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0783` | 9,000,000.00 USD | 9,000,000.00 USD | 8,010.00 USD | 184,740.00 USD | 145,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0784` | 723.88 USD | 4,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0784` | 9,390,000.00 USD | 9,390,000.00 USD | 265,800.00 USD | 86,850.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0785` | 9,740,000.00 USD | 9,740,000.00 USD | 177,210.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0786` | 10,280,000.00 USD | 10,280,000.00 USD | 191,180.00 USD | 117,040.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0787` | 11,230,000.00 USD | 11,230,000.00 USD | 298,820.00 USD | 307,550.00 USD | 344,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0788` | 113.24 USD | 4,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0788` | 11,560,000.00 USD | 11,560,000.00 USD | 75,490.00 USD | 181,170.00 USD | 75,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0789` | 12,090,000.00 USD | 12,090,000.00 USD | 234,900.00 USD | 192,150.00 USD | 96,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 12,250,000.00 USD | 12,250,000.00 USD | 102,120.00 USD | 57,780.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0791` | 12,590,000.00 USD | 12,590,000.00 USD | 152,950.00 USD | 95,070.00 USD | 95,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0792` | 12,750,000.00 USD | 12,750,000.00 USD | 104,950.00 USD | 18,870.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0793` | 423.67 USD | 5,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0794` | 12,930,000.00 USD | 12,930,000.00 USD | 92,580.00 USD | 41,370.00 USD | 47,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0795` | 13,010,000.00 USD | 13,010,000.00 USD | 10,150.00 USD | 0.00 USD | 73,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 13,200,000.00 USD | 13,200,000.00 USD | 174,010.00 USD | 0.00 USD | 16,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0796` | 309,520.00 USD | 314,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0797` | 13,730,000.00 USD | 13,730,000.00 USD | 191,110.00 USD | 89,760.00 USD | 242,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 13,950,000.00 USD | 13,950,000.00 USD | 51,440.00 USD | 164,620.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 14,520,000.00 USD | 14,520,000.00 USD | 191,450.00 USD | 193,600.00 USD | 194,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 14,630,000.00 USD | 14,630,000.00 USD | 4,510.00 USD | 5,610.00 USD | 94,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0800` | 113.67 USD | 314,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0801` | 14,640,000.00 USD | 14,640,000.00 USD | 6,300.00 USD | 0.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0802` | 14,650,000.00 USD | 14,650,000.00 USD | 7,730.00 USD | 1,770.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0803` | 14,700,000.00 USD | 14,700,000.00 USD | 9,970.00 USD | 0.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 14,720,000.00 USD | 14,720,000.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0805` | 14,860,000.00 USD | 14,860,000.00 USD | 56,220.00 USD | 37,230.00 USD | 41,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0805` | 435.61 USD | 315,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0806` | 15,120,000.00 USD | 15,120,000.00 USD | 27,790.00 USD | 21,040.00 USD | 215,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 15,590,000.00 USD | 15,590,000.00 USD | 221,690.00 USD | 208,070.00 USD | 41,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 16,670,000.00 USD | 16,670,000.00 USD | 419,500.00 USD | 131,030.00 USD | 523,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 17,490,000.00 USD | 17,490,000.00 USD | 477,790.00 USD | 336,610.00 USD | 12,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 18,100,000.00 USD | 18,100,000.00 USD | 293,220.00 USD | 180,540.00 USD | 133,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 18,430,000.00 USD | 18,430,000.00 USD | 83,280.00 USD | 241,410.00 USD | 875.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 18,790,000.00 USD | 18,790,000.00 USD | 144,600.00 USD | 99,490.00 USD | 120,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 19,070,000.00 USD | 19,070,000.00 USD | 49,290.00 USD | 23,210.00 USD | 208,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 19,470,000.00 USD | 19,470,000.00 USD | 29,840.00 USD | 79,960.00 USD | 292,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 19,820,000.00 USD | 19,820,000.00 USD | 150,190.00 USD | 72,710.00 USD | 124,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 20,540,000.00 USD | 20,540,000.00 USD | 348,980.00 USD | 194,790.00 USD | 177,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 21,100,000.00 USD | 21,100,000.00 USD | 301,230.00 USD | 127,050.00 USD | 130,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0818` | 21,840,000.00 USD | 21,840,000.00 USD | 269,340.00 USD | 161,260.00 USD | 308,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0819` | 380.85 USD | 315,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0819` | 22,460,000.00 USD | 22,460,000.00 USD | 174,640.00 USD | 312,480.00 USD | 128,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 23,140,000.00 USD | 23,140,000.00 USD | 136,010.00 USD | 202,840.00 USD | 344,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 23,600,000.00 USD | 23,600,000.00 USD | 210,590.00 USD | 79,630.00 USD | 170,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 24,190,000.00 USD | 24,190,000.00 USD | 262,170.00 USD | 169,200.00 USD | 156,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 24,540,000.00 USD | 24,540,000.00 USD | 270,850.00 USD | 75,420.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 25,120,000.00 USD | 25,120,000.00 USD | 151,910.00 USD | 226,510.00 USD | 198,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 25,400,000.00 USD | 25,400,000.00 USD | 127,790.00 USD | 122,020.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 25,820,000.00 USD | 25,820,000.00 USD | 150,570.00 USD | 84,820.00 USD | 190,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 25,920,000.00 USD | 25,920,000.00 USD | 49,040.00 USD | 48,230.00 USD | 399.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 26,270,000.00 USD | 26,270,000.00 USD | 216,200.00 USD | 75,940.00 USD | 58,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 26,640,000.00 USD | 26,640,000.00 USD | 182,720.00 USD | 111,290.00 USD | 72,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 26,960,000.00 USD | 26,960,000.00 USD | 140,600.00 USD | 84,690.00 USD | 98,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 27,030,000.00 USD | 27,030,000.00 USD | 39,850.00 USD | 0.00 USD | 24,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,580.00 USD | 319,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 27,340,000.00 USD | 27,340,000.00 USD | 171,130.00 USD | 66,230.00 USD | 80,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0833` | 500.17 USD | 319,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0833` | 27,680,000.00 USD | 27,680,000.00 USD | 119,590.00 USD | 55,260.00 USD | 165,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 28,030,000.00 USD | 28,030,000.00 USD | 127,020.00 USD | 94,190.00 USD | 126,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 28,380,000.00 USD | 28,380,000.00 USD | 104,680.00 USD | 176,580.00 USD | 65,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 28,640,000.00 USD | 28,640,000.00 USD | 48,890.00 USD | 63,220.00 USD | 144,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 320,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 28,850,000.00 USD | 28,850,000.00 USD | 129,000.00 USD | 30,430.00 USD | 51,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 321,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 29,120,000.00 USD | 29,120,000.00 USD | 168,220.00 USD | 70,030.00 USD | 38,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 29,210,000.00 USD | 29,210,000.00 USD | 52,570.00 USD | 16,550.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0840` | 29,270,000.00 USD | 29,270,000.00 USD | 13,720.00 USD | 15,480.00 USD | 28,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0841` | 29,290,000.00 USD | 29,290,000.00 USD | 23,380.00 USD | 2,010.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0842` | 29,360,000.00 USD | 29,360,000.00 USD | 22,710.00 USD | 0.00 USD | 46,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0843` | 29,400,000.00 USD | 29,400,000.00 USD | 33,600.00 USD | 0.00 USD | 634.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 29,470,000.00 USD | 29,470,000.00 USD | 79,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 29,490,000.00 USD | 29,490,000.00 USD | 18,230.00 USD | 0.00 USD | 264.53 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0846` | 110,220.00 USD | 431,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0846` | 29,580,000.00 USD | 29,580,000.00 USD | 72,340.00 USD | 16,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 128.58 USD | 432,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0847` | 29,590,000.00 USD | 29,590,000.00 USD | 11,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 1,150.00 USD | 433,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 433,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0859` | 4,450.00 USD | 437,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0871` | 138.58 USD | 437,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0876` | 127.82 USD | 438,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 438,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 438,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 439,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 439,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0905` | 6,760.00 USD | 446,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 1,310.00 USD | 447,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 4,940.00 USD | 452,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 452,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0931` | 805.37 USD | 453,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0944` | 39,700.00 USD | 493,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0946` | 4,260.00 USD | 497,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 24,460.00 USD | 522,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0954` | 194.24 USD | 522,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0955` | 47,770.00 USD | 570,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0959` | 1,160.00 USD | 571,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 571,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0974` | 121.23 USD | 571,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0979` | 952.67 USD | 572,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 573,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 580,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 583,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 584,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1047` | 6,300.00 USD | 590,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 596,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1076` | 616.19 USD | 597,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 600,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1095` | 1,760.00 USD | 602,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 602,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 602,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1142` | 154.22 USD | 602,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1158` | 131.49 USD | 603,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 603,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 604,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1277` | 921.51 USD | 604,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1291` | 124.63 USD | 605,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 605,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1300` | 44,510.00 USD | 649,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 651,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 651,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 652,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1351` | 34,920.00 USD | 687,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1371` | 6,220.00 USD | 693,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1383` | 22,420.00 USD | 715,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 100.35 USD | 715,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 716,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1419` | 989.83 USD | 717,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1426` | 2,000.00 USD | 719,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 721,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1436` | 4,010.00 USD | 725,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1441` | 196.63 USD | 725,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 727,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1472` | 6,420.00 USD | 733,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,260.00 USD | 741,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1482` | 23,820.00 USD | 765,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1492` | 1,980.00 USD | 767,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0155` | 16,870,000.00 USD | 0.00 USD | 1,390.00 USD | `-79.25%` | `89,145.00` |
| `Live` | `Long` | `0.0160` | 16,860,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.58%` | `244,573.00` |
| `Live` | `Long` | `0.0164` | 16,860,000.00 USD | 0.00 USD | 407.02 USD | `-78.05%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,860,000.00 USD | 0.00 USD | 5,290.00 USD | `-77.91%` | `319,394.00` |
| `Live` | `Long` | `0.0185` | 16,850,000.00 USD | 0.00 USD | 1,090.00 USD | `-75.38%` | `59,317.00` |
| `Live` | `Long` | `0.0193` | 16,850,000.00 USD | 0.00 USD | 1,860.00 USD | `-74.18%` | `95,954.00` |
| `Live` | `Long` | `0.0194` | 16,850,000.00 USD | 0.00 USD | 1,170.00 USD | `-74.04%` | `60,000.00` |
| `Live` | `Long` | `0.0197` | 16,850,000.00 USD | 0.00 USD | 628.80 USD | `-73.78%` | `32,000.00` |
| `Live` | `Long` | `0.0199` | 16,850,000.00 USD | 0.00 USD | 4,990.00 USD | `-73.38%` | `250,000.00` |
| `Live` | `Long` | `0.0208` | 16,850,000.00 USD | 0.00 USD | 810.27 USD | `-72.31%` | `39,049.00` |
| `Live` | `Long` | `0.0214` | 16,840,000.00 USD | 0.00 USD | 10,680.00 USD | `-71.51%` | `500,000.00` |
| `Live` | `Long` | `0.0215` | 16,830,000.00 USD | 0.00 USD | 18,970.00 USD | `-71.24%` | `880,408.00` |
| `Live` | `Long` | `0.0216` | 16,810,000.00 USD | 0.00 USD | 541.25 USD | `-71.11%` | `25,000.00` |
| `Live` | `Long` | `0.0243` | 16,810,000.00 USD | 0.00 USD | 225.11 USD | `-67.64%` | `9,283.00` |
| `Live` | `Long` | `0.0244` | 16,810,000.00 USD | 0.00 USD | 369.37 USD | `-67.50%` | `15,169.00` |
| `Live` | `Long` | `0.0246` | 16,810,000.00 USD | 0.00 USD | 152.98 USD | `-67.10%` | `6,206.00` |
| `Live` | `Long` | `0.0256` | 16,810,000.00 USD | 0.00 USD | 4,070.00 USD | `-65.77%` | `158,606.00` |
| `Live` | `Long` | `0.0262` | 16,810,000.00 USD | 0.00 USD | 1,970.00 USD | `-64.97%` | `75,012.00` |
| `Live` | `Long` | `0.0276` | 16,810,000.00 USD | 0.00 USD | 3,070.00 USD | `-63.23%` | `111,254.00` |
| `Live` | `Long` | `0.0279` | 16,800,000.00 USD | 0.00 USD | 1,730.00 USD | `-62.70%` | `61,775.00` |
| `Live` | `Long` | `0.0282` | 16,800,000.00 USD | 0.00 USD | 563.00 USD | `-62.43%` | `20,000.00` |
| `Live` | `Long` | `0.0284` | 16,800,000.00 USD | 0.00 USD | 152.04 USD | `-62.03%` | `5,344.00` |
| `Live` | `Long` | `0.0294` | 16,800,000.00 USD | 0.00 USD | 463.58 USD | `-60.83%` | `15,795.00` |
| `Live` | `Long` | `0.0306` | 16,800,000.00 USD | 0.00 USD | 137.41 USD | `-59.23%` | `4,498.00` |
| `Live` | `Long` | `0.0307` | 16,800,000.00 USD | 0.00 USD | 27,480.00 USD | `-58.96%` | `893,720.00` |
| `Live` | `Long` | `0.0309` | 16,770,000.00 USD | 0.00 USD | 684.83 USD | `-58.70%` | `22,127.00` |
| `Live` | `Long` | `0.0321` | 16,770,000.00 USD | 0.00 USD | 3,510.00 USD | `-57.09%` | `109,191.00` |
| `Live` | `Long` | `0.0333` | 16,770,000.00 USD | 0.00 USD | 573.99 USD | `-55.63%` | `17,263.00` |
| `Live` | `Long` | `0.0336` | 16,770,000.00 USD | 0.00 USD | 393.23 USD | `-55.09%` | `11,686.00` |
| `Live` | `Long` | `0.0340` | 16,770,000.00 USD | 0.00 USD | 780.85 USD | `-54.69%` | `23,000.00` |
| `Live` | `Long` | `0.0350` | 16,770,000.00 USD | 0.00 USD | 13,620.00 USD | `-53.36%` | `389,633.00` |
| `Live` | `Long` | `0.0352` | 16,750,000.00 USD | 0.00 USD | 1,140.00 USD | `-53.09%` | `32,298.00` |
| `Live` | `Long` | `0.0352` | 16,750,000.00 USD | 0.00 USD | 421.91 USD | `-52.96%` | `11,969.00` |
| `Live` | `Long` | `0.0355` | 16,750,000.00 USD | 0.00 USD | 6,680.00 USD | `-52.56%` | `187,979.00` |
| `Live` | `Long` | `0.0358` | 16,750,000.00 USD | 0.00 USD | 214.53 USD | `-52.16%` | `5,984.00` |
| `Live` | `Long` | `0.0360` | 16,750,000.00 USD | 0.00 USD | 5,520.00 USD | `-51.89%` | `153,201.00` |
| `Live` | `Long` | `0.0367` | 16,740,000.00 USD | 0.00 USD | 221.77 USD | `-51.09%` | `6,051.00` |
| `Live` | `Long` | `0.0367` | 16,740,000.00 USD | 0.00 USD | 4,940.00 USD | `-50.95%` | `134,443.00` |
| `Live` | `Long` | `0.0369` | 16,730,000.00 USD | 0.00 USD | 1,250.00 USD | `-50.82%` | `33,816.00` |
| `Live` | `Long` | `0.0381` | 16,730,000.00 USD | 0.00 USD | 1,600.00 USD | `-49.22%` | `41,929.00` |
| `Live` | `Long` | `0.0386` | 16,730,000.00 USD | 0.00 USD | 36,740.00 USD | `-48.55%` | `953,158.00` |
| `Live` | `Long` | `0.0389` | 16,700,000.00 USD | 0.00 USD | 546.74 USD | `-48.02%` | `14,037.00` |
| `Live` | `Long` | `0.0393` | 16,690,000.00 USD | 0.00 USD | 2,370.00 USD | `-47.62%` | `60,333.00` |
| `Live` | `Long` | `0.0394` | 16,690,000.00 USD | 0.00 USD | 211.02 USD | `-47.35%` | `5,349.00` |
| `Live` | `Long` | `0.0396` | 16,690,000.00 USD | 0.00 USD | 178.57 USD | `-47.22%` | `4,515.00` |
| `Live` | `Long` | `0.0399` | 16,690,000.00 USD | 0.00 USD | 103.31 USD | `-46.68%` | `2,586.00` |
| `Live` | `Long` | `0.0404` | 16,690,000.00 USD | 0.00 USD | 115.12 USD | `-46.02%` | `2,846.00` |
| `Live` | `Long` | `0.0406` | 16,690,000.00 USD | 0.00 USD | 75,870.00 USD | `-45.75%` | `1,866,299.00` |
| `Live` | `Long` | `0.0408` | 16,620,000.00 USD | 0.00 USD | 1,910.00 USD | `-45.62%` | `46,942.00` |
| `Live` | `Long` | `0.0415` | 16,610,000.00 USD | 0.00 USD | 1,030.00 USD | `-44.55%` | `24,809.00` |
| `Live` | `Long` | `0.0420` | 16,610,000.00 USD | 0.00 USD | 266.05 USD | `-44.02%` | `6,342.00` |
| `Live` | `Long` | `0.0423` | 16,610,000.00 USD | 0.00 USD | 1,670.00 USD | `-43.61%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,610,000.00 USD | 0.00 USD | 267.52 USD | `-43.48%` | `6,317.00` |
| `Live` | `Long` | `0.0425` | 16,610,000.00 USD | 0.00 USD | 455.06 USD | `-43.35%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,610,000.00 USD | 0.00 USD | 883.34 USD | `-43.21%` | `20,760.00` |
| `Live` | `Long` | `0.0427` | 16,610,000.00 USD | 0.00 USD | 8,830.00 USD | `-43.08%` | `207,066.00` |
| `Live` | `Long` | `0.0430` | 16,600,000.00 USD | 0.00 USD | 859.00 USD | `-42.68%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 16,600,000.00 USD | 0.00 USD | 10,120.00 USD | `-42.28%` | `233,977.00` |
| `Live` | `Long` | `0.0433` | 16,590,000.00 USD | 0.00 USD | 2,450.00 USD | `-42.15%` | `56,456.00` |
| `Live` | `Long` | `0.0435` | 16,590,000.00 USD | 0.00 USD | 4,960.00 USD | `-42.01%` | `114,259.00` |
| `Live` | `Long` | `0.0439` | 16,580,000.00 USD | 0.00 USD | 1,610.00 USD | `-41.48%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 16,580,000.00 USD | 0.00 USD | 750.58 USD | `-41.35%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,580,000.00 USD | 0.00 USD | 1,060.00 USD | `-41.21%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 16,580,000.00 USD | 0.00 USD | 216,270.00 USD | `-40.81%` | `4,876,482.00` |
| `Live` | `Long` | `0.0447` | 16,360,000.00 USD | 0.00 USD | 444.76 USD | `-40.41%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 16,360,000.00 USD | 0.00 USD | 248.63 USD | `-40.28%` | `5,556.00` |
| `Live` | `Long` | `0.0449` | 16,360,000.00 USD | 0.00 USD | 13,010.00 USD | `-40.14%` | `290,000.00` |
| `Live` | `Long` | `0.0449` | 16,350,000.00 USD | 0.00 USD | 810.81 USD | `-40.01%` | `18,038.00` |
| `Live` | `Long` | `0.0452` | 16,350,000.00 USD | 0.00 USD | 5,240.00 USD | `-39.61%` | `115,774.00` |
| `Live` | `Long` | `0.0454` | 16,340,000.00 USD | 0.00 USD | 2,370.00 USD | `-39.48%` | `52,202.00` |
| `Live` | `Long` | `0.0454` | 16,340,000.00 USD | 0.00 USD | 2,170.00 USD | `-39.34%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 16,340,000.00 USD | 0.00 USD | 32,650.00 USD | `-39.21%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 16,310,000.00 USD | 0.00 USD | 6,480.00 USD | `-38.94%` | `141,700.00` |
| `Live` | `Long` | `0.0459` | 16,300,000.00 USD | 0.00 USD | 689.25 USD | `-38.68%` | `15,000.00` |
| `Live` | `Long` | `0.0461` | 16,300,000.00 USD | 0.00 USD | 4,500.00 USD | `-38.54%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 16,290,000.00 USD | 0.00 USD | 114.36 USD | `-38.41%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 16,290,000.00 USD | 0.00 USD | 362.87 USD | `-38.14%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 16,290,000.00 USD | 0.00 USD | 16,780.00 USD | `-38.01%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 16,280,000.00 USD | 0.00 USD | 109.49 USD | `-37.74%` | `2,347.00` |
| `Live` | `Long` | `0.0467` | 16,280,000.00 USD | 0.00 USD | 451.75 USD | `-37.61%` | `9,663.00` |
| `Live` | `Long` | `0.0469` | 16,280,000.00 USD | 0.00 USD | 4,700.00 USD | `-37.34%` | `100,000.00` |
| `Live` | `Long` | `0.0473` | 16,270,000.00 USD | 0.00 USD | 3,180.00 USD | `-36.94%` | `67,207.00` |
| `Live` | `Long` | `0.0476` | 16,270,000.00 USD | 0.00 USD | 925.74 USD | `-36.41%` | `19,428.00` |
| `Live` | `Long` | `0.0479` | 16,270,000.00 USD | 0.00 USD | 71,390.00 USD | `-36.01%` | `1,488,849.00` |
| `Live` | `Long` | `0.0481` | 16,200,000.00 USD | 0.00 USD | 56,440.00 USD | `-35.87%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 16,140,000.00 USD | 0.00 USD | 2,330.00 USD | `-35.74%` | `48,418.00` |
| `Live` | `Long` | `0.0483` | 16,140,000.00 USD | 0.00 USD | 42,370.00 USD | `-35.47%` | `876,325.00` |
| `Live` | `Long` | `0.0485` | 16,090,000.00 USD | 0.00 USD | 1,480.00 USD | `-35.34%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 16,090,000.00 USD | 0.00 USD | 1,280.00 USD | `-34.81%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 16,090,000.00 USD | 0.00 USD | 5,470.00 USD | `-34.67%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 16,090,000.00 USD | 0.00 USD | 1,080.00 USD | `-34.54%` | `21,989.00` |
| `Live` | `Long` | `0.0491` | 16,090,000.00 USD | 0.00 USD | 104,040.00 USD | `-34.41%` | `2,116,686.00` |
| `Live` | `Long` | `0.0495` | 15,980,000.00 USD | 0.00 USD | 267.52 USD | `-34.01%` | `5,410.00` |
| `Live` | `Long` | `0.0495` | 15,980,000.00 USD | 0.00 USD | 52,340.00 USD | `-33.87%` | `1,056,296.00` |
| `Live` | `Long` | `0.0498` | 15,930,000.00 USD | 0.00 USD | 253.82 USD | `-33.61%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 15,930,000.00 USD | 0.00 USD | 501.50 USD | `-33.21%` | `10,020.00` |
| `Live` | `Long` | `0.0502` | 15,930,000.00 USD | 0.00 USD | 120.06 USD | `-33.07%` | `2,394.00` |
| `Live` | `Long` | `0.0503` | 15,930,000.00 USD | 0.00 USD | 10,280.00 USD | `-32.94%` | `204,529.00` |
| `Live` | `Long` | `0.0503` | 15,920,000.00 USD | 0.00 USD | 1,360.00 USD | `-32.80%` | `27,061.00` |
| `Live` | `Long` | `0.0505` | 15,920,000.00 USD | 0.00 USD | 334.89 USD | `-32.67%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 15,920,000.00 USD | 0.00 USD | 1,040.00 USD | `-32.40%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 15,910,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-32.27%` | `21,529,860.00` |
| `Live` | `Long` | `0.0510` | 14,820,000.00 USD | 0.00 USD | 535.43 USD | `-32.00%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,820,000.00 USD | 0.00 USD | 566.65 USD | `-31.87%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,820,000.00 USD | 0.00 USD | 11,000.00 USD | `-31.74%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,810,000.00 USD | 0.00 USD | 2,680.00 USD | `-31.60%` | `52,212.00` |
| `Live` | `Long` | `0.0515` | 14,810,000.00 USD | 0.00 USD | 308.55 USD | `-31.34%` | `5,997.00` |
| `Live` | `Long` | `0.0517` | 14,810,000.00 USD | 0.00 USD | 1,190.00 USD | `-30.94%` | `23,007.00` |
| `Live` | `Long` | `0.0519` | 14,810,000.00 USD | 0.00 USD | 7,510.00 USD | `-30.80%` | `144,770.00` |
| `Live` | `Long` | `0.0520` | 14,800,000.00 USD | 0.00 USD | 277.72 USD | `-30.67%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,800,000.00 USD | 0.00 USD | 5,350.00 USD | `-30.54%` | `102,859.00` |
| `Live` | `Long` | `0.0522` | 14,790,000.00 USD | 0.00 USD | 315,250.00 USD | `-30.27%` | `6,033,568.00` |
| `Live` | `Long` | `0.0524` | 14,480,000.00 USD | 0.00 USD | 2,230.00 USD | `-30.00%` | `42,425.00` |
| `Live` | `Long` | `0.0525` | 14,480,000.00 USD | 0.00 USD | 10,260.00 USD | `-29.87%` | `195,318.00` |
| `Live` | `Long` | `0.0527` | 14,470,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.60%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,460,000.00 USD | 0.00 USD | 673.52 USD | `-29.47%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,460,000.00 USD | 0.00 USD | 182,740.00 USD | `-29.33%` | `3,451,252.00` |
| `Live` | `Long` | `0.0532` | 14,280,000.00 USD | 0.00 USD | 12,030.00 USD | `-29.07%` | `226,274.00` |
| `Live` | `Long` | `0.0532` | 14,270,000.00 USD | 0.00 USD | 8,420.00 USD | `-28.93%` | `158,210.00` |
| `Live` | `Long` | `0.0534` | 14,260,000.00 USD | 0.00 USD | 1,890.00 USD | `-28.67%` | `35,411.00` |
| `Live` | `Long` | `0.0536` | 14,260,000.00 USD | 0.00 USD | 942.48 USD | `-28.53%` | `17,600.00` |
| `Live` | `Long` | `0.0537` | 14,260,000.00 USD | 0.00 USD | 1,590.00 USD | `-28.40%` | `29,631.00` |
| `Live` | `Long` | `0.0539` | 14,250,000.00 USD | 0.00 USD | 5,290.00 USD | `-28.00%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 14,250,000.00 USD | 0.00 USD | 14,430.00 USD | `-27.87%` | `266,999.00` |
| `Live` | `Long` | `0.0541` | 14,240,000.00 USD | 0.00 USD | 3,290.00 USD | `-27.73%` | `60,699.00` |
| `Live` | `Long` | `0.0542` | 14,230,000.00 USD | 0.00 USD | 96,530.00 USD | `-27.60%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 14,140,000.00 USD | 0.00 USD | 28,620.00 USD | `-27.47%` | `526,651.00` |
| `Live` | `Long` | `0.0546` | 14,110,000.00 USD | 0.00 USD | 2,840.00 USD | `-27.20%` | `52,101.00` |
| `Live` | `Long` | `0.0546` | 14,100,000.00 USD | 0.00 USD | 1,420.00 USD | `-27.07%` | `25,899.00` |
| `Live` | `Long` | `0.0548` | 14,100,000.00 USD | 0.00 USD | 188.07 USD | `-26.93%` | `3,435.00` |
| `Live` | `Long` | `0.0551` | 14,100,000.00 USD | 0.00 USD | 1,760.00 USD | `-26.40%` | `31,888.00` |
| `Live` | `Long` | `0.0556` | 14,100,000.00 USD | 0.00 USD | 907.02 USD | `-25.87%` | `16,328.00` |
| `Live` | `Long` | `0.0558` | 14,100,000.00 USD | 0.00 USD | 6,290.00 USD | `-25.46%` | `112,671.00` |
| `Live` | `Long` | `0.0561` | 14,090,000.00 USD | 0.00 USD | 8,410.00 USD | `-25.20%` | `150,077.00` |
| `Live` | `Long` | `0.0561` | 14,080,000.00 USD | 0.00 USD | 38,870.00 USD | `-25.06%` | `692,198.00` |
| `Live` | `Long` | `0.0563` | 14,050,000.00 USD | 0.00 USD | 1,820.00 USD | `-24.93%` | `32,433.00` |
| `Live` | `Long` | `0.0563` | 14,040,000.00 USD | 0.00 USD | 351.85 USD | `-24.80%` | `6,244.00` |
| `Live` | `Long` | `0.0565` | 14,040,000.00 USD | 0.00 USD | 178.61 USD | `-24.66%` | `3,164.00` |
| `Live` | `Long` | `0.0566` | 14,040,000.00 USD | 0.00 USD | 131.48 USD | `-24.53%` | `2,325.00` |
| `Live` | `Long` | `0.0566` | 14,040,000.00 USD | 0.00 USD | 749.76 USD | `-24.40%` | `13,235.00` |
| `Live` | `Long` | `0.0568` | 14,040,000.00 USD | 0.00 USD | 567.50 USD | `-24.26%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 14,040,000.00 USD | 0.00 USD | 315.67 USD | `-24.00%` | `5,543.00` |
| `Live` | `Long` | `0.0570` | 14,040,000.00 USD | 0.00 USD | 8,350.00 USD | `-23.86%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 14,030,000.00 USD | 0.00 USD | 814.04 USD | `-23.73%` | `14,244.00` |
| `Live` | `Long` | `0.0573` | 14,030,000.00 USD | 0.00 USD | 359.24 USD | `-23.60%` | `6,275.00` |
| `Live` | `Long` | `0.0573` | 14,030,000.00 USD | 0.00 USD | 3,910.00 USD | `-23.46%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 14,030,000.00 USD | 0.00 USD | 3,960.00 USD | `-23.20%` | `68,830.00` |
| `Live` | `Long` | `0.0576` | 14,020,000.00 USD | 0.00 USD | 10,600.00 USD | `-23.06%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 14,010,000.00 USD | 0.00 USD | 14,210.00 USD | `-22.93%` | `245,980.00` |
| `Live` | `Long` | `0.0578` | 14,000,000.00 USD | 0.00 USD | 6,430.00 USD | `-22.80%` | `111,181.00` |
| `Live` | `Long` | `0.0580` | 13,990,000.00 USD | 0.00 USD | 441.75 USD | `-22.66%` | `7,623.00` |
| `Live` | `Long` | `0.0580` | 13,990,000.00 USD | 0.00 USD | 431.14 USD | `-22.53%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,990,000.00 USD | 0.00 USD | 447.17 USD | `-22.40%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,990,000.00 USD | 0.00 USD | 582.50 USD | `-22.26%` | `10,000.00` |
| `Live` | `Long` | `0.0583` | 13,990,000.00 USD | 0.00 USD | 347,440.00 USD | `-22.13%` | `5,954,428.00` |
| `Live` | `Long` | `0.0585` | 13,640,000.00 USD | 0.00 USD | 19,490.00 USD | `-21.99%` | `333,408.00` |
| `Live` | `Long` | `0.0585` | 13,620,000.00 USD | 0.00 USD | 172.78 USD | `-21.86%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,620,000.00 USD | 0.00 USD | 5,280.00 USD | `-21.73%` | `90,000.00` |
| `Live` | `Long` | `0.0587` | 13,620,000.00 USD | 0.00 USD | 305.15 USD | `-21.59%` | `5,194.00` |
| `Live` | `Long` | `0.0590` | 13,620,000.00 USD | 0.00 USD | 212.22 USD | `-21.33%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 13,620,000.00 USD | 0.00 USD | 26,980.00 USD | `-21.06%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,590,000.00 USD | 0.00 USD | 546.26 USD | `-20.79%` | `9,204.00` |
| `Live` | `Long` | `0.0595` | 13,590,000.00 USD | 0.00 USD | 4,520.00 USD | `-20.66%` | `76,002.00` |
| `Live` | `Long` | `0.0595` | 13,590,000.00 USD | 0.00 USD | 2,940.00 USD | `-20.53%` | `49,364.00` |
| `Live` | `Long` | `0.0597` | 13,580,000.00 USD | 0.00 USD | 25,990.00 USD | `-20.26%` | `435,000.00` |
| `Live` | `Long` | `0.0599` | 13,560,000.00 USD | 0.00 USD | 4,560.00 USD | `-20.13%` | `76,220.00` |
| `Live` | `Long` | `0.0600` | 13,550,000.00 USD | 0.00 USD | 1,130.00 USD | `-19.99%` | `18,786.00` |
| `Live` | `Long` | `0.0600` | 13,550,000.00 USD | 0.00 USD | 7,210.00 USD | `-19.86%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 13,540,000.00 USD | 0.00 USD | 8,490.00 USD | `-19.73%` | `141,093.00` |
| `Live` | `Long` | `0.0602` | 13,540,000.00 USD | 0.00 USD | 830.97 USD | `-19.59%` | `13,792.00` |
| `Live` | `Long` | `0.0604` | 13,540,000.00 USD | 0.00 USD | 548.46 USD | `-19.46%` | `9,088.00` |
| `Live` | `Long` | `0.0605` | 13,530,000.00 USD | 0.00 USD | 32,090.00 USD | `-19.19%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 13,500,000.00 USD | 0.00 USD | 622.63 USD | `-19.06%` | `10,266.00` |
| `Live` | `Long` | `0.0607` | 13,500,000.00 USD | 0.00 USD | 1,220.00 USD | `-18.93%` | `20,080.00` |
| `Live` | `Long` | `0.0609` | 13,500,000.00 USD | 0.00 USD | 717.73 USD | `-18.79%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 13,500,000.00 USD | 0.00 USD | 6,160.00 USD | `-18.66%` | `101,022.00` |
| `Live` | `Long` | `0.0612` | 13,490,000.00 USD | 0.00 USD | 629.72 USD | `-18.39%` | `10,298.00` |
| `Live` | `Long` | `0.0612` | 13,490,000.00 USD | 0.00 USD | 298.17 USD | `-18.26%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 13,490,000.00 USD | 0.00 USD | 655.16 USD | `-18.12%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 13,490,000.00 USD | 0.00 USD | 1,890.00 USD | `-17.86%` | `30,770.00` |
| `Live` | `Long` | `0.0617` | 13,490,000.00 USD | 0.00 USD | 11,100.00 USD | `-17.72%` | `180,028.00` |
| `Live` | `Long` | `0.0617` | 13,480,000.00 USD | 0.00 USD | 6,090,000.00 USD | `-17.59%` | `98,668,984.00` |
| `Live` | `Long` | `0.0619` | 7,390,000.00 USD | 0.00 USD | 17,440.00 USD | `-17.32%` | `281,570.00` |
| `Live` | `Long` | `0.0621` | 7,370,000.00 USD | 0.00 USD | 26,790.00 USD | `-17.19%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,340,000.00 USD | 0.00 USD | 345.86 USD | `-17.06%` | `5,565.00` |
| `Live` | `Long` | `0.0624` | 7,340,000.00 USD | 0.00 USD | 1,900.00 USD | `-16.79%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,340,000.00 USD | 0.00 USD | 43,420.00 USD | `-16.66%` | `695,308.00` |
| `Live` | `Long` | `0.0625` | 7,300,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-16.52%` | `17,630,450.00` |
| `Live` | `Long` | `0.0626` | 6,190,000.00 USD | 0.00 USD | 870.40 USD | `-16.39%` | `13,893.00` |
| `Live` | `Long` | `0.0628` | 6,190,000.00 USD | 0.00 USD | 461.78 USD | `-16.26%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,190,000.00 USD | 0.00 USD | 8,460.00 USD | `-16.12%` | `134,561.00` |
| `Live` | `Long` | `0.0630` | 6,180,000.00 USD | 0.00 USD | 2,430.00 USD | `-15.86%` | `38,603.00` |
| `Live` | `Long` | `0.0631` | 6,180,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-15.72%` | `20,783,139.00` |
| `Live` | `Long` | `0.0633` | 4,870,000.00 USD | 0.00 USD | 3,030.00 USD | `-15.59%` | `47,852.00` |
| `Live` | `Long` | `0.0634` | 4,870,000.00 USD | 0.00 USD | 12,660.00 USD | `-15.46%` | `199,771.00` |
| `Live` | `Long` | `0.0635` | 4,850,000.00 USD | 0.00 USD | 1,690.00 USD | `-15.32%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 4,850,000.00 USD | 0.00 USD | 905.97 USD | `-15.19%` | `14,256.00` |
| `Live` | `Long` | `0.0636` | 4,850,000.00 USD | 0.00 USD | 4,770.00 USD | `-15.06%` | `74,997.00` |
| `Live` | `Long` | `0.0638` | 4,850,000.00 USD | 0.00 USD | 5,600.00 USD | `-14.92%` | `87,791.00` |
| `Live` | `Long` | `0.0639` | 4,840,000.00 USD | 0.00 USD | 23,220.00 USD | `-14.79%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 4,820,000.00 USD | 0.00 USD | 2,100.00 USD | `-14.65%` | `32,904.00` |
| `Live` | `Long` | `0.0640` | 4,820,000.00 USD | 0.00 USD | 150.01 USD | `-14.52%` | `2,342.00` |
| `Live` | `Long` | `0.0641` | 4,810,000.00 USD | 0.00 USD | 17,700.00 USD | `-14.39%` | `275,923.00` |
| `Live` | `Long` | `0.0643` | 4,800,000.00 USD | 0.00 USD | 9,390.00 USD | `-14.25%` | `146,111.00` |
| `Live` | `Long` | `0.0644` | 4,790,000.00 USD | 0.00 USD | 76,280.00 USD | `-14.12%` | `1,185,416.00` |
| `Live` | `Long` | `0.0644` | 4,710,000.00 USD | 0.00 USD | 27,180.00 USD | `-13.99%` | `421,717.00` |
| `Live` | `Long` | `0.0645` | 4,680,000.00 USD | 0.00 USD | 631.94 USD | `-13.85%` | `9,790.00` |
| `Live` | `Long` | `0.0648` | 4,680,000.00 USD | 0.00 USD | 162,920.00 USD | `-13.59%` | `2,516,210.00` |
| `Live` | `Long` | `0.0649` | 4,520,000.00 USD | 0.00 USD | 8,800.00 USD | `-13.45%` | `135,642.00` |
| `Live` | `Long` | `0.0649` | 4,510,000.00 USD | 0.00 USD | 21,910.00 USD | `-13.32%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 4,490,000.00 USD | 0.00 USD | 2,380.00 USD | `-13.05%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,490,000.00 USD | 0.00 USD | 13,770.00 USD | `-12.92%` | `210,965.00` |
| `Live` | `Long` | `0.0654` | 4,470,000.00 USD | 0.00 USD | 4,720.00 USD | `-12.65%` | `72,076.00` |
| `Live` | `Long` | `0.0655` | 4,470,000.00 USD | 0.00 USD | 7,790.00 USD | `-12.52%` | `118,852.00` |
| `Live` | `Long` | `0.0658` | 4,460,000.00 USD | 0.00 USD | 66,820.00 USD | `-12.25%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,390,000.00 USD | 0.00 USD | 14,600.00 USD | `-12.12%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,380,000.00 USD | 0.00 USD | 9,600.00 USD | `-11.99%` | `145,525.00` |
| `Live` | `Long` | `0.0660` | 4,370,000.00 USD | 0.00 USD | 2,510.00 USD | `-11.85%` | `38,008.00` |
| `Live` | `Long` | `0.0662` | 4,370,000.00 USD | 0.00 USD | 2,280.00 USD | `-11.72%` | `34,474.00` |
| `Live` | `Long` | `0.0663` | 4,370,000.00 USD | 0.00 USD | 1,630.00 USD | `-11.59%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,360,000.00 USD | 0.00 USD | 17,410.00 USD | `-11.45%` | `262,335.00` |
| `Live` | `Long` | `0.0664` | 4,350,000.00 USD | 0.00 USD | 1,270.00 USD | `-11.32%` | `19,149.00` |
| `Live` | `Long` | `0.0667` | 4,350,000.00 USD | 0.00 USD | 34,860.00 USD | `-11.05%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,310,000.00 USD | 0.00 USD | 7,620.00 USD | `-10.92%` | `114,225.00` |
| `Live` | `Long` | `0.0669` | 4,300,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-10.78%` | `17,148,056.00` |
| `Live` | `Long` | `0.0669` | 3,160,000.00 USD | 0.00 USD | 1,180.00 USD | `-10.65%` | `17,570.00` |
| `Live` | `Long` | `0.0670` | 3,160,000.00 USD | 0.00 USD | 9,190.00 USD | `-10.52%` | `136,993.00` |
| `Live` | `Long` | `0.0673` | 3,150,000.00 USD | 0.00 USD | 9,220.00 USD | `-10.25%` | `137,152.00` |
| `Live` | `Long` | `0.0673` | 3,140,000.00 USD | 0.00 USD | 15,370.00 USD | `-10.12%` | `228,139.00` |
| `Live` | `Long` | `0.0674` | 3,120,000.00 USD | 0.00 USD | 1,780.00 USD | `-9.98%` | `26,361.00` |
| `Live` | `Long` | `0.0675` | 3,120,000.00 USD | 0.00 USD | 11,450.00 USD | `-9.85%` | `169,510.00` |
| `Live` | `Long` | `0.0677` | 3,110,000.00 USD | 0.00 USD | 14,030.00 USD | `-9.72%` | `207,451.00` |
| `Live` | `Long` | `0.0678` | 3,090,000.00 USD | 0.00 USD | 4,290.00 USD | `-9.58%` | `63,374.00` |
| `Live` | `Long` | `0.0678` | 3,090,000.00 USD | 0.00 USD | 34,560.00 USD | `-9.45%` | `509,370.00` |
| `Live` | `Long` | `0.0679` | 3,060,000.00 USD | 0.00 USD | 16,630.00 USD | `-9.32%` | `244,729.00` |
| `Live` | `Long` | `0.0680` | 3,040,000.00 USD | 0.00 USD | 212.72 USD | `-9.18%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,040,000.00 USD | 0.00 USD | 117.29 USD | `-9.05%` | `1,721.00` |
| `Live` | `Long` | `0.0683` | 3,040,000.00 USD | 0.00 USD | 6,220.00 USD | `-8.92%` | `91,110.00` |
| `Live` | `Long` | `0.0683` | 3,030,000.00 USD | 0.00 USD | 49,510.00 USD | `-8.78%` | `724,293.00` |
| `Live` | `Long` | `0.0684` | 2,980,000.00 USD | 0.00 USD | 80,430.00 USD | `-8.65%` | `1,174,961.00` |
| `Live` | `Long` | `0.0685` | 2,900,000.00 USD | 0.00 USD | 13,120.00 USD | `-8.52%` | `191,414.00` |
| `Live` | `Long` | `0.0687` | 2,890,000.00 USD | 0.00 USD | 595.81 USD | `-8.38%` | `8,679.00` |
| `Live` | `Long` | `0.0688` | 2,890,000.00 USD | 0.00 USD | 16,210.00 USD | `-8.25%` | `235,726.00` |
| `Live` | `Long` | `0.0688` | 2,870,000.00 USD | 0.00 USD | 870.75 USD | `-8.12%` | `12,647.00` |
| `Live` | `Long` | `0.0689` | 2,870,000.00 USD | 0.00 USD | 507,660.00 USD | `-7.98%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,360,000.00 USD | 0.00 USD | 10,310.00 USD | `-7.85%` | `149,295.00` |
| `Live` | `Long` | `0.0692` | 2,350,000.00 USD | 0.00 USD | 13,510.00 USD | `-7.72%` | `195,385.00` |
| `Live` | `Long` | `0.0693` | 2,340,000.00 USD | 0.00 USD | 9,970.00 USD | `-7.58%` | `144,028.00` |
| `Live` | `Long` | `0.0693` | 2,330,000.00 USD | 0.00 USD | 2,020.00 USD | `-7.45%` | `29,107.00` |
| `Live` | `Long` | `0.0694` | 2,330,000.00 USD | 0.00 USD | 4,980.00 USD | `-7.31%` | `71,770.00` |
| `Live` | `Long` | `0.0697` | 2,320,000.00 USD | 0.00 USD | 5,240.00 USD | `-7.05%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,320,000.00 USD | 0.00 USD | 4,720.00 USD | `-6.91%` | `67,696.00` |
| `Live` | `Long` | `0.0698` | 2,310,000.00 USD | 0.00 USD | 38,610.00 USD | `-6.78%` | `552,700.00` |
| `Live` | `Long` | `0.0699` | 2,270,000.00 USD | 0.00 USD | 1,310.00 USD | `-6.65%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,270,000.00 USD | 0.00 USD | 9,620.00 USD | `-6.51%` | `137,335.00` |
| `Live` | `Long` | `0.0702` | 2,260,000.00 USD | 0.00 USD | 8,310.00 USD | `-6.38%` | `118,427.00` |
| `Live` | `Long` | `0.0703` | 2,260,000.00 USD | 0.00 USD | 1,070.00 USD | `-6.25%` | `15,205.00` |
| `Live` | `Long` | `0.0703` | 2,250,000.00 USD | 0.00 USD | 4,360.00 USD | `-6.11%` | `61,923.00` |
| `Live` | `Long` | `0.0704` | 2,250,000.00 USD | 0.00 USD | 216.56 USD | `-5.98%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 423.90 USD | `-5.71%` | `6,000.00` |
| `Live` | `Long` | `0.0707` | 2,250,000.00 USD | 0.00 USD | 536.00 USD | `-5.58%` | `7,576.00` |
| `Live` | `Long` | `0.0708` | 2,250,000.00 USD | 0.00 USD | 94,010.00 USD | `-5.45%` | `1,326,872.00` |
| `Live` | `Long` | `0.0709` | 2,150,000.00 USD | 0.00 USD | 821.60 USD | `-5.31%` | `11,580.00` |
| `Live` | `Long` | `0.0711` | 2,150,000.00 USD | 0.00 USD | 9,660.00 USD | `-5.18%` | `135,904.00` |
| `Live` | `Long` | `0.0712` | 2,140,000.00 USD | 0.00 USD | 2,160.00 USD | `-5.05%` | `30,362.00` |
| `Live` | `Long` | `0.0712` | 2,140,000.00 USD | 0.00 USD | 802.06 USD | `-4.91%` | `11,257.00` |
| `Live` | `Long` | `0.0713` | 2,140,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-4.78%` | `24,517,328.00` |
| `Live` | `Long` | `0.0714` | 391,920.00 USD | 0.00 USD | 213.78 USD | `-4.65%` | `2,992.00` |
| `Live` | `Long` | `0.0716` | 391,710.00 USD | 0.00 USD | 8,120.00 USD | `-4.51%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 383,590.00 USD | 0.00 USD | 1,170.00 USD | `-4.38%` | `16,291.00` |
| `Live` | `Long` | `0.0717` | 382,420.00 USD | 0.00 USD | 22,270.00 USD | `-4.25%` | `310,316.00` |
| `Live` | `Long` | `0.0718` | 360,160.00 USD | 0.00 USD | 1,070.00 USD | `-4.11%` | `14,951.00` |
| `Live` | `Long` | `0.0720` | 359,080.00 USD | 0.00 USD | 1,900.00 USD | `-3.98%` | `26,342.00` |
| `Live` | `Long` | `0.0721` | 357,190.00 USD | 0.00 USD | 12,160.00 USD | `-3.84%` | `168,703.00` |
| `Live` | `Long` | `0.0722` | 345,030.00 USD | 0.00 USD | 22,360.00 USD | `-3.71%` | `309,869.00` |
| `Live` | `Long` | `0.0722` | 322,680.00 USD | 0.00 USD | 322,050.00 USD | `-3.58%` | `4,457,443.00` |
| `Live` | `Long` | `0.0723` | 626.77 USD | 0.00 USD | 626.77 USD | `-3.44%` | `8,663.00` |
| `Live` | `Short` | `0.0775` | 3,830.00 USD | 3,830.00 USD | 0.00 USD | `+3.36%` | `49,453.00` |
| `Live` | `Short` | `0.0775` | 4,070.00 USD | 240.95 USD | 0.00 USD | `+3.50%` | `3,107.00` |
| `Live` | `Short` | `0.0784` | 4,790.00 USD | 723.88 USD | 0.00 USD | `+4.56%` | `9,239.00` |
| `Live` | `Short` | `0.0788` | 4,910.00 USD | 113.24 USD | 0.00 USD | `+5.10%` | `1,438.00` |
| `Live` | `Short` | `0.0793` | 5,330.00 USD | 423.67 USD | 0.00 USD | `+5.76%` | `5,346.00` |
| `Live` | `Short` | `0.0796` | 314,860.00 USD | 309,520.00 USD | 0.00 USD | `+6.30%` | `3,886,050.00` |
| `Live` | `Short` | `0.0800` | 314,970.00 USD | 113.67 USD | 0.00 USD | `+6.83%` | `1,420.00` |
| `Live` | `Short` | `0.0805` | 315,410.00 USD | 435.61 USD | 0.00 USD | `+7.50%` | `5,408.00` |
| `Live` | `Short` | `0.0819` | 315,790.00 USD | 380.85 USD | 0.00 USD | `+9.23%` | `4,653.00` |
| `Live` | `Short` | `0.0832` | 319,370.00 USD | 3,580.00 USD | 0.00 USD | `+10.97%` | `43,108.00` |
| `Live` | `Short` | `0.0833` | 319,870.00 USD | 500.17 USD | 0.00 USD | `+11.10%` | `6,008.00` |
| `Live` | `Short` | `0.0837` | 320,160.00 USD | 293.44 USD | 0.00 USD | `+11.64%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 321,740.00 USD | 1,570.00 USD | 0.00 USD | `+11.77%` | `18,767.00` |
| `Live` | `Short` | `0.0846` | 431,950.00 USD | 110,220.00 USD | 0.00 USD | `+12.84%` | `1,303,554.00` |
| `Live` | `Short` | `0.0847` | 432,080.00 USD | 128.58 USD | 0.00 USD | `+12.97%` | `1,519.00` |
| `Live` | `Short` | `0.0848` | 433,230.00 USD | 1,150.00 USD | 0.00 USD | `+13.24%` | `13,561.00` |
| `Live` | `Short` | `0.0858` | 433,350.00 USD | 115.30 USD | 0.00 USD | `+14.57%` | `1,343.00` |
| `Live` | `Short` | `0.0859` | 437,800.00 USD | 4,450.00 USD | 0.00 USD | `+14.71%` | `51,791.00` |
| `Live` | `Short` | `0.0871` | 437,940.00 USD | 138.58 USD | 0.00 USD | `+16.17%` | `1,592.00` |
| `Live` | `Short` | `0.0876` | 438,060.00 USD | 127.82 USD | 0.00 USD | `+16.84%` | `1,460.00` |
| `Live` | `Short` | `0.0881` | 438,530.00 USD | 465.17 USD | 0.00 USD | `+17.51%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 438,940.00 USD | 411.53 USD | 0.00 USD | `+18.44%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 439,360.00 USD | 418.80 USD | 0.00 USD | `+18.84%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 439,640.00 USD | 285.70 USD | 0.00 USD | `+19.38%` | `3,194.00` |
| `Live` | `Short` | `0.0905` | 446,410.00 USD | 6,760.00 USD | 0.00 USD | `+20.71%` | `74,784.00` |
| `Live` | `Short` | `0.0906` | 447,720.00 USD | 1,310.00 USD | 0.00 USD | `+20.98%` | `14,420.00` |
| `Live` | `Short` | `0.0911` | 452,660.00 USD | 4,940.00 USD | 0.00 USD | `+21.65%` | `54,197.00` |
| `Live` | `Short` | `0.0921` | 452,830.00 USD | 171.49 USD | 0.00 USD | `+22.85%` | `1,863.00` |
| `Live` | `Short` | `0.0931` | 453,630.00 USD | 805.37 USD | 0.00 USD | `+24.31%` | `8,646.00` |
| `Live` | `Short` | `0.0944` | 493,340.00 USD | 39,700.00 USD | 0.00 USD | `+25.92%` | `420,808.00` |
| `Live` | `Short` | `0.0946` | 497,600.00 USD | 4,260.00 USD | 0.00 USD | `+26.32%` | `45,000.00` |
| `Live` | `Short` | `0.0950` | 522,060.00 USD | 24,460.00 USD | 0.00 USD | `+26.72%` | `257,659.00` |
| `Live` | `Short` | `0.0954` | 522,250.00 USD | 194.24 USD | 0.00 USD | `+27.38%` | `2,035.00` |
| `Live` | `Short` | `0.0955` | 570,030.00 USD | 47,770.00 USD | 0.00 USD | `+27.52%` | `500,000.00` |
| `Live` | `Short` | `0.0959` | 571,190.00 USD | 1,160.00 USD | 0.00 USD | `+28.05%` | `12,089.00` |
| `Live` | `Short` | `0.0961` | 571,800.00 USD | 609.59 USD | 0.00 USD | `+28.32%` | `6,340.00` |
| `Live` | `Short` | `0.0974` | 571,920.00 USD | 121.23 USD | 0.00 USD | `+30.05%` | `1,244.00` |
| `Live` | `Short` | `0.0979` | 572,870.00 USD | 952.67 USD | 0.00 USD | `+30.59%` | `9,736.00` |
| `Live` | `Short` | `0.0983` | 573,350.00 USD | 477.50 USD | 0.00 USD | `+31.12%` | `4,860.00` |
| `Live` | `Short` | `0.1014` | 580,980.00 USD | 7,630.00 USD | 0.00 USD | `+35.39%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 583,950.00 USD | 2,970.00 USD | 0.00 USD | `+35.66%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 584,440.00 USD | 492.85 USD | 0.00 USD | `+35.93%` | `4,839.00` |
| `Live` | `Short` | `0.1047` | 590,740.00 USD | 6,300.00 USD | 0.00 USD | `+39.66%` | `60,217.00` |
| `Live` | `Short` | `0.1061` | 596,850.00 USD | 6,110.00 USD | 0.00 USD | `+41.66%` | `57,554.00` |
| `Live` | `Short` | `0.1076` | 597,470.00 USD | 616.19 USD | 0.00 USD | `+43.67%` | `5,724.00` |
| `Live` | `Short` | `0.1085` | 600,710.00 USD | 3,240.00 USD | 0.00 USD | `+44.87%` | `29,849.00` |
| `Live` | `Short` | `0.1095` | 602,470.00 USD | 1,760.00 USD | 0.00 USD | `+46.20%` | `16,110.00` |
| `Live` | `Short` | `0.1127` | 602,690.00 USD | 214.15 USD | 0.00 USD | `+50.34%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 602,830.00 USD | 142.88 USD | 0.00 USD | `+50.74%` | `1,265.00` |
| `Live` | `Short` | `0.1142` | 602,980.00 USD | 154.22 USD | 0.00 USD | `+52.34%` | `1,351.00` |
| `Live` | `Short` | `0.1158` | 603,110.00 USD | 131.49 USD | 0.00 USD | `+54.61%` | `1,135.00` |
| `Live` | `Short` | `0.1222` | 603,910.00 USD | 796.83 USD | 0.00 USD | `+63.15%` | `6,518.00` |
| `Live` | `Short` | `0.1270` | 604,020.00 USD | 108.80 USD | 0.00 USD | `+69.42%` | `857.00` |
| `Live` | `Short` | `0.1277` | 604,940.00 USD | 921.51 USD | 0.00 USD | `+70.36%` | `7,219.00` |
| `Live` | `Short` | `0.1291` | 605,070.00 USD | 124.63 USD | 0.00 USD | `+72.36%` | `965.00` |
| `Live` | `Short` | `0.1296` | 605,240.00 USD | 171.66 USD | 0.00 USD | `+73.03%` | `1,324.00` |
| `Live` | `Short` | `0.1300` | 649,740.00 USD | 44,510.00 USD | 0.00 USD | `+73.56%` | `342,231.00` |
| `Live` | `Short` | `0.1311` | 651,880.00 USD | 2,140.00 USD | 0.00 USD | `+75.03%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 651,990.00 USD | 102.97 USD | 0.00 USD | `+75.96%` | `781.00` |
| `Live` | `Short` | `0.1338` | 652,190.00 USD | 205.31 USD | 0.00 USD | `+78.50%` | `1,535.00` |
| `Live` | `Short` | `0.1351` | 687,110.00 USD | 34,920.00 USD | 0.00 USD | `+80.37%` | `258,360.00` |
| `Live` | `Short` | `0.1371` | 693,320.00 USD | 6,220.00 USD | 0.00 USD | `+83.04%` | `45,319.00` |
| `Live` | `Short` | `0.1383` | 715,750.00 USD | 22,420.00 USD | 0.00 USD | `+84.50%` | `162,180.00` |
| `Live` | `Short` | `0.1404` | 715,850.00 USD | 100.35 USD | 0.00 USD | `+87.31%` | `715.00` |
| `Live` | `Short` | `0.1404` | 716,510.00 USD | 663.63 USD | 0.00 USD | `+87.44%` | `4,725.00` |
| `Live` | `Short` | `0.1419` | 717,500.00 USD | 989.83 USD | 0.00 USD | `+89.31%` | `6,978.00` |
| `Live` | `Short` | `0.1426` | 719,500.00 USD | 2,000.00 USD | 0.00 USD | `+90.24%` | `14,000.00` |
| `Live` | `Short` | `0.1432` | 721,360.00 USD | 1,860.00 USD | 0.00 USD | `+91.18%` | `13,010.00` |
| `Live` | `Short` | `0.1436` | 725,370.00 USD | 4,010.00 USD | 0.00 USD | `+91.58%` | `27,933.00` |
| `Live` | `Short` | `0.1441` | 725,570.00 USD | 196.63 USD | 0.00 USD | `+92.24%` | `1,365.00` |
| `Live` | `Short` | `0.1444` | 727,110.00 USD | 1,540.00 USD | 0.00 USD | `+92.64%` | `10,691.00` |
| `Live` | `Short` | `0.1472` | 733,520.00 USD | 6,420.00 USD | 0.00 USD | `+96.38%` | `43,601.00` |
| `Live` | `Short` | `0.1479` | 741,780.00 USD | 8,260.00 USD | 0.00 USD | `+97.31%` | `55,849.00` |
| `Live` | `Short` | `0.1482` | 765,600.00 USD | 23,820.00 USD | 0.00 USD | `+97.72%` | `160,802.00` |
| `Live` | `Short` | `0.1492` | 767,580.00 USD | 1,980.00 USD | 0.00 USD | `+99.18%` | `13,240.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 928,340.00 USD | 0.00 USD | 375.42 USD | `-65.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 927,970.00 USD | 0.00 USD | 409.59 USD | `-46.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 927,560.00 USD | 0.00 USD | 132.68 USD | `-45.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 927,420.00 USD | 0.00 USD | 788.27 USD | `-44.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 926,640.00 USD | 0.00 USD | 527.05 USD | `-44.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 926,110.00 USD | 0.00 USD | 286.87 USD | `-40.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 925,820.00 USD | 0.00 USD | 252.42 USD | `-38.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 925,570.00 USD | 0.00 USD | 468.67 USD | `-37.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 925,100.00 USD | 0.00 USD | 5,160.00 USD | `-34.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 919,940.00 USD | 0.00 USD | 920.48 USD | `-34.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 919,020.00 USD | 0.00 USD | 236.01 USD | `-33.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 918,790.00 USD | 0.00 USD | 175.41 USD | `-31.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0517` | 918,610.00 USD | 0.00 USD | 242.96 USD | `-31.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 918,370.00 USD | 0.00 USD | 2,670.00 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 915,690.00 USD | 0.00 USD | 1,370.00 USD | `-26.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 914,320.00 USD | 0.00 USD | 437.58 USD | `-25.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 913,880.00 USD | 0.00 USD | 752.54 USD | `-21.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 913,130.00 USD | 0.00 USD | 9,830.00 USD | `-21.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 903,300.00 USD | 0.00 USD | 952.91 USD | `-21.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 902,350.00 USD | 0.00 USD | 668.84 USD | `-19.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 901,680.00 USD | 0.00 USD | 273.90 USD | `-19.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 901,410.00 USD | 0.00 USD | 8,800.00 USD | `-19.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0607` | 892,610.00 USD | 0.00 USD | 218.94 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 892,390.00 USD | 0.00 USD | 504.26 USD | `-17.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 891,880.00 USD | 0.00 USD | 2,470.00 USD | `-17.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 889,410.00 USD | 0.00 USD | 118.27 USD | `-17.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 889,290.00 USD | 0.00 USD | 1,280.00 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0631` | 888,020.00 USD | 0.00 USD | 1,820.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 886,190.00 USD | 0.00 USD | 1,340.00 USD | `-14.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 884,860.00 USD | 0.00 USD | 386.70 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0644` | 884,470.00 USD | 0.00 USD | 644.50 USD | `-13.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 883,830.00 USD | 0.00 USD | 19,520.00 USD | `-13.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 864,310.00 USD | 0.00 USD | 1,410.00 USD | `-12.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 862,900.00 USD | 0.00 USD | 3,140.00 USD | `-12.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 859,760.00 USD | 0.00 USD | 1,100.00 USD | `-12.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 858,660.00 USD | 0.00 USD | 1,200.00 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 857,460.00 USD | 0.00 USD | 996.31 USD | `-11.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 856,470.00 USD | 0.00 USD | 909.85 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 855,560.00 USD | 0.00 USD | 115.57 USD | `-10.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 855,440.00 USD | 0.00 USD | 33,620.00 USD | `-10.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 821,820.00 USD | 0.00 USD | 12,860.00 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 808,960.00 USD | 0.00 USD | 1,540.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 807,420.00 USD | 0.00 USD | 108.08 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 807,310.00 USD | 0.00 USD | 19,540.00 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 787,770.00 USD | 0.00 USD | 1,430.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 786,330.00 USD | 0.00 USD | 7,990.00 USD | `-9.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 778,340.00 USD | 0.00 USD | 8,580.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 769,770.00 USD | 0.00 USD | 4,970.00 USD | `-9.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0683` | 764,800.00 USD | 0.00 USD | 3,100.00 USD | `-8.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0684` | 761,700.00 USD | 0.00 USD | 160.31 USD | `-8.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 761,540.00 USD | 0.00 USD | 38,710.00 USD | `-8.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 722,830.00 USD | 0.00 USD | 295,640.00 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 427,200.00 USD | 0.00 USD | 2,590.00 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 424,610.00 USD | 0.00 USD | 533.09 USD | `-7.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 424,080.00 USD | 0.00 USD | 378.50 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 423,700.00 USD | 0.00 USD | 925.29 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 422,770.00 USD | 0.00 USD | 797.80 USD | `-6.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 421,980.00 USD | 0.00 USD | 11,920.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0702` | 410,060.00 USD | 0.00 USD | 141.77 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 409,920.00 USD | 0.00 USD | 895.27 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 409,020.00 USD | 0.00 USD | 523.23 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0706` | 408,500.00 USD | 0.00 USD | 468.88 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 408,030.00 USD | 0.00 USD | 235.12 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 407,790.00 USD | 0.00 USD | 1,090.00 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 406,710.00 USD | 0.00 USD | 71,660.00 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 335,050.00 USD | 0.00 USD | 497.62 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 334,550.00 USD | 0.00 USD | 20,330.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 314,210.00 USD | 0.00 USD | 608.76 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 313,600.00 USD | 0.00 USD | 16,880.00 USD | `-4.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0716` | 296,730.00 USD | 0.00 USD | 265.67 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 296,460.00 USD | 0.00 USD | 1,670.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 294,790.00 USD | 0.00 USD | 4,210.00 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 290,580.00 USD | 0.00 USD | 13,550.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 277,030.00 USD | 0.00 USD | 413.42 USD | `-3.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 276,620.00 USD | 0.00 USD | 138,380.00 USD | `-3.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 138,240.00 USD | 0.00 USD | 849.15 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 137,390.00 USD | 0.00 USD | 34,460.00 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0726` | 102,930.00 USD | 0.00 USD | 2,030.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 100,900.00 USD | 0.00 USD | 3,400.00 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 97,500.00 USD | 0.00 USD | 29,060.00 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 68,440.00 USD | 0.00 USD | 4,110.00 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 64,320.00 USD | 0.00 USD | 2,090.00 USD | `-2.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 62,230.00 USD | 0.00 USD | 1,950.00 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 60,280.00 USD | 0.00 USD | 535.16 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0735` | 59,750.00 USD | 0.00 USD | 123.40 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 59,620.00 USD | 0.00 USD | 397.76 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 59,230.00 USD | 0.00 USD | 398.00 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 58,830.00 USD | 0.00 USD | 797.39 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 58,030.00 USD | 0.00 USD | 27,920.00 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 30,110.00 USD | 0.00 USD | 1,640.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0741` | 28,470.00 USD | 0.00 USD | 7,330.00 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 21,140.00 USD | 0.00 USD | 2,900.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 18,250.00 USD | 0.00 USD | 415.62 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 17,830.00 USD | 0.00 USD | 16,520.00 USD | `-0.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 1,310.00 USD | 0.00 USD | 398.54 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 915.07 USD | 0.00 USD | 375.86 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 539.21 USD | 0.00 USD | 399.17 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 140.04 USD | 0.00 USD | 140.04 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0750` | 6,280.00 USD | 6,280.00 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0751` | 9,730.00 USD | 3,450.00 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0751` | 10,460.00 USD | 736.17 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0752` | 10,870.00 USD | 406.95 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0754` | 11,090.00 USD | 221.00 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0755` | 11,500.00 USD | 407.73 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 11,910.00 USD | 408.57 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 12,320.00 USD | 408.81 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0757` | 16,830.00 USD | 4,520.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0759` | 17,340.00 USD | 504.10 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0760` | 17,740.00 USD | 398.13 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 17,850.00 USD | 113.01 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 18,660.00 USD | 806.81 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 19,470.00 USD | 814.81 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 23,250.00 USD | 3,770.00 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 23,350.00 USD | 109.63 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 24,600.00 USD | 1,250.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 24,780.00 USD | 183.50 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 25,630.00 USD | 843.94 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 26,130.00 USD | 502.52 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 26,950.00 USD | 816.05 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 27,210.00 USD | 266.52 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 29,450.00 USD | 2,240.00 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 29,690.00 USD | 240.02 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 33,630.00 USD | 3,930.00 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 34,030.00 USD | 407.23 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 34,350.00 USD | 321.13 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 35,850.00 USD | 1,490.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 36,250.00 USD | 407.72 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 36,580.00 USD | 329.23 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 36,890.00 USD | 303.77 USD | 0.00 USD | `+4.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 37,070.00 USD | 186.07 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 40,150.00 USD | 3,080.00 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 41,350.00 USD | 1,200.00 USD | 0.00 USD | `+4.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 45,720.00 USD | 4,370.00 USD | 0.00 USD | `+4.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 45,880.00 USD | 157.14 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 46,010.00 USD | 130.71 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 87,620.00 USD | 41,610.00 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 90,650.00 USD | 3,030.00 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 91,420.00 USD | 773.68 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 92,090.00 USD | 673.60 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 99,960.00 USD | 7,860.00 USD | 0.00 USD | `+5.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 104,550.00 USD | 4,600.00 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 109,820.00 USD | 5,270.00 USD | 0.00 USD | `+5.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 117,640.00 USD | 7,820.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 117,950.00 USD | 312.56 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 118,410.00 USD | 455.34 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 118,530.00 USD | 125.45 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 118,760.00 USD | 230.40 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 119,080.00 USD | 319.16 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 120,090.00 USD | 1,010.00 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 142,840.00 USD | 22,750.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 143,240.00 USD | 400.91 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 143,440.00 USD | 200.46 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 143,700.00 USD | 259.13 USD | 0.00 USD | `+7.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 144,410.00 USD | 707.08 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 153,410.00 USD | 9,010.00 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 250,190.00 USD | 96,780.00 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 251,000.00 USD | 807.50 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 251,260.00 USD | 257.18 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 251,680.00 USD | 424.74 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 251,790.00 USD | 101.80 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 253,170.00 USD | 1,380.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 255,200.00 USD | 2,030.00 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 256,630.00 USD | 1,430.00 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 256,760.00 USD | 129.67 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 257,780.00 USD | 1,020.00 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 260,220.00 USD | 2,450.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 261,250.00 USD | 1,030.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 264,270.00 USD | 3,020.00 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 264,600.00 USD | 327.80 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 265,060.00 USD | 457.92 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 265,750.00 USD | 691.29 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 266,550.00 USD | 800.79 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 267,060.00 USD | 512.05 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 267,560.00 USD | 495.36 USD | 0.00 USD | `+10.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 267,940.00 USD | 389.31 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 268,100.00 USD | 154.58 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 268,400.00 USD | 303.56 USD | 0.00 USD | `+10.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 268,520.00 USD | 112.89 USD | 0.00 USD | `+10.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 268,900.00 USD | 381.45 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 269,050.00 USD | 155.82 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 313,440.00 USD | 44,390.00 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 313,580.00 USD | 138.69 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 314,840.00 USD | 1,260.00 USD | 0.00 USD | `+11.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 314,940.00 USD | 107.03 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,060,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,060,000.00 USD | 3,150.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,060,000.00 USD | 1,470.00 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,060,000.00 USD | 107.71 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,070,000.00 USD | 2,690.00 USD | 0.00 USD | `+12.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,070,000.00 USD | 529.92 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,070,000.00 USD | 219.07 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,070,000.00 USD | 242.84 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,080,000.00 USD | 10,140.00 USD | 0.00 USD | `+13.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,080,000.00 USD | 876.11 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,080,000.00 USD | 812.54 USD | 0.00 USD | `+14.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,080,000.00 USD | 126.76 USD | 0.00 USD | `+14.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,080,000.00 USD | 307.41 USD | 0.00 USD | `+14.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,080,000.00 USD | 614.09 USD | 0.00 USD | `+14.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,080,000.00 USD | 859.50 USD | 0.00 USD | `+14.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,080,000.00 USD | 2,020.00 USD | 0.00 USD | `+14.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,130,000.00 USD | 43,760.00 USD | 0.00 USD | `+15.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,130,000.00 USD | 123.94 USD | 0.00 USD | `+15.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0867` | 2,130,000.00 USD | 271.53 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,130,000.00 USD | 857.15 USD | 0.00 USD | `+16.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,130,000.00 USD | 1,840.00 USD | 0.00 USD | `+16.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,130,000.00 USD | 2,760.00 USD | 0.00 USD | `+16.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,130,000.00 USD | 117.71 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,130,000.00 USD | 111.61 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,130,000.00 USD | 571.18 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,130,000.00 USD | 375.94 USD | 0.00 USD | `+17.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,130,000.00 USD | 627.55 USD | 0.00 USD | `+17.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,130,000.00 USD | 211.04 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,130,000.00 USD | 108.36 USD | 0.00 USD | `+18.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,140,000.00 USD | 543.32 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,140,000.00 USD | 1,820.00 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,140,000.00 USD | 2,080.00 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,160,000.00 USD | 17,680.00 USD | 0.00 USD | `+19.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,160,000.00 USD | 1,370.00 USD | 0.00 USD | `+19.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,160,000.00 USD | 5,630.00 USD | 0.00 USD | `+20.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,160,000.00 USD | 1,090.00 USD | 0.00 USD | `+20.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,170,000.00 USD | 224.86 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,190,000.00 USD | 20,540.00 USD | 0.00 USD | `+20.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,190,000.00 USD | 114.93 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,190,000.00 USD | 679.12 USD | 0.00 USD | `+21.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,190,000.00 USD | 173.36 USD | 0.00 USD | `+21.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,190,000.00 USD | 1,810.00 USD | 0.00 USD | `+22.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,190,000.00 USD | 1,480.00 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,190,000.00 USD | 2,280.00 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,190,000.00 USD | 541.32 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,330,000.00 USD | 137,500.00 USD | 0.00 USD | `+23.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,330,000.00 USD | 691.07 USD | 0.00 USD | `+23.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,340,000.00 USD | 6,250.00 USD | 0.00 USD | `+23.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,350,000.00 USD | 13,480.00 USD | 0.00 USD | `+23.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,350,000.00 USD | 734.82 USD | 0.00 USD | `+24.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,350,000.00 USD | 1,230.00 USD | 0.00 USD | `+24.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0932` | 2,350,000.00 USD | 105.00 USD | 0.00 USD | `+24.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,350,000.00 USD | 184.09 USD | 0.00 USD | `+24.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,350,000.00 USD | 1,120.00 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,360,000.00 USD | 1,860.00 USD | 0.00 USD | `+25.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,360,000.00 USD | 1,070.00 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,360,000.00 USD | 512.15 USD | 0.00 USD | `+25.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,360,000.00 USD | 6,620.00 USD | 0.00 USD | `+26.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,360,000.00 USD | 404.96 USD | 0.00 USD | `+26.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,360,000.00 USD | 129.85 USD | 0.00 USD | `+27.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,370,000.00 USD | 3,740.00 USD | 0.00 USD | `+27.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,370,000.00 USD | 409.17 USD | 0.00 USD | `+28.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,370,000.00 USD | 203.74 USD | 0.00 USD | `+28.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,370,000.00 USD | 2,800.00 USD | 0.00 USD | `+29.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,370,000.00 USD | 1,320.00 USD | 0.00 USD | `+30.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,370,000.00 USD | 694.56 USD | 0.00 USD | `+30.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,370,000.00 USD | 940.91 USD | 0.00 USD | `+31.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,380,000.00 USD | 2,980.00 USD | 0.00 USD | `+32.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,380,000.00 USD | 104.99 USD | 0.00 USD | `+32.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,380,000.00 USD | 1,930.00 USD | 0.00 USD | `+32.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,380,000.00 USD | 1,490.00 USD | 0.00 USD | `+32.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,380,000.00 USD | 1,090.00 USD | 0.00 USD | `+32.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,380,000.00 USD | 438.96 USD | 0.00 USD | `+32.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,380,000.00 USD | 973.76 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,390,000.00 USD | 10,000.00 USD | 0.00 USD | `+33.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,390,000.00 USD | 175.59 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1003` | 2,400,000.00 USD | 2,060.00 USD | 0.00 USD | `+33.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,400,000.00 USD | 482.89 USD | 0.00 USD | `+34.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,400,000.00 USD | 201.90 USD | 0.00 USD | `+34.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,400,000.00 USD | 489.46 USD | 0.00 USD | `+34.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,400,000.00 USD | 103.68 USD | 0.00 USD | `+35.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,400,000.00 USD | 2,590.00 USD | 0.00 USD | `+35.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,400,000.00 USD | 3,810.00 USD | 0.00 USD | `+36.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,410,000.00 USD | 11,200.00 USD | 0.00 USD | `+36.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,420,000.00 USD | 4,330.00 USD | 0.00 USD | `+36.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,420,000.00 USD | 205.50 USD | 0.00 USD | `+37.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,420,000.00 USD | 3,490.00 USD | 0.00 USD | `+37.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,420,000.00 USD | 1,300.00 USD | 0.00 USD | `+37.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,420,000.00 USD | 207.50 USD | 0.00 USD | `+38.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,430,000.00 USD | 813.88 USD | 0.00 USD | `+39.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,450,000.00 USD | 23,160.00 USD | 0.00 USD | `+39.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,450,000.00 USD | 781.51 USD | 0.00 USD | `+39.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,450,000.00 USD | 209.30 USD | 0.00 USD | `+39.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,450,000.00 USD | 1,440.00 USD | 0.00 USD | `+39.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,460,000.00 USD | 5,140.00 USD | 0.00 USD | `+40.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,460,000.00 USD | 585.32 USD | 0.00 USD | `+40.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,460,000.00 USD | 210.90 USD | 0.00 USD | `+40.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,460,000.00 USD | 1,850.00 USD | 0.00 USD | `+40.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,460,000.00 USD | 105.75 USD | 0.00 USD | `+41.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,460,000.00 USD | 3,220.00 USD | 0.00 USD | `+41.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,460,000.00 USD | 1,600.00 USD | 0.00 USD | `+41.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,460,000.00 USD | 212.90 USD | 0.00 USD | `+42.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,460,000.00 USD | 472.63 USD | 0.00 USD | `+42.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,460,000.00 USD | 214.50 USD | 0.00 USD | `+43.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,470,000.00 USD | 1,040.00 USD | 0.00 USD | `+43.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,470,000.00 USD | 136.12 USD | 0.00 USD | `+44.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,470,000.00 USD | 216.10 USD | 0.00 USD | `+44.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,470,000.00 USD | 1,010.00 USD | 0.00 USD | `+45.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,470,000.00 USD | 217.90 USD | 0.00 USD | `+45.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,470,000.00 USD | 219.70 USD | 0.00 USD | `+46.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,480,000.00 USD | 7,920.00 USD | 0.00 USD | `+46.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,480,000.00 USD | 154.22 USD | 0.00 USD | `+47.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,480,000.00 USD | 221.30 USD | 0.00 USD | `+47.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,480,000.00 USD | 1,050.00 USD | 0.00 USD | `+47.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,500,000.00 USD | 24,440.00 USD | 0.00 USD | `+48.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,500,000.00 USD | 223.10 USD | 0.00 USD | `+48.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,500,000.00 USD | 224.70 USD | 0.00 USD | `+49.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,500,000.00 USD | 226.30 USD | 0.00 USD | `+51.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,500,000.00 USD | 950.34 USD | 0.00 USD | `+52.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,500,000.00 USD | 229.50 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,500,000.00 USD | 771.08 USD | 0.00 USD | `+53.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1150` | 2,500,000.00 USD | 942.95 USD | 0.00 USD | `+53.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,500,000.00 USD | 230.90 USD | 0.00 USD | `+54.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,510,000.00 USD | 288.18 USD | 0.00 USD | `+54.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,510,000.00 USD | 619.10 USD | 0.00 USD | `+54.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,510,000.00 USD | 1,250.00 USD | 0.00 USD | `+54.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+54.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,510,000.00 USD | 232.30 USD | 0.00 USD | `+55.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,510,000.00 USD | 1,600.00 USD | 0.00 USD | `+55.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+56.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,510,000.00 USD | 3,730.00 USD | 0.00 USD | `+56.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,520,000.00 USD | 676.22 USD | 0.00 USD | `+57.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,520,000.00 USD | 648.25 USD | 0.00 USD | `+57.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,520,000.00 USD | 1,510.00 USD | 0.00 USD | `+57.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,520,000.00 USD | 448.52 USD | 0.00 USD | `+57.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,520,000.00 USD | 124.58 USD | 0.00 USD | `+58.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,520,000.00 USD | 1,050.00 USD | 0.00 USD | `+58.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,520,000.00 USD | 691.80 USD | 0.00 USD | `+59.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,640,000.00 USD | 117,860.00 USD | 0.00 USD | `+60.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,640,000.00 USD | 143.22 USD | 0.00 USD | `+60.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,640,000.00 USD | 1,380.00 USD | 0.00 USD | `+61.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,640,000.00 USD | 2,270.00 USD | 0.00 USD | `+62.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,640,000.00 USD | 871.99 USD | 0.00 USD | `+63.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,670,000.00 USD | 29,610.00 USD | 0.00 USD | `+69.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,670,000.00 USD | 400.21 USD | 0.00 USD | `+69.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,690,000.00 USD | 13,850.00 USD | 0.00 USD | `+75.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,690,000.00 USD | 2,360.00 USD | 0.00 USD | `+76.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,690,000.00 USD | 4,160.00 USD | 0.00 USD | `+80.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1366` | 2,690,000.00 USD | 114.70 USD | 0.00 USD | `+82.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,690,000.00 USD | 278.50 USD | 0.00 USD | `+86.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,690,000.00 USD | 1,160.00 USD | 0.00 USD | `+88.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,690,000.00 USD | 173.57 USD | 0.00 USD | `+89.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,690,000.00 USD | 380.09 USD | 0.00 USD | `+89.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,710,000.00 USD | 17,150.00 USD | 0.00 USD | `+89.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1439` | 2,710,000.00 USD | 1,440.00 USD | 0.00 USD | `+92.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,710,000.00 USD | 433.35 USD | 0.00 USD | `+92.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1457` | 2,710,000.00 USD | 452.26 USD | 0.00 USD | `+94.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,720,000.00 USD | 3,640.00 USD | 0.00 USD | `+96.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,770,000.00 USD | 55,720.00 USD | 0.00 USD | `+97.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,780,000.00 USD | 2,120.00 USD | 0.00 USD | `+97.85%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.0678` | 11,770,000.00 USD | 0.00 USD | 11,770,000.00 USD | 3,200.00 USD | 39,890.00 USD | 58,170.00 USD |
| `1D` | `0.0679` | 11,670,000.00 USD | 0.00 USD | 11,670,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD |
| `1D` | `0.0680` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 4,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0681` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 134,240.00 USD |
| `1D` | `0.0682` | 11,500,000.00 USD | 0.00 USD | 11,500,000.00 USD | 2,550.00 USD | 33,950.00 USD | 9,630.00 USD |
| `1D` | `0.0683` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 0.00 USD | 20,340.00 USD | 723.57 USD |
| `1D` | `0.0684` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 24,150.00 USD | 15,070.00 USD | 584.27 USD |
| `1D` | `0.0685` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 41,510.00 USD | 12,720.00 USD | 17,260.00 USD |
| `1D` | `0.0686` | 11,320,000.00 USD | 0.00 USD | 11,320,000.00 USD | 41,080.00 USD | 1,410.00 USD | 13,570.00 USD |
| `1D` | `0.0687` | 11,260,000.00 USD | 0.00 USD | 11,260,000.00 USD | 3,150.00 USD | 16,550.00 USD | 14,970.00 USD |
| `1D` | `0.0688` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD |
| `1D` | `0.0691` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0695` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `1D` | `0.0697` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 14,390.00 USD | 24,590.00 USD | 16,440.00 USD |
| `1D` | `0.0698` | 11,140,000.00 USD | 0.00 USD | 11,140,000.00 USD | 25,600.00 USD | 13,930.00 USD | 19,650.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0699` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 53,800.00 USD | 45,460.00 USD | 35,850.00 USD |
| `1D` | `0.0700` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 88,520.00 USD | 32,810.00 USD | 19,750.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0701` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 35,400.00 USD | 18,030.00 USD | 29,630.00 USD |
| `1D` | `0.0702` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 78,740.00 USD | 36,780.00 USD | 164.89 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0703` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 87,540.00 USD | 31,470.00 USD | 41,850.00 USD |
| `1D` | `0.0704` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 44,920.00 USD | 24,150.00 USD | 20,120.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0705` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 41,490.00 USD | 24,910.00 USD | 32,230.00 USD |
| `1D` | `0.0706` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 36,930.00 USD | 29,080.00 USD | 26,890.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0707` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 54,240.00 USD | 21,680.00 USD | 23,150.00 USD |
| `1D` | `0.0708` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 25,410.00 USD | 16,310.00 USD | 27,960.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0709` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 36,740.00 USD | 37,120.00 USD | 15,180.00 USD |
| `1D` | `0.0710` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 21,430.00 USD | 9,300.00 USD | 34,580.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 9,840,000.00 USD | 0.00 USD | 9,840,000.00 USD | 27,890.00 USD | 8,560.00 USD | 42,320.00 USD |
| `1D` | `0.0712` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 56,550.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 35,120.00 USD | 58,130.00 USD | 67,120.00 USD |
| `1D` | `0.0714` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 42,610.00 USD | 42,090.00 USD | 8,650.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 34,440.00 USD | 8,830.00 USD | 38,710.00 USD |
| `1D` | `0.0716` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 24,840.00 USD | 31,610.00 USD | 0.00 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 10,910.00 USD | 7,710.00 USD | 21,890.00 USD |
| `1D` | `0.0718` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 67,080.00 USD | 31,390.00 USD | 32,350.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 10,150.00 USD | 0.00 USD | 2,170.00 USD |
| `1D` | `0.0720` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 31,160.00 USD | 29,440.00 USD | 32,460.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 136,510.00 USD | 76,220.00 USD | 15,670.00 USD |
| `1D` | `0.0722` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 43,930.00 USD | 15,630.00 USD | 22,670.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 54,790.00 USD | 162,040.00 USD | 153,140.00 USD |
| `1D` | `0.0724` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 27,830.00 USD | 87,980.00 USD | 92,380.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 54,140.00 USD | 22,980.00 USD | 23,580.00 USD |
| `1D` | `0.0726` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 51,960.00 USD | 0.00 USD | 2,600.00 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 168,660.00 USD | 0.00 USD | 345,080.00 USD |
| `1D` | `0.0728` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 66,510.00 USD | 85,670.00 USD | 75,670.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 19,510.00 USD | 82,260.00 USD | 30,250.00 USD |
| `1D` | `0.0730` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 112,200.00 USD | 54,520.00 USD | 1,580.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 152,870.00 USD | 49,300.00 USD | 43,260.00 USD |
| `1D` | `0.0732` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 154,930.00 USD | 60,240.00 USD | 81,810.00 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 15,550.00 USD | 0.00 USD | 71,460.00 USD |
| `1D` | `0.0734` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 43,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 33,390.00 USD | 31,100.00 USD | 299.76 USD |
| `1D` | `0.0736` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 234,720.00 USD | 123,630.00 USD | 1.38 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 51,890.00 USD | 42,510.00 USD | 636.56 USD |
| `1D` | `0.0738` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 31,820.00 USD | 199,460.00 USD | 284,360.00 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 33,680.00 USD | 161,430.00 USD | 78,490.00 USD |
| `1D` | `0.0740` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 33,740.00 USD | 0.00 USD | 267.65 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 36,980.00 USD | 0.00 USD | 560.08 USD |
| `1D` | `0.0742` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 286,340.00 USD | 0.00 USD | 684,970.00 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 118,640.00 USD | 234,470.00 USD | 190,020.00 USD |
| `1D` | `0.0744` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 19,880.00 USD | 187,400.00 USD | 59,430.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 199,850.00 USD | 166,270.00 USD | 24,880.00 USD |
| `1D` | `0.0746` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 371,240.00 USD | 274,020.00 USD | 211,560.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 466,980.00 USD | 159,330.00 USD | 131,210.00 USD |
| `1D` | `0.0748` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 130,290.00 USD | 143,100.00 USD | 194,200.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 635,760.00 USD | 0.00 USD | 635,760.00 USD | 203,330.00 USD | 0.00 USD | 149,470.00 USD |
| `1D` | `0.0750` | 282,960.00 USD | 0.00 USD | 282,960.00 USD | 69,890.00 USD | 0.00 USD | 120,790.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 92,290.00 USD | 0.00 USD | 92,290.00 USD | 0.00 USD | 6,860.00 USD | 0.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 85,440.00 USD | 0.00 USD | 85,440.00 USD | 0.00 USD | 85,010.00 USD | 0.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0760` | 424.91 USD | 0.00 USD | 424.91 USD | 0.00 USD | 0.00 USD | 424.91 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 412.85 USD | 412.85 USD | 0.00 USD | 0.00 USD | 0.00 USD | 412.85 USD |
| `1D` | `0.0761` | 825.70 USD | 825.70 USD | 0.00 USD | 0.00 USD | 0.00 USD | 412.85 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 14,210.00 USD | 14,210.00 USD | 0.00 USD | 0.00 USD | 13,220.00 USD | 168.86 USD |
| `1D` | `0.0764` | 340,180.00 USD | 340,180.00 USD | 0.00 USD | 0.00 USD | 325,960.00 USD | 0.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 598,420.00 USD | 598,420.00 USD | 0.00 USD | 0.00 USD | 257,590.00 USD | 656.49 USD |
| `1D` | `0.0766` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 745,930.00 USD | 360,800.00 USD | 0.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 169,980.00 USD | 188,260.00 USD | 502.92 USD |
| `1D` | `0.0768` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 351,760.00 USD | 0.00 USD | 514,350.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 181,440.00 USD | 341,350.00 USD | 148,810.00 USD |
| `1D` | `0.0770` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 272,760.00 USD | 93,300.00 USD | 253,920.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 216,410.00 USD | 232,340.00 USD | 212,480.00 USD |
| `1D` | `0.0772` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 286,340.00 USD | 0.00 USD | 685,130.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 65,160.00 USD | 169,730.00 USD | 149,070.00 USD |
| `1D` | `0.0774` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 164,510.00 USD | 19,440.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 155,740.00 USD | 109,050.00 USD | 0.00 USD |
| `1D` | `0.0776` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 190,100.00 USD | 110,600.00 USD | 86,320.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 205,390.00 USD | 264,690.00 USD | 80,710.00 USD |
| `1D` | `0.0778` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 16,790.00 USD | 202,930.00 USD | 295,930.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 85,950.00 USD | 140,460.00 USD |
| `1D` | `0.0780` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 69,890.00 USD | 31,980.00 USD | 253.82 USD |
| `1D` | `0.0781` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 113,060.00 USD | 68,670.00 USD | 1,410.00 USD |
| `1D` | `0.0782` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 8,010.00 USD | 184,740.00 USD | 145,430.00 USD |
| `1D` | `0.0784` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 265,800.00 USD | 86,850.00 USD | 39,240.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 177,210.00 USD | 110,520.00 USD | 61,840.00 USD |
| `1D` | `0.0786` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 191,180.00 USD | 117,040.00 USD | 233,900.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 298,820.00 USD | 307,550.00 USD | 344,880.00 USD |
| `1D` | `0.0788` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 75,490.00 USD | 181,170.00 USD | 75,110.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 234,900.00 USD | 192,150.00 USD | 96,560.00 USD |
| `1D` | `0.0790` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 102,120.00 USD | 57,780.00 USD | 1,460.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 152,950.00 USD | 95,070.00 USD | 95,210.00 USD |
| `1D` | `0.0792` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 104,950.00 USD | 18,870.00 USD | 33,930.00 USD |
| `1D` | `0.0794` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 92,580.00 USD | 41,370.00 USD | 47,790.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0795` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 10,150.00 USD | 0.00 USD | 73,430.00 USD |
| `1D` | `0.0796` | 13,200,000.00 USD | 13,200,000.00 USD | 0.00 USD | 174,010.00 USD | 0.00 USD | 16,850.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 191,110.00 USD | 89,760.00 USD | 242,940.00 USD |
| `1D` | `0.0798` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 51,440.00 USD | 164,620.00 USD | 1,170.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 191,450.00 USD | 193,600.00 USD | 194,180.00 USD |
| `1D` | `0.0800` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 4,510.00 USD | 5,610.00 USD | 94,010.00 USD |
| `1D` | `0.0801` | 14,640,000.00 USD | 14,640,000.00 USD | 0.00 USD | 6,300.00 USD | 0.00 USD | 2,110.00 USD |
| `1D` | `0.0802` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 7,730.00 USD | 1,770.00 USD | 2,600.00 USD |
| `1D` | `0.0803` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 38,610.00 USD |
| `1D` | `0.0804` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 13,900.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0805` | 14,860,000.00 USD | 14,860,000.00 USD | 0.00 USD | 56,220.00 USD | 37,230.00 USD | 41,110.00 USD |
| `1D` | `0.0806` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 27,790.00 USD | 21,040.00 USD | 215,300.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 221,690.00 USD | 208,070.00 USD | 41,170.00 USD |
| `1D` | `0.0808` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 419,500.00 USD | 131,030.00 USD | 523,560.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 17,490,000.00 USD | 17,490,000.00 USD | 0.00 USD | 477,790.00 USD | 336,610.00 USD | 12,790.00 USD |
| `1D` | `0.0810` | 18,100,000.00 USD | 18,100,000.00 USD | 0.00 USD | 293,220.00 USD | 180,540.00 USD | 133,520.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 18,430,000.00 USD | 18,430,000.00 USD | 0.00 USD | 83,280.00 USD | 241,410.00 USD | 875.97 USD |
| `1D` | `0.0812` | 18,790,000.00 USD | 18,790,000.00 USD | 0.00 USD | 144,600.00 USD | 99,490.00 USD | 120,600.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 19,070,000.00 USD | 19,070,000.00 USD | 0.00 USD | 49,290.00 USD | 23,210.00 USD | 208,970.00 USD |
| `1D` | `0.0814` | 19,470,000.00 USD | 19,470,000.00 USD | 0.00 USD | 29,840.00 USD | 79,960.00 USD | 292,740.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 19,820,000.00 USD | 19,820,000.00 USD | 0.00 USD | 150,190.00 USD | 72,710.00 USD | 124,900.00 USD |
| `1D` | `0.0816` | 20,540,000.00 USD | 20,540,000.00 USD | 0.00 USD | 348,980.00 USD | 194,790.00 USD | 177,540.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 21,100,000.00 USD | 21,100,000.00 USD | 0.00 USD | 301,230.00 USD | 127,050.00 USD | 130,180.00 USD |
| `1D` | `0.0818` | 21,840,000.00 USD | 21,840,000.00 USD | 0.00 USD | 269,340.00 USD | 161,260.00 USD | 308,240.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 174,640.00 USD | 312,480.00 USD | 128,780.00 USD |
| `1D` | `0.0820` | 23,140,000.00 USD | 23,140,000.00 USD | 0.00 USD | 136,010.00 USD | 202,840.00 USD | 344,550.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 23,600,000.00 USD | 23,600,000.00 USD | 0.00 USD | 210,590.00 USD | 79,630.00 USD | 170,610.00 USD |
| `1D` | `0.0822` | 24,190,000.00 USD | 24,190,000.00 USD | 0.00 USD | 262,170.00 USD | 169,200.00 USD | 156,380.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 24,540,000.00 USD | 24,540,000.00 USD | 0.00 USD | 270,850.00 USD | 75,420.00 USD | 8,520.00 USD |
| `1D` | `0.0824` | 25,120,000.00 USD | 25,120,000.00 USD | 0.00 USD | 151,910.00 USD | 226,510.00 USD | 198,590.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 25,400,000.00 USD | 25,400,000.00 USD | 0.00 USD | 127,790.00 USD | 122,020.00 USD | 27,800.00 USD |
| `1D` | `0.0826` | 25,820,000.00 USD | 25,820,000.00 USD | 0.00 USD | 150,570.00 USD | 84,820.00 USD | 190,080.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 25,920,000.00 USD | 25,920,000.00 USD | 0.00 USD | 49,040.00 USD | 48,230.00 USD | 399.88 USD |
| `1D` | `0.0828` | 26,270,000.00 USD | 26,270,000.00 USD | 0.00 USD | 216,200.00 USD | 75,940.00 USD | 58,410.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 26,640,000.00 USD | 26,640,000.00 USD | 0.00 USD | 182,720.00 USD | 111,290.00 USD | 72,580.00 USD |
| `1D` | `0.0830` | 26,960,000.00 USD | 26,960,000.00 USD | 0.00 USD | 140,600.00 USD | 84,690.00 USD | 98,250.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 27,030,000.00 USD | 27,030,000.00 USD | 0.00 USD | 39,850.00 USD | 0.00 USD | 24,360.00 USD |
| `1D` | `0.0832` | 27,340,000.00 USD | 27,340,000.00 USD | 0.00 USD | 171,130.00 USD | 66,230.00 USD | 80,110.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 27,680,000.00 USD | 27,680,000.00 USD | 0.00 USD | 119,590.00 USD | 55,260.00 USD | 165,680.00 USD |
| `1D` | `0.0834` | 28,030,000.00 USD | 28,030,000.00 USD | 0.00 USD | 127,020.00 USD | 94,190.00 USD | 126,700.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 28,380,000.00 USD | 28,380,000.00 USD | 0.00 USD | 104,680.00 USD | 176,580.00 USD | 65,050.00 USD |
| `1D` | `0.0836` | 28,640,000.00 USD | 28,640,000.00 USD | 0.00 USD | 48,890.00 USD | 63,220.00 USD | 144,680.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 28,850,000.00 USD | 28,850,000.00 USD | 0.00 USD | 129,000.00 USD | 30,430.00 USD | 51,350.00 USD |
| `1D` | `0.0838` | 29,120,000.00 USD | 29,120,000.00 USD | 0.00 USD | 168,220.00 USD | 70,030.00 USD | 38,860.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 29,210,000.00 USD | 29,210,000.00 USD | 0.00 USD | 52,570.00 USD | 16,550.00 USD | 15,430.00 USD |
| `1D` | `0.0840` | 29,270,000.00 USD | 29,270,000.00 USD | 0.00 USD | 13,720.00 USD | 15,480.00 USD | 28,470.00 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0841` | 29,290,000.00 USD | 29,290,000.00 USD | 0.00 USD | 23,380.00 USD | 2,010.00 USD | 1,220.00 USD |
| `1D` | `0.0842` | 29,360,000.00 USD | 29,360,000.00 USD | 0.00 USD | 22,710.00 USD | 0.00 USD | 46,530.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 29,400,000.00 USD | 29,400,000.00 USD | 0.00 USD | 33,600.00 USD | 0.00 USD | 634.86 USD |
| `1D` | `0.0844` | 29,470,000.00 USD | 29,470,000.00 USD | 0.00 USD | 79,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0845` | 29,490,000.00 USD | 29,490,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | 264.53 USD |
| `1D` | `0.0846` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 72,340.00 USD | 16,670.00 USD | 0.00 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0847` | 29,590,000.00 USD | 29,590,000.00 USD | 0.00 USD | 11,040.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `1.05B` | Total OI Tokens: `13,887,062,823.7 DOGE`
  * 1h OI Change: `+0.79%` | 4h OI Change: `-1.53%` | 24h OI Change: `-5.59%`
  * Exchange Breakdown: Binance=`244.49M` | Bybit=`106.57M` | OKX=`110.00M` | Hyperliquid=`76.30M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-5.02K` | Last 24h: `35.55K` | Last 3d: `229.21K` | Last 7d: `310.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0005%` | **USDT OKX** | `-0.0057%` |
| **USDT Bybit** | `-0.0028%` | **USDT KuCoin** | `-0.0113%` |
| **USDT MEXC** | `0.0003%` | **USDT BingX** | `0.0019%` |
| **USDT Gate** | `0.0062%` | **USDT Bitget** | `-0.0018%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `57.89%` | `42.11%` | `1.37` | 15,750,000.00 USD |
| `15M` | `Binance` | `60.1%` | `39.9%` | `1.51` | 6,420,000.00 USD |
| `15M` | `OKX` | `61.16%` | `38.84%` | `1.57` | 3,500,000.00 USD |
| `15M` | `Bybit` | `61.97%` | `38.03%` | `1.63` | 1,330,000.00 USD |
| `15M` | `KuCoin` | `11.11%` | `88.89%` | `0.12` | 441,130.00 USD |
| `15M` | `Gate` | `50.29%` | `49.71%` | `1.01` | 1,690,000.00 USD |
| `15M` | `Bitget` | `50.66%` | `49.34%` | `1.03` | 312,420.00 USD |
| `15M` | `BingX` | `60.2%` | `39.8%` | `1.51` | 165,740.00 USD |
| `15M` | `MEXC` | `42.7%` | `57.3%` | `0.75` | 307,540.00 USD |
| `15M` | `Bitunix` | `63.61%` | `36.39%` | `1.75` | 455,420.00 USD |
| `15M` | `Hyperliquid` | `80.66%` | `19.34%` | `4.17` | 656,250.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.36%` | `43.64%` | `1.29` | 53,320.00 USD |
| `15M` | `Crypto.com` | `41.52%` | `58.48%` | `0.71` | 28,540.00 USD |
| `15M` | `WhiteBIT` | `30.02%` | `69.98%` | `0.43` | 157,380.00 USD |
| `15M` | `HTX` | `44.16%` | `55.84%` | `0.79` | 124,790.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `42.47%` | `57.53%` | `0.74` | 117,360.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.83%` | `55.17%` | `0.81` | 4,390.00 USD |
| `15M` | `Whale Positions` | `60.1%` | `39.9%` | `1.51` | 6,420,000.00 USD |
| `15M` | `Global Accounts` | `57.89%` | `42.11%` | `1.37` | 15,750,000.00 USD |
| `1H` | `DOGE` | `52.39%` | `47.61%` | `1.10` | 46,990,000.00 USD |
| `1H` | `Binance` | `54.38%` | `45.62%` | `1.19` | 19,460,000.00 USD |
| `1H` | `OKX` | `53.71%` | `46.29%` | `1.16` | 9,400,000.00 USD |
| `1H` | `Bybit` | `53.6%` | `46.4%` | `1.16` | 3,560,000.00 USD |
| `1H` | `KuCoin` | `26%` | `74%` | `0.35` | 611,100.00 USD |
| `1H` | `Gate` | `54.42%` | `45.58%` | `1.19` | 6,710,000.00 USD |
| `1H` | `Bitget` | `68.97%` | `31.03%` | `2.22` | 1,110,000.00 USD |
| `1H` | `BingX` | `56.86%` | `43.14%` | `1.32` | 616,210.00 USD |
| `1H` | `MEXC` | `20.91%` | `79.09%` | `0.26` | 1,590,000.00 USD |
| `1H` | `Bitunix` | `45.57%` | `54.43%` | `0.84` | 1,670,000.00 USD |
| `1H` | `Hyperliquid` | `68.18%` | `31.82%` | `2.14` | 873,200.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.95%` | `50.05%` | `1.00` | 187,950.00 USD |
| `1H` | `Crypto.com` | `51.25%` | `48.75%` | `1.05` | 66,120.00 USD |
| `1H` | `WhiteBIT` | `9.93%` | `90.07%` | `0.11` | 478,740.00 USD |
| `1H` | `HTX` | `45.42%` | `54.58%` | `0.83` | 353,950.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `28.97%` | `71.03%` | `0.41` | 18,540.00 USD |
| `1H` | `Aster` | `45.84%` | `54.16%` | `0.85` | 274,850.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `24.93%` | `75.07%` | `0.33` | 19,770.00 USD |
| `1H` | `Whale Positions` | `54.38%` | `45.62%` | `1.19` | 19,460,000.00 USD |
| `1H` | `Global Accounts` | `52.39%` | `47.61%` | `1.10` | 46,990,000.00 USD |
| `4H` | `DOGE` | `48.55%` | `51.45%` | `0.94` | 852,140,000.00 USD |
| `4H` | `Binance` | `48.53%` | `51.47%` | `0.94` | 540,090,000.00 USD |
| `4H` | `OKX` | `46.48%` | `53.52%` | `0.87` | 71,760,000.00 USD |
| `4H` | `Bybit` | `53.14%` | `46.86%` | `1.13` | 60,050,000.00 USD |
| `4H` | `KuCoin` | `55.28%` | `44.72%` | `1.24` | 4,690,000.00 USD |
| `4H` | `Gate` | `47.38%` | `52.62%` | `0.90` | 21,570,000.00 USD |
| `4H` | `Bitget` | `49.72%` | `50.28%` | `0.99` | 16,490,000.00 USD |
| `4H` | `BingX` | `39.2%` | `60.8%` | `0.64` | 13,310,000.00 USD |
| `4H` | `MEXC` | `52.37%` | `47.63%` | `1.10` | 9,910,000.00 USD |
| `4H` | `Bitunix` | `50.76%` | `49.24%` | `1.03` | 20,060,000.00 USD |
| `4H` | `Hyperliquid` | `49.78%` | `50.22%` | `0.99` | 51,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.29%` | `50.71%` | `0.97` | 5,420,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `26.8%` | `73.2%` | `0.37` | 654,790.00 USD |
| `4H` | `HTX` | `43.44%` | `56.56%` | `0.77` | 2,600,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `62.36%` | `37.64%` | `1.66` | 2,970,000.00 USD |
| `4H` | `Aster` | `47.95%` | `52.05%` | `0.92` | 22,520,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `30.56%` | `69.44%` | `0.44` | 9,030,000.00 USD |
| `4H` | `Whale Positions` | `48.53%` | `51.47%` | `0.94` | 540,090,000.00 USD |
| `4H` | `Global Accounts` | `48.55%` | `51.45%` | `0.94` | 852,140,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0740` | `0.0741` | `0.0740` | `0.0745` | `0.0738` | 9,556,878.93 USD | 5,124,624.51 USD | 4,432,254.42 USD | 692,370.09 USD | `+7.24%` | `10B / 10S` |
| `0:00 UTC` | `0.0744` | `0.0740` | `0.0744` | `0.0745` | `0.0733` | 8,985,417.81 USD | 4,020,216.59 USD | 4,965,201.22 USD | -944,984.63 USD | `-10.52%` | `10B / 15S` |
| `5:00 UTC` | `0.0739` | `0.0740` | `0.0739` | `0.0743` | `0.0738` | 4,177,023.31 USD | 1,948,188.05 USD | 2,228,835.27 USD | -280,647.22 USD | `-6.72%` | `6B / 5S` |
| `0:00 UTC` | `0.0737` | `0.0739` | `0.0737` | `0.0743` | `0.0736` | 6,164,268.63 USD | 2,938,067.77 USD | 3,226,200.86 USD | -288,133.08 USD | `-4.67%` | `9B / 6S` |
| `5:00 UTC` | `0.0749` | `0.0747` | `0.0749` | `0.0751` | `0.0743` | 6,484,284.24 USD | 3,589,529.58 USD | 2,894,754.66 USD | 694,774.91 USD | `+10.71%` | `19B / 5S` |
| `0:00 UTC` | `0.0749` | `0.0750` | `0.0749` | `0.0752` | `0.0748` | 6,915,504.04 USD | 3,908,951.74 USD | 3,006,552.30 USD | 902,399.44 USD | `+13.05%` | `6B / 3S` |
| `5:00 UTC` | `0.0749` | `0.0749` | `0.0749` | `0.0752` | `0.0748` | 4,286,041.88 USD | 2,098,889.29 USD | 2,187,152.59 USD | -88,263.30 USD | `-2.06%` | `4B / 13S` |
| `0:00 UTC` | `0.0751` | `0.0751` | `0.0751` | `0.0752` | `0.0749` | 4,647,855.36 USD | 2,795,154.23 USD | 1,852,701.13 USD | 942,453.10 USD | `+20.28%` | `6B / 2S` |
| `5:00 UTC` | `0.0753` | `0.0752` | `0.0753` | `0.0754` | `0.0750` | 3,128,035.72 USD | 1,829,490.22 USD | 1,298,545.51 USD | 530,944.71 USD | `+16.97%` | `7B / 3S` |
| `0:00 UTC` | `0.0755` | `0.0755` | `0.0755` | `0.0756` | `0.0754` | 1,122,878.46 USD | 704,120.64 USD | 418,757.81 USD | 285,362.83 USD | `+25.41%` | `4B / 1S` |

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
| `5m` | 125,090.00 USD | 836,150.00 USD | **`ACCUMULATION`** |
| `15m` | 497,430.00 USD | 1,750,000.00 USD | **`ACCUMULATION`** |
| `30m` | 536,280.00 USD | 2,220,000.00 USD | **`ACCUMULATION`** |
| `1h` | 1,590,000.00 USD | 4,130,000.00 USD | **`ACCUMULATION`** |
| `2h` | 2,450,000.00 USD | 4,220,000.00 USD | **`ACCUMULATION`** |
| `4h` | -7,490,000.00 USD | -20,770,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -8,480,000.00 USD | -19,020,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -18,450,000.00 USD | -53,290,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -21,550,000.00 USD | -55,450,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -18,600,000.00 USD | -60,750,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -60,150,000.00 USD | -187,170,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -285,660,000.00 USD | -794,690,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+125.09K` | 15m=`+497.43K` | 1h=`+1.59M` | 24h=`-18.60M`
* Futures Capital Netflows: 5m=`+836.15K` | 15m=`+1.75M` | 1h=`+4.13M` | 24h=`-60.75M`
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
  * `2026-10-30 08:34:50 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:50 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:02:50 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:02:50 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:01:50 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:03:50 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:03:50 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:03:50 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0731` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0691` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0836`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0757` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0797` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0652`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0763`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
