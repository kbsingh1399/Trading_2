# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 09:46:25 IST` (`2026-10-30 04:16:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3990.57` | **Live Ask Quote**: `3990.65` | **Mid Price**: `3990.61`
- **Spread Points**: `8.00` | **Spread BPS**: `0.20 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `4004.16` | VWAP Z-Score: `-1.93` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `8.06` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.06` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4020.20` | Lower -3.00σ Band: `3988.13`
  * Upper +2.51σ Band: `4017.58` | Lower -2.51σ Band: `3990.75`
  * Upper +2.01σ Band: `4014.91` | Lower -2.01σ Band: `3993.42`
  * Upper +2.00σ Band: `4014.85` | Lower -2.00σ Band: `3993.48`
  * Upper +1.28σ Band: `4011.01` | Lower -1.28σ Band: `3997.32`
  * Upper +1.00σ Band: `4009.51` | Lower -1.00σ Band: `3998.82`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3999.12` | EMA-20=`4004.38` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4012.39` (Slope: `+0.0000`) | EMA-100=`4020.53`
  * Institutional Anchors: EMA-144=`4024.28` | EMA-200=`4026.20` (Slope: `-0.0793`) | EMA-233=`4027.76`
- **Range Boundaries**: 24H High=`4048.10` | 24H Low=`3990.41` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.20` (Distance: `-0.55%`)
  * Point of Control (POC) = `4006.85` (Distance: `-0.39%`)
  * Value Area Low (VAL) = `3997.85` (Distance: `-0.17%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4050.33` | Weekly POC=`4014.77` | Weekly VAL=`4004.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3989.24`
  * London Session (08:00-16:00 UTC): High=`4006.57` | Low=`3974.65`
  * New York Session (13:00-21:00 UTC): High=`4014.55` | Low=`3966.67`
  * Initial Balance (First Hour): IB High=`4002.58` | IB Low=`3978.64`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3974.65` - `4006.57`
  * Optimal Trade Entry (OTE 0.705): `3998.59`
  * Structural Invalidation Anchor (0.786): `4022.53`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3999.40` | `4000.20` | `3999.16` | `3999.52` | `21` | 83,399.54 USD | 16,142.43 USD | `+19.36%` | -769,423.18 USD | `+0.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `3999.51` | `3999.52` | `3998.26` | `3998.30` | `56` | 223,411.96 USD | -53,208.44 USD | `-23.82%` | -822,631.61 USD | `-0.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `3998.31` | `3998.31` | `3998.31` | `3998.31` | `2` | 6,989.05 USD | 6,989.05 USD | `+100.00%` | -815,642.57 USD | `+0.19` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `3998.48` | `4006.40` | `3997.76` | `4005.94` | `205` | 819,646.00 USD | 310,792.17 USD | `+37.92%` | -751,036.02 USD | `+1.66` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4005.94` | `4005.94` | `3999.14` | `3999.52` | `146` | 582,852.10 USD | -7,069.16 USD | `-1.21%` | -758,105.17 USD | `+0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `3999.51` | `3999.52` | `3998.26` | `3998.31` | `58` | 230,401.01 USD | -46,219.39 USD | `-20.06%` | -804,324.56 USD | `+0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4008.10` | `4013.95` | `3999.00` | `4008.79` | `1,150` | 4,606,132.72 USD | -286,613.67 USD | `-6.22%` | -396,780.69 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4008.80` | `4014.92` | `4001.35` | `4002.36` | `667` | 2,671,119.24 USD | -91,693.11 USD | `-3.43%` | -488,473.81 USD | `-0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4002.37` | `4006.40` | `3997.76` | `3998.30` | `781` | 3,123,420.96 USD | -322,839.80 USD | `-10.34%` | -811,313.61 USD | `-0.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 614,369.34 USD | `+1.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 632,225.70 USD | `-0.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.76` | `3998.31` | `3,739` | 14,982,012.27 USD | -1,436,550.26 USD | `-9.59%` | -804,324.56 USD | `-1.63` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -910,560.46 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | -478,447.19 USD | `+1.31` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 614,369.34 USD | `+1.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 632,225.70 USD | `-0.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.76` | `3998.31` | `3,739` | 14,982,012.27 USD | -1,436,550.26 USD | `-9.59%` | -804,324.56 USD | `-1.63` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `3991.10` | `6.6716` | 26,627.02 USD | 564,804.22 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `3991.20` | `57.0115` | 227,544.30 USD | 538,177.19 USD | `9 orders` | `-0.05%` | `-` |
| `BID` | `3991.40` | `0.5812` | 2,319.80 USD | 310,632.90 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3991.50` | `17.4540` | 69,667.64 USD | 308,313.09 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `3991.60` | `5.5758` | 22,256.36 USD | 238,645.45 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3991.70` | `0.0455` | 181.62 USD | 216,389.09 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `3991.80` | `8.7713` | 35,013.28 USD | 216,207.47 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3991.90` | `4.8833` | 19,493.65 USD | 181,194.19 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3992.00` | `3.8990` | 15,564.81 USD | 161,700.55 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `3992.10` | `2.8243` | 11,274.89 USD | 146,135.74 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3992.20` | `0.7314` | 2,919.90 USD | 134,860.85 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3992.40` | `5.8191` | 23,232.17 USD | 131,940.95 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3992.50` | `0.4887` | 1,951.13 USD | 108,708.78 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3992.60` | `3.7569` | 14,999.80 USD | 106,757.65 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3992.70` | `8.2359` | 32,883.48 USD | 91,757.85 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `3992.80` | `5.2587` | 20,996.94 USD | 58,874.37 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3992.90` | `3.7566` | 14,999.73 USD | 37,877.43 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3993.00` | `3.3558` | 13,399.71 USD | 22,877.70 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3993.10` | `0.5196` | 2,074.81 USD | 9,477.99 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3993.30` | `1.8539` | 7,403.18 USD | 7,403.18 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3993.35` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,993.35` | `0.00%` | `-` |
| `ASK` | `3993.40` | `106.9066` | 426,920.82 USD | 426,920.82 USD | `14 orders` | `+0.00%` | `-` |
| `ASK` | `3993.50` | `9.2650` | 36,999.78 USD | 463,920.59 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `3993.60` | `16.9849` | 67,830.90 USD | 531,751.49 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3993.70` | `4.1590` | 16,609.80 USD | 548,361.29 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3993.80` | `80.3756` | 321,004.07 USD | 869,365.36 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3993.90` | `3.7557` | 14,999.89 USD | 884,365.25 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3994.00` | `29.6572` | 118,450.86 USD | 1,002,816.11 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `3994.10` | `53.8294` | 215,000.01 USD | 1,217,816.11 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `3994.20` | `11.8934` | 47,504.62 USD | 1,265,320.73 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3994.30` | `4.1956` | 16,758.49 USD | 1,282,079.22 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `3994.40` | `14.0201` | 56,001.89 USD | 1,338,081.10 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3994.50` | `18.4455` | 73,680.55 USD | 1,411,761.65 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3994.60` | `22.9329` | 91,607.76 USD | 1,503,369.42 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `3994.70` | `1.0602` | 4,235.18 USD | 1,507,604.60 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3994.90` | `17.9826` | 71,838.69 USD | 1,579,443.29 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `3995.10` | `13.1475` | 52,525.58 USD | 1,631,968.86 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `3995.20` | `6.3754` | 25,471.00 USD | 1,657,439.86 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `3995.30` | `14.6473` | 58,520.36 USD | 1,715,960.22 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `3995.40` | `33.5303` | 133,966.96 USD | 1,849,927.18 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `3995.50` | `10.7106` | 42,794.20 USD | 1,892,721.38 USD | `4 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,910,622.32 USD | `6,489.82` | `4185.46` | `3991.10` | `30271.42` | 1,252,328.69 USD | `+4.83%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,144,232.01 USD | `6,298.81` | `4129.54` | `3991.10` | `14019.73` | 867,008.73 USD | `+3.45%` | `5X Cross` |
| `62` | `0xb83d...6e36` | `SHORT` | 23,436,160.34 USD | `5,869.90` | `4228.86` | `3991.10` | `27902.09` | 1,386,861.59 USD | `+5.92%` | `5X Cross` |
| `98` | `0xec0b...b078` | `LONG` | 19,282,791.03 USD | `4,828.91` | `4157.43` | `3991.10` | `2301.41` | -793,091.28 USD | `-4.11%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,148,581.79 USD | `3,544.32` | `4128.09` | `3991.10` | `606.01` | -482,733.35 USD | `-3.41%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 13,048,341.20 USD | `3,268.21` | `4228.94` | `3991.10` | `4398.29` | 772,737.93 USD | `+5.92%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,578,250.40 USD | `2,900.00` | `4364.92` | `3991.10` | `4235.87` | 1,080,025.93 USD | `+9.33%` | `20X Cross` |
| `260` | `0x41e5...0825` | `SHORT` | 8,783,720.00 USD | `2,200.00` | `4112.20` | `3991.10` | `4331.35` | 263,134.59 USD | `+3.00%` | `20X Cross` |
| `261` | `0x3678...b209` | `LONG` | 8,781,960.00 USD | `2,200.00` | `4176.09` | `3991.10` | `2684.08` | -405,459.30 USD | `-4.62%` | `25X Cross` |
| `297` | `0xacb6...efbd` | `SHORT` | 7,886,858.67 USD | `1,975.37` | `4048.55` | `3991.10` | `6605.97` | 110,533.04 USD | `+1.40%` | `6X Cross` |
| `360` | `0xc26c...b8f4` | `LONG` | 6,307,957.56 USD | `1,579.95` | `4075.62` | `3991.10` | `0.000000` | -131,339.41 USD | `-2.08%` | `1X Cross` |
| `512` | `0x354b...6425` | `LONG` | 4,343,383.60 USD | `1,088.05` | `4004.95` | `3991.10` | `0.000000` | -14,205.60 USD | `-0.33%` | `10X Cross` |
| `559` | `0x63da...8add` | `LONG` | 3,992,500.00 USD | `1,000.00` | `4021.46` | `3991.10` | `3564.32` | -28,960.96 USD | `-0.73%` | `25X Cross` |
| `569` | `0xf3dc...1672` | `LONG` | 3,929,307.06 USD | `984.27` | `4018.39` | `3991.10` | `2868.64` | -25,879.63 USD | `-0.66%` | `20X Cross` |
| `581` | `0x9aa5...58af` | `LONG` | 3,879,377.85 USD | `971.64` | `4279.98` | `3991.10` | `0.000000` | -279,231.23 USD | `-7.20%` | `20X Cross` |
| `662` | `0x4a20...3c26` | `LONG` | 3,342,732.12 USD | `837.40` | `4599.73` | `3991.10` | `0.000000` | -509,088.26 USD | `-15.23%` | `20X Cross` |
| `823` | `0x0fac...7a0a` | `LONG` | 2,740,310.82 USD | `686.49` | `4290.34` | `3991.10` | `1294.41` | -204,947.88 USD | `-7.48%` | `25X Cross` |
| `895` | `0xd8c5...99b0` | `SHORT` | 2,516,250.69 USD | `630.35` | `4175.35` | `3991.10` | `33783.84` | 115,706.20 USD | `+4.60%` | `4X Cross` |
| `906` | `0x625e...a354` | `SHORT` | 2,475,412.00 USD | `620.00` | `4122.81` | `3991.10` | `4342.45` | 80,735.03 USD | `+3.26%` | `20X Cross` |
| `935` | `0xeae3...e8ad` | `SHORT` | 2,395,140.00 USD | `600.00` | `4104.77` | `3991.10` | `4325.47` | 67,725.11 USD | `+2.83%` | `20X Cross` |
| `937` | `0xf285...fa82` | `LONG` | 2,387,937.81 USD | `598.11` | `4146.45` | `3991.10` | `3891.45` | -92,081.75 USD | `-3.86%` | `25X Cross` |
| `951` | `0x12f7...8750` | `LONG` | 2,338,050.72 USD | `585.61` | `4082.77` | `3991.10` | `2715.84` | -52,866.26 USD | `-2.26%` | `10X Cross` |
| `1093` | `0x413c...886c` | `LONG` | 1,996,150.00 USD | `500.00` | `4010.43` | `3991.10` | `0.000000` | -9,066.23 USD | `-0.45%` | `2X Cross` |
| `1099` | `0x61ce...a62b` | `SHORT` | 1,986,083.72 USD | `497.50` | `4071.66` | `3991.10` | `4723.52` | 39,585.07 USD | `+1.99%` | `20X Cross` |
| `1177` | `0x2edd...8179` | `LONG` | 1,878,471.26 USD | `469.89` | `4164.68` | `3996.60` | `0.000000` | -78,461.26 USD | `-4.18%` | `10X Cross` |
| `1218` | `0xead5...69f2` | `LONG` | 1,811,777.60 USD | `453.78` | `4220.88` | `3991.10` | `3539.15` | -103,590.46 USD | `-5.72%` | `5X Isolated` |
| `1278` | `0x7a6d...f79c` | `SHORT` | 1,712,478.89 USD | `428.38` | `4136.09` | `3996.60` | `5313.95` | 59,336.11 USD | `+3.46%` | `10X Cross` |
| `1284` | `0x46fc...1195` | `LONG` | 1,692,328.80 USD | `423.95` | `4053.27` | `3991.10` | `2181.95` | -26,061.28 USD | `-1.54%` | `20X Cross` |
| `1355` | `0x6d15...d374` | `LONG` | 1,597,040.00 USD | `400.00` | `4068.25` | `3991.10` | `3842.02` | -30,260.00 USD | `-1.89%` | `25X Cross` |
| `1356` | `0xee02...309d` | `SHORT` | 1,597,000.00 USD | `400.00` | `4438.84` | `3991.10` | `4227.09` | 178,538.60 USD | `+11.18%` | `25X Isolated` |
| `1376` | `0x51f6...2b39` | `LONG` | 1,560,105.31 USD | `390.33` | `4228.91` | `3996.60` | `472.75` | -90,547.78 USD | `-5.80%` | `10X Cross` |
| `1393` | `0x02a7...fe9f` | `SHORT` | 1,557,387.00 USD | `390.00` | `4055.02` | `3991.10` | `4306.91` | 24,072.25 USD | `+1.55%` | `25X Cross` |
| `1427` | `0x7e77...b8d2` | `SHORT` | 1,516,884.00 USD | `380.00` | `4131.92` | `3991.10` | `4293.71` | 53,245.64 USD | `+3.51%` | `20X Cross` |
| `1449` | `0x9c06...0560` | `LONG` | 1,490,244.14 USD | `373.26` | `4018.98` | `3991.10` | `0.000000` | -9,887.66 USD | `-0.66%` | `25X Cross` |
| `1450` | `0x72c2...9b37` | `LONG` | 1,489,577.46 USD | `373.13` | `4000.98` | `3991.10` | `3778.25` | -3,316.05 USD | `-0.22%` | `13X Isolated` |
| `1491` | `0x781e...96b7` | `SHORT` | 1,443,079.33 USD | `361.02` | `4363.60` | `3996.60` | `13507.53` | 132,279.48 USD | `+9.17%` | `10X Cross` |
| `1497` | `0xaa44...b844` | `LONG` | 1,437,228.00 USD | `360.00` | `4043.10` | `3991.10` | `2820.72` | -18,289.63 USD | `-1.27%` | `4X Cross` |
| `1611` | `0xa41f...d50a` | `LONG` | 1,313,644.35 USD | `328.96` | `4468.89` | `3991.10` | `3802.38` | -156,453.50 USD | `-11.91%` | `15X Cross` |
| `1624` | `0x7fda...17d1` | `SHORT` | 1,300,951.57 USD | `325.91` | `4013.13` | `3991.10` | `29800.72` | 6,951.98 USD | `+0.53%` | `20X Cross` |
| `1658` | `0xbf5a...88ba` | `SHORT` | 1,268,237.19 USD | `317.65` | `4091.80` | `3991.10` | `9783.35` | 31,545.84 USD | `+2.49%` | `20X Cross` |
| `1696` | `0xff31...ff6c` | `SHORT` | 1,237,458.00 USD | `310.00` | `4372.43` | `3991.10` | `4789.38` | 117,997.38 USD | `+9.54%` | `10X Isolated` |
| `1717` | `0xada6...6f88` | `LONG` | 1,211,593.57 USD | `303.50` | `4166.46` | `3991.10` | `1796.83` | -52,919.30 USD | `-4.37%` | `5X Cross` |
| `1879` | `0x50e2...d770` | `LONG` | 1,079,252.59 USD | `270.37` | `4243.58` | `3991.10` | `2562.31` | -68,073.87 USD | `-6.31%` | `20X Cross` |
| `1891` | `0x4c92...4f17` | `SHORT` | 1,064,721.56 USD | `266.72` | `4260.98` | `3991.10` | `6508.77` | 71,770.67 USD | `+6.74%` | `20X Cross` |
| `1962` | `0xd346...c4f3` | `LONG` | 1,018,781.40 USD | `255.17` | `4188.66` | `3991.10` | `3310.63` | -50,055.11 USD | `-4.91%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4096.43` (Vol: 350,100.00 USD, Dist: `+2.45%`) | Long MP=`3949.75` (Vol: 346,900.00 USD, Dist: `--1.22%`)
  * 48H Horizon: Short MP=`4110.89` (Vol: 346,900.00 USD, Dist: `+2.81%`) | Long MP=`3950.25` (Vol: 348,600.00 USD, Dist: `--1.21%`)
  * 3D Horizon: Short MP=`4110.89` (Vol: 386,200.00 USD, Dist: `+2.81%`) | Long MP=`3950.25` (Vol: 373,700.00 USD, Dist: `--1.21%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 893,800.00 USD, Dist: `+2.82%`) | Long MP=`3923.02` (Vol: 1,000,000.00 USD, Dist: `--1.89%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,240,000.00 USD | 16,240,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,170,000.00 USD | 16,170,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.40` | 3,900,000.00 USD | 3,900,000.00 USD | 30,440.00 USD | 0.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,030,000.00 USD | 16,030,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.50` | 3,870,000.00 USD | 3,870,000.00 USD | 69,970.00 USD | 0.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 15,960,000.00 USD | 15,960,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3626.60` | 3,790,000.00 USD | 3,790,000.00 USD | 41,750.00 USD | 0.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,870,000.00 USD | 15,870,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.70` | 3,740,000.00 USD | 3,740,000.00 USD | 35,480.00 USD | 0.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,680,000.00 USD | 15,680,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.80` | 3,700,000.00 USD | 3,700,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,570,000.00 USD | 15,570,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3638.90` | 3,670,000.00 USD | 3,670,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,440,000.00 USD | 15,440,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.00` | 3,630,000.00 USD | 3,630,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,370,000.00 USD | 15,370,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.10` | 3,610,000.00 USD | 3,610,000.00 USD | 12,080.00 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,330,000.00 USD | 15,330,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.20` | 3,600,000.00 USD | 3,600,000.00 USD | 12,210.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,310,000.00 USD | 15,310,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.30` | 3,590,000.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,280,000.00 USD | 15,280,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,250,000.00 USD | 15,250,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,220,000.00 USD | 15,220,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,210,000.00 USD | 15,210,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,850,000.00 USD | 14,850,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,360,000.00 USD | 14,360,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,830,000.00 USD | 13,830,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.10` | 3,580,000.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,510,000.00 USD | 13,510,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.20` | 3,580,000.00 USD | 3,580,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,200,000.00 USD | 13,200,000.00 USD | 272,330.00 USD | 0.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.30` | 3,490,000.00 USD | 3,490,000.00 USD | 121,680.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,910,000.00 USD | 12,910,000.00 USD | 183,740.00 USD | 0.00 USD | 76,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.40` | 3,350,000.00 USD | 3,350,000.00 USD | 202,550.00 USD | 0.00 USD | 35,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,650,000.00 USD | 12,650,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.50` | 3,120,000.00 USD | 3,120,000.00 USD | 151,760.00 USD | 0.00 USD | 23,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,110,000.00 USD | 12,110,000.00 USD | 352,520.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.60` | 2,940,000.00 USD | 2,940,000.00 USD | 142,240.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,710,000.00 USD | 11,710,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.70` | 2,780,000.00 USD | 2,780,000.00 USD | 76,690.00 USD | 0.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,170,000.00 USD | 11,170,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.80` | 2,700,000.00 USD | 2,700,000.00 USD | 128,720.00 USD | 0.00 USD | 19,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,830,000.00 USD | 10,830,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3884.90` | 2,550,000.00 USD | 2,550,000.00 USD | 24,980.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,690,000.00 USD | 10,690,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.00` | 2,510,000.00 USD | 2,510,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,580,000.00 USD | 10,580,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.10` | 2,480,000.00 USD | 2,480,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,450,000.00 USD | 10,450,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.20` | 2,440,000.00 USD | 2,440,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,340,000.00 USD | 10,340,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.30` | 2,400,000.00 USD | 2,400,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,250,000.00 USD | 10,250,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,210,000.00 USD | 10,210,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,160,000.00 USD | 10,160,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,140,000.00 USD | 10,140,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,410,000.00 USD | 9,410,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,460,000.00 USD | 8,460,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,570,000.00 USD | 7,570,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.10` | 2,390,000.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,730,000.00 USD | 6,730,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.20` | 2,320,000.00 USD | 2,320,000.00 USD | 153,540.00 USD | 0.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,270,000.00 USD | 6,270,000.00 USD | 625,340.00 USD | 0.00 USD | 39,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.30` | 2,150,000.00 USD | 2,150,000.00 USD | 299,910.00 USD | 0.00 USD | 59,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,600,000.00 USD | 5,600,000.00 USD | 376,840.00 USD | 0.00 USD | 113,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.40` | 1,790,000.00 USD | 1,790,000.00 USD | 385,320.00 USD | 0.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,110,000.00 USD | 5,110,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.50` | 1,360,000.00 USD | 1,360,000.00 USD | 359,720.00 USD | 0.00 USD | 40,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,140,000.00 USD | 4,140,000.00 USD | 848,650.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.60` | 955,040.00 USD | 955,040.00 USD | 170,180.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.70` | 752,230.00 USD | 752,230.00 USD | 255,750.00 USD | 0.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3962.80` | 487,860.00 USD | 487,860.00 USD | 139,630.00 USD | 0.00 USD | 49,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3966.90` | 298,610.00 USD | 298,610.00 USD | 36,900.00 USD | 0.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.00` | 243,280.00 USD | 243,280.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.10` | 167,990.00 USD | 167,990.00 USD | 102,560.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.20` | 58,070.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.30` | 23,310.00 USD | 23,310.00 USD | 19,950.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.00` | 27,170.00 USD | 27,170.00 USD | 20,110.00 USD | 0.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.10` | 183,960.00 USD | 183,960.00 USD | 149,400.00 USD | 0.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.20` | 504,520.00 USD | 504,520.00 USD | 263,830.00 USD | 0.00 USD | 56,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,870,000.00 USD | 4,870,000.00 USD | 330,140.00 USD | 0.00 USD | 115,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.30` | 986,760.00 USD | 986,760.00 USD | 428,010.00 USD | 0.00 USD | 54,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,490,000.00 USD | 5,490,000.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.40` | 1,290,000.00 USD | 1,290,000.00 USD | 258,370.00 USD | 0.00 USD | 41,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,670,000.00 USD | 6,670,000.00 USD | 1,090,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.50` | 1,580,000.00 USD | 1,580,000.00 USD | 264,830.00 USD | 0.00 USD | 32,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,320,000.00 USD | 7,320,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.60` | 1,760,000.00 USD | 1,760,000.00 USD | 160,660.00 USD | 0.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,330,000.00 USD | 8,330,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.70` | 2,050,000.00 USD | 2,050,000.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,840,000.00 USD | 8,840,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4126.80` | 2,140,000.00 USD | 2,140,000.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,090,000.00 USD | 9,090,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4130.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,310,000.00 USD | 9,310,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.00` | 2,280,000.00 USD | 2,280,000.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,540,000.00 USD | 9,540,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.10` | 2,330,000.00 USD | 2,330,000.00 USD | 37,970.00 USD | 0.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,760,000.00 USD | 9,760,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.20` | 2,370,000.00 USD | 2,370,000.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,920,000.00 USD | 9,920,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.30` | 2,390,000.00 USD | 2,390,000.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,020,000.00 USD | 10,020,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,110,000.00 USD | 10,110,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,490,000.00 USD | 10,490,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,920,000.00 USD | 10,920,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,250,000.00 USD | 11,250,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,760,000.00 USD | 11,760,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,910,000.00 USD | 11,910,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.00` | 2,430,000.00 USD | 2,430,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,360,000.00 USD | 12,360,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.10` | 2,530,000.00 USD | 2,530,000.00 USD | 89,560.00 USD | 0.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,530,000.00 USD | 12,530,000.00 USD | 133,800.00 USD | 0.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.20` | 2,700,000.00 USD | 2,700,000.00 USD | 144,610.00 USD | 0.00 USD | 30,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,850,000.00 USD | 12,850,000.00 USD | 249,690.00 USD | 0.00 USD | 66,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.30` | 2,900,000.00 USD | 2,900,000.00 USD | 173,790.00 USD | 0.00 USD | 26,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,430,000.00 USD | 13,430,000.00 USD | 556,060.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.40` | 3,100,000.00 USD | 3,100,000.00 USD | 179,860.00 USD | 0.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,750,000.00 USD | 13,750,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.50` | 3,200,000.00 USD | 3,200,000.00 USD | 85,090.00 USD | 0.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,190,000.00 USD | 14,190,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.60` | 3,310,000.00 USD | 3,310,000.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,530,000.00 USD | 14,530,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.70` | 3,420,000.00 USD | 3,420,000.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,670,000.00 USD | 14,670,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4208.80` | 3,460,000.00 USD | 3,460,000.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,780,000.00 USD | 14,780,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.90` | 3,480,000.00 USD | 3,480,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,890,000.00 USD | 14,890,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.00` | 3,530,000.00 USD | 3,530,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,000,000.00 USD | 15,000,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.10` | 3,560,000.00 USD | 3,560,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,100,000.00 USD | 15,100,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,150,000.00 USD | 15,150,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.30` | 3,580,000.00 USD | 3,580,000.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,200,000.00 USD | 15,200,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,220,000.00 USD | 15,220,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,300,000.00 USD | 15,300,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,420,000.00 USD | 15,420,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,560,000.00 USD | 15,560,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,700,000.00 USD | 15,700,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,760,000.00 USD | 15,760,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4413.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 300.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,890,000.00 USD | 15,890,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4417.90` | 3,600,000.00 USD | 3,600,000.00 USD | 23,120.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,940,000.00 USD | 15,940,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.00` | 3,630,000.00 USD | 3,630,000.00 USD | 21,930.00 USD | 0.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.10` | 3,680,000.00 USD | 3,680,000.00 USD | 38,710.00 USD | 0.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,000,000.00 USD | 16,000,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.20` | 3,740,000.00 USD | 3,740,000.00 USD | 53,490.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,110,000.00 USD | 16,110,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.30` | 3,780,000.00 USD | 3,780,000.00 USD | 33,280.00 USD | 0.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,260,000.00 USD | 16,260,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,340,000.00 USD | 16,340,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,500,000.00 USD | 16,500,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,530,000.00 USD | 16,530,000.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.30` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,170,000.00 USD | 0.00 USD | 16,170,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.40` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 30,440.00 USD | 0.00 USD | 3,780.00 USD |
| `7D` | `3619.70` | 16,030,000.00 USD | 0.00 USD | 16,030,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3622.50` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 69,970.00 USD | 0.00 USD | 10,330.00 USD |
| `7D` | `3623.90` | 15,960,000.00 USD | 0.00 USD | 15,960,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3626.60` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 41,750.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3628.10` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3630.70` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 35,480.00 USD | 0.00 USD | 5,650.00 USD |
| `7D` | `3632.30` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3634.80` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD |
| `7D` | `3636.50` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3638.90` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD |
| `7D` | `3640.70` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3643.00` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `3644.90` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3647.10` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 12,080.00 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `3649.10` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.20` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 12,210.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `3653.30` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.30` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.70` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,850,000.00 USD | 0.00 USD | 14,850,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.10` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD |
| `7D` | `3854.90` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.20` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `3859.10` | 13,200,000.00 USD | 0.00 USD | 13,200,000.00 USD | 272,330.00 USD | 0.00 USD | 19,140.00 USD |
| `1D` | `3860.30` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 121,680.00 USD | 0.00 USD | 17,380.00 USD |
| `7D` | `3863.30` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 183,740.00 USD | 0.00 USD | 76,420.00 USD |
| `1D` | `3864.40` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 202,550.00 USD | 0.00 USD | 35,420.00 USD |
| `7D` | `3867.50` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3868.50` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 151,760.00 USD | 0.00 USD | 23,530.00 USD |
| `7D` | `3871.70` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 352,520.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3872.60` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 142,240.00 USD | 0.00 USD | 18,230.00 USD |
| `7D` | `3875.90` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3876.70` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 76,690.00 USD | 0.00 USD | 5,830.00 USD |
| `7D` | `3880.10` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3880.80` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 128,720.00 USD | 0.00 USD | 19,540.00 USD |
| `7D` | `3884.30` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3884.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 24,980.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3888.50` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3889.00` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `3892.70` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3893.10` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `3896.90` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3897.20` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `3901.10` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3901.30` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3905.30` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3934.10` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3934.70` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.20` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 153,540.00 USD | 0.00 USD | 14,710.00 USD |
| `7D` | `3938.90` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 625,340.00 USD | 0.00 USD | 39,370.00 USD |
| `1D` | `3942.30` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 299,910.00 USD | 0.00 USD | 59,080.00 USD |
| `7D` | `3943.10` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 376,840.00 USD | 0.00 USD | 113,800.00 USD |
| `1D` | `3946.40` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 385,320.00 USD | 0.00 USD | 53,070.00 USD |
| `7D` | `3947.30` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD |
| `1D` | `3950.50` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 359,720.00 USD | 0.00 USD | 40,530.00 USD |
| `7D` | `3951.50` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 848,650.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3954.60` | 955,040.00 USD | 0.00 USD | 955,040.00 USD | 170,180.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3958.70` | 752,230.00 USD | 0.00 USD | 752,230.00 USD | 255,750.00 USD | 0.00 USD | 8,620.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3962.80` | 487,860.00 USD | 0.00 USD | 487,860.00 USD | 139,630.00 USD | 0.00 USD | 49,610.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3966.90` | 298,610.00 USD | 0.00 USD | 298,610.00 USD | 36,900.00 USD | 0.00 USD | 18,440.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.00` | 243,280.00 USD | 0.00 USD | 243,280.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.10` | 167,990.00 USD | 0.00 USD | 167,990.00 USD | 102,560.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.20` | 58,070.00 USD | 0.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 10,850.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.30` | 23,310.00 USD | 0.00 USD | 23,310.00 USD | 19,950.00 USD | 0.00 USD | 3,370.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4020.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4020.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `1D` | `4094.00` | 27,170.00 USD | 27,170.00 USD | 0.00 USD | 20,110.00 USD | 0.00 USD | 7,060.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4098.10` | 183,960.00 USD | 183,960.00 USD | 0.00 USD | 149,400.00 USD | 0.00 USD | 7,400.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4102.20` | 504,520.00 USD | 504,520.00 USD | 0.00 USD | 263,830.00 USD | 0.00 USD | 56,730.00 USD |
| `7D` | `4102.70` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 115,300.00 USD |
| `1D` | `4106.30` | 986,760.00 USD | 986,760.00 USD | 0.00 USD | 428,010.00 USD | 0.00 USD | 54,230.00 USD |
| `7D` | `4106.90` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD |
| `1D` | `4110.40` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 258,370.00 USD | 0.00 USD | 41,060.00 USD |
| `7D` | `4111.10` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4114.50` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 264,830.00 USD | 0.00 USD | 32,150.00 USD |
| `7D` | `4115.30` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4118.60` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 160,660.00 USD | 0.00 USD | 14,120.00 USD |
| `7D` | `4119.50` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4122.70` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `4123.70` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4126.80` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD |
| `7D` | `4127.90` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4130.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,270.00 USD |
| `7D` | `4132.10` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.00` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4136.30` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.10` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 37,970.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `4140.50` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.20` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,920,000.00 USD | 9,920,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.30` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.00` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.10` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 89,560.00 USD | 0.00 USD | 5,930.00 USD |
| `7D` | `4182.50` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 40,030.00 USD |
| `1D` | `4184.20` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 144,610.00 USD | 0.00 USD | 30,460.00 USD |
| `7D` | `4186.70` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 66,760.00 USD |
| `1D` | `4188.30` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 173,790.00 USD | 0.00 USD | 26,620.00 USD |
| `7D` | `4190.90` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 556,060.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4192.40` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 179,860.00 USD | 0.00 USD | 18,810.00 USD |
| `7D` | `4195.10` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4196.50` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 85,090.00 USD | 0.00 USD | 15,950.00 USD |
| `7D` | `4199.30` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4200.60` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4203.50` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4204.70` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD |
| `7D` | `4207.70` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4208.80` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD |
| `7D` | `4211.90` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4212.90` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `4216.10` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4217.00` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `4220.30` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4221.10` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `4224.50` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4225.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4229.30` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4413.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 300.94 USD |
| `7D` | `4417.70` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4417.90` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 23,120.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `4421.90` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4422.00` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 21,930.00 USD | 0.00 USD | 2,500.00 USD |
| `1D` | `4426.10` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 38,710.00 USD | 0.00 USD | 8,260.00 USD |
| `7D` | `4426.10` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4430.20` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 53,490.00 USD | 0.00 USD | 8,690.00 USD |
| `7D` | `4430.30` | 16,110,000.00 USD | 16,110,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4433.30` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 33,280.00 USD | 0.00 USD | 4,000.00 USD |
| `7D` | `4434.50` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `4438.70` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.44M` | Total OI Tokens: `68,905.3 PAXG`
  * 1h OI Change: `-0.02%` | 4h OI Change: `+0.61%` | 24h OI Change: `+0.61%`
  * Exchange Breakdown: Binance=`107.25M` | Bybit=`21.15M` | OKX=`-` | Hyperliquid=`24.63M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-563.10` | Last 24h: `24.09K` | Last 3d: `91.36K` | Last 7d: `222.86K`
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
| `15M` | `PAXG` | `49.22%` | `50.78%` | `0.97` | 1,020,000.00 USD |
| `15M` | `Binance` | `47.3%` | `52.7%` | `0.90` | 395,230.00 USD |
| `15M` | `OKX` | `54.33%` | `45.67%` | `1.19` | 117,900.00 USD |
| `15M` | `Bybit` | `37.16%` | `62.84%` | `0.59` | 102,680.00 USD |
| `15M` | `KuCoin` | `46.7%` | `53.3%` | `0.88` | 50,460.00 USD |
| `15M` | `Gate` | `70.64%` | `29.36%` | `2.41` | 33,650.00 USD |
| `15M` | `Bitget` | `12.96%` | `87.04%` | `0.15` | 13,910.00 USD |
| `15M` | `BingX` | `40.27%` | `59.73%` | `0.67` | 27,750.00 USD |
| `15M` | `MEXC` | `69.07%` | `30.93%` | `2.23` | 58,310.00 USD |
| `15M` | `Bitunix` | `40.7%` | `59.3%` | `0.69` | 8,410.00 USD |
| `15M` | `Hyperliquid` | `46.61%` | `53.39%` | `0.87` | 1,430.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.72%` | `50.28%` | `0.99` | 202,060.00 USD |
| `15M` | `Crypto.com` | `0.01%` | `99.99%` | `0.00` | 688.76 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 8,400.00 USD |
| `15M` | `HTX` | `0.68%` | `99.32%` | `0.01` | 75.96 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 89.57 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0.31%` | `99.69%` | `0.00` | 320.79 USD |
| `15M` | `Whale Positions` | `47.3%` | `52.7%` | `0.90` | 395,230.00 USD |
| `15M` | `Global Accounts` | `49.22%` | `50.78%` | `0.97` | 1,020,000.00 USD |
| `1H` | `PAXG` | `53.61%` | `46.39%` | `1.16` | 3,510,000.00 USD |
| `1H` | `Binance` | `57.07%` | `42.93%` | `1.33` | 1,310,000.00 USD |
| `1H` | `OKX` | `52.01%` | `47.99%` | `1.08` | 493,300.00 USD |
| `1H` | `Bybit` | `65.26%` | `34.74%` | `1.88` | 384,690.00 USD |
| `1H` | `KuCoin` | `50.22%` | `49.78%` | `1.01` | 368,780.00 USD |
| `1H` | `Gate` | `42.9%` | `57.1%` | `0.75` | 120,570.00 USD |
| `1H` | `Bitget` | `73.77%` | `26.23%` | `2.81` | 73,280.00 USD |
| `1H` | `BingX` | `47.14%` | `52.86%` | `0.89` | 254,570.00 USD |
| `1H` | `MEXC` | `42.08%` | `57.92%` | `0.73` | 162,820.00 USD |
| `1H` | `Bitunix` | `53%` | `47%` | `1.13` | 45,220.00 USD |
| `1H` | `Hyperliquid` | `64.83%` | `35.17%` | `1.84` | 49,580.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.53%` | `50.47%` | `0.98` | 156,400.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `10.36%` | `89.64%` | `0.12` | 79,920.00 USD |
| `1H` | `HTX` | `4.55%` | `95.45%` | `0.05` | 1,990.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `100%` | `0%` | `1.00` | 573.23 USD |
| `1H` | `Aster` | `89.29%` | `10.71%` | `8.34` | 3,890.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `5.27%` | `94.73%` | `0.06` | 3,020.00 USD |
| `1H` | `Whale Positions` | `57.07%` | `42.93%` | `1.33` | 1,310,000.00 USD |
| `1H` | `Global Accounts` | `53.61%` | `46.39%` | `1.16` | 3,510,000.00 USD |
| `4H` | `PAXG` | `50.16%` | `49.84%` | `1.01` | 83,010,000.00 USD |
| `4H` | `Binance` | `49.44%` | `50.56%` | `0.98` | 33,490,000.00 USD |
| `4H` | `OKX` | `52.69%` | `47.31%` | `1.11` | 11,670,000.00 USD |
| `4H` | `Bybit` | `51.34%` | `48.66%` | `1.06` | 11,180,000.00 USD |
| `4H` | `KuCoin` | `45.73%` | `54.27%` | `0.84` | 656,440.00 USD |
| `4H` | `Gate` | `48.68%` | `51.32%` | `0.95` | 3,270,000.00 USD |
| `4H` | `Bitget` | `54.36%` | `45.64%` | `1.19` | 6,090,000.00 USD |
| `4H` | `BingX` | `41.71%` | `58.29%` | `0.72` | 2,410,000.00 USD |
| `4H` | `MEXC` | `48.9%` | `51.1%` | `0.96` | 3,690,000.00 USD |
| `4H` | `Bitunix` | `47.7%` | `52.3%` | `0.91` | 2,140,000.00 USD |
| `4H` | `Hyperliquid` | `47.13%` | `52.87%` | `0.89` | 4,570,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.3%` | `51.7%` | `0.93` | 2,750,000.00 USD |
| `4H` | `Crypto.com` | `44.53%` | `55.47%` | `0.80` | 32,900.00 USD |
| `4H` | `WhiteBIT` | `80.59%` | `19.41%` | `4.15` | 532,300.00 USD |
| `4H` | `HTX` | `52.05%` | `47.95%` | `1.09` | 134,580.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.32%` | `52.68%` | `0.90` | 134,880.00 USD |
| `4H` | `Aster` | `50.12%` | `49.88%` | `1.00` | 76,140.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `33.19%` | `66.81%` | `0.50` | 181,380.00 USD |
| `4H` | `Whale Positions` | `49.44%` | `50.56%` | `0.98` | 33,490,000.00 USD |
| `4H` | `Global Accounts` | `50.16%` | `49.84%` | `1.01` | 83,010,000.00 USD |


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
| `5m` | -102,650.00 USD | 44,910.00 USD | **`DISTRIBUTION`** |
| `15m` | -176,590.00 USD | 45,650.00 USD | **`DISTRIBUTION`** |
| `30m` | -155,870.00 USD | 108,250.00 USD | **`DISTRIBUTION`** |
| `1h` | -96,080.00 USD | -81,130.00 USD | **`DISTRIBUTION`** |
| `2h` | -262,320.00 USD | -65,480.00 USD | **`DISTRIBUTION`** |
| `4h` | -76,170.00 USD | -757,990.00 USD | **`DISTRIBUTION`** |
| `6h` | 12,230.00 USD | -982,710.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,140,000.00 USD | -1,120,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -876,730.00 USD | 174,610.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,340,000.00 USD | -407,140.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,660,000.00 USD | -9,140,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,880,000.00 USD | -71,890,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-102.65K` | 15m=`-176.59K` | 1h=`-96.08K` | 24h=`-1.34M`
* Futures Capital Netflows: 5m=`+44.91K` | 15m=`+45.65K` | 1h=`-81.13K` | 24h=`-407.14K`
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
  * `2026-10-30 09:09:49 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:41:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:43:49 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3997.85` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3988.05` (Risk Distance: `9.80` pts)
  * +2.5R Take Profit: `4022.34`
  * Mathematical Lot Sizing: **`1.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.20` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4023.00` (Risk Distance: `9.80` pts)
  * +2.5R Take Profit: `3988.71`
  * Mathematical Lot Sizing: **`1.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4022.53`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
