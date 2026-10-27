# INSTITUTIONAL AI COUNCIL REVIEW PROMPT: 360° DATA LAKE THINKING CHAIN & SOVEREIGN QUANT ARCHITECTURE

> **Target Systems**: Arena.ai (Claude 3.5 Sonnet / Opus 5.5 / GPT-4o / Gemini 1.5 Pro / DeepSeek V3 / Qwen 2.5), Copilot Studio, OpenAI GPT-4o.
> **Repository Context**: `https://github.com/kbsingh1399/Trading_2` (Branch: `main`)
> **Mission**: Forensic quantitative peer review of the Antigravity Sovereign Quant Trading Decision Architecture, Parquet Data Lake Synthesis, and Multi-Asset Execution Chain.

---

### PROMPT INSTRUCTIONS FOR EXTERNAL AI (COPY & PASTE BELOW)

```markdown
# 🏛️ INSTITUTIONAL QUANT AUDIT: 360° DATA LAKE & MULTI-ASSET TRADING CHAIN REVIEW

You are an Elite Managing Director of Quantitative Research, Statistical Arbitrage, and Market Microstructure at a premier quantitative hedge fund (Citadel, Renaissance Technologies, Jump Trading, Millennium). 

We have engineered an autonomous, institutional-grade quantitative trading and risk governance desk ("Antigravity Quant Fleet") managing a **Blueberry Markets MetaTrader 5 Account (#5064568, SVG Raw Spread, 5,000 USD Phase 1 Evaluation)**. 

We request your rigorous, mathematical, and adversarial critique of our entire end-to-end thinking chain, data lake synthesis engine, dynamic stop ratchet mechanics, and active multi-asset portfolio.

---

## 1. DESK CONTEXT & INVIOLABLE RISK BUDGET
- **Account Model**: Blueberry Markets MT5 Account #5064568
- **Initial Capital / Balance**: 5,000.00 USD / Current Balance: **4,833.47 USD** | Equity: **4,831.55 USD**
- **Statutory Profit Target**: +10.0% (5,500.00 USD equity)
- **Inviolable Triple Floor Governance**:
  * **Statutory Hard Floor**: **4,775.00 USD** (Max total drawdown 4.50% / 225.00 USD). Breach = Instant Challenge Forfeiture.
  * **Internal Operating Buffer**: **4,795.00 USD** (Defensive boundary).
  * **Current Cushion**: **+56.55 USD above Hard Floor** | **+36.55 USD above Operating Buffer**.
- **Ticket Risk Envelope**: Tier 1 Standard = **8.00–10.00 USD nominal risk per ticket** (0.16%–0.20% of NAV).
- **Flexible Capacity Policy**: Up to **4 concurrent filled positions** across ANY high-confluence combination (Crypto, Forex, Metals, Commodities, Indices) + **N resting maker limits**.

---

## 2. CANONICAL 36-FEED PARQUET DATA LAKE & ATOMIC OS.REPLACE ARCHITECTURE
Our desk operates on a 100% pure Parquet data lake located in `Data/feeds/*.parquet` (36 canonical feeds, 0 nulls, strictly updated every 60–120s with age < 3.0m).
- **Zero-Deletion Protocol**: Parquet files are NEVER unlinked or deleted from disk.
- **Atomic Replacement**: Ingestion daemons write to `.tmp_xyz.parquet` and atomically commit via `os.replace()`.
- **The 6 Strategic Pillars**:
  1. **Broker Telemetry & Solvency** (`00_MT5_Account_Telemetry`, `23_Master_Pipeline_Telemetry`) -> Live margin utilization, tick age, and stressed cushion.
  2. **Macro & Institutional Flows** (`1_Crypto_ETF_Flows`, `2_Spot_Netflow_S`, `19_News`, `19_Calendar`) -> Institutional ETF inflows/outflows, spot exchange netflows, Tier-1 economic embargoes.
  3. **Sentiment & Leverage Crowding** (`3_Exchanges_LS_Ratio_15M/1H/4H`, `5_OI`, `5_Funding_Rate`, `6_Funding_Fee_Settlement`) -> Retail long/short bias, open interest expansion, funding carry traps.
  4. **Liquidation Geometry & Stop Sweep Magnets** (`7_Liq_Heapmap`, `7_Live_Liq`, `8_Exchange_Liquidation_Map_1D/7D`, `9_Liquidation_Max_Pain_24H/48H/3D/7D`, `14_Liquidation_Matrix`, `14_Hyperdash_Liq_Map`, `15_Hyperdash_Stops_Map`, `22_Forced_Liquidations_MTF`) -> Cumulative liquidation ladders, max pain magnets, and cascade exhaustion bands.
  5. **Microstructure, Whales & Footprint Signals** (`10_Whale_Orders`, `17_Orderbook`, `18_CVD*`, `21_Tradfye_Orderflow`, `25_CoinGlass_Footprint_Signals`, `26_Aggregated_Footprint_Bar_Metrics`) -> L2/L3 orderbook depth asymmetry, resting whale armor (>= 100K USD, persistence tau >= 180s), CVD taker delta divergence, footprint buyer/seller exhaustion.
  6. **Technical & Auction Market Structure** (`11_Technical`, `11_Technical_BTC_Ribbon`, `12_Hyperdash`, `13_Hyperliquid`, `16_Hyperdash_telegram_Intel`, `20_Auction_Market_Structure`) -> Daily/Weekly Volume Profile VPOC, Value Area High/Low (VAH/VAL), VWAP Z-scores, and Fibonacci Prime EMA Ribbons (34, 89, 233).

---

## 3. NEW MECHANISM: 360° DATA LAKE DOSSIER ENGINE (`asset_360_dossier_engine.py`)
To prevent "context amnesia" or overlooking critical data feeds (e.g. footprint signals, whale walls, liquidation maps), we built an automated extraction engine:
- **CLI/API**: `python Terminal/Data_Factory/asset_360_dossier_engine.py --asset <ASSET>`
- **Schema-Aware Multi-Column Resolver**: Automatically resolves base tokens (`BTC`), crypto pairs (`BTCUSDT`, `BTC-PERP`), broker symbols (`BTCUSD.pi`), and commodities/forex (`XAUUSD`, `OIL`, `USDCAD`).
- **Exhaustive Traversal**: Traverses all 42 parquet files in `Data/feeds/`, parses rows matching the asset across 10+ symbol columns, and compiles:
  * Machine-readable database: `Data/dossiers/{ASSET}_360_dossier.json`
  * Institutional dossier briefing: `docs/dossiers/{ASSET}_360_DOSSIER.md`
- **Zero Omission Guarantee**: Every single file containing data for the candidate asset is extracted into the 6 pillars with zero omission prior to trade formulation.

---

## 4. TWO-SPEED DYNAMIC ARCHITECTURE
- **Speed 1 (Macro Analytical Cycle Delay - 20 Minutes)**:
  * Between cycle completions, the macro coordinator yields execution for strictly **1,200 seconds (`T_finish + 20 min`)** via `schedule`.
  * Allows 15m candle bars to close, orderbooks to absorb volume, and new data to populate the lake.
  * Relies on reactive system wakeups with zero polling loops.
- **Speed 2 (Continuous Microstructure Supervisor Daemon - 5.0 Seconds)**:
  * Background daemon (`Terminal/dynamic_position_supervisor.py --interval 5.0`) runs continuously at **5.0-second intervals**.
  * Monitors live MT5 tick quotes, triggers Stage 1 BE ratchets (+0.15R lock at +0.80R gain), triggers Stage 2 Profit ratchets (+0.80R lock at +1.50R gain), and enforces 6-hour time decay exits.
  * **Monotone Non-Loosening Invariant**: For Buy: `target_sl > p.sl`. For Sell: `target_sl < p.sl`. Stop loosening is mathematically impossible.

---

## 5. ACTIVE MULTI-ASSET PORTFOLIO & RECENT TRADE RESULTS

### Closed Trades:
- `GBPUSD.pi` Short (`#19376886` @ 1.33242): Stage 2 dynamic ratchet moved SL to `1.33181` (+0.80R lock). Closed via Deal `#17555634` realizing **+7.32 USD gross profit (+6.48 USD net profit after commissions)**.

### Active Filled Positions (2 Slots):
1. **`BTCUSD.pi` Short (`#19379711`)**:
   - Entry: `80,560.00 USD` (Passive Maker Limit fill)
   - Current Price: `80,473.50 USD` | **PnL: +1.73 USD (IN PROFIT, +0.36R)**
   - Protective Bracket: SL = `80,860.00 USD` (Risk: 6.00 USD) | TP = `79,910.00 USD` (Reward: 13.00 USD | 2.17 R:R)
   - Data Lake Confluence: Feed 33 (`25_CoinGlass_Footprint_Signals`) stamped Buyer Exhaustion at 80,692.10 USD (volume vacuum in top 10% of bar); Feed 10 stamped 12.29M USD Ask whale wall at 80,750-80,800 USD protecting our SL; TP front-runs buyer absorption shelf at 79,911.40 USD.
2. **`USDJPY.pi` Short (`#19376039`)**:
   - Entry: `157.850` | Current Price: `157.922` | PnL: **-3.65 USD**
   - Protective Bracket: SL = `158.024` (Risk: 8.81 USD) | TP = `157.450` (Reward: 20.26 USD | 2.30 R:R)
   - Data Lake Confluence: Feed 18 (`18_CVD`) negative taker delta; Feed 11 (`11_Technical`) VWAP Z-score +1.58 SD rejection.

### Resting Maker Limits (3 Slots):
3. **`ETHUSD.pi` SELL_LIMIT (`#19383569`)**:
   - Entry: `2,348.50 USD` (0.50 lots) | SL = `2,365.00 USD` (Risk: 8.25 USD) | TP = `2,312.00 USD` (Reward: 18.25 USD | 2.21 R:R)
   - Data Lake Confluence: 35 feeds populated; VWAP Z-score = **+2.14 SD**; RSI = **70.90**; 425 Whale orders with resting sell bunker at 2,352.20 USD; liquidation cascade magnet at 2,312.00 USD.
4. **`UKBRENT.p` SELL_LIMIT (`#19378313`)**:
   - Entry: `115.175` (0.20 lots) | SL = `115.668` (Risk: 9.86 USD) | TP = `113.943` (Reward: 24.64 USD | 2.50 R:R)
   - Data Lake Confluence: Commodities supply sweep pool above 115.00 handle.
5. **`XAUUSD.pi` BUY_LIMIT (`#19381300`)**:
   - Entry: `4033.00 USD` (0.01 lots) | SL = `4025.50 USD` (Risk: 7.50 USD) | TP = `4051.75 USD` (Reward: 18.75 USD | 2.50 R:R)
   - Data Lake Confluence: Institutional Volume Profile VPOC shelf at 4033.00 USD.

### Stressed Solvency Math:
- Total Joint Contingent Risk across ALL 5 positions: `6.00 + 8.81 + 8.25 + 9.86 + 7.50 = 40.42 USD`
- Live Account Equity: `4,831.55 USD`
- Stressed Worst-Case Equity (if all 5 stopped out simultaneously): **4,791.13 USD**
- **Surplus above 4,775.00 USD Statutory Hard Floor**: **+16.13 USD (100% Intact)**

---

## 6. YOUR ADVERSARIAL AUDIT MANDATE
Please conduct an unsparing, institutional review addressing the following 5 dimensions:

1. **Data Lake Synthesis & The 360° Dossier Mechanism**:
   - Is our schema-aware multi-column traversal pattern sufficient to eliminate orderflow blindspots?
   - What additional statistical or orderflow metrics should be extracted from our footprint (`25_CoinGlass_Footprint_Signals`) or liquidation (`14_Liquidation_Matrix`) feeds?
2. **Two-Speed Dynamic Architecture (20m Macro / 5s Micro)**:
   - Does a 20-minute macro delay with a 5.0-second background supervisor strike the optimal balance between token preservation and execution speed?
   - How can we optimize the ratchet logic to prevent premature whipouts on trailing stops while preserving paper gains?
3. **Cross-Asset Correlation & Risk Allocation**:
   - We currently have short exposure on `BTCUSD.pi` and `ETHUSD.pi`. How should we model intra-crypto co-movement in our worst-case stress simulations?
   - Is our flexible capacity policy (permitting all-crypto, all-forex, or multi-asset combinations based purely on confluence) sound, or should hard sector caps be re-enforced?
4. **Trade Structure & Entry Precision**:
   - Critique the entry, SL, and TP geometry of `ETHUSD.pi` (2,348.50 / 2,365.00 / 2,312.00) and `BTCUSD.pi` (80,560.00 / 80,860.00 / 79,910.00). Are our stops placed sufficiently beyond structural sweep liquidity?
5. **Phase 1 Challenge Acceleration Strategy**:
   - Account equity is at 4,831.55 USD, targeting 5,500.00 USD (668.45 USD needed).
   - How should we calibrate risk scaling (e.g. from 10.00 USD base risk to 15.00 USD house money) as accumulated profit expands our cushion above 4,850 USD?
```
