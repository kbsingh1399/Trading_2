# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 03:16:11 IST` (`2026-10-29 21:46:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `53` | `0x4692...164f` | `SHORT` | 25,375,381.27 USD | `6,314.95` | `4133.22` | `4018.50` | `13718.11` | 725,773.77 USD | `+2.86%` | `5X Cross` |
| `54` | `0x5b5d...c060` | `SHORT` | 25,228,820.20 USD | `6,278.48` | `4191.26` | `4018.50` | `31837.47` | 1,085,970.56 USD | `+4.30%` | `4X Cross` |
| `70` | `0xb83d...6e36` | `SHORT` | 22,997,865.67 USD | `5,723.28` | `4234.26` | `4018.50` | `29582.99` | 1,236,015.04 USD | `+5.37%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,403,996.60 USD | `4,828.91` | `4157.43` | `4018.50` | `2190.80` | -671,885.72 USD | `-3.46%` | `25X Cross` |
| `146` | `0x645b...87b8` | `LONG` | 14,168,771.72 USD | `3,526.06` | `4129.34` | `4018.50` | `402.82` | -391,537.79 USD | `-2.76%` | `3X Cross` |
| `160` | `0x7a6d...f79c` | `SHORT` | 13,132,987.92 USD | `3,268.21` | `4228.94` | `4018.50` | `4396.99` | 688,091.21 USD | `+5.24%` | `25X Cross` |
| `177` | `0xa742...e390` | `SHORT` | 11,653,070.40 USD | `2,900.00` | `4364.92` | `4018.50` | `4235.67` | 1,005,205.93 USD | `+8.63%` | `20X Cross` |
| `262` | `0xfc66...ca06` | `SHORT` | 8,980,962.29 USD | `2,235.07` | `4031.28` | `4018.50` | `22253.94` | 29,250.35 USD | `+0.33%` | `3X Cross` |
| `267` | `0x3678...b209` | `LONG` | 8,840,480.00 USD | `2,200.00` | `4176.09` | `4018.50` | `2506.32` | -346,939.30 USD | `-3.92%` | `25X Cross` |
| `268` | `0x41e5...0825` | `SHORT` | 8,840,260.00 USD | `2,200.00` | `4112.20` | `4018.50` | `4331.15` | 206,594.59 USD | `+2.34%` | `20X Cross` |
| `306` | `0xacb6...efbd` | `SHORT` | 7,937,625.65 USD | `1,975.37` | `4048.55` | `4018.50` | `6497.61` | 59,766.06 USD | `+0.75%` | `6X Cross` |
| `377` | `0xc26c...b8f4` | `LONG` | 6,348,562.32 USD | `1,579.95` | `4075.62` | `4018.50` | `0.000000` | -90,734.65 USD | `-1.43%` | `1X Cross` |
| `407` | `0x12d2...f97f` | `LONG` | 5,633,426.75 USD | `1,401.94` | `4278.91` | `4018.50` | `2857.69` | -365,363.83 USD | `-6.49%` | `20X Cross` |
| `566` | `0x63da...8add` | `LONG` | 4,018,200.00 USD | `1,000.00` | `4021.46` | `4018.50` | `3564.11` | -3,260.96 USD | `-0.08%` | `25X Cross` |
| `581` | `0x354b...6425` | `LONG` | 3,969,018.77 USD | `987.74` | `4031.85` | `4018.50` | `0.000000` | -13,388.57 USD | `-0.34%` | `10X Cross` |
| `592` | `0x9aa5...58af` | `LONG` | 3,904,349.05 USD | `971.64` | `4279.98` | `4018.50` | `0.000000` | -254,260.04 USD | `-6.51%` | `20X Cross` |
| `615` | `0xf3dc...1672` | `LONG` | 3,739,914.34 USD | `930.74` | `4024.62` | `4018.50` | `3337.59` | -5,978.23 USD | `-0.16%` | `20X Cross` |
| `687` | `0x4a20...3c26` | `LONG` | 3,365,006.95 USD | `837.40` | `4599.73` | `4018.50` | `0.000000` | -486,813.43 USD | `-14.47%` | `20X Cross` |
| `840` | `0x0fac...7a0a` | `LONG` | 2,758,502.68 USD | `686.49` | `4290.34` | `4018.50` | `1230.87` | -186,756.03 USD | `-6.77%` | `25X Cross` |
| `888` | `0xd8c5...99b0` | `SHORT` | 2,581,238.93 USD | `642.35` | `4175.35` | `4018.50` | `32728.01` | 100,822.25 USD | `+3.91%` | `4X Cross` |
| `922` | `0x625e...a354` | `SHORT` | 2,491,346.00 USD | `620.00` | `4122.81` | `4018.50` | `4342.25` | 64,801.03 USD | `+2.60%` | `20X Cross` |
| `949` | `0xeae3...e8ad` | `SHORT` | 2,411,040.00 USD | `600.00` | `4104.77` | `4018.50` | `4325.27` | 51,825.11 USD | `+2.15%` | `20X Cross` |
| `954` | `0xf285...fa82` | `LONG` | 2,403,368.94 USD | `598.11` | `4146.45` | `4018.50` | `3891.24` | -76,650.61 USD | `-3.19%` | `25X Cross` |
| `973` | `0x12f7...8750` | `LONG` | 2,353,218.04 USD | `585.61` | `4082.77` | `4018.50` | `2411.36` | -37,698.94 USD | `-1.60%` | `10X Cross` |
| `1120` | `0x413c...886c` | `LONG` | 2,009,100.00 USD | `500.00` | `4010.43` | `4018.50` | `0.000000` | 3,883.77 USD | `+0.19%` | `2X Cross` |
| `1131` | `0x61ce...a62b` | `SHORT` | 1,999,068.56 USD | `497.50` | `4071.66` | `4018.50` | `4700.96` | 26,600.23 USD | `+1.33%` | `20X Cross` |
| `1134` | `0x0593...40f9` | `LONG` | 1,993,837.66 USD | `496.18` | `4024.57` | `4018.50` | `3701.73` | -3,066.17 USD | `-0.15%` | `10X Isolated` |
| `1215` | `0x2edd...8179` | `LONG` | 1,893,305.72 USD | `470.91` | `4164.68` | `4020.50` | `0.000000` | -67,895.60 USD | `-3.59%` | `10X Cross` |
| `1256` | `0xead5...69f2` | `LONG` | 1,823,349.09 USD | `453.78` | `4220.88` | `4018.50` | `3538.94` | -92,018.97 USD | `-5.05%` | `5X Isolated` |
| `1316` | `0x7a6d...f79c` | `SHORT` | 1,722,295.63 USD | `428.38` | `4136.09` | `4020.50` | `5654.40` | 49,519.38 USD | `+2.88%` | `10X Cross` |
| `1370` | `0x46fc...1195` | `LONG` | 1,653,738.60 USD | `411.55` | `4055.10` | `4018.50` | `2116.56` | -15,146.94 USD | `-0.92%` | `20X Cross` |
| `1404` | `0x6d15...d374` | `LONG` | 1,607,320.00 USD | `400.00` | `4068.25` | `4018.50` | `3841.81` | -19,980.00 USD | `-1.24%` | `25X Cross` |
| `1405` | `0xee02...309d` | `SHORT` | 1,607,320.00 USD | `400.00` | `4438.84` | `4018.50` | `4226.89` | 168,218.60 USD | `+10.47%` | `25X Isolated` |
| `1444` | `0x02a7...fe9f` | `SHORT` | 1,567,176.00 USD | `390.00` | `4055.02` | `4018.50` | `4306.71` | 14,283.25 USD | `+0.91%` | `25X Cross` |
| `1476` | `0x51f6...2b39` | `LONG` | 1,529,743.96 USD | `380.49` | `4234.66` | `4020.50` | `0.000000` | -81,484.10 USD | `-5.33%` | `10X Cross` |
| `1480` | `0x7e77...b8d2` | `SHORT` | 1,526,992.00 USD | `380.00` | `4131.92` | `4018.50` | `4293.51` | 43,137.64 USD | `+2.83%` | `20X Cross` |
| `1497` | `0x72c2...9b37` | `LONG` | 1,499,316.19 USD | `373.13` | `4000.98` | `4018.50` | `3778.04` | 6,422.67 USD | `+0.43%` | `13X Isolated` |
| `1547` | `0xaa44...b844` | `LONG` | 1,446,624.00 USD | `360.00` | `4043.10` | `4018.50` | `2803.26` | -8,893.63 USD | `-0.61%` | `4X Cross` |
| `1548` | `0x781e...96b7` | `SHORT` | 1,445,534.82 USD | `359.55` | `4365.03` | `4020.50` | `13236.38` | 123,912.66 USD | `+8.57%` | `10X Cross` |
| `1656` | `0xa41f...d50a` | `LONG` | 1,321,868.41 USD | `328.96` | `4468.89` | `4018.50` | `3833.19` | -148,229.45 USD | `-11.21%` | `15X Cross` |
| `1672` | `0x49e9...e1d0` | `SHORT` | 1,299,836.47 USD | `323.48` | `4025.23` | `4018.50` | `31846.01` | 2,241.86 USD | `+0.17%` | `4X Cross` |
| `1687` | `0xada6...6f88` | `LONG` | 1,282,913.22 USD | `319.28` | `4166.46` | `4018.50` | `1967.68` | -47,337.29 USD | `-3.69%` | `5X Cross` |
| `1692` | `0xbf5a...88ba` | `SHORT` | 1,276,432.68 USD | `317.65` | `4091.80` | `4018.50` | `9989.37` | 23,350.35 USD | `+1.83%` | `20X Cross` |
| `1723` | `0xff31...ff6c` | `SHORT` | 1,245,704.00 USD | `310.00` | `4372.43` | `4018.50` | `4789.18` | 109,751.38 USD | `+8.81%` | `10X Isolated` |
| `1890` | `0x50e2...d770` | `LONG` | 1,086,444.36 USD | `270.37` | `4243.58` | `4018.50` | `2562.10` | -60,882.10 USD | `-5.60%` | `20X Cross` |
| `1907` | `0x4c92...4f17` | `SHORT` | 1,071,789.66 USD | `266.72` | `4260.98` | `4018.50` | `6522.71` | 64,702.58 USD | `+6.04%` | `20X Cross` |
| `1977` | `0xd346...c4f3` | `LONG` | 1,025,364.88 USD | `255.17` | `4188.66` | `4018.50` | `3310.42` | -43,471.63 USD | `-4.24%` | `5X Isolated` |
| `2014` | `0x1581...463b` | `LONG` | 1,004,550.00 USD | `250.00` | `4003.77` | `4018.50` | `3525.17` | 3,606.41 USD | `+0.36%` | `15X Cross` |

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
  * Total Open Interest: `274.74M` | Total OI Tokens: `68,324.2 PAXG`
  * 1h OI Change: `-0.07%` | 4h OI Change: `-0.10%` | 24h OI Change: `+0.17%`
  * Exchange Breakdown: Binance=`107.22M` | Bybit=`19.92M` | OKX=`-` | Hyperliquid=`24.64M`
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
| `15M` | `PAXG` | `56.36%` | `43.64%` | `1.29` | 8,390,000.00 USD |
| `15M` | `Binance` | `52.21%` | `47.79%` | `1.09` | 3,990,000.00 USD |
| `15M` | `OKX` | `70.04%` | `29.96%` | `2.34` | 1,530,000.00 USD |
| `15M` | `Bybit` | `56.83%` | `43.17%` | `1.32` | 634,300.00 USD |
| `15M` | `KuCoin` | `62.52%` | `37.48%` | `1.67` | 76,150.00 USD |
| `15M` | `Gate` | `63.59%` | `36.41%` | `1.75` | 171,010.00 USD |
| `15M` | `Bitget` | `35.14%` | `64.86%` | `0.54` | 114,620.00 USD |
| `15M` | `BingX` | `38.78%` | `61.22%` | `0.63` | 250,640.00 USD |
| `15M` | `MEXC` | `55.26%` | `44.74%` | `1.24` | 555,220.00 USD |
| `15M` | `Bitunix` | `49.95%` | `50.05%` | `1.00` | 118,220.00 USD |
| `15M` | `Hyperliquid` | `77.04%` | `22.96%` | `3.36` | 119,490.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.35%` | `49.65%` | `1.01` | 679,900.00 USD |
| `15M` | `Crypto.com` | `64.54%` | `35.46%` | `1.82` | 3,890.00 USD |
| `15M` | `WhiteBIT` | `87.74%` | `12.26%` | `7.16` | 114,100.00 USD |
| `15M` | `HTX` | `58.85%` | `41.15%` | `1.43` | 774.45 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `31.72%` | `68.28%` | `0.46` | 21,160.00 USD |
| `15M` | `Aster` | `91.57%` | `8.43%` | `10.86` | 11,140.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `65.63%` | `34.37%` | `1.91` | 5,190.00 USD |
| `15M` | `Whale Positions` | `52.21%` | `47.79%` | `1.09` | 3,990,000.00 USD |
| `15M` | `Global Accounts` | `56.36%` | `43.64%` | `1.29` | 8,390,000.00 USD |
| `1H` | `PAXG` | `46.64%` | `53.36%` | `0.87` | 6,130,000.00 USD |
| `1H` | `Binance` | `46.05%` | `53.95%` | `0.85` | 3,840,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `46.67%` | `53.33%` | `0.88` | 258,000.00 USD |
| `1H` | `KuCoin` | `59.21%` | `40.79%` | `1.45` | 487,160.00 USD |
| `1H` | `Gate` | `53.97%` | `46.03%` | `1.17` | 106,530.00 USD |
| `1H` | `Bitget` | `50.63%` | `49.37%` | `1.03` | 317,070.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `33.13%` | `66.87%` | `0.50` | 44,250.00 USD |
| `1H` | `Bitunix` | `24.92%` | `75.08%` | `0.33` | 160,050.00 USD |
| `1H` | `Hyperliquid` | `27.05%` | `72.95%` | `0.37` | 627,960.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `96.63%` | `3.37%` | `28.67` | 221,800.00 USD |
| `1H` | `HTX` | `66.06%` | `33.94%` | `1.95` | 22,210.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0.96%` | `99.04%` | `0.01` | 20,070.00 USD |
| `1H` | `Aster` | `24%` | `76%` | `0.32` | 1,710.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.98%` | `57.02%` | `0.75` | 29,870.00 USD |
| `1H` | `Whale Positions` | `46.05%` | `53.95%` | `0.85` | 3,840,000.00 USD |
| `1H` | `Global Accounts` | `46.64%` | `53.36%` | `0.87` | 6,130,000.00 USD |
| `4H` | `PAXG` | `46.66%` | `53.34%` | `0.87` | 65,300,000.00 USD |
| `4H` | `Binance` | `55.49%` | `44.51%` | `1.25` | 5,910,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `55.04%` | `44.96%` | `1.22` | 6,490,000.00 USD |
| `4H` | `KuCoin` | `26.33%` | `73.67%` | `0.36` | 338,830.00 USD |
| `4H` | `Gate` | `52.85%` | `47.15%` | `1.12` | 2,600,000.00 USD |
| `4H` | `Bitget` | `53.48%` | `46.52%` | `1.15` | 1,890,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `42.62%` | `57.38%` | `0.74` | 38,340,000.00 USD |
| `4H` | `Bitunix` | `53.66%` | `46.34%` | `1.16` | 3,240,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54%` | `46%` | `1.17` | 5,260,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `14.49%` | `85.51%` | `0.17` | 1,060,000.00 USD |
| `4H` | `HTX` | `40.86%` | `59.14%` | `0.69` | 11,590.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.23%` | `59.77%` | `0.67` | 154,880.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `55.49%` | `44.51%` | `1.25` | 5,910,000.00 USD |
| `4H` | `Global Accounts` | `46.66%` | `53.34%` | `0.87` | 65,300,000.00 USD |


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
| `5m` | -185,350.00 USD | -69,190.00 USD | **`DISTRIBUTION`** |
| `15m` | -554,050.00 USD | -143,350.00 USD | **`DISTRIBUTION`** |
| `30m` | -947,940.00 USD | -113,540.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,060,000.00 USD | -574,460.00 USD | **`DISTRIBUTION`** |
| `2h` | -920,940.00 USD | -431,020.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,350,000.00 USD | -184,950.00 USD | **`DISTRIBUTION`** |
| `6h` | -638,540.00 USD | 584,120.00 USD | **`DISTRIBUTION`** |
| `8h` | -906,990.00 USD | 634,890.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,340,000.00 USD | 1,210,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -850,130.00 USD | 1,490,000.00 USD | **`ACCUMULATION`** |
| `1w` | -9,230,000.00 USD | -8,050,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,890,000.00 USD | -71,440,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-185.35K` | 15m=`-554.05K` | 1h=`-1.06M` | 24h=`-850.13K`
* Futures Capital Netflows: 5m=`-69.19K` | 15m=`-143.35K` | 1h=`-574.46K` | 24h=`+1.49M`
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
