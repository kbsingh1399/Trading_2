"""
Terminal/dispatch_improvement_prompt.py
Dispatches a specialized Strategic & Quantitative Methodology Improvement Prompt to Arena.ai tabs:
  - Arena 1 Primary (01a1311e, GPT Astra)
  - Arena 2 Fable (01a136b2, Claude Fable Orchestrator)
Solicits deep quantitative guidance on:
  1. Resolving the Trailing SL Premature Choke Trap (whorl/retest scratches)
  2. Pruning the 24-Asset Universe down to Top 5 Prime Liquid Majors
  3. Overcoming Stand-Aside Paralysis with decoupled Model 1 (MR) vs Model 2 (Trend Pullback) execution rules
  4. Preserving the 4,775.00 USD hard floor while expanding asymmetric R-multiples (2.5R to 3.5R).
"""
import asyncio
import json
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.arena_bridge import post_prompt_to_arena, dismiss_arena_popup

PROMPT_TEXT = """# INSTITUTIONAL QUANTITATIVE AUDIT & METHODOLOGY IMPROVEMENT MANDATE

## Context & Purpose
This prompt is submitted simultaneously to Arena Tab 1 (GPT Astra) and Arena Tab 2 (Claude Fable Orchestrator) for our algorithmic trading desk on MetaTrader 5 (Blueberry Markets Account 5064568).
GitHub Repository: https://github.com/kbsingh1399/Trading_2 (branch: main)
Active Telemetry: docs/telemetry/live_snapshot_latest.json
Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
Standardized Decision Chain (SOP): https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/STANDARDIZED_TRADING_DECISION_CHAIN.md

The desk operator has raised a critical performance review:
"We are trading so many assets but still not able to get proper trades and winning... mostly hitting trailing SL or breakeven scratches. How can we improve our methodology, universe selection, and execution?"

We need your independent, rigorous quantitative critique and concrete architectural recommendations to resolve this specific structural dilemma.

---

## 1. EMPIRICAL FORENSIC BASELINE & ACCOUNT STATE

- Account: Blueberry Markets MT5 #5064568
- Capital State: Balance = 4,869.65 USD | Equity = 4,869.65 USD | Free Margin = 4,869.65 USD
- Hard Capital Floor: 4,775.00 USD hard floor | 4,795.00 USD operating buffer
- Current Floor Cushion: +94.65 USD above hard floor (+74.65 USD above buffer)
- Current Book: 0 Open Positions | 0 Pending Orders (4 / 4 capacity slots available)

### Empirical Breakdown of Last 31 Realized Trades:
1. Full Target Winners (+16.10 to +34.00 USD / +1.7R to +3.4R):
   - Deal #16944675: USWTI.p (+30.00 USD / +3.0R)
   - Deal #16948363: SP500.p (+34.00 USD / +3.4R)
   - Deal #16954370: BTCUSD.pi (+24.00 USD / +2.4R)
   - Deal #16924690: BTCUSD.pi (+16.10 USD / +1.7R)
   -> Proves that when the full structural thesis develops, asymmetric gains (+2.0R to +3.4R) are highly profitable.

2. Full Initial Stopouts (-10.88 to -13.70 USD / -1.0R):
   - 7 trades stopped out cleanly at initial stop loss (-1.0R risk budget well-controlled, defending capital).

3. The Trailing SL Retracement Trap / Micro-Scratches (+0.70 to +3.72 USD and -0.85 to -1.41 USD):
   - Deal #16945968: GBPUSD.pi (+1.98 USD)
   - Deal #16952451: USWTI.p (+0.70 USD)
   - Deal #17019869: SP500.p (+3.72 USD)
   - Deal #17039158: ETHUSD.pi (-1.41 USD)
   - Deal #17050770: ETHUSD.pi (+1.92 USD)
   - Deal #17073763: SP500.p (+0.90 USD)
   - Deal #17075016: ETHUSD.pi (-0.85 USD)
   -> 8 trades entered cleanly, showed initial profit (+0.70R to +1.00R), had their stop ratcheted mechanically to Entry + 0.15R0 (Phase 0 Breakeven Lock), and were subsequently choked out by normal 15m/1H orderflow retests of the entry shelf, booking scratch profits (+0.70 to +1.92 USD) right before the primary market move unfolded without us!

4. Universe & Activity Concentration:
   - 100% of realized trades occurred in only 5 assets: BTCUSD.pi, ETHUSD.pi, SOLUSD.p, SP500.p, and USWTI.p.
   - 10 Crypto Altcoins (ADA, DOGE, TRX, DOT, LINK, BCH, LTC, AVAX, NEAR) produced 0 trades over the entire period because broker spreads (30 to 250 bps) or lack of deep orderbook depth fail initial viability checks.
   - Over 85% of 15m scanning cycles end in unanimous STAND ASIDE due to conflicting filter gauntlets.

---

## 2. CORE STRATEGIC QUESTIONS FOR THE COUNCIL

### Issue 1: Fixing the Trailing Stop Retracement / Choke Mechanism
Our current Autonomous Ratchet Daemon enforces:
- Phase 0 (Breakeven Lock): At +0.80R0 unrealized gain, move SL to Entry + 0.15R0.
- Phase 1 (Profit Lock): At +1.50R0 unrealized gain, move SL to Entry + 0.80R0.
- Phase 2 (Trailing Lock): At +2.00R0 unrealized gain, trail at High - 0.75R0.

In volatile crypto (BTC, ETH, SOL) and equity index CFDs (SP500, NAS100), an initial impulse of +0.80R almost always experiences an orderflow backfill / retest of the entry shelf / POC / breakout level before the multi-hundred point continuation leg develops.
Moving SL to Entry + 0.15R0 chokes the position right at the retest wick.

Question 1.1: What is the optimal mathematical and structural solution to this problem?
- Approach A (Delay Threshold): Delay Breakeven movement until price reaches +1.20R0 to +1.30R0.
- Approach B (Partial Risk Reduction instead of Breakeven Choke): At +0.80R0, instead of moving SL to Entry + 0.15R0, move SL to Entry - 0.30R0 (or Entry - 0.35R0). This reduces capital risk by 65% to 70% (from -1.0R to -0.30R) while leaving a generous 0.30R breathing buffer below the entry price for normal retests. Only move to Breakeven (Entry + 0.10R0) once price achieves +1.25R0 or +1.50R0.
- Approach C (Structure-Based Dynamic Ratchet): Never move stops based on static R increments alone; trail only behind confirmed 15m fractal swing pivots or behind newly formed resting whale absorption walls.
Which approach (or hybrid) do you recommend, and what exact parameter numbers should we code into Terminal/risk/autonomous_ratchet_daemon.py?

---

### Issue 2: Universe Pruning — 24 Assets vs. Top 5 Prime Liquid Majors
We currently stream telemetry across 24 assets (14 Crypto Perpetuals + 10 TradFi CFDs).
Empirical reality:
- 10 Crypto Altcoins carry massive broker spreads (30 to 250 bps on Blueberry Markets) and fail the spread/friction gate (spread / ATR > 0.18) 95% of the time.
- Most TradFi CFDs lack native Binance/Hyperliquid on-chain L2/L3 orderbook depth and genuine liquidation clusters (we only have MT5 synthetic orderflow).
- True multi-million dollar resting L2/L3 whale walls (10M to 40M USD), tight broker spreads (<= 5 bps), and deep liquidation cascades exist almost exclusively in the Top 5 Prime Liquid Majors:
  1. BTCUSD.pi (Bitcoin Perpetual)
  2. ETHUSD.pi (Ethereum Perpetual)
  3. SOLUSD.p (Solana Perpetual)
  4. NAS100.p (Nasdaq 100 CFD)
  5. SP500.p (S&P 500 CFD)

Question 2.1: Should our algorithmic desk prune the active execution universe down to these 5 Prime Liquid Majors?
What are the quantitative advantages and potential risks of concentrating our capital, execution focus, and compute on these 5 liquid assets?

---

### Issue 3: Eliminating Stand-Aside Paralysis (Decoupling Model 1 vs Model 2)
The models frequently stand aside 20 cycles in a row because of conflicting criteria (e.g., demanding extreme mean-reversion exhaustion |Z| >= 2.0 SD in the middle of a powerful trending market, or demanding trend alignment when looking for mean reversion).

Question 3.1: How should we clearly formalize and separate the execution rules for:
1. Model 2 (Trend Following Pullbacks):
   - When Higher Timeframe Structure (1H/4H EMAs: Price < EMA20 < EMA50 on 1H/4H) confirms a dominant trend with negative cumulative volume delta (CVD), what are the exact rules for staging limit entries on relief pullbacks to 15m/1H EMA20/EMA50 or Session VWAP shelves backed by resting Ask whale walls?
2. Model 1 (Extreme Mean Reversion):
   - When the market is in a confirmed range or overextension (|Z| >= 2.2 SD into major structural liquidation pools with CVD deceleration/absorption), what are the exact rules for staging fade entries?
3. Stand-Aside Condition:
   - When should the desk stand aside (e.g. chop/undefined regime with no resting whale backing or off-hours spread expansion)?

---

### Issue 4: Risk Budget & Asymmetry Calibration
- We have an account balance of 4,869.65 USD.
- Hard floor is 4,775.00 USD (cushion = +94.65 USD).
- Risk per trade is 10.00 to 18.00 USD (0.20% to 0.35% equity risk).
- With up to 2-3 concurrent positions, total worst-case book risk is ~35-45 USD, safely defending the floor.
- How can we calibrate Take Profit magnets (e.g. 2.5R to 3.5R) and liquidity sweeps so that our winners generate +25 to +45 USD while preserving our 70% win rate?

---

## 3. REQUIRED DELIVERABLES IN YOUR RESPONSE
Please provide a comprehensive, structured blueprint containing:
1. Specific Code-Level Recommendations for the Autonomous Ratchet Daemon (Phase 0, Phase 1, Phase 2 thresholds, risk reduction buffers, and trailing mechanics).
2. Universe Recommendation: Concrete ruling on universe pruning (Top 5 Prime Majors vs 24 assets).
3. Playbook Refinement: Concrete entry, SL bunker, and TP magnet rules for Model 2 (Trend Pullbacks) and Model 1 (Mean Reversion).
4. Concrete Action Plan: Immediate implementation steps for Antigravity to code and execute right now.

Be precise, mathematically rigorous, and grounded in market microstructure. Avoid generic advice; give us exact numbers, formulas, and rules.
"""

async def main():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}] Starting Improvement Prompt Dispatch...")
    
    # Dismiss any popups on all Arena tabs first
    await dismiss_arena_popup(target="all")
    await asyncio.sleep(0.5)
    
    # Post prompt to all open Arena tabs
    ok = await post_prompt_to_arena(PROMPT_TEXT, target="all")
    if ok:
        print("✅ Improvement Methodology Prompt successfully dispatched to both Arena tabs!")
    else:
        print("❌ Failed to dispatch prompt to Arena tabs.")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
