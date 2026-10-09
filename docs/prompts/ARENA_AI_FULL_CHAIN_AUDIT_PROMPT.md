# ================================================================================
# INSTITUTIONAL QUANTITATIVE AUDIT & ARCHITECTURAL UPGRADE DIRECTIVE
# TARGET: ARENA.AI QUANTITATIVE AUDIT MODELS (FULL GITHUB READ ACCESS)
# REPOSITORY: https://github.com/kbsingh1399/Trading_2 (Branch: main)
# ================================================================================

You are an Elite Institutional Quantitative Portfolio Manager, High-Frequency/Microstructure Architect, and Senior Trading Systems Auditor. 
You have direct read access to our GitHub repository: https://github.com/kbsingh1399/Trading_2.

### YOUR MANDATE:
Perform an exhaustive 360-degree forensic review of our entire quantitative trading engine, orderflow algorithms, risk governors, and execution pipeline. Provide deep mathematical critique and PRODUCTION-READY CODE REPLACEMENTS for any areas where our logic, execution speed, edge extraction, or capital defense can be upgraded for greater profitability.

The operator will bring your complete response back to our Antigravity execution desk for local evaluation, backtesting, and production implementation.

---

## 1. OUR LIVE PRODUCTION BASELINE & CURRENT OPERATING METRICS

Inspect the repository and ground your critique in our authentic production state:
- Repository: https://github.com/kbsingh1399/Trading_2 (branch: main)
- Master Invariants: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/AGENTS.md
- Active Operational Context: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md
- Decision Gates V3: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/decision_gates_v3.py
- Omni Execution Engine: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/Omni_Trader.py
- Live Admission Governor: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/live_admission.py
- Orderflow Telemetry Daemon: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/Data_Factory/autonomous_telemetry_git_daemon.py
- Live Telemetry Snapshot: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
- Collaborative Order Desk: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md
- 360-Degree Forensic Verifier: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/Terminal/chain_verification_360.py

### Live Financial Milestones:
- Broker: MetaTrader 5 Account #5064568 (Blueberry Markets SVG-Live)
- Starting Capital: 5,000.00 USD
- Current Balance / Equity: 4,896.55 USD (100% Cash Reserves | 0.00 USD Margin Used)
- Hard Capital Floor (G-1): 4,775.00 USD (Lifetime Max DD: 4.50% / 225.00 USD)
- Operating Buffer: 4,795.00 USD (Mandatory >= 20.00 USD cushion above floor)
- Live Cushion: +121.55 USD above hard floor (+101.55 USD above operating buffer)
- Realized Performance Banked Today: +84.05 USD Net Cash Profit (17 completed trades: 11 Wins / 6 Losses = 64.7% Win Rate)
  * Closed Wins Today: BTCUSD +24.00 USD TP, SP500 +34.00 USD TP, USWTI +30.00 USD TP, USWTI +0.70 USD BE lock.
- Capacity Allocation: 4 Concurrent Positions across orthogonal clusters (Forex, Metals, Energies, Indices, Crypto Majors). Risk budget: 10.00 to 14.50 USD per trade.

---

## 2. CORE AREAS REQUIRING YOUR FORENSIC REVIEW & CODE PROPOSALS

Inspect the codebase files and address each of the following 6 core pillars:

### Pillar 1: Execution Gates & Microstructure Latency (`Terminal/decision_gates_v3.py` & `Terminal/Omni_Trader.py`)
- We recently noted that local host machine time was ~29 seconds behind broker server time, creating negative `broker_tick_age_s` in telemetry and risking false rejections in `pre_send_gate`.
- **Review Question**: How should our pre-send and pre-modify execution gates dynamically calibrate broker clock skew, manage tick freshness, and prevent slip/rejections while guaranteeing fail-closed safety?
- **Deliverable**: Provide exact drop-in Python code modifying `Terminal/decision_gates_v3.py` to handle dynamic clock offset calibration cleanly.

### Pillar 2: Strategy Models & Alpha Generation (`Terminal/Omni_Trader.py` & `Terminal/OF_Strategy.py`)
- Our desk operates two primary quantitative engines on 15m bars:
  * Model 1 (Extreme Mean Reversion): Fades extreme standard deviation flushes (|Z| >= 2.0 SD up to 3.5 SD) from Session VWAP with verified CVD absorption and resting L2/L3 whale wall backing.
  * Model 2 (Trend-Continuation Pullbacks): Enters in the direction of HTF trend (Price > VWAP & positive EMA slope) on pullbacks into Session VWAP, Value Area Low, or 20/50 EMA support shelves.
- **Review Question**: 
  1. How can we sharpen the entry trigger for Model 2 so we never chase extended moves (e.g. entering at VAH) while still entering pullbacks with high precision?
  2. What additional quantitative features (e.g. microstructure drift, tick imbalance, delta divergence ratios) would increase win rate and Expectancy?
- **Deliverable**: Provide code improvements or new helper functions for signal confluence scoring and pullback geometry validation.

### Pillar 3: Dynamic Sizing & Capital Floor Optimization (`Terminal/live_admission.py`)
- Initial Capital: 5,000.00 USD. Hard Floor: 4,775.00 USD. Current Equity: 4,896.55 USD.
- Sizing Policy: Risk per trade is scaled between 10.00 and 14.50 USD (0.20% to 0.29%). Max 4 concurrent positions. Moving a trade to Breakeven (Phase 0 BE lock) reduces its contingent book risk to 0.00 USD, liberating capital budget for subsequent orders.
- **Review Question**: 
  1. Is our dynamic capacity and risk recirculation mathematically optimal, or does Kelly / fractional volatility parity offer a safer and faster growth trajectory without threatening the 4,775.00 USD floor?
  2. How can we optimize position sizing across correlated vs. uncorrelated assets?
- **Deliverable**: Provide Python code enhancements for `Terminal/live_admission.py` to upgrade the dynamic risk allocator.

### Pillar 4: Telemetry & Multi-Timeframe Regime Engine (`Terminal/Data_Factory/autonomous_telemetry_git_daemon.py`)
- Our telemetry snapshot currently serializes 15m indicators across 24 assets, but external models require >= 35 1H and 4H closes to compute multi-timeframe regime filters deterministically.
- In addition, the snapshot metadata block needs to be aligned to our active 4-slot capacity governance.
- **Review Question**: What is the most token-efficient and causal data structure for multi-timeframe market telemetry?
- **Deliverable**: Provide the exact code updates for `autonomous_telemetry_git_daemon.py` to serialize 1H/4H bar arrays and clean metadata.

### Pillar 5: Microstructure Piecewise Ratchets & Trade Lifecycle
- Active Ratchet Schedule:
  * Phase 0 (BE Lock): At +0.80R gain, move stop to Entry +0.35R (clearing fees and locking profit).
  * Phase 1 (Profit Lock): At +1.50R gain, move stop to Entry +0.80R.
  * Target Exit: +2.00R to +2.50R structural liquidity target.
  * Time Decay: Exit at market if profit < +0.20R within 24 bars (6 hours).
- **Review Question**: Does this piecewise schedule suffer from premature stop-outs during intraday volatility? How can we enhance trailing ratchets using dynamic ATR or orderbook liquidity shelf tracking?
- **Deliverable**: Provide refined trade lifecycle / trailing ratchet code.

### Pillar 6: Macro Economic Risk Gating (`Data/macro_calendar.json`)
- We enforce strict 30-minute pre-event and 30-minute post-event trading blackouts on Tier-1 economic releases.
- **Review Question & Deliverable**: Review `Data/macro_calendar.json` and provide the complete JSON dataset of Tier-1 releases for the upcoming trading week (October 12–18, 2026), including US CPI, Retail Sales, and central bank speeches.

---

## 3. RESPONSE STRUCTURE & OUTPUT FORMAT

Please structure your response into the following clear sections:
1. **Executive Evaluation**: Direct summary of strengths, hidden vulnerabilities, and highest-impact upgrade opportunities across the pipeline.
2. **Mathematical & Microstructure Critique**: In-depth analysis of our 6 pillars with rigorous quant reasoning.
3. **Exact Production-Ready Code Blocks**: Complete, drop-in replacement Python functions or classes (with file paths and line contexts) for all proposed improvements.
4. **Actionable Implementation Roadmap**: Prioritized list of changes that our execution desk should deploy first for maximum profitability.
