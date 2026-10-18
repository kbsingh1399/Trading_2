# 🏛️ STANDARDIZED QUANTITATIVE TRADING DECISION CHAIN (SOP)
## Canonical Multi-Pillar Institutional Microstructure Decision Architecture

> **Document Status**: CANONICAL PRODUCTION SPECIFICATION  
> **Target Environment**: MetaTrader 5 (Blueberry Markets, Account #5064568)  
> **Execution Engine**: Antigravity Autonomous Decision Desk  
> **Mandatory Foundation**: 8 Core Multi-Domain Skill Ensembles (Non-Bypassable)

---

## SECTION 1: MANDATORY SKILLS ENSEMBLE FOUNDATION

Under strict hedge fund operational governance, **no trading analysis, hypothesis formation, order staging, or modification may ever occur in an ad-hoc or single-agent vacuum**. Every cycle and decision must systematically activate and apply the following foundational skill suite as the **absolute minimum requirement**, dynamically augmenting with additional specialized skills as market conditions dictate:

```mermaid
flowchart TD
    subgraph CoreFoundationalSkills ["Mandatory Minimum Skills Ensemble"]
        S1["/remember<br/>Cross-Session Memory & Trajectory"]
        S2["/graphify<br/>AST Knowledge & Architecture Traversal"]
        S3["/data-engineer<br/>Data Contracts & Pipeline Ingestion"]
        S4["/dataform-bigquery<br/>Institutional Data Modeling & Scalability"]
        S5["/data-analyst<br/>Orderflow & Distribution Dissection"]
        S6["/data-engineering-data-driven-feature<br/>Statistical Rigor & Feature Hypotheses"]
        S7["/brainstorm<br/>Multi-Perspective Dialectic Stress-Testing"]
        S8["/verify<br/>Ex-Ante Pre-Execution Gate Verification"]
    end
    
    subgraph QuantitativeExecution ["Institutional Quant Desk"]
        QD["10-Step Decision-Making Chain"]
    end
    
    CoreFoundationalSkills --> QD
```

### The 8 Mandatory Foundation Skills:
1. **`/remember` (Persistent Cross-Session Memory & Trajectory Continuity)**:
   - Eliminates context amnesia. Retrieves past operator directives, settled invariants, post-loss autopsies, avoided traps (e.g., chasing unaligned limits, illiquid FX rollover hours, buying into un-swept stop clusters), and running capital cushion trajectory.
2. **`/graphify` (AST Knowledge Graph & Structural Traversal)**:
   - Queries repository semantic graphs (`graphify-out/graph.json`, 7.4k+ nodes) before modifying code, validating execution schemas, parameter bounds, broker symbols, and contract specifications.
3. **`/data-engineer` (Data Contract Enforcement & Pipeline Integrity)**:
   - Verifies raw tick ingestion, timestamp monotonicity, zero nulls, broker basis normalization (`venue_basis`), and telemetry data freshness. Rejects stale or corrupted data frames fail-closed.
4. **`/dataform-bigquery` (Institutional Data Modeling & Scalability)**:
   - Governs historical time-series consistency across all 43 canonical Parquet datasets and 3.47M 15m bars. Enforces unified data definitions from micro-ticks to multi-year horizons.
5. **`/data-analyst` (Orderflow, Auction & Distribution Dissection)**:
   - Decomposes multidimensional metrics: MT5 spreads in bps, VWAP standard deviations, volume profile POC/VAH/VAL, multi-horizon CVD deltas, and auction imbalance ratios.
6. **`/data-engineering-data-driven-feature` (Empirical Feature Engineering & Statistical Rigor)**:
   - Formulates verifiable quantitative hypotheses, establishes statistical significance (p_win lower bounds, z-score thresholds), and designs causal features with zero lookahead.
7. **`/brainstorm` (Multi-Perspective Dialectic & Persona Stress-Testing)**:
   - Simulates adversarial multi-agent debate (Orderflow Specialist vs Macro Risk Officer vs Forensic Position Auditor). Tests edge cases: *What if the whale pulls? What if the market blows through the cascade?*
8. **`/verify` (Ex-Ante Pre-Execution Gate & Boundary Verification)**:
   - Mathematical proof before dispatch. Verifies cash risk calculations against `mt5.order_calc_profit`, checks hard floor cushion (>= 4,775 USD), verifies passive limit posture, and validates SL/TP placement.
9. **`/risk-engine` (Stressed Multi-Ticket Floor Defense Simulator)**:
   - Computes worst-case stressed equity across all open and staged tickets: $\text{Stressed Equity} = \text{Current Equity} - \sum (\text{Risk}_i \times 1.25 + 2.00) \ge 4,795.00\text{ USD}$ (preserving a mandatory $+20.00\text{ USD}$ operating buffer above the $4,775.00\text{ USD}$ absolute hard floor).
10. **`/execution-sim` (Microstructure Execution & Friction Compensation)**:
    - Models half-spread offset ($\text{Entry} = \text{Shelf} - \text{half\_spread}$ for longs, $\text{Shelf} + \text{half\_spread}$ for shorts), verifies `ORDER_FILLING_IOC` with automatic failover to `RETURN` and `FOK`.
11. **`/onchain-forensics` (Arkham Institutional Deanonymization)**:
    - Parses live `onchain_arkham_intelligence`, calculates net flow velocity ($\text{Outflow} - \text{Inflow}$), flags institutional CEX deposits, and attributes wallet flows to specific assets.
12. **`/market-microstructure` (Orderbook Replenishment & Spoof Detection)**:
    - Analyzes L2 replenishment velocity $d(\text{depth})/dt$, calculates book imbalance ratios, and filters out phantom/ephemeral orders using presence fraction ($\ge 0.85$) and minimum persistence ($\ge 180\text{s}$).

---

## SECTION 2: THE 10-STEP STANDARDIZED TRADING DECISION CHAIN

```mermaid
flowchart TD
    Step1["Step 1: Data Contract, Ingestion & Sanity Gate (/data-engineer, /dataform-bigquery)"] --> Step2["Step 2: Tri-Layer Memory & Trajectory Audit (/remember)"]
    Step2 --> Step3["Step 3: AST Knowledge Graph Traversal (/graphify)"]
    Step3 --> Step4["Step 4: HTF Auction & Regime Profiling (/data-analyst)"]
    Step4 --> Step5["Step 5: Dual-Engine Strategy Dialectic (/brainstorm, /data-driven-feature)"]
    Step5 --> Step6["Step 6: Microstructure Coincidence Stack & On-Chain Intel"]
    Step6 --> Step7["Step 7: Liquidation & Stop Magnet Dynamics (Absorption vs Blow-Through)"]
    Step7 --> Step8["Step 8: Mathematical Risk Budget & Capital Floor Gate"]
    Step8 --> Step9["Step 9: Pre-Execution Ex-Ante Audit (/verify)"]
    Step9 --> Step10["Step 10: Autonomous Punch & Dynamic Ratchet Lifecycle"]
```

---

### STEP 1: Data Contract, Ingestion & Sanity Gate (Mandatory Line-by-Line Ingestion & JIT Refresh)
*Active Skills: `@[data-engineer]`, `@[dataform-bigquery]`, `@[performance-engineer]`*

Every analysis begins by establishing absolute data integrity across the telemetry pipeline and macro calendar:

1. **Mandatory Just-In-Time (JIT) Telemetry Refresh Gate**:
   - While the background synchronization daemon operates at a peaceful 5-minute (300s) cadence to eliminate Git push collisions and CPU bloat, **prior to dispatching any subagents or compiling a prompt for Arena.ai**, Step 1 mandates an immediate synchronous run of `Terminal/Data_Factory/generate_telemetry_snapshot.py`.
   - This guarantees that all subagents and external models make decisions exclusively on **0-second-fresh live MT5 quotes, open ticket PnL, margin levels, and L2/L3 orderbook depth**.

2. **Mandatory Line-by-Line Telemetry Ingestion & Narrative Continuity**:
   - Agents, subagents, and external council models are **strictly forbidden from skimming or reading only top-level summary keys**.
   - You MUST read `docs/telemetry/live_snapshot_latest.json` **line-by-line and section-by-section**:
     * Trace the running account narrative: track how equity, balance, floating PnL, and hard floor cushion have progressed turn-over-turn.
     * Track active positions and tickets: inspect entry fills, current bid/ask, ATR-14 volatility, and distance to dynamic ratchet triggers.
     * Trace orderbook and whale wall evolution: confirm whether supporting whale bunkers are persistent (persist >= 180s) or decaying.
     * Trace liquidation floor/ceiling migration: map evolving short-squeeze and long-liquidation cascade pools across cycles.

3. **Mandatory Line-by-Line Forex Factory Macro Calendar & News Ingestion (Macro Idea Generation)**:
   - Systematically read `Data/forex_factory_live.json` and `Data/forex_factory_summary.json` **line-by-line**:
     * **High-Impact Macro Releases**: Scrutinize inflation prints (CPI, PPI), employment data (NFP, unemployment), retail sales, and GDP metrics, analyzing actual vs forecast surprises.
     * **Central Bank Speeches & Policy**: Dissect public statements from Federal Reserve officials, Bank of Japan (MoF intervention warnings), Bank of England (Gov Bailey), and ECB governors.
     * **Geopolitical & Commodity Catalysts**: Track breaking geopolitical headlines, trade policies, and energy supply shocks (e.g. crude oil surging toward $100/bbl).
     * **Macro Trade Idea Generation**: Actively synthesize this macro intelligence into fresh, asymmetric trade hypotheses (e.g. fading USD/JPY at 158.20 intervention tripwires, shorting risk-off equities under stagflation, or trading commodities with structural flow tailwinds).

4. **Clock & Freshness Audit**: Verify telemetry timestamp is within 180 seconds of live UTC. Stale telemetry triggers immediate live tick refresh.
5. **Monotonicity & Zero-Null Invariant**: Ingest 15m and HTF OHLCV bars, verifying strict time monotonicity and zero NaN/null values in closing prices, volume, and CVD.
6. **Broker Venue Basis Mapping**: Map Binance / Hyperdash crypto levels to MT5 execution symbols using `venue_basis`:
   $$\text{Price}_{\text{MT5}} = \text{Price}_{\text{Binance}} + \text{venue\_basis}$$
7. **Spread Friction Threshold Gate**:
   - Crypto Perpetuals: MT5 Spread must be $\le 25.0\text{ bps}$ (e.g. BTC ~2.5 bps, ETH ~12 bps).
   - TradFi CFDs (Forex/Indices/Commodities): MT5 Spread must be $\le 5.0\text{ bps}$ (Gold ~0.2 bps, SP500 ~0.4 bps, USDJPY ~0.1 bps).
   - Any asset with spread exceeding its ceiling (e.g. DOGE at 261 bps) is disqualified immediately.

---

### STEP 2: Tri-Layer Memory & Trajectory Audit
*Active Skills: `@[memory-system]`, `@[anti-sycophancy]`, `@[quant-analyst]`, `@[odb-microstructure-forensics]`*

No trade is evaluated in a vacuum. The system reviews the persistent narrative and past lessons:
1. **Persistent Memory System Audit (`/memory-system`)**:
   - Review `.agents/memory/MEMORY.md` index, `.agents/memory/feedback-history.md` (past issues, setbacks & permanent resolutions), `.agents/memory/operator-directives.md` (active operational mandates & rights), `.agents/memory/user-preferences.md`, and `.agents/rules/ACTIVE_CONTEXT.md`.
   - Zero context amnesia: Ensure all past feedback and lessons raised by the operator are perpetually enforced.
2. **Mandatory Forensic Autopsy Reference (`LOSING_TRADES_DEEP_FORENSIC_AUTOPSY.md`)**:
   - The desk MUST refer to [`LOSING_TRADES_DEEP_FORENSIC_AUTOPSY.md`](file:///c:/Users/SIGMA/Documents/Trading_2/docs/specs/LOSING_TRADES_DEEP_FORENSIC_AUTOPSY.md) (Brain Artifact: `C:\Users\SIGMA\.gemini\antigravity\brain\b00c810a-61bb-46bf-a147-4c8859c64058\LOSING_TRADES_DEEP_FORENSIC_AUTOPSY.md`) on EVERY evaluation turn to eliminate historical failure patterns.
   - **The Three Inviolable Anti-Regression Invariants**:
     * **Invariant A (Whale Bunker Stop Sizing — Never Choke Stops & Expanded Risk Rights)**: In 38.5% of historical losses, direction was 100% correct, and 4 trades (EURUSD, USWTI, BTC, Gold) hit full Take Profit immediately post-stop. Stops must NEVER be calculated from arbitrary point or ATR fractions inside the market sweep zone. All stops MUST anchor behind verified resting institutional liquidity (persistent L2/L3 whale walls with $\text{persist} \ge 180\text{s}$) plus a $0.50\text{ ATR}$ structural buffer. Per explicit operator directive, the stop loss dollar budget is expanded to **$15.00–$25.00 USD** (0.30%–0.51% equity) or lot size scaled down (0.05 or 0.01) to safely clear the whale bunker without choking!
     * **Invariant B (Higher-Timeframe Trend Hierarchy Gate — Zero Falling Knives)**: In 38.5% of historical losses, the desk bought dips in aggressive HTF bear trends (BTC plunging -2,151 pts further, ETH dropping -$155 further). In a confirmed 1H/4H Bear Trend ($\text{Price} < \text{EMA}_{20} < \text{EMA}_{50} < \text{EMA}_{200}$), Model 1 Long dip-buying is **strictly FORBIDDEN** regardless of 15m oversold oscillator readings. The desk may ONLY stage Model 2 Trend Pullback Shorts at overhead resistance shelves.
     * **Invariant C (Adaptive Early Breakeven at +0.75R0 to +0.80R0 — Protecting Positive MFE)**: 76.9% of historical losing trades (20 of 26) were in positive profit before reversing. Once price reaches $+0.75\text{R0 to }+0.80\text{R0}$ and reclaims the session Volume Profile POC or VWAP, arm an early risk cut to Entry $+ 0.10\text{R0}$ to prevent green trades from turning into full stop-outs during session volatility transitions (e.g. 13:30 UTC NY Cash Open).
3. **Anti-Trap Checklist**: Confirm candidate setup does not match known trap patterns:
   - Never stage limit entries directly above/below un-swept opposing stop clusters.
   - Never catch falling knives against massive unidirectional CVD without absorption evidence.
   - Never place orders during illiquid interbank rollover spread expansion (21:30–22:30 UTC).
4. **Live Capital Floor Cushion**:
   $$\text{Floor Cushion} = \text{Current Equity} - 4,775.00\text{ USD}$$
   Confirm that existing open positions and staged pending orders leave the cushion strictly positive.

---

### STEP 3: AST Knowledge Graph Traversal & Rule Check
*Active Skills: `@[graphify]`*

Query the system architecture to prevent logic regressions:
1. **Canonical Schema Query**: Verify symbol mapping (`Terminal/Asset_Universe.py`), lot steps, minimum volume, and digits via AST lookup.
2. **Strategy Module Integrity**: Verify active logic resides in canonical single modules (`Terminal/OF_Strategy.py`, `Engine/s1_liquidation_cascade.py`), adhering to the Single Strategy File Mandate.
3. **Mathematical Invariant Check**: Ensure ATR calculations, VWAP standard deviation formulas, and volume profile definitions match `.okf/` verified contracts.

---

### STEP 4: Higher-Timeframe Auction & Regime Profiling
*Active Skills: `@[data-analyst]`*

Determine the macro structural environment before looking at intraday triggers:
1. **HTF Trend Hierarchy (1H & 4H)**:
   - **Bullish Regime**: $\text{Price} > \text{EMA}_{20} > \text{EMA}_{50} > \text{EMA}_{200}$ on 1H/4H.
   - **Bearish Regime**: $\text{Price} < \text{EMA}_{20} < \text{EMA}_{50} < \text{EMA}_{200}$ on 1H/4H.
   - **Ranging / Mean-Reverting**: EMAs flat, compressed, or oscillating.
2. **Auction Market Structure**:
   - Identify Prior Day and Prior Week POC, VAH (Value Area High), and VAL (Value Area Low).
   - Evaluate Session VWAP and Multi-Day Anchor VWAPs.
3. **Stand-Aside Protocol**: If the market displays conflicting regimes or choppy liquidity without clear structural edges, the desk **stands aside unconditionally**. Cash is a valid position.

---

### STEP 5: Dual-Engine Strategy Dialectic & Opportunity Screening
*Active Skills: `@[brainstorm]`, `@[data-engineering-data-driven-feature]`*

Screen candidates across the universe into two distinct, non-overlapping quantitative models:

#### Model 1: Extreme Mean Reversion
- **Condition**: Market reaches statistical extremes ($|Z_{\text{VWAP}}| \ge 2.0\text{ SD}$ to $3.5\text{ SD}$).
- **Required Confluence**:
  1. Price tested an extreme structural boundary (outer VWAP band +2.0 SD / -2.0 SD, extreme weekly deviation).
  2. Orderflow shows **Trapped Traders** (`TRAPPED_BUYERS_ABOVE` for Shorts, `TRAPPED_SELLERS_BELOW` for Longs).
  3. Microstructure tape reveals clear momentum exhaustion (CVD delta decelerating, lack of volume follow-through).
- **Execution**: Counter-trend passive limit order targeting mean reversion back toward Volume POC or Session VWAP.

#### Model 2: VWAP & Structural Trend Pullback
- **Condition**: In-range statistical score ($|Z_{\text{VWAP}}| < 2.0\text{ SD}$, typically $0.2\text{ SD}$ to $1.7\text{ SD}$) within a confirmed HTF trend.
- **Required Confluence**:
  1. Primary trend confirmed by HTF EMA hierarchy and directional multi-horizon CVD.
  2. Pullback retraces into a confirmed structural shelf:
     - 20 EMA / 50 EMA shelf.
     - Volume Profile Value Area edge (VAL in uptrend, VAH in downtrend).
     - **Daily VWAP +1.0D / -1.0D Band coincidence with persistent whale orders**.
- **Execution**: Pro-trend passive limit order placed at the shelf, targeting cascade momentum into the next structural magnet.

#### Mandatory Wake-Up Candidate Identification Protocol (Passive Limit Orders)
- **Active Scanning Mandate**: On EVERY wake-up cycle and autonomous turn, the coordinator, all dispatched subagents (`Orderflow Analyst`, `Position Manager`, `Macro Risk Analyst`), and the external council models are **strictly mandated to actively scan the 24 mutual assets and the 93-asset screener to discover, qualify, and formulate explicit passive limit order candidates**.
- **Execution Readiness**: Do not remain passive when valid setups exist. Whenever portfolio capacity permits (up to 4 tickets total across orthogonal asset clusters: Crypto, Metals, Energy, Forex, Indices), actively identify and stage:
  1. **Model 1 Extreme Mean Reversion Limits**: Staged at outer shelves (|Z| >= 2.0 to 3.5 SD in verified `MEAN_REVERT` regimes) with confirmed tape exhaustion and un-swept resting whale shelters.
  2. **Model 2 Trend Pullback Limits**: Staged at 20/50 EMA, VAH/VAL, or Session VWAP shelves in verified `TREND_UP` or `TREND_DOWN` regimes, defended by resting whale bunkers outside opposing sweep bands.
- **Complete Order Specification**: Every identified candidate must be fully parameterized: Symbol, Order Type (`BUY_LIMIT` / `SELL_LIMIT`), Entry Price (shelf-anchored, accounting for half-spread), Stop Loss (safely bunkered behind whale wall with >= 0.35–0.50 ATR clearance), Take Profit (front-running magnet by 5–10 bps), Lot Size (calibrated to $15.00–$25.00 USD risk envelope), and Stressed Floor Cushion check (>= 4,775.00 USD hard floor).

---

### STEP 6: Microstructure Coincidence Stack & On-Chain Intelligence
*Active Skills: `@[data-analyst]`, `@[quant-analyst]`*

Every candidate setup must achieve simultaneous confluence across the multi-pillar microstructure stack:

1. **L2 Orderbook Depth Asymmetry**:
   - Top-20 depth must heavily support the trade direction:
     $$\text{Imbalance} = \frac{\text{Bid Depth} - \text{Ask Depth}}{\text{Bid Depth} + \text{Ask Depth}}$$
   - For Longs: Bid Depth > Ask Depth (Imbalance $> +0.25$).
   - For Shorts: Ask Depth > Bid Depth (Imbalance $< -0.25$).
2. **L3 Attributed Whale Wall Backing & Anti-Spoof Persistence Gate**:
   - Order must be shielded by genuine on-chain/L3 whale orders (`0x...`).
   - **Strict Persistence Contract (Non-Bypassable)**:
     * `persistence_status == "SAMPLED_RECURRENCE_VERIFIED"`
     * `persist_s >= 180.0\text{ seconds}`
     * `presence_frac >= 0.85`
     * `gate_g7_eligible == True`
     * **Reject All Unverified Walls**: Any wall showing `persist_s == 0.0` or `SINGLE_SAMPLE` is classified as potential spoof liquidity and rejected fail-closed.
   - Minimum Notional: $\ge 5,000,000\text{ USD}$ for BTC/ETH; $\ge 1,000,000\text{ USD}$ for TradFi (Gold, Indices, Oil); $\ge 500,000\text{ USD}$ for FX and Altcoins.
3. **Multi-Horizon CVD Directional Taker Flow**:
   - Inspect 1m, 15m, Session, and Weekly cumulative volume delta.
   - Strong alignment: Massive negative CVD (-10M to -100M+ USD) confirms short dominance; massive positive CVD confirms buyer aggression.
4. **Arkham Intelligence On-Chain Institutional Forensics (`onchain_arkham_intelligence`)**:
   - Telemetry directly embeds the live Arkham on-chain feed harvested via Chrome CDP into `docs/telemetry/live_snapshot_latest.json`, granting all downstream agents (Arena, Copilot Studio, Ox Alpha) full on-chain visibility via Git without requiring browser access.
   - **Data Schema & Core Fields**:
     * `market_flow_sentiment`: Global macro flow tag (`NET_ACCUMULATION (BULLISH_FLOW)`, `NET_DISTRIBUTION (BEARISH_FLOW)`, or `NEUTRAL_BALANCED_FLOW`).
     * `aggregate_metrics`:
       - `total_transfers_monitored`: Sample transfer volume.
       - `exchange_inflow_events` & `total_inflow_volume_usd`: Institutional deposits to CEXs (Binance, OKX, Bybit, Coinbase, Kraken, etc.). Direct proxy for impending sell pressure / dumping.
       - `exchange_outflow_events` & `total_outflow_volume_usd`: Institutional withdrawals from CEXs to cold storage / self-custody. Direct proxy for spot accumulation.
       - `net_flow_usd`: Calculated as `total_outflow_volume_usd - total_inflow_volume_usd`. Positive = Net Accumulation; Negative = Net Distribution.
       - `market_maker_events`: Flow to/from top liquidity providers (Wintermute, Jump, GSR, Cumberland, FalconX, DWF Labs).
     * `asset_breakdown`: Per-asset flow mapping for `BTC`, `ETH`, `SOL`, `USDT`, and `USDC` (`inflow_usd`, `outflow_usd`, `tx_count`, and `sentiment`). Also mapped into `assets_matrix_24[symbol].arkham_onchain`.
     * `trending_institutional_entities`: Live balances, 24h change, largest asset, and active wallet counts for tracked institutions (e.g. MicroStrategy, Kraken, MEXC, Drift Protocol, Vitalik Buterin, Purpose Bitcoin ETF).
     * `whale_alerts`: Real-time transaction alerts for individual on-chain transfers $\ge 50,000\text{ USD}$ with counterparty deanonymization (`from_entity`, `to_entity`, `token`, `usd_value`, `tx_hash`).
   - **Decision Rules for Arkham On-Chain Flow**:
     * *Long Confirmation*: `market_flow_sentiment == NET_ACCUMULATION` AND `asset_breakdown[asset].outflow_usd > inflow_usd`. Confirms smart money spot absorption.
     * *Short Confirmation*: `market_flow_sentiment == NET_DISTRIBUTION` AND `asset_breakdown[asset].inflow_usd > outflow_usd`. Confirms institutional exchange deposits / inventory dumping.
     * *Stablecoin Mint / Whale Inflow Alert*: Significant USDT/USDC deposits from Treasury/Whales to CEXs flag imminent liquidity surges. Do not stage limit orders against the incoming flow.

---

### STEP 7: Liquidation & Stop Magnet Dynamics (Absorption vs. Blow-Through)
*Active Skills: `@[brainstorm]`, `@[data-analyst]`, `@[market-microstructure]`*

Reconstructed liquidation bands and dense structural stop clusters serve two critical functions:

```
        DEFENSIVE USE (BUNKER)                    OFFENSIVE USE (MAGNET)
┌───────────────────────────────────────┐ ┌───────────────────────────────────────┐
│ Place SL strictly outside outer       │ │ Use opposing liquidation band /       │
│ boundary [min_price, max_price] with  │ │ stop cluster as high-probability      │
│ >= 0.50 ATR + half_spread buffer.     │ │ TARGET MAGNET. Ride cascade momentum! │
│ Defends position against wick flushes.│ │ Front-run target by 5-10 bps.         │
└───────────────────────────────────────┘ └───────────────────────────────────────┘
```

#### 1. Significant Notional Filter (Eliminating Ladder Noise):
To resolve the "continuous ladder impossibility" where every 10 points contains tiny orders:
- **Significant Clusters**: Only clusters meeting institutional notional thresholds count as valid defensive bunkers or offensive TP magnets:
  * **BTC & ETH**: $\ge 5,000,000\text{ USD}$ (Intraday micro-clusters $\ge 1,000,000\text{ USD}$)
  * **TradFi CFDs (Gold, SP500, NAS100, USWTI)**: $\ge 1,000,000\text{ USD}$
  * **Forex & Altcoins**: $\ge 500,000\text{ USD}$
- **Noise Filter**: All clusters $< 50,000\text{ USD}$ are classified as retail noise and ignored for bunker clearance.

#### 2. Canonical Mathematical Bunker Formula (Non-Ambiguous):
Stop Losses must NEVER be measured from `mid_price`. They are strictly calculated from the outer boundary:
$$\text{SL}_{\text{short}} = \max(\text{max\_price}_{\text{nearest\_buy\_stops}}, \text{max\_price}_{\text{short\_squeeze\_band}}, \text{price}_{\text{defending\_ask\_wall}}) + 0.50 \times \text{ATR} + \text{half\_spread}$$
$$\text{SL}_{\text{long}} = \min(\text{min\_price}_{\text{nearest\_sell\_stops}}, \text{min\_price}_{\text{long\_cascade\_band}}, \text{price}_{\text{defending\_bid\_wall}}) - 0.50 \times \text{ATR} - \text{half\_spread}$$

#### 3. Quantified Absorption vs. Trend Blow-Through Forensics:
When price approaches a significant cascade band, differentiate between absorption and continuation using 4 empirical metrics:

| Metric | Absorption / Reversal Protocol | Trend Blow-Through Protocol |
|:---|:---|:---|
| **1. CVD Acceleration** | CVD second derivative $d^2(\text{CVD})/dt^2 < 0$ and $15\text{m}$ delta decelerating $> 30\%$ | CVD accelerates exponentially through the band ($d^2(\text{CVD})/dt^2 > 0$) |
| **2. L2 Book Replenishment** | Opposing depth replenishes $\ge 80\%$ within 2 seconds of the sweep | Orderbook remains hollowed out ($< 30\%$ replenishment); depth vanishes |
| **3. Arkham Net Flow** | Net on-chain flow shows counter-trend divergence $> 500,000\text{ USD}$ in trailing 1h | Institutional wallet flow continues aggressively in direction of cascade |
| **4. Structural Auction Location** | Band sits at statistical extreme ($|Z| \ge 2.5\text{ SD}$, HTF POC/VAH/VAL shelf) | Band sits in the middle of a fresh HTF breakout channel with open space |

- **If Absorption Confirmed**: Trade Model 1 counter-trend mean reversion with tight bunker SL.
- **If Blow-Through Confirmed**: Trade Model 2 pro-trend continuation, riding momentum into the *next* distal cascade band.

---

### STEP 8: Mathematical Risk Budget & Capital Floor Gate
*Active Skills: `@[quant-analyst]`, `@[risk-engine]`, `@[clean-code]`*

Every staged order must undergo strict broker-specific contract sizing and capital defense auditing:

1. **Broker Contract Math**:
   - Calculate cash risk precisely using broker parameters:
     $$\text{Cash Risk (USD)} = \text{Volume} \times \text{Contract Size} \times |\text{Entry} - \text{SL}| \times \text{Quote Conversion}$$
   - Verify calculation directly via `mt5.order_calc_profit()`.
2. **Expanded Operational Risk Envelope (Explicit Operator Authorization)**:
   - **Operator Directive**: The operator has explicitly granted full authorization to expand the stop loss dollar budget to capture more trades and prevent choked stops.
   - **Unified Risk Envelope across all assets (Crypto, Metals, FX, Energy, Indices)**: Authorized up to **15.00 USD to 25.00 USD** (0.30% to 0.51% of equity).
   - **Mandatory Rationale & Invariant A Enforcement**: Stops must NEVER be choked or compressed inside market sweep zones to satisfy a rigid sub-15 USD cap. Stops MUST anchor safely behind genuine resting institutional whale walls (`persist >= 180s`) with a 0.35–0.50 ATR structural buffer. If placing the stop behind the true bunker requires 18.00 to 25.00 USD risk on minimum lots (e.g. on USDJPY, BTC, Gold, Indices), that risk is fully authorized.
3. **Stressed Floor Defense (Unconditional Invariant)**:
   - Stressed post-loss simulation across all active positions and staged pending orders:
     $$\text{Total Staged Risk} = \sum_{i} \text{Risk}_i$$
     $$\text{Stressed Equity} = \text{Current Equity} - \sum_{i} (\text{Risk}_i \times 1.25 + 2.00) \ge 4,795.00\text{ USD}$$
   - Under no circumstances may an order be staged if Stressed Equity violates the 4,795.00 USD operating buffer (and 4,775.00 USD hard floor). With equity at 4,857.32 USD (+82.32 USD above hard floor), a 20.00 to 25.00 USD risk trade is safely supported (+29.07 USD surplus above buffer, +49.07 USD above floor).
4. **Unified Dynamic Position Capacity Formula**:
   - **At 25.00 USD cash risk**: Each slot incurs $25.00 \times 1.25 + 2.00 = 33.25\text{ USD}$ stressed risk.
     $$\text{Max Slots} = \lfloor \frac{68.74}{33.25} \rfloor = \mathbf{2\text{ concurrent positions}}$$
     (Consumes 66.50 USD stressed risk, preserving a +2.24 USD buffer surplus and +22.24 USD hard floor surplus).
   - **At 15.00 USD cash risk**: Each slot incurs $15.00 \times 1.25 + 2.00 = 20.75\text{ USD}$ stressed risk.
     $$\text{Max Slots} = \lfloor \frac{68.74}{20.75} \rfloor = \mathbf{3\text{ concurrent positions}}$$
     (Consumes 62.25 USD stressed risk, preserving a +6.49 USD buffer surplus and +26.49 USD hard floor surplus).
   - **4 concurrent positions**: Mathematically permitted ONLY when equity expands above $4,878.00\text{ USD}$ ($4,795.00 + 4 \times 20.75\text{ USD}$). Under current equity, any attempt to stage 4 positions is hard-blocked fail-closed.

---

### STEP 9: Pre-Execution Ex-Ante Audit
*Active Skills: `@[verify]`, `@[clean-code]`*

Prior to order transmission, perform the final 5-point sanity audit:
1. **Passive Limit Posture**: Confirm order type is strictly `BUY_LIMIT` or `SELL_LIMIT`. Market orders and spread-crossing taker executions are permanently banned.
2. **Reward-to-Risk (R:R) Gate**:
   $$\text{R:R Ratio} = \frac{|\text{TP} - \text{Entry}|}{|\text{Entry} - \text{SL}|} \ge 2.0\text{R}$$
   (Default target is 2.5R to 3.0R).
3. **Bunker Stop Verification**: SL is positioned safely beyond the outer boundary of the resting whale wall and liquidation band with $\ge 0.50\text{ ATR}$ safety margin.
4. **Target Magnet Front-Run**: TP is set 5 to 10 bps ahead of the opposing structural cluster or liquidation band to guarantee fill liquidity before depletion.
5. **Filling Policy Compatibility**: Test `ORDER_FILLING_IOC`, with automatic failover to `ORDER_FILLING_RETURN` / `ORDER_FILLING_FOK` if rejected by broker bridge.

---

### STEP 10: Autonomous Punch & Dynamic Ratchet Lifecycle
*Active Skills: `@[quant-analyst]`*

Once verified, the order is transmitted autonomously into MetaTrader 5 without operator hesitation:

```mermaid
stateDiagram-v2
    [*] --> PendingLimitOrder: Punch Limit Order into MT5
    PendingLimitOrder --> FilledPosition: Price fills at limit
    PendingLimitOrder --> Cancelled: Distance > 2.0 ATR or Whale pulls
    
    FilledPosition --> Phase0RiskCut: Profit reaches +1.25R0
    note right of Phase0RiskCut: Move SL to -0.25R0 (Cut 75% risk)
    
    Phase0RiskCut --> Phase1ProfitLock: Profit reaches +1.65R0
    note right of Phase1ProfitLock: Move SL to +0.80R0 (Bank profit)
    
    Phase1ProfitLock --> Phase2Trailing: Profit reaches >= +2.00R0
    note right of Phase2Trailing: Continuous 0.50 ATR trail behind micro-shelves
    
    Phase2Trailing --> TakeProfitExit: Hit TP Magnet (+2.5R to +3.0R)
    FilledPosition --> TimeDecayExit: Time > 24 bars (6h) & gain < +0.20R0
    FilledPosition --> StoppedOut: Hit initial SL (Controlled risk)
```

1. **Autonomous Execution**: Execute via `mt5.order_send()` with unique magic number (`888888`) and descriptive comment.
2. **Dynamic Profit Ratchet Protocol (Frozen $R_0$)**:
   - **Phase Early-BE (Adaptive Microstructure Breakeven — Mandated by Forensic Autopsy)**: At $+0.75R_0$ to $+0.80R_0$ unrealized profit once price reclaims the session Volume Profile POC or VWAP $\to$ Move SL to $\text{Entry} + 0.10R_0$ (eliminates 100% of risk and guarantees zero-loss protection, preventing the 76.9% positive MFE from ever turning into a full stop-out).
   - **Phase 0 (Risk Cut)**: At $+1.25R_0$ unrealized profit $\to$ Move SL to $\text{Entry} + 0.15R_0$ (locks in minor profit + broker commission buffer).
   - **Phase 1 (Profit Lock)**: At $+1.65R_0$ unrealized profit $\to$ Move SL to $\text{Entry} + 0.80R_0$ (locks in guaranteed major profit).
   - **Phase 2 (Continuous Trailing Ratchet)**: At $\ge +2.00R_0$ unrealized profit $\to$ Trail SL behind structural 15m swing shelves or $0.50\text{ ATR}$ trailing stop.
3. **Time-Decay Exit**: If a position has been active for 24 bars (6 hours) and has not generated at least $+0.20R_0$ gain, close at market to redeploy capital.

---

## SECTION 3: 40-SHEET INSTITUTIONAL EXCEL DATA MATRIX DECISION SYNTHESIS PROTOCOL
### Operationalizing the 209,597-Cell Quantitative Data Warehouse in `DataBase_Trading.xlsx`

> **Data Warehouse Status**: 40 LIVE PRODUCTION WORKSHEETS | 209,597 CELLS | ZERO FORMULA ERRORS  
> **Master File Location**: `Data/DataBase_Trading.xlsx`  
> **Refresh Latency**: 15.42 Seconds End-to-End Ingestion & Serialization  
> **Core Mandate**: Every trading decision, macro hypothesis, and order staging must systematically cross-reference and weight the 4 functional data clusters below before capital commitment.

```mermaid
flowchart TD
    subgraph DataWarehouse ["DataBase_Trading.xlsx (40 Sheets)"]
        CA["Cluster A: Global Macro & System Defense<br/>(Sheets 21-28, 31, 37, 38)"]
        CB["Cluster B: Microstructure, Depth & Orderflow<br/>(Sheets 1-15, 20, 21, 32, 33)"]
        CC["Cluster C: On-Chain Whales & Liquidations<br/>(Sheets 16-19, 22, 34-36)"]
        CD["Cluster D: Brokerage & Cognitive Councils<br/>(Sheets 39, 40)"]
    end

    subgraph DecisionWorkflow ["4-Stage Institutional Synthesis Workflow"]
        Stage1["Stage 1: Macro Regime & Event Defense Gate<br/>(FOMC Blackout, FNG Index, Central Bank Rates, DVOL Term Structure)"]
        Stage2["Stage 2: Universe Screening & Dual-Engine Dialectic<br/>(Spread Gate, VWAP Z-Score, HTF Auction, Basis Spreads)"]
        Stage3["Stage 3: On-Chain Whales & Bunker Entry Confluence<br/>(Arkham 100K+ Transfers, Whale Orders >=100K, Hyperdash Flow, L2/L3 Walls)"]
        Stage4["Stage 4: Risk Sizing, Floor Defense & Council Ratification<br/>(MT5 Cash Risk, Stressed Equity >= $4,795, Gemini/Heretic/Arena Consensus)"]
    end

    CA --> Stage1
    Stage1 --> Stage2
    CB --> Stage2
    Stage2 --> Stage3
    CC --> Stage3
    Stage3 --> Stage4
    CD --> Stage4
    Stage4 --> MT5Execution["Autonomous Limit Order Punch in MetaTrader 5"]
```

---

### PART 3.1: THE 4 FUNCTIONAL EXCEL DATA CLUSTERS & MAPPING

#### 1. Cluster A: Global Macro Regime, Event Defense & Corporate Anchors (Sheets 21–28, 31, 37, 38)
- **`Telemetry_System_State` (Sheet 31)**:
  - System protocol (`omni.telemetry.v3`), MT5 account balance ($4,863.74), equity ($4,863.74), hard floor ($4,775.00), live floor cushion (**+$88.74**), 4 joint capacity slots.
  - Clopper-Pearson 95% one-sided binomial lower confidence bound (`p_win >= 0.4197`) across 17 calibration trades (11 wins).
  - Macro Calendar FOMC proximity (252.26 hours runway to hard blackout), Crypto Fear & Greed index (`53` Neutral), institutional ETF netflows (-$82.40M BTC / -$69.70M ETH), and Coinbase spot premium (-14.36 bps).
- **`Volatility_Sentiment` (Sheet 38)**:
  - Table 1 (Alternative.me Crypto Fear & Greed Index): 30 daily historical records (53 to 78) mapping sentiment extremes (`Extreme Accumulation` vs `Extreme Greed`).
  - Table 2 (Deribit BTC DVOL): 30 daily forward implied volatility records (Close IV: 37.93%, Implied Daily Move: 1.99%).
  - Table 3 (Deribit ETH DVOL): 30 daily forward implied volatility records (Close IV: 52.22%, Implied Daily Move: 2.73%, exhibiting a +14.29% persistent volatility risk premium over BTC).
- **`FF_Economic_Calendar` (Sheet 23)**:
  - 38 scheduled weekly macro releases categorized by impact (High/Medium/Low) with exact UTC release times, currencies, forecasts, and previous prints.
- **`FF_News_Latest`, `FF_News_Fundamental`, `FF_News_Technical` (Sheets 24, 25, 26)**:
  - 60 curated articles with complete body summaries, publisher URLs, and technical chart setups covering central bank policy statements (Fed, BoJ, BoE, ECB), energy shocks, and geopolitics.
- **`Bitcoin_Treasuries` (Sheet 37)**:
  - 60 publicly listed corporate balance sheet holdings (Strategy / MicroStrategy: 848,000 BTC, Metaplanet, XXI, MARA, Coinbase, Tesla, etc.) totaling 1,265,370 BTC ($104.77B USD), plus the 124-row historical purchasing ledger from 2020 to 2026.
- **`ETF_Overview`, `Spot_ETF_Net_Inflow`, `Spot_ETF_Net_Inflow_Graph` (Sheets 1, 2, 3)**:
  - 44 institutional spot ETFs across BTC, ETH, SOL, XRP, and HYPE with daily inflows/outflows, cumulative flows, and AUM across 11 major sponsors (BlackRock IBIT, Fidelity FBTC, Grayscale, Bitwise, VanEck, etc.).

#### 2. Cluster B: Microstructure, Orderbook Depth & Orderflow Confluence (Sheets 4–15, 20, 21, 32, 33)
- **`Live_Orderbook_CVD_Depth` (Sheet 32)**:
  - Matrix across all 24 institutional assets (14 Crypto, 4 Indices, 3 Commodities, 3 Forex): Real-time tick Bid, Ask, Spread (points and bps), Binance Mid, Hyperliquid Mid, Top-20 Bid Depth USD, Top-20 Ask Depth USD, Book Imbalance %, Skew Ratio, Session CVD USD, 24h CVD USD, and 15m Bar Delta USD.
- **`Exchange_Basis_Spreads` (Sheet 33)**:
  - Multi-exchange pricing across all 24 assets: Mark Price, Index Price, Basis Premium/Discount (bps), Last Funding Rate (bps), Annualized Funding %, Trend Regime, RSI (14), ATR (14) in points and %, EMA (20), EMA (50), EMA (200), VWAP Z-Score, and Whale Imbalance Rho.
- **`Whales_Orders` (Sheet 20)**:
  - 520 resting institutional whale orders across all 18 institutional perpetuals filtered strictly for notional >= $100K USD at 15m timeframe, with canceled orders excluded.
- **`Spot_Netflow` (Sheet 21)**:
  - 740 assets across 13 timeframes (5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 24h, 3d, 7d, 30d) displaying dynamic green accumulation (#D4EDDA) and red distribution (#F8D7DA) heatmaps.
- **`Funding_Rates` & `Funding_Fees` (Sheets 4, 5)**:
  - Cross-venue funding rates and fees across 12 exchanges identifying overcrowded retail positioning.
- **`Open_Interest` Suite (Sheets 10, 11, 12, 13, 14, 15)**:
  - 387 exchange breakdown rows across 19 assets, top OI gainers/losers, and multi-timeframe OI charts (15M, 1H, 4H) diagnosing aggressive positioning vs deleveraging.

#### 3. Cluster C: On-Chain Whale Conviction & Liquidation Dynamics (Sheets 16–19, 22, 34–36)
- **`Arkham_Transfers_100K` (Sheet 35)**:
  - 138 live on-chain whale transfers >= $100,000 USD harvested via Chrome CDP across Base, Optimism, Polygon, BNB Chain, Tron, and Solana. 100% full 42-character EVM addresses, 34-character Tron addresses, and full 66-character transaction hashes (zero truncation, zero ellipsis).
- **`Arkham_Whales_Holdings` (Sheet 36)**:
  - 48 tracked institutional whale entities (BlackRock $49.32B, Strategy $38.96B, Wintermute $195.08M, VanEck $1.43B, ARK Invest $2.60B, Jump Crypto $450M, etc.) controlling $402.16B in on-chain assets.
- **`Hyperdash_Flow_Feed` (Sheet 34)**:
  - 273 rows across 4 sections: Flow summary KPIs, 50 real-time whale trades with full 42-char addresses, 50 confirmed liquidations with directional market impact (`SELL_PRESSURE` / `BUY_PRESSURE`), and 158-asset universe liquidation profile.
- **`Hyperliquid_Whales` (Sheet 22)**:
  - 1,922 active whale positions across 39 pages with 100% full 42-character addresses, unrealized PnL, leverage, entry price, and mark price.
- **`liquidation_maxpain_1D/2D` & `Exchange_Liquidation_Map_1D/7D` (Sheets 16, 17, 18, 19)**:
  - Multi-exchange liquidation surfaces mapping dense short-squeeze and long-liquidation cascade pools across 18 perpetuals.

#### 4. Cluster D: Execution Brokerage & Multi-Model Cognitive Councils (Sheets 38, 39)
- **`MT5_Live_Quotes_Account` (Sheet 38)**:
  - Live Blueberry Markets broker ledger ($4,863.74 balance/equity, +$88.74 hard floor cushion, +$68.74 buffer cushion) and live interbank tick bid/ask quotes, spreads, digits, and contract specifications for all 24 symbols.
- **`Cognitive_Council_Telemetry` (Sheet 39)**:
  - Real-time operational status of Google Gemini Web2API (port 8081, 11 models, HTTP 200 OK), Heretic Engine Daemon (port 8083, v2.0.0.dev0, HTTP 200 OK), Arena.ai consensus, Autonomous Telemetry Git Sync Daemon (60s cadence), AST Knowledge Graph Watcher (7.4k nodes), and Tier-2 Swarm Cron.

---

### PART 3.2: THE 4-STAGE INSTITUTIONAL SYNTHESIS WORKFLOW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: MACRO REGIME & EVENT DEFENSE GATE (CLUSTER A)                      │
│ 1. Check FF_Economic_Calendar & Telemetry_System_State: Is FOMC or Tier-1   │
│    release within the mandatory hard blackout window (< 1.0 hour)?          │
│    -> If YES: Stand aside unconditionally across all 24 assets.             │
│    -> FOMC Runway: 252.77 hours runway to hard blackout.                    │
│ 2. Check Volatility_Sentiment & Alternative.me FNG:                         │
│    -> FNG <= 25: Extreme Accumulation Regime (Favor Long Mean Reversions).  │
│    -> FNG >= 75: Extreme Greed / Risk-Off (Favor Overhead Shorts).          │
│    -> Compare Deribit DVOL IV (BTC vs ETH): ETH IV exhibits a +14.29 IV pt  │
│       absolute (+37.67% relative) risk premium, mandating wider buffers.    │
│ 3. Check Spot_ETF_Net_Inflow & Bitcoin_Treasuries (Sheet 36):               │
│    -> Cumulative institutional inflows (+716k BTC) and $104.71B public     │
│       treasury holdings confirm underlying sovereign accumulation.          │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 2: UNIVERSE SCREENING & DUAL-ENGINE DIALECTIC (CLUSTER B)             │
│ 1. Strict Spread Friction Gate (Live_Orderbook_CVD_Depth):                  │
│    -> Crypto perps must have MT5 Spread <= 25.0 bps (BTC 1.96, ETH 11.6,    │
│       BNB 8.33, BCH 20.95 bps pass; wide altcoins like DOGE 264 bps fail).   │
│    -> TradFi CFDs must have MT5 Spread <= 5.0 bps (SP500 1.14, NAS100 0.49, │
│       DJ30 0.39, GER40 0.31, Gold 1.06, USWTI 3.0 bps pass).                │
│    -> Wide spread assets are disqualified automatically to prevent slippage.│
│ 2. Statistical Regime Assignment (Exchange_Basis_Spreads):                  │
│    -> Model 1 (Extreme Mean Reversion): |Z_VWAP| >= 2.0 to 3.5 SD in        │
│       confirmed MEAN_REVERT regime with tape exhaustion & trapped traders.  │
│    -> Model 2 (Structural Trend Pullback): |Z_VWAP| < 2.0 SD (0.2 to 1.7 SD)│
│       in confirmed TREND_UP / TREND_DOWN regime retracing to 20/50 EMA shelf│
│    -> If Regime is UNDEFINED: Stand aside unconditionally.                  │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 3: BIFURCATED LIQUIDITY & BUNKER ENTRY CONFLUENCE (CLUSTER C)         │
│ STAGE 3A: Crypto Perpetuals (BTC, ETH, SOL, BNB, XRP, BCH, etc.):          │
│ 1. Arkham Whale Validation (Arkham_Transfers_100K & Arkham_Whales_Holdings):│
│    -> Cross-reference with 48 institutional whale entities ($402.16B).      │
│    -> MicroStrategy: $38.96B on-chain custody / 848k BTC balance sheet.     │
│ 2. Hyperdash Flow Feed (Hyperdash_Flow_Feed):                               │
│    -> Directional whale trades & confirmed liquidation pressure confirmation│
│ 3. Resting Whale Bunker Shelter (Whales_Orders >= $100K):                   │
│    -> Limit order sheltered behind verified resting whale wall (persist>=180s)
│       with a 0.50 ATR structural buffer.                            │
│                                                                             │
│ STAGE 3B: TradFi Instruments (Indices, Commodities, Forex Majors):          │
│ 1. Interbank Tick Spread & Session Liquidity Gate:                          │
│    -> Active session spread <= 5.0 bps. Stand aside during 21:30-22:30 UTC  │
│       interbank rollover spread expansion.                                  │
│ 2. Forex Factory Economic Calendar & Breaking Intelligence Filter:          │
│    -> Zero Tier-1 releases within 60 minutes for base/quote currency.       │
│ 3. Structural Auction Shelf Defense (Live_Orderbook_CVD_Depth):             │
│    -> Limit entry sheltered behind verified L2 top-of-book depth cluster    │
│       with mandatory 0.50 ATR structural buffer.                    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 4: RISK SIZING, FLOOR DEFENSE & COUNCIL RATIFICATION (CLUSTER D)      │
│ 1. Exact Cash Risk Sizing: Calculate risk via mt5.order_calc_profit().      │
│    -> Authorized Envelope: 15.00 to 25.00 USD (0.30% to 0.51% equity).      │
│ 2. Unified Stressed Floor Defense Gate:                                     │
│    -> Stressed Equity = Current Equity - sum(Risk_i * 1.25 + 2.00) >= $4,795 │
│    -> Maximum 2 slots at $25.00 risk ($66.50 stressed <= $68.74 buffer).    │
│    -> Maximum 3 slots at $15.00 risk ($62.25 stressed <= $68.74 buffer).    │
│    -> 4 slots require equity expansion above $4,878.00 USD.                 │
│ 3. Cognitive Council Consensus (Cognitive_Council_Telemetry):               │
│    -> Ratify trade through Gemini Web2API (8081), Heretic (8083), and Arena.│
│    -> Autonomous limit order punch via MT5 Execution Bridge (magic: 888888).│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SECTION 4: INSTITUTIONAL BENCHMARK & ACCOUNTABILITY CONTRACT

1. **Benchmark Comparison**: All desk performance, equity metrics, and Sharpe ratios must be continuously benchmarked against the **BTC Buy and Hold** benchmark normalized to initial capital ($5,000 USD).
2. **Immutable Audit Provenance**: Every trade decision, council debate, and execution log must be recorded in:
   - `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md`
   - `.agents/memory/session_chat_history.md`
   - Telemetry snapshots pushed to Git repository (`main` branch) every 60 seconds.
3. **Zero-Litter Discipline**: All scratch scripts and exploratory debug artifacts must be immediately purged upon validation.

---

## SECTION 5: FULL EMBEDDED SKILL HANDBOOKS & EXECUTION PROTOCOLS
> **Self-Contained Operating Handbooks**: To ensure models without local skill repositories (external AIs, sandboxed instances, or remote auditors) execute with 100% fidelity, the complete operational instructions, constraints, and methodologies for all 8 foundational skills are embedded below directly.

```mermaid
flowchart LR
    subgraph SocraticSkills ["Discovery & Synthesis"]
        SK1["Skill 1: /brainstorm<br/>Socratic Gate & Dialectic"]
        SK2["Skill 2: /graphify<br/>AST Semantic Graph Traversal"]
        SK3["Skill 3: /remember<br/>Persistent Trajectory & Anti-Amnesia"]
    end
    subgraph DataSkills ["Engineering & Diagnostics"]
        SK4["Skill 4: /data-analyst<br/>Orderflow & Auction Profiling"]
        SK5["Skill 5: /data-engineer<br/>Data Contracts & Monotonicity"]
        SK6["Skill 6: /dataform-bigquery<br/>Time-Series Modeling & Partitioning"]
        SK7["Skill 7: /data-driven-feature<br/>Statistical Power & Feature Rigor"]
    end
    subgraph ExecutionSkills ["Verification & Risk"]
        SK8["Skill 8: /verify & test-guard<br/>Ex-Ante Pre-Execution Gate"]
    end
    SocraticSkills --> DataSkills --> ExecutionSkills
```

---

### SKILL 1: `/brainstorm` (Socratic Gate & Multi-Perspective Adversarial Trade Debate)
*Source: `.agents/skills/brainstorming/SKILL.md`*

#### 1. Purpose & Core Mandate
The `/brainstorm` protocol enforces structured dialectic reasoning and prevents premature execution, confirmation bias, or single-agent echo chambers. It guarantees that any trade hypothesis is stress-tested against counter-hypotheses before capital is committed.

#### 2. The Socratic Gate (Mandatory Rules)
Before any order proposal is ratified:
1. **The 3 Mandatory Pre-Flight Questions**:
   - **Target Problem / Edge**: What exact structural inefficiency or orderflow imbalance is being exploited? (e.g. resting whale absorption vs exhausted taker cascade).
   - **Adverse Scenarios**: What happens if the resting whale wall pulls, cancels, or is eaten in a violent blow-through? Where is the invalidation point?
   - **Boundary & Capacity Constraints**: Does this order respect the hard floor ($4,775.00 USD), the $10.00–$14.50 USD risk envelope, and the 4-position capacity limit?
2. **Dynamic Questioning Principles**:
   - Never use static or boilerplate affirmations.
   - Every question must connect directly to an empirical risk or execution consequence.
   - Questions must systematically eliminate invalid implementation paths.

#### 3. 3-Persona Adversarial Debate Protocol
Every trade setup must be evaluated through three distinct adversarial viewpoints:
- **Persona A (The Aggressive Orderflow Specialist)**:
  - Advocates for the setup based on micro-level tape data: CVD delta deceleration, footprint absorption, resting L2/L3 whale walls, and basis-mapped stop sweeps.
- **Persona B (The Skeptical Macro & Regime Risk Officer)**:
  - Challenges the setup: Inspects higher-timeframe EMA alignment (Price vs EMA20/EMA50/EMA200), upcoming Tier-1 macro catalysts, interbank FX rollover spread widening (21:30–22:30 UTC), and cross-asset correlation shocks.
- **Persona C (The Forensic Position & Friction Auditor)**:
  - Audits broker friction and execution math: Evaluates spread in bps, calculates tick slippage, tests IOC vs RETURN filling policies, verifies `mt5.order_calc_profit` cash risk, and computes post-loss stressed floor cushion.
- **Ratification Threshold**: A trade is approved ONLY if Persona A's edge withstands the critiques of Persona B and Persona C with verifiable empirical evidence.

---

### SKILL 2: `/graphify` (AST Knowledge Graph & Structural Architecture Traversal)
*Source: `.agents/rules/graphify.md`*

#### 1. Purpose & Knowledge Base Structure
`graphify` provides instant AST-level semantic navigation of the codebase (`graphify-out/graph.json`, comprising 7,400+ nodes and dependencies) without loading entire multi-thousand-line source files into context windows, preventing token exhaustion and hallucination.

#### 2. Core Execution Protocols & Commands
- **`graphify query "<question>"`**:
  - Queries scoped subgraphs for specific symbols, function contracts, risk constants, or execution routes.
  - Example: `graphify query "order_calc_profit"` or `graphify query "bunker stop formula"`.
- **`graphify path "<Node_A>" "<Node_B>"`**:
  - Finds the shortest dependency path between two components (e.g. from `generate_telemetry_snapshot.py` to `OF_Strategy.py`).
- **`graphify explain "<concept>"`**:
  - Extracts focused architectural summaries and dependencies for classes, invariants, and pipelines.
- **Rules of Engagement**:
  - For architecture and code structure queries, always query the AST knowledge graph first.
  - After modifying any core logic or execution modules, run `graphify update .` to keep the semantic graph synchronized.

---

### SKILL 3: `/remember` & `agent-memory` (Persistent Cross-Session Knowledge Management)
*Source: `.agents/skills/agent-memory/SKILL.md`*

#### 1. Purpose & Anti-Amnesia Protocol
Maintains durable, persistent memory across AI coding sessions, multi-account Gemini handoffs, and external council rounds. Eliminates context amnesia, ensures past operator feedback is permanently respected, and prevents regression into previously identified failure modes.

#### 2. Architecture & File Hierarchy
- **Layer 1 (Semantic Graph Memory)**: `.agents/memory/graph/mcp_graph_memory.json`
- **Layer 2 (Roadmap & Milestones)**: `.agents/memory/SESSION_CONTEXT_MAP.md`
- **Layer 3 (Active Mission & Invariants Card)**: `.agents/rules/ACTIVE_CONTEXT.md`
- **Layer 4 (Immutable Session History)**: `.agents/memory/session_chat_history.md`

#### 3. Mandatory Behavioral Invariants
1. **Turn-0 Retrospective**: On every single turn, before analyzing data or modifying code, review previous conversation logs and active context to establish unbroken continuity.
2. **The Anti-Trap Memory Registry**: Never repeat an identified trap:
   - *Trap 1*: Placing limit entries directly above un-swept opposing stop clusters.
   - *Trap 2*: Buying falling knives into aggressive seller CVD cascades without absorption.
   - *Trap 3*: Measuring stop loss buffers from `mid_price` instead of the outer bunker boundary (`min_price` / `max_price`).
   - *Trap 4*: Staging orders backed by ephemeral/spoofed whale walls (`persist_s < 180s`).
   - *Trap 5*: Staging limit entries > 2.0 ATR away from current market price.
3. **Turn-Ending Append**: Append prompt, decisions, and execution outcomes to `session_chat_history.md` at the conclusion of every cycle.

---

### SKILL 4: `/data-analyst` (Advanced Orderflow, Distribution & Auction Dissection)
*Source: `.agents/skills/data-analyst/SKILL.md`*

#### 1. Purpose & Analytical Rigor
Transforms raw market streams into decision-ready econometric and orderflow intelligence. Decomposes multidimensional metrics with mathematical precision, identifies instrumentation caveats, and separates causal signals from statistical noise.

#### 2. Core Methodologies & Analysis Patterns
1. **Multi-Dimensional Metric Slicing**:
   - Always decompose metrics across multiple dimensions: Asset Class (Crypto vs TradFi), Timeframe (1m, 5m, 15m, 1h, 1d), Venue (Binance Futures vs Hyperdash vs Blueberry MT5).
   - Never rely on single aggregate metrics; aggregate stability often masks severe localized divergence.
2. **Spread Analysis in Basis Points**:
   $$\text{Spread (bps)} = \frac{\text{Ask} - \text{Bid}}{\text{Mid}} \times 10,000$$
   - Enforce hard eligibility gates: Crypto $\le 25.0\text{ bps}$, TradFi CFDs $\le 5.0\text{ bps}$.
3. **Auction Profile Dissection**:
   - Identify Point of Control (POC), Value Area High (VAH, 70% volume threshold), and Value Area Low (VAL).
   - Detect Virgin / Naked POCs that act as unvisited liquidity magnets.
4. **Cumulative Volume Delta (CVD) Forensics**:
   - Calculate multi-horizon CVD deltas (Session, Weekly, 24h, 15m).
   - Detect **Absorption**: Price makes a lower low but 15m CVD makes a higher low (passive limit buyers absorbing aggressive sellers).
   - Detect **Continuation / Blow-Through**: Price and CVD decline synchronously with accelerating negative velocity ($d^2(\text{CVD})/dt^2 < 0$), signaling that resting liquidity will be consumed without reversing.
5. **Data Caveat Verification**:
   - Verify instrumentation provenance before trusting any metric. Ensure taker volume excludes exchange wash-trading and that MT5 tick feeds reflect live broker quotes.

---

### SKILL 5: `/data-engineer` (Data Contract Enforcement, Pipeline Ingestion & Monotonicity)
*Source: `.agents/skills/data-engineer/SKILL.md`*

#### 1. Purpose & Pipeline Governance
Guarantees the structural integrity, latency, and reliability of the data pipeline feeding the trading desk. Governs data contracts, timestamp monotonicity, venue basis translation, and fail-closed error handling.

#### 2. Execution Standards & Protocols
1. **Data Contracts & SLA Enforcement**:
   - Telemetry snapshots (`docs/telemetry/live_snapshot_latest.json`) must be regenerated every 60 seconds with strict schema compliance.
   - Latency Gate: Reject snapshots with $\text{Age} > 180\text{ seconds}$.
2. **Monotonicity & Zero-Null Invariant**:
   - All historical and real-time candle series must exhibit strictly increasing timestamps ($t_i > t_{i-1}$).
   - Zero null, NaN, or infinite values permitted across Open, High, Low, Close, Volume, and CVD fields.
3. **Venue Basis Normalization**:
   - Map external Binance / Hyperdash orderbook feeds onto the broker MT5 execution grid:
     $$\text{MT5 Level} = \text{Venue Level} + \text{venue\_basis}$$
   - Prevents misaligned limit placement caused by cross-venue pricing discrepancies.
4. **Fail-Closed Architecture**:
   - If an upstream API (Binance, Arkham, MT5) returns corrupt payloads or connection errors, the data pipeline raises immediate alerts and freezes new order generation until data consistency is restored.

---

### SKILL 6: `/dataform-bigquery` (Institutional Time-Series Modeling & Scalability)
*Source: Modern BigQuery / Dataform Data Engineering Standards*

#### 1. Purpose & Architecture
Governs massive time-series modeling, table partitioning, clustering, and reproducible ELT transformations across 43 canonical Parquet datasets and 3,467,571 historical 15m bars.

#### 2. Time-Series Partitioning & Query Optimization
1. **Partition Pruning**:
   - In all analytical queries and backtests, always filter by partition columns (`_PARTITIONDATE`, `timestamp_utc`) first to prevent full table scans and eliminate execution latency.
2. **Clustering Strategy**:
   - Cluster datasets by `symbol`, `venue`, and `regime_id` to optimize filter speed for multi-asset scans.
3. **Data Quality Assertions**:
   - Implement automated Dataform-style assertions:
     - `unique_key`: Combination of `(timestamp, symbol)` must be strictly unique.
     - `row_conditions`: High $\ge$ Max(Open, Close), Low $\le$ Min(Open, Close), Volume $\ge 0$.
     - `referential_integrity`: All mapped assets must exist in the canonical 43-symbol universe.

---

### SKILL 7: `/data-engineering-data-driven-feature` (Empirical Feature Engineering & Statistical Power)
*Source: `.agents/skills/data-engineering-data-driven-feature/SKILL.md`*

#### 1. Purpose & Scientific Method
Drives the systematic creation, testing, and validation of quantitative trading features using statistical experiment design, A/B testing frameworks, and causal econometrics.

#### 2. Two-Phase Development Workflow
- **Phase 1: Hypothesis Formulation & Statistical Power**:
  1. *Exploratory Data Analysis*: Identify empirical anomalies in price distribution, orderbook skew, or liquidation cascades.
  2. *Quantitative Hypothesis Definition*: State the causal mechanism clearly:
     $$\mathcal{H}_1: \text{Long Liquidation Z-Score} > 1.8 \land \text{RSI} < 40 \land \text{Whale Wall Persist} \ge 180\text{s} \implies \mathbb{P}(\text{Win}) \ge 60\%$$
  3. *Statistical Significance & Power Analysis*:
     - Sample size must provide $\ge 80\%$ statistical power ($\beta = 0.20$) at $\alpha = 0.05$.
     - Compute Clopper-Pearson exact binomial confidence bounds for win rates across non-overlapping windows.
     - Apply Benjamini-Hochberg False Discovery Rate (FDR) corrections when testing multiple parameter combinations.
- **Phase 2: Feature Architecture & Zero-Lookahead Invariant**:
  1. *Causal Calculation*: All feature values for bar $t$ must be calculated strictly using information available at or before $t$. Any future data leakage permanently invalidates the model.
  2. *Out-of-Sample Validation*: Validate features across 20 non-overlapping 1-month walk-forward windows (2021–2026) with causal 72h purge buffers.

---

### SKILL 8: `/verify` & `test-guard` (Ex-Ante Pre-Execution Gate Verification)
*Source: `.agents/skills/test-guard/SKILL.md` & Institutional Pre-Execution Governance*

#### 1. Purpose & Review Discipline
Acts as the final, immutable gatekeeper before live order dispatch. Enforces the 9 Universal Rules of Test Guard and conducts ex-ante mathematical proofs of risk, margin, and boundary safety.

#### 2. The 9 Universal Verification Rules
1. **Rule 1: Verify Observable Behavior, Not Mocks**: Test actual broker responses, real MT5 tick quotes, and live order ticket states. Never rely on simulated or mocked assumptions.
2. **Rule 2: Ex-Ante Cash Risk Verification**:
   - Compute cash risk via `mt5.order_calc_profit()` for the exact proposed lot size, entry, and stop loss.
   - Confirm risk is strictly within the authorized envelope ($10.00–$14.50 USD for Tier 1; up to $22.00 USD for Tier 2 TradFi indices).
3. **Rule 3: Stressed Capital Floor Defense Gate**:
   - Verify that in the event of an immediate stop-out on all active positions and staged orders:
     $$\text{Stressed Equity} = \text{Current Equity} - \sum_{i} (\text{Risk}_i \times 1.25) \ge 4,775.00\text{ USD}$$
   - If Stressed Equity $< 4,775.00\text{ USD}$, the order is rejected immediately.
4. **Rule 4: Outer Bunker Boundary Audit**:
   - For Longs: $\text{SL} \le \text{min\_price} - 0.50\text{ ATR} - \text{half\_spread}$.
   - For Shorts: $\text{SL} \ge \text{max\_price} + 0.50\text{ ATR} + \text{half\_spread}$.
   - Measuring stop distance from `mid_price` is strictly prohibited.
5. **Rule 5: Resting Whale Wall Persistence Gate**:
   - The supporting whale wall must show $\text{persist\_s} \ge 180\text{s}$, $\text{presence\_frac} \ge 0.85$, and `gate_g7_eligible: True`. Any wall with $0.0\text{s}$ persistence is rejected as spoofed.
6. **Rule 6: Target Magnet Front-Run Gate**:
   - Take Profit must front-run the opposing liquidation band or structural stop cluster by 5 to 10 bps to ensure fill priority before exhaustion.
7. **Rule 7: Proximity / Runway Gate**:
   - Limit entry price must be within $2.0\text{ ATR}$ of current market price. Orders $> 2.0\text{ ATR}$ away are rejected as unfillable noise.
8. **Rule 8: Passive Order Posture**:
   - Verify order type is strictly `BUY_LIMIT` or `SELL_LIMIT`. Market orders and aggressive spread-crossing are banned.
9. **Rule 9: Broker Filling Compatibility**:
   - Transmit with `ORDER_FILLING_IOC`, with automated sequential fallback to `ORDER_FILLING_RETURN` and `ORDER_FILLING_FOK`.

