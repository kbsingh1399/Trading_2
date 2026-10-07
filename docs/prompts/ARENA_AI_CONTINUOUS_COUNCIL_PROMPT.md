# 🏛️ ARENA.AI CONTINUOUS COUNCIL & ORDER DESK PROMPT (POST-PRUNING & FOMC RUNWAY)

> **INSTRUCTIONS FOR USER**: Copy and paste the prompt below directly into your Arena.ai chat session. It reconciles the broker order cancellation, syncs git state, and instructs Arena's multi-agent council to prepare the 18:35:00 UTC post-FOMC reopening slate.

---

```markdown
# 🏛️ ARENA.AI 360° QUANTITATIVE COUNCIL: BROKER RECONCILIATION & 18:35 POST-FOMC ROADMAP

## 🚨 CRITICAL BROKER UPDATE & GIT FAST-FORWARD DIRECTIVE
1. **Ticket #18648927 Has Been Pruned (CANCEL CONFIRMED)**:
   - At **17:35:21 UTC**, Antigravity executed `TRADE_ACTION_REMOVE` on MT5.
   - Broker Return: **`retcode: 10009` (`TRADE_RETCODE_DONE`) — Request executed**.
   - Verified Broker State: **0 Open Positions | 0 Pending Orders | Balance: 4,811.62 USD | Equity: 4,811.62 USD (100% Cash)**.
   - Preserved Floor Cushion: **+36.62 USD** above the 4,775.00 USD hard floor. The account is 100% FLAT and fully insulated against FOMC spread shock.
2. **Git Synchronization**:
   - Section 15 documenting this exact execution was committed and pushed to our branch at commit `ff53b34`.
   - Run: `git fetch origin arena/83d03e3f-trading-2 && git pull origin arena/83d03e3f-trading-2` to bring your workspace to the latest telemetry snapshot (as of 17:42+ UTC).
   - Verify that your background monitor now reflects `orders_total = 0`, `positions_total = 0`, and flat book status.

---

## 🎯 MANDATORY CONTINUOUS COUNCIL MANDATE (18:00 FOMC -> 18:35 REOPENING)
You are the Lead Quantitative Strategist and Governance Council. We are entering the 18:00:00 UTC FOMC Minutes release (T - 15 minutes) inside the 17:00–18:30 UTC Hard Blackout.

Your standing directives for this turn and subsequent heartbeats:
1. **Maintain Observational Blackout**:
   - Zero orders may be placed or recommended between 17:00 and 18:30 UTC.
   - Monitor post-minutes price volatility, spread blowout, and initial market reaction.
2. **Formulate the 18:35:00 UTC Desk Reopening Slate (Model 2 Focus)**:
   - Today's trade forensics proved that unhedged mean-reversion knife-catching is toxic in trending markets (EURUSD -11.00 USD, BTC -6.80 USD, USWTI -10.03 USD), while Model 2 Trend-Following Pullbacks generated all profits (USDJPY +1.82 USD profit, USWTI morning trend +9.88 USD profit).
   - Audit the 24-asset matrix in `docs/telemetry/live_snapshot_latest.json` and rank the top 3 Model 2 setups for desk reopening:
     * **Rank 1 (SOLUSD.p Bearish Trend Pullback Short)**: Target 117.80–118.20 USD zone (Session VWAP / VAL retest), SL: 119.50 USD (anchored above 15m 200 EMA @ 118.96 USD), TP: 114.25 USD (+2.50R target), Volume: 0.07 lots (contract_size=100.0), Dollar Risk: 10.50 USD.
     * **Rank 2 (USDJPY.pi Bullish Continuation Long)**: Target 158.140 USD dip test (if FOMC minutes are hawkish for USD), SL: 157.995 USD, TP: 158.503 USD (+2.50R), Volume: 0.11 lots, Dollar Risk: 10.09 USD.
     * **Rank 3 (ETHUSD.pi Bearish Trend Pullback Short)**: Target ~2,602 USD (Session VWAP retest), SL: 2,630 USD, TP: 2,533 USD (+2.50R), Dollar Risk: ~10.50 USD.
3. **The 5 Post-FOMC Reopening Validation Gates (Mandatory Checklist)**:
   - Detail the exact conditions under which Antigravity is authorized to punch Rank 1 at 18:35 UTC:
     * Gate 1: Broker spread <= 25 bps for crypto (SOL <= 0.28 USD), <= 0.8 pips for FX.
     * Gate 2: Minimum two closed 15m post-event candles (18:15 and 18:30 UTC).
     * Gate 3: Causal taker CVD confirming directional aggression (negative 5m CVD for shorts).
     * Gate 4: Orderbook depth showing resting whale wall >= 150k USD backing the entry level.
     * Gate 5: Single-fill capacity constraint strictly enforced (max 1 active position until Phase 0 BE is armed).

---

## 📝 OUTPUT REQUIREMENTS
1. Reconcile and confirm that the broker book is 100% FLAT (`orders_total = 0`).
2. Present the 3-Persona Dialectic (Orderflow Specialist, Strategy Architect, Capital Floor Guardian).
3. Append **Section 16** to `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md` and push the commit to `origin/arena/83d03e3f-trading-2`.
4. Keep your background telemetry runner (`scripts/arena_endless_runner.py`) running with verbose logging so that the desk remains continuously monitored.
```
