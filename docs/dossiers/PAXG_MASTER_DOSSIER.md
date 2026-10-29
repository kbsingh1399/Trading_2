# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-29 23:37:49 IST` (`2026-10-29 18:07:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4009.55` | **Live Ask Quote**: `4009.64` | **Mid Price**: `4009.60`
- **Spread Points**: `9.00` | **Spread BPS**: `0.22 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `4030.98` | VWAP Z-Score: `-2.11` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `8.02` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `34.74` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.88` | Lower -3.00σ Band: `3997.08`
  * Upper +2.51σ Band: `4059.35` | Lower -2.51σ Band: `4002.62`
  * Upper +2.01σ Band: `4053.70` | Lower -2.01σ Band: `4008.27`
  * Upper +2.00σ Band: `4053.58` | Lower -2.00σ Band: `4008.38`
  * Upper +1.28σ Band: `4045.45` | Lower -1.28σ Band: `4016.52`
  * Upper +1.00σ Band: `4042.28` | Lower -1.00σ Band: `4019.68`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4016.32` | EMA-20=`4020.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4026.39` (Slope: `+0.0000`) | EMA-100=`4032.46`
  * Institutional Anchors: EMA-144=`4033.54` | EMA-200=`4032.91` (Slope: `-0.0466`) | EMA-233=`4031.93`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4006.70` | Weekly High=`4082.75` | Weekly Low=`3988.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4041.12` (Distance: `-0.77%`)
  * Point of Control (POC) = `4027.35` (Distance: `-0.43%`)
  * Value Area Low (VAL) = `4019.01` (Distance: `-0.22%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.72` | Weekly POC=`4015.46` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3993.56` - `4025.63`
  * Optimal Trade Entry (OTE 0.705): `4017.61`
  * Structural Invalidation Anchor (0.786): `4041.67`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4014.52` | `4014.79` | `4011.95` | `4011.96` | `59` | 237,263.59 USD | -40,433.29 USD | `-17.04%` | 457,804.30 USD | `-0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4011.95` | `4013.92` | `4011.95` | `4013.92` | `39` | 156,363.07 USD | 22,668.30 USD | `+14.50%` | 480,472.61 USD | `+0.09` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `4013.92` | `4014.73` | `4013.92` | `4014.41` | `3` | 12,577.44 USD | -5,793.27 USD | `-46.06%` | 474,679.34 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4023.50` | `4025.66` | `4017.14` | `4018.05` | `81` | 323,985.33 USD | -88,175.28 USD | `-27.22%` | 771,400.69 USD | `-0.78` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4018.05` | `4018.76` | `4011.95` | `4011.96` | `238` | 956,530.83 USD | -295,289.50 USD | `-30.87%` | 476,111.20 USD | `-1.70` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4011.95` | `4014.73` | `4011.95` | `4014.41` | `42` | 168,940.51 USD | 16,875.04 USD | `+9.99%` | 492,986.23 USD | `-0.06` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4026.82` | `4026.82` | `4016.00` | `4023.30` | `951` | 3,823,725.36 USD | 850,414.22 USD | `+22.24%` | 1,062,379.10 USD | `+1.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4023.30` | `4029.00` | `4011.95` | `4011.96` | `549` | 2,206,317.77 USD | -210,291.82 USD | `-9.53%` | 852,087.28 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4011.95` | `4014.73` | `4011.95` | `4014.41` | `42` | 168,940.51 USD | 16,875.04 USD | `+9.99%` | 868,962.32 USD | `-0.14` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.95` | `4014.41` | `1,542` | 6,198,983.64 USD | 656,997.44 USD | `+10.60%` | 1,034,047.71 USD | `+1.01` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.95` | `4014.41` | `1,542` | 6,198,983.64 USD | 656,997.44 USD | `+10.60%` | 1,034,047.71 USD | `+1.01` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4009.40` | `4.0126` | 16,088.12 USD | 1,614,086.14 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4009.50` | `10.7103` | 42,942.95 USD | 1,597,998.03 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4009.60` | `83.7462` | 335,788.76 USD | 1,555,055.08 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4009.70` | `1.3464` | 5,398.66 USD | 1,219,266.31 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4009.80` | `20.8622` | 83,653.25 USD | 1,213,867.65 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4009.90` | `31.9340` | 128,052.15 USD | 1,130,214.40 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4010.00` | `20.3462` | 81,588.26 USD | 1,002,162.26 USD | `15 orders` | `-0.04%` | `-` |
| `BID` | `4010.10` | `8.7863` | 35,233.94 USD | 920,574.00 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4010.20` | `63.7451` | 255,630.60 USD | 885,340.05 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4010.30` | `1.3468` | 5,401.07 USD | 629,709.45 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4010.50` | `27.6672` | 110,959.31 USD | 624,308.38 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4010.60` | `26.0402` | 104,436.83 USD | 513,349.08 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4010.70` | `4.5874` | 18,398.69 USD | 408,912.25 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4010.80` | `7.5411` | 30,245.84 USD | 390,513.56 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4010.90` | `2.9913` | 11,997.81 USD | 360,267.72 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4011.00` | `28.8248` | 115,616.27 USD | 348,269.92 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4011.10` | `14.8779` | 59,676.74 USD | 232,653.64 USD | `8 orders` | `-0.01%` | `-` |
| `BID` | `4011.20` | `17.5138` | 70,251.35 USD | 172,976.90 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4011.30` | `7.9429` | 31,861.35 USD | 102,725.54 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `4011.40` | `17.6657` | 70,864.19 USD | 70,864.19 USD | `9 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4011.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,011.45` | `0.00%` | `-` |
| `ASK` | `4011.50` | `9.7447` | 39,090.86 USD | 39,090.86 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `4011.70` | `7.4791` | 30,003.91 USD | 69,094.77 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4011.80` | `2.4139` | 9,684.08 USD | 78,778.85 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4011.90` | `2.8663` | 11,499.31 USD | 90,278.16 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4012.00` | `1.9434` | 7,796.92 USD | 98,075.08 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4012.10` | `0.9487` | 3,806.28 USD | 101,881.36 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4012.20` | `17.1480` | 68,801.21 USD | 170,682.57 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4012.30` | `25.3617` | 101,758.75 USD | 272,441.32 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4012.40` | `4.7279` | 18,970.23 USD | 291,411.54 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4012.50` | `7.2389` | 29,046.09 USD | 320,457.63 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `4012.60` | `4.6728` | 18,750.08 USD | 339,207.71 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4012.70` | `3.7381` | 14,999.87 USD | 354,207.58 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4012.80` | `30.7870` | 123,542.07 USD | 477,749.65 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `4012.90` | `53.3883` | 214,241.91 USD | 691,991.56 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4013.00` | `0.9597` | 3,851.28 USD | 695,842.84 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4013.10` | `19.2282` | 77,164.69 USD | 773,007.53 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `4013.20` | `57.8036` | 231,977.41 USD | 1,004,984.94 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4013.30` | `25.2227` | 101,226.26 USD | 1,106,211.20 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `4013.40` | `23.0148` | 92,367.60 USD | 1,198,578.80 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `4013.50` | `80.8459` | 324,475.02 USD | 1,523,053.82 USD | `5 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,567,245.57 USD | `6,373.65` | `4191.43` | `4010.60` | `29004.93` | 1,147,503.63 USD | `+4.49%` | `4X Cross` |
| `57` | `0x4692...164f` | `SHORT` | 25,342,975.02 USD | `6,317.74` | `4134.24` | `4010.60` | `13295.61` | 776,108.13 USD | `+3.06%` | `5X Cross` |
| `72` | `0xb83d...6e36` | `SHORT` | 22,933,412.08 USD | `5,717.06` | `4234.49` | `4010.60` | `27370.01` | 1,275,463.15 USD | `+5.56%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,370,677.14 USD | `4,828.91` | `4157.43` | `4010.60` | `2070.05` | -705,205.18 USD | `-3.64%` | `25X Cross` |
| `147` | `0x645b...87b8` | `LONG` | 14,097,179.18 USD | `3,514.28` | `4129.71` | `4010.60` | `186.66` | -415,798.96 USD | `-2.95%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,110,110.43 USD | `3,268.21` | `4228.94` | `4010.60` | `4408.31` | 710,968.70 USD | `+5.42%` | `25X Cross` |
| `178` | `0xa742...e390` | `SHORT` | 11,633,060.40 USD | `2,900.00` | `4364.92` | `4010.60` | `4235.59` | 1,025,215.93 USD | `+8.81%` | `20X Cross` |
| `275` | `0x3678...b209` | `LONG` | 8,825,080.00 USD | `2,200.00` | `4176.09` | `4010.60` | `2476.80` | -362,339.30 USD | `-4.11%` | `25X Cross` |
| `276` | `0x41e5...0825` | `SHORT` | 8,825,080.00 USD | `2,200.00` | `4112.20` | `4010.60` | `4331.08` | 221,774.59 USD | `+2.51%` | `20X Cross` |
| `309` | `0xfc66...ca06` | `SHORT` | 7,970,208.94 USD | `1,986.89` | `4032.86` | `4010.60` | `25059.44` | 42,657.23 USD | `+0.54%` | `3X Cross` |
| `312` | `0xacb6...efbd` | `SHORT` | 7,923,995.61 USD | `1,975.37` | `4048.55` | `4010.60` | `6502.07` | 73,396.11 USD | `+0.93%` | `6X Cross` |
| `379` | `0xc26c...b8f4` | `LONG` | 6,337,818.65 USD | `1,579.95` | `4075.62` | `4010.60` | `0.000000` | -101,478.32 USD | `-1.60%` | `1X Cross` |
| `421` | `0x12d2...f97f` | `LONG` | 5,623,753.35 USD | `1,401.94` | `4278.91` | `4010.60` | `2472.36` | -375,037.23 USD | `-6.67%` | `20X Cross` |
| `575` | `0x63da...8add` | `LONG` | 4,011,400.00 USD | `1,000.00` | `4021.46` | `4010.60` | `3564.03` | -10,060.96 USD | `-0.25%` | `25X Cross` |
| `594` | `0x9aa5...58af` | `LONG` | 3,897,644.72 USD | `971.64` | `4279.98` | `4010.60` | `0.000000` | -260,964.37 USD | `-6.70%` | `20X Cross` |
| `625` | `0xf3dc...1672` | `LONG` | 3,733,585.28 USD | `930.74` | `4024.62` | `4010.60` | `3337.51` | -12,307.28 USD | `-0.33%` | `20X Cross` |
| `688` | `0x4a20...3c26` | `LONG` | 3,359,145.16 USD | `837.40` | `4599.73` | `4010.60` | `0.000000` | -492,675.22 USD | `-14.67%` | `20X Cross` |
| `810` | `0x354b...6425` | `LONG` | 2,869,785.24 USD | `715.41` | `4037.02` | `4010.60` | `0.000000` | -18,330.56 USD | `-0.64%` | `10X Cross` |
| `845` | `0x0fac...7a0a` | `LONG` | 2,753,765.93 USD | `686.49` | `4290.34` | `4010.60` | `1348.64` | -191,492.77 USD | `-6.95%` | `25X Cross` |
| `868` | `0xd8c5...99b0` | `SHORT` | 2,643,307.62 USD | `658.95` | `4175.35` | `4010.60` | `31405.64` | 108,039.44 USD | `+4.09%` | `4X Cross` |
| `920` | `0x625e...a354` | `SHORT` | 2,487,068.00 USD | `620.00` | `4122.81` | `4010.60` | `4342.18` | 69,079.03 USD | `+2.78%` | `20X Cross` |
| `951` | `0xeae3...e8ad` | `SHORT` | 2,406,840.00 USD | `600.00` | `4104.77` | `4010.60` | `4325.20` | 56,025.11 USD | `+2.33%` | `20X Cross` |
| `953` | `0xf285...fa82` | `LONG` | 2,399,242.01 USD | `598.11` | `4146.45` | `4010.60` | `3891.17` | -80,777.55 USD | `-3.37%` | `25X Cross` |
| `971` | `0x12f7...8750` | `LONG` | 2,349,118.76 USD | `585.61` | `4082.77` | `4010.60` | `2180.71` | -41,798.22 USD | `-1.78%` | `10X Cross` |
| `1126` | `0x413c...886c` | `LONG` | 2,005,700.00 USD | `500.00` | `4010.43` | `4010.60` | `0.000000` | 483.77 USD | `+0.02%` | `2X Cross` |
| `1135` | `0x61ce...a62b` | `SHORT` | 1,995,685.54 USD | `497.50` | `4071.66` | `4010.60` | `4689.86` | 29,983.25 USD | `+1.50%` | `20X Cross` |
| `1144` | `0x0593...40f9` | `LONG` | 1,990,364.42 USD | `496.18` | `4024.57` | `4010.60` | `3701.65` | -6,539.41 USD | `-0.33%` | `10X Isolated` |
| `1255` | `0x2edd...8179` | `LONG` | 1,825,231.34 USD | `454.70` | `4169.95` | `4013.64` | `0.000000` | -70,867.29 USD | `-3.88%` | `10X Cross` |
| `1259` | `0xead5...69f2` | `LONG` | 1,820,308.74 USD | `453.78` | `4220.88` | `4010.60` | `3538.86` | -95,059.32 USD | `-5.22%` | `5X Isolated` |
| `1318` | `0x7a6d...f79c` | `SHORT` | 1,719,813.17 USD | `428.38` | `4136.09` | `4013.64` | `5852.75` | 52,001.83 USD | `+3.02%` | `10X Cross` |
| `1386` | `0x46fc...1195` | `LONG` | 1,632,754.12 USD | `407.03` | `4055.53` | `4010.60` | `1911.29` | -17,965.69 USD | `-1.10%` | `20X Cross` |
| `1420` | `0x6d15...d374` | `LONG` | 1,604,560.00 USD | `400.00` | `4068.25` | `4010.60` | `3841.73` | -22,740.00 USD | `-1.42%` | `25X Cross` |
| `1421` | `0xee02...309d` | `SHORT` | 1,604,560.00 USD | `400.00` | `4438.84` | `4010.60` | `4226.81` | 170,978.60 USD | `+10.66%` | `25X Isolated` |
| `1452` | `0x02a7...fe9f` | `SHORT` | 1,564,446.00 USD | `390.00` | `4055.02` | `4010.60` | `4306.63` | 17,013.25 USD | `+1.09%` | `25X Cross` |
| `1486` | `0x51f6...2b39` | `LONG` | 1,527,537.14 USD | `380.49` | `4234.66` | `4013.64` | `0.000000` | -83,690.92 USD | `-5.48%` | `10X Cross` |
| `1488` | `0x7e77...b8d2` | `SHORT` | 1,524,332.00 USD | `380.00` | `4131.92` | `4010.60` | `4293.44` | 45,797.64 USD | `+3.00%` | `20X Cross` |
| `1508` | `0x72c2...9b37` | `LONG` | 1,496,778.90 USD | `373.13` | `4000.98` | `4010.60` | `3777.97` | 3,885.38 USD | `+0.26%` | `13X Isolated` |
| `1545` | `0xaa44...b844` | `LONG` | 1,444,104.00 USD | `360.00` | `4043.10` | `4010.60` | `2816.92` | -11,413.63 USD | `-0.79%` | `9X Cross` |
| `1546` | `0x781e...96b7` | `SHORT` | 1,443,485.39 USD | `359.55` | `4365.03` | `4013.64` | `12443.90` | 125,962.10 USD | `+8.73%` | `10X Cross` |
| `1655` | `0xa41f...d50a` | `LONG` | 1,319,598.57 USD | `328.96` | `4468.89` | `4010.60` | `3833.11` | -150,499.28 USD | `-11.40%` | `15X Cross` |
| `1687` | `0x49e9...e1d0` | `SHORT` | 1,297,917.75 USD | `323.56` | `4025.23` | `4010.60` | `29228.25` | 4,474.95 USD | `+0.34%` | `4X Cross` |
| `1706` | `0xada6...6f88` | `LONG` | 1,280,742.14 USD | `319.28` | `4166.46` | `4010.60` | `1864.00` | -49,508.37 USD | `-3.87%` | `5X Cross` |
| `1714` | `0xbf5a...88ba` | `SHORT` | 1,274,240.87 USD | `317.65` | `4091.80` | `4010.60` | `10500.30` | 25,542.17 USD | `+2.00%` | `20X Cross` |
| `1730` | `0xff31...ff6c` | `SHORT` | 1,243,534.00 USD | `310.00` | `4372.43` | `4010.60` | `4789.11` | 111,921.38 USD | `+9.00%` | `10X Isolated` |
| `1898` | `0x50e2...d770` | `LONG` | 1,084,551.79 USD | `270.37` | `4243.58` | `4010.60` | `2562.02` | -62,774.67 USD | `-5.79%` | `20X Cross` |
| `1915` | `0x4c92...4f17` | `SHORT` | 1,069,922.61 USD | `266.72` | `4260.98` | `4010.60` | `6530.08` | 66,569.62 USD | `+6.22%` | `20X Cross` |
| `1987` | `0xd346...c4f3` | `LONG` | 1,023,604.18 USD | `255.17` | `4188.66` | `4010.60` | `3310.35` | -45,232.33 USD | `-4.42%` | `5X Isolated` |
| `2023` | `0x1581...463b` | `LONG` | 1,002,850.00 USD | `250.00` | `4003.77` | `4010.60` | `3504.56` | 1,906.41 USD | `+0.19%` | `15X Cross` |
| `2024` | `0xe47f...758c` | `LONG` | 1,002,850.00 USD | `250.00` | `4020.00` | `4010.60` | `3774.26` | -2,150.00 USD | `-0.21%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4111.37` (Vol: 316,800.00 USD, Dist: `+2.46%`) | Long MP=`3951.26` (Vol: 223,500.00 USD, Dist: `--1.53%`)
  * 48H Horizon: Short MP=`4111.21` (Vol: 296,500.00 USD, Dist: `+2.45%`) | Long MP=`3945.11` (Vol: 234,600.00 USD, Dist: `--1.69%`)
  * 3D Horizon: Short MP=`4109.24` (Vol: 329,000.00 USD, Dist: `+2.40%`) | Long MP=`3979.55` (Vol: 340,800.00 USD, Dist: `--0.83%`)
  * 7D Horizon: Short MP=`4117.50` (Vol: 1,100,000.00 USD, Dist: `+2.61%`) | Long MP=`3953.89` (Vol: 1,100,000.00 USD, Dist: `--1.47%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3612.10` | 16,290,000.00 USD | 16,290,000.00 USD | 41,480.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3614.20` | 4,110,000.00 USD | 4,110,000.00 USD | 2,900.00 USD | 0.00 USD | 198.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3616.40` | 16,230,000.00 USD | 16,230,000.00 USD | 94,440.00 USD | 0.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.40` | 4,110,000.00 USD | 4,110,000.00 USD | 7,800.00 USD | 0.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3620.70` | 16,130,000.00 USD | 16,130,000.00 USD | 63,310.00 USD | 0.00 USD | 10,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.60` | 4,100,000.00 USD | 4,100,000.00 USD | 50,360.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3625.00` | 16,060,000.00 USD | 16,060,000.00 USD | 139,860.00 USD | 0.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3626.80` | 4,040,000.00 USD | 4,040,000.00 USD | 28,710.00 USD | 0.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3629.30` | 15,900,000.00 USD | 15,900,000.00 USD | 168,390.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.00` | 4,000,000.00 USD | 4,000,000.00 USD | 32,880.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3633.60` | 15,710,000.00 USD | 15,710,000.00 USD | 108,730.00 USD | 0.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.20` | 3,970,000.00 USD | 3,970,000.00 USD | 50,590.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.90` | 15,580,000.00 USD | 15,580,000.00 USD | 87,660.00 USD | 0.00 USD | 10,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.40` | 3,910,000.00 USD | 3,910,000.00 USD | 36,130.00 USD | 0.00 USD | 10,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3642.20` | 15,480,000.00 USD | 15,480,000.00 USD | 33,140.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.60` | 3,860,000.00 USD | 3,860,000.00 USD | 16,550.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3646.50` | 15,440,000.00 USD | 15,440,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.80` | 3,850,000.00 USD | 3,850,000.00 USD | 18,580.00 USD | 0.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3650.80` | 15,410,000.00 USD | 15,410,000.00 USD | 24,210.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3652.00` | 3,820,000.00 USD | 3,820,000.00 USD | 26,300.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3655.10` | 15,380,000.00 USD | 15,380,000.00 USD | 53,090.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3656.20` | 3,790,000.00 USD | 3,790,000.00 USD | 13,340.00 USD | 0.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3659.40` | 15,320,000.00 USD | 15,320,000.00 USD | 11,970.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3660.40` | 3,770,000.00 USD | 3,770,000.00 USD | 10,130.00 USD | 0.00 USD | 2,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3663.70` | 15,310,000.00 USD | 15,310,000.00 USD | 7,390.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3664.60` | 3,760,000.00 USD | 3,760,000.00 USD | 6,340.00 USD | 0.00 USD | 1,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3668.00` | 15,300,000.00 USD | 15,300,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3673.00` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3831.40` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3835.70` | 15,290,000.00 USD | 15,290,000.00 USD | 74,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3840.00` | 15,210,000.00 USD | 15,210,000.00 USD | 358,280.00 USD | 0.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3844.30` | 14,820,000.00 USD | 14,820,000.00 USD | 470,290.00 USD | 0.00 USD | 66,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3848.60` | 14,280,000.00 USD | 14,280,000.00 USD | 537,650.00 USD | 0.00 USD | 68,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.90` | 13,680,000.00 USD | 13,680,000.00 USD | 133,680.00 USD | 0.00 USD | 47,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3853.60` | 3,750,000.00 USD | 3,750,000.00 USD | 7,240.00 USD | 0.00 USD | 276.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3857.20` | 13,490,000.00 USD | 13,490,000.00 USD | 291,610.00 USD | 0.00 USD | 16,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3857.80` | 3,750,000.00 USD | 3,750,000.00 USD | 9,340.00 USD | 0.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3861.50` | 13,190,000.00 USD | 13,190,000.00 USD | 185,410.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.00` | 3,730,000.00 USD | 3,730,000.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3865.80` | 12,970,000.00 USD | 12,970,000.00 USD | 374,550.00 USD | 0.00 USD | 67,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.20` | 3,660,000.00 USD | 3,660,000.00 USD | 128,400.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3870.10` | 12,530,000.00 USD | 12,530,000.00 USD | 541,600.00 USD | 0.00 USD | 43,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.40` | 3,510,000.00 USD | 3,510,000.00 USD | 154,970.00 USD | 0.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3874.40` | 11,940,000.00 USD | 11,940,000.00 USD | 398,220.00 USD | 0.00 USD | 36,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3874.60` | 3,330,000.00 USD | 3,330,000.00 USD | 83,320.00 USD | 0.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3878.70` | 11,510,000.00 USD | 11,510,000.00 USD | 451,810.00 USD | 0.00 USD | 65,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3878.80` | 3,230,000.00 USD | 3,230,000.00 USD | 203,300.00 USD | 0.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.00` | 3,010,000.00 USD | 3,010,000.00 USD | 87,010.00 USD | 0.00 USD | 27,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3883.00` | 10,990,000.00 USD | 10,990,000.00 USD | 198,420.00 USD | 0.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3887.20` | 2,900,000.00 USD | 2,900,000.00 USD | 62,600.00 USD | 0.00 USD | 8,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3887.30` | 10,750,000.00 USD | 10,750,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3891.40` | 2,830,000.00 USD | 2,830,000.00 USD | 77,540.00 USD | 0.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3891.60` | 10,670,000.00 USD | 10,670,000.00 USD | 129,360.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3895.60` | 2,740,000.00 USD | 2,740,000.00 USD | 76,460.00 USD | 0.00 USD | 7,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.90` | 10,520,000.00 USD | 10,520,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3899.80` | 2,650,000.00 USD | 2,650,000.00 USD | 52,670.00 USD | 0.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3900.20` | 10,410,000.00 USD | 10,410,000.00 USD | 99,580.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3904.00` | 2,590,000.00 USD | 2,590,000.00 USD | 48,740.00 USD | 0.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3904.50` | 10,300,000.00 USD | 10,300,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3908.20` | 2,540,000.00 USD | 2,540,000.00 USD | 20,800.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3908.80` | 10,260,000.00 USD | 10,260,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.10` | 10,210,000.00 USD | 10,210,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3916.60` | 2,510,000.00 USD | 2,510,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.40` | 10,180,000.00 USD | 10,180,000.00 USD | 459,090.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3921.70` | 9,690,000.00 USD | 9,690,000.00 USD | 1,020,000.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.00` | 8,600,000.00 USD | 8,600,000.00 USD | 744,170.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.30` | 7,710,000.00 USD | 7,710,000.00 USD | 809,190.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.40` | 2,500,000.00 USD | 2,500,000.00 USD | 14,490.00 USD | 0.00 USD | 552.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.60` | 6,750,000.00 USD | 6,750,000.00 USD | 378,690.00 USD | 0.00 USD | 42,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3937.60` | 2,490,000.00 USD | 2,490,000.00 USD | 18,680.00 USD | 0.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,330,000.00 USD | 6,330,000.00 USD | 422,280.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3941.80` | 2,470,000.00 USD | 2,470,000.00 USD | 113,640.00 USD | 0.00 USD | 16,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.20` | 5,880,000.00 USD | 5,880,000.00 USD | 489,070.00 USD | 0.00 USD | 74,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.00` | 2,340,000.00 USD | 2,340,000.00 USD | 275,270.00 USD | 0.00 USD | 34,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.50` | 5,310,000.00 USD | 5,310,000.00 USD | 859,010.00 USD | 0.00 USD | 114,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.20` | 2,030,000.00 USD | 2,030,000.00 USD | 272,920.00 USD | 0.00 USD | 42,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.80` | 4,340,000.00 USD | 4,340,000.00 USD | 1,000,000.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.40` | 1,710,000.00 USD | 1,710,000.00 USD | 204,780.00 USD | 0.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3956.10` | 3,240,000.00 USD | 3,240,000.00 USD | 892,120.00 USD | 0.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.60` | 1,480,000.00 USD | 1,480,000.00 USD | 348,190.00 USD | 0.00 USD | 21,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3960.40` | 2,250,000.00 USD | 2,250,000.00 USD | 651,020.00 USD | 0.00 USD | 91,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3962.80` | 1,110,000.00 USD | 1,110,000.00 USD | 244,100.00 USD | 0.00 USD | 60,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.70` | 1,510,000.00 USD | 1,510,000.00 USD | 307,000.00 USD | 0.00 USD | 105,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.00` | 802,200.00 USD | 802,200.00 USD | 125,190.00 USD | 0.00 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3969.00` | 1,090,000.00 USD | 1,090,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.20` | 657,910.00 USD | 657,910.00 USD | 57,990.00 USD | 0.00 USD | 28,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3973.30` | 874,480.00 USD | 874,480.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.40` | 571,170.00 USD | 571,170.00 USD | 237,910.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3977.60` | 646,890.00 USD | 646,890.00 USD | 241,180.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.60` | 315,870.00 USD | 315,870.00 USD | 83,910.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.90` | 388,050.00 USD | 388,050.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.80` | 213,340.00 USD | 213,340.00 USD | 123,010.00 USD | 0.00 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3986.20` | 219,990.00 USD | 219,990.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3988.00` | 79,760.00 USD | 79,760.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3990.50` | 120,370.00 USD | 120,370.00 USD | 73,770.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3994.80` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3996.40` | 20,280.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4072.20` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4076.50` | 372,250.00 USD | 372,250.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4080.80` | 1,160,000.00 USD | 1,160,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.10` | 2,200,000.00 USD | 2,200,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4089.40` | 3,260,000.00 USD | 3,260,000.00 USD | 936,410.00 USD | 0.00 USD | 122,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4093.70` | 3,590,000.00 USD | 3,590,000.00 USD | 239,740.00 USD | 0.00 USD | 95,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4097.20` | 16,990.00 USD | 16,990.00 USD | 14,490.00 USD | 0.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.00` | 4,200,000.00 USD | 4,200,000.00 USD | 583,220.00 USD | 0.00 USD | 31,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.40` | 130,850.00 USD | 130,850.00 USD | 100,800.00 USD | 0.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.30` | 4,550,000.00 USD | 4,550,000.00 USD | 292,950.00 USD | 0.00 USD | 55,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4105.60` | 401,740.00 USD | 401,740.00 USD | 256,710.00 USD | 0.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.60` | 5,280,000.00 USD | 5,280,000.00 USD | 625,970.00 USD | 0.00 USD | 104,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4109.80` | 641,870.00 USD | 641,870.00 USD | 193,290.00 USD | 0.00 USD | 46,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.90` | 6,590,000.00 USD | 6,590,000.00 USD | 1,230,000.00 USD | 0.00 USD | 79,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.00` | 954,030.00 USD | 954,030.00 USD | 276,610.00 USD | 0.00 USD | 35,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.20` | 7,320,000.00 USD | 7,320,000.00 USD | 634,940.00 USD | 0.00 USD | 90,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.20` | 1,140,000.00 USD | 1,140,000.00 USD | 159,780.00 USD | 0.00 USD | 21,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,380,000.00 USD | 8,380,000.00 USD | 935,130.00 USD | 0.00 USD | 125,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.40` | 1,640,000.00 USD | 1,640,000.00 USD | 450,390.00 USD | 0.00 USD | 51,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.80` | 8,890,000.00 USD | 8,890,000.00 USD | 417,860.00 USD | 0.00 USD | 91,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4126.60` | 1,750,000.00 USD | 1,750,000.00 USD | 73,020.00 USD | 0.00 USD | 35,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4128.10` | 9,140,000.00 USD | 9,140,000.00 USD | 202,410.00 USD | 0.00 USD | 49,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4130.80` | 1,870,000.00 USD | 1,870,000.00 USD | 92,150.00 USD | 0.00 USD | 30,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.40` | 9,380,000.00 USD | 9,380,000.00 USD | 199,830.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.00` | 2,060,000.00 USD | 2,060,000.00 USD | 184,570.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.70` | 9,610,000.00 USD | 9,610,000.00 USD | 204,390.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.20` | 2,220,000.00 USD | 2,220,000.00 USD | 147,350.00 USD | 0.00 USD | 15,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4141.00` | 9,800,000.00 USD | 9,800,000.00 USD | 184,250.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.40` | 2,330,000.00 USD | 2,330,000.00 USD | 81,430.00 USD | 0.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4145.30` | 9,980,000.00 USD | 9,980,000.00 USD | 147,710.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.60` | 2,430,000.00 USD | 2,430,000.00 USD | 97,480.00 USD | 0.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4149.60` | 10,130,000.00 USD | 10,130,000.00 USD | 110,560.00 USD | 0.00 USD | 32,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4151.80` | 2,480,000.00 USD | 2,480,000.00 USD | 41,610.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.90` | 10,160,000.00 USD | 10,160,000.00 USD | 36,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4158.20` | 10,590,000.00 USD | 10,590,000.00 USD | 410,790.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.20` | 2,500,000.00 USD | 2,500,000.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4162.50` | 11,040,000.00 USD | 11,040,000.00 USD | 407,770.00 USD | 0.00 USD | 45,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4166.80` | 11,500,000.00 USD | 11,500,000.00 USD | 392,410.00 USD | 0.00 USD | 67,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4171.10` | 11,930,000.00 USD | 11,930,000.00 USD | 350,430.00 USD | 0.00 USD | 70,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4175.40` | 12,090,000.00 USD | 12,090,000.00 USD | 147,430.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.00` | 2,510,000.00 USD | 2,510,000.00 USD | 7,240.00 USD | 0.00 USD | 771.53 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4179.70` | 12,330,000.00 USD | 12,330,000.00 USD | 219,930.00 USD | 0.00 USD | 15,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.20` | 2,540,000.00 USD | 2,540,000.00 USD | 27,640.00 USD | 0.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4184.00` | 12,580,000.00 USD | 12,580,000.00 USD | 219,800.00 USD | 0.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.40` | 2,640,000.00 USD | 2,640,000.00 USD | 87,820.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4188.30` | 12,970,000.00 USD | 12,970,000.00 USD | 327,710.00 USD | 0.00 USD | 68,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4189.60` | 2,800,000.00 USD | 2,800,000.00 USD | 142,370.00 USD | 0.00 USD | 24,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4192.60` | 13,530,000.00 USD | 13,530,000.00 USD | 524,540.00 USD | 0.00 USD | 32,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4193.80` | 2,940,000.00 USD | 2,940,000.00 USD | 118,070.00 USD | 0.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.90` | 13,960,000.00 USD | 13,960,000.00 USD | 389,870.00 USD | 0.00 USD | 44,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4198.00` | 3,050,000.00 USD | 3,050,000.00 USD | 98,400.00 USD | 0.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4201.20` | 14,490,000.00 USD | 14,490,000.00 USD | 460,170.00 USD | 0.00 USD | 65,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4202.20` | 3,250,000.00 USD | 3,250,000.00 USD | 185,840.00 USD | 0.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4205.50` | 14,690,000.00 USD | 14,690,000.00 USD | 165,880.00 USD | 0.00 USD | 33,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.40` | 3,360,000.00 USD | 3,360,000.00 USD | 78,630.00 USD | 0.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4209.80` | 14,790,000.00 USD | 14,790,000.00 USD | 74,330.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4210.60` | 3,430,000.00 USD | 3,430,000.00 USD | 62,600.00 USD | 0.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4214.10` | 14,900,000.00 USD | 14,900,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4214.80` | 3,490,000.00 USD | 3,490,000.00 USD | 54,900.00 USD | 0.00 USD | 12,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4218.40` | 15,030,000.00 USD | 15,030,000.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4219.00` | 3,600,000.00 USD | 3,600,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4222.70` | 15,170,000.00 USD | 15,170,000.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4223.20` | 3,650,000.00 USD | 3,650,000.00 USD | 41,960.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4227.00` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4227.40` | 3,710,000.00 USD | 3,710,000.00 USD | 60,070.00 USD | 0.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4231.30` | 15,260,000.00 USD | 15,260,000.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4231.60` | 3,730,000.00 USD | 3,730,000.00 USD | 10,380.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4235.60` | 15,290,000.00 USD | 15,290,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4235.80` | 3,740,000.00 USD | 3,740,000.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4240.00` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4244.20` | 3,750,000.00 USD | 3,750,000.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4390.40` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4399.00` | 15,440,000.00 USD | 15,440,000.00 USD | 141,850.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4403.30` | 15,590,000.00 USD | 15,590,000.00 USD | 137,570.00 USD | 0.00 USD | 18,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4407.60` | 15,760,000.00 USD | 15,760,000.00 USD | 145,420.00 USD | 0.00 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.90` | 15,830,000.00 USD | 15,830,000.00 USD | 50,960.00 USD | 0.00 USD | 22,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4416.20` | 15,890,000.00 USD | 15,890,000.00 USD | 51,780.00 USD | 0.00 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.40` | 3,760,000.00 USD | 3,760,000.00 USD | 2,900.00 USD | 0.00 USD | 198.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4420.50` | 15,960,000.00 USD | 15,960,000.00 USD | 62,350.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4420.60` | 3,760,000.00 USD | 3,760,000.00 USD | 3,740.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4424.80` | 3,790,000.00 USD | 3,790,000.00 USD | 24,000.00 USD | 0.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4424.80` | 16,000,000.00 USD | 16,000,000.00 USD | 34,880.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4429.00` | 3,830,000.00 USD | 3,830,000.00 USD | 33,960.00 USD | 0.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4429.10` | 16,100,000.00 USD | 16,100,000.00 USD | 77,220.00 USD | 0.00 USD | 18,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.20` | 3,860,000.00 USD | 3,860,000.00 USD | 28,790.00 USD | 0.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4433.40` | 16,310,000.00 USD | 16,310,000.00 USD | 201,720.00 USD | 0.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.50` | 3,870,000.00 USD | 3,870,000.00 USD | 4,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4437.70` | 16,400,000.00 USD | 16,400,000.00 USD | 82,170.00 USD | 0.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.00` | 16,540,000.00 USD | 16,540,000.00 USD | 114,900.00 USD | 0.00 USD | 23,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.30` | 16,600,000.00 USD | 16,600,000.00 USD | 48,670.00 USD | 0.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.30` | 16,630,000.00 USD | 16,630,000.00 USD | 25,230.00 USD | 0.00 USD | 1,890.00 USD | `Tier 1 CEX` |

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
| `7D` | `3612.10` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 41,480.00 USD | 0.00 USD | 14,680.00 USD |
| `1D` | `3614.20` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 2,900.00 USD | 0.00 USD | 198.18 USD |
| `7D` | `3616.40` | 16,230,000.00 USD | 0.00 USD | 16,230,000.00 USD | 94,440.00 USD | 0.00 USD | 4,740.00 USD |
| `1D` | `3618.40` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 7,800.00 USD | 0.00 USD | 1,810.00 USD |
| `7D` | `3620.70` | 16,130,000.00 USD | 0.00 USD | 16,130,000.00 USD | 63,310.00 USD | 0.00 USD | 10,550.00 USD |
| `1D` | `3622.60` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 50,360.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `3625.00` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 139,860.00 USD | 0.00 USD | 23,510.00 USD |
| `1D` | `3626.80` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 28,710.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3629.30` | 15,900,000.00 USD | 0.00 USD | 15,900,000.00 USD | 168,390.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3631.00` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 32,880.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3633.60` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 108,730.00 USD | 0.00 USD | 27,200.00 USD |
| `1D` | `3635.20` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 50,590.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `3637.90` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 87,660.00 USD | 0.00 USD | 10,810.00 USD |
| `1D` | `3639.40` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 36,130.00 USD | 0.00 USD | 10,830.00 USD |
| `7D` | `3642.20` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 33,140.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `3643.60` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 16,550.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `3646.50` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3647.80` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 18,580.00 USD | 0.00 USD | 5,150.00 USD |
| `7D` | `3650.80` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 24,210.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3652.00` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 26,300.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `3655.10` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 53,090.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3656.20` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 13,340.00 USD | 0.00 USD | 4,100.00 USD |
| `7D` | `3659.40` | 15,320,000.00 USD | 0.00 USD | 15,320,000.00 USD | 11,970.00 USD | 0.00 USD | 5,410.00 USD |
| `1D` | `3660.40` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 10,130.00 USD | 0.00 USD | 2,130.00 USD |
| `7D` | `3663.70` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 7,390.00 USD | 0.00 USD | 3,650.00 USD |
| `1D` | `3664.60` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 6,340.00 USD | 0.00 USD | 1,050.00 USD |
| `7D` | `3668.00` | 15,300,000.00 USD | 0.00 USD | 15,300,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3673.00` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3831.40` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3835.70` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 74,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3840.00` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 358,280.00 USD | 0.00 USD | 33,930.00 USD |
| `7D` | `3844.30` | 14,820,000.00 USD | 0.00 USD | 14,820,000.00 USD | 470,290.00 USD | 0.00 USD | 66,380.00 USD |
| `7D` | `3848.60` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 537,650.00 USD | 0.00 USD | 68,950.00 USD |
| `7D` | `3852.90` | 13,680,000.00 USD | 0.00 USD | 13,680,000.00 USD | 133,680.00 USD | 0.00 USD | 47,620.00 USD |
| `1D` | `3853.60` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 7,240.00 USD | 0.00 USD | 276.09 USD |
| `7D` | `3857.20` | 13,490,000.00 USD | 0.00 USD | 13,490,000.00 USD | 291,610.00 USD | 0.00 USD | 16,710.00 USD |
| `1D` | `3857.80` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 9,340.00 USD | 0.00 USD | 3,870.00 USD |
| `7D` | `3861.50` | 13,190,000.00 USD | 0.00 USD | 13,190,000.00 USD | 185,410.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `3862.00` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD |
| `7D` | `3865.80` | 12,970,000.00 USD | 0.00 USD | 12,970,000.00 USD | 374,550.00 USD | 0.00 USD | 67,840.00 USD |
| `1D` | `3866.20` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 128,400.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `3870.10` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 541,600.00 USD | 0.00 USD | 43,240.00 USD |
| `1D` | `3870.40` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 154,970.00 USD | 0.00 USD | 20,170.00 USD |
| `7D` | `3874.40` | 11,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 398,220.00 USD | 0.00 USD | 36,760.00 USD |
| `1D` | `3874.60` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 83,320.00 USD | 0.00 USD | 15,860.00 USD |
| `7D` | `3878.70` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 451,810.00 USD | 0.00 USD | 65,180.00 USD |
| `1D` | `3878.80` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 203,300.00 USD | 0.00 USD | 15,330.00 USD |
| `1D` | `3883.00` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 87,010.00 USD | 0.00 USD | 27,760.00 USD |
| `7D` | `3883.00` | 10,990,000.00 USD | 0.00 USD | 10,990,000.00 USD | 198,420.00 USD | 0.00 USD | 39,990.00 USD |
| `1D` | `3887.20` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 62,600.00 USD | 0.00 USD | 8,250.00 USD |
| `7D` | `3887.30` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD |
| `1D` | `3891.40` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 77,540.00 USD | 0.00 USD | 11,930.00 USD |
| `7D` | `3891.60` | 10,670,000.00 USD | 0.00 USD | 10,670,000.00 USD | 129,360.00 USD | 0.00 USD | 19,970.00 USD |
| `1D` | `3895.60` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 76,460.00 USD | 0.00 USD | 7,970.00 USD |
| `7D` | `3895.90` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `3899.80` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 52,670.00 USD | 0.00 USD | 11,210.00 USD |
| `7D` | `3900.20` | 10,410,000.00 USD | 0.00 USD | 10,410,000.00 USD | 99,580.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3904.00` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 48,740.00 USD | 0.00 USD | 3,990.00 USD |
| `7D` | `3904.50` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `1D` | `3908.20` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 20,800.00 USD | 0.00 USD | 4,330.00 USD |
| `7D` | `3908.80` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `3913.10` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3916.60` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3917.40` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 459,090.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3921.70` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 1,020,000.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `3926.00` | 8,600,000.00 USD | 0.00 USD | 8,600,000.00 USD | 744,170.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `3930.30` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 809,190.00 USD | 0.00 USD | 147,240.00 USD |
| `1D` | `3933.40` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 14,490.00 USD | 0.00 USD | 552.18 USD |
| `7D` | `3934.60` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 378,690.00 USD | 0.00 USD | 42,870.00 USD |
| `1D` | `3937.60` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 18,680.00 USD | 0.00 USD | 1,950.00 USD |
| `7D` | `3938.90` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 422,280.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3941.80` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 113,640.00 USD | 0.00 USD | 16,100.00 USD |
| `7D` | `3943.20` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 489,070.00 USD | 0.00 USD | 74,120.00 USD |
| `1D` | `3946.00` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 275,270.00 USD | 0.00 USD | 34,040.00 USD |
| `7D` | `3947.50` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 859,010.00 USD | 0.00 USD | 114,580.00 USD |
| `1D` | `3950.20` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 272,920.00 USD | 0.00 USD | 42,200.00 USD |
| `7D` | `3951.80` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 1,000,000.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3954.40` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 204,780.00 USD | 0.00 USD | 31,910.00 USD |
| `7D` | `3956.10` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 892,120.00 USD | 0.00 USD | 100,750.00 USD |
| `1D` | `3958.60` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 348,190.00 USD | 0.00 USD | 21,430.00 USD |
| `7D` | `3960.40` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 651,020.00 USD | 0.00 USD | 91,830.00 USD |
| `1D` | `3962.80` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 244,100.00 USD | 0.00 USD | 60,280.00 USD |
| `7D` | `3964.70` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 307,000.00 USD | 0.00 USD | 105,930.00 USD |
| `1D` | `3967.00` | 802,200.00 USD | 0.00 USD | 802,200.00 USD | 125,190.00 USD | 0.00 USD | 19,100.00 USD |
| `7D` | `3969.00` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD |
| `1D` | `3971.20` | 657,910.00 USD | 0.00 USD | 657,910.00 USD | 57,990.00 USD | 0.00 USD | 28,740.00 USD |
| `7D` | `3973.30` | 874,480.00 USD | 0.00 USD | 874,480.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `3975.40` | 571,170.00 USD | 0.00 USD | 571,170.00 USD | 237,910.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `3977.60` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 241,180.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.60` | 315,870.00 USD | 0.00 USD | 315,870.00 USD | 83,910.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `3981.90` | 388,050.00 USD | 0.00 USD | 388,050.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `3983.80` | 213,340.00 USD | 0.00 USD | 213,340.00 USD | 123,010.00 USD | 0.00 USD | 10,580.00 USD |
| `7D` | `3986.20` | 219,990.00 USD | 0.00 USD | 219,990.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `3988.00` | 79,760.00 USD | 0.00 USD | 79,760.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `3990.50` | 120,370.00 USD | 0.00 USD | 120,370.00 USD | 73,770.00 USD | 0.00 USD | 13,510.00 USD |
| `7D` | `3994.80` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3996.40` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4012.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4012.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4072.20` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4076.50` | 372,250.00 USD | 372,250.00 USD | 0.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `4080.80` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `4085.10` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `4089.40` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 936,410.00 USD | 0.00 USD | 122,920.00 USD |
| `7D` | `4093.70` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 239,740.00 USD | 0.00 USD | 95,230.00 USD |
| `1D` | `4097.20` | 16,990.00 USD | 16,990.00 USD | 0.00 USD | 14,490.00 USD | 0.00 USD | 2,500.00 USD |
| `7D` | `4098.00` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 583,220.00 USD | 0.00 USD | 31,660.00 USD |
| `1D` | `4101.40` | 130,850.00 USD | 130,850.00 USD | 0.00 USD | 100,800.00 USD | 0.00 USD | 13,070.00 USD |
| `7D` | `4102.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 292,950.00 USD | 0.00 USD | 55,820.00 USD |
| `1D` | `4105.60` | 401,740.00 USD | 401,740.00 USD | 0.00 USD | 256,710.00 USD | 0.00 USD | 14,180.00 USD |
| `7D` | `4106.60` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 625,970.00 USD | 0.00 USD | 104,820.00 USD |
| `1D` | `4109.80` | 641,870.00 USD | 641,870.00 USD | 0.00 USD | 193,290.00 USD | 0.00 USD | 46,840.00 USD |
| `7D` | `4110.90` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 79,390.00 USD |
| `1D` | `4114.00` | 954,030.00 USD | 954,030.00 USD | 0.00 USD | 276,610.00 USD | 0.00 USD | 35,540.00 USD |
| `7D` | `4115.20` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 634,940.00 USD | 0.00 USD | 90,390.00 USD |
| `1D` | `4118.20` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 159,780.00 USD | 0.00 USD | 21,310.00 USD |
| `7D` | `4119.50` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 935,130.00 USD | 0.00 USD | 125,510.00 USD |
| `1D` | `4122.40` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 450,390.00 USD | 0.00 USD | 51,070.00 USD |
| `7D` | `4123.80` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 91,610.00 USD |
| `1D` | `4126.60` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 73,020.00 USD | 0.00 USD | 35,580.00 USD |
| `7D` | `4128.10` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 49,090.00 USD |
| `1D` | `4130.80` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 92,150.00 USD | 0.00 USD | 30,370.00 USD |
| `7D` | `4132.40` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 199,830.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.00` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 184,570.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4136.70` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 204,390.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.20` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 147,350.00 USD | 0.00 USD | 15,930.00 USD |
| `7D` | `4141.00` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 184,250.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.40` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 81,430.00 USD | 0.00 USD | 22,420.00 USD |
| `7D` | `4145.30` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4147.60` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 97,480.00 USD | 0.00 USD | 6,780.00 USD |
| `7D` | `4149.60` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 110,560.00 USD | 0.00 USD | 32,540.00 USD |
| `1D` | `4151.80` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 41,610.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.90` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 36,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4158.20` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 410,790.00 USD | 0.00 USD | 17,920.00 USD |
| `1D` | `4160.20` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4162.50` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 407,770.00 USD | 0.00 USD | 45,580.00 USD |
| `7D` | `4166.80` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 392,410.00 USD | 0.00 USD | 67,510.00 USD |
| `7D` | `4171.10` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 350,430.00 USD | 0.00 USD | 70,160.00 USD |
| `7D` | `4175.40` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 147,430.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `4177.00` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 7,240.00 USD | 0.00 USD | 771.53 USD |
| `7D` | `4179.70` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 219,930.00 USD | 0.00 USD | 15,340.00 USD |
| `1D` | `4181.20` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 27,640.00 USD | 0.00 USD | 5,220.00 USD |
| `7D` | `4184.00` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 219,800.00 USD | 0.00 USD | 27,490.00 USD |
| `1D` | `4185.40` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 87,820.00 USD | 0.00 USD | 4,670.00 USD |
| `7D` | `4188.30` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 327,710.00 USD | 0.00 USD | 68,830.00 USD |
| `1D` | `4189.60` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 142,370.00 USD | 0.00 USD | 24,440.00 USD |
| `7D` | `4192.60` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 524,540.00 USD | 0.00 USD | 32,190.00 USD |
| `1D` | `4193.80` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 118,070.00 USD | 0.00 USD | 19,830.00 USD |
| `7D` | `4196.90` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 389,870.00 USD | 0.00 USD | 44,580.00 USD |
| `1D` | `4198.00` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 98,400.00 USD | 0.00 USD | 11,210.00 USD |
| `7D` | `4201.20` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 460,170.00 USD | 0.00 USD | 65,180.00 USD |
| `1D` | `4202.20` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 185,840.00 USD | 0.00 USD | 15,330.00 USD |
| `7D` | `4205.50` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 165,880.00 USD | 0.00 USD | 33,520.00 USD |
| `1D` | `4206.40` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 78,630.00 USD | 0.00 USD | 27,210.00 USD |
| `7D` | `4209.80` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 74,330.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `4210.60` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 62,600.00 USD | 0.00 USD | 6,550.00 USD |
| `7D` | `4214.10` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD |
| `1D` | `4214.80` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 54,900.00 USD | 0.00 USD | 12,910.00 USD |
| `7D` | `4218.40` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD |
| `1D` | `4219.00` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `4222.70` | 15,170,000.00 USD | 15,170,000.00 USD | 0.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD |
| `1D` | `4223.20` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 41,960.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `4227.00` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,710.00 USD |
| `1D` | `4227.40` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 60,070.00 USD | 0.00 USD | 5,290.00 USD |
| `7D` | `4231.30` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD |
| `1D` | `4231.60` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 10,380.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `4235.60` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4235.80` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4240.00` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD |
| `1D` | `4244.20` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4390.40` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4399.00` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 141,850.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4403.30` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 137,570.00 USD | 0.00 USD | 18,550.00 USD |
| `7D` | `4407.60` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 145,420.00 USD | 0.00 USD | 19,100.00 USD |
| `7D` | `4411.90` | 15,830,000.00 USD | 15,830,000.00 USD | 0.00 USD | 50,960.00 USD | 0.00 USD | 22,970.00 USD |
| `7D` | `4416.20` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 51,780.00 USD | 0.00 USD | 5,030.00 USD |
| `1D` | `4416.40` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 2,900.00 USD | 0.00 USD | 198.18 USD |
| `7D` | `4420.50` | 15,960,000.00 USD | 15,960,000.00 USD | 0.00 USD | 62,350.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4420.60` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 3,740.00 USD | 0.00 USD | 1,350.00 USD |
| `1D` | `4424.80` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 24,000.00 USD | 0.00 USD | 1,780.00 USD |
| `7D` | `4424.80` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 34,880.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `4429.00` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 33,960.00 USD | 0.00 USD | 5,910.00 USD |
| `7D` | `4429.10` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 77,220.00 USD | 0.00 USD | 18,950.00 USD |
| `1D` | `4433.20` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 28,790.00 USD | 0.00 USD | 5,230.00 USD |
| `7D` | `4433.40` | 16,310,000.00 USD | 16,310,000.00 USD | 0.00 USD | 201,720.00 USD | 0.00 USD | 10,210.00 USD |
| `1D` | `4433.50` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 4,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4437.70` | 16,400,000.00 USD | 16,400,000.00 USD | 0.00 USD | 82,170.00 USD | 0.00 USD | 14,310.00 USD |
| `7D` | `4442.00` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 114,900.00 USD | 0.00 USD | 23,290.00 USD |
| `7D` | `4446.30` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 48,670.00 USD | 0.00 USD | 9,170.00 USD |
| `7D` | `4448.30` | 16,630,000.00 USD | 16,630,000.00 USD | 0.00 USD | 25,230.00 USD | 0.00 USD | 1,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.96M` | Total OI Tokens: `68,370.4 PAXG`
  * 1h OI Change: `+0.15%` | 4h OI Change: `-0.34%` | 24h OI Change: `+0.53%`
  * Exchange Breakdown: Binance=`106.75M` | Bybit=`19.99M` | OKX=`-` | Hyperliquid=`25.76M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.15K` | Last 24h: `25.27K` | Last 3d: `95.73K` | Last 7d: `222.33K`
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
| `15M` | `PAXG` | `44.95%` | `55.05%` | `0.82` | 2,340,000.00 USD |
| `15M` | `Binance` | `63.13%` | `36.87%` | `1.71` | 1,100,000.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `62.4%` | `37.6%` | `1.66` | 51,380.00 USD |
| `15M` | `KuCoin` | `53.25%` | `46.75%` | `1.14` | 108,610.00 USD |
| `15M` | `Gate` | `88.19%` | `11.81%` | `7.47` | 61,870.00 USD |
| `15M` | `Bitget` | `51.39%` | `48.61%` | `1.06` | 65,570.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `0.92%` | `99.08%` | `0.01` | 486,050.00 USD |
| `15M` | `Bitunix` | `45.58%` | `54.42%` | `0.84` | 38,350.00 USD |
| `15M` | `Hyperliquid` | `28.53%` | `71.47%` | `0.40` | 293,780.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `80%` | `20%` | `4.00` | 83,970.00 USD |
| `15M` | `HTX` | `57.72%` | `42.28%` | `1.37` | 2,830.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0.36%` | `99.64%` | `0.00` | 16,570.00 USD |
| `15M` | `Aster` | `19.48%` | `80.52%` | `0.24` | 5,730.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `1.98%` | `98.02%` | `0.02` | 20,240.00 USD |
| `15M` | `Whale Positions` | `63.13%` | `36.87%` | `1.71` | 1,100,000.00 USD |
| `15M` | `Global Accounts` | `44.95%` | `55.05%` | `0.82` | 2,340,000.00 USD |
| `1H` | `PAXG` | `44.04%` | `55.96%` | `0.79` | 5,830,000.00 USD |
| `1H` | `Binance` | `54.08%` | `45.92%` | `1.18` | 2,640,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `56.33%` | `43.67%` | `1.29` | 109,630.00 USD |
| `1H` | `KuCoin` | `52.18%` | `47.82%` | `1.09` | 408,020.00 USD |
| `1H` | `Gate` | `77.52%` | `22.48%` | `3.45` | 101,150.00 USD |
| `1H` | `Bitget` | `44.84%` | `55.16%` | `0.81` | 357,760.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `2.43%` | `97.57%` | `0.02` | 496,640.00 USD |
| `1H` | `Bitunix` | `47.94%` | `52.06%` | `0.92` | 79,970.00 USD |
| `1H` | `Hyperliquid` | `28.55%` | `71.45%` | `0.40` | 1,170,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `60.22%` | `39.78%` | `1.51` | 377,720.00 USD |
| `1H` | `HTX` | `50.39%` | `49.61%` | `1.02` | 17,940.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `17.13%` | `82.87%` | `0.21` | 21,500.00 USD |
| `1H` | `Aster` | `22.25%` | `77.75%` | `0.29` | 6,980.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `3.7%` | `96.3%` | `0.04` | 46,180.00 USD |
| `1H` | `Whale Positions` | `54.08%` | `45.92%` | `1.18` | 2,640,000.00 USD |
| `1H` | `Global Accounts` | `44.04%` | `55.96%` | `0.79` | 5,830,000.00 USD |
| `4H` | `PAXG` | `48.92%` | `51.08%` | `0.96` | 22,740,000.00 USD |
| `4H` | `Binance` | `52.72%` | `47.28%` | `1.12` | 11,590,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `35.46%` | `64.54%` | `0.55` | 623,690.00 USD |
| `4H` | `KuCoin` | `48.22%` | `51.78%` | `0.93` | 1,740,000.00 USD |
| `4H` | `Gate` | `68.41%` | `31.59%` | `2.17` | 764,060.00 USD |
| `4H` | `Bitget` | `49.06%` | `50.94%` | `0.96` | 2,750,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `8.73%` | `91.27%` | `0.10` | 570,850.00 USD |
| `4H` | `Bitunix` | `53.8%` | `46.2%` | `1.16` | 296,200.00 USD |
| `4H` | `Hyperliquid` | `41.02%` | `58.98%` | `0.70` | 1,880,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `44.58%` | `55.42%` | `0.80` | 2,240,000.00 USD |
| `4H` | `HTX` | `46.07%` | `53.93%` | `0.85` | 83,460.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `26.12%` | `73.88%` | `0.35` | 45,640.00 USD |
| `4H` | `Aster` | `82.97%` | `17.03%` | `4.87` | 45,570.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `15.2%` | `84.8%` | `0.18` | 112,710.00 USD |
| `4H` | `Whale Positions` | `52.72%` | `47.28%` | `1.12` | 11,590,000.00 USD |
| `4H` | `Global Accounts` | `48.92%` | `51.08%` | `0.96` | 22,740,000.00 USD |


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
| `5m` | 23,440.00 USD | 35,010.00 USD | **`ACCUMULATION`** |
| `15m` | 31,690.00 USD | -103,890.00 USD | **`DISTRIBUTION`** |
| `30m` | -164,640.00 USD | -315,180.00 USD | **`DISTRIBUTION`** |
| `1h` | -223,660.00 USD | -200,260.00 USD | **`DISTRIBUTION`** |
| `2h` | 417,130.00 USD | 364,960.00 USD | **`ACCUMULATION`** |
| `4h` | 502,070.00 USD | 27,550.00 USD | **`ACCUMULATION`** |
| `6h` | 249,610.00 USD | 621,800.00 USD | **`ACCUMULATION`** |
| `8h` | 94,580.00 USD | 851,950.00 USD | **`ACCUMULATION`** |
| `12h` | 90,440.00 USD | 204,520.00 USD | **`ACCUMULATION`** |
| `24h` | -251,600.00 USD | 788,020.00 USD | **`ACCUMULATION`** |
| `1w` | -8,930,000.00 USD | -8,060,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,070,000.00 USD | -72,680,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+23.44K` | 15m=`+31.69K` | 1h=`-223.66K` | 24h=`-251.60K`
* Futures Capital Netflows: 5m=`+35.01K` | 15m=`-103.89K` | 1h=`-200.26K` | 24h=`+788.02K`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4019.01` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4009.25` (Risk Distance: `9.76` pts)
  * +2.5R Take Profit: `4043.41`
  * Mathematical Lot Sizing: **`1.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4041.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4050.88` (Risk Distance: `9.76` pts)
  * +2.5R Take Profit: `4016.72`
  * Mathematical Lot Sizing: **`1.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4041.67`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
