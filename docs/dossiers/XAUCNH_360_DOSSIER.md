# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-29 23:37:49 IST` (`2026-10-29 18:07:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26687.80` | **Live Ask Quote**: `26689.67` | **Mid Price**: `26688.74`
- **Spread Points**: `187.00` | **Spread BPS**: `0.70 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26688.74` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.72` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26875.56` | Lower -3.00σ Band: `26501.91`
  * Upper +2.51σ Band: `26835.52` | Lower -2.51σ Band: `26541.95`
  * Upper +2.01σ Band: `26800.83` | Lower -2.01σ Band: `26576.64`
  * Upper +2.00σ Band: `26795.49` | Lower -2.00σ Band: `26581.98`
  * Upper +1.28σ Band: `26763.46` | Lower -1.28σ Band: `26614.01`
  * Upper +1.00σ Band: `26742.11` | Lower -1.00σ Band: `26635.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26688.74` | EMA-20=`26688.74` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26688.74` (Slope: `+0.0000`) | EMA-100=`26688.74`
  * Institutional Anchors: EMA-144=`26688.74` | EMA-200=`26688.74` (Slope: `+0.0000`) | EMA-233=`26688.74`
- **Range Boundaries**: 24H High=`26955.62` | 24H Low=`26421.85` | Weekly High=`27222.51` | Weekly Low=`26154.96`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26768.80` (Distance: `+0.00%`)
  * Point of Control (POC) = `26688.74` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26608.67` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26795.49` | POC=`26688.74` | VAL=`26581.98`
  * Prior Day Extremes: PDH=`26848.87` | PDL=`26528.60` | PDC=`26688.74`
  * Monday Range Blueprint: High=`26822.18` | Mid=`26688.74` | Low=`26555.29`
  * Developing Weekly Value Area: Weekly VAH=`26902.24` | Weekly POC=`26688.74` | Weekly VAL=`26475.23`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26742.11` | Low=`26635.36`
  * London Session (08:00-16:00 UTC): High=`26795.49` | Low=`26581.98`
  * New York Session (13:00-21:00 UTC): High=`26848.87` | Low=`26528.60`
  * Initial Balance (First Hour): IB High=`26768.80` | IB Low=`26608.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26581.98` - `26795.49`
  * Optimal Trade Entry (OTE 0.705): `26742.11`
  * Structural Invalidation Anchor (0.786): `26902.24`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15m` | - | - | - | - | - | 0.00 USD | 0.00 USD | `+0.00%` | 0.00 USD | `0.00` | **`BALANCED`** | Interbank Volume |

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
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

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
| `1259` | `0xead5...69f2` | `LONG` | 1,820,308.74 USD | `453.78` | `4220.88` | `4010.60` | `3538.86` | -95,059.32 USD | `-5.22%` | `5X Isolated` |
| `1386` | `0x46fc...1195` | `LONG` | 1,632,754.12 USD | `407.03` | `4055.53` | `4010.60` | `1911.29` | -17,965.69 USD | `-1.10%` | `20X Cross` |
| `1420` | `0x6d15...d374` | `LONG` | 1,604,560.00 USD | `400.00` | `4068.25` | `4010.60` | `3841.73` | -22,740.00 USD | `-1.42%` | `25X Cross` |
| `1421` | `0xee02...309d` | `SHORT` | 1,604,560.00 USD | `400.00` | `4438.84` | `4010.60` | `4226.81` | 170,978.60 USD | `+10.66%` | `25X Isolated` |
| `1452` | `0x02a7...fe9f` | `SHORT` | 1,564,446.00 USD | `390.00` | `4055.02` | `4010.60` | `4306.63` | 17,013.25 USD | `+1.09%` | `25X Cross` |
| `1488` | `0x7e77...b8d2` | `SHORT` | 1,524,332.00 USD | `380.00` | `4131.92` | `4010.60` | `4293.44` | 45,797.64 USD | `+3.00%` | `20X Cross` |
| `1508` | `0x72c2...9b37` | `LONG` | 1,496,778.90 USD | `373.13` | `4000.98` | `4010.60` | `3777.97` | 3,885.38 USD | `+0.26%` | `13X Isolated` |
| `1545` | `0xaa44...b844` | `LONG` | 1,444,104.00 USD | `360.00` | `4043.10` | `4010.60` | `2816.92` | -11,413.63 USD | `-0.79%` | `9X Cross` |
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
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
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
| `7D` | `3606.60` | 22,870,000.00 USD | 0.00 USD | 22,870,000.00 USD | 25,640.00 USD | 0.00 USD | 82,740.00 USD |
| `1D` | `3608.90` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 6,510.00 USD |
| `7D` | `3610.80` | 22,760,000.00 USD | 0.00 USD | 22,760,000.00 USD | 41,120.00 USD | 0.00 USD | 60,830.00 USD |
| `1D` | `3613.10` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 5,770.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `3615.00` | 22,660,000.00 USD | 0.00 USD | 22,660,000.00 USD | 82,510.00 USD | 0.00 USD | 67,760.00 USD |
| `1D` | `3617.30` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 7,370.00 USD | 0.00 USD | 23,180.00 USD |
| `7D` | `3619.20` | 22,510,000.00 USD | 0.00 USD | 22,510,000.00 USD | 44,160.00 USD | 0.00 USD | 126,270.00 USD |
| `1D` | `3621.50` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 16,740.00 USD | 0.00 USD | 70,080.00 USD |
| `7D` | `3623.40` | 22,340,000.00 USD | 0.00 USD | 22,340,000.00 USD | 74,730.00 USD | 0.00 USD | 189,810.00 USD |
| `1D` | `3625.70` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 16,750.00 USD | 0.00 USD | 31,000.00 USD |
| `7D` | `3627.60` | 22,080,000.00 USD | 0.00 USD | 22,080,000.00 USD | 69,700.00 USD | 0.00 USD | 52,580.00 USD |
| `1D` | `3629.90` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 52,240.00 USD | 0.00 USD | 59,800.00 USD |
| `7D` | `3631.80` | 21,950,000.00 USD | 0.00 USD | 21,950,000.00 USD | 40,350.00 USD | 0.00 USD | 97,860.00 USD |
| `1D` | `3634.10` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 35,700.00 USD | 0.00 USD | 25,410.00 USD |
| `7D` | `3636.00` | 21,820,000.00 USD | 0.00 USD | 21,820,000.00 USD | 69,010.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3638.30` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 11,970.00 USD | 0.00 USD | 2,500.00 USD |
| `7D` | `3640.20` | 21,750,000.00 USD | 0.00 USD | 21,750,000.00 USD | 45,100.00 USD | 0.00 USD | 12,090.00 USD |
| `1D` | `3642.50` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 17,700.00 USD | 0.00 USD | 5,960.00 USD |
| `7D` | `3644.40` | 21,690,000.00 USD | 0.00 USD | 21,690,000.00 USD | 32,450.00 USD | 0.00 USD | 7,240.00 USD |
| `1D` | `3646.70` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 10,690.00 USD | 0.00 USD | 17,870.00 USD |
| `7D` | `3648.60` | 21,650,000.00 USD | 0.00 USD | 21,650,000.00 USD | 7,110.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3650.90` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 17,890.00 USD | 0.00 USD | 13,210.00 USD |
| `7D` | `3652.80` | 21,620,000.00 USD | 0.00 USD | 21,620,000.00 USD | 2,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.10` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 5,180.00 USD | 0.00 USD | 11,150.00 USD |
| `7D` | `3657.00` | 21,620,000.00 USD | 0.00 USD | 21,620,000.00 USD | 14,670.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3659.30` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 8,370.00 USD | 0.00 USD | 16,130.00 USD |
| `7D` | `3661.20` | 21,600,000.00 USD | 0.00 USD | 21,600,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3820.80` | 21,600,000.00 USD | 0.00 USD | 21,600,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3825.00` | 21,580,000.00 USD | 0.00 USD | 21,580,000.00 USD | 21,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.20` | 21,560,000.00 USD | 0.00 USD | 21,560,000.00 USD | 101,060.00 USD | 0.00 USD | 171,370.00 USD |
| `7D` | `3833.40` | 21,290,000.00 USD | 0.00 USD | 21,290,000.00 USD | 204,730.00 USD | 0.00 USD | 429,430.00 USD |
| `7D` | `3837.60` | 20,660,000.00 USD | 0.00 USD | 20,660,000.00 USD | 299,300.00 USD | 0.00 USD | 796,720.00 USD |
| `7D` | `3841.80` | 19,560,000.00 USD | 0.00 USD | 19,560,000.00 USD | 327,490.00 USD | 0.00 USD | 311,660.00 USD |
| `7D` | `3846.00` | 18,920,000.00 USD | 0.00 USD | 18,920,000.00 USD | 94,400.00 USD | 0.00 USD | 284,200.00 USD |
| `1D` | `3848.30` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 8,810.00 USD |
| `7D` | `3850.20` | 18,540,000.00 USD | 0.00 USD | 18,540,000.00 USD | 74,560.00 USD | 0.00 USD | 185,580.00 USD |
| `1D` | `3852.50` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 11,930.00 USD | 0.00 USD | 47,520.00 USD |
| `7D` | `3854.40` | 18,280,000.00 USD | 0.00 USD | 18,280,000.00 USD | 258,410.00 USD | 0.00 USD | 238,150.00 USD |
| `1D` | `3856.70` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 20,740.00 USD | 0.00 USD | 66,550.00 USD |
| `7D` | `3858.60` | 17,780,000.00 USD | 0.00 USD | 17,780,000.00 USD | 169,730.00 USD | 0.00 USD | 293,860.00 USD |
| `1D` | `3860.90` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 46,300.00 USD | 0.00 USD | 121,080.00 USD |
| `7D` | `3862.80` | 17,320,000.00 USD | 0.00 USD | 17,320,000.00 USD | 305,210.00 USD | 0.00 USD | 507,720.00 USD |
| `1D` | `3865.10` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 66,490.00 USD | 0.00 USD | 179,860.00 USD |
| `7D` | `3867.00` | 16,510,000.00 USD | 0.00 USD | 16,510,000.00 USD | 169,570.00 USD | 0.00 USD | 360,260.00 USD |
| `1D` | `3869.30` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 108,200.00 USD | 0.00 USD | 80,500.00 USD |
| `7D` | `3871.20` | 15,980,000.00 USD | 0.00 USD | 15,980,000.00 USD | 175,790.00 USD | 0.00 USD | 201,390.00 USD |
| `1D` | `3873.50` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 108,080.00 USD | 0.00 USD | 168,490.00 USD |
| `7D` | `3875.40` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 170,610.00 USD | 0.00 USD | 184,350.00 USD |
| `1D` | `3877.70` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 87,490.00 USD | 0.00 USD | 42,370.00 USD |
| `7D` | `3879.60` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 235,310.00 USD | 0.00 USD | 18,540.00 USD |
| `1D` | `3881.90` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 23,730.00 USD | 0.00 USD | 4,430.00 USD |
| `7D` | `3883.80` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 153,020.00 USD | 0.00 USD | 72,260.00 USD |
| `1D` | `3886.10` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 53,410.00 USD | 0.00 USD | 21,710.00 USD |
| `7D` | `3888.00` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 47,590.00 USD | 0.00 USD | 97,950.00 USD |
| `1D` | `3890.30` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 33,650.00 USD | 0.00 USD | 37,880.00 USD |
| `7D` | `3892.20` | 14,620,000.00 USD | 0.00 USD | 14,620,000.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `3894.50` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 47,660.00 USD | 0.00 USD | 39,080.00 USD |
| `7D` | `3896.40` | 14,550,000.00 USD | 0.00 USD | 14,550,000.00 USD | 25,520.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3898.70` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 18,880.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `3900.60` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 74,670.00 USD | 0.00 USD | 75,140.00 USD |
| `1D` | `3902.90` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 25,190.00 USD | 0.00 USD | 40,320.00 USD |
| `7D` | `3904.80` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 48,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3907.10` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3909.00` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 202,120.00 USD | 0.00 USD | 342,730.00 USD |
| `7D` | `3913.20` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 409,470.00 USD | 0.00 USD | 858,860.00 USD |
| `7D` | `3917.40` | 12,520,000.00 USD | 0.00 USD | 12,520,000.00 USD | 598,600.00 USD | 0.00 USD | 1,500,000.00 USD |
| `7D` | `3921.60` | 10,420,000.00 USD | 0.00 USD | 10,420,000.00 USD | 654,980.00 USD | 0.00 USD | 683,960.00 USD |
| `7D` | `3925.80` | 9,080,000.00 USD | 0.00 USD | 9,080,000.00 USD | 188,800.00 USD | 0.00 USD | 579,920.00 USD |
| `7D` | `3930.00` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 149,120.00 USD | 0.00 USD | 392,150.00 USD |
| `1D` | `3932.30` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 23,870.00 USD | 0.00 USD | 112,650.00 USD |
| `7D` | `3934.20` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 470,890.00 USD | 0.00 USD | 344,800.00 USD |
| `1D` | `3936.50` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 35,260.00 USD | 0.00 USD | 95,710.00 USD |
| `7D` | `3938.40` | 6,950,000.00 USD | 0.00 USD | 6,950,000.00 USD | 374,080.00 USD | 0.00 USD | 719,210.00 USD |
| `1D` | `3940.70` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 79,900.00 USD | 0.00 USD | 181,030.00 USD |
| `7D` | `3942.60` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 453,980.00 USD | 0.00 USD | 854,580.00 USD |
| `1D` | `3944.90` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 141,490.00 USD | 0.00 USD | 438,620.00 USD |
| `7D` | `3946.80` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 431,550.00 USD | 0.00 USD | 650,730.00 USD |
| `1D` | `3949.10` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 137,710.00 USD | 0.00 USD | 145,110.00 USD |
| `7D` | `3951.00` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 409,730.00 USD | 0.00 USD | 591,600.00 USD |
| `1D` | `3953.30` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 261,050.00 USD | 0.00 USD | 325,030.00 USD |
| `7D` | `3955.20` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 321,600.00 USD | 0.00 USD | 410,530.00 USD |
| `1D` | `3957.50` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 216,270.00 USD | 0.00 USD | 124,760.00 USD |
| `7D` | `3959.40` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 424,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3961.70` | 768,570.00 USD | 0.00 USD | 768,570.00 USD | 50,390.00 USD | 0.00 USD | 13,710.00 USD |
| `7D` | `3963.60` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 277,440.00 USD | 0.00 USD | 181,590.00 USD |
| `1D` | `3965.90` | 704,470.00 USD | 0.00 USD | 704,470.00 USD | 103,560.00 USD | 0.00 USD | 27,810.00 USD |
| `7D` | `3967.80` | 852,100.00 USD | 0.00 USD | 852,100.00 USD | 145,360.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `3970.10` | 573,090.00 USD | 0.00 USD | 573,090.00 USD | 58,250.00 USD | 0.00 USD | 73,850.00 USD |
| `7D` | `3972.00` | 603,940.00 USD | 0.00 USD | 603,940.00 USD | 97,260.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `3974.30` | 440,990.00 USD | 0.00 USD | 440,990.00 USD | 85,040.00 USD | 0.00 USD | 58,770.00 USD |
| `7D` | `3976.20` | 354,040.00 USD | 0.00 USD | 354,040.00 USD | 66,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3978.50` | 297,170.00 USD | 0.00 USD | 297,170.00 USD | 52,040.00 USD | 0.00 USD | 68,970.00 USD |
| `7D` | `3980.40` | 287,140.00 USD | 0.00 USD | 287,140.00 USD | 106,350.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `3982.70` | 176,160.00 USD | 0.00 USD | 176,160.00 USD | 38,340.00 USD | 0.00 USD | 110,090.00 USD |
| `7D` | `3984.60` | 64,940.00 USD | 0.00 USD | 64,940.00 USD | 30,500.00 USD | 0.00 USD | 34,430.00 USD |
| `1D` | `3986.90` | 27,730.00 USD | 0.00 USD | 27,730.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4006.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4007.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4064.40` | 24,220.00 USD | 24,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,220.00 USD |
| `7D` | `4068.60` | 458,640.00 USD | 458,640.00 USD | 0.00 USD | 115,900.00 USD | 0.00 USD | 318,510.00 USD |
| `7D` | `4072.80` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 385,550.00 USD | 0.00 USD | 801,820.00 USD |
| `7D` | `4077.00` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 609,590.00 USD | 0.00 USD | 1,480,000.00 USD |
| `7D` | `4081.20` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 628,480.00 USD | 0.00 USD | 706,940.00 USD |
| `7D` | `4085.40` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 188,370.00 USD | 0.00 USD | 539,830.00 USD |
| `7D` | `4089.60` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 122,280.00 USD | 0.00 USD | 305,050.00 USD |
| `1D` | `4091.90` | 114,250.00 USD | 114,250.00 USD | 0.00 USD | 15,550.00 USD | 0.00 USD | 98,700.00 USD |
| `7D` | `4093.80` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 354,750.00 USD | 0.00 USD | 379,560.00 USD |
| `1D` | `4096.10` | 246,800.00 USD | 246,800.00 USD | 0.00 USD | 22,890.00 USD | 0.00 USD | 109,660.00 USD |
| `7D` | `4098.00` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 462,870.00 USD | 0.00 USD | 439,630.00 USD |
| `1D` | `4100.30` | 422,010.00 USD | 422,010.00 USD | 0.00 USD | 47,700.00 USD | 0.00 USD | 127,510.00 USD |
| `7D` | `4102.20` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 364,620.00 USD | 0.00 USD | 926,810.00 USD |
| `1D` | `4104.50` | 973,110.00 USD | 973,110.00 USD | 0.00 USD | 157,780.00 USD | 0.00 USD | 393,320.00 USD |
| `7D` | `4106.40` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 454,550.00 USD | 0.00 USD | 830,540.00 USD |
| `1D` | `4108.70` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 97,040.00 USD | 0.00 USD | 198,090.00 USD |
| `7D` | `4110.60` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 491,660.00 USD | 0.00 USD | 541,140.00 USD |
| `1D` | `4112.90` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 271,420.00 USD | 0.00 USD | 282,080.00 USD |
| `7D` | `4114.80` | 12,060,000.00 USD | 12,060,000.00 USD | 0.00 USD | 234,080.00 USD | 0.00 USD | 346,150.00 USD |
| `1D` | `4117.10` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 216,570.00 USD | 0.00 USD | 199,230.00 USD |
| `7D` | `4119.00` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 403,440.00 USD | 0.00 USD | 286,230.00 USD |
| `1D` | `4121.30` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 98,330.00 USD | 0.00 USD | 23,580.00 USD |
| `7D` | `4123.20` | 13,180,000.00 USD | 13,180,000.00 USD | 0.00 USD | 379,850.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `4125.50` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 67,780.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `4127.40` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 217,200.00 USD | 0.00 USD | 217,580.00 USD |
| `1D` | `4129.70` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 71,380.00 USD | 0.00 USD | 51,280.00 USD |
| `7D` | `4131.60` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 74,180.00 USD | 0.00 USD | 107,640.00 USD |
| `1D` | `4133.90` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 53,620.00 USD | 0.00 USD | 83,520.00 USD |
| `7D` | `4135.80` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `4138.10` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 95,320.00 USD | 0.00 USD | 62,540.00 USD |
| `7D` | `4140.00` | 13,990,000.00 USD | 13,990,000.00 USD | 0.00 USD | 63,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4142.30` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 37,760.00 USD | 0.00 USD | 58,930.00 USD |
| `7D` | `4144.20` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 162,400.00 USD |
| `1D` | `4146.50` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 50,370.00 USD | 0.00 USD | 80,640.00 USD |
| `7D` | `4148.40` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 112,610.00 USD | 0.00 USD | 159,260.00 USD |
| `1D` | `4150.70` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 7,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4152.60` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 192,770.00 USD | 0.00 USD | 400,910.00 USD |
| `7D` | `4156.80` | 16,130,000.00 USD | 16,130,000.00 USD | 0.00 USD | 282,060.00 USD | 0.00 USD | 705,560.00 USD |
| `7D` | `4161.00` | 16,830,000.00 USD | 16,830,000.00 USD | 0.00 USD | 306,320.00 USD | 0.00 USD | 389,380.00 USD |
| `7D` | `4165.20` | 17,130,000.00 USD | 17,130,000.00 USD | 0.00 USD | 108,280.00 USD | 0.00 USD | 194,750.00 USD |
| `7D` | `4169.40` | 17,430,000.00 USD | 17,430,000.00 USD | 0.00 USD | 68,430.00 USD | 0.00 USD | 227,690.00 USD |
| `1D` | `4171.70` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 4,900.00 USD | 0.00 USD | 33,950.00 USD |
| `7D` | `4173.60` | 17,780,000.00 USD | 17,780,000.00 USD | 0.00 USD | 180,310.00 USD | 0.00 USD | 176,300.00 USD |
| `1D` | `4175.90` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 10,670.00 USD | 0.00 USD | 57,260.00 USD |
| `7D` | `4177.80` | 18,230,000.00 USD | 18,230,000.00 USD | 0.00 USD | 215,160.00 USD | 0.00 USD | 233,300.00 USD |
| `1D` | `4180.10` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 23,580.00 USD | 0.00 USD | 76,720.00 USD |
| `7D` | `4182.00` | 18,790,000.00 USD | 18,790,000.00 USD | 0.00 USD | 169,770.00 USD | 0.00 USD | 391,590.00 USD |
| `1D` | `4184.30` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 73,360.00 USD | 0.00 USD | 178,920.00 USD |
| `7D` | `4186.20` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 240,030.00 USD | 0.00 USD | 443,220.00 USD |
| `1D` | `4188.50` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 55,080.00 USD | 0.00 USD | 94,080.00 USD |
| `7D` | `4190.40` | 19,950,000.00 USD | 19,950,000.00 USD | 0.00 USD | 211,880.00 USD | 0.00 USD | 262,560.00 USD |
| `1D` | `4192.70` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 109,310.00 USD | 0.00 USD | 100,060.00 USD |
| `7D` | `4194.60` | 20,250,000.00 USD | 20,250,000.00 USD | 0.00 USD | 113,440.00 USD | 0.00 USD | 183,710.00 USD |
| `1D` | `4196.90` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 86,650.00 USD | 0.00 USD | 153,040.00 USD |
| `7D` | `4198.80` | 20,660,000.00 USD | 20,660,000.00 USD | 0.00 USD | 225,250.00 USD | 0.00 USD | 184,350.00 USD |
| `1D` | `4201.10` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 89,030.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4203.00` | 20,850,000.00 USD | 20,850,000.00 USD | 0.00 USD | 171,420.00 USD | 0.00 USD | 18,540.00 USD |
| `1D` | `4205.30` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4207.20` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 153,020.00 USD | 0.00 USD | 72,260.00 USD |
| `1D` | `4209.50` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 53,410.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `4211.40` | 21,170,000.00 USD | 21,170,000.00 USD | 0.00 USD | 47,590.00 USD | 0.00 USD | 51,400.00 USD |
| `1D` | `4213.70` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 31,370.00 USD | 0.00 USD | 42,200.00 USD |
| `7D` | `4215.60` | 21,290,000.00 USD | 21,290,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `4217.90` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 38,650.00 USD | 0.00 USD | 19,340.00 USD |
| `7D` | `4219.80` | 21,310,000.00 USD | 21,310,000.00 USD | 0.00 USD | 19,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4222.10` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 26,020.00 USD | 0.00 USD | 34,480.00 USD |
| `7D` | `4224.00` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 46,450.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `4226.30` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 19,170.00 USD | 0.00 USD | 55,050.00 USD |
| `7D` | `4228.20` | 21,440,000.00 USD | 21,440,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `1D` | `4230.50` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4379.40` | 21,450,000.00 USD | 21,450,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4383.60` | 21,450,000.00 USD | 21,450,000.00 USD | 0.00 USD | 6,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4387.80` | 21,530,000.00 USD | 21,530,000.00 USD | 0.00 USD | 36,240.00 USD | 0.00 USD | 45,030.00 USD |
| `7D` | `4392.00` | 21,710,000.00 USD | 21,710,000.00 USD | 0.00 USD | 58,490.00 USD | 0.00 USD | 116,070.00 USD |
| `7D` | `4396.20` | 22,000,000.00 USD | 22,000,000.00 USD | 0.00 USD | 80,970.00 USD | 0.00 USD | 210,210.00 USD |
| `7D` | `4400.40` | 22,220,000.00 USD | 22,220,000.00 USD | 0.00 USD | 102,130.00 USD | 0.00 USD | 112,920.00 USD |
| `7D` | `4404.60` | 22,310,000.00 USD | 22,310,000.00 USD | 0.00 USD | 37,920.00 USD | 0.00 USD | 53,740.00 USD |
| `7D` | `4408.80` | 22,420,000.00 USD | 22,420,000.00 USD | 0.00 USD | 16,390.00 USD | 0.00 USD | 94,890.00 USD |
| `1D` | `4411.10` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,510.00 USD |
| `7D` | `4413.00` | 22,510,000.00 USD | 22,510,000.00 USD | 0.00 USD | 41,120.00 USD | 0.00 USD | 48,680.00 USD |
| `1D` | `4415.30` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `4417.20` | 22,630,000.00 USD | 22,630,000.00 USD | 0.00 USD | 55,550.00 USD | 0.00 USD | 64,890.00 USD |
| `1D` | `4419.50` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 7,520.00 USD | 0.00 USD | 19,870.00 USD |
| `7D` | `4421.40` | 22,760,000.00 USD | 22,760,000.00 USD | 0.00 USD | 51,620.00 USD | 0.00 USD | 80,320.00 USD |
| `1D` | `4423.70` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 9,050.00 USD | 0.00 USD | 32,870.00 USD |
| `7D` | `4425.60` | 22,970,000.00 USD | 22,970,000.00 USD | 0.00 USD | 73,250.00 USD | 0.00 USD | 137,930.00 USD |
| `1D` | `4426.30` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 9,000.00 USD | 0.00 USD | 40,520.00 USD |
| `7D` | `4429.80` | 23,130,000.00 USD | 23,130,000.00 USD | 0.00 USD | 50,900.00 USD | 0.00 USD | 104,530.00 USD |
| `7D` | `4434.00` | 23,220,000.00 USD | 23,220,000.00 USD | 0.00 USD | 39,790.00 USD | 0.00 USD | 48,750.00 USD |
| `7D` | `4438.20` | 23,330,000.00 USD | 23,330,000.00 USD | 0.00 USD | 34,650.00 USD | 0.00 USD | 75,620.00 USD |
| `7D` | `4440.30` | 23,370,000.00 USD | 23,370,000.00 USD | 0.00 USD | 19,430.00 USD | 0.00 USD | 22,240.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `842.47M` | Total OI Tokens: `209,797.7 XAUT`
  * 1h OI Change: `-0.39%` | 4h OI Change: `-3.22%` | 24h OI Change: `+6.25%`
  * Exchange Breakdown: Binance=`62.36M` | Bybit=`144.43M` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `0.0000%` | Last 24h: `0.0000%` | Last 3d: `0.0000%` | Last 7d: `0.0000%`
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
| `15M` | `XAUT` | `56.01%` | `43.99%` | `1.27` | 6,210,000.00 USD |
| `15M` | `Binance` | `70.48%` | `29.52%` | `2.39` | 563,570.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `65.19%` | `34.81%` | `1.87` | 932,930.00 USD |
| `15M` | `KuCoin` | `2.46%` | `97.54%` | `0.03` | 32,920.00 USD |
| `15M` | `Gate` | `37.88%` | `62.12%` | `0.61` | 180,340.00 USD |
| `15M` | `Bitget` | `32.52%` | `67.48%` | `0.48` | 169,060.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `57.59%` | `42.41%` | `1.36` | 3,520,000.00 USD |
| `15M` | `Bitunix` | `67.16%` | `32.84%` | `2.05` | 163,720.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `33.56%` | `66.44%` | `0.51` | 550,270.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.71%` | `99.29%` | `0.01` | 40,690.00 USD |
| `15M` | `HTX` | `86.77%` | `13.23%` | `6.56` | 1,580.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.49%` | `53.51%` | `0.87` | 58,470.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `70.48%` | `29.52%` | `2.39` | 563,570.00 USD |
| `15M` | `Global Accounts` | `56.01%` | `43.99%` | `1.27` | 6,210,000.00 USD |
| `1H` | `XAUT` | `51.25%` | `48.75%` | `1.05` | 14,380,000.00 USD |
| `1H` | `Binance` | `55.2%` | `44.8%` | `1.23` | 1,070,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `52.93%` | `47.07%` | `1.12` | 1,630,000.00 USD |
| `1H` | `KuCoin` | `52.46%` | `47.54%` | `1.10` | 145,080.00 USD |
| `1H` | `Gate` | `46.15%` | `53.85%` | `0.86` | 389,580.00 USD |
| `1H` | `Bitget` | `34.81%` | `65.19%` | `0.53` | 477,770.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `52.93%` | `47.07%` | `1.12` | 8,700,000.00 USD |
| `1H` | `Bitunix` | `62.23%` | `37.77%` | `1.65` | 462,590.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.65%` | `53.35%` | `0.87` | 1,240,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.19%` | `99.81%` | `0.00` | 204,540.00 USD |
| `1H` | `HTX` | `89.01%` | `10.99%` | `8.10` | 6,130.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `30.98%` | `69.02%` | `0.45` | 50,400.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `55.2%` | `44.8%` | `1.23` | 1,070,000.00 USD |
| `1H` | `Global Accounts` | `51.25%` | `48.75%` | `1.05` | 14,380,000.00 USD |
| `4H` | `XAUT` | `48.26%` | `51.74%` | `0.93` | 85,760,000.00 USD |
| `4H` | `Binance` | `52.49%` | `47.51%` | `1.10` | 6,140,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `49.9%` | `50.1%` | `1.00` | 5,830,000.00 USD |
| `4H` | `KuCoin` | `51.49%` | `48.51%` | `1.06` | 539,110.00 USD |
| `4H` | `Gate` | `44.79%` | `55.21%` | `0.81` | 1,950,000.00 USD |
| `4H` | `Bitget` | `45.24%` | `54.76%` | `0.83` | 2,860,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `48.32%` | `51.68%` | `0.93` | 57,980,000.00 USD |
| `4H` | `Bitunix` | `54.71%` | `45.29%` | `1.21` | 2,340,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.92%` | `46.08%` | `1.17` | 6,010,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `7.54%` | `92.46%` | `0.08` | 1,890,000.00 USD |
| `4H` | `HTX` | `92.95%` | `7.05%` | `13.18` | 67,070.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.94%` | `54.06%` | `0.85` | 172,880.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `52.49%` | `47.51%` | `1.10` | 6,140,000.00 USD |
| `4H` | `Global Accounts` | `48.26%` | `51.74%` | `0.93` | 85,760,000.00 USD |


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
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_AUD (XAUAUD.pi) Metal Auction: ROTA | `5747.46` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 20,070.00 USD | 448,860.00 USD | **`ACCUMULATION`** |
| `15m` | -262,820.00 USD | 452,950.00 USD | **`ACCUMULATION`** |
| `30m` | -146,050.00 USD | 323,260.00 USD | **`ACCUMULATION`** |
| `1h` | -219,020.00 USD | 247,590.00 USD | **`ACCUMULATION`** |
| `2h` | -446,710.00 USD | -47,090.00 USD | **`DISTRIBUTION`** |
| `4h` | -675,760.00 USD | 219,310.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,240,000.00 USD | 224,770.00 USD | **`DISTRIBUTION`** |
| `8h` | 545,590.00 USD | 463,530.00 USD | **`ACCUMULATION`** |
| `12h` | 2,030,000.00 USD | 1,020,000.00 USD | **`ACCUMULATION`** |
| `24h` | -1,310,000.00 USD | 190,370.00 USD | **`DISTRIBUTION`** |
| `1w` | -85,040,000.00 USD | -21,060,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -177,780,000.00 USD | -85,190,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+20.07K` | 15m=`-262.82K` | 1h=`-219.02K` | 24h=`-1.31M`
* Futures Capital Netflows: 5m=`+448.86K` | 15m=`+452.95K` | 1h=`+247.59K` | 24h=`+190.37K`
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
  * Execution Entry: `26608.67` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26525.80` (Risk Distance: `82.87` pts)
  * +2.5R Take Profit: `26815.85`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26768.80` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26851.67` (Risk Distance: `82.87` pts)
  * +2.5R Take Profit: `26561.62`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26902.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
