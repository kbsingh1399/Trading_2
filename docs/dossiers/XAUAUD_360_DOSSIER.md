# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUAUD
**Canonical Key**: `XAUAUD` | **Broker Instrument**: `XAUAUD.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-29 22:49:01 IST` (`2026-10-29 17:19:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `5716.15` | **Live Ask Quote**: `5716.63` | **Mid Price**: `5716.39`
- **Spread Points**: `48.00` | **Spread BPS**: `0.84 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `100.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `1.00 USD` | Point Value (0.01 Lot): `0.0100 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `4031.73` | VWAP Z-Score: `-1.20` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `8.11` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.79` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.86` | Lower -3.00σ Band: `3998.61`
  * Upper +2.51σ Band: `4059.45` | Lower -2.51σ Band: `4004.02`
  * Upper +2.01σ Band: `4053.92` | Lower -2.01σ Band: `4009.54`
  * Upper +2.00σ Band: `4053.81` | Lower -2.00σ Band: `4009.65`
  * Upper +1.28σ Band: `4045.87` | Lower -1.28σ Band: `4017.60`
  * Upper +1.00σ Band: `4042.77` | Lower -1.00σ Band: `4020.69`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4019.99` | EMA-20=`4022.90` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4028.40` (Slope: `+0.0000`) | EMA-100=`4033.93`
  * Institutional Anchors: EMA-144=`4034.66` | EMA-200=`4033.61` (Slope: `-0.0346`) | EMA-233=`4032.43`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4010.16` | Weekly High=`4082.75` | Weekly Low=`3988.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `5737.23` (Distance: `-0.37%`)
  * Point of Control (POC) = `5727.85` (Distance: `-0.21%`)
  * Value Area Low (VAL) = `5715.67` (Distance: `+0.01%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`5764.78` | POC=`5754.66` | VAL=`5735.88`
  * Prior Day Extremes: PDH=`5785.73` | PDL=`5713.48` | PDC=`5765.90`
  * Monday Range Blueprint: High=`5739.86` | Mid=`5698.93` | Low=`5658.00`
  * Developing Weekly Value Area: Weekly VAH=`5754.65` | Weekly POC=`5728.25` | Weekly VAL=`5702.71`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`5767.92` | Low=`5722.11`
  * London Session (08:00-16:00 UTC): High=`5737.22` | Low=`5707.15`
  * New York Session (13:00-21:00 UTC): High=`5748.81` | Low=`5697.63`
  * Initial Balance (First Hour): IB High=`5734.96` | IB Low=`5707.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `5693.52` - `5739.26`
  * Optimal Trade Entry (OTE 0.705): `5727.82`
  * Structural Invalidation Anchor (0.786): `5762.12`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4023.30` | `4024.01` | `4022.15` | `4022.67` | `23` | 91,006.45 USD | -11,562.25 USD | `-12.70%` | 966,104.60 USD | `-0.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `4022.71` | `4027.05` | `4022.71` | `4027.05` | `51` | 204,320.84 USD | 79,817.65 USD | `+39.06%` | 1,045,922.25 USD | `+0.39` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4027.05` | `4029.00` | `4026.44` | `4026.45` | `67` | 269,723.43 USD | 116,882.30 USD | `+43.33%` | 1,162,804.55 USD | `+0.71` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4019.60` | `4021.70` | `4017.67` | `4021.36` | `133` | 536,295.57 USD | -74,630.45 USD | `-13.92%` | 494,219.57 USD | `-0.70` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4021.36` | `4023.30` | `4019.39` | `4023.30` | `201` | 809,848.30 USD | 483,447.28 USD | `+59.70%` | 977,666.85 USD | `+2.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4023.30` | `4029.00` | `4022.15` | `4026.45` | `140` | 565,042.67 USD | 185,129.64 USD | `+32.76%` | 1,162,796.49 USD | `+0.72` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4029.13` | `4030.46` | `4023.08` | `4026.82` | `526` | 2,116,236.19 USD | -146,951.88 USD | `-6.94%` | -157,920.93 USD | `-0.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4026.82` | `4026.82` | `4016.00` | `4023.30` | `951` | 3,823,725.36 USD | 850,414.22 USD | `+22.24%` | 692,493.29 USD | `+1.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4023.30` | `4029.00` | `4022.15` | `4026.45` | `140` | 565,050.72 USD | 185,137.69 USD | `+32.76%` | 877,630.98 USD | `+0.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4016.00` | `4026.45` | `1,091` | 4,388,772.05 USD | 1,035,547.88 USD | `+23.60%` | 1,412,598.16 USD | `+1.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4016.00` | `4026.45` | `1,091` | 4,388,772.05 USD | 1,035,547.88 USD | `+23.60%` | 1,412,598.16 USD | `+1.43` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4020.80` | `1.9419` | 7,807.99 USD | 1,590,900.30 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4020.90` | `8.1991` | 32,967.76 USD | 1,583,092.30 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4021.00` | `6.8726` | 27,634.72 USD | 1,550,124.54 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4021.10` | `10.9684` | 44,105.03 USD | 1,522,489.82 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4021.20` | `17.0225` | 68,450.88 USD | 1,478,384.79 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4021.30` | `127.8459` | 514,106.72 USD | 1,409,933.91 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `4021.40` | `4.1419` | 16,656.24 USD | 895,827.19 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4021.50` | `14.9051` | 59,940.86 USD | 879,170.95 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4021.60` | `8.5463` | 34,369.80 USD | 819,230.09 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4021.70` | `3.8986` | 15,679.00 USD | 784,860.29 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4021.80` | `12.8333` | 51,612.97 USD | 769,181.29 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4022.00` | `63.1664` | 254,055.26 USD | 717,568.33 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4022.10` | `7.6757` | 30,872.43 USD | 463,513.07 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4022.20` | `41.0424` | 165,080.74 USD | 432,640.64 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4022.30` | `7.8028` | 31,385.20 USD | 267,559.89 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4022.40` | `17.8688` | 71,875.46 USD | 236,174.69 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4022.50` | `36.4668` | 146,687.70 USD | 164,299.23 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4022.60` | `1.3319` | 5,357.70 USD | 17,611.53 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4022.70` | `0.2485` | 999.64 USD | 12,253.83 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `4022.80` | `2.7976` | 11,254.19 USD | 11,254.19 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4022.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,022.85` | `0.00%` | `-` |
| `ASK` | `4022.90` | `12.8762` | 51,799.66 USD | 51,799.66 USD | `7 orders` | `+0.00%` | `-` |
| `ASK` | `4023.00` | `14.5241` | 58,430.45 USD | 110,230.12 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `4023.20` | `10.5846` | 42,583.96 USD | 152,814.08 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4023.30` | `6.1798` | 24,863.19 USD | 177,677.27 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4023.40` | `27.2798` | 109,757.55 USD | 287,434.82 USD | `13 orders` | `+0.01%` | `-` |
| `ASK` | `4023.50` | `20.9442` | 84,268.99 USD | 371,703.81 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4023.60` | `51.0499` | 205,404.38 USD | 577,108.18 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4023.70` | `9.1139` | 36,671.60 USD | 613,779.78 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4023.80` | `3.2957` | 13,261.24 USD | 627,041.02 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4023.90` | `17.6041` | 70,837.14 USD | 697,878.16 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `4024.00` | `70.8998` | 285,300.80 USD | 983,178.96 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `4024.10` | `12.2340` | 49,230.84 USD | 1,032,409.79 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4024.20` | `7.1793` | 28,890.94 USD | 1,061,300.73 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4024.30` | `1.9065` | 7,672.33 USD | 1,068,973.06 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4024.40` | `15.6287` | 62,896.14 USD | 1,131,869.20 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `4024.50` | `7.9026` | 31,804.01 USD | 1,163,673.22 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4024.60` | `5.5310` | 22,260.06 USD | 1,185,933.28 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4024.70` | `58.5952` | 235,828.10 USD | 1,421,761.38 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4024.80` | `22.2723` | 89,641.55 USD | 1,511,402.93 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `4024.90` | `8.4390` | 33,966.13 USD | 1,545,369.06 USD | `4 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `56` | `0x5b5d...c060` | `SHORT` | 25,636,130.83 USD | `6,373.66` | `4191.43` | `4022.80` | `28452.07` | 1,078,670.35 USD | `+4.21%` | `4X Cross` |
| `58` | `0x4692...164f` | `SHORT` | 25,257,644.35 USD | `6,279.09` | `4135.05` | `4022.80` | `13265.21` | 706,769.63 USD | `+2.80%` | `5X Cross` |
| `78` | `0xb83d...6e36` | `SHORT` | 22,995,156.32 USD | `5,717.06` | `4234.49` | `4022.80` | `26731.74` | 1,213,718.91 USD | `+5.28%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,422,829.33 USD | `4,828.91` | `4157.43` | `4022.80` | `2052.74` | -653,052.98 USD | `-3.36%` | `25X Cross` |
| `150` | `0x645b...87b8` | `LONG` | 14,146,407.62 USD | `3,517.08` | `4129.71` | `4022.80` | `29.61` | -378,146.12 USD | `-2.67%` | `3X Cross` |
| `162` | `0x7a6d...f79c` | `SHORT` | 13,145,407.13 USD | `3,268.21` | `4228.94` | `4022.80` | `4406.34` | 675,672.00 USD | `+5.14%` | `25X Cross` |
| `185` | `0xa742...e390` | `SHORT` | 11,664,380.40 USD | `2,900.00` | `4364.92` | `4022.80` | `4235.56` | 993,895.93 USD | `+8.52%` | `20X Cross` |
| `279` | `0x41e5...0825` | `SHORT` | 8,848,840.00 USD | `2,200.00` | `4112.20` | `4022.80` | `4331.05` | 198,014.59 USD | `+2.24%` | `20X Cross` |
| `280` | `0x3678...b209` | `LONG` | 8,847,960.00 USD | `2,200.00` | `4176.09` | `4022.80` | `2401.54` | -339,459.30 USD | `-3.84%` | `25X Cross` |
| `317` | `0xfc66...ca06` | `SHORT` | 7,991,866.04 USD | `1,986.89` | `4032.86` | `4022.80` | `24728.70` | 21,000.13 USD | `+0.26%` | `3X Cross` |
| `318` | `0xacb6...efbd` | `SHORT` | 7,945,329.59 USD | `1,975.37` | `4048.55` | `4022.80` | `6482.59` | 52,062.12 USD | `+0.66%` | `6X Cross` |
| `387` | `0xc26c...b8f4` | `LONG` | 6,354,882.13 USD | `1,579.95` | `4075.62` | `4022.80` | `0.000000` | -84,414.84 USD | `-1.33%` | `1X Cross` |
| `433` | `0x12d2...f97f` | `LONG` | 5,638,894.33 USD | `1,401.94` | `4278.91` | `4022.80` | `2426.80` | -359,896.25 USD | `-6.38%` | `20X Cross` |
| `593` | `0x63da...8add` | `LONG` | 4,022,200.00 USD | `1,000.00` | `4021.46` | `4022.80` | `3564.00` | 739.04 USD | `+0.02%` | `25X Cross` |
| `613` | `0x9aa5...58af` | `LONG` | 3,908,138.45 USD | `971.64` | `4279.98` | `4022.80` | `0.000000` | -250,470.63 USD | `-6.41%` | `20X Cross` |
| `636` | `0xf3dc...1672` | `LONG` | 3,743,078.86 USD | `930.74` | `4024.62` | `4022.80` | `3337.48` | -2,813.70 USD | `-0.08%` | `20X Cross` |
| `688` | `0x354b...6425` | `LONG` | 3,431,509.47 USD | `853.08` | `4037.02` | `4022.80` | `0.000000` | -12,389.44 USD | `-0.36%` | `10X Cross` |
| `702` | `0x4a20...3c26` | `LONG` | 3,367,854.11 USD | `837.40` | `4599.73` | `4022.80` | `0.000000` | -483,966.27 USD | `-14.37%` | `20X Cross` |
| `857` | `0x0fac...7a0a` | `LONG` | 2,761,248.62 USD | `686.49` | `4290.34` | `4022.80` | `1227.89` | -184,010.09 USD | `-6.66%` | `25X Cross` |
| `883` | `0xd8c5...99b0` | `SHORT` | 2,650,160.69 USD | `658.95` | `4175.35` | `4022.80` | `31154.13` | 101,186.37 USD | `+3.82%` | `4X Cross` |
| `935` | `0x625e...a354` | `SHORT` | 2,493,764.00 USD | `620.00` | `4122.81` | `4022.80` | `4342.14` | 62,383.03 USD | `+2.50%` | `20X Cross` |
| `962` | `0xeae3...e8ad` | `SHORT` | 2,413,140.00 USD | `600.00` | `4104.77` | `4022.80` | `4325.17` | 49,725.11 USD | `+2.06%` | `20X Cross` |
| `966` | `0xf285...fa82` | `LONG` | 2,405,701.55 USD | `598.11` | `4146.45` | `4022.80` | `3891.13` | -74,318.00 USD | `-3.09%` | `25X Cross` |
| `982` | `0x12f7...8750` | `LONG` | 2,355,443.36 USD | `585.61` | `4082.77` | `4022.80` | `2121.07` | -35,473.62 USD | `-1.51%` | `10X Cross` |
| `1136` | `0x413c...886c` | `LONG` | 2,010,800.00 USD | `500.00` | `4010.43` | `4022.80` | `0.000000` | 5,583.77 USD | `+0.28%` | `2X Cross` |
| `1144` | `0x61ce...a62b` | `SHORT` | 2,001,207.83 USD | `497.50` | `4071.66` | `4022.80` | `4684.06` | 24,460.96 USD | `+1.22%` | `20X Cross` |
| `1147` | `0x0593...40f9` | `LONG` | 1,995,772.75 USD | `496.18` | `4024.57` | `4022.80` | `3701.62` | -1,131.08 USD | `-0.06%` | `10X Isolated` |
| `1267` | `0xead5...69f2` | `LONG` | 1,825,209.60 USD | `453.78` | `4220.88` | `4022.80` | `3538.83` | -90,158.46 USD | `-4.94%` | `5X Isolated` |
| `1395` | `0x46fc...1195` | `LONG` | 1,637,262.49 USD | `407.03` | `4055.53` | `4022.80` | `1895.67` | -13,447.70 USD | `-0.82%` | `20X Cross` |
| `1435` | `0x6d15...d374` | `LONG` | 1,608,880.00 USD | `400.00` | `4068.25` | `4022.80` | `3841.70` | -18,420.00 USD | `-1.14%` | `25X Cross` |
| `1436` | `0xee02...309d` | `SHORT` | 1,608,880.00 USD | `400.00` | `4438.84` | `4022.80` | `4226.78` | 166,658.60 USD | `+10.36%` | `25X Isolated` |
| `1467` | `0x02a7...fe9f` | `SHORT` | 1,568,658.00 USD | `390.00` | `4055.02` | `4022.80` | `4306.60` | 12,801.25 USD | `+0.82%` | `25X Cross` |
| `1503` | `0x7e77...b8d2` | `SHORT` | 1,528,322.00 USD | `380.00` | `4131.92` | `4022.80` | `4293.41` | 41,807.64 USD | `+2.74%` | `20X Cross` |
| `1521` | `0x72c2...9b37` | `LONG` | 1,500,584.84 USD | `373.13` | `4000.98` | `4022.80` | `3777.93` | 7,691.32 USD | `+0.51%` | `13X Isolated` |
| `1568` | `0xaa44...b844` | `LONG` | 1,447,776.00 USD | `360.00` | `4043.10` | `4022.80` | `2820.88` | -7,741.63 USD | `-0.53%` | `9X Cross` |
| `1680` | `0xa41f...d50a` | `LONG` | 1,323,151.36 USD | `328.96` | `4468.89` | `4022.80` | `3833.08` | -146,946.49 USD | `-11.11%` | `15X Cross` |
| `1709` | `0x49e9...e1d0` | `SHORT` | 1,301,412.17 USD | `323.56` | `4025.23` | `4022.80` | `29785.31` | 980.53 USD | `+0.08%` | `4X Cross` |
| `1728` | `0xada6...6f88` | `LONG` | 1,283,998.75 USD | `319.28` | `4166.46` | `4022.80` | `1850.66` | -46,251.76 USD | `-3.60%` | `5X Cross` |
| `1734` | `0xbf5a...88ba` | `SHORT` | 1,277,671.54 USD | `317.65` | `4091.80` | `4022.80` | `10535.69` | 22,111.49 USD | `+1.73%` | `20X Cross` |
| `1753` | `0xff31...ff6c` | `SHORT` | 1,246,758.00 USD | `310.00` | `4372.43` | `4022.80` | `4789.07` | 108,697.38 USD | `+8.72%` | `10X Isolated` |
| `1933` | `0x50e2...d770` | `LONG` | 1,087,363.61 USD | `270.37` | `4243.58` | `4022.80` | `2561.99` | -59,962.85 USD | `-5.51%` | `20X Cross` |
| `1955` | `0x4c92...4f17` | `SHORT` | 1,072,803.20 USD | `266.72` | `4260.98` | `4022.80` | `6533.46` | 63,689.04 USD | `+5.94%` | `20X Cross` |
| `2014` | `0xd346...c4f3` | `LONG` | 1,026,360.06 USD | `255.17` | `4188.66` | `4022.80` | `3310.31` | -42,476.45 USD | `-4.14%` | `5X Isolated` |
| `2051` | `0x1581...463b` | `LONG` | 1,005,550.00 USD | `250.00` | `4003.77` | `4022.80` | `3504.53` | 4,606.41 USD | `+0.46%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4118.06` (Vol: 271,900.00 USD, Dist: `+2.34%`) | Long MP=`3958.87` (Vol: 230,100.00 USD, Dist: `--1.61%`)
  * 48H Horizon: Short MP=`4118.06` (Vol: 350,900.00 USD, Dist: `+2.34%`) | Long MP=`3958.87` (Vol: 346,400.00 USD, Dist: `--1.61%`)
  * 3D Horizon: Short MP=`4110.46` (Vol: 300,700.00 USD, Dist: `+2.15%`) | Long MP=`3959.21` (Vol: 388,300.00 USD, Dist: `--1.60%`)
  * 7D Horizon: Short MP=`4082.49` (Vol: 552,000.00 USD, Dist: `+1.46%`) | Long MP=`3921.81` (Vol: 617,500.00 USD, Dist: `--2.53%`)
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
| `1D` | `3610.30` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `3610.30` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `1D` | `3614.50` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 4,120.00 USD | 0.00 USD | 12,600.00 USD |
| `7D` | `3614.50` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 4,120.00 USD | 0.00 USD | 12,600.00 USD |
| `1D` | `3618.70` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 9,620.00 USD | 0.00 USD | 25,870.00 USD |
| `7D` | `3618.70` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 8,500.00 USD | 0.00 USD | 24,060.00 USD |
| `1D` | `3622.90` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 17,390.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3622.90` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 17,390.00 USD | 0.00 USD | 69,950.00 USD |
| `1D` | `3627.10` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 25,060.00 USD | 0.00 USD | 26,370.00 USD |
| `7D` | `3627.10` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 25,060.00 USD | 0.00 USD | 26,370.00 USD |
| `1D` | `3631.30` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 45,550.00 USD | 0.00 USD | 56,520.00 USD |
| `7D` | `3631.30` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 45,550.00 USD | 0.00 USD | 56,520.00 USD |
| `1D` | `3635.50` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 39,260.00 USD | 0.00 USD | 23,450.00 USD |
| `7D` | `3635.50` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 39,930.00 USD | 0.00 USD | 23,450.00 USD |
| `1D` | `3639.70` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 12,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3639.70` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 12,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3643.90` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 15,910.00 USD | 0.00 USD | 10,260.00 USD |
| `7D` | `3643.90` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 15,910.00 USD | 0.00 USD | 10,260.00 USD |
| `1D` | `3648.10` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 10,570.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `3648.10` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 10,570.00 USD | 0.00 USD | 21,320.00 USD |
| `1D` | `3652.30` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 19,030.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `3652.30` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 19,030.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `3656.50` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 6,030.00 USD | 0.00 USD | 27,270.00 USD |
| `7D` | `3656.50` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 6,030.00 USD | 0.00 USD | 27,270.00 USD |
| `1D` | `3660.70` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3660.70` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3853.90` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 11,550.00 USD | 0.00 USD | 36,200.00 USD |
| `7D` | `3853.90` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 11,550.00 USD | 0.00 USD | 36,200.00 USD |
| `1D` | `3858.10` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 18,940.00 USD | 0.00 USD | 62,010.00 USD |
| `7D` | `3858.10` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 18,940.00 USD | 0.00 USD | 62,010.00 USD |
| `1D` | `3862.30` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 76,420.00 USD | 0.00 USD | 204,570.00 USD |
| `7D` | `3862.30` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 72,260.00 USD | 0.00 USD | 197,090.00 USD |
| `1D` | `3866.50` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 56,660.00 USD | 0.00 USD | 102,470.00 USD |
| `7D` | `3866.50` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 56,660.00 USD | 0.00 USD | 102,470.00 USD |
| `1D` | `3870.70` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 122,880.00 USD | 0.00 USD | 158,470.00 USD |
| `7D` | `3870.70` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 122,880.00 USD | 0.00 USD | 158,470.00 USD |
| `1D` | `3874.90` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 133,370.00 USD | 0.00 USD | 115,860.00 USD |
| `7D` | `3874.90` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 133,370.00 USD | 0.00 USD | 115,860.00 USD |
| `1D` | `3879.10` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 65,310.00 USD | 0.00 USD | 17,870.00 USD |
| `7D` | `3879.10` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 68,060.00 USD | 0.00 USD | 17,870.00 USD |
| `1D` | `3883.30` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 30,070.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `3883.30` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 30,070.00 USD | 0.00 USD | 3,510.00 USD |
| `1D` | `3887.50` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 30,170.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `3887.50` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 30,170.00 USD | 0.00 USD | 32,130.00 USD |
| `1D` | `3891.70` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 41,760.00 USD | 0.00 USD | 46,800.00 USD |
| `7D` | `3891.70` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 41,760.00 USD | 0.00 USD | 46,800.00 USD |
| `1D` | `3895.90` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 41,330.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `3895.90` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 41,330.00 USD | 0.00 USD | 19,740.00 USD |
| `1D` | `3900.10` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 25,280.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `3900.10` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 25,280.00 USD | 0.00 USD | 69,790.00 USD |
| `1D` | `3904.30` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3904.30` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3933.70` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `7D` | `3933.70` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `1D` | `3937.90` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 45,160.00 USD | 0.00 USD | 120,280.00 USD |
| `7D` | `3937.90` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 45,160.00 USD | 0.00 USD | 120,280.00 USD |
| `1D` | `3942.10` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 116,160.00 USD | 0.00 USD | 308,520.00 USD |
| `7D` | `3942.10` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 107,830.00 USD | 0.00 USD | 293,550.00 USD |
| `1D` | `3946.30` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 134,190.00 USD | 0.00 USD | 303,170.00 USD |
| `7D` | `3946.30` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 134,190.00 USD | 0.00 USD | 303,170.00 USD |
| `1D` | `3950.50` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 203,270.00 USD | 0.00 USD | 198,870.00 USD |
| `7D` | `3950.50` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 203,270.00 USD | 0.00 USD | 198,870.00 USD |
| `1D` | `3954.70` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 215,080.00 USD | 0.00 USD | 331,940.00 USD |
| `7D` | `3954.70` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 215,080.00 USD | 0.00 USD | 331,940.00 USD |
| `1D` | `3958.90` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 199,810.00 USD | 0.00 USD | 69,840.00 USD |
| `7D` | `3958.90` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 205,310.00 USD | 0.00 USD | 69,840.00 USD |
| `1D` | `3963.10` | 749,680.00 USD | 0.00 USD | 749,680.00 USD | 51,840.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3963.10` | 749,680.00 USD | 0.00 USD | 749,680.00 USD | 51,840.00 USD | 0.00 USD | 7,030.00 USD |
| `1D` | `3967.30` | 690,810.00 USD | 0.00 USD | 690,810.00 USD | 107,870.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3967.30` | 690,810.00 USD | 0.00 USD | 690,810.00 USD | 107,870.00 USD | 0.00 USD | 43,420.00 USD |
| `1D` | `3971.50` | 539,520.00 USD | 0.00 USD | 539,520.00 USD | 55,160.00 USD | 0.00 USD | 91,380.00 USD |
| `7D` | `3971.50` | 539,520.00 USD | 0.00 USD | 539,520.00 USD | 55,160.00 USD | 0.00 USD | 91,380.00 USD |
| `1D` | `3975.70` | 392,970.00 USD | 0.00 USD | 392,970.00 USD | 95,320.00 USD | 0.00 USD | 62,540.00 USD |
| `7D` | `3975.70` | 392,970.00 USD | 0.00 USD | 392,970.00 USD | 95,320.00 USD | 0.00 USD | 62,540.00 USD |
| `1D` | `3979.90` | 235,110.00 USD | 0.00 USD | 235,110.00 USD | 37,760.00 USD | 0.00 USD | 58,930.00 USD |
| `7D` | `3979.90` | 235,110.00 USD | 0.00 USD | 235,110.00 USD | 37,760.00 USD | 0.00 USD | 58,930.00 USD |
| `1D` | `3984.10` | 138,420.00 USD | 0.00 USD | 138,420.00 USD | 50,370.00 USD | 0.00 USD | 80,640.00 USD |
| `7D` | `3984.10` | 138,420.00 USD | 0.00 USD | 138,420.00 USD | 50,370.00 USD | 0.00 USD | 80,640.00 USD |
| `1D` | `3988.30` | 7,400.00 USD | 0.00 USD | 7,400.00 USD | 7,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3988.30` | 7,400.00 USD | 0.00 USD | 7,400.00 USD | 7,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4020.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4020.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4093.30` | 78,120.00 USD | 78,120.00 USD | 0.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `7D` | `4093.30` | 78,120.00 USD | 78,120.00 USD | 0.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `1D` | `4097.50` | 224,030.00 USD | 224,030.00 USD | 0.00 USD | 41,480.00 USD | 0.00 USD | 104,430.00 USD |
| `7D` | `4097.50` | 224,030.00 USD | 224,030.00 USD | 0.00 USD | 41,480.00 USD | 0.00 USD | 104,430.00 USD |
| `1D` | `4101.70` | 489,400.00 USD | 489,400.00 USD | 0.00 USD | 73,680.00 USD | 0.00 USD | 191,690.00 USD |
| `7D` | `4101.70` | 472,020.00 USD | 472,020.00 USD | 0.00 USD | 65,360.00 USD | 0.00 USD | 182,640.00 USD |
| `1D` | `4105.90` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 141,490.00 USD | 0.00 USD | 398,230.00 USD |
| `7D` | `4105.90` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 141,490.00 USD | 0.00 USD | 392,320.00 USD |
| `1D` | `4110.10` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 137,710.00 USD | 0.00 USD | 118,510.00 USD |
| `7D` | `4110.10` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 137,710.00 USD | 0.00 USD | 118,510.00 USD |
| `1D` | `4114.30` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 261,050.00 USD | 0.00 USD | 337,060.00 USD |
| `7D` | `4114.30` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 261,050.00 USD | 0.00 USD | 337,060.00 USD |
| `1D` | `4118.50` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 228,880.00 USD | 0.00 USD | 168,370.00 USD |
| `7D` | `4118.50` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 232,210.00 USD | 0.00 USD | 168,370.00 USD |
| `1D` | `4122.70` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 70,150.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `4122.70` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 72,330.00 USD | 0.00 USD | 14,320.00 USD |
| `1D` | `4126.90` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 76,320.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `4126.90` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 76,320.00 USD | 0.00 USD | 19,170.00 USD |
| `1D` | `4131.10` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 69,470.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `4131.10` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 69,470.00 USD | 0.00 USD | 52,120.00 USD |
| `1D` | `4135.30` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 58,220.00 USD | 0.00 USD | 93,600.00 USD |
| `7D` | `4135.30` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 58,220.00 USD | 0.00 USD | 93,600.00 USD |
| `1D` | `4139.50` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 82,670.00 USD | 0.00 USD | 39,490.00 USD |
| `7D` | `4139.50` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 82,670.00 USD | 0.00 USD | 39,490.00 USD |
| `1D` | `4143.70` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `4143.70` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `1D` | `4147.90` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4147.90` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4173.10` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 7,910.00 USD | 0.00 USD | 31,150.00 USD |
| `7D` | `4173.10` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 7,910.00 USD | 0.00 USD | 31,150.00 USD |
| `1D` | `4177.30` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 17,630.00 USD | 0.00 USD | 41,130.00 USD |
| `7D` | `4177.30` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 17,630.00 USD | 0.00 USD | 41,130.00 USD |
| `1D` | `4181.50` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 24,180.00 USD | 0.00 USD | 82,950.00 USD |
| `7D` | `4181.50` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 20,010.00 USD | 0.00 USD | 78,420.00 USD |
| `1D` | `4185.70` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 80,920.00 USD | 0.00 USD | 195,570.00 USD |
| `7D` | `4185.70` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 80,920.00 USD | 0.00 USD | 192,620.00 USD |
| `1D` | `4189.90` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 44,580.00 USD | 0.00 USD | 81,570.00 USD |
| `7D` | `4189.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 44,580.00 USD | 0.00 USD | 81,570.00 USD |
| `1D` | `4194.10` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 147,970.00 USD | 0.00 USD | 173,750.00 USD |
| `7D` | `4194.10` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 147,970.00 USD | 0.00 USD | 173,750.00 USD |
| `1D` | `4198.30` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 96,620.00 USD | 0.00 USD | 76,410.00 USD |
| `7D` | `4198.30` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 96,620.00 USD | 0.00 USD | 76,410.00 USD |
| `1D` | `4202.50` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 65,310.00 USD | 0.00 USD | 14,940.00 USD |
| `7D` | `4202.50` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 68,060.00 USD | 0.00 USD | 14,940.00 USD |
| `1D` | `4206.70` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 24,560.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4206.70` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 24,560.00 USD | 0.00 USD | 3,510.00 USD |
| `1D` | `4210.90` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 35,690.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `4210.90` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 35,690.00 USD | 0.00 USD | 25,640.00 USD |
| `1D` | `4215.10` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | 41,760.00 USD |
| `7D` | `4215.10` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | 41,760.00 USD |
| `1D` | `4219.30` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 47,660.00 USD | 0.00 USD | 31,270.00 USD |
| `7D` | `4219.30` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 47,660.00 USD | 0.00 USD | 31,270.00 USD |
| `1D` | `4223.50` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 18,880.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `4223.50` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 18,880.00 USD | 0.00 USD | 29,460.00 USD |
| `1D` | `4227.70` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | 40,320.00 USD |
| `7D` | `4227.70` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | 40,320.00 USD |
| `1D` | `4231.90` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4231.90` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4412.50` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `4412.50` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `1D` | `4416.70` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD | 7,410.00 USD |
| `7D` | `4416.70` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD | 7,410.00 USD |
| `1D` | `4420.90` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 7,370.00 USD | 0.00 USD | 12,930.00 USD |
| `7D` | `4420.90` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 7,370.00 USD | 0.00 USD | 12,930.00 USD |
| `1D` | `4425.10` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 11,750.00 USD | 0.00 USD | 59,900.00 USD |
| `7D` | `4425.10` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD | 58,090.00 USD |
| `1D` | `4426.80` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 6,520.00 USD | 0.00 USD | 16,990.00 USD |
| `7D` | `4426.80` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 6,520.00 USD | 0.00 USD | 16,990.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `841.02M` | Total OI Tokens: `209,178.7 XAUT`
  * 1h OI Change: `-1.10%` | 4h OI Change: `-3.66%` | 24h OI Change: `+5.83%`
  * Exchange Breakdown: Binance=`62.47M` | Bybit=`144.57M` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `147.27K` | Last 24h: `265.18K` | Last 3d: `925.43K` | Last 7d: `2.46M`
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
| `15M` | `XAUT` | `38.95%` | `61.05%` | `0.64` | 3,080,000.00 USD |
| `15M` | `Binance` | `34.18%` | `65.82%` | `0.52` | 1,190,000.00 USD |
| `15M` | `OKX` | `38.95%` | `61.05%` | `0.64` | 734,170.00 USD |
| `15M` | `Bybit` | `25.05%` | `74.95%` | `0.33` | 230,250.00 USD |
| `15M` | `KuCoin` | `47.66%` | `52.34%` | `0.91` | 34,430.00 USD |
| `15M` | `Gate` | `42.95%` | `57.05%` | `0.75` | 46,940.00 USD |
| `15M` | `Bitget` | `54.62%` | `45.38%` | `1.20` | 94,830.00 USD |
| `15M` | `BingX` | `29.62%` | `70.38%` | `0.42` | 84,110.00 USD |
| `15M` | `MEXC` | `33.69%` | `66.31%` | `0.51` | 248,940.00 USD |
| `15M` | `Bitunix` | `35.8%` | `64.2%` | `0.56` | 40,090.00 USD |
| `15M` | `Hyperliquid` | `87.5%` | `12.5%` | `7.00` | 77,510.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.16%` | `49.84%` | `1.01` | 210,120.00 USD |
| `15M` | `Crypto.com` | `42.66%` | `57.34%` | `0.74` | 1,720.00 USD |
| `15M` | `WhiteBIT` | `81.08%` | `18.92%` | `4.29` | 79,160.00 USD |
| `15M` | `HTX` | `20.77%` | `79.23%` | `0.26` | 261.95 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `4.49%` | `95.51%` | `0.05` | 8,210.00 USD |
| `15M` | `Aster` | `1%` | `99%` | `0.01` | 1,150.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `35.21%` | `64.79%` | `0.54` | 3,420.00 USD |
| `15M` | `Whale Positions` | `34.18%` | `65.82%` | `0.52` | 1,190,000.00 USD |
| `15M` | `Global Accounts` | `38.95%` | `61.05%` | `0.64` | 3,080,000.00 USD |
| `1H` | `XAUT` | `40.62%` | `59.38%` | `0.68` | 12,580,000.00 USD |
| `1H` | `Binance` | `37.47%` | `62.53%` | `0.60` | 4,490,000.00 USD |
| `1H` | `OKX` | `35.47%` | `64.53%` | `0.55` | 2,990,000.00 USD |
| `1H` | `Bybit` | `49.43%` | `50.57%` | `0.98` | 1,030,000.00 USD |
| `1H` | `KuCoin` | `52.33%` | `47.67%` | `1.10` | 139,130.00 USD |
| `1H` | `Gate` | `48.04%` | `51.96%` | `0.92` | 380,970.00 USD |
| `1H` | `Bitget` | `37.78%` | `62.22%` | `0.61` | 673,870.00 USD |
| `1H` | `BingX` | `54.21%` | `45.79%` | `1.18` | 418,970.00 USD |
| `1H` | `MEXC` | `31.32%` | `68.68%` | `0.46` | 1,270,000.00 USD |
| `1H` | `Bitunix` | `42.75%` | `57.25%` | `0.75` | 194,560.00 USD |
| `1H` | `Hyperliquid` | `60.52%` | `39.48%` | `1.53` | 170,120.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.94%` | `50.06%` | `1.00` | 406,890.00 USD |
| `1H` | `Crypto.com` | `54.47%` | `45.53%` | `1.20` | 5,420.00 USD |
| `1H` | `WhiteBIT` | `88.97%` | `11.03%` | `8.07` | 340,390.00 USD |
| `1H` | `HTX` | `56.03%` | `43.97%` | `1.27` | 4,340.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `24.56%` | `75.44%` | `0.33` | 31,910.00 USD |
| `1H` | `Aster` | `82.55%` | `17.45%` | `4.73` | 10,660.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `34.5%` | `65.5%` | `0.53` | 14,750.00 USD |
| `1H` | `Whale Positions` | `37.47%` | `62.53%` | `0.60` | 4,490,000.00 USD |
| `1H` | `Global Accounts` | `40.62%` | `59.38%` | `0.68` | 12,580,000.00 USD |
| `4H` | `XAUT` | `47.85%` | `52.15%` | `0.92` | 60,600,000.00 USD |
| `4H` | `Binance` | `44.96%` | `55.04%` | `0.82` | 21,990,000.00 USD |
| `4H` | `OKX` | `49.68%` | `50.32%` | `0.99` | 12,200,000.00 USD |
| `4H` | `Bybit` | `49.2%` | `50.8%` | `0.97` | 5,230,000.00 USD |
| `4H` | `KuCoin` | `46.59%` | `53.41%` | `0.87` | 603,060.00 USD |
| `4H` | `Gate` | `48.8%` | `51.2%` | `0.95` | 1,350,000.00 USD |
| `4H` | `Bitget` | `49.94%` | `50.06%` | `1.00` | 3,740,000.00 USD |
| `4H` | `BingX` | `37.36%` | `62.64%` | `0.60` | 2,870,000.00 USD |
| `4H` | `MEXC` | `44.62%` | `55.38%` | `0.81` | 5,000,000.00 USD |
| `4H` | `Bitunix` | `50.28%` | `49.72%` | `1.01` | 1,380,000.00 USD |
| `4H` | `Hyperliquid` | `52.89%` | `47.11%` | `1.12` | 1,890,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.38%` | `50.62%` | `0.98` | 2,630,000.00 USD |
| `4H` | `Crypto.com` | `48.48%` | `51.52%` | `0.94` | 23,490.00 USD |
| `4H` | `WhiteBIT` | `86.13%` | `13.87%` | `6.21` | 1,350,000.00 USD |
| `4H` | `HTX` | `50.42%` | `49.58%` | `1.02` | 16,420.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `60.23%` | `39.77%` | `1.51` | 140,410.00 USD |
| `4H` | `Aster` | `77.29%` | `22.71%` | `3.40` | 75,550.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.97%` | `53.03%` | `0.89` | 119,400.00 USD |
| `4H` | `Whale Positions` | `44.96%` | `55.04%` | `0.82` | 21,990,000.00 USD |
| `4H` | `Global Accounts` | `47.85%` | `52.15%` | `0.92` | 60,600,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4038.45` | `4039.21` | `4038.45` | `4044.45` | `4033.95` | 27,240,137.17 USD | 11,767,150.02 USD | 15,472,987.15 USD | -3,705,837.13 USD | `-13.60%` | `1B / 8S` |
| `0:00 UTC` | `4031.85` | `4032.39` | `4031.85` | `4035.45` | `4029.75` | 19,957,078.91 USD | 8,693,953.80 USD | 11,263,125.11 USD | -2,569,171.31 USD | `-12.87%` | `0B / 1S` |
| `5:00 UTC` | `4030.35` | `4029.61` | `4030.35` | `4031.85` | `4027.35` | 28,806,935.84 USD | 12,003,806.54 USD | 16,803,129.30 USD | -4,799,322.75 USD | `-16.66%` | `0B / 1S` |
| `0:00 UTC` | `4032.75` | `4032.21` | `4032.75` | `4033.95` | `4030.35` | 24,251,255.66 USD | 11,335,444.57 USD | 12,915,811.09 USD | -1,580,366.52 USD | `-6.52%` | `0B / 2S` |
| `5:00 UTC` | `4028.85` | `4029.33` | `4028.85` | `4032.45` | `4026.75` | 27,633,720.84 USD | 14,667,923.52 USD | 12,965,797.32 USD | 1,702,126.19 USD | `+6.16%` | `3B / 0S` |
| `0:00 UTC` | `4022.85` | `4023.63` | `4022.85` | `4030.65` | `4017.75` | 50,953,409.81 USD | 20,150,897.83 USD | 30,802,511.97 USD | -10,651,614.14 USD | `-20.90%` | `3B / 16S` |
| `5:00 UTC` | `4023.45` | `4023.44` | `4023.45` | `4025.25` | `4021.65` | 20,710,982.12 USD | 10,208,497.33 USD | 10,502,484.80 USD | -293,987.47 USD | `-1.42%` | `0B / 0S` |
| `0:00 UTC` | `4020.15` | `4021.78` | `4020.15` | `4024.35` | `4019.55` | 13,323,426.37 USD | 6,724,680.36 USD | 6,598,746.01 USD | 125,934.34 USD | `+0.95%` | `2B / 0S` |
| `5:00 UTC` | `4024.95` | `4023.96` | `4024.95` | `4025.85` | `4021.05` | 10,712,179.92 USD | 5,438,050.75 USD | 5,274,129.18 USD | 163,921.57 USD | `+1.53%` | `0B / 1S` |
| `0:00 UTC` | `4029.15` | `4028.22` | `4029.15` | `4033.05` | `4024.65` | 20,514,732.34 USD | 13,525,757.60 USD | 6,988,974.74 USD | 6,536,782.86 USD | `+31.86%` | `8B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_AUD (XAUAUD.pi) Metal Auction: ROTA | `5747.46` | 0.00 USD | 0.00 USD |
| `10-28 20:04` | `Volume 5.0K XAU` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `4045.20` | 1,000.00 USD | 0.00 USD |
| `10-28 17:48` | `Volume 5.0K XAU` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `4068.50` | 2,200.00 USD | 0.00 USD |
| `10-28 16:57` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4052.80` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 10:56` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4041.20` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD (XAUUSD.pi) Metal Auction: ROTATION | `4045.64` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_EUR (XAUEUR.pi) Metal Auction: ROTA | `3633.06` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_GBP (XAUGBP.pi) Metal Auction: ROTA | `3040.99` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -39,730.00 USD | -39,870.00 USD | **`DISTRIBUTION`** |
| `15m` | -11,970.00 USD | -34,240.00 USD | **`DISTRIBUTION`** |
| `30m` | -76,730.00 USD | -41,550.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,800.00 USD | -91,730.00 USD | **`DISTRIBUTION`** |
| `2h` | -93,250.00 USD | -121,380.00 USD | **`DISTRIBUTION`** |
| `4h` | -520,560.00 USD | 351,720.00 USD | **`DISTRIBUTION`** |
| `6h` | 280,770.00 USD | -152,100.00 USD | **`ACCUMULATION`** |
| `8h` | 952,450.00 USD | -199,140.00 USD | **`ACCUMULATION`** |
| `12h` | 1,850,000.00 USD | -706,700.00 USD | **`ACCUMULATION`** |
| `24h` | -577,680.00 USD | -47,130.00 USD | **`DISTRIBUTION`** |
| `1w` | -85,570,000.00 USD | -21,890,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -177,050,000.00 USD | -85,800,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-39.73K` | 15m=`-11.97K` | 1h=`-2.80K` | 24h=`-577.68K`
* Futures Capital Netflows: 5m=`-39.87K` | 15m=`-34.24K` | 1h=`-91.73K` | 24h=`-47.13K`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `5715.67` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `5705.21` (Risk Distance: `10.46` pts)
  * +2.5R Take Profit: `5741.81`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `5737.23` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `5747.69` (Risk Distance: `10.46` pts)
  * +2.5R Take Profit: `5711.09`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`5762.12`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
