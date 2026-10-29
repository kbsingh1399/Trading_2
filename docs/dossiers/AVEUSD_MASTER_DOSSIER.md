# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 22:30:50 IST` (`2026-10-29 17:00:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `133.16` | **Live Ask Quote**: `133.42` | **Mid Price**: `133.29`
- **Spread Points**: `26.00` | **Spread BPS**: `19.51 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `131.20` | VWAP Z-Score: `+1.02` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.9176` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `58.53` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `135.84` | Lower -3.00σ Band: `126.57`
  * Upper +2.51σ Band: `135.08` | Lower -2.51σ Band: `127.32`
  * Upper +2.01σ Band: `134.31` | Lower -2.01σ Band: `128.10`
  * Upper +2.00σ Band: `134.29` | Lower -2.00σ Band: `128.11`
  * Upper +1.28σ Band: `133.18` | Lower -1.28σ Band: `129.23`
  * Upper +1.00σ Band: `132.75` | Lower -1.00σ Band: `129.66`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`132.50` | EMA-20=`132.08` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`131.72` (Slope: `+0.0000`) | EMA-100=`132.03`
  * Institutional Anchors: EMA-144=`132.31` | EMA-200=`132.44` (Slope: `+0.0243`) | EMA-233=`132.56`
- **Range Boundaries**: 24H High=`138.47` | 24H Low=`128.25` | Weekly High=`138.47` | Weekly Low=`128.25`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `134.44` (Distance: `-0.84%`)
  * Point of Control (POC) = `132.88` (Distance: `+0.33%`)
  * Value Area Low (VAL) = `130.17` (Distance: `+2.41%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`135.85` | POC=`134.70` | VAL=`132.04`
  * Prior Day Extremes: PDH=`138.47` | PDL=`129.42` | PDC=`134.07`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`135.98` | Weekly POC=`134.76` | Weekly VAL=`131.69`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`135.37` | Low=`128.25`
  * London Session (08:00-16:00 UTC): High=`133.60` | Low=`129.16`
  * New York Session (13:00-21:00 UTC): High=`133.60` | Low=`130.09`
  * Initial Balance (First Hour): IB High=`131.85` | IB Low=`129.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `132.76` - `133.82`
  * Optimal Trade Entry (OTE 0.705): `133.56`
  * Structural Invalidation Anchor (0.786): `134.36`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `412` | `0x3ee5...4fab` | `LONG` | 5,769,802.31 USD | `43,303.83` | `77.35` | `133.13` | `114.26` | 2,420,112.27 USD | `+41.94%` | `10X Cross` |
| `768` | `0x0514...bdfe` | `SHORT` | 3,066,130.00 USD | `23,000.00` | `87.41` | `133.13` | `184.23` | -1,055,650.78 USD | `-34.43%` | `10X Cross` |
| `804` | `0x08c1...1135` | `LONG` | 2,910,762.79 USD | `21,836.18` | `80.89` | `133.13` | `92.24` | 1,144,428.44 USD | `+39.32%` | `10X Cross` |
| `1014` | `0x0996...0ba6` | `SHORT` | 2,266,780.00 USD | `17,000.00` | `107.97` | `133.13` | `196.58` | -431,206.70 USD | `-19.02%` | `3X Cross` |
| `1084` | `0x45d2...4029` | `SHORT` | 2,095,452.09 USD | `15,721.00` | `118.40` | `133.13` | `2252.96` | -234,060.91 USD | `-11.17%` | `10X Cross` |
| `1097` | `0xbfc7...80b4` | `SHORT` | 2,076,212.66 USD | `15,561.48` | `115.30` | `133.13` | `417.73` | -281,913.34 USD | `-13.58%` | `10X Cross` |
| `1190` | `0x6540...f7b7` | `LONG` | 1,931,600.15 USD | `14,488.45` | `145.90` | `133.13` | `91.06` | -182,255.59 USD | `-9.44%` | `5X Isolated` |
| `1256` | `0x07fd...689d` | `LONG` | 1,827,578.99 USD | `13,710.27` | `150.69` | `133.13` | `0.000000` | -238,475.69 USD | `-13.05%` | `10X Cross` |
| `1434` | `0xcac1...26b3` | `SHORT` | 1,600,200.00 USD | `12,000.00` | `125.37` | `133.13` | `782.23` | -95,759.14 USD | `-5.98%` | `10X Cross` |
| `1447` | `0xeadc...9d55` | `LONG` | 1,575,773.82 USD | `11,823.92` | `89.93` | `133.13` | `0.000000` | 512,417.41 USD | `+32.52%` | `10X Cross` |
| `1589` | `0x9df2...c665` | `SHORT` | 1,404,024.91 USD | `10,532.82` | `133.81` | `133.13` | `2865.11` | 5,424.73 USD | `+0.39%` | `10X Cross` |
| `1645` | `0x3dc9...54b0` | `SHORT` | 1,332,200.00 USD | `10,000.00` | `128.60` | `133.13` | `1872.65` | -46,178.17 USD | `-3.47%` | `10X Cross` |
| `1764` | `0x8af7...fa05` | `SHORT` | 1,217,711.55 USD | `9,133.75` | `131.49` | `133.13` | `2231.46` | -16,730.80 USD | `-1.37%` | `10X Cross` |
| `1950` | `0x72db...8bb6` | `LONG` | 1,066,400.00 USD | `8,000.00` | `180.99` | `133.13` | `0.000000` | -381,557.43 USD | `-35.78%` | `10X Cross` |
| `2007` | `0x12d2...f97f` | `LONG` | 1,023,186.81 USD | `7,675.82` | `143.31` | `133.13` | `0.000000` | -76,805.92 USD | `-7.51%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`133.91` (Vol: 206,000.00 USD, Dist: `+0.21%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.68%`)
  * 48H Horizon: Short MP=`133.91` (Vol: 206,000.00 USD, Dist: `+0.21%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.68%`)
  * 3D Horizon: Short MP=`133.91` (Vol: 206,000.00 USD, Dist: `+0.21%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.68%`)
  * 7D Horizon: Short MP=`139.76` (Vol: 320,000.00 USD, Dist: `+4.58%`) | Long MP=`127.18` (Vol: 326,000.00 USD, Dist: `--4.83%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `29.50` | 118.00 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 853.08 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 2,010.00 USD | 10,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 415.00 USD | 10,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 232.54 USD | 10,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 1,880.00 USD | 10,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 80,520.00 USD | 10,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 4,090.00 USD | 10,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 37,400.00 USD | 10,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 1,070.00 USD | 10,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 10,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 1,410.00 USD | 10,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,510.00 USD | 10,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 2,010.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 1,850.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,890.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 559.38 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 488.95 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 14,180.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,320.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 2,050.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 19,520.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 23,570.00 USD | 10,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 7,180.00 USD | 10,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 11,820.00 USD | 10,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,800.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,050.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 8,650.00 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 2,550.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 543.59 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 47,300.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 7,910.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 17,470.00 USD | 10,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 65,710.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 4,520.00 USD | 10,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 1,320,000.00 USD | 10,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 2,330,000.00 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 21,570.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 16,280.00 USD | 6,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,910.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 13,190.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 8,350.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 90,730.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 43,560.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 946.25 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 15,350.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 1,700.00 USD | 6,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 21,670.00 USD | 6,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 7,320.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 1,790.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 33,060.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 14,600.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 44,680.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 11,900.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 31,420.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 606,920.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 3,500.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 12,370.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 5,010,000.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 13,780.00 USD | 509,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 13,150.00 USD | 496,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 68,620.00 USD | 483,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 122,500.00 USD | 414,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 11,320.00 USD | 291,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 1,050.00 USD | 280,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 4,160.00 USD | 279,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 7,060.00 USD | 275,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 21,960.00 USD | 268,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `123.50` | 30,920.00 USD | 246,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `124.50` | 37,300.00 USD | 215,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `125.50` | 80,480.00 USD | 178,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 83,960.00 USD | 97,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `127.50` | 4,260.00 USD | 13,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `128.50` | 9,480.00 USD | 9,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 9,950.00 USD | 9,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 110.00 USD | 10,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 464.54 USD | 10,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 3,240.00 USD | 13,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 1,070.00 USD | 14,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 731.87 USD | 15,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 89,490.00 USD | 105,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 237.85 USD | 105,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 594,500.00 USD | 699,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 1,900.00 USD | 701,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,820.00 USD | 703,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.50` | 2,350.00 USD | 705,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 337.99 USD | 706,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,580.00 USD | 707,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 995.84 USD | 708,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 1,830.00 USD | 710,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 252.34 USD | 710,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 31,000.00 USD | 741,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 747,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,330.00 USD | 749,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 55,320.00 USD | 805,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 4,250,000.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 22,260.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 671,700.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 2,660.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 867.91 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.50` | 186.69 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 1,500.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 1,820.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 1,980.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,350,000.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 70,000.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `207.50` | 871.50 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `209.50` | 42,910.00 USD | 9,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 10,230.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `215.50` | 1,940.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `217.50` | 21,890.00 USD | 9,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 9,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `221.50` | 21,970.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `223.50` | 47,810.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `228.50` | 2,290.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `235.50` | 53,850.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `237.50` | 997.50 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `238.50` | 4,770.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `239.50` | 876.57 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 103.41 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 1,200.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `243.50` | 265.42 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `244.50` | 7,840.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `247.50` | 277.20 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `253.50` | 139.43 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `254.50` | 10,370.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `255.50` | 424.13 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `257.50` | 1,430.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `258.50` | 7,230.00 USD | 9,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `259.50` | 15,570.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `262.50` | 763.88 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `263.50` | 532.27 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `265.50` | 230.98 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `29.50` | 10,590,000.00 USD | 0.00 USD | 118.00 USD | `-77.84%` | `4.00` |
| `Live` | `Long` | `30.50` | 10,590,000.00 USD | 0.00 USD | 853.08 USD | `-77.09%` | `27.97` |
| `Live` | `Long` | `33.50` | 10,590,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.83%` | `60.00` |
| `Live` | `Long` | `36.50` | 10,580,000.00 USD | 0.00 USD | 415.00 USD | `-72.58%` | `11.37` |
| `Live` | `Long` | `38.50` | 10,580,000.00 USD | 0.00 USD | 232.54 USD | `-71.08%` | `6.04` |
| `Live` | `Long` | `40.50` | 10,580,000.00 USD | 0.00 USD | 1,880.00 USD | `-69.57%` | `46.30` |
| `Live` | `Long` | `43.50` | 10,580,000.00 USD | 0.00 USD | 80,520.00 USD | `-67.32%` | `1,850.93` |
| `Live` | `Long` | `44.50` | 10,500,000.00 USD | 0.00 USD | 4,090.00 USD | `-66.57%` | `91.87` |
| `Live` | `Long` | `45.50` | 10,500,000.00 USD | 0.00 USD | 37,400.00 USD | `-65.82%` | `822.04` |
| `Live` | `Long` | `51.50` | 10,460,000.00 USD | 0.00 USD | 1,070.00 USD | `-61.31%` | `20.74` |
| `Live` | `Long` | `54.50` | 10,460,000.00 USD | 0.00 USD | 805.51 USD | `-59.05%` | `14.78` |
| `Live` | `Long` | `55.50` | 10,460,000.00 USD | 0.00 USD | 1,410.00 USD | `-58.30%` | `25.36` |
| `Live` | `Long` | `56.50` | 10,460,000.00 USD | 0.00 USD | 1,510.00 USD | `-57.55%` | `26.66` |
| `Live` | `Long` | `57.50` | 10,450,000.00 USD | 0.00 USD | 2,010.00 USD | `-56.80%` | `35.00` |
| `Live` | `Long` | `58.50` | 10,450,000.00 USD | 0.00 USD | 1,610.00 USD | `-56.05%` | `27.49` |
| `Live` | `Long` | `59.50` | 10,450,000.00 USD | 0.00 USD | 1,850.00 USD | `-55.30%` | `31.14` |
| `Live` | `Long` | `60.50` | 10,450,000.00 USD | 0.00 USD | 1,890.00 USD | `-54.55%` | `31.27` |
| `Live` | `Long` | `61.50` | 10,450,000.00 USD | 0.00 USD | 168.51 USD | `-53.80%` | `2.74` |
| `Live` | `Long` | `62.50` | 10,450,000.00 USD | 0.00 USD | 559.38 USD | `-53.04%` | `8.95` |
| `Live` | `Long` | `63.50` | 10,450,000.00 USD | 0.00 USD | 488.95 USD | `-52.29%` | `7.70` |
| `Live` | `Long` | `66.50` | 10,450,000.00 USD | 0.00 USD | 14,180.00 USD | `-50.04%` | `213.26` |
| `Live` | `Long` | `67.50` | 10,430,000.00 USD | 0.00 USD | 24,320.00 USD | `-49.29%` | `360.30` |
| `Live` | `Long` | `68.50` | 10,410,000.00 USD | 0.00 USD | 2,050.00 USD | `-48.54%` | `29.96` |
| `Live` | `Long` | `69.50` | 10,410,000.00 USD | 0.00 USD | 19,520.00 USD | `-47.79%` | `280.90` |
| `Live` | `Long` | `70.50` | 10,390,000.00 USD | 0.00 USD | 23,570.00 USD | `-47.03%` | `334.33` |
| `Live` | `Long` | `71.50` | 10,360,000.00 USD | 0.00 USD | 7,180.00 USD | `-46.28%` | `100.46` |
| `Live` | `Long` | `73.50` | 10,360,000.00 USD | 0.00 USD | 11,820.00 USD | `-44.78%` | `160.80` |
| `Live` | `Long` | `74.50` | 10,340,000.00 USD | 0.00 USD | 1,800.00 USD | `-44.03%` | `24.13` |
| `Live` | `Long` | `75.50` | 10,340,000.00 USD | 0.00 USD | 1,050.00 USD | `-43.28%` | `13.87` |
| `Live` | `Long` | `77.50` | 10,340,000.00 USD | 0.00 USD | 9,050.00 USD | `-41.78%` | `116.79` |
| `Live` | `Long` | `78.50` | 10,330,000.00 USD | 0.00 USD | 4,310.00 USD | `-41.02%` | `54.87` |
| `Live` | `Long` | `79.50` | 10,330,000.00 USD | 0.00 USD | 8,650.00 USD | `-40.27%` | `108.76` |
| `Live` | `Long` | `82.50` | 10,320,000.00 USD | 0.00 USD | 2,550.00 USD | `-38.02%` | `30.96` |
| `Live` | `Long` | `83.50` | 10,320,000.00 USD | 0.00 USD | 543.59 USD | `-37.27%` | `6.51` |
| `Live` | `Long` | `85.50` | 10,320,000.00 USD | 0.00 USD | 47,300.00 USD | `-35.76%` | `553.17` |
| `Live` | `Long` | `86.50` | 10,270,000.00 USD | 0.00 USD | 7,910.00 USD | `-35.01%` | `91.41` |
| `Live` | `Long` | `87.50` | 10,260,000.00 USD | 0.00 USD | 17,470.00 USD | `-34.26%` | `199.64` |
| `Live` | `Long` | `88.50` | 10,240,000.00 USD | 0.00 USD | 65,710.00 USD | `-33.51%` | `742.43` |
| `Live` | `Long` | `89.50` | 10,180,000.00 USD | 0.00 USD | 4,520.00 USD | `-32.76%` | `50.55` |
| `Live` | `Long` | `90.50` | 10,170,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-32.01%` | `14,599.11` |
| `Live` | `Long` | `91.50` | 8,850,000.00 USD | 0.00 USD | 2,330,000.00 USD | `-31.26%` | `25,472.25` |
| `Live` | `Long` | `92.50` | 6,520,000.00 USD | 0.00 USD | 21,570.00 USD | `-30.51%` | `233.18` |
| `Live` | `Long` | `93.50` | 6,500,000.00 USD | 0.00 USD | 16,280.00 USD | `-29.75%` | `174.16` |
| `Live` | `Long` | `94.50` | 6,480,000.00 USD | 0.00 USD | 2,910.00 USD | `-29.00%` | `30.81` |
| `Live` | `Long` | `95.50` | 6,480,000.00 USD | 0.00 USD | 13,190.00 USD | `-28.25%` | `138.14` |
| `Live` | `Long` | `96.50` | 6,470,000.00 USD | 0.00 USD | 8,350.00 USD | `-27.50%` | `86.56` |
| `Live` | `Long` | `97.50` | 6,460,000.00 USD | 0.00 USD | 90,730.00 USD | `-26.75%` | `930.53` |
| `Live` | `Long` | `98.50` | 6,370,000.00 USD | 0.00 USD | 43,560.00 USD | `-26.00%` | `442.23` |
| `Live` | `Long` | `99.50` | 6,320,000.00 USD | 0.00 USD | 946.25 USD | `-25.25%` | `9.51` |
| `Live` | `Long` | `100.50` | 6,320,000.00 USD | 0.00 USD | 15,350.00 USD | `-24.50%` | `152.69` |
| `Live` | `Long` | `101.50` | 6,310,000.00 USD | 0.00 USD | 1,700.00 USD | `-23.74%` | `16.78` |
| `Live` | `Long` | `102.50` | 6,310,000.00 USD | 0.00 USD | 21,670.00 USD | `-22.99%` | `211.45` |
| `Live` | `Long` | `103.50` | 6,280,000.00 USD | 0.00 USD | 7,320.00 USD | `-22.24%` | `70.76` |
| `Live` | `Long` | `104.50` | 6,280,000.00 USD | 0.00 USD | 1,790.00 USD | `-21.49%` | `17.14` |
| `Live` | `Long` | `105.50` | 6,280,000.00 USD | 0.00 USD | 33,060.00 USD | `-20.74%` | `313.40` |
| `Live` | `Long` | `106.50` | 6,240,000.00 USD | 0.00 USD | 14,600.00 USD | `-19.99%` | `137.12` |
| `Live` | `Long` | `107.50` | 6,230,000.00 USD | 0.00 USD | 44,680.00 USD | `-19.24%` | `415.60` |
| `Live` | `Long` | `108.50` | 6,180,000.00 USD | 0.00 USD | 11,900.00 USD | `-18.49%` | `109.69` |
| `Live` | `Long` | `109.50` | 6,170,000.00 USD | 0.00 USD | 31,420.00 USD | `-17.73%` | `286.93` |
| `Live` | `Long` | `110.50` | 6,140,000.00 USD | 0.00 USD | 606,920.00 USD | `-16.98%` | `5,492.51` |
| `Live` | `Long` | `111.50` | 5,530,000.00 USD | 0.00 USD | 3,500.00 USD | `-16.23%` | `31.36` |
| `Live` | `Long` | `112.50` | 5,530,000.00 USD | 0.00 USD | 12,370.00 USD | `-15.48%` | `109.97` |
| `Live` | `Long` | `113.50` | 5,520,000.00 USD | 0.00 USD | 5,010,000.00 USD | `-14.73%` | `44,114.21` |
| `Live` | `Long` | `114.50` | 509,990.00 USD | 0.00 USD | 13,780.00 USD | `-13.98%` | `120.31` |
| `Live` | `Long` | `115.50` | 496,220.00 USD | 0.00 USD | 13,150.00 USD | `-13.23%` | `113.86` |
| `Live` | `Long` | `116.50` | 483,060.00 USD | 0.00 USD | 68,620.00 USD | `-12.48%` | `588.98` |
| `Live` | `Long` | `117.50` | 414,450.00 USD | 0.00 USD | 122,500.00 USD | `-11.72%` | `1,042.53` |
| `Live` | `Long` | `118.50` | 291,950.00 USD | 0.00 USD | 11,320.00 USD | `-10.97%` | `95.51` |
| `Live` | `Long` | `119.50` | 280,630.00 USD | 0.00 USD | 1,050.00 USD | `-10.22%` | `8.75` |
| `Live` | `Long` | `120.50` | 279,590.00 USD | 0.00 USD | 4,160.00 USD | `-9.47%` | `34.56` |
| `Live` | `Long` | `121.50` | 275,420.00 USD | 0.00 USD | 7,060.00 USD | `-8.72%` | `58.13` |
| `Live` | `Long` | `122.50` | 268,360.00 USD | 0.00 USD | 21,960.00 USD | `-7.97%` | `179.23` |
| `Live` | `Long` | `123.50` | 246,410.00 USD | 0.00 USD | 30,920.00 USD | `-7.22%` | `250.38` |
| `Live` | `Long` | `124.50` | 215,480.00 USD | 0.00 USD | 37,300.00 USD | `-6.46%` | `299.60` |
| `Live` | `Long` | `125.50` | 178,180.00 USD | 0.00 USD | 80,480.00 USD | `-5.71%` | `641.31` |
| `Live` | `Long` | `126.50` | 97,700.00 USD | 0.00 USD | 83,960.00 USD | `-4.96%` | `663.72` |
| `Live` | `Long` | `127.50` | 13,740.00 USD | 0.00 USD | 4,260.00 USD | `-4.21%` | `33.43` |
| `Live` | `Long` | `128.50` | 9,480.00 USD | 0.00 USD | 9,480.00 USD | `-3.46%` | `73.74` |
| `Live` | `Short` | `136.50` | 9,950.00 USD | 9,950.00 USD | 0.00 USD | `+2.55%` | `72.89` |
| `Live` | `Short` | `137.50` | 10,060.00 USD | 110.00 USD | 0.00 USD | `+3.30%` | `0.80` |
| `Live` | `Short` | `139.50` | 10,520.00 USD | 464.54 USD | 0.00 USD | `+4.80%` | `3.33` |
| `Live` | `Short` | `140.50` | 13,770.00 USD | 3,240.00 USD | 0.00 USD | `+5.56%` | `23.08` |
| `Live` | `Short` | `141.50` | 14,840.00 USD | 1,070.00 USD | 0.00 USD | `+6.31%` | `7.56` |
| `Live` | `Short` | `145.50` | 15,570.00 USD | 731.87 USD | 0.00 USD | `+9.31%` | `5.03` |
| `Live` | `Short` | `150.50` | 105,060.00 USD | 89,490.00 USD | 0.00 USD | `+13.07%` | `594.60` |
| `Live` | `Short` | `151.50` | 105,290.00 USD | 237.85 USD | 0.00 USD | `+13.82%` | `1.57` |
| `Live` | `Short` | `152.50` | 699,800.00 USD | 594,500.00 USD | 0.00 USD | `+14.57%` | `3,898.38` |
| `Live` | `Short` | `155.50` | 701,700.00 USD | 1,900.00 USD | 0.00 USD | `+16.83%` | `12.22` |
| `Live` | `Short` | `158.50` | 703,510.00 USD | 1,820.00 USD | 0.00 USD | `+19.08%` | `11.47` |
| `Live` | `Short` | `160.50` | 705,860.00 USD | 2,350.00 USD | 0.00 USD | `+20.58%` | `14.63` |
| `Live` | `Short` | `166.50` | 706,200.00 USD | 337.99 USD | 0.00 USD | `+25.09%` | `2.03` |
| `Live` | `Short` | `167.50` | 707,780.00 USD | 1,580.00 USD | 0.00 USD | `+25.84%` | `9.42` |
| `Live` | `Short` | `168.50` | 708,770.00 USD | 995.84 USD | 0.00 USD | `+26.59%` | `5.91` |
| `Live` | `Short` | `169.50` | 710,610.00 USD | 1,830.00 USD | 0.00 USD | `+27.34%` | `10.82` |
| `Live` | `Short` | `170.50` | 710,860.00 USD | 252.34 USD | 0.00 USD | `+28.09%` | `1.48` |
| `Live` | `Short` | `173.50` | 741,870.00 USD | 31,000.00 USD | 0.00 USD | `+30.35%` | `178.70` |
| `Live` | `Short` | `175.50` | 747,490.00 USD | 5,620.00 USD | 0.00 USD | `+31.85%` | `32.04` |
| `Live` | `Short` | `181.50` | 749,820.00 USD | 2,330.00 USD | 0.00 USD | `+36.36%` | `12.83` |
| `Live` | `Short` | `183.50` | 805,140.00 USD | 55,320.00 USD | 0.00 USD | `+37.86%` | `301.47` |
| `Live` | `Short` | `184.50` | 5,050,000.00 USD | 4,250,000.00 USD | 0.00 USD | `+38.61%` | `23,027.00` |
| `Live` | `Short` | `185.50` | 5,080,000.00 USD | 22,260.00 USD | 0.00 USD | `+39.36%` | `120.00` |
| `Live` | `Short` | `186.50` | 5,750,000.00 USD | 671,700.00 USD | 0.00 USD | `+40.11%` | `3,601.60` |
| `Live` | `Short` | `187.50` | 5,750,000.00 USD | 2,660.00 USD | 0.00 USD | `+40.87%` | `14.20` |
| `Live` | `Short` | `189.50` | 5,750,000.00 USD | 867.91 USD | 0.00 USD | `+42.37%` | `4.58` |
| `Live` | `Short` | `190.50` | 5,750,000.00 USD | 186.69 USD | 0.00 USD | `+43.12%` | `0.98` |
| `Live` | `Short` | `191.50` | 5,750,000.00 USD | 1,500.00 USD | 0.00 USD | `+43.87%` | `7.83` |
| `Live` | `Short` | `193.50` | 5,750,000.00 USD | 1,820.00 USD | 0.00 USD | `+45.37%` | `9.42` |
| `Live` | `Short` | `195.50` | 5,760,000.00 USD | 1,980.00 USD | 0.00 USD | `+46.88%` | `10.15` |
| `Live` | `Short` | `196.50` | 9,110,000.00 USD | 3,350,000.00 USD | 0.00 USD | `+47.63%` | `17,041.00` |
| `Live` | `Short` | `200.50` | 9,180,000.00 USD | 70,000.00 USD | 0.00 USD | `+50.63%` | `349.15` |
| `Live` | `Short` | `203.50` | 9,180,000.00 USD | 372.41 USD | 0.00 USD | `+52.89%` | `1.83` |
| `Live` | `Short` | `205.50` | 9,260,000.00 USD | 84,610.00 USD | 0.00 USD | `+54.39%` | `411.72` |
| `Live` | `Short` | `207.50` | 9,260,000.00 USD | 871.50 USD | 0.00 USD | `+55.89%` | `4.20` |
| `Live` | `Short` | `209.50` | 9,300,000.00 USD | 42,910.00 USD | 0.00 USD | `+57.39%` | `204.83` |
| `Live` | `Short` | `210.50` | 9,310,000.00 USD | 10,230.00 USD | 0.00 USD | `+58.15%` | `48.58` |
| `Live` | `Short` | `215.50` | 9,320,000.00 USD | 1,940.00 USD | 0.00 USD | `+61.90%` | `9.00` |
| `Live` | `Short` | `217.50` | 9,340,000.00 USD | 21,890.00 USD | 0.00 USD | `+63.40%` | `100.65` |
| `Live` | `Short` | `220.50` | 9,340,000.00 USD | 2,000.00 USD | 0.00 USD | `+65.66%` | `9.06` |
| `Live` | `Short` | `221.50` | 9,360,000.00 USD | 21,970.00 USD | 0.00 USD | `+66.41%` | `99.20` |
| `Live` | `Short` | `223.50` | 9,410,000.00 USD | 47,810.00 USD | 0.00 USD | `+67.91%` | `213.92` |
| `Live` | `Short` | `228.50` | 9,410,000.00 USD | 2,290.00 USD | 0.00 USD | `+71.67%` | `10.00` |
| `Live` | `Short` | `235.50` | 9,470,000.00 USD | 53,850.00 USD | 0.00 USD | `+76.93%` | `228.65` |
| `Live` | `Short` | `237.50` | 9,470,000.00 USD | 997.50 USD | 0.00 USD | `+78.43%` | `4.20` |
| `Live` | `Short` | `238.50` | 9,470,000.00 USD | 4,770.00 USD | 0.00 USD | `+79.18%` | `20.00` |
| `Live` | `Short` | `239.50` | 9,470,000.00 USD | 876.57 USD | 0.00 USD | `+79.93%` | `3.66` |
| `Live` | `Short` | `240.50` | 9,470,000.00 USD | 103.41 USD | 0.00 USD | `+80.68%` | `0.43` |
| `Live` | `Short` | `242.50` | 9,470,000.00 USD | 1,200.00 USD | 0.00 USD | `+82.19%` | `4.95` |
| `Live` | `Short` | `243.50` | 9,470,000.00 USD | 265.42 USD | 0.00 USD | `+82.94%` | `1.09` |
| `Live` | `Short` | `244.50` | 9,480,000.00 USD | 7,840.00 USD | 0.00 USD | `+83.69%` | `32.05` |
| `Live` | `Short` | `247.50` | 9,480,000.00 USD | 277.20 USD | 0.00 USD | `+85.94%` | `1.12` |
| `Live` | `Short` | `253.50` | 9,480,000.00 USD | 139.43 USD | 0.00 USD | `+90.45%` | `0.55` |
| `Live` | `Short` | `254.50` | 9,490,000.00 USD | 10,370.00 USD | 0.00 USD | `+91.20%` | `40.75` |
| `Live` | `Short` | `255.50` | 9,490,000.00 USD | 424.13 USD | 0.00 USD | `+91.95%` | `1.66` |
| `Live` | `Short` | `257.50` | 9,490,000.00 USD | 1,430.00 USD | 0.00 USD | `+93.46%` | `5.57` |
| `Live` | `Short` | `258.50` | 9,500,000.00 USD | 7,230.00 USD | 0.00 USD | `+94.21%` | `27.95` |
| `Live` | `Short` | `259.50` | 9,520,000.00 USD | 15,570.00 USD | 0.00 USD | `+94.96%` | `60.00` |
| `Live` | `Short` | `262.50` | 9,520,000.00 USD | 763.88 USD | 0.00 USD | `+97.21%` | `2.91` |
| `Live` | `Short` | `263.50` | 9,520,000.00 USD | 532.27 USD | 0.00 USD | `+97.96%` | `2.02` |
| `Live` | `Short` | `265.50` | 9,520,000.00 USD | 230.98 USD | 0.00 USD | `+99.47%` | `0.87` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `10.26K` | Last 24h: `24.24K` | Last 3d: `65.40K` | Last 7d: `98.48K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0057%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0058%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0091%` | **USDT Bitget** | `0.0027%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `133.00` | `133.31` | `133.00` | `133.87` | `132.88` | 1,394,606.15 USD | 574,363.62 USD | 820,242.53 USD | -245,878.91 USD | `-17.63%` | `23B / 21S` |
| `0:00 UTC` | `132.70` | `132.70` | `132.70` | `133.16` | `132.43` | 1,163,967.46 USD | 517,621.76 USD | 646,345.69 USD | -128,723.93 USD | `-11.06%` | `9B / 18S` |
| `5:00 UTC` | `132.72` | `132.82` | `132.72` | `133.16` | `132.50` | 689,662.85 USD | 385,039.87 USD | 304,622.98 USD | 80,416.90 USD | `+11.66%` | `16B / 11S` |
| `0:00 UTC` | `132.70` | `132.87` | `132.70` | `133.68` | `132.50` | 2,567,158.24 USD | 1,839,735.69 USD | 727,422.55 USD | 1,112,313.15 USD | `+43.33%` | `33B / 23S` |
| `5:00 UTC` | `133.03` | `132.93` | `133.03` | `133.25` | `132.59` | 568,772.83 USD | 230,823.42 USD | 337,949.41 USD | -107,125.99 USD | `-18.83%` | `7B / 30S` |
| `0:00 UTC` | `133.47` | `133.21` | `133.47` | `133.69` | `132.75` | 923,039.28 USD | 377,871.88 USD | 545,167.39 USD | -167,295.51 USD | `-18.12%` | `15B / 22S` |
| `5:00 UTC` | `132.88` | `132.95` | `132.88` | `133.53` | `132.61` | 809,326.65 USD | 463,393.77 USD | 345,932.87 USD | 117,460.90 USD | `+14.51%` | `19B / 20S` |
| `0:00 UTC` | `131.86` | `132.33` | `131.86` | `133.11` | `131.81` | 1,471,215.69 USD | 656,271.37 USD | 814,944.32 USD | -158,672.95 USD | `-10.79%` | `19B / 38S` |
| `5:00 UTC` | `132.53` | `132.73` | `132.53` | `133.53` | `132.00` | 1,448,788.15 USD | 848,288.39 USD | 600,499.76 USD | 247,788.63 USD | `+17.10%` | `53B / 21S` |
| `0:00 UTC` | `132.80` | `132.97` | `132.80` | `133.34` | `132.62` | 927,178.60 USD | 448,934.81 USD | 478,243.79 USD | -29,308.98 USD | `-3.16%` | `15B / 13S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:02` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `132.86` | 0.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.95` | 1,200.00 USD | 0.00 USD |
| `10-28 19:52` | `Volume 20K AAVE` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `130.77` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `130.77` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.5` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `130.77` | 3,200.00 USD | 0.00 USD |
| `10-28 19:42` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `131.45` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.5` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `131.08` | 3,500.00 USD | 0.00 USD |
| `10-28 19:06` | `Volume 20K AAVE` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.72` | 3,400.00 USD | 0.00 USD |
| `10-28 18:47` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `131.61` | 4,500.00 USD | 0.00 USD |
| `10-28 18:36` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.46` | 1,300.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.24` | 0.00 USD | 0.00 USD |
| `10-28 17:46` | `Volume 20K AAVE` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `133.63` | 5,700.00 USD | 0.00 USD |
| `10-28 17:44` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `133.04` | 0.00 USD | 0.00 USD |
| `10-28 16:41` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `134.42` | 0.00 USD | 0.00 USD |
| `10-28 15:53` | `Range 0.5` | `Divergence` | **`BULLISH`** | Drop without taker selling | `135.39` | 0.00 USD | 0.00 USD |
| `10-28 13:58` | `Volume 20K AAVE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `136.84` | 0.00 USD | 0.00 USD |
| `10-28 13:36` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `135.33` | 3,200.00 USD | 0.00 USD |
| `10-28 11:03` | `Range 0.5` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.16` | 3,800.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `134.87` | 0.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.5` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.37` | 1,400.00 USD | 0.00 USD |
| `10-28 09:16` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `136.00` | 1,200.00 USD | 0.00 USD |
| `10-28 09:02` | `Range 0.5` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `136.00` | 3,700.00 USD | 0.00 USD |
| `10-28 08:34` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.67` | 3,800.00 USD | 0.00 USD |
| `10-28 08:31` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.22` | 0.00 USD | 0.00 USD |
| `10-28 08:15` | `Volume 20K AAVE` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.66` | 0.00 USD | 0.00 USD |
| `10-28 08:09` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.15` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.5` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `135.87` | 3,900.00 USD | 0.00 USD |
| `10-28 07:26` | `Range 0.5` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `135.17` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 18,410.00 USD | 30,740.00 USD | **`ACCUMULATION`** |
| `15m` | -96,460.00 USD | 210,190.00 USD | **`ACCUMULATION`** |
| `30m` | -163,090.00 USD | 360,850.00 USD | **`ACCUMULATION`** |
| `1h` | -328,300.00 USD | -222,270.00 USD | **`DISTRIBUTION`** |
| `2h` | -76,050.00 USD | 951,720.00 USD | **`ACCUMULATION`** |
| `4h` | 116,270.00 USD | -507,120.00 USD | **`DISTRIBUTION`** |
| `6h` | 6,160.00 USD | 415,480.00 USD | **`ACCUMULATION`** |
| `8h` | 134,970.00 USD | 368,970.00 USD | **`ACCUMULATION`** |
| `12h` | 221,770.00 USD | 1,330,000.00 USD | **`ACCUMULATION`** |
| `24h` | -2,080,000.00 USD | 433,390.00 USD | **`DISTRIBUTION`** |
| `1w` | -23,580,000.00 USD | -43,260,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -114,030,000.00 USD | -106,860,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+18.41K` | 15m=`-96.46K` | 1h=`-328.30K` | 24h=`-2.08M`
* Futures Capital Netflows: 5m=`+30.74K` | 15m=`+210.19K` | 1h=`-222.27K` | 24h=`+433.39K`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `130.17` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `128.68` (Risk Distance: `1.49` pts)
  * +2.5R Take Profit: `133.90`
  * Mathematical Lot Sizing: **`6.70 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `134.44` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `135.93` (Risk Distance: `1.49` pts)
  * +2.5R Take Profit: `130.71`
  * Mathematical Lot Sizing: **`6.70 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`134.36`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
