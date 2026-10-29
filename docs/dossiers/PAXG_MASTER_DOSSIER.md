# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 03:19:13 IST` (`2026-10-29 21:49:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4021.40` | **Live Ask Quote**: `4021.59` | **Mid Price**: `4021.49`
- **Spread Points**: `19.00` | **Spread BPS**: `0.47 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `4029.58` | VWAP Z-Score: `-0.61` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.86` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.06` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.67` | Lower -3.00σ Band: `3994.49`
  * Upper +2.51σ Band: `4058.94` | Lower -2.51σ Band: `4000.22`
  * Upper +2.01σ Band: `4053.09` | Lower -2.01σ Band: `4006.07`
  * Upper +2.00σ Band: `4052.97` | Lower -2.00σ Band: `4006.19`
  * Upper +1.28σ Band: `4044.55` | Lower -1.28σ Band: `4014.61`
  * Upper +1.00σ Band: `4041.28` | Lower -1.00σ Band: `4017.88`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4020.13` | EMA-20=`4019.02` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4023.17` (Slope: `+0.0000`) | EMA-100=`4029.33`
  * Institutional Anchors: EMA-144=`4031.17` | EMA-200=`4031.48` (Slope: `-0.0489`) | EMA-233=`4030.83`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4039.67` (Distance: `-0.45%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.14%`)
  * Value Area Low (VAL) = `4016.67` (Distance: `+0.12%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4005.41` - `4037.58`
  * Optimal Trade Entry (OTE 0.705): `4029.54`
  * Structural Invalidation Anchor (0.786): `4053.67`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4019.11` | `4020.53` | `4019.11` | `4019.81` | `39` | 157,838.63 USD | 36,053.33 USD | `+22.84%` | 1,536,398.67 USD | `+0.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4019.81` | `4020.73` | `4019.80` | `4020.73` | `38` | 153,014.15 USD | 55,099.69 USD | `+36.01%` | 1,591,498.36 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4020.72` | `4023.84` | `4020.00` | `4020.01` | `115` | 462,998.83 USD | 188,288.82 USD | `+40.67%` | 1,779,787.18 USD | `+1.63` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4021.37` | `4022.18` | `4017.98` | `4020.96` | `230` | 924,323.44 USD | 24,555.35 USD | `+2.66%` | 1,622,022.93 USD | `-0.02` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4020.96` | `4024.66` | `4018.45` | `4019.12` | `146` | 586,168.49 USD | -121,677.59 USD | `-20.76%` | 1,500,345.34 USD | `-0.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4019.11` | `4023.84` | `4019.11` | `4020.01` | `192` | 773,851.60 USD | 279,441.84 USD | `+36.11%` | 1,779,787.18 USD | `+0.86` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4017.56` | `4025.99` | `4014.71` | `4025.60` | `520` | 2,091,733.78 USD | -652,688.52 USD | `-31.20%` | 1,838,471.59 USD | `-1.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4025.61` | `4033.50` | `4020.69` | `4021.36` | `1,040` | 4,187,720.97 USD | -239,141.91 USD | `-5.71%` | 1,599,329.68 USD | `-0.58` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4021.37` | `4024.66` | `4017.98` | `4020.01` | `568` | 2,284,391.78 USD | 182,367.84 USD | `+7.98%` | 1,781,697.53 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.98` | `4020.01` | `1,608` | 6,472,112.75 USD | -56,774.07 USD | `-0.88%` | 1,190,373.26 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.98` | `4020.01` | `1,608` | 6,472,112.75 USD | -56,774.07 USD | `-0.88%` | 1,190,373.26 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `BID` | `4016.60` | `4.0056` | 16,088.89 USD | 220,299.59 USD | `3 orders` | `-0.07%` | `-` |
| `BID` | `4016.70` | `0.0547` | 219.71 USD | 204,210.70 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `4016.80` | `0.9336` | 3,750.08 USD | 203,990.98 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `4016.90` | `0.9669` | 3,883.94 USD | 200,240.90 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `4017.00` | `1.9263` | 7,737.95 USD | 196,356.96 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `4017.20` | `6.6470` | 26,702.33 USD | 188,619.01 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4017.40` | `3.5177` | 14,132.01 USD | 161,916.68 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4017.50` | `1.4661` | 5,890.06 USD | 147,784.67 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4017.60` | `3.3297` | 13,377.40 USD | 141,894.62 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4017.70` | `0.9667` | 3,883.91 USD | 128,517.21 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4017.80` | `1.9833` | 7,968.50 USD | 124,633.30 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4017.90` | `11.9292` | 47,930.33 USD | 116,664.80 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4018.00` | `1.6387` | 6,584.30 USD | 68,734.47 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4018.20` | `1.6354` | 6,571.36 USD | 62,150.17 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4018.30` | `2.4261` | 9,748.80 USD | 55,578.81 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4018.40` | `1.0345` | 4,157.03 USD | 45,830.01 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4018.50` | `3.2536` | 13,074.59 USD | 41,672.97 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4018.60` | `0.7186` | 2,887.77 USD | 28,598.38 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4018.80` | `0.8865` | 3,562.67 USD | 25,710.62 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4019.30` | `5.5104` | 22,147.95 USD | 22,147.95 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4019.35` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,019.35` | `0.00%` | `-` |
| `ASK` | `4019.40` | `5.5641` | 22,364.34 USD | 22,364.34 USD | `7 orders` | `+0.00%` | `-` |
| `ASK` | `4019.50` | `3.5598` | 14,308.62 USD | 36,672.96 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `4019.70` | `2.8545` | 11,474.23 USD | 48,147.19 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4019.80` | `1.8785` | 7,551.19 USD | 55,698.39 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4019.90` | `3.6619` | 14,720.47 USD | 70,418.86 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4020.00` | `3.8432` | 15,449.66 USD | 85,868.52 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4020.10` | `0.3838` | 1,542.91 USD | 87,411.44 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4020.20` | `5.4050` | 21,729.18 USD | 109,140.62 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4020.30` | `2.1722` | 8,732.90 USD | 117,873.51 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4020.40` | `2.7395` | 11,013.89 USD | 128,887.40 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4020.50` | `13.6688` | 54,955.41 USD | 183,842.81 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4020.60` | `1.6901` | 6,795.22 USD | 190,638.03 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4020.70` | `3.1140` | 12,520.46 USD | 203,158.49 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4020.90` | `4.0704` | 16,366.67 USD | 219,525.16 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4021.10` | `4.3531` | 17,504.25 USD | 237,029.41 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4021.20` | `9.1680` | 36,866.36 USD | 273,895.77 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4021.30` | `11.8702` | 47,733.64 USD | 321,629.41 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4021.50` | `12.1609` | 48,905.06 USD | 370,534.46 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4021.60` | `0.0027` | 10.86 USD | 370,545.32 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `4021.70` | `1.8533` | 7,453.42 USD | 377,998.74 USD | `2 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:15:37 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x5b5d...c060` | `SHORT` | 25,584,383.89 USD | `6,365.38` | `4188.90` | `4019.30` | `32458.22` | 1,079,587.40 USD | `+4.22%` | `4X Cross` |
| `53` | `0x4692...164f` | `SHORT` | 25,405,980.83 USD | `6,321.00` | `4133.07` | `4019.30` | `13690.64` | 719,192.96 USD | `+2.83%` | `5X Cross` |
| `68` | `0xb83d...6e36` | `SHORT` | 23,593,473.65 USD | `5,869.90` | `4228.86` | `4019.30` | `29949.09` | 1,229,548.29 USD | `+5.21%` | `5X Cross` |
| `96` | `0xec0b...b078` | `LONG` | 19,408,825.50 USD | `4,828.91` | `4157.43` | `4019.30` | `2225.72` | -667,056.81 USD | `-3.44%` | `25X Cross` |
| `142` | `0x645b...87b8` | `LONG` | 14,200,270.90 USD | `3,533.02` | `4129.12` | `4019.30` | `399.28` | -388,006.40 USD | `-2.73%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,135,929.31 USD | `3,268.21` | `4228.94` | `4019.30` | `4395.59` | 685,149.82 USD | `+5.22%` | `25X Cross` |
| `178` | `0xa742...e390` | `SHORT` | 11,655,970.40 USD | `2,900.00` | `4364.92` | `4019.30` | `4235.67` | 1,002,305.93 USD | `+8.60%` | `20X Cross` |
| `261` | `0xfc66...ca06` | `SHORT` | 8,983,644.38 USD | `2,235.07` | `4031.28` | `4019.30` | `22250.67` | 26,568.26 USD | `+0.30%` | `3X Cross` |
| `265` | `0x3678...b209` | `LONG` | 8,842,680.00 USD | `2,200.00` | `4176.09` | `4019.30` | `2592.51` | -344,739.30 USD | `-3.90%` | `25X Cross` |
| `266` | `0x41e5...0825` | `SHORT` | 8,842,460.00 USD | `2,200.00` | `4112.20` | `4019.30` | `4331.15` | 204,394.59 USD | `+2.31%` | `20X Cross` |
| `303` | `0xacb6...efbd` | `SHORT` | 7,939,601.02 USD | `1,975.37` | `4048.55` | `4019.30` | `6496.64` | 57,790.69 USD | `+0.73%` | `6X Cross` |
| `374` | `0xc26c...b8f4` | `LONG` | 6,350,458.26 USD | `1,579.95` | `4075.62` | `4019.30` | `0.000000` | -88,838.71 USD | `-1.40%` | `1X Cross` |
| `404` | `0x12d2...f97f` | `LONG` | 5,634,968.89 USD | `1,401.94` | `4278.91` | `4019.30` | `3027.54` | -363,821.69 USD | `-6.46%` | `20X Cross` |
| `559` | `0x63da...8add` | `LONG` | 4,019,400.00 USD | `1,000.00` | `4021.46` | `4019.30` | `3564.11` | -2,060.96 USD | `-0.05%` | `25X Cross` |
| `572` | `0x354b...6425` | `LONG` | 3,970,006.50 USD | `987.74` | `4031.85` | `4019.30` | `0.000000` | -12,400.84 USD | `-0.31%` | `10X Cross` |
| `583` | `0x9aa5...58af` | `LONG` | 3,905,320.69 USD | `971.64` | `4279.98` | `4019.30` | `0.000000` | -253,288.39 USD | `-6.49%` | `20X Cross` |
| `610` | `0xf3dc...1672` | `LONG` | 3,740,938.15 USD | `930.74` | `4024.62` | `4019.30` | `3337.59` | -4,954.41 USD | `-0.13%` | `20X Cross` |
| `688` | `0x4a20...3c26` | `LONG` | 3,365,760.61 USD | `837.40` | `4599.73` | `4019.30` | `0.000000` | -486,059.77 USD | `-14.44%` | `20X Cross` |
| `838` | `0x0fac...7a0a` | `LONG` | 2,759,257.81 USD | `686.49` | `4290.34` | `4019.30` | `1439.65` | -186,000.89 USD | `-6.74%` | `25X Cross` |
| `883` | `0xd8c5...99b0` | `SHORT` | 2,581,238.93 USD | `642.35` | `4175.35` | `4019.30` | `32749.31` | 100,822.25 USD | `+3.91%` | `4X Cross` |
| `917` | `0x625e...a354` | `SHORT` | 2,491,842.00 USD | `620.00` | `4122.81` | `4019.30` | `4342.25` | 64,305.03 USD | `+2.58%` | `20X Cross` |
| `943` | `0xeae3...e8ad` | `SHORT` | 2,411,580.00 USD | `600.00` | `4104.77` | `4019.30` | `4325.27` | 51,285.11 USD | `+2.13%` | `20X Cross` |
| `947` | `0xf285...fa82` | `LONG` | 2,403,967.04 USD | `598.11` | `4146.45` | `4019.30` | `3891.24` | -76,052.51 USD | `-3.16%` | `25X Cross` |
| `964` | `0x12f7...8750` | `LONG` | 2,353,745.09 USD | `585.61` | `4082.77` | `4019.30` | `2491.29` | -37,171.89 USD | `-1.58%` | `10X Cross` |
| `1105` | `0x413c...886c` | `LONG` | 2,009,700.00 USD | `500.00` | `4010.43` | `4019.30` | `0.000000` | 4,483.77 USD | `+0.22%` | `2X Cross` |
| `1115` | `0x61ce...a62b` | `SHORT` | 1,999,615.82 USD | `497.50` | `4071.66` | `4019.30` | `4711.19` | 26,052.97 USD | `+1.30%` | `20X Cross` |
| `1118` | `0x0593...40f9` | `LONG` | 1,994,284.22 USD | `496.18` | `4024.57` | `4019.30` | `3701.73` | -2,619.61 USD | `-0.13%` | `10X Isolated` |
| `1198` | `0x2edd...8179` | `LONG` | 1,893,117.35 USD | `470.91` | `4164.68` | `4019.80` | `0.000000` | -68,083.96 USD | `-3.60%` | `10X Cross` |
| `1248` | `0xead5...69f2` | `LONG` | 1,823,893.63 USD | `453.78` | `4220.88` | `4019.30` | `3538.94` | -91,474.43 USD | `-5.02%` | `5X Isolated` |
| `1309` | `0x7a6d...f79c` | `SHORT` | 1,722,169.26 USD | `428.38` | `4136.09` | `4019.80` | `5739.49` | 49,645.75 USD | `+2.88%` | `10X Cross` |
| `1360` | `0x46fc...1195` | `LONG` | 1,654,150.15 USD | `411.55` | `4055.10` | `4019.30` | `2117.41` | -14,735.39 USD | `-0.89%` | `20X Cross` |
| `1395` | `0x6d15...d374` | `LONG` | 1,607,720.00 USD | `400.00` | `4068.25` | `4019.30` | `3841.81` | -19,580.00 USD | `-1.22%` | `25X Cross` |
| `1396` | `0xee02...309d` | `SHORT` | 1,607,720.00 USD | `400.00` | `4438.84` | `4019.30` | `4226.89` | 167,818.60 USD | `+10.44%` | `25X Isolated` |
| `1440` | `0x02a7...fe9f` | `SHORT` | 1,567,566.00 USD | `390.00` | `4055.02` | `4019.30` | `4306.71` | 13,893.25 USD | `+0.89%` | `25X Cross` |
| `1468` | `0x51f6...2b39` | `LONG` | 1,529,593.92 USD | `380.50` | `4234.65` | `4019.80` | `0.000000` | -81,674.36 USD | `-5.34%` | `10X Cross` |
| `1473` | `0x7e77...b8d2` | `SHORT` | 1,527,334.00 USD | `380.00` | `4131.92` | `4019.30` | `4293.51` | 42,795.64 USD | `+2.80%` | `20X Cross` |
| `1495` | `0x72c2...9b37` | `LONG` | 1,499,726.63 USD | `373.13` | `4000.98` | `4019.30` | `3778.04` | 6,833.12 USD | `+0.46%` | `13X Isolated` |
| `1542` | `0xaa44...b844` | `LONG` | 1,446,948.00 USD | `360.00` | `4043.10` | `4019.30` | `2803.26` | -8,569.63 USD | `-0.59%` | `4X Cross` |
| `1543` | `0x781e...96b7` | `SHORT` | 1,445,574.14 USD | `359.61` | `4364.97` | `4019.80` | `13580.94` | 124,126.79 USD | `+8.59%` | `10X Cross` |
| `1650` | `0xa41f...d50a` | `LONG` | 1,322,230.26 USD | `328.96` | `4468.89` | `4019.30` | `3833.19` | -147,867.59 USD | `-11.18%` | `15X Cross` |
| `1667` | `0x49e9...e1d0` | `SHORT` | 1,300,159.95 USD | `323.48` | `4025.23` | `4019.30` | `32230.68` | 1,918.38 USD | `+0.15%` | `4X Cross` |
| `1678` | `0xada6...6f88` | `LONG` | 1,282,977.07 USD | `319.28` | `4166.46` | `4019.30` | `1969.36` | -47,273.44 USD | `-3.68%` | `5X Cross` |
| `1683` | `0xbf5a...88ba` | `SHORT` | 1,276,750.34 USD | `317.65` | `4091.80` | `4019.30` | `9948.79` | 23,032.69 USD | `+1.80%` | `20X Cross` |
| `1723` | `0xff31...ff6c` | `SHORT` | 1,245,983.00 USD | `310.00` | `4372.43` | `4019.30` | `4789.18` | 109,472.38 USD | `+8.79%` | `10X Isolated` |
| `1886` | `0x50e2...d770` | `LONG` | 1,086,714.73 USD | `270.37` | `4243.58` | `4019.30` | `2562.10` | -60,611.73 USD | `-5.58%` | `20X Cross` |
| `1902` | `0x4c92...4f17` | `SHORT` | 1,072,029.71 USD | `266.72` | `4260.98` | `4019.30` | `6520.76` | 64,462.53 USD | `+6.01%` | `20X Cross` |
| `1966` | `0xd346...c4f3` | `LONG` | 1,025,620.05 USD | `255.17` | `4188.66` | `4019.30` | `3310.42` | -43,216.45 USD | `-4.21%` | `5X Isolated` |
| `2003` | `0x1581...463b` | `LONG` | 1,004,850.00 USD | `250.00` | `4003.77` | `4019.30` | `3543.36` | 3,906.41 USD | `+0.39%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4225.80` | 325.39 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.33K USD at 4225.8000 USD [API] | `2026-09-28 01:01:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4110.50` (Vol: 281,800.00 USD, Dist: `+2.05%`) | Long MP=`3936.63` (Vol: 356,200.00 USD, Dist: `--2.27%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.74%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.26%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.72%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.25%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.07%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.60%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,280,000.00 USD | 16,280,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,210,000.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.80` | 3,900,000.00 USD | 3,900,000.00 USD | 31,030.00 USD | 0.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,070,000.00 USD | 16,070,000.00 USD | 45,440.00 USD | 0.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.00` | 3,860,000.00 USD | 3,860,000.00 USD | 67,500.00 USD | 0.00 USD | 7,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 16,010,000.00 USD | 16,010,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.20` | 3,790,000.00 USD | 3,790,000.00 USD | 35,590.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,910,000.00 USD | 15,910,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.40` | 3,750,000.00 USD | 3,750,000.00 USD | 33,620.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,730,000.00 USD | 15,730,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.60` | 3,710,000.00 USD | 3,710,000.00 USD | 41,580.00 USD | 0.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,610,000.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.80` | 3,660,000.00 USD | 3,660,000.00 USD | 17,490.00 USD | 0.00 USD | 9,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,480,000.00 USD | 15,480,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3644.00` | 3,640,000.00 USD | 3,640,000.00 USD | 6,610.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,410,000.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3648.20` | 3,630,000.00 USD | 3,630,000.00 USD | 16,690.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,380,000.00 USD | 15,380,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3652.40` | 3,610,000.00 USD | 3,610,000.00 USD | 20,490.00 USD | 0.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,360,000.00 USD | 15,360,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3656.60` | 3,590,000.00 USD | 3,590,000.00 USD | 5,500.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,330,000.00 USD | 15,330,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3660.80` | 3,580,000.00 USD | 3,580,000.00 USD | 4,080.00 USD | 0.00 USD | 812.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,290,000.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3665.00` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 396.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,270,000.00 USD | 15,270,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,260,000.00 USD | 15,260,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,890,000.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,410,000.00 USD | 14,410,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,880,000.00 USD | 13,880,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.00` | 3,570,000.00 USD | 3,570,000.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,550,000.00 USD | 13,550,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.20` | 3,540,000.00 USD | 3,540,000.00 USD | 78,390.00 USD | 0.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,240,000.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.40` | 3,460,000.00 USD | 3,460,000.00 USD | 140,190.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,960,000.00 USD | 12,960,000.00 USD | 204,080.00 USD | 0.00 USD | 53,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.60` | 3,300,000.00 USD | 3,300,000.00 USD | 193,320.00 USD | 0.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,700,000.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.80` | 3,080,000.00 USD | 3,080,000.00 USD | 153,750.00 USD | 0.00 USD | 23,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,160,000.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.00` | 2,910,000.00 USD | 2,910,000.00 USD | 92,870.00 USD | 0.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,740,000.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.20` | 2,800,000.00 USD | 2,800,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,200,000.00 USD | 11,200,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.40` | 2,650,000.00 USD | 2,650,000.00 USD | 47,790.00 USD | 0.00 USD | 20,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,860,000.00 USD | 10,860,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3887.60` | 2,580,000.00 USD | 2,580,000.00 USD | 15,370.00 USD | 0.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,720,000.00 USD | 10,720,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3891.80` | 2,560,000.00 USD | 2,560,000.00 USD | 68,400.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,610,000.00 USD | 10,610,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3896.00` | 2,480,000.00 USD | 2,480,000.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,480,000.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3900.20` | 2,430,000.00 USD | 2,430,000.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,370,000.00 USD | 10,370,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3904.40` | 2,410,000.00 USD | 2,410,000.00 USD | 24,370.00 USD | 0.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,280,000.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3908.60` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,230,000.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,190,000.00 USD | 10,190,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,170,000.00 USD | 10,170,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,440,000.00 USD | 9,440,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,490,000.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,600,000.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.80` | 2,380,000.00 USD | 2,380,000.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,760,000.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.00` | 2,350,000.00 USD | 2,350,000.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,300,000.00 USD | 6,300,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.20` | 2,170,000.00 USD | 2,170,000.00 USD | 272,030.00 USD | 0.00 USD | 24,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,640,000.00 USD | 5,640,000.00 USD | 417,530.00 USD | 0.00 USD | 73,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.40` | 1,880,000.00 USD | 1,880,000.00 USD | 360,890.00 USD | 0.00 USD | 45,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,150,000.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 119,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.60` | 1,470,000.00 USD | 1,470,000.00 USD | 359,720.00 USD | 0.00 USD | 38,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,180,000.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.80` | 1,070,000.00 USD | 1,070,000.00 USD | 181,840.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.00` | 856,730.00 USD | 856,730.00 USD | 275,140.00 USD | 0.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.20` | 568,300.00 USD | 568,300.00 USD | 108,590.00 USD | 0.00 USD | 50,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.40` | 409,520.00 USD | 409,520.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.60` | 359,430.00 USD | 359,430.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.80` | 264,840.00 USD | 264,840.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3980.00` | 131,870.00 USD | 131,870.00 USD | 53,190.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3984.20` | 64,460.00 USD | 64,460.00 USD | 56,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3988.40` | 8,150.00 USD | 8,150.00 USD | 2,110.00 USD | 0.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4093.40` | 12,130.00 USD | 12,130.00 USD | 5,620.00 USD | 0.00 USD | 6,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4097.60` | 183,330.00 USD | 183,330.00 USD | 163,880.00 USD | 0.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.80` | 404,110.00 USD | 404,110.00 USD | 200,400.00 USD | 0.00 USD | 20,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,830,000.00 USD | 4,830,000.00 USD | 330,140.00 USD | 0.00 USD | 69,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.00` | 853,570.00 USD | 853,570.00 USD | 408,710.00 USD | 0.00 USD | 40,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,480,000.00 USD | 5,480,000.00 USD | 547,190.00 USD | 0.00 USD | 101,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.20` | 1,150,000.00 USD | 1,150,000.00 USD | 252,410.00 USD | 0.00 USD | 44,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.40` | 1,450,000.00 USD | 1,450,000.00 USD | 269,460.00 USD | 0.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,350,000.00 USD | 7,350,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.60` | 1,640,000.00 USD | 1,640,000.00 USD | 171,150.00 USD | 0.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,360,000.00 USD | 8,360,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.80` | 1,930,000.00 USD | 1,930,000.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.00` | 2,020,000.00 USD | 2,020,000.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,120,000.00 USD | 9,120,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.20` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.40` | 2,180,000.00 USD | 2,180,000.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.60` | 2,290,000.00 USD | 2,290,000.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.80` | 2,330,000.00 USD | 2,330,000.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.00` | 2,380,000.00 USD | 2,380,000.00 USD | 48,740.00 USD | 0.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4152.20` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,280,000.00 USD | 11,280,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4173.20` | 2,390,000.00 USD | 2,390,000.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.40` | 2,470,000.00 USD | 2,470,000.00 USD | 76,990.00 USD | 0.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,390,000.00 USD | 12,390,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.60` | 2,570,000.00 USD | 2,570,000.00 USD | 96,270.00 USD | 0.00 USD | 9,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,540,000.00 USD | 12,540,000.00 USD | 133,800.00 USD | 0.00 USD | 24,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.80` | 2,730,000.00 USD | 2,730,000.00 USD | 142,450.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,870,000.00 USD | 12,870,000.00 USD | 270,030.00 USD | 0.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.00` | 2,910,000.00 USD | 2,910,000.00 USD | 153,150.00 USD | 0.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,480,000.00 USD | 13,480,000.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4194.20` | 3,090,000.00 USD | 3,090,000.00 USD | 164,460.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,800,000.00 USD | 13,800,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4198.40` | 3,150,000.00 USD | 3,150,000.00 USD | 52,550.00 USD | 0.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,240,000.00 USD | 14,240,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4202.60` | 3,310,000.00 USD | 3,310,000.00 USD | 142,710.00 USD | 0.00 USD | 14,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,580,000.00 USD | 14,580,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.80` | 3,370,000.00 USD | 3,370,000.00 USD | 41,800.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4211.00` | 3,400,000.00 USD | 3,400,000.00 USD | 18,450.00 USD | 0.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4215.20` | 3,450,000.00 USD | 3,450,000.00 USD | 45,970.00 USD | 0.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,940,000.00 USD | 14,940,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4219.40` | 3,510,000.00 USD | 3,510,000.00 USD | 54,090.00 USD | 0.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,040,000.00 USD | 15,040,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4223.60` | 3,540,000.00 USD | 3,540,000.00 USD | 26,600.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,150,000.00 USD | 15,150,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4227.80` | 3,570,000.00 USD | 3,570,000.00 USD | 28,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,190,000.00 USD | 15,190,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4232.00` | 3,570,000.00 USD | 3,570,000.00 USD | 1,060.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,260,000.00 USD | 15,260,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,460,000.00 USD | 15,460,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,610,000.00 USD | 15,610,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,810,000.00 USD | 15,810,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.80` | 3,590,000.00 USD | 3,590,000.00 USD | 12,730.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,940,000.00 USD | 15,940,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4421.00` | 3,620,000.00 USD | 3,620,000.00 USD | 27,270.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4425.20` | 3,650,000.00 USD | 3,650,000.00 USD | 32,100.00 USD | 0.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,040,000.00 USD | 16,040,000.00 USD | 40,010.00 USD | 0.00 USD | 11,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4429.40` | 3,710,000.00 USD | 3,710,000.00 USD | 53,770.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,150,000.00 USD | 16,150,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.60` | 3,750,000.00 USD | 3,750,000.00 USD | 35,840.00 USD | 0.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4437.80` | 3,780,000.00 USD | 3,780,000.00 USD | 24,810.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4438.40` | 3,790,000.00 USD | 3,790,000.00 USD | 4,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,540,000.00 USD | 16,540,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,560,000.00 USD | 16,560,000.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.30` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.80` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 31,030.00 USD | 0.00 USD | 3,350.00 USD |
| `7D` | `3619.70` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 45,440.00 USD | 0.00 USD | 12,060.00 USD |
| `1D` | `3623.00` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 67,500.00 USD | 0.00 USD | 7,890.00 USD |
| `7D` | `3623.90` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3627.20` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 35,590.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `3628.10` | 15,910,000.00 USD | 0.00 USD | 15,910,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3631.40` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 33,620.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3632.30` | 15,730,000.00 USD | 0.00 USD | 15,730,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3635.60` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 41,580.00 USD | 0.00 USD | 1,950.00 USD |
| `7D` | `3636.50` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3639.80` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 17,490.00 USD | 0.00 USD | 9,120.00 USD |
| `7D` | `3640.70` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3644.00` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 6,610.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `3644.90` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3648.20` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 16,690.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `3649.10` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3652.40` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 20,490.00 USD | 0.00 USD | 1,280.00 USD |
| `7D` | `3653.30` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3656.60` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 5,500.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `1D` | `3660.80` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 4,080.00 USD | 0.00 USD | 812.11 USD |
| `7D` | `3661.70` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3665.00` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 396.25 USD |
| `7D` | `3665.90` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3854.00` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `3854.90` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3858.20` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 78,390.00 USD | 0.00 USD | 5,560.00 USD |
| `7D` | `3859.10` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD |
| `1D` | `3862.40` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 140,190.00 USD | 0.00 USD | 13,730.00 USD |
| `7D` | `3863.30` | 12,960,000.00 USD | 0.00 USD | 12,960,000.00 USD | 204,080.00 USD | 0.00 USD | 53,800.00 USD |
| `1D` | `3866.60` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 193,320.00 USD | 0.00 USD | 25,080.00 USD |
| `7D` | `3867.50` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3870.80` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 153,750.00 USD | 0.00 USD | 23,090.00 USD |
| `7D` | `3871.70` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3875.00` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 92,870.00 USD | 0.00 USD | 10,410.00 USD |
| `7D` | `3875.90` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3879.20` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD |
| `7D` | `3880.10` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3883.40` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 47,790.00 USD | 0.00 USD | 20,890.00 USD |
| `7D` | `3884.30` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3887.60` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 15,370.00 USD | 0.00 USD | 9,490.00 USD |
| `7D` | `3888.50` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3891.80` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 68,400.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3892.70` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3896.00` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD |
| `7D` | `3896.90` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3900.20` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3901.10` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3904.40` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 24,370.00 USD | 0.00 USD | 1,200.00 USD |
| `7D` | `3905.30` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `3908.60` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3909.50` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3933.80` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3934.70` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.00` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD |
| `7D` | `3938.90` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3942.20` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 272,030.00 USD | 0.00 USD | 24,730.00 USD |
| `7D` | `3943.10` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 417,530.00 USD | 0.00 USD | 73,100.00 USD |
| `1D` | `3946.40` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 360,890.00 USD | 0.00 USD | 45,790.00 USD |
| `7D` | `3947.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 119,280.00 USD |
| `1D` | `3950.60` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 359,720.00 USD | 0.00 USD | 38,900.00 USD |
| `7D` | `3951.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3954.80` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 181,840.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3959.00` | 856,730.00 USD | 0.00 USD | 856,730.00 USD | 275,140.00 USD | 0.00 USD | 13,290.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3963.20` | 568,300.00 USD | 0.00 USD | 568,300.00 USD | 108,590.00 USD | 0.00 USD | 50,190.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3967.40` | 409,520.00 USD | 0.00 USD | 409,520.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.60` | 359,430.00 USD | 0.00 USD | 359,430.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.80` | 264,840.00 USD | 0.00 USD | 264,840.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3980.00` | 131,870.00 USD | 0.00 USD | 131,870.00 USD | 53,190.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3984.20` | 64,460.00 USD | 0.00 USD | 64,460.00 USD | 56,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `1D` | `3988.40` | 8,150.00 USD | 0.00 USD | 8,150.00 USD | 2,110.00 USD | 0.00 USD | 6,040.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4020.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4020.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `1D` | `4093.40` | 12,130.00 USD | 12,130.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | 6,500.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4097.60` | 183,330.00 USD | 183,330.00 USD | 0.00 USD | 163,880.00 USD | 0.00 USD | 7,310.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4101.80` | 404,110.00 USD | 404,110.00 USD | 0.00 USD | 200,400.00 USD | 0.00 USD | 20,380.00 USD |
| `7D` | `4102.70` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 69,830.00 USD |
| `1D` | `4106.00` | 853,570.00 USD | 853,570.00 USD | 0.00 USD | 408,710.00 USD | 0.00 USD | 40,760.00 USD |
| `7D` | `4106.90` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 547,190.00 USD | 0.00 USD | 101,580.00 USD |
| `1D` | `4110.20` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 252,410.00 USD | 0.00 USD | 44,680.00 USD |
| `7D` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4114.40` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 269,460.00 USD | 0.00 USD | 30,900.00 USD |
| `7D` | `4115.30` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4118.60` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 171,150.00 USD | 0.00 USD | 15,360.00 USD |
| `7D` | `4119.50` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4122.80` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4127.00` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD |
| `7D` | `4127.90` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4131.20` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.40` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.60` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.80` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4148.00` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 48,740.00 USD | 0.00 USD | 1,210.00 USD |
| `7D` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `1D` | `4152.20` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD |
| `7D` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `1D` | `4173.20` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD |
| `7D` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4177.40` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 76,990.00 USD | 0.00 USD | 4,760.00 USD |
| `7D` | `4178.30` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4181.60` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 96,270.00 USD | 0.00 USD | 9,390.00 USD |
| `7D` | `4182.50` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 24,870.00 USD |
| `1D` | `4185.80` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 14,290.00 USD |
| `7D` | `4186.70` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 270,030.00 USD | 0.00 USD | 54,580.00 USD |
| `1D` | `4190.00` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 153,150.00 USD | 0.00 USD | 24,710.00 USD |
| `7D` | `4190.90` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4194.20` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 164,460.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `4195.10` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4198.40` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 52,550.00 USD | 0.00 USD | 9,760.00 USD |
| `7D` | `4199.30` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4202.60` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 142,710.00 USD | 0.00 USD | 14,280.00 USD |
| `7D` | `4203.50` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4206.80` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 41,800.00 USD | 0.00 USD | 18,160.00 USD |
| `7D` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4211.00` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 18,450.00 USD | 0.00 USD | 7,770.00 USD |
| `7D` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4215.20` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 45,970.00 USD | 0.00 USD | 5,710.00 USD |
| `7D` | `4216.10` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4219.40` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 54,090.00 USD | 0.00 USD | 4,850.00 USD |
| `7D` | `4220.30` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4223.60` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 26,600.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4224.50` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4227.80` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 28,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4228.70` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4232.00` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4416.80` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 12,730.00 USD | 0.00 USD | 2,280.00 USD |
| `7D` | `4417.70` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4421.00` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 27,270.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4425.20` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 32,100.00 USD | 0.00 USD | 3,670.00 USD |
| `7D` | `4426.10` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 11,470.00 USD |
| `1D` | `4429.40` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 53,770.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4430.30` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4433.60` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 35,840.00 USD | 0.00 USD | 5,230.00 USD |
| `7D` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `4437.80` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 24,810.00 USD | 0.00 USD | 5,770.00 USD |
| `1D` | `4438.40` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 4,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.77M` | Total OI Tokens: `68,348.3 PAXG`
  * 1h OI Change: `-0.09%` | 4h OI Change: `+0.03%` | 24h OI Change: `+0.17%`
  * Exchange Breakdown: Binance=`107.23M` | Bybit=`19.97M` | OKX=`-` | Hyperliquid=`24.63M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.36K` | Last 24h: `25.45K` | Last 3d: `95.42K` | Last 7d: `223.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `47.70%` | `52.30%` | `0.91` | 3,200,000.00 USD |
| `15M` | `Binance` | `45.43%` | `54.57%` | `0.83` | 1,460,000.00 USD |
| `15M` | `OKX` | `44.74%` | `55.26%` | `0.81` | 288,970.00 USD |
| `15M` | `Bybit` | `51.7%` | `48.3%` | `1.07` | 437,750.00 USD |
| `15M` | `KuCoin` | `53.75%` | `46.25%` | `1.16` | 187,260.00 USD |
| `15M` | `Gate` | `50.86%` | `49.14%` | `1.04` | 46,430.00 USD |
| `15M` | `Bitget` | `74.06%` | `25.94%` | `2.86` | 169,370.00 USD |
| `15M` | `BingX` | `42.58%` | `57.42%` | `0.74` | 145,200.00 USD |
| `15M` | `MEXC` | `47.69%` | `52.31%` | `0.91` | 85,920.00 USD |
| `15M` | `Bitunix` | `50.04%` | `49.96%` | `1.00` | 42,700.00 USD |
| `15M` | `Hyperliquid` | `19.95%` | `80.05%` | `0.25` | 118,270.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.29%` | `50.71%` | `0.97` | 79,550.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `43.91%` | `56.09%` | `0.78` | 109,320.00 USD |
| `15M` | `HTX` | `0.13%` | `99.87%` | `0.00` | 100.44 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `88.71%` | `11.29%` | `7.86` | 15,560.00 USD |
| `15M` | `Aster` | `98.75%` | `1.25%` | `79.00` | 6,490.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `21.53%` | `78.47%` | `0.27` | 3,440.00 USD |
| `15M` | `Whale Positions` | `45.43%` | `54.57%` | `0.83` | 1,460,000.00 USD |
| `15M` | `Global Accounts` | `47.70%` | `52.30%` | `0.91` | 3,200,000.00 USD |
| `1H` | `PAXG` | `51.51%` | `48.49%` | `1.06` | 27,430,000.00 USD |
| `1H` | `Binance` | `49.4%` | `50.6%` | `0.98` | 11,520,000.00 USD |
| `1H` | `OKX` | `52.74%` | `47.26%` | `1.12` | 4,060,000.00 USD |
| `1H` | `Bybit` | `53.85%` | `46.15%` | `1.17` | 4,860,000.00 USD |
| `1H` | `KuCoin` | `50.57%` | `49.43%` | `1.02` | 796,420.00 USD |
| `1H` | `Gate` | `47.89%` | `52.11%` | `0.92` | 707,350.00 USD |
| `1H` | `Bitget` | `56.52%` | `43.48%` | `1.30` | 1,190,000.00 USD |
| `1H` | `BingX` | `61.85%` | `38.15%` | `1.62` | 780,040.00 USD |
| `1H` | `MEXC` | `50.13%` | `49.87%` | `1.01` | 994,270.00 USD |
| `1H` | `Bitunix` | `51.68%` | `48.32%` | `1.07` | 441,840.00 USD |
| `1H` | `Hyperliquid` | `55.02%` | `44.98%` | `1.22` | 756,630.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.91%` | `50.09%` | `1.00` | 256,860.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `45.95%` | `54.05%` | `0.85` | 795,530.00 USD |
| `1H` | `HTX` | `52.69%` | `47.31%` | `1.11` | 21,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `57.08%` | `42.92%` | `1.33` | 102,370.00 USD |
| `1H` | `Aster` | `62.02%` | `37.98%` | `1.63` | 124,450.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `17.24%` | `82.76%` | `0.21` | 34,640.00 USD |
| `1H` | `Whale Positions` | `49.4%` | `50.6%` | `0.98` | 11,520,000.00 USD |
| `1H` | `Global Accounts` | `51.51%` | `48.49%` | `1.06` | 27,430,000.00 USD |
| `4H` | `PAXG` | `43.53%` | `56.47%` | `0.77` | 78,000,000.00 USD |
| `4H` | `Binance` | `44.19%` | `55.81%` | `0.79` | 31,840,000.00 USD |
| `4H` | `OKX` | `49.08%` | `50.92%` | `0.96` | 9,110,000.00 USD |
| `4H` | `Bybit` | `46.61%` | `53.39%` | `0.87` | 11,880,000.00 USD |
| `4H` | `KuCoin` | `48.9%` | `51.1%` | `0.96` | 2,450,000.00 USD |
| `4H` | `Gate` | `51.32%` | `48.68%` | `1.05` | 1,660,000.00 USD |
| `4H` | `Bitget` | `45.06%` | `54.94%` | `0.82` | 3,150,000.00 USD |
| `4H` | `BingX` | `18.4%` | `81.6%` | `0.23` | 6,570,000.00 USD |
| `4H` | `MEXC` | `41.52%` | `58.48%` | `0.71` | 4,220,000.00 USD |
| `4H` | `Bitunix` | `48.08%` | `51.92%` | `0.93` | 1,240,000.00 USD |
| `4H` | `Hyperliquid` | `44.91%` | `55.09%` | `0.82` | 1,700,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.94%` | `51.06%` | `0.96` | 1,330,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.42%` | `53.58%` | `0.87` | 2,090,000.00 USD |
| `4H` | `HTX` | `55%` | `45%` | `1.22` | 76,290.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `70.57%` | `29.43%` | `2.40` | 444,650.00 USD |
| `4H` | `Aster` | `55.19%` | `44.81%` | `1.23` | 177,820.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `20.95%` | `79.05%` | `0.27` | 78,090.00 USD |
| `4H` | `Whale Positions` | `44.19%` | `55.81%` | `0.79` | 31,840,000.00 USD |
| `4H` | `Global Accounts` | `43.53%` | `56.47%` | `0.77` | 78,000,000.00 USD |


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
| `5m` | -185,350.00 USD | -31,470.00 USD | **`DISTRIBUTION`** |
| `15m` | -554,050.00 USD | -35,320.00 USD | **`DISTRIBUTION`** |
| `30m` | -947,940.00 USD | -64,460.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,060,000.00 USD | -165,240.00 USD | **`DISTRIBUTION`** |
| `2h` | -920,940.00 USD | -198,470.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,350,000.00 USD | -84,110.00 USD | **`DISTRIBUTION`** |
| `6h` | -638,540.00 USD | 700,250.00 USD | **`ACCUMULATION`** |
| `8h` | -906,990.00 USD | 827,870.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,340,000.00 USD | 1,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -850,130.00 USD | 1,620,000.00 USD | **`ACCUMULATION`** |
| `1w` | -9,230,000.00 USD | -8,030,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,890,000.00 USD | -71,420,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-185.35K` | 15m=`-554.05K` | 1h=`-1.06M` | 24h=`-850.13K`
* Futures Capital Netflows: 5m=`-31.47K` | 15m=`-35.32K` | 1h=`-165.24K` | 24h=`+1.62M`
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
  * `2026-10-30 02:54:26 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:10:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:11:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4016.67` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4008.15` (Risk Distance: `8.52` pts)
  * +2.5R Take Profit: `4037.98`
  * Mathematical Lot Sizing: **`1.17 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4039.67` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4048.19` (Risk Distance: `8.52` pts)
  * +2.5R Take Profit: `4018.36`
  * Mathematical Lot Sizing: **`1.17 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4053.67`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
