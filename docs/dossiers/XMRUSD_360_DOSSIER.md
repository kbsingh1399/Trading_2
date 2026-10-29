# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XMRUSD
**Canonical Key**: `XMRUSD` | **Broker Instrument**: `XMRUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:36:03 IST` (`2026-10-29 20:06:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `600.62` | **Live Ask Quote**: `600.98` | **Mid Price**: `600.80`
- **Spread Points**: `36.00` | **Spread BPS**: `5.99 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `599.07` | VWAP Z-Score: `+0.32` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.97` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.97` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `619.24` | Lower -3.00σ Band: `578.90`
  * Upper +2.51σ Band: `615.94` | Lower -2.51σ Band: `582.20`
  * Upper +2.01σ Band: `612.58` | Lower -2.01σ Band: `585.56`
  * Upper +2.00σ Band: `612.51` | Lower -2.00σ Band: `585.63`
  * Upper +1.28σ Band: `607.67` | Lower -1.28σ Band: `590.47`
  * Upper +1.00σ Band: `605.79` | Lower -1.00σ Band: `592.35`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`603.12` | EMA-20=`603.62` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`601.58` (Slope: `+0.0000`) | EMA-100=`600.21`
  * Institutional Anchors: EMA-144=`599.89` | EMA-200=`599.62` (Slope: `+0.1020`) | EMA-233=`599.93`
- **Range Boundaries**: 24H High=`617.68` | 24H Low=`583.39` | Weekly High=`619.59` | Weekly Low=`583.39`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `608.65` (Distance: `-1.25%`)
  * Point of Control (POC) = `599.51` (Distance: `+0.25%`)
  * Value Area Low (VAL) = `594.71` (Distance: `+1.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`609.02` | POC=`603.23` | VAL=`598.35`
  * Prior Day Extremes: PDH=`619.59` | PDL=`592.48` | PDC=`598.93`
  * Monday Range Blueprint: High=`602.04` | Mid=`592.51` | Low=`582.99`
  * Developing Weekly Value Area: Weekly VAH=`604.34` | Weekly POC=`594.58` | Weekly VAL=`589.70`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`609.29` | Low=`583.39`
  * London Session (08:00-16:00 UTC): High=`603.20` | Low=`588.63`
  * New York Session (13:00-21:00 UTC): High=`617.68` | Low=`596.96`
  * Initial Balance (First Hour): IB High=`592.17` | IB Low=`588.63`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `598.40` - `603.20`
  * Optimal Trade Entry (OTE 0.705): `602.00`
  * Structural Invalidation Anchor (0.786): `605.61`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:33:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `96` | `0xc179...e0c8` | `LONG` | 19,645,071.41 USD | `32,651,450,000.00` | `602.06` | `601.08` | `388.84` | -12,948.11 USD | `-0.07%` | `5X Cross` |
| `134` | `0xefe4...194b` | `LONG` | 15,150,299.23 USD | `25,203,033,000.00` | `599.00` | `601.08` | `0.000000` | 53,566.46 USD | `+0.35%` | `5X Cross` |
| `240` | `0x7fda...17d1` | `SHORT` | 9,819,105.95 USD | `16,333,870,000.00` | `602.93` | `601.08` | `2648.89` | 29,099.37 USD | `+0.30%` | `5X Cross` |
| `388` | `0x880a...311c` | `SHORT` | 6,160,020.16 USD | `10,247,401,000.00` | `596.85` | `601.08` | `1307.15` | -43,880.64 USD | `-0.71%` | `5X Cross` |
| `663` | `0x645b...87b8` | `SHORT` | 3,503,702.16 USD | `5,823,731,000.00` | `603.14` | `601.08` | `3747.64` | 8,827.16 USD | `+0.25%` | `5X Cross` |
| `740` | `0x07fd...689d` | `LONG` | 3,184,511.84 USD | `5,294,108,000.00` | `568.69` | `601.08` | `0.000000` | 173,790.75 USD | `+5.46%` | `5X Cross` |
| `843` | `0x5ad9...f5ef` | `SHORT` | 2,759,443.31 USD | `4,586,650,000.00` | `601.82` | `601.08` | `995.37` | 877.12 USD | `+0.03%` | `2X Cross` |
| `1131` | `0x26b6...9a13` | `LONG` | 2,003,850.84 USD | `3,332,143,000.00` | `604.79` | `601.08` | `0.000000` | -11,389.32 USD | `-0.57%` | `5X Cross` |
| `1214` | `0xe4a6...bd55` | `LONG` | 1,886,990.80 USD | `3,136,490,000.00` | `579.90` | `601.08` | `541.81` | 68,129.79 USD | `+3.61%` | `5X Cross` |
| `1251` | `0x27c9...d65d` | `SHORT` | 1,846,280.74 USD | `3,071,248,000.00` | `603.43` | `601.08` | `1062.26` | 7,009.29 USD | `+0.38%` | `5X Cross` |
| `1276` | `0x8b1d...ae3c` | `LONG` | 1,806,158.09 USD | `3,002,507,000.00` | `609.91` | `601.08` | `497.57` | -25,104.72 USD | `-1.39%` | `4X Isolated` |
| `1295` | `0x4c6d...5ee9` | `SHORT` | 1,761,818.39 USD | `2,928,944,000.00` | `608.78` | `601.08` | `843.76` | 21,267.97 USD | `+1.21%` | `3X Cross` |
| `1338` | `0x5b5d...c060` | `SHORT` | 1,694,453.80 USD | `2,818,359,000.00` | `599.58` | `601.08` | `53559.78` | -4,609.49 USD | `-0.27%` | `3X Cross` |
| `1397` | `0xf946...aebd` | `SHORT` | 1,623,780.00 USD | `2,700,000,000.00` | `510.68` | `601.08` | `705.32` | -244,942.03 USD | `-15.08%` | `5X Cross` |
| `1509` | `0xac48...3201` | `LONG` | 1,497,705.50 USD | `2,489,744,000.00` | `607.33` | `601.08` | `0.000000` | -14,382.45 USD | `-0.96%` | `5X Cross` |
| `1546` | `0x0274...a7f7` | `SHORT` | 1,446,146.29 USD | `2,404,633,000.00` | `528.54` | `601.08` | `832.28` | -175,202.59 USD | `-12.12%` | `2X Cross` |
| `1688` | `0x258a...ff03` | `SHORT` | 1,297,822.74 USD | `2,158,900,000.00` | `601.17` | `601.08` | `2389.88` | 54.02 USD | `+0.00%` | `5X Cross` |
| `1778` | `0x3dc9...54b0` | `SHORT` | 1,203,100.00 USD | `2,000,000,000.00` | `505.19` | `601.08` | `7345.72` | -192,721.55 USD | `-16.02%` | `5X Cross` |
| `1810` | `0xd2b2...11ed` | `SHORT` | 1,173,344.44 USD | `1,951,898,000.00` | `554.70` | `601.08` | `3385.63` | -90,617.24 USD | `-7.72%` | `5X Cross` |
| `1833` | `0x1bf6...5bfa` | `SHORT` | 1,154,265.60 USD | `1,920,000,000.00` | `566.73` | `601.08` | `1541.40` | -66,150.77 USD | `-5.73%` | `5X Cross` |
| `1848` | `0xdc51...6ef7` | `LONG` | 1,138,572.80 USD | `1,893,015,000.00` | `600.22` | `601.08` | `0.000000` | 2,338.99 USD | `+0.21%` | `5X Cross` |
| `1889` | `0x833b...db06` | `SHORT` | 1,105,373.47 USD | `1,838,826,000.00` | `554.51` | `601.08` | `1144.33` | -85,718.15 USD | `-7.75%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `540.76` | 1,230.77 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 1.23K USD at 540.7600 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `540.76` | 140.60 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.14K USD at 540.7600 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `540.76` | 32.45 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.03K USD at 540.7600 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `540.78` | 3,350.13 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 3.35K USD at 540.7800 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `540.82` | 705.23 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.71K USD at 540.8200 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `540.83` | 201.19 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.20K USD at 540.8300 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `540.84` | 504.06 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.50K USD at 540.8400 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `540.86` | 49.76 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.05K USD at 540.8600 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `540.94` | 1,229.56 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 1.23K USD at 540.9400 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `540.99` | 200.71 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.20K USD at 540.9900 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.02` | 137.42 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.14K USD at 541.0200 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.07` | 154.20 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.15K USD at 541.0700 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.09` | 42.21 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.04K USD at 541.0900 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.14` | 200.22 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.20K USD at 541.1400 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.15` | 5,343.86 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 5.34K USD at 541.1500 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.20` | 541.20 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.54K USD at 541.2000 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.20` | 541.20 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.54K USD at 541.2000 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.21` | 4,998.62 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 5.00K USD at 541.2100 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.21` | 95.25 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.10K USD at 541.2100 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.25` | 416.76 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.42K USD at 541.2500 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.27` | 504.46 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.50K USD at 541.2700 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.30` | 200.28 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.20K USD at 541.3000 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.31` | 510.46 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.51K USD at 541.3100 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.40` | 5,346.32 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 5.35K USD at 541.4000 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.40` | 1,296.11 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 1.30K USD at 541.4000 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.40` | 510.54 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.51K USD at 541.4000 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.41` | 510.01 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.51K USD at 541.4100 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `541.41` | 7.04 USD | `-` | `NEWS_INTEL` | `-` | #XMR Liquidated Long: 0.01K USD at 541.4100 USD [API] | `2026-10-15 02:24:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`619.17` (Vol: 258,700.00 USD, Dist: `+2.97%`) | Long MP=`594.91` (Vol: 258,700.00 USD, Dist: `--1.07%`)
  * 48H Horizon: Short MP=`618.79` (Vol: 221,500.00 USD, Dist: `+2.90%`) | Long MP=`594.72` (Vol: 276,600.00 USD, Dist: `--1.10%`)
  * 3D Horizon: Short MP=`618.79` (Vol: 221,500.00 USD, Dist: `+2.90%`) | Long MP=`582.68` (Vol: 319,000.00 USD, Dist: `--3.10%`)
  * 7D Horizon: Short MP=`625.29` (Vol: 402,800.00 USD, Dist: `+3.98%`) | Long MP=`582.51` (Vol: 376,400.00 USD, Dist: `--3.13%`)
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
  * Current Rate: `34.39K` | Last 24h: `45.46K` | Last 3d: `120.00K` | Last 7d: `265.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0346%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0328%` | **USDT KuCoin** | `0.0218%` |
| **USDT MEXC** | `0.0347%` | **USDT BingX** | `0.0325%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0190%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

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
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| Live | 15m | Tape Flow | NEUTRAL | Orderflow balanced at current level | - | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 4,280.00 USD | 14,990.00 USD | **`ACCUMULATION`** |
| `15m` | 3,890.00 USD | 46,470.00 USD | **`ACCUMULATION`** |
| `30m` | -4,420.00 USD | 490,820.00 USD | **`ACCUMULATION`** |
| `1h` | -72,730.00 USD | 675,340.00 USD | **`ACCUMULATION`** |
| `2h` | -68,230.00 USD | 965,860.00 USD | **`ACCUMULATION`** |
| `4h` | 336,360.00 USD | 2,400,000.00 USD | **`ACCUMULATION`** |
| `6h` | 906,990.00 USD | 2,410,000.00 USD | **`ACCUMULATION`** |
| `8h` | 1,170,000.00 USD | 2,920,000.00 USD | **`ACCUMULATION`** |
| `12h` | 2,410,000.00 USD | 2,900,000.00 USD | **`ACCUMULATION`** |
| `24h` | 4,080,000.00 USD | 59,210.00 USD | **`ACCUMULATION`** |
| `1w` | 14,670,000.00 USD | 3,630,000.00 USD | **`ACCUMULATION`** |
| `30d` | 31,850,000.00 USD | -10,010,000.00 USD | **`ACCUMULATION`** |

* Spot Capital Netflows: 5m=`+4.28K` | 15m=`+3.89K` | 1h=`-72.73K` | 24h=`+4.08M`
* Futures Capital Netflows: 5m=`+14.99K` | 15m=`+46.47K` | 1h=`+675.34K` | 24h=`+59.21K`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `594.71` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `589.40` (Risk Distance: `5.31` pts)
  * +2.5R Take Profit: `607.98`
  * Mathematical Lot Sizing: **`1.88 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `608.65` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `613.96` (Risk Distance: `5.31` pts)
  * +2.5R Take Profit: `595.38`
  * Mathematical Lot Sizing: **`1.88 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`605.61`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
