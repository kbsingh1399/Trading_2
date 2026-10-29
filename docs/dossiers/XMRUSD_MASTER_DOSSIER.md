# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XMRUSD
**Canonical Key**: `XMRUSD` | **Broker Instrument**: `XMRUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:57:19 IST` (`2026-10-29 20:27:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `600.04` | **Live Ask Quote**: `600.47` | **Mid Price**: `600.25`
- **Spread Points**: `43.00` | **Spread BPS**: `7.16 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `599.09` | VWAP Z-Score: `+0.19` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.98` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.42` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `619.09` | Lower -3.00σ Band: `579.08`
  * Upper +2.51σ Band: `615.82` | Lower -2.51σ Band: `582.35`
  * Upper +2.01σ Band: `612.49` | Lower -2.01σ Band: `585.69`
  * Upper +2.00σ Band: `612.42` | Lower -2.00σ Band: `585.75`
  * Upper +1.28σ Band: `607.62` | Lower -1.28σ Band: `590.55`
  * Upper +1.00σ Band: `605.75` | Lower -1.00σ Band: `592.42`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`602.57` | EMA-20=`603.31` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`601.54` (Slope: `+0.0000`) | EMA-100=`600.21`
  * Institutional Anchors: EMA-144=`599.90` | EMA-200=`599.64` (Slope: `+0.0832`) | EMA-233=`599.98`
- **Range Boundaries**: 24H High=`617.68` | 24H Low=`583.39` | Weekly High=`619.59` | Weekly Low=`583.39`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `608.65` (Distance: `-1.36%`)
  * Point of Control (POC) = `599.51` (Distance: `+0.14%`)
  * Value Area Low (VAL) = `595.16` (Distance: `+0.87%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `597.85` - `602.66`
  * Optimal Trade Entry (OTE 0.705): `601.46`
  * Structural Invalidation Anchor (0.786): `605.06`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:54:30 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `96` | `0xc179...e0c8` | `LONG` | 19,591,359.77 USD | `32,651,450,000.00` | `602.06` | `600.06` | `390.56` | -66,659.74 USD | `-0.34%` | `5X Cross` |
| `133` | `0xefe4...194b` | `LONG` | 15,140,077.25 USD | `25,232,621,000.00` | `599.01` | `600.06` | `0.000000` | 25,580.23 USD | `+0.17%` | `5X Cross` |
| `240` | `0x7fda...17d1` | `SHORT` | 9,751,250.83 USD | `16,251,543,000.00` | `602.93` | `600.06` | `2761.31` | 47,316.94 USD | `+0.49%` | `5X Cross` |
| `387` | `0x880a...311c` | `SHORT` | 6,177,183.62 USD | `10,292,407,000.00` | `596.86` | `600.06` | `1313.10` | -34,034.99 USD | `-0.55%` | `5X Cross` |
| `658` | `0x645b...87b8` | `SHORT` | 3,494,267.72 USD | `5,823,731,000.00` | `603.14` | `600.06` | `3825.27` | 18,261.60 USD | `+0.52%` | `5X Cross` |
| `724` | `0x07fd...689d` | `LONG` | 3,183,984.12 USD | `5,301,383,000.00` | `568.74` | `600.06` | `0.000000` | 168,899.84 USD | `+5.30%` | `5X Cross` |
| `839` | `0x5ad9...f5ef` | `SHORT` | 2,740,002.03 USD | `4,566,632,000.00` | `601.81` | `600.06` | `999.69` | 8,244.72 USD | `+0.30%` | `2X Cross` |
| `1124` | `0x26b6...9a13` | `LONG` | 2,000,751.94 USD | `3,332,143,000.00` | `604.79` | `600.06` | `0.000000` | -14,488.21 USD | `-0.72%` | `5X Cross` |
| `1202` | `0xe4a6...bd55` | `LONG` | 1,881,941.05 USD | `3,136,490,000.00` | `579.90` | `600.06` | `541.87` | 63,080.04 USD | `+3.35%` | `5X Cross` |
| `1228` | `0x27c9...d65d` | `SHORT` | 1,852,019.33 USD | `3,086,596,000.00` | `603.42` | `600.06` | `1065.16` | 10,493.82 USD | `+0.57%` | `5X Cross` |
| `1266` | `0x8b1d...ae3c` | `LONG` | 1,802,945.40 USD | `3,002,507,000.00` | `609.91` | `600.06` | `497.64` | -28,317.40 USD | `-1.57%` | `4X Isolated` |
| `1286` | `0x4c6d...5ee9` | `SHORT` | 1,759,109.12 USD | `2,928,944,000.00` | `608.78` | `600.06` | `843.81` | 23,977.24 USD | `+1.36%` | `3X Cross` |
| `1323` | `0x5b5d...c060` | `SHORT` | 1,698,033.35 USD | `2,830,032,000.00` | `599.58` | `600.06` | `55379.89` | -1,189.42 USD | `-0.07%` | `3X Cross` |
| `1385` | `0xf946...aebd` | `SHORT` | 1,621,485.00 USD | `2,700,000,000.00` | `510.68` | `600.06` | `705.37` | -242,647.03 USD | `-14.96%` | `5X Cross` |
| `1509` | `0xac48...3201` | `LONG` | 1,493,896.19 USD | `2,489,744,000.00` | `607.33` | `600.06` | `0.000000` | -18,191.76 USD | `-1.22%` | `5X Cross` |
| `1542` | `0x0274...a7f7` | `SHORT` | 1,444,078.30 USD | `2,404,633,000.00` | `528.54` | `600.06` | `832.50` | -173,134.61 USD | `-11.99%` | `2X Cross` |
| `1656` | `0x258a...ff03` | `SHORT` | 1,311,774.02 USD | `2,186,035,000.00` | `601.16` | `600.06` | `2370.21` | 2,380.71 USD | `+0.18%` | `5X Cross` |
| `1772` | `0x3dc9...54b0` | `SHORT` | 1,200,140.00 USD | `2,000,000,000.00` | `505.19` | `600.06` | `7676.68` | -189,761.55 USD | `-15.81%` | `5X Cross` |
| `1801` | `0xd2b2...11ed` | `SHORT` | 1,171,376.93 USD | `1,951,898,000.00` | `554.70` | `600.06` | `3370.04` | -88,649.72 USD | `-7.57%` | `5X Cross` |
| `1823` | `0x1bf6...5bfa` | `SHORT` | 1,152,000.00 USD | `1,920,000,000.00` | `566.73` | `600.06` | `1545.59` | -63,885.17 USD | `-5.55%` | `5X Cross` |
| `1838` | `0xdc51...6ef7` | `LONG` | 1,136,850.16 USD | `1,893,015,000.00` | `600.22` | `600.06` | `0.000000` | 616.34 USD | `+0.05%` | `5X Cross` |
| `1877` | `0x833b...db06` | `SHORT` | 1,103,519.94 USD | `1,838,826,000.00` | `554.51` | `600.06` | `1179.89` | -83,864.62 USD | `-7.60%` | `5X Cross` |

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
  * 24H Horizon: Short MP=`619.17` (Vol: 258,700.00 USD, Dist: `+3.35%`) | Long MP=`594.91` (Vol: 258,700.00 USD, Dist: `--0.70%`)
  * 48H Horizon: Short MP=`618.79` (Vol: 221,500.00 USD, Dist: `+3.29%`) | Long MP=`594.72` (Vol: 276,600.00 USD, Dist: `--0.73%`)
  * 3D Horizon: Short MP=`618.79` (Vol: 221,500.00 USD, Dist: `+3.29%`) | Long MP=`582.68` (Vol: 319,000.00 USD, Dist: `--2.74%`)
  * 7D Horizon: Short MP=`625.29` (Vol: 402,800.00 USD, Dist: `+4.37%`) | Long MP=`582.51` (Vol: 376,400.00 USD, Dist: `--2.77%`)
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
  * Current Rate: `31.78K` | Last 24h: `45.46K` | Last 3d: `120.00K` | Last 7d: `264.99K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0329%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0275%` | **USDT KuCoin** | `0.0225%` |
| **USDT MEXC** | `0.0331%` | **USDT BingX** | `0.0319%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0169%` |
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
| `5m` | 8,580.00 USD | -34,250.00 USD | **`DISTRIBUTION`** |
| `15m` | 633.20 USD | 150,310.00 USD | **`ACCUMULATION`** |
| `30m` | 22,950.00 USD | 179,120.00 USD | **`ACCUMULATION`** |
| `1h` | -7,810.00 USD | 754,810.00 USD | **`ACCUMULATION`** |
| `2h` | -77,610.00 USD | 680,080.00 USD | **`ACCUMULATION`** |
| `4h` | 226,410.00 USD | 2,020,000.00 USD | **`ACCUMULATION`** |
| `6h` | 897,220.00 USD | 2,300,000.00 USD | **`ACCUMULATION`** |
| `8h` | 1,080,000.00 USD | 3,220,000.00 USD | **`ACCUMULATION`** |
| `12h` | 2,320,000.00 USD | 2,940,000.00 USD | **`ACCUMULATION`** |
| `24h` | 4,010,000.00 USD | 341,450.00 USD | **`ACCUMULATION`** |
| `1w` | 14,600,000.00 USD | 3,780,000.00 USD | **`ACCUMULATION`** |
| `30d` | 31,960,000.00 USD | -9,860,000.00 USD | **`ACCUMULATION`** |

* Spot Capital Netflows: 5m=`+8.58K` | 15m=`+633.20` | 1h=`-7.81K` | 24h=`+4.01M`
* Futures Capital Netflows: 5m=`-34.25K` | 15m=`+150.31K` | 1h=`+754.81K` | 24h=`+341.45K`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `595.16` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `589.74` (Risk Distance: `5.42` pts)
  * +2.5R Take Profit: `608.72`
  * Mathematical Lot Sizing: **`1.84 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `608.65` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `614.07` (Risk Distance: `5.42` pts)
  * +2.5R Take Profit: `595.09`
  * Mathematical Lot Sizing: **`1.84 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`605.06`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
