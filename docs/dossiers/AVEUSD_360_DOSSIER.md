# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `126.38` | **Live Ask Quote**: `126.65` | **Mid Price**: `126.52`
- **Spread Points**: `27.00` | **Spread BPS**: `21.34 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `120.68` | VWAP Z-Score: `+1.71` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.39` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `60.53` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `129.32` | Lower -3.00σ Band: `112.04`
  * Upper +2.51σ Band: `127.91` | Lower -2.51σ Band: `113.45`
  * Upper +2.01σ Band: `126.47` | Lower -2.01σ Band: `114.89`
  * Upper +2.00σ Band: `126.44` | Lower -2.00σ Band: `114.92`
  * Upper +1.28σ Band: `124.36` | Lower -1.28σ Band: `116.99`
  * Upper +1.00σ Band: `123.56` | Lower -1.00σ Band: `117.80`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`124.78` | EMA-20=`123.61` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`124.77` (Slope: `+0.0000`) | EMA-100=`127.15`
  * Institutional Anchors: EMA-144=`128.34` | EMA-200=`129.32` (Slope: `-0.5001`) | EMA-233=`129.78`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`114.69` | Weekly High=`138.47` | Weekly Low=`114.69`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `123.98` (Distance: `+2.08%`)
  * Point of Control (POC) = `119.02` (Distance: `+6.34%`)
  * Value Area Low (VAL) = `117.73` (Distance: `+7.50%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.01` | Weekly POC=`135.06` | Weekly VAL=`130.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`126.87` | Low=`123.92`
  * New York Session (13:00-21:00 UTC): High=`127.27` | Low=`125.76`
  * Initial Balance (First Hour): IB High=`126.87` | IB Low=`123.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `126.01` - `127.02`
  * Optimal Trade Entry (OTE 0.705): `126.77`
  * Structural Invalidation Anchor (0.786): `127.53`

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
| --- | **`126.52`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `410` | `0x3ee5...4fab` | `LONG` | 5,487,677.86 USD | `43,303.83` | `77.35` | `126.66` | `72.48` | 2,137,987.82 USD | `+38.96%` | `10X Cross` |
| `718` | `0xecb6...2b00` | `SHORT` | 3,145,073.82 USD | `24,819.08` | `133.17` | `126.66` | `1232.24` | 160,147.31 USD | `+5.09%` | `10X Cross` |
| `782` | `0x0514...bdfe` | `SHORT` | 2,914,560.00 USD | `23,000.00` | `87.41` | `126.66` | `154.82` | -904,080.78 USD | `-31.02%` | `10X Cross` |
| `823` | `0x08c1...1135` | `LONG` | 2,769,045.99 USD | `21,836.18` | `80.89` | `126.66` | `87.09` | 1,002,711.63 USD | `+36.21%` | `10X Cross` |
| `1012` | `0x0996...0ba6` | `SHORT` | 2,155,260.00 USD | `17,000.00` | `107.97` | `126.66` | `196.59` | -319,686.70 USD | `-14.83%` | `3X Cross` |
| `1095` | `0x45d2...4029` | `SHORT` | 1,993,422.80 USD | `15,721.00` | `118.40` | `126.66` | `2643.72` | -132,031.62 USD | `-6.62%` | `10X Cross` |
| `1113` | `0xbfc7...80b4` | `SHORT` | 1,972,028.55 USD | `15,561.48` | `115.30` | `126.66` | `220.05` | -177,729.23 USD | `-9.01%` | `10X Cross` |
| `1143` | `0x6540...f7b7` | `LONG` | 1,933,924.44 USD | `15,251.77` | `144.40` | `126.66` | `76.39` | -268,370.53 USD | `-13.88%` | `5X Isolated` |
| `1214` | `0x07fd...689d` | `LONG` | 1,817,060.51 USD | `14,332.73` | `148.42` | `126.66` | `0.000000` | -310,221.76 USD | `-17.07%` | `10X Cross` |
| `1427` | `0xcac1...26b3` | `SHORT` | 1,521,324.00 USD | `12,000.00` | `125.37` | `126.66` | `827.92` | -16,883.14 USD | `-1.11%` | `10X Cross` |
| `1432` | `0x12d2...f97f` | `LONG` | 1,516,431.68 USD | `11,961.41` | `133.88` | `126.66` | `0.000000` | -84,972.76 USD | `-5.60%` | `10X Cross` |
| `1446` | `0xeadc...9d55` | `LONG` | 1,498,386.26 USD | `11,823.92` | `89.93` | `126.66` | `0.000000` | 435,029.85 USD | `+29.03%` | `10X Cross` |
| `1602` | `0x9df2...c665` | `SHORT` | 1,315,790.35 USD | `10,380.17` | `133.78` | `126.66` | `3004.88` | 72,918.92 USD | `+5.54%` | `10X Cross` |
| `1660` | `0x3dc9...54b0` | `SHORT` | 1,267,600.00 USD | `10,000.00` | `128.60` | `126.66` | `1740.91` | 18,421.83 USD | `+1.45%` | `10X Cross` |
| `1773` | `0x8af7...fa05` | `SHORT` | 1,158,159.50 USD | `9,133.75` | `131.49` | `126.66` | `2191.42` | 42,821.25 USD | `+3.70%` | `10X Cross` |
| `1965` | `0xbc5b...7fdc` | `LONG` | 1,018,513.75 USD | `8,033.71` | `136.30` | `126.66` | `18.25` | -76,515.45 USD | `-7.51%` | `10X Cross` |
| `1975` | `0x72db...8bb6` | `LONG` | 1,013,760.00 USD | `8,000.00` | `180.99` | `126.66` | `0.000000` | -434,197.43 USD | `-42.83%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`128.80` (Vol: 368,100.00 USD, Dist: `+1.87%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--7.85%`)
  * 48H Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+1.88%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--7.85%`)
  * 3D Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+1.88%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--7.85%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`116.46` (Vol: 253,400.00 USD, Dist: `--7.89%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `25.50` | 1,160.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 6,170.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 18,660.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 126,310.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 367.90 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 951.07 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 900.28 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 299.30 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 3,670.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 348.39 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 37,920.00 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.50` | 5,460.00 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 99.61 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 21,650.00 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 209.30 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 346.50 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 55,750.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 818.62 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 5,700.00 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,690.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 10,500.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 3,560.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 313.47 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 6,900.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 101.08 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,470.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 7,110.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 23,780.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 953.16 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 1,410.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 3,150,000.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 11,400.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 3,040.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 1,170,000.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 6,790.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 5,560.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 15,140.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 15,230.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 44,800.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 56,790.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,930,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 5,290.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 18,400.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 6,910.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,420.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 14,750.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 11,230.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 19,120.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 16,510.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 9,350.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 95,290.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 37,380.00 USD | 956,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 12,640.00 USD | 919,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 68,570.00 USD | 906,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 27,230.00 USD | 838,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 17,370.00 USD | 810,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 114,080.00 USD | 793,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 11,320.00 USD | 679,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 24,330.00 USD | 668,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 10,350.00 USD | 643,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 34,850.00 USD | 633,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 8,750.00 USD | 598,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 2,400.00 USD | 589,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 433,620.00 USD | 587,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 18,290.00 USD | 153,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 33,900.00 USD | 135,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 52,030.00 USD | 101,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,560.00 USD | 49,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 30,810.00 USD | 44,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 8,270.00 USD | 14,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 195.05 USD | 5,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 2,490.00 USD | 5,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 2,230.00 USD | 3,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 967.61 USD | 967.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 3,260.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 11,120.00 USD | 14,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 21,620.00 USD | 35,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 298.12 USD | 36,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 15,370.00 USD | 51,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 252.53 USD | 51,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 3,460.00 USD | 55,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,850.00 USD | 58,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 58,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 59,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 108,610.00 USD | 168,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 2,530.00 USD | 170,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 2,290.00 USD | 172,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 584,190.00 USD | 757,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.50` | 732.50 USD | 757,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 1,240.00 USD | 759,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 457.53 USD | 759,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 3,570,000.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 2,200.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.50` | 154.94 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.50` | 4,080.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 49,950.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 1,240.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 1,530.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 45,880.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 712.42 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 1,120.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 353,680.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,230.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 295.62 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 1,510.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 16,670.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.50` | 5,360.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 9,850.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `202.50` | 38,880.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 85,670.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `211.50` | 8,670.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `218.50` | 3,400,000.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `222.50` | 1,070,000.00 USD | 12,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `230.50` | 2,310.00 USD | 12,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 818,270.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `233.50` | 378.27 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `235.50` | 256.69 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 2,120.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `241.50` | 65,140.00 USD | 13,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `250.50` | 167,320.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `252.50` | 97,980.00 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `25.50` | 8,220,000.00 USD | 0.00 USD | 1,160.00 USD | `-79.89%` | `45.35` |
| `Live` | `Long` | `27.50` | 8,220,000.00 USD | 0.00 USD | 6,170.00 USD | `-78.31%` | `224.32` |
| `Live` | `Long` | `29.50` | 8,210,000.00 USD | 0.00 USD | 18,660.00 USD | `-76.73%` | `632.60` |
| `Live` | `Long` | `31.50` | 8,200,000.00 USD | 0.00 USD | 126,310.00 USD | `-75.15%` | `4,010.00` |
| `Live` | `Long` | `32.50` | 8,070,000.00 USD | 0.00 USD | 367.90 USD | `-74.37%` | `11.32` |
| `Live` | `Long` | `33.50` | 8,070,000.00 USD | 0.00 USD | 951.07 USD | `-73.58%` | `28.39` |
| `Live` | `Long` | `35.50` | 8,070,000.00 USD | 0.00 USD | 900.28 USD | `-72.00%` | `25.36` |
| `Live` | `Long` | `36.50` | 8,070,000.00 USD | 0.00 USD | 299.30 USD | `-71.21%` | `8.20` |
| `Live` | `Long` | `38.50` | 8,070,000.00 USD | 0.00 USD | 3,670.00 USD | `-69.63%` | `95.27` |
| `Live` | `Long` | `39.50` | 8,060,000.00 USD | 0.00 USD | 348.39 USD | `-68.84%` | `8.82` |
| `Live` | `Long` | `40.50` | 8,060,000.00 USD | 0.00 USD | 37,920.00 USD | `-68.05%` | `936.21` |
| `Live` | `Long` | `42.50` | 8,020,000.00 USD | 0.00 USD | 5,460.00 USD | `-66.48%` | `128.40` |
| `Live` | `Long` | `43.50` | 8,020,000.00 USD | 0.00 USD | 99.61 USD | `-65.69%` | `2.29` |
| `Live` | `Long` | `44.50` | 8,020,000.00 USD | 0.00 USD | 21,650.00 USD | `-64.90%` | `486.56` |
| `Live` | `Long` | `45.50` | 8,000,000.00 USD | 0.00 USD | 209.30 USD | `-64.11%` | `4.60` |
| `Live` | `Long` | `49.50` | 8,000,000.00 USD | 0.00 USD | 346.50 USD | `-60.96%` | `7.00` |
| `Live` | `Long` | `51.50` | 8,000,000.00 USD | 0.00 USD | 55,750.00 USD | `-59.38%` | `1,082.57` |
| `Live` | `Long` | `54.50` | 7,940,000.00 USD | 0.00 USD | 805.51 USD | `-57.01%` | `14.78` |
| `Live` | `Long` | `55.50` | 7,940,000.00 USD | 0.00 USD | 818.62 USD | `-56.22%` | `14.75` |
| `Live` | `Long` | `56.50` | 7,940,000.00 USD | 0.00 USD | 5,700.00 USD | `-55.43%` | `100.95` |
| `Live` | `Long` | `58.50` | 7,930,000.00 USD | 0.00 USD | 1,610.00 USD | `-53.86%` | `27.49` |
| `Live` | `Long` | `60.50` | 7,930,000.00 USD | 0.00 USD | 1,690.00 USD | `-52.28%` | `27.87` |
| `Live` | `Long` | `61.50` | 7,930,000.00 USD | 0.00 USD | 168.51 USD | `-51.49%` | `2.74` |
| `Live` | `Long` | `62.50` | 7,930,000.00 USD | 0.00 USD | 10,500.00 USD | `-50.70%` | `168.03` |
| `Live` | `Long` | `63.50` | 7,920,000.00 USD | 0.00 USD | 3,560.00 USD | `-49.91%` | `56.00` |
| `Live` | `Long` | `64.50` | 7,920,000.00 USD | 0.00 USD | 313.47 USD | `-49.12%` | `4.86` |
| `Live` | `Long` | `65.50` | 7,920,000.00 USD | 0.00 USD | 6,900.00 USD | `-48.34%` | `105.39` |
| `Live` | `Long` | `66.50` | 7,910,000.00 USD | 0.00 USD | 101.08 USD | `-47.55%` | `1.52` |
| `Live` | `Long` | `67.50` | 7,910,000.00 USD | 0.00 USD | 24,470.00 USD | `-46.76%` | `362.50` |
| `Live` | `Long` | `68.50` | 7,880,000.00 USD | 0.00 USD | 7,110.00 USD | `-45.97%` | `103.75` |
| `Live` | `Long` | `69.50` | 7,880,000.00 USD | 0.00 USD | 23,780.00 USD | `-45.18%` | `342.17` |
| `Live` | `Long` | `70.50` | 7,850,000.00 USD | 0.00 USD | 953.16 USD | `-44.39%` | `13.52` |
| `Live` | `Long` | `71.50` | 7,850,000.00 USD | 0.00 USD | 1,410.00 USD | `-43.60%` | `19.76` |
| `Live` | `Long` | `72.50` | 7,850,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-42.81%` | `43,411.83` |
| `Live` | `Long` | `73.50` | 4,700,000.00 USD | 0.00 USD | 11,400.00 USD | `-42.03%` | `155.11` |
| `Live` | `Long` | `74.50` | 4,690,000.00 USD | 0.00 USD | 1,060.00 USD | `-41.24%` | `14.20` |
| `Live` | `Long` | `75.50` | 4,690,000.00 USD | 0.00 USD | 3,040.00 USD | `-40.45%` | `40.23` |
| `Live` | `Long` | `76.50` | 4,690,000.00 USD | 0.00 USD | 1,170,000.00 USD | `-39.66%` | `15,255.85` |
| `Live` | `Long` | `77.50` | 3,520,000.00 USD | 0.00 USD | 9,050.00 USD | `-38.87%` | `116.79` |
| `Live` | `Long` | `78.50` | 3,510,000.00 USD | 0.00 USD | 4,310.00 USD | `-38.08%` | `54.87` |
| `Live` | `Long` | `79.50` | 3,510,000.00 USD | 0.00 USD | 6,790.00 USD | `-37.29%` | `85.43` |
| `Live` | `Long` | `80.50` | 3,500,000.00 USD | 0.00 USD | 5,560.00 USD | `-36.50%` | `69.07` |
| `Live` | `Long` | `82.50` | 3,500,000.00 USD | 0.00 USD | 15,140.00 USD | `-34.93%` | `183.51` |
| `Live` | `Long` | `83.50` | 3,480,000.00 USD | 0.00 USD | 15,230.00 USD | `-34.14%` | `182.44` |
| `Live` | `Long` | `85.50` | 3,470,000.00 USD | 0.00 USD | 44,800.00 USD | `-32.56%` | `524.00` |
| `Live` | `Long` | `86.50` | 3,420,000.00 USD | 0.00 USD | 56,790.00 USD | `-31.77%` | `656.48` |
| `Live` | `Long` | `87.50` | 3,360,000.00 USD | 0.00 USD | 1,930,000.00 USD | `-30.98%` | `22,090.96` |
| `Live` | `Long` | `88.50` | 1,430,000.00 USD | 0.00 USD | 5,290.00 USD | `-30.19%` | `59.81` |
| `Live` | `Long` | `89.50` | 1,430,000.00 USD | 0.00 USD | 18,400.00 USD | `-29.41%` | `205.58` |
| `Live` | `Long` | `90.50` | 1,410,000.00 USD | 0.00 USD | 6,910.00 USD | `-28.62%` | `76.33` |
| `Live` | `Long` | `91.50` | 1,400,000.00 USD | 0.00 USD | 277,420.00 USD | `-27.83%` | `3,031.94` |
| `Live` | `Long` | `92.50` | 1,120,000.00 USD | 0.00 USD | 14,750.00 USD | `-27.04%` | `159.47` |
| `Live` | `Long` | `93.50` | 1,110,000.00 USD | 0.00 USD | 11,230.00 USD | `-26.25%` | `120.06` |
| `Live` | `Long` | `94.50` | 1,100,000.00 USD | 0.00 USD | 19,120.00 USD | `-25.46%` | `202.34` |
| `Live` | `Long` | `95.50` | 1,080,000.00 USD | 0.00 USD | 16,510.00 USD | `-24.67%` | `172.89` |
| `Live` | `Long` | `96.50` | 1,060,000.00 USD | 0.00 USD | 9,350.00 USD | `-23.88%` | `96.87` |
| `Live` | `Long` | `97.50` | 1,050,000.00 USD | 0.00 USD | 95,290.00 USD | `-23.10%` | `977.30` |
| `Live` | `Long` | `98.50` | 956,620.00 USD | 0.00 USD | 37,380.00 USD | `-22.31%` | `379.53` |
| `Live` | `Long` | `99.50` | 919,240.00 USD | 0.00 USD | 12,640.00 USD | `-21.52%` | `126.99` |
| `Live` | `Long` | `100.50` | 906,600.00 USD | 0.00 USD | 68,570.00 USD | `-20.73%` | `682.28` |
| `Live` | `Long` | `101.50` | 838,030.00 USD | 0.00 USD | 27,230.00 USD | `-19.94%` | `268.27` |
| `Live` | `Long` | `102.50` | 810,810.00 USD | 0.00 USD | 17,370.00 USD | `-19.15%` | `169.44` |
| `Live` | `Long` | `103.50` | 793,440.00 USD | 0.00 USD | 114,080.00 USD | `-18.36%` | `1,102.27` |
| `Live` | `Long` | `104.50` | 679,350.00 USD | 0.00 USD | 11,320.00 USD | `-17.57%` | `108.29` |
| `Live` | `Long` | `105.50` | 668,040.00 USD | 0.00 USD | 24,330.00 USD | `-16.78%` | `230.59` |
| `Live` | `Long` | `106.50` | 643,710.00 USD | 0.00 USD | 10,350.00 USD | `-16.00%` | `97.16` |
| `Live` | `Long` | `107.50` | 633,360.00 USD | 0.00 USD | 34,850.00 USD | `-15.21%` | `324.23` |
| `Live` | `Long` | `108.50` | 598,510.00 USD | 0.00 USD | 8,750.00 USD | `-14.42%` | `80.63` |
| `Live` | `Long` | `109.50` | 589,760.00 USD | 0.00 USD | 2,400.00 USD | `-13.63%` | `21.88` |
| `Live` | `Long` | `110.50` | 587,360.00 USD | 0.00 USD | 433,620.00 USD | `-12.84%` | `3,924.17` |
| `Live` | `Long` | `111.50` | 153,740.00 USD | 0.00 USD | 18,290.00 USD | `-12.05%` | `164.08` |
| `Live` | `Long` | `112.50` | 135,450.00 USD | 0.00 USD | 33,900.00 USD | `-11.26%` | `301.33` |
| `Live` | `Long` | `113.50` | 101,550.00 USD | 0.00 USD | 52,030.00 USD | `-10.47%` | `458.42` |
| `Live` | `Long` | `114.50` | 49,520.00 USD | 0.00 USD | 4,560.00 USD | `-9.69%` | `39.82` |
| `Live` | `Long` | `115.50` | 44,960.00 USD | 0.00 USD | 30,810.00 USD | `-8.90%` | `266.74` |
| `Live` | `Long` | `116.50` | 14,150.00 USD | 0.00 USD | 8,270.00 USD | `-8.11%` | `71.00` |
| `Live` | `Long` | `117.50` | 5,880.00 USD | 0.00 USD | 195.05 USD | `-7.32%` | `1.66` |
| `Live` | `Long` | `118.50` | 5,680.00 USD | 0.00 USD | 2,490.00 USD | `-6.53%` | `20.99` |
| `Live` | `Long` | `119.50` | 3,200.00 USD | 0.00 USD | 2,230.00 USD | `-5.74%` | `18.64` |
| `Live` | `Long` | `120.50` | 967.61 USD | 0.00 USD | 967.61 USD | `-4.95%` | `8.03` |
| `Live` | `Short` | `129.50` | 3,260.00 USD | 3,260.00 USD | 0.00 USD | `+2.15%` | `25.14` |
| `Live` | `Short` | `130.50` | 14,380.00 USD | 11,120.00 USD | 0.00 USD | `+2.93%` | `85.21` |
| `Live` | `Short` | `131.50` | 35,990.00 USD | 21,620.00 USD | 0.00 USD | `+3.72%` | `164.38` |
| `Live` | `Short` | `132.50` | 36,290.00 USD | 298.12 USD | 0.00 USD | `+4.51%` | `2.25` |
| `Live` | `Short` | `133.50` | 51,660.00 USD | 15,370.00 USD | 0.00 USD | `+5.30%` | `115.15` |
| `Live` | `Short` | `136.50` | 51,910.00 USD | 252.53 USD | 0.00 USD | `+7.67%` | `1.85` |
| `Live` | `Short` | `137.50` | 55,380.00 USD | 3,460.00 USD | 0.00 USD | `+8.46%` | `25.19` |
| `Live` | `Short` | `138.50` | 58,230.00 USD | 2,850.00 USD | 0.00 USD | `+9.24%` | `20.56` |
| `Live` | `Short` | `139.50` | 58,330.00 USD | 100.44 USD | 0.00 USD | `+10.03%` | `0.72` |
| `Live` | `Short` | `140.50` | 59,480.00 USD | 1,150.00 USD | 0.00 USD | `+10.82%` | `8.19` |
| `Live` | `Short` | `141.50` | 168,080.00 USD | 108,610.00 USD | 0.00 USD | `+11.61%` | `767.54` |
| `Live` | `Short` | `142.50` | 170,610.00 USD | 2,530.00 USD | 0.00 USD | `+12.40%` | `17.73` |
| `Live` | `Short` | `143.50` | 172,900.00 USD | 2,290.00 USD | 0.00 USD | `+13.19%` | `15.94` |
| `Live` | `Short` | `144.50` | 757,090.00 USD | 584,190.00 USD | 0.00 USD | `+13.98%` | `4,042.83` |
| `Live` | `Short` | `146.50` | 757,820.00 USD | 732.50 USD | 0.00 USD | `+15.55%` | `5.00` |
| `Live` | `Short` | `150.50` | 759,060.00 USD | 1,240.00 USD | 0.00 USD | `+18.71%` | `8.23` |
| `Live` | `Short` | `151.50` | 759,520.00 USD | 457.53 USD | 0.00 USD | `+19.50%` | `3.02` |
| `Live` | `Short` | `154.50` | 4,330,000.00 USD | 3,570,000.00 USD | 0.00 USD | `+21.86%` | `23,079.66` |
| `Live` | `Short` | `155.50` | 4,330,000.00 USD | 2,200.00 USD | 0.00 USD | `+22.65%` | `14.13` |
| `Live` | `Short` | `156.50` | 4,330,000.00 USD | 154.94 USD | 0.00 USD | `+23.44%` | `0.99` |
| `Live` | `Short` | `157.50` | 4,330,000.00 USD | 4,080.00 USD | 0.00 USD | `+24.23%` | `25.90` |
| `Live` | `Short` | `158.50` | 4,330,000.00 USD | 1,480.00 USD | 0.00 USD | `+25.02%` | `9.36` |
| `Live` | `Short` | `166.50` | 4,380,000.00 USD | 49,950.00 USD | 0.00 USD | `+31.33%` | `300.00` |
| `Live` | `Short` | `168.50` | 4,380,000.00 USD | 1,240.00 USD | 0.00 USD | `+32.91%` | `7.37` |
| `Live` | `Short` | `170.50` | 4,390,000.00 USD | 1,530.00 USD | 0.00 USD | `+34.48%` | `9.00` |
| `Live` | `Short` | `171.50` | 4,430,000.00 USD | 45,880.00 USD | 0.00 USD | `+35.27%` | `267.54` |
| `Live` | `Short` | `172.50` | 4,430,000.00 USD | 712.42 USD | 0.00 USD | `+36.06%` | `4.13` |
| `Live` | `Short` | `175.50` | 4,440,000.00 USD | 5,620.00 USD | 0.00 USD | `+38.43%` | `32.04` |
| `Live` | `Short` | `180.50` | 4,440,000.00 USD | 1,120.00 USD | 0.00 USD | `+42.37%` | `6.20` |
| `Live` | `Short` | `181.50` | 4,440,000.00 USD | 2,170.00 USD | 0.00 USD | `+43.16%` | `11.93` |
| `Live` | `Short` | `183.50` | 4,800,000.00 USD | 353,680.00 USD | 0.00 USD | `+44.74%` | `1,927.41` |
| `Live` | `Short` | `187.50` | 4,800,000.00 USD | 4,230.00 USD | 0.00 USD | `+47.89%` | `22.56` |
| `Live` | `Short` | `189.50` | 4,800,000.00 USD | 295.62 USD | 0.00 USD | `+49.47%` | `1.56` |
| `Live` | `Short` | `194.50` | 4,800,000.00 USD | 1,510.00 USD | 0.00 USD | `+53.42%` | `7.76` |
| `Live` | `Short` | `195.50` | 4,820,000.00 USD | 16,670.00 USD | 0.00 USD | `+54.20%` | `85.28` |
| `Live` | `Short` | `196.50` | 8,160,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+54.99%` | `17,003.34` |
| `Live` | `Short` | `198.50` | 8,160,000.00 USD | 5,360.00 USD | 0.00 USD | `+56.57%` | `27.00` |
| `Live` | `Short` | `200.50` | 8,170,000.00 USD | 9,850.00 USD | 0.00 USD | `+58.15%` | `49.15` |
| `Live` | `Short` | `202.50` | 8,210,000.00 USD | 38,880.00 USD | 0.00 USD | `+59.73%` | `192.00` |
| `Live` | `Short` | `203.50` | 8,210,000.00 USD | 372.41 USD | 0.00 USD | `+60.51%` | `1.83` |
| `Live` | `Short` | `205.50` | 8,300,000.00 USD | 85,670.00 USD | 0.00 USD | `+62.09%` | `416.87` |
| `Live` | `Short` | `210.50` | 8,300,000.00 USD | 151.56 USD | 0.00 USD | `+66.04%` | `0.72` |
| `Live` | `Short` | `211.50` | 8,310,000.00 USD | 8,670.00 USD | 0.00 USD | `+66.82%` | `41.00` |
| `Live` | `Short` | `218.50` | 11,710,000.00 USD | 3,400,000.00 USD | 0.00 USD | `+72.35%` | `15,561.48` |
| `Live` | `Short` | `220.50` | 11,710,000.00 USD | 2,000.00 USD | 0.00 USD | `+73.92%` | `9.06` |
| `Live` | `Short` | `222.50` | 12,780,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+75.50%` | `4,808.67` |
| `Live` | `Short` | `230.50` | 12,780,000.00 USD | 2,310.00 USD | 0.00 USD | `+81.81%` | `10.00` |
| `Live` | `Short` | `232.50` | 13,600,000.00 USD | 818,270.00 USD | 0.00 USD | `+83.39%` | `3,519.45` |
| `Live` | `Short` | `233.50` | 13,600,000.00 USD | 378.27 USD | 0.00 USD | `+84.18%` | `1.62` |
| `Live` | `Short` | `235.50` | 13,600,000.00 USD | 256.69 USD | 0.00 USD | `+85.75%` | `1.09` |
| `Live` | `Short` | `240.50` | 13,600,000.00 USD | 2,120.00 USD | 0.00 USD | `+89.70%` | `8.82` |
| `Live` | `Short` | `241.50` | 13,670,000.00 USD | 65,140.00 USD | 0.00 USD | `+90.49%` | `269.73` |
| `Live` | `Short` | `250.50` | 13,840,000.00 USD | 167,320.00 USD | 0.00 USD | `+97.59%` | `667.95` |
| `Live` | `Short` | `252.50` | 13,930,000.00 USD | 97,980.00 USD | 0.00 USD | `+99.16%` | `388.04` |

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
  * Current Rate: `-10.56K` | Last 24h: `15.72K` | Last 3d: `55.76K` | Last 7d: `119.40K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0018%` | **USDT OKX** | `-0.0005%` |
| **USDT Bybit** | `-0.0219%` | **USDT KuCoin** | `-0.0174%` |
| **USDT MEXC** | `0.0019%` | **USDT BingX** | `0.0093%` |
| **USDT Gate** | `-0.0100%` | **USDT Bitget** | `0.0090%` |
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
| `5:00 UTC` | `124.25` | `124.03` | `124.25` | `124.45` | `123.66` | 1,500,731.33 USD | 697,230.09 USD | 803,501.24 USD | -106,271.15 USD | `-7.08%` | `8B / 7S` |
| `0:00 UTC` | `123.52` | `123.26` | `123.52` | `123.91` | `122.69` | 2,022,565.96 USD | 1,006,456.45 USD | 1,016,109.51 USD | -9,653.06 USD | `-0.48%` | `17B / 14S` |
| `5:00 UTC` | `123.70` | `123.95` | `123.70` | `124.31` | `123.44` | 1,609,872.44 USD | 851,411.54 USD | 758,460.89 USD | 92,950.65 USD | `+5.77%` | `11B / 9S` |
| `0:00 UTC` | `124.56` | `124.51` | `124.56` | `124.78` | `124.06` | 1,620,060.54 USD | 772,586.85 USD | 847,473.69 USD | -74,886.85 USD | `-4.62%` | `14B / 15S` |
| `5:00 UTC` | `124.41` | `124.50` | `124.41` | `124.75` | `124.13` | 1,180,503.64 USD | 644,282.82 USD | 536,220.82 USD | 108,062.00 USD | `+9.15%` | `7B / 8S` |
| `0:00 UTC` | `124.66` | `125.75` | `124.66` | `127.18` | `124.34` | 2,947,595.56 USD | 1,739,301.93 USD | 1,208,293.63 USD | 531,008.30 USD | `+18.01%` | `27B / 7S` |
| `5:00 UTC` | `126.50` | `126.66` | `126.50` | `127.48` | `126.16` | 2,126,180.43 USD | 1,170,588.46 USD | 955,591.97 USD | 214,996.49 USD | `+10.11%` | `24B / 7S` |
| `0:00 UTC` | `126.53` | `126.53` | `126.53` | `126.84` | `126.18` | 1,565,984.43 USD | 839,070.01 USD | 726,914.42 USD | 112,155.59 USD | `+7.16%` | `10B / 13S` |
| `5:00 UTC` | `125.81` | `126.13` | `125.81` | `126.84` | `125.66` | 1,758,403.62 USD | 807,545.85 USD | 950,857.77 USD | -143,311.92 USD | `-8.15%` | `11B / 29S` |
| `0:00 UTC` | `126.20` | `126.30` | `126.20` | `126.73` | `125.81` | 1,264,660.39 USD | 716,055.24 USD | 548,605.15 USD | 167,450.09 USD | `+13.24%` | `18B / 17S` |

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
| `5m` | -89,800.00 USD | 3,300.00 USD | **`DISTRIBUTION`** |
| `15m` | 99,210.00 USD | 206,560.00 USD | **`ACCUMULATION`** |
| `30m` | -7,650.00 USD | -25,780.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,770.00 USD | 798,640.00 USD | **`ACCUMULATION`** |
| `2h` | 591,180.00 USD | 3,350,000.00 USD | **`ACCUMULATION`** |
| `4h` | 809,770.00 USD | 4,630,000.00 USD | **`ACCUMULATION`** |
| `6h` | -610,110.00 USD | 2,460,000.00 USD | **`ACCUMULATION`** |
| `8h` | -739,970.00 USD | -2,280,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,560,000.00 USD | -6,970,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -6,590,000.00 USD | -7,370,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -28,360,000.00 USD | -47,390,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -116,430,000.00 USD | -96,810,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-89.80K` | 15m=`+99.21K` | 1h=`-1.77K` | 24h=`-6.59M`
* Futures Capital Netflows: 5m=`+3.30K` | 15m=`+206.56K` | 1h=`+798.64K` | 24h=`-7.37M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `117.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `115.66` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `122.90`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `123.98` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `126.05` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `118.81`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`127.53`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
