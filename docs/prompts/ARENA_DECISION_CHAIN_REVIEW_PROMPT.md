# 🏛️ ARENA.AI COMPREHENSIVE METHODOLOGY & DECISION CHAIN REVIEW PROMPT

> **PROMPT PURPOSE**: Cross-Council Peer Audit of our Canonical 10-Step Quantitative Trading Decision Chain Specification.  
> **TARGET AGENT**: Arena.ai (Agent Mode / Council Persona)  
> **REPOSITORY**: https://github.com/kbsingh1399/Trading_2 (Branch: `main`)  
> **CANONICAL SPECIFICATION**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md  
> **ACTIVE CONTEXT**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md  
> **LIVE TELEMETRY SNAPSHOT**: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json  

---

```text
========================================================================================
ARENA.AI QUANTITATIVE AUDIT TASK: STANDARDIZED TRADING DECISION CHAIN SPECIFICATION
========================================================================================

You are an institutional quant researcher, microstructure expert, and senior hedge fund portfolio manager. You have been tasked with conducting an exhaustive, rigorous peer review of our desk's canonical production specification:
"STANDARDIZED QUANTITATIVE TRADING DECISION CHAIN (SOP)"

FETCH AND READ THESE LIVE RAW REPOSITORY FILES FIRST:
1. Canonical Decision Chain Spec:
   https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md
2. Active Operational Context & Capital Rules:
   https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md
3. Live Market Telemetry Snapshot (24 Assets):
   https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
4. Master Trade Decision Playbook:
   https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md

----------------------------------------------------------------------------------------
EXECUTIVE DESK STATE & CURRENT LIVE POSTURE
----------------------------------------------------------------------------------------
- Broker: Blueberry Markets (MetaTrader 5 Account #5064568)
- Current Account Equity: 4,859.55 USD | Balance: 4,859.55 USD | Margin Free: 4,859.55 USD
- Capital Defense Floor: 4,775.00 USD (Non-negotiable hard stop) | Operating Buffer: 4,795.00 USD
- Live Floor Cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
- Active Open Positions: 0 (100% capacity available)
- Staged Pending Limit Orders on MetaTrader 5:
  1. Ticket #18954801: BTCUSD.pi SELL LIMIT 0.04 lots @ 81,280.00 USD | SL: 81,560.00 (-11.20 USD risk) | TP: 80,440.00 (+33.60 USD reward, 3.00R) | Defended by 25.38M USD Ask whale wall (81,959.00 USD) and 13.28M wall (81,438.00 USD).
  2. Ticket #18954803: XAUUSD.pi BUY LIMIT 0.01 lots @ 4,140.00 USD | SL: 4,128.50 (-11.50 USD risk) | TP: 4,168.00 (+28.00 USD reward, 2.43R) | Defended by 1.05M USD Bid whale wall (4,120.60 USD).
  3. Ticket #18956325: ETHUSD.pi SELL LIMIT 0.61 lots @ 2,377.00 USD | SL: 2,395.00 (-10.98 USD risk) | TP: 2,340.00 (+22.57 USD reward, 2.06R) | Defended by 14.69M USD Ask whale wall (2,392.70 USD, 611s persist) and 7.53M wall (2,377.50 USD).
- Total Staged Book Risk: 33.68 USD across all 3 tickets (0.69% of equity).
- Stressed Post-All-Loss Equity: 4,825.87 USD (+50.87 USD safely above the 4,775.00 USD hard floor).

----------------------------------------------------------------------------------------
WHAT YOU MUST SPECIFICALLY AUDIT IN THE SPECIFICATION:
----------------------------------------------------------------------------------------

1. THE MANDATORY 8-SKILLS FOUNDATION ENSEMBLE:
   The document mandates that every analysis and trading decision MUST activate at minimum:
   - /brainstorm (Multi-perspective dialectic debate, stress-testing edge cases)
   - /graphify (AST knowledge graph & semantic node relationship traversal)
   - /remember (Persistent cross-session memory & trajectory continuity)
   - /data-analyst (Orderflow, auction profiles, and distribution dissection)
   - /data-engineer (Data contracts, pipeline ingestion, venue_basis mapping, spread gates)
   - /dataform-bigquery (Institutional time-series modeling across 43 Parquet datasets)
   - /data-engineering-data-driven-feature (Empirical feature hypotheses & statistical rigor)
   - /verify (Ex-ante pre-execution mathematical verification of risk & boundaries)
   -> Audit: Is this 8-skill foundation complete, or are there additional quant/risk skills that should be added to the mandatory minimum?

2. THE 4 RECENT QUANTITATIVE BREAKTHROUGHS:
   - Breakthrough 1: Coincidence of Daily VWAP 1D / -1D bands with resting L2/L3 whale walls (>= 180s persistence) as high-conviction entry shelves for Model 2 Trend Pullbacks.
   - Breakthrough 2: Using reconstructed liquidation bands and structural stop clusters as offensive TARGET MAGNETS (riding cascade momentum into them) rather than solely defensive stops.
   - Breakthrough 3: 4-Pillar Absorption vs Trend Blow-Through Forensics (CVD delta acceleration, L2 book replenishment velocity, Arkham on-chain net flow, structural location).
   - Breakthrough 4: Arkham Intelligence On-Chain Institutional Forensics (live exchange net inflows/outflows, whale deposits).
   -> Audit: Are the mathematical criteria and decision thresholds for these 4 breakthroughs robust? How would you sharpen the absorption vs blow-through detection?

3. THE 10-STEP DECISION EXECUTION CHAIN:
   - Step 1: Data Contract, Ingestion & Sanity Gate
   - Step 2: Tri-Layer Memory & Trajectory Audit
   - Step 3: AST Knowledge Graph Traversal
   - Step 4: Higher-Timeframe Auction & Regime Profiling (Stand aside if UNDEFINED)
   - Step 5: Dual-Engine Strategy Dialectic (Model 1 Mean Reversion vs Model 2 Trend Pullback)
   - Step 6: Microstructure Coincidence Stack & On-Chain Intel
   - Step 7: Liquidation & Stop Magnet Dynamics (Absorption vs Blow-Through)
   - Step 8: Mathematical Risk Budget & Capital Floor Gate (Tier 1 10-14.50 USD, Tier 2 16-22 USD)
   - Step 9: Pre-Execution Ex-Ante Audit (Strict passive limit posture, R:R >= 2.0R)
   - Step 10: Autonomous Punch & Dynamic Ratchet Lifecycle (Phase 0 at +1.25R0, Phase 1 at +1.65R0, Phase 2 at >= +2.00R0)
   -> Audit: Is any critical step missing between raw tick ingestion and order closure? Are the dynamic ratchet thresholds optimal for capturing 2.5R-3.0R runs without getting prematurely stopped out?

4. AUDIT OF CURRENT 3 LIVE ORDERS:
   - Evaluate our 3 staged orders (BTC short @ 81,280, Gold long @ 4,140, ETH short @ 2,377) against the latest live telemetry in `live_snapshot_latest.json`.
   - Recommend: WAIT AS-IS, SLIGHT MODIFICATION, or CANCELLATION for each order with mathematical justification.

----------------------------------------------------------------------------------------
REQUIRED OUTPUT FORMAT:
----------------------------------------------------------------------------------------
Please provide your review structured as:
1. EXECUTIVE VERDICT: Overall methodology soundness rating (1-10) and primary thesis.
2. STRENGTHS & SOUNDNESS: What this specification gets 100% right from an institutional quant perspective.
3. VULNERABILITIES & GAP ANALYSIS: Microstructure, econometric, or execution edge cases that need tightening.
4. ACTIONABLE REFINEMENT SUGGESTIONS: Specific modifications to formulas, thresholds, or ratchet rules.
5. AUDIT OF THE 3 STAGED ORDERS: Line-by-line verdict on BTC (#18954801), Gold (#18954803), and ETH (#18956325).
6. RATIFICATION CLAUSE: Confirm whether this document is ratified as the permanent desk SOP.
========================================================================================
```
