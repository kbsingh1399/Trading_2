# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 02:36:43 IST` (`2026-10-29 21:06:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `4021.20` | `4021.88` | `4020.69` | `4021.36` | `79` | 316,330.44 USD | -25,394.66 USD | `-8.03%` | 1,508,327.53 USD | `-0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4021.37` | `4021.37` | `4017.98` | `4018.34` | `129` | 518,954.80 USD | -11,514.92 USD | `-2.22%` | 1,496,812.60 USD | `+0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `4018.34` | `4018.58` | `4018.34` | `4018.58` | `16` | 64,124.83 USD | 17,062.03 USD | `+26.61%` | 1,513,874.63 USD | `+0.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4027.95` | `4030.42` | `4023.58` | `4024.17` | `313` | 1,259,892.82 USD | -400,755.58 USD | `-31.81%` | 1,524,666.35 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4024.17` | `4026.05` | `4020.69` | `4021.36` | `303` | 1,217,913.75 USD | -63,332.79 USD | `-5.20%` | 1,461,333.56 USD | `-0.37` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4021.37` | `4021.37` | `4017.98` | `4018.34` | `138` | 556,108.41 USD | -21,391.97 USD | `-3.85%` | 1,439,941.59 USD | `-0.17` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4017.56` | `4025.99` | `4014.71` | `4025.60` | `520` | 2,091,733.78 USD | -652,688.52 USD | `-31.20%` | 1,838,471.59 USD | `-1.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4025.61` | `4033.50` | `4020.69` | `4021.36` | `1,040` | 4,187,720.97 USD | -239,141.91 USD | `-5.71%` | 1,599,329.68 USD | `-0.58` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4021.37` | `4021.37` | `4017.98` | `4018.34` | `138` | 556,024.02 USD | -21,339.73 USD | `-3.84%` | 1,577,989.95 USD | `-0.05` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.98` | `4018.34` | `1,178` | 4,743,781.16 USD | -260,517.81 USD | `-5.49%` | 986,629.52 USD | `-0.70` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.98` | `4018.34` | `1,178` | 4,743,781.16 USD | -260,517.81 USD | `-5.49%` | 986,629.52 USD | `-0.70` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `4017.30` | `2.5412` | 10,208.76 USD | 238,379.70 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `4017.40` | `3.9320` | 15,796.42 USD | 228,170.93 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `4017.60` | `5.0566` | 20,315.40 USD | 212,374.52 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4017.70` | `1.4863` | 5,971.51 USD | 192,059.12 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4017.80` | `1.2436` | 4,996.54 USD | 186,087.61 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4017.90` | `1.4084` | 5,658.81 USD | 181,091.08 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4018.00` | `0.9333` | 3,750.00 USD | 175,432.27 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4018.10` | `1.9830` | 7,967.89 USD | 171,682.27 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4018.20` | `5.9507` | 23,911.10 USD | 163,714.38 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4018.30` | `3.7946` | 15,247.84 USD | 139,803.27 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4018.40` | `0.0547` | 219.81 USD | 124,555.43 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4018.50` | `5.1037` | 20,509.22 USD | 124,335.63 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4018.60` | `1.7861` | 7,177.62 USD | 103,826.41 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4018.80` | `3.9660` | 15,938.56 USD | 96,648.79 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4018.90` | `0.0547` | 219.83 USD | 80,710.23 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4019.00` | `5.9490` | 23,909.03 USD | 80,490.39 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4019.10` | `0.4961` | 1,993.88 USD | 56,581.36 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4019.20` | `7.6986` | 30,942.21 USD | 54,587.48 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4019.30` | `2.5387` | 10,203.80 USD | 23,645.27 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4019.70` | `3.3439` | 13,441.47 USD | 13,441.47 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4019.75` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,019.75` | `0.00%` | `-` |
| `ASK` | `4019.80` | `0.6624` | 2,662.72 USD | 2,662.72 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `4020.00` | `0.2323` | 933.85 USD | 3,596.56 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4020.10` | `0.9328` | 3,749.95 USD | 7,346.51 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4020.30` | `4.9124` | 19,749.32 USD | 27,095.83 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4020.50` | `1.0047` | 4,039.40 USD | 31,135.23 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4020.60` | `2.2724` | 9,136.41 USD | 40,271.64 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4020.70` | `2.2257` | 8,948.87 USD | 49,220.51 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4020.80` | `12.8297` | 51,585.66 USD | 100,806.17 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4020.90` | `7.3988` | 29,749.83 USD | 130,556.00 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `4021.00` | `5.8129` | 23,373.67 USD | 153,929.68 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4021.10` | `0.9326` | 3,750.08 USD | 157,679.75 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4021.20` | `0.0547` | 219.96 USD | 157,899.71 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4021.30` | `2.1630` | 8,698.07 USD | 166,597.79 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4021.40` | `6.1192` | 24,607.75 USD | 191,205.54 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4021.50` | `7.9834` | 32,105.24 USD | 223,310.78 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4021.60` | `0.0027` | 10.86 USD | 223,321.64 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `4021.70` | `2.9144` | 11,720.84 USD | 235,042.48 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4021.80` | `0.2730` | 1,097.95 USD | 236,140.43 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4021.90` | `0.9324` | 3,750.02 USD | 239,890.45 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `4022.00` | `4.4495` | 17,895.89 USD | 257,786.34 USD | `2 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `53` | `0x4692...164f` | `SHORT` | 25,385,187.01 USD | `6,313.15` | `4133.51` | `4021.30` | `13663.36` | 710,314.23 USD | `+2.80%` | `5X Cross` |
| `54` | `0x5b5d...c060` | `SHORT` | 25,316,514.99 USD | `6,295.45` | `4191.43` | `4021.30` | `33232.02` | 1,070,470.40 USD | `+4.23%` | `4X Cross` |
| `67` | `0xb83d...6e36` | `SHORT` | 22,987,152.44 USD | `5,717.06` | `4234.49` | `4021.30` | `30986.77` | 1,221,722.79 USD | `+5.31%` | `5X Cross` |
| `95` | `0xec0b...b078` | `LONG` | 19,413,171.52 USD | `4,828.91` | `4157.43` | `4021.30` | `2245.20` | -662,710.80 USD | `-3.41%` | `25X Cross` |
| `141` | `0x645b...87b8` | `LONG` | 14,157,170.98 USD | `3,520.81` | `4129.50` | `4021.30` | `368.26` | -382,029.11 USD | `-2.70%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 13,141,812.10 USD | `3,268.21` | `4228.94` | `4021.30` | `4393.69` | 679,267.03 USD | `+5.17%` | `25X Cross` |
| `172` | `0xa742...e390` | `SHORT` | 11,658,870.40 USD | `2,900.00` | `4364.92` | `4021.30` | `4235.64` | 999,405.93 USD | `+8.57%` | `20X Cross` |
| `268` | `0x3678...b209` | `LONG` | 8,846,200.00 USD | `2,200.00` | `4176.09` | `4021.30` | `2582.59` | -341,219.30 USD | `-3.86%` | `25X Cross` |
| `269` | `0x41e5...0825` | `SHORT` | 8,844,220.00 USD | `2,200.00` | `4112.20` | `4021.30` | `4331.13` | 202,634.59 USD | `+2.29%` | `20X Cross` |
| `303` | `0xfc66...ca06` | `SHORT` | 7,965,696.65 USD | `1,981.17` | `4032.86` | `4021.30` | `24588.02` | 24,109.57 USD | `+0.30%` | `3X Cross` |
| `305` | `0xacb6...efbd` | `SHORT` | 7,944,144.37 USD | `1,975.37` | `4048.55` | `4021.30` | `6506.07` | 53,247.34 USD | `+0.67%` | `6X Cross` |
| `373` | `0xc26c...b8f4` | `LONG` | 6,351,722.23 USD | `1,579.95` | `4075.62` | `4021.30` | `0.000000` | -87,574.74 USD | `-1.38%` | `1X Cross` |
| `406` | `0x12d2...f97f` | `LONG` | 5,636,090.44 USD | `1,401.94` | `4278.91` | `4021.30` | `3074.39` | -362,700.13 USD | `-6.44%` | `20X Cross` |
| `553` | `0x63da...8add` | `LONG` | 4,021,000.00 USD | `1,000.00` | `4021.46` | `4021.30` | `3564.08` | -460.96 USD | `-0.01%` | `25X Cross` |
| `564` | `0x354b...6425` | `LONG` | 3,971,685.65 USD | `987.74` | `4031.85` | `4021.30` | `0.000000` | -10,721.68 USD | `-0.27%` | `10X Cross` |
| `577` | `0x9aa5...58af` | `LONG` | 3,907,555.47 USD | `971.64` | `4279.98` | `4021.30` | `0.000000` | -251,053.62 USD | `-6.42%` | `20X Cross` |
| `607` | `0xf3dc...1672` | `LONG` | 3,742,706.57 USD | `930.74` | `4024.62` | `4021.30` | `3337.56` | -3,186.00 USD | `-0.09%` | `20X Cross` |
| `669` | `0x4a20...3c26` | `LONG` | 3,366,932.97 USD | `837.40` | `4599.73` | `4021.30` | `0.000000` | -484,887.41 USD | `-14.40%` | `20X Cross` |
| `827` | `0x0fac...7a0a` | `LONG` | 2,760,493.48 USD | `686.49` | `4290.34` | `4021.30` | `1288.86` | -184,765.22 USD | `-6.69%` | `25X Cross` |
| `868` | `0xd8c5...99b0` | `SHORT` | 2,583,037.52 USD | `642.35` | `4175.35` | `4021.30` | `32816.79` | 99,023.65 USD | `+3.83%` | `4X Cross` |
| `897` | `0x625e...a354` | `SHORT` | 2,492,524.00 USD | `620.00` | `4122.81` | `4021.30` | `4342.23` | 63,623.03 USD | `+2.55%` | `20X Cross` |
| `923` | `0xeae3...e8ad` | `SHORT` | 2,412,720.00 USD | `600.00` | `4104.77` | `4021.30` | `4325.25` | 50,145.11 USD | `+2.08%` | `20X Cross` |
| `930` | `0xf285...fa82` | `LONG` | 2,404,505.34 USD | `598.11` | `4146.45` | `4021.30` | `3891.22` | -75,514.21 USD | `-3.14%` | `25X Cross` |
| `946` | `0x12f7...8750` | `LONG` | 2,354,799.19 USD | `585.61` | `4082.77` | `4021.30` | `2512.71` | -36,117.79 USD | `-1.53%` | `10X Cross` |
| `1102` | `0x413c...886c` | `LONG` | 2,010,700.00 USD | `500.00` | `4010.43` | `4021.30` | `0.000000` | 5,483.77 USD | `+0.27%` | `2X Cross` |
| `1111` | `0x61ce...a62b` | `SHORT` | 2,000,561.07 USD | `497.50` | `4071.66` | `4021.30` | `4712.53` | 25,107.72 USD | `+1.26%` | `20X Cross` |
| `1116` | `0x0593...40f9` | `LONG` | 1,995,226.95 USD | `496.18` | `4024.57` | `4021.30` | `3701.71` | -1,676.88 USD | `-0.08%` | `10X Isolated` |
| `1189` | `0x2edd...8179` | `LONG` | 1,884,845.13 USD | `468.76` | `4165.34` | `4020.71` | `0.000000` | -67,708.08 USD | `-3.59%` | `10X Cross` |
| `1239` | `0xead5...69f2` | `LONG` | 1,824,302.03 USD | `453.78` | `4220.88` | `4021.30` | `3538.92` | -91,066.02 USD | `-4.99%` | `5X Isolated` |
| `1299` | `0x7a6d...f79c` | `SHORT` | 1,722,383.45 USD | `428.38` | `4136.09` | `4020.71` | `5788.73` | 49,431.56 USD | `+2.87%` | `10X Cross` |
| `1344` | `0x46fc...1195` | `LONG` | 1,646,553.26 USD | `409.49` | `4055.28` | `4021.30` | `2094.20` | -14,037.63 USD | `-0.85%` | `20X Cross` |
| `1382` | `0xee02...309d` | `SHORT` | 1,608,640.00 USD | `400.00` | `4438.84` | `4021.30` | `4226.86` | 166,898.60 USD | `+10.38%` | `25X Isolated` |
| `1383` | `0x6d15...d374` | `LONG` | 1,608,320.00 USD | `400.00` | `4068.25` | `4021.30` | `3841.79` | -18,980.00 USD | `-1.18%` | `25X Cross` |
| `1421` | `0x02a7...fe9f` | `SHORT` | 1,568,190.00 USD | `390.00` | `4055.02` | `4021.30` | `4306.68` | 13,269.25 USD | `+0.85%` | `25X Cross` |
| `1457` | `0x51f6...2b39` | `LONG` | 1,529,896.16 USD | `380.49` | `4234.66` | `4020.71` | `0.000000` | -81,331.91 USD | `-5.32%` | `10X Cross` |
| `1462` | `0x7e77...b8d2` | `SHORT` | 1,528,056.00 USD | `380.00` | `4131.92` | `4021.30` | `4293.49` | 42,073.64 USD | `+2.75%` | `20X Cross` |
| `1483` | `0x72c2...9b37` | `LONG` | 1,500,435.58 USD | `373.13` | `4000.98` | `4021.30` | `3778.02` | 7,542.07 USD | `+0.50%` | `13X Isolated` |
| `1519` | `0xaa44...b844` | `LONG` | 1,447,668.00 USD | `360.00` | `4043.10` | `4021.30` | `2803.24` | -7,849.63 USD | `-0.54%` | `4X Cross` |
| `1521` | `0x781e...96b7` | `SHORT` | 1,445,714.59 USD | `359.55` | `4365.03` | `4020.71` | `13627.03` | 123,732.89 USD | `+8.56%` | `10X Cross` |
| `1632` | `0xa41f...d50a` | `LONG` | 1,322,493.43 USD | `328.96` | `4468.89` | `4021.30` | `3833.16` | -147,604.42 USD | `-11.16%` | `15X Cross` |
| `1652` | `0x49e9...e1d0` | `SHORT` | 1,300,709.86 USD | `323.48` | `4025.23` | `4021.30` | `30978.66` | 1,368.46 USD | `+0.11%` | `4X Cross` |
| `1668` | `0xada6...6f88` | `LONG` | 1,283,871.04 USD | `319.28` | `4166.46` | `4021.30` | `1940.43` | -46,379.47 USD | `-3.61%` | `5X Cross` |
| `1672` | `0xbf5a...88ba` | `SHORT` | 1,277,036.23 USD | `317.65` | `4091.80` | `4021.30` | `10337.50` | 22,746.80 USD | `+1.78%` | `20X Cross` |
| `1708` | `0xff31...ff6c` | `SHORT` | 1,246,572.00 USD | `310.00` | `4372.43` | `4021.30` | `4789.15` | 108,883.38 USD | `+8.73%` | `10X Isolated` |
| `1872` | `0x50e2...d770` | `LONG` | 1,087,066.21 USD | `270.37` | `4243.58` | `4021.30` | `2562.07` | -60,260.26 USD | `-5.54%` | `20X Cross` |
| `1896` | `0x4c92...4f17` | `SHORT` | 1,072,483.13 USD | `266.72` | `4260.98` | `4021.30` | `6500.43` | 64,009.11 USD | `+5.97%` | `20X Cross` |
| `1951` | `0xd346...c4f3` | `LONG` | 1,026,053.85 USD | `255.17` | `4188.66` | `4021.30` | `3310.40` | -42,782.66 USD | `-4.17%` | `5X Isolated` |
| `1982` | `0x1581...463b` | `LONG` | 1,005,100.00 USD | `250.00` | `4003.77` | `4021.30` | `3504.62` | 4,156.41 USD | `+0.41%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


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
| `7D` | `Long Liquidation` | `3611.20` | 16,440,000.00 USD | 16,440,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,360,000.00 USD | 16,360,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3615.60` | 3,740,000.00 USD | 3,740,000.00 USD | 28,900.00 USD | 0.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.80` | 3,710,000.00 USD | 3,710,000.00 USD | 24,570.00 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,210,000.00 USD | 16,210,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3624.00` | 3,690,000.00 USD | 3,690,000.00 USD | 60,480.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,160,000.00 USD | 16,160,000.00 USD | 88,630.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3628.20` | 3,620,000.00 USD | 3,620,000.00 USD | 43,260.00 USD | 0.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,050,000.00 USD | 16,050,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3632.40` | 3,570,000.00 USD | 3,570,000.00 USD | 21,740.00 USD | 0.00 USD | 5,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 15,850,000.00 USD | 15,850,000.00 USD | 103,510.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3636.60` | 3,540,000.00 USD | 3,540,000.00 USD | 47,040.00 USD | 0.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,740,000.00 USD | 15,740,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3640.80` | 3,490,000.00 USD | 3,490,000.00 USD | 15,030.00 USD | 0.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,600,000.00 USD | 15,600,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3645.00` | 3,470,000.00 USD | 3,470,000.00 USD | 3,610.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,540,000.00 USD | 15,540,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3649.20` | 3,460,000.00 USD | 3,460,000.00 USD | 21,830.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,510,000.00 USD | 15,510,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3653.40` | 3,440,000.00 USD | 3,440,000.00 USD | 16,880.00 USD | 0.00 USD | 977.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,490,000.00 USD | 15,490,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3657.60` | 3,420,000.00 USD | 3,420,000.00 USD | 5,110.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,430,000.00 USD | 15,430,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3661.80` | 3,410,000.00 USD | 3,410,000.00 USD | 2,940.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,420,000.00 USD | 15,420,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,400,000.00 USD | 15,400,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,390,000.00 USD | 15,390,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 14,970,000.00 USD | 14,970,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,450,000.00 USD | 14,450,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 13,920,000.00 USD | 13,920,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3855.00` | 3,410,000.00 USD | 3,410,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,630,000.00 USD | 13,630,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3859.20` | 3,360,000.00 USD | 3,360,000.00 USD | 68,860.00 USD | 0.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,210,000.00 USD | 13,210,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3863.40` | 3,290,000.00 USD | 3,290,000.00 USD | 105,760.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,030,000.00 USD | 13,030,000.00 USD | 289,880.00 USD | 0.00 USD | 58,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3867.60` | 3,170,000.00 USD | 3,170,000.00 USD | 202,490.00 USD | 0.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,680,000.00 USD | 12,680,000.00 USD | 631,610.00 USD | 0.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3871.80` | 2,940,000.00 USD | 2,940,000.00 USD | 174,900.00 USD | 0.00 USD | 18,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 12,010,000.00 USD | 12,010,000.00 USD | 309,370.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.00` | 2,750,000.00 USD | 2,750,000.00 USD | 67,070.00 USD | 0.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,650,000.00 USD | 11,650,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.20` | 2,670,000.00 USD | 2,670,000.00 USD | 147,450.00 USD | 0.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,060,000.00 USD | 11,060,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3884.40` | 2,500,000.00 USD | 2,500,000.00 USD | 30,560.00 USD | 0.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,850,000.00 USD | 10,850,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3888.60` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,760,000.00 USD | 10,760,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3892.80` | 2,450,000.00 USD | 2,450,000.00 USD | 78,150.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,630,000.00 USD | 10,630,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.00` | 2,370,000.00 USD | 2,370,000.00 USD | 43,750.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,500,000.00 USD | 10,500,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.20` | 2,320,000.00 USD | 2,320,000.00 USD | 21,270.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,380,000.00 USD | 10,380,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3905.40` | 2,290,000.00 USD | 2,290,000.00 USD | 15,640.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,330,000.00 USD | 10,330,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,280,000.00 USD | 10,280,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,250,000.00 USD | 10,250,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,890,000.00 USD | 9,890,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,100,000.00 USD | 9,100,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,120,000.00 USD | 8,120,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 7,010,000.00 USD | 7,010,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.80` | 2,270,000.00 USD | 2,270,000.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,510,000.00 USD | 6,510,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3939.00` | 2,200,000.00 USD | 2,200,000.00 USD | 160,570.00 USD | 0.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,790,000.00 USD | 5,790,000.00 USD | 375,470.00 USD | 0.00 USD | 60,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.20` | 2,030,000.00 USD | 2,030,000.00 USD | 178,160.00 USD | 0.00 USD | 18,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,360,000.00 USD | 5,360,000.00 USD | 617,970.00 USD | 0.00 USD | 132,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.40` | 1,840,000.00 USD | 1,840,000.00 USD | 418,420.00 USD | 0.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,600,000.00 USD | 4,600,000.00 USD | 1,120,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.60` | 1,370,000.00 USD | 1,370,000.00 USD | 272,600.00 USD | 0.00 USD | 43,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,410,000.00 USD | 3,410,000.00 USD | 734,780.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.80` | 1,050,000.00 USD | 1,050,000.00 USD | 176,910.00 USD | 0.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3960.00` | 853,620.00 USD | 853,620.00 USD | 284,040.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3964.20` | 544,770.00 USD | 544,770.00 USD | 95,580.00 USD | 0.00 USD | 40,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3968.40` | 408,230.00 USD | 408,230.00 USD | 30,740.00 USD | 0.00 USD | 19,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3972.60` | 357,700.00 USD | 357,700.00 USD | 127,000.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3976.80` | 223,400.00 USD | 223,400.00 USD | 109,130.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3981.00` | 105,580.00 USD | 105,580.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3985.20` | 64,500.00 USD | 64,500.00 USD | 54,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3989.40` | 9,870.00 USD | 9,870.00 USD | 0.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.40` | 29,250.00 USD | 29,250.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.60` | 208,440.00 USD | 208,440.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.80` | 374,660.00 USD | 374,660.00 USD | 149,750.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,350,000.00 USD | 5,350,000.00 USD | 606,780.00 USD | 0.00 USD | 103,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.00` | 788,360.00 USD | 788,360.00 USD | 372,780.00 USD | 0.00 USD | 40,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,480,000.00 USD | 6,480,000.00 USD | 1,060,000.00 USD | 0.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.20` | 1,120,000.00 USD | 1,120,000.00 USD | 288,670.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,340,000.00 USD | 7,340,000.00 USD | 751,280.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.40` | 1,380,000.00 USD | 1,380,000.00 USD | 232,080.00 USD | 0.00 USD | 30,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,220,000.00 USD | 8,220,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.60` | 1,570,000.00 USD | 1,570,000.00 USD | 185,550.00 USD | 0.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 8,940,000.00 USD | 8,940,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.80` | 1,830,000.00 USD | 1,830,000.00 USD | 210,630.00 USD | 0.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,190,000.00 USD | 9,190,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4128.00` | 1,900,000.00 USD | 1,900,000.00 USD | 45,250.00 USD | 0.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,390,000.00 USD | 9,390,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4132.20` | 1,960,000.00 USD | 1,960,000.00 USD | 41,070.00 USD | 0.00 USD | 17,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,620,000.00 USD | 9,620,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4136.40` | 2,080,000.00 USD | 2,080,000.00 USD | 121,070.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,870,000.00 USD | 9,870,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4140.60` | 2,170,000.00 USD | 2,170,000.00 USD | 81,660.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,040,000.00 USD | 10,040,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4144.80` | 2,220,000.00 USD | 2,220,000.00 USD | 32,780.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,140,000.00 USD | 10,140,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4149.00` | 2,270,000.00 USD | 2,270,000.00 USD | 41,040.00 USD | 0.00 USD | 7,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,230,000.00 USD | 10,230,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4153.20` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,610,000.00 USD | 10,610,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,040,000.00 USD | 11,040,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,460,000.00 USD | 11,460,000.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 11,900,000.00 USD | 11,900,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.20` | 2,280,000.00 USD | 2,280,000.00 USD | 10,060.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,140,000.00 USD | 12,140,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.40` | 2,360,000.00 USD | 2,360,000.00 USD | 74,700.00 USD | 0.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,480,000.00 USD | 12,480,000.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4182.60` | 2,450,000.00 USD | 2,450,000.00 USD | 74,470.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,650,000.00 USD | 12,650,000.00 USD | 146,480.00 USD | 0.00 USD | 30,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4186.80` | 2,650,000.00 USD | 2,650,000.00 USD | 179,480.00 USD | 0.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 12,990,000.00 USD | 12,990,000.00 USD | 292,190.00 USD | 0.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4191.00` | 2,790,000.00 USD | 2,790,000.00 USD | 129,190.00 USD | 0.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,660,000.00 USD | 13,660,000.00 USD | 616,630.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4195.20` | 2,940,000.00 USD | 2,940,000.00 USD | 132,410.00 USD | 0.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 13,980,000.00 USD | 13,980,000.00 USD | 286,520.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.40` | 3,030,000.00 USD | 3,030,000.00 USD | 80,330.00 USD | 0.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,480,000.00 USD | 14,480,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4203.60` | 3,180,000.00 USD | 3,180,000.00 USD | 125,260.00 USD | 0.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,740,000.00 USD | 14,740,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4207.80` | 3,220,000.00 USD | 3,220,000.00 USD | 30,560.00 USD | 0.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 14,870,000.00 USD | 14,870,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.00` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 14,980,000.00 USD | 14,980,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4216.20` | 3,300,000.00 USD | 3,300,000.00 USD | 68,400.00 USD | 0.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,090,000.00 USD | 15,090,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4220.40` | 3,350,000.00 USD | 3,350,000.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,200,000.00 USD | 15,200,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4224.60` | 3,370,000.00 USD | 3,370,000.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,290,000.00 USD | 15,290,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4228.80` | 3,400,000.00 USD | 3,400,000.00 USD | 27,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,330,000.00 USD | 15,330,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4233.00` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,380,000.00 USD | 15,380,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,390,000.00 USD | 15,390,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,530,000.00 USD | 15,530,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,670,000.00 USD | 15,670,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,800,000.00 USD | 15,800,000.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 15,920,000.00 USD | 15,920,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 15,980,000.00 USD | 15,980,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4417.80` | 3,430,000.00 USD | 3,430,000.00 USD | 23,120.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,090,000.00 USD | 16,090,000.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.00` | 3,450,000.00 USD | 3,450,000.00 USD | 13,580.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,140,000.00 USD | 16,140,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.20` | 3,480,000.00 USD | 3,480,000.00 USD | 30,460.00 USD | 0.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,220,000.00 USD | 16,220,000.00 USD | 65,320.00 USD | 0.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.40` | 3,550,000.00 USD | 3,550,000.00 USD | 56,840.00 USD | 0.00 USD | 8,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,380,000.00 USD | 16,380,000.00 USD | 154,640.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4434.60` | 3,580,000.00 USD | 3,580,000.00 USD | 33,230.00 USD | 0.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,490,000.00 USD | 16,490,000.00 USD | 95,850.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4438.70` | 3,610,000.00 USD | 3,610,000.00 USD | 21,740.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,620,000.00 USD | 16,620,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,690,000.00 USD | 16,690,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,740,000.00 USD | 16,740,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,440,000.00 USD | 0.00 USD | 16,440,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,360,000.00 USD | 0.00 USD | 16,360,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3615.60` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 28,900.00 USD | 0.00 USD | 2,470.00 USD |
| `1D` | `3619.80` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 24,570.00 USD | 0.00 USD | 3,540.00 USD |
| `7D` | `3619.80` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3624.00` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 60,480.00 USD | 0.00 USD | 7,490.00 USD |
| `7D` | `3624.10` | 16,160,000.00 USD | 0.00 USD | 16,160,000.00 USD | 88,630.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3628.20` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 43,260.00 USD | 0.00 USD | 6,480.00 USD |
| `7D` | `3628.40` | 16,050,000.00 USD | 0.00 USD | 16,050,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3632.40` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 21,740.00 USD | 0.00 USD | 5,630.00 USD |
| `7D` | `3632.70` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 103,510.00 USD | 0.00 USD | 13,730.00 USD |
| `1D` | `3636.60` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 47,040.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `3637.00` | 15,740,000.00 USD | 0.00 USD | 15,740,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3640.80` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 15,030.00 USD | 0.00 USD | 7,450.00 USD |
| `7D` | `3641.30` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3645.00` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 3,610.00 USD | 0.00 USD | 3,970.00 USD |
| `7D` | `3645.60` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3649.20` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 21,830.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3649.90` | 15,510,000.00 USD | 0.00 USD | 15,510,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3653.40` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 16,880.00 USD | 0.00 USD | 977.78 USD |
| `7D` | `3654.20` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3657.60` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 5,110.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3658.50` | 15,430,000.00 USD | 0.00 USD | 15,430,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3661.80` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 2,940.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3662.80` | 15,420,000.00 USD | 0.00 USD | 15,420,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3667.10` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3830.50` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 14,970,000.00 USD | 0.00 USD | 14,970,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,450,000.00 USD | 0.00 USD | 14,450,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD |
| `7D` | `3852.00` | 13,920,000.00 USD | 0.00 USD | 13,920,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3855.00` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `3856.30` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3859.20` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 68,860.00 USD | 0.00 USD | 4,400.00 USD |
| `7D` | `3860.60` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3863.40` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 105,760.00 USD | 0.00 USD | 11,120.00 USD |
| `7D` | `3864.90` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 289,880.00 USD | 0.00 USD | 58,570.00 USD |
| `1D` | `3867.60` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 202,490.00 USD | 0.00 USD | 28,420.00 USD |
| `7D` | `3869.20` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 631,610.00 USD | 0.00 USD | 39,700.00 USD |
| `1D` | `3871.80` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 174,900.00 USD | 0.00 USD | 18,190.00 USD |
| `7D` | `3873.50` | 12,010,000.00 USD | 0.00 USD | 12,010,000.00 USD | 309,370.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3876.00` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 67,070.00 USD | 0.00 USD | 9,470.00 USD |
| `7D` | `3877.80` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `3880.20` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 147,450.00 USD | 0.00 USD | 20,220.00 USD |
| `7D` | `3882.10` | 11,060,000.00 USD | 0.00 USD | 11,060,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3884.40` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 30,560.00 USD | 0.00 USD | 13,950.00 USD |
| `7D` | `3886.40` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3888.60` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 9,190.00 USD |
| `7D` | `3890.70` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3892.80` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 78,150.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `3895.00` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3897.00` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 43,750.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `3899.30` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3901.20` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 21,270.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3903.60` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3905.40` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 15,640.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.90` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3912.20` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `7D` | `3916.50` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `7D` | `3933.70` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3934.80` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3938.00` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3939.00` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 160,570.00 USD | 0.00 USD | 8,800.00 USD |
| `7D` | `3942.30` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 375,470.00 USD | 0.00 USD | 60,430.00 USD |
| `1D` | `3943.20` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 178,160.00 USD | 0.00 USD | 18,170.00 USD |
| `7D` | `3946.60` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 617,970.00 USD | 0.00 USD | 132,630.00 USD |
| `1D` | `3947.40` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 418,420.00 USD | 0.00 USD | 51,570.00 USD |
| `7D` | `3950.90` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 1,120,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3951.60` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 272,600.00 USD | 0.00 USD | 43,470.00 USD |
| `7D` | `3955.20` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 734,780.00 USD | 0.00 USD | 66,110.00 USD |
| `1D` | `3955.80` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 176,910.00 USD | 0.00 USD | 20,170.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3960.00` | 853,620.00 USD | 0.00 USD | 853,620.00 USD | 284,040.00 USD | 0.00 USD | 24,800.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3964.20` | 544,770.00 USD | 0.00 USD | 544,770.00 USD | 95,580.00 USD | 0.00 USD | 40,960.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3968.40` | 408,230.00 USD | 0.00 USD | 408,230.00 USD | 30,740.00 USD | 0.00 USD | 19,790.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3972.60` | 357,700.00 USD | 0.00 USD | 357,700.00 USD | 127,000.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3976.80` | 223,400.00 USD | 0.00 USD | 223,400.00 USD | 109,130.00 USD | 0.00 USD | 8,700.00 USD |
| `1D` | `3981.00` | 105,580.00 USD | 0.00 USD | 105,580.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3985.20` | 64,500.00 USD | 0.00 USD | 64,500.00 USD | 54,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3989.40` | 9,870.00 USD | 0.00 USD | 9,870.00 USD | 0.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4019.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4021.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD |
| `7D` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4094.40` | 29,250.00 USD | 29,250.00 USD | 0.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4098.60` | 208,440.00 USD | 208,440.00 USD | 0.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD |
| `7D` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4102.80` | 374,660.00 USD | 374,660.00 USD | 0.00 USD | 149,750.00 USD | 0.00 USD | 16,470.00 USD |
| `7D` | `4105.70` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 606,780.00 USD | 0.00 USD | 103,510.00 USD |
| `1D` | `4107.00` | 788,360.00 USD | 788,360.00 USD | 0.00 USD | 372,780.00 USD | 0.00 USD | 40,920.00 USD |
| `7D` | `4110.00` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 68,720.00 USD |
| `1D` | `4111.20` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 288,670.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `4114.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 751,280.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4115.40` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 232,080.00 USD | 0.00 USD | 30,280.00 USD |
| `7D` | `4118.60` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD |
| `1D` | `4119.60` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 185,550.00 USD | 0.00 USD | 9,560.00 USD |
| `7D` | `4122.90` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4123.80` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 210,630.00 USD | 0.00 USD | 43,960.00 USD |
| `7D` | `4127.20` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4128.00` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 45,250.00 USD | 0.00 USD | 23,060.00 USD |
| `7D` | `4131.50` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4132.20` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 41,070.00 USD | 0.00 USD | 17,850.00 USD |
| `7D` | `4135.80` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4136.40` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 121,070.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `4140.10` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4140.60` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 81,660.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4144.40` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4144.80` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 32,780.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4148.70` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4149.00` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 41,040.00 USD | 0.00 USD | 7,890.00 USD |
| `7D` | `4153.00` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `1D` | `4153.20` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `4157.30` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.60` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.90` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `1D` | `4174.20` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 3,530.00 USD |
| `7D` | `4174.50` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4178.40` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 74,700.00 USD | 0.00 USD | 3,700.00 USD |
| `7D` | `4178.80` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4182.60` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 74,470.00 USD | 0.00 USD | 8,050.00 USD |
| `7D` | `4183.10` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 30,210.00 USD |
| `1D` | `4186.80` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 179,480.00 USD | 0.00 USD | 19,900.00 USD |
| `7D` | `4187.40` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 292,190.00 USD | 0.00 USD | 50,790.00 USD |
| `1D` | `4191.00` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 129,190.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `4191.70` | 13,660,000.00 USD | 13,660,000.00 USD | 0.00 USD | 616,630.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4195.20` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 132,410.00 USD | 0.00 USD | 16,070.00 USD |
| `7D` | `4196.00` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 286,520.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4199.40` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 80,330.00 USD | 0.00 USD | 7,060.00 USD |
| `7D` | `4200.30` | 14,480,000.00 USD | 14,480,000.00 USD | 0.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD |
| `1D` | `4203.60` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 125,260.00 USD | 0.00 USD | 20,220.00 USD |
| `7D` | `4204.60` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4207.80` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 30,560.00 USD | 0.00 USD | 12,920.00 USD |
| `7D` | `4208.90` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4212.00` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,230.00 USD |
| `7D` | `4213.20` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4216.20` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 68,400.00 USD | 0.00 USD | 2,560.00 USD |
| `7D` | `4217.50` | 15,090,000.00 USD | 15,090,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4220.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD |
| `7D` | `4221.80` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4224.60` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4226.10` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4228.80` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 27,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4230.40` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4233.00` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `4234.70` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.00` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4389.50` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `7D` | `4415.30` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4417.80` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 23,120.00 USD | 0.00 USD | 2,280.00 USD |
| `7D` | `4419.60` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4422.00` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 13,580.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4423.90` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4426.20` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 30,460.00 USD | 0.00 USD | 2,950.00 USD |
| `7D` | `4428.20` | 16,220,000.00 USD | 16,220,000.00 USD | 0.00 USD | 65,320.00 USD | 0.00 USD | 17,120.00 USD |
| `1D` | `4430.40` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 56,840.00 USD | 0.00 USD | 8,420.00 USD |
| `7D` | `4432.50` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 154,640.00 USD | 0.00 USD | 11,860.00 USD |
| `1D` | `4434.60` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 33,230.00 USD | 0.00 USD | 4,980.00 USD |
| `7D` | `4436.80` | 16,490,000.00 USD | 16,490,000.00 USD | 0.00 USD | 95,850.00 USD | 0.00 USD | 10,990.00 USD |
| `1D` | `4438.70` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 21,740.00 USD | 0.00 USD | 5,190.00 USD |
| `7D` | `4441.10` | 16,620,000.00 USD | 16,620,000.00 USD | 0.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `4445.40` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,740,000.00 USD | 16,740,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.69M` | Total OI Tokens: `68,296.5 PAXG`
  * 1h OI Change: `-0.01%` | 4h OI Change: `-0.21%` | 24h OI Change: `+0.01%`
  * Exchange Breakdown: Binance=`107.11M` | Bybit=`19.91M` | OKX=`-` | Hyperliquid=`24.71M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.35K` | Last 24h: `25.45K` | Last 3d: `95.42K` | Last 7d: `223.50K`
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
| `15M` | `PAXG` | `18.40%` | `81.60%` | `0.23` | 13,850,000.00 USD |
| `15M` | `Binance` | `37.5%` | `62.5%` | `0.60` | 1,120,000.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `29.28%` | `70.72%` | `0.41` | 664,150.00 USD |
| `15M` | `KuCoin` | `4.92%` | `95.08%` | `0.05` | 110,210.00 USD |
| `15M` | `Gate` | `29.66%` | `70.34%` | `0.42` | 466,510.00 USD |
| `15M` | `Bitget` | `59.43%` | `40.57%` | `1.46` | 184,510.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `10.41%` | `89.59%` | `0.12` | 10,180,000.00 USD |
| `15M` | `Bitunix` | `32.5%` | `67.5%` | `0.48` | 346,380.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `72.12%` | `27.88%` | `2.59` | 693,460.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `1.97%` | `98.03%` | `0.02` | 65,130.00 USD |
| `15M` | `HTX` | `8.76%` | `91.24%` | `0.10` | 1,510.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `41.64%` | `58.36%` | `0.71` | 8,290.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `37.5%` | `62.5%` | `0.60` | 1,120,000.00 USD |
| `15M` | `Global Accounts` | `18.40%` | `81.60%` | `0.23` | 13,850,000.00 USD |
| `1H` | `PAXG` | `47.21%` | `52.79%` | `0.89` | 6,990,000.00 USD |
| `1H` | `Binance` | `47.49%` | `52.51%` | `0.90` | 4,150,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `47.64%` | `52.36%` | `0.91` | 229,420.00 USD |
| `1H` | `KuCoin` | `60.2%` | `39.8%` | `1.51` | 472,140.00 USD |
| `1H` | `Gate` | `48.58%` | `51.42%` | `0.94` | 78,520.00 USD |
| `1H` | `Bitget` | `53.83%` | `46.17%` | `1.17` | 844,700.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `32.66%` | `67.34%` | `0.49` | 34,690.00 USD |
| `1H` | `Bitunix` | `35.36%` | `64.64%` | `0.55` | 165,940.00 USD |
| `1H` | `Hyperliquid` | `18.76%` | `81.24%` | `0.23` | 573,560.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `61.13%` | `38.87%` | `1.57` | 404,740.00 USD |
| `1H` | `HTX` | `37.65%` | `62.35%` | `0.60` | 16,870.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `83.25%` | `16.75%` | `4.97` | 3,390.00 USD |
| `1H` | `Aster` | `15.66%` | `84.34%` | `0.19` | 1,960.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `56.61%` | `43.39%` | `1.30` | 12,290.00 USD |
| `1H` | `Whale Positions` | `47.49%` | `52.51%` | `0.90` | 4,150,000.00 USD |
| `1H` | `Global Accounts` | `47.21%` | `52.79%` | `0.89` | 6,990,000.00 USD |
| `4H` | `PAXG` | `49.31%` | `50.69%` | `0.97` | 19,050,000.00 USD |
| `4H` | `Binance` | `50.3%` | `49.7%` | `1.01` | 10,500,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `54.84%` | `45.16%` | `1.21` | 465,600.00 USD |
| `4H` | `KuCoin` | `53.4%` | `46.6%` | `1.15` | 1,340,000.00 USD |
| `4H` | `Gate` | `66.38%` | `33.62%` | `1.97` | 279,040.00 USD |
| `4H` | `Bitget` | `53.32%` | `46.68%` | `1.14` | 1,890,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `10.32%` | `89.68%` | `0.12` | 582,540.00 USD |
| `4H` | `Bitunix` | `43.64%` | `56.36%` | `0.77` | 339,850.00 USD |
| `4H` | `Hyperliquid` | `34.17%` | `65.83%` | `0.52` | 2,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `67.11%` | `32.89%` | `2.04` | 1,460,000.00 USD |
| `4H` | `HTX` | `54.73%` | `45.27%` | `1.21` | 56,060.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.37%` | `57.63%` | `0.74` | 38,760.00 USD |
| `4H` | `Aster` | `41.73%` | `58.27%` | `0.72` | 22,070.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `24.66%` | `75.34%` | `0.33` | 76,870.00 USD |
| `4H` | `Whale Positions` | `50.3%` | `49.7%` | `1.01` | 10,500,000.00 USD |
| `4H` | `Global Accounts` | `49.31%` | `50.69%` | `0.97` | 19,050,000.00 USD |


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
| `5m` | -191,580.00 USD | 64,160.00 USD | **`DISTRIBUTION`** |
| `15m` | -238,790.00 USD | -45,600.00 USD | **`DISTRIBUTION`** |
| `30m` | -142,330.00 USD | -456,340.00 USD | **`DISTRIBUTION`** |
| `1h` | -53,860.00 USD | -74,450.00 USD | **`DISTRIBUTION`** |
| `2h` | 81,010.00 USD | -368,640.00 USD | **`DISTRIBUTION`** |
| `4h` | -531,620.00 USD | 105,390.00 USD | **`DISTRIBUTION`** |
| `6h` | 225,000.00 USD | 616,600.00 USD | **`ACCUMULATION`** |
| `8h` | -127,980.00 USD | 1,000,000.00 USD | **`ACCUMULATION`** |
| `12h` | -365,460.00 USD | 1,230,000.00 USD | **`ACCUMULATION`** |
| `24h` | 59,750.00 USD | 1,580,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,060,000.00 USD | -7,910,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,980,000.00 USD | -71,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-191.58K` | 15m=`-238.79K` | 1h=`-53.86K` | 24h=`+59.75K`
* Futures Capital Netflows: 5m=`+64.16K` | 15m=`-45.60K` | 1h=`-74.45K` | 24h=`+1.58M`
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
