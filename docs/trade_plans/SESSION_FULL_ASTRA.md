text
TRADING DESK COUNCIL: CYCLE 106 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: f214c940152c4deaa1d81de871342925 (2026-10-14 20:21:28 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 1/4 filled, 3 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81877.0 | Spread 1.95 bps | Z = -1.02 SD | RSI 47.76 | Trend BEARISH | L2 Imb 0.9606 | Sess CVD -92.24M | Wk CVD -80.00M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 83147.80 [VAH 83818.86 / VAL 82604.57] | WkVWAP 82936.86 | L3 Whales (tot/elig>=180s): 404/261 | Stops Below/Above: [81900.0-82000.0 $1.76M] / [82000.0-82100.0 $1.73M] | Liq Below/Above (Attraction Bands): [81900.0-82000.0 $0.01M] / [82000.0-82100.0 $0.00M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2430.25 | Spread 11.93 bps | Z = -1.09 SD | RSI 41.7 | Trend BEARISH | L2 Imb 0.2334 | Sess CVD -93.74M | Wk CVD -109.24M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 2501.43 [VAH 2528.87 / VAL 2484.43] | WkVWAP 2494.48 | L3 Whales (tot/elig>=180s): 165/54 | Stops Below/Above: [2420.0-2430.0 $0.20M] / [2430.0-2440.0 $0.14M] | Liq Below/Above (Attraction Bands): [2420.0-2430.0 $0.00M] / [2440.0-2450.0 $0.01M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.355 | Spread 22.04 bps | Z = -0.86 SD | RSI 42.57 | Trend BEARISH | L2 Imb 0.1165 | Sess CVD +7.56M | Wk CVD +18.94M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 107.38 [VAH 108.05 / VAL 105.68] | WkVWAP 106.97 | L3 Whales (tot/elig>=180s): 98/35 | Stops Below/Above: [103.0-104.0 $2.24M] / [104.0-105.0 $0.03M] | Liq Below/Above (Attraction Bands): [103.0-104.0 $0.61M] / [104.0-105.0 $0.01M]
• BNB (BNBUSD.p | CRYPTO): Mid 729.75 | Spread 6.85 bps | Z = -1.42 SD | RSI 41.77 | Trend BEARISH | L2 Imb -0.1224 | Sess CVD -1.16M | Wk CVD -7.63M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 744.09 [VAH 745.97 / VAL 737.39] | WkVWAP 740.69 | L3 Whales (tot/elig>=180s): 10/10 | Stops Below/Above: [729.0-730.0 $0.00M] / [730.0-731.0 $0.00M] | Liq Below/Above (Attraction Bands): [729.0-730.0 $0.00M] / [731.0-732.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.3265 | Spread 22.62 bps | Z = -1.22 SD | RSI 40.5 | Trend BEARISH | L2 Imb 0.1786 | Sess CVD +27.29M | Wk CVD +58.52M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.38 / VAL 1.35] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.02M] / [1.3-1.3 $0.01M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.02M] / [1.3-1.3 $0.03M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2291 | Spread 96.03 bps | Z = -0.58 SD | RSI 47.65 | Trend BEARISH | L2 Imb 0.0245 | Sess CVD -0.17M | Wk CVD -2.21M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 0.23 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0822 | Spread 255.63 bps | Z = -0.21 SD | RSI 47.04 | Trend BEARISH | L2 Imb -0.0773 | Sess CVD -11.21M | Wk CVD -21.48M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.01M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3329 | Spread 27.03 bps | Z = 0.67 SD | RSI 44.92 | Trend BULLISH | L2 Imb 0.1173 | Sess CVD +11.53M | Wk CVD +3.49M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 0.33 [VAH 0.33 / VAL 0.33] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.00M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.00M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.138 | Spread 175.75 bps | Z = 0.32 SD | RSI 53.4 | Trend BEARISH | L2 Imb 0.2338 | Sess CVD -0.05M | Wk CVD -0.75M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.16 [VAH 1.18 / VAL 1.10] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.00M] / [1.1-1.1 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.1 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.44 | Spread 69.13 bps | Z = -1.02 SD | RSI 42.16 | Trend BEARISH | L2 Imb 0.0287 | Sess CVD -3.60M | Wk CVD -4.92M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 12.88 [VAH 13.02 / VAL 12.75] | WkVWAP 12.87 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.3-12.4 $0.03M] / [12.4-12.5 $0.00M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 270.45 | Spread 21.45 bps | Z = -0.99 SD | RSI 47.31 | Trend BEARISH | L2 Imb -0.024 | Sess CVD +0.53M | Wk CVD -0.02M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 271.86 [VAH 273.87 / VAL 268.04] | WkVWAP 274.56 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [270.0-271.0 $0.01M] / [271.0-272.0 $0.00M] | Liq Below/Above (Attraction Bands): [270.0-271.0 $0.06M] / [272.0-273.0 $0.00M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.92 | Spread 50.07 bps | Z = -0.4 SD | RSI 52.11 | Trend BEARISH | L2 Imb 0.39 | Sess CVD -1.29M | Wk CVD -3.05M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 61.27 [VAH 61.72 / VAL 60.48] | WkVWAP 61.66 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.9-60.0 $0.00M] / [60.0-60.1 $0.00M] | Liq Below/Above (Attraction Bands): [59.9-60.0 $0.00M] / [60.0-60.1 $0.00M]
• AVAX (AVXUSD.p | CRYPTO): Mid 9.93 | Spread 40.28 bps | Z = -0.76 SD | RSI 48.93 | Trend BEARISH | L2 Imb 0.1806 | Sess CVD -0.47M | Wk CVD -0.35M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 10.22 [VAH 10.40 / VAL 10.05] | WkVWAP 10.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [9.9-9.9 $0.00M] / [9.9-9.9 $0.00M] | Liq Below/Above (Attraction Bands): [9.9-9.9 $0.00M] / [10.0-10.0 $0.00M]
• NEAR (NERUSD.p | CRYPTO): Mid 4.8265 | Spread 64.23 bps | Z = -1.53 SD | RSI 43.08 | Trend BEARISH | L2 Imb -0.1896 | Sess CVD -8.06M | Wk CVD -6.85M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 5.06 [VAH 5.18 / VAL 4.87] | WkVWAP 5.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.8-4.8 $0.01M] / [4.8-4.8 $0.00M] | Liq Below/Above (Attraction Bands): [4.8-4.8 $0.02M] / [4.8-4.8 $0.02M]
• SP500 (SP500.p | INDICES): Mid 7717.95 | Spread 0.44 bps | Z = -1.13 SD | RSI 39.11 | Trend BEARISH | L2 Imb -0.0951 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 7801.07 [VAH 7803.15 / VAL 7791.87] | WkVWAP 7789.85 | L3 Whales (tot/elig>=180s): 95/66 | Stops Below/Above: [7710.0-7720.0 $271.20M] / [7720.0-7730.0 $0.40M] | Liq Below/Above (Attraction Bands): [7710.0-7720.0 $0.13M] / [7730.0-7740.0 $0.00M]
• NAS100 (NAS100.p | INDICES): Mid 29930.01 | Spread 0.41 bps | Z = -1.42 SD | RSI 31.4 | Trend BEARISH | L2 Imb -0.0836 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 30436.30 [VAH 30534.13 / VAL 30420.52] | WkVWAP 30505.93 | L3 Whales (tot/elig>=180s): 80/68 | Stops Below/Above: [29800.0-29900.0 $0.80M] / [29900.0-30000.0 $0.04M] | Liq Below/Above (Attraction Bands): [29800.0-29900.0 $0.01M] / [29900.0-30000.0 $0.11M]
• DJ30 (DJ30.p | INDICES): Mid 51584.4 | Spread 0.23 bps | Z = -0.15 SD | RSI 51.43 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 51822.61 [VAH 52078.36 / VAL 51582.36] | WkVWAP 51746.52 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25238.25 | Spread 0.95 bps | Z = -1.76 SD | RSI 39.28 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25299.66 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4100.625 | Spread 0.17 bps | Z = -0.54 SD | RSI 51.37 | Trend BEARISH | L2 Imb -0.1788 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4153.59 | L3 Whales (tot/elig>=180s): 56/48 | Stops Below/Above: [4090.0-4100.0 $0.00M] / [4100.0-4110.0 $0.16M] | Liq Below/Above (Attraction Bands): [4090.0-4100.0 $0.01M] / [4100.0-4110.0 $0.00M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 55.578 | Spread 6.48 bps | Z = -1.37 SD | RSI 31.69 | Trend BEARISH | L2 Imb -0.1264 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 60.11 [VAH 60.64 / VAL 59.94] | WkVWAP 59.16 | L3 Whales (tot/elig>=180s): 45/25 | Stops Below/Above: [55.5-55.6 $0.04M] / [55.6-55.7 $0.02M] | Liq Below/Above (Attraction Bands): [55.5-55.6 $0.00M] / [55.6-55.7 $0.00M]
• USWTI (USWTI.p | COMMODITIES): Mid 95.229 | Spread 4.83 bps | Z = -0.12 SD | RSI 45.68 | Trend BULLISH | L2 Imb -0.0133 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 94.45 [VAH 94.66 / VAL 92.74] | WkVWAP 93.83 | L3 Whales (tot/elig>=180s): 44/30 | Stops Below/Above: [93.8-93.9 $0.11M] / [93.9-94.0 $0.00M] | Liq Below/Above (Attraction Bands): [93.7-93.8 $0.04M] / [94.0-94.1 $0.04M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1158 | Spread 0.09 bps | Z = 0.1 SD | RSI 58.86 | Trend BEARISH | L2 Imb -0.0074 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/8 | Stops Below/Above: [1.1-1.1 $0.04M] / [1.1-1.1 $0.23M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.3192 | Spread 0.23 bps | Z = -0.39 SD | RSI 53.76 | Trend BEARISH | L2 Imb 0.3295 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/7 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.13M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.11M] / [1.3-1.3 $0.00M]
• USDJPY (USDJPY.pi | FOREX): Mid 158.2935 | Spread 0.19 bps | Z = -0.87 SD | RSI 41.89 | Trend BEARISH | L2 Imb -0.1383 | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 158.32 [VAH 158.44 / VAL 158.13] | WkVWAP 158.40 | L3 Whales (tot/elig>=180s): 38/27 | Stops Below/Above: [157.0-158.0 $0.02M] / [158.0-159.0 $0.01M] | Liq Below/Above (Attraction Bands): [157.0-158.0 $0.00M] / [158.0-159.0 $0.00M]

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 1 pending order(s):
  - Ticket #18925596: ETHUSD.pi SELL_LIMIT 1.0 lots @ Entry 2447.5 USD | Live Mid: 2429.95 USD (Distance: 1.65 ATR, ATR_14=10.6457) | Current SL: 2457.0 USD | Current TP: 2425.0 USD | Trend: BEARISH | Z: -1.09 SD
• For EACH unfilled limit order listed above, perform a complete logical & quantitative audit against the latest live_snapshot_latest.json and explicitly classify it into one of three decisions:
  (A) VIABLE — WAIT TO BE FILLED AS-IS: Confirm that distance to entry is <= 2.0 ATR, supporting L3 whale walls (persistence_s >= 180s) remain intact, 5m/15m/30m CVD and L2 imbalance support absorption, SL sits safely 0.35x-0.50x ATR outside min_price/max_price of the governing bunker, and TP front-runs the opposing buy-stop/sell-stop magnet by 5-10 bps.
  (B) SLIGHT MODIFICATION REQUIRED (MODIFY ENTRY / SL / TP): If the thesis remains valid but live whale walls, stop clusters (nearest_*), or liquidation band boundaries (min_price/max_price) have shifted in the latest snapshot, specify the exact modified Entry, SL, and/or TP levels and why.
  (C) DELETE / CANCEL IMMEDIATELY: If the structural thesis has degraded (e.g., supporting whale walls pulled/thinned >50%, price drifted >2.0 ATR away, regime invalidated, or unabsorbed aggressive selling/buying broke the shelf), recommend immediate deletion to free capacity.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 1 / 4 capacity slots (3 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: f214c940152c4deaa1d81de871342925, as_of_utc: 2026-10-14 20:21:28 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 105:
1. 100% Unanimous Consensus Ratified (STAND ASIDE):
   - All three models agreed unanimously on Cycle 105: STAND ASIDE across all 24 assets. Zero forced trades.
   - Cash equity preserved at 4,859.55 USD (+84.55 USD above 4,775.00 USD hard floor, +64.55 USD above 4,795.00 USD operating buffer). 4/4 capacity slots available!
2. Microstructure & Orderflow Breakthroughs from Cycle 105:
   - Fable's Two-Sided Market-Maker Discovery: 75.9% of BTC persistent notional and 90.7% of SP500 persistent notional belongs to two-sided wallets (e.g. 0xf517639a bidding $38.36M @ 7,687 while asking $12.59M; 0xf5a523b1 bidding $44.54M on BTC while asking $45.38M). They are market-maker inventory, NOT directional defenders!
   - Fable's Contiguous Bins Warning: BTC's $100 bins and SP500's 10-pt bins mean any stop placed arbitrarily close to market lands inside a published sweep band (Archetype 1 & 2).
   - Argon's Stop-on-Stop Proof: SP500 relief short into 7,715-7,725 risks getting swept into the [7,720, 7,730] 0.42M buy-stop cluster, while 45.18M bids at 7,686-7,688 cap gross reward to 1.30R.
3. MANDATE 3 LIVE ORDER AUDIT (STRICT OPERATOR MANDATE):
   - MetaTrader 5 Ticket #18925596 IS LIVE: SELL LIMIT 1.00 lot ETHUSD.pi @ 2447.50 | SL: 2457.00 (-9.50 USD risk) | TP: 2425.00 (+22.50 USD reward, 2.37R).
   - Staged at the Model 2 relief pullback shelf, sheltered behind 7.40M USD Ask Wall @ 2450.30 and 50 EMA @ 2454.54.
   - Task for Astra: Audit Ticket #18925596 (WAIT / MODIFY / DELETE) and evaluate whether BTCUSD.pi SELL LIMIT @ 82,190 (SL 82,420, TP 81,660, 2.30R) should also be staged.

==================== MESSAGE BOUNDARY ====================

Re-issuing Cycle 106 through the standing mandate: confirming arena-skill, checking for a fresh snapshot, then issuing the verdict only through the completed tournament.

==================== MESSAGE BOUNDARY ====================

TRADING DESK COUNCIL — CYCLE 106 · GPT ASTRA FINAL VERDICT

(Issued only after the mandated arena-skill multi-agent tournament — see §7)

1. TELEMETRY & PLAYBOOK INGESTION CITATION
Prompt-cited generation f214c940… (20:21:28 UTC) is SUPERSEDED in the repository. Ground truth used: generation_id=c82b8c85623c4368812f708ca9dd33e8, as_of_utc=2026-10-14 20:56:21 UTC, protocol=omni.telemetry.v3.observed_only, trade_authorization=DENIED_UNVERIFIED_ORDERFLOW. I will not falsely "confirm" f214 — the repo file is 35 minutes newer and materially different (only BTC/ETH/SP500 carry live causal_indicators; the other 21 assets are INSUFFICIENT_HISTORY in-file).
Macro: Fed Bowman Speech, 2026-10-15 02:55:00 UTC, blackout_active=False, enforcement DISABLED_BY_OPERATOR — noted, never a halt reason.
Account MT5 #5064568: balance = equity 4,859.55 USD, margin 0.00, hard floor 4,775.00 (+84.55), buffer 4,795.00 (+64.55). Pending stress is 13.875 USD (not 0.00 — #18925596 is broker-valued), post-joint-stop equity 4,845.675 ≥ 4,795 ✓, capacity 1/4 joint-fill. Playbook §3.A/§3.B/§3.C/§7.4 complied with; p_win=0.4197 uncalibrated (n=17 < 100).

Decisive fact: every wall on all 24 assets is persist_s=0 / samples=1 / SINGLE_SAMPLE — 0 ≥180s-eligible walls anywhere (programmatically verified, scripts/cycle106_telemetry_audit.py). Two-sided MM share: BTC 86.0%, ETH 91.1%, SP500 93.2% — Fable's Cycle-105 discovery re-verified (Archetype 4).

2. MANDATE 1 — 24-ASSET DUAL-ENGINE SCREENING (champion version)

Universal kill W0 = no verified ≥180s defense. Engine 2 evaluated first-class at low |Z| everywhere.

BTC 81,725, Z−1.18 BEARISH: E1 NO (|Z|<2; MR-long = Arch-2) · E2 NO (EMA50 shelf undefended; contiguous $100 bins) → NO SETUP
ETH 2,421.2, Z−1.30 BEARISH: E1 NO · E2 NO-new (W0, two-sided defender) → NO SETUP
SOL causal unavailable, 13.8% friction needs ≥2.5R unprovable → NO SETUP · BNB, XRP, BCH, AVAX: causal unavailable / 0 walls → NO SETUP
ADA (89%), DOGE (210%), DOT (122%), LINK (68%), NEAR (62%): friction-BANNED → NO SETUP
LTC 50.4bps spread, TRX regime conflict → NO SETUP
SP500 7,717.7, Z−1.13 BEARISH, $271M sell-stop bin [7710,7720] directly below price: shorting = into the magnet (Argon's stop-on-stop), long = counter-trend → NO SETUP
NAS100, GOLD, SILVER, USWTI, EURUSD, GBPUSD, USDJPY: in-file causal INSUFFICIENT_HISTORY, W0 → NO SETUP · DJ30, GER40: no bands/book at all → NO SETUP

0 CANDIDATE / 24 NO SETUP. BTC SELL LIMIT @ 82,190 / SL 82,420 / TP 81,660 → DO NOT STAGE: SL sits inside buy-stop bin [82400,82500] ($1.58M, auto-proven), defenders are single-sample two-sided MM (0xf5a523b1 $44.6M/$45.4M), authorization DENIED — Archetypes 1+4. Conditional revisit (champion spec): fresh snapshot + ≥180s one-sided ≥$5M ask wall between entry and a SL placed outside the largest bin within 1 ATR + 0.35–0.50 ATR, 0.04–0.06 lots, authorization lifted.

3. MANDATE 2 — ACTIVE TRADES

active_positions=[] — flat, no ratchets or TP/SL changes needed. Confirmed.

4. MANDATE 3 — #18925596 → (C) DELETE / CANCEL IMMEDIATELY

ETHUSD.pi SELL LIMIT 1.00 @ 2,447.50 / SL 2,457.00 / TP 2,425.00 fails on label-independent grounds: (i) 2.46 ATR from live mid 2,421.2 > 2.0 ATR bound (Playbook §3.A binds Mandate 3); (ii) SL 2,457 inside governing buy-stop bin [2450,2460] $2.349M (Archetype 1), and every compliant SL lands in the contiguous next bin; (iii) cited $7.40M wall relocated to 2,439.1, two-sided MM, persist 0s (Archetype 4). A lots+SL+TP change = a new order under DENIED authorization → DELETE, not MODIFY (this exact MODIFY hypothesis was fielded in the tournament and conceded two FATAL attacks). Cancel frees 13.875 USD stress; stressed equity returns to 4,859.55. Drift policy (champion): pending >2.0 ATR = delete; re-stage only as a fresh ticket under the conditional spec — never chase. (Operator/daemon executes the MT5 cancel; this council does no broker execution.)

Step 4: worst-case post-stop equity as-is 4,845.68 ✓; after cancel 4,859.55, 0/4 slots, 64.55 USD budget (3 max-risk tickets of unused headroom).

5. ACTIONABLE EXECUTION SUMMARY
Action	Symbol	Side	Lots	Entry	SL Bunker	TP Magnet	Risk USD	R:R	Engine	Archetype Defense	Rationale
DELETE #18925596	ETHUSD.pi	SELL LIMIT	1.00	2,447.50	2,457.00 (defective)	2,425.00	9.50 (stress 13.88)	2.37 gross	2	Removes A1+A4	SL in $2.35M bin; 2.46 ATR; MM defender 0s
STAND ASIDE	—	—	—	—	—	—	—	—	—	A1–A5 / R-1–R-4	0/24 certifiable under DENIED authorization; BTC 82,190 rejected as staged
7. ARENA-SKILL TOURNAMENT (standing mandate, executed)

Skill re-confirmed this turn (git pull up-to-date; upstream ≡ .agent/skills/arena/ byte-identical). Tournament run-20261014-211019-s106, seed 106, 4 competitors / 2 rounds / 19 bracket jobs, rubric-judged: R1 a003 beat a001 87–77 (MODIFY hypothesis killed), a002 beat a004 89–81; Final 🏆 a002 beat a003 89–85.5 (card: Working backwards + Build-then-break + Built to last). The champion confirms STAND ASIDE + DELETE and adds the conditional re-stage specs, drift policy, and persistence-observability clause. Record: docs/trade_plans/arena_cycle106/; desk appended; mandate persisted in .agents/rules/ACTIVE_CONTEXT.md; commits 464f7b3 + 0cf450a on arena/97f65666-trading-2 (push still hangs on pack negotiation — safe locally).

8. TELEMETRY ENHANCEMENTS (delivered, not just proposed)

scripts/cycle106_telemetry_audit.py → docs/telemetry/CYCLE106_TELEMETRY_AUDIT.md auto-computes OFI L1/L5/L20, microprice drift, taker ratios, two-sided share, and both SL traps from existing fields. Required schema fixes: cross-generation wall continuity (age_s, re-peg rate, two_sided_mm_flag), in-pipeline causal indicators for 21/24 assets, USD-normalized TradFi CVD, MT5-mapped band prices, governing-bin (largest-within-1-ATR) bunker math, dynamic buffer max(0.35·ATR, ½ bin width, spread+2σ_basis) with lot downsizing (R-4) instead of buffer-shrinking. Macro blackout remains permanently disabled.

Bottom line: STAND ASIDE · CANCEL #18925596 · flat book · 4,859.55 USD and the 4,775.00 floor fully intact · verdict tournament-certified.

==================== MESSAGE BOUNDARY ====================

text
TRADING DESK COUNCIL: CYCLE 108 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)
MANDATORY SKILL ENFORCEMENT: https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
You MUST verify/clone `https://github.com/Jakeschincariol/arena-skill.git` (or read in-repo `.agent/skills/arena/SKILL.md`) and apply the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: c7f7f4cd72cd4b128e956535dfcbbea1 (2026-10-14 21:59:42 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)
4. Mandatory Arena Skill: https://github.com/Jakeschincariol/arena-skill (in-repo at `.agent/skills/arena/SKILL.md` or clone to `~/.claude/skills/arena`) — STRICT MANDATE TO USE ALWAYS.

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 1/4 filled, 3 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81671.0 | Spread 1.96 bps | Z = -1.19 SD | RSI 45.06 | Trend BEARISH | L2 Imb -0.5134 | Sess CVD -94.01M | Wk CVD -79.59M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 83147.80 [VAH 83818.86 / VAL 82604.57] | WkVWAP 82915.99 | L3 Whales (tot/elig>=180s): 420/290 | Stops Below/Above: [81700.0-81800.0 $0.00M] / [81800.0-81900.0 $4.53M] | Liq Below/Above (Attraction Bands): [81700.0-81800.0 $0.05M] / [81900.0-82000.0 $0.01M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2417.3 | Spread 12.41 bps | Z = -1.32 SD | RSI 40.52 | Trend BEARISH | L2 Imb -0.7192 | Sess CVD -91.61M | Wk CVD -102.05M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 2501.43 [VAH 2528.87 / VAL 2484.43] | WkVWAP 2492.76 | L3 Whales (tot/elig>=180s): 168/48 | Stops Below/Above: [2410.0-2420.0 $0.59M] / [2420.0-2430.0 $0.03M] | Liq Below/Above (Attraction Bands): [2410.0-2420.0 $0.87M] / [2420.0-2430.0 $0.00M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.61 | Spread 21.03 bps | Z = -0.61 SD | RSI 53.44 | Trend BEARISH | L2 Imb 0.0622 | Sess CVD +7.93M | Wk CVD +18.84M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 107.38 [VAH 107.90 / VAL 105.68] | WkVWAP 106.91 | L3 Whales (tot/elig>=180s): 104/68 | Stops Below/Above: [104.0-105.0 $1.35M] / [105.0-106.0 $0.25M] | Liq Below/Above (Attraction Bands): [104.0-105.0 $0.00M] / none
• BNB (BNBUSD.p | CRYPTO): Mid 728.9 | Spread 8.23 bps | Z = -1.41 SD | RSI 46.17 | Trend BEARISH | L2 Imb -0.2258 | Sess CVD -2.29M | Wk CVD -8.51M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 743.91 [VAH 745.18 / VAL 737.05] | WkVWAP 740.48 | L3 Whales (tot/elig>=180s): 10/8 | Stops Below/Above: [728.0-729.0 $0.00M] / [729.0-730.0 $0.00M] | Liq Below/Above (Attraction Bands): [725.0-726.0 $0.00M] / [729.0-730.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.333 | Spread 30.01 bps | Z = -0.75 SD | RSI 50.4 | Trend BEARISH | L2 Imb -0.0159 | Sess CVD +28.88M | Wk CVD +60.79M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.38 / VAL 1.35] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.01M] / [1.3-1.3 $0.03M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.02M] / [1.3-1.4 $0.09M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2289 | Spread 91.72 bps | Z = -0.56 SD | RSI 50.68 | Trend BEARISH | L2 Imb 0.0605 | Sess CVD -0.31M | Wk CVD -1.95M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.23 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.01M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0818 | Spread 268.95 bps | Z = -0.41 SD | RSI 44.48 | Trend BEARISH | L2 Imb 0.2206 | Sess CVD -9.28M | Wk CVD -19.29M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3327 | Spread 30.06 bps | Z = 0.51 SD | RSI 38.54 | Trend BULLISH | L2 Imb 0.1401 | Sess CVD +10.78M | Wk CVD +3.26M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 0.33 [VAH 0.33 / VAL 0.33] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.00M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.00M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.1405 | Spread 184.13 bps | Z = 0.52 SD | RSI 57.24 | Trend BEARISH | L2 Imb 0.2218 | Sess CVD -0.05M | Wk CVD -0.72M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.17 [VAH 1.18 / VAL 1.10] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.00M] / [1.1-1.1 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.1 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.4225 | Spread 68.42 bps | Z = -1.01 SD | RSI 44.26 | Trend BEARISH | L2 Imb 0.2721 | Sess CVD -3.66M | Wk CVD -4.91M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 12.88 [VAH 13.02 / VAL 12.75] | WkVWAP 12.86 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.3-12.4 $0.03M] / [12.4-12.5 $0.00M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 269.0 | Spread 14.87 bps | Z = -1.22 SD | RSI 42.61 | Trend BEARISH | L2 Imb 0.0672 | Sess CVD +0.47M | Wk CVD -0.22M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 271.86 [VAH 274.23 / VAL 268.77] | WkVWAP 274.48 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [268.0-269.0 $0.10M] / [269.0-270.0 $0.00M] | Liq Below/Above (Attraction Bands): [268.0-269.0 $0.00M] / [269.0-270.0 $0.00M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.57 | Spread 50.36 bps | Z = -0.67 SD | RSI 45.15 | Trend BEARISH | L2 Imb 0.2477 | Sess CVD -1.30M | Wk CVD -3.05M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 61.26 [VAH 61.68 / VAL 60.46] | WkVWAP 61.62 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.5-59.6 $0.08M] / [59.6-59.7 $0.00M] | Liq Below/Above (Attraction Bands): [59.5-59.6 $0.00M] / [59.6-59.7 $0.00M]
• AVAX (AVXUSD.p | CRYPTO): Mid 9.975 | Spread 30.08 bps | Z = -0.47 SD | RSI 57.7 | Trend BEARISH | L2 Imb 0.3164 | Sess CVD -0.83M | Wk CVD -0.73M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 10.27 [VAH 10.37 / VAL 10.10] | WkVWAP 10.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [10.0-10.0 $0.00M] / [10.0-10.0 $0.01M] | Liq Below/Above (Attraction Bands): [10.0-10.0 $0.00M] / [10.0-10.0 $0.00M]
• NEAR (NERUSD.p | CRYPTO): Mid 4.8445 | Spread 68.12 bps | Z = -1.22 SD | RSI 47.7 | Trend BEARISH | L2 Imb 0.0758 | Sess CVD -8.34M | Wk CVD -2.25M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 5.07 [VAH 5.16 / VAL 4.87] | WkVWAP 5.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.8-4.8 $0.01M] / [4.8-4.8 $0.00M] | Liq Below/Above (Attraction Bands): [4.8-4.8 $0.02M] / [4.8-4.8 $0.00M]
• SP500 (SP500.p | INDICES): Mid 7717.125 | Spread 1.13 bps | Z = None SD | RSI None | Trend INSUFFICIENT_HISTORY | L2 Imb 0.0445 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 7801.07 [VAH 7803.15 / VAL 7791.27] | WkVWAP 7789.63 | L3 Whales (tot/elig>=180s): 70/62 | Stops Below/Above: [7710.0-7720.0 $4335.48M] / [7720.0-7730.0 $0.66M] | Liq Below/Above (Attraction Bands): [7710.0-7720.0 $0.13M] / [7730.0-7740.0 $0.00M]
• NAS100 (NAS100.p | INDICES): Mid 29918.2 | Spread 0.47 bps | Z = None SD | RSI None | Trend INSUFFICIENT_HISTORY | L2 Imb -0.0662 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 30436.30 [VAH 30534.13 / VAL 30420.52] | WkVWAP 30503.95 | L3 Whales (tot/elig>=180s): 57/56 | Stops Below/Above: [29800.0-29900.0 $0.83M] / [29900.0-30000.0 $0.31M] | Liq Below/Above (Attraction Bands): [29800.0-29900.0 $0.01M] / [29900.0-30000.0 $0.11M]
• DJ30 (DJ30.p | INDICES): Mid 51600.75 | Spread 0.4 bps | Z = None SD | RSI None | Trend INSUFFICIENT_HISTORY | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 51822.61 [VAH 52062.86 / VAL 51582.36] | WkVWAP 51745.75 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25238.8 | Spread 1.27 bps | Z = None SD | RSI None | Trend INSUFFICIENT_HISTORY | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: BALANCED | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25299.16 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4105.105 | Spread 0.76 bps | Z = None SD | RSI None | Trend INSUFFICIENT_HISTORY | L2 Imb 0.1107 | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4153.47 | L3 Whales (tot/elig>=180s): 49/39 | Stops Below/Above: [4100.0-4110.0 $0.16M] / [4110.0-4120.0 $0.19M] | Liq Below/Above (Attraction Bands): [4100.0-4110.0 $0.00M] / [4110.0-4120.0 $0.02M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 56.8605 | Spread 140.87 bps | Z = None SD | RSI None | Trend INSUFFICIENT_HISTORY | L2 Imb -0.1669 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 60.11 [VAH 60.64 / VAL 59.79] | WkVWAP 59.16 | L3 Whales (tot/elig>=180s): 19/18 | Stops Below/Above: [55.6-55.7 $0.02M] / [55.7-55.8 $0.01M] | Liq Below/Above (Attraction Bands): [55.6-55.7 $0.00M] / [55.7-55.8 $0.13M]
• USWTI (USWTI.p | COMMODITIES): Mid 95.329 | Spread 3.15 bps | Z = None SD | RSI None | Trend INSUFFICIENT_HISTORY | L2 Imb 0.518 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: BALANCED | PriorDay POC 92.29 [VAH 94.05 / VAL 92.02] | WkVWAP 93.84 | L3 Whales (tot/elig>=180s): 14/1 | Stops Below/Above: [93.9-94.0 $0.00M] / [94.0-94.1 $0.06M] | Liq Below/Above (Attraction Bands): [93.7-93.8 $0.04M] / [94.0-94.1 $0.04M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1155 | Spread 3.85 bps | Z = 0.02 SD | RSI 54.05 | Trend BEARISH | L2 Imb 0.0933 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/9 | Stops Below/Above: [1.1-1.1 $0.05M] / [1.1-1.1 $0.23M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.319 | Spread 3.03 bps | Z = -0.43 SD | RSI 50.91 | Trend BEARISH | L2 Imb 0.9492 | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/9 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.13M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.11M] / [1.3-1.3 $0.00M]
• USDJPY (USDJPY.pi | FOREX): Mid 158.322 | Spread 5.43 bps | Z = -0.73 SD | RSI 38.36 | Trend BEARISH | L2 Imb 0.6174 | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 158.28 [VAH 158.43 / VAL 158.12] | WkVWAP 158.40 | L3 Whales (tot/elig>=180s): 34/31 | Stops Below/Above: [157.0-158.0 $0.02M] / [158.0-159.0 $0.02M] | Liq Below/Above (Attraction Bands): [157.0-158.0 $0.00M] / none

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 1 pending order(s):
  - Ticket #18925879: SOLUSD.p SELL_LIMIT 0.1 lots @ Entry 104.9 USD | Live Mid: 104.66499999999999 USD (Distance: 0.43 ATR, ATR_14=0.5419) | Current SL: 105.75 USD | Current TP: 103.1 USD | Trend: BEARISH | Z: -0.61 SD
• For EACH unfilled limit order listed above, perform a complete logical & quantitative audit against the latest live_snapshot_latest.json and explicitly classify it into one of three decisions:
  (A) VIABLE — WAIT TO BE FILLED AS-IS: Confirm that distance to entry is <= 2.0 ATR, supporting L3 whale walls (persistence_s >= 180s) remain intact, 5m/15m/30m CVD and L2 imbalance support absorption, SL sits safely 0.35x-0.50x ATR outside min_price/max_price of the governing bunker, and TP front-runs the opposing buy-stop/sell-stop magnet by 5-10 bps.
  (B) SLIGHT MODIFICATION REQUIRED (MODIFY ENTRY / SL / TP): If the thesis remains valid but live whale walls, stop clusters (nearest_*), or liquidation band boundaries (min_price/max_price) have shifted in the latest snapshot, specify the exact modified Entry, SL, and/or TP levels and why.
  (C) DELETE / CANCEL IMMEDIATELY: If the structural thesis has degraded (e.g., supporting whale walls pulled/thinned >50%, price drifted >2.0 ATR away, regime invalidated, or unabsorbed aggressive selling/buying broke the shelf), recommend immediate deletion to free capacity.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 1 / 4 capacity slots (3 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: c7f7f4cd72cd4b128e956535dfcbbea1, as_of_utc: 2026-10-14 21:59:42 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 106:
1. Tournament Engine Feature Built by Fable:
   - Fable implemented the persistent repo tournament engine at `Terminal/arena_tournament.py` with 30/30 passing unit tests (`Tests/Test_Arena_Tournament.py`) and opened PR #3 on GitHub!
2. Unanimous Ratification on MT5 Orders Executed by Desk:
   - ETH Ticket #18925596: DELETED from MT5. Fable and your champion a002 independently proved the distance (26 pts / 2.45 ATR) breached the <=2.0 ATR proximity gate, and SL @ 2457 sat inside the [2450, 2460] 2.35M squeeze band.
   - BTC Ticket #18925868: DELETED from MT5. The 82,190 limit had SL @ 82,420 inside the [82400, 82500] 1.05M sweep band.
3. LIVE ORDER STAGED ON MT5 (TICKET #18925879):
   - Desk staged Model 2 Pullback Short on Solana: SELL LIMIT 0.10 lots SOLUSD.p @ 104.90 USD | SL: 105.75 USD (-8.50 USD risk, 0.17% equity) | TP: 103.10 USD (+18.00 USD reward, 2.12R).
   - Defended by 50 EMA @ 104.85, 2.48M Ask Wall @ 104.88, and SL sheltered behind 4.85M Ask Wall @ 105.64 outside the [104, 105] buy-stop band.
   - Distance to market is currently only 0.46 pts (<1.0 ATR).
4. MANDATE FOR CYCLE 107:
   - Mandate 1: Screen all 24 assets in `live_snapshot_latest.json` for new high-confluence Model 1 / Model 2 setups across the 3 remaining capacity slots.
   - Mandate 3: Audit Ticket #18925879 (`SOLUSD.p` SELL LIMIT @ 104.90) against fresh orderbook depth and distance (WAIT / MODIFY / CANCEL).
5. MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) INVARIANT:
   - https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
   - Run tournament bracket evaluations (`bracket.py`, `rubric.md`) across competing hypotheses before issuing your final ruling.

==================== MESSAGE BOUNDARY ====================

Cycle 108 received — new snapshot, ETH ticket gone, new SOL pending to audit. Following the mandate: arena-skill first, fresh telemetry second, tournament before any verdict.

==================== MESSAGE BOUNDARY ====================

Persistence is real this cycle (614 eligible walls, max ~3,900s) — the Cycle 106 universal kill is gone. Deep-auditing the live SOL ticket and all shelves before the tournament.

==================== MESSAGE BOUNDARY ====================

Round 1 done: WAIT and MODIFY both eliminated — final is DELETE (first-principles) vs DELETE (evidence/edge-cases).

==================== MESSAGE BOUNDARY ====================

TRADING DESK COUNCIL — CYCLE 108 · GPT ASTRA FINAL VERDICT

(Arena-skill tournament certified — §7. No verdict was issued before the bracket completed.)

1. INGESTION CITATION (as found, not as asserted)

Prompt-cited generation c7f7f4cd… (21:59:42 UTC) is already superseded on origin/main: ground truth is 31601187035742c39248d4fd72118721, 2026-10-14 22:01:47 UTC, trade_authorization=DENIED_UNVERIFIED_ORDERFLOW. Account 4,859.55/4,859.55 USD, floor 4,775 (+84.55), buffer 4,795. Pending: #18925879 SOLUSD.p SELL_LIMIT 0.10 @ 104.90 / SL 105.75 / TP 103.10 (risk 8.50, stressed 12.625, post-joint-stop equity 4,846.925 ✓). Positions: 0. Macro: Bowman 2026-10-15 02:55 UTC, blackout False, enforcement DISABLED — not a factor. Cycle 106 peer ratifications confirmed (ETH #18925596 + BTC #18925868 deleted; both traps auto-re-proven by my audit script).

What changed since Cycle 106: persistence is cured — 614 walls at persist ≥180s (max ~3,941s), causal indicators live for 17/24 assets. But SOL's two-sided MM share is 99.6%: every material defender (0xeac842b2 BUY $8.40M/SELL $8.60M; 0x5323b922 grid BUY $3.79M/SELL $4.35M) is a market-making grid — the same wall complex from the Cycle 43/44 SOL autopsy losses.

2. MANDATE 1 — 24 ASSETS

BTC (Z−1.23 BEARISH, CVD30m −$1.16M): E1 NO (|Z|<2) · E2 NO (two-sided asks, contiguous $100 bins) · ETH (Z−1.33): same → NO SETUP. BNB/XRP/BCH/LTC/AVAX/TRX/EURUSD/GBPUSD/USDJPY: 0 walls, spread, regime-flow conflict, or unresolvable FX bins → NO SETUP. ADA/DOGE/DOT/LINK/NEAR: 15%-friction banned → NO SETUP. SP500/NAS100/DJ30/GER40/GOLD/SILVER/USWTI: causal INSUFFICIENT_HISTORY in-file → NO SETUP. SOL: no new (resting ticket below).
Result: 0 CANDIDATE / 24 NO SETUP.

3. MANDATE 2

0 open positions — no ratchets needed. Confirmed.

4. MANDATE 3 — #18925879 → (C) DELETE

The WAIT and MODIFY hypotheses were fielded in the tournament and eliminated on conceded attacks: WAIT's defender admitted its band test was mis-scored (SL is inside the band) and its CVD "absorption" reading inverted (taker-buy 0.77 = aggression into the short); MODIFY's defender admitted 24.4% live friction and an SL sheltered behind a two-sided grid. Surviving kills:

Archetype 1: SL 105.75 sits inside the only buy-stop band above, [105,106] $0.25M (compliant SL ≥ 106.18–106.26)
Friction 25.9%, lot-invariant: spread ÷ SL-distance = 0.22/0.85 — no lot size can cure this ticket
R:R 2.12 < SOL's ≥2.5R calibration (§7.4)
Archetype 4: all defenders are two-sided MM grids, persistence notwithstanding
Hostile fill flow: CVD +149k/+227k/+664k (5/15/30m), velocity 2.27

False-delete cost is priced: forgone +18.00 USD if it would have run clean — accepted as the premium against repeating A1/A4 (it died exactly this way twice). Cancel frees 12.625 stress → stressed equity 4,859.55. Champion re-stage spec (fresh ticket only): spread ≤0.15 or spread/distance ≤15%; SL = governing-bin max + 0.35–0.50 ATR; shield wallet one-sided by |BUY−SELL|/(BUY+SELL) ≥ 0.80, ≥$500k, ≥180s; CVD decelerating; R:R ≥2.5; authorization lifted. (Operator/daemon executes the MT5 cancel.)

5. EXECUTION SUMMARY
Action	Symbol	Side	Lots	Entry	SL Bunker	TP Magnet	Risk USD	R:R	Engine	Archetype Defense	Rationale
DELETE #18925879	SOLUSD.p	SELL LIMIT	0.10	104.90	105.75 (in-band)	103.10	8.50 (stress 12.63)	2.12	2	Removes A1+A4	SL in [105,106]; 25.9% scale-invariant friction; MM-grid defense
STAND ASIDE	—	—	—	—	—	—	—	—	—	A1–A5/R-1–R-4	0/24 certifiable; SOL re-stage pre-registered behind spread + sidedness gates
7. ARENA TOURNAMENT (mandate enforced)

Skill re-cloned from Jakeschincariol/arena-skill, byte-identical to .agent/skills/arena/. Run run-20261014-220353-s108 (seed 108, 4 agents, 2 rounds): R1 a004 beat a003 85–73, a001 beat a002 85–77; Final 🏆 a004 (First principles + Built to last) beat a001 86.5–85. Record in docs/trade_plans/arena_cycle108/, diagnostics in docs/telemetry/CYCLE108_TELEMETRY_AUDIT.md, desk appended, committed on arena/97f65666-trading-2.

8. TELEMETRY ENHANCEMENTS

Shipped diagnostics now compute OFI/microprice/taker-ratios/sidedness per cycle. Build next: publish directional_index + two_sided_mm_flag per wallet (formula ratified by the tournament), net-directional notional, causal indicators for the remaining 7 assets, USD-normalized TradFi CVD, governing-bin bunker fields — and print SOL spread_price on every cycle checklist so the re-stage trigger is actually watched.

Bottom line: DELETE #18925879 · STAND ASIDE on all new staging · flat book · floor intact at 4,859.55 USD · tournament-certified.

==================== MESSAGE BOUNDARY ====================

text
TRADING DESK COUNCIL: CYCLE 109 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)
MANDATORY SKILL ENFORCEMENT: https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
You MUST verify/clone `https://github.com/Jakeschincariol/arena-skill.git` (or read in-repo `.agent/skills/arena/SKILL.md`) and apply the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: c74503df3d29434c9ca2ac5f3d61c647 (2026-10-14 22:30:40 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)
4. Mandatory Arena Skill: https://github.com/Jakeschincariol/arena-skill (in-repo at `.agent/skills/arena/SKILL.md` or clone to `~/.claude/skills/arena`) — STRICT MANDATE TO USE ALWAYS.

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 0/4 filled, 4 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81530.0 | Spread 1.96 bps | Z = -1.32 SD | RSI 37.56 | Trend BEARISH | L2 Imb 0.846 | Sess CVD -98.85M | Wk CVD -83.88M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 83147.80 [VAH 83818.86 / VAL 82732.39] | WkVWAP 82902.96 | L3 Whales (tot/elig>=180s): 410/271 | Stops Below/Above: [81500.0-81600.0 $4.71M] / [81600.0-81700.0 $0.51M] | Liq Below/Above (Attraction Bands): [81500.0-81600.0 $0.00M] / [81700.0-81800.0 $0.00M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2413.8 | Spread 11.6 bps | Z = -1.37 SD | RSI 35.6 | Trend BEARISH | L2 Imb 0.9124 | Sess CVD -95.90M | Wk CVD -105.69M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 2501.43 [VAH 2528.87 / VAL 2484.43] | WkVWAP 2492.07 | L3 Whales (tot/elig>=180s): 151/36 | Stops Below/Above: [2410.0-2420.0 $1.24M] / [2420.0-2430.0 $0.40M] | Liq Below/Above (Attraction Bands): [2410.0-2420.0 $0.87M] / [2420.0-2430.0 $0.00M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.37 | Spread 23.0 bps | Z = -0.76 SD | RSI 47.68 | Trend BEARISH | L2 Imb 0.1877 | Sess CVD +7.67M | Wk CVD +18.70M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 107.38 [VAH 108.05 / VAL 105.68] | WkVWAP 106.89 | L3 Whales (tot/elig>=180s): 102/53 | Stops Below/Above: [103.0-104.0 $1.33M] / [104.0-105.0 $0.14M] | Liq Below/Above (Attraction Bands): [103.0-104.0 $0.61M] / [104.0-105.0 $0.00M]
• BNB (BNBUSD.p | CRYPTO): Mid 728.2 | Spread 8.24 bps | Z = -1.47 SD | RSI 41.4 | Trend BEARISH | L2 Imb 0.0514 | Sess CVD -2.19M | Wk CVD -8.05M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 743.91 [VAH 745.18 / VAL 737.05] | WkVWAP 740.38 | L3 Whales (tot/elig>=180s): 10/5 | Stops Below/Above: [728.0-729.0 $0.00M] / [729.0-730.0 $0.00M] | Liq Below/Above (Attraction Bands): [725.0-726.0 $0.00M] / [729.0-730.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.3335 | Spread 22.5 bps | Z = -0.67 SD | RSI 52.86 | Trend BEARISH | L2 Imb 0.1529 | Sess CVD +29.60M | Wk CVD +61.47M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.38 / VAL 1.35] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.01M] / [1.3-1.3 $0.02M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.07M] / [1.3-1.4 $0.09M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2288 | Spread 91.76 bps | Z = -0.57 SD | RSI 49.03 | Trend BEARISH | L2 Imb 0.0894 | Sess CVD -0.21M | Wk CVD -1.86M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.23 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.01M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0819 | Spread 256.57 bps | Z = -0.33 SD | RSI 45.51 | Trend BEARISH | L2 Imb 0.2454 | Sess CVD -8.97M | Wk CVD -18.98M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3322 | Spread 24.08 bps | Z = 0.21 SD | RSI 30.72 | Trend BULLISH | L2 Imb 0.1903 | Sess CVD +9.86M | Wk CVD +2.40M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 0.33 [VAH 0.33 / VAL 0.32] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.01M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.00M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.1395 | Spread 184.29 bps | Z = 0.47 SD | RSI 54.43 | Trend BEARISH | L2 Imb 0.1567 | Sess CVD -0.04M | Wk CVD -0.76M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 1.17 [VAH 1.18 / VAL 1.11] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.05M] / [1.1-1.1 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.1 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.3915 | Spread 68.6 bps | Z = -1.1 SD | RSI 41.88 | Trend BEARISH | L2 Imb -0.0443 | Sess CVD -3.68M | Wk CVD -4.81M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 12.88 [VAH 13.04 / VAL 12.75] | WkVWAP 12.86 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.3-12.4 $0.03M] / [12.4-12.5 $0.00M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 267.85 | Spread 21.65 bps | Z = -1.42 SD | RSI 39.93 | Trend BEARISH | L2 Imb -0.0382 | Sess CVD +0.49M | Wk CVD -0.37M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 271.86 [VAH 274.23 / VAL 268.40] | WkVWAP 274.42 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [267.0-268.0 $0.00M] / [268.0-269.0 $0.10M] | Liq Below/Above (Attraction Bands): [267.0-268.0 $0.00M] / [268.0-269.0 $0.00M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.48 | Spread 50.44 bps | Z = -0.74 SD | RSI 44.62 | Trend BEARISH | L2 Imb 0.3358 | Sess CVD -1.38M | Wk CVD -3.10M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 61.26 [VAH 61.68 / VAL 60.46] | WkVWAP 61.60 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.4-59.5 $0.00M] / [59.5-59.6 $0.08M] | Liq Below/Above (Attraction Bands): [59.4-59.5 $0.00M] / [59.5-59.6 $0.00M]
• AVAX (AVXUSD.p | CRYPTO): Mid 10.0 | Spread 40.0 bps | Z = -0.32 SD | RSI 60.07 | Trend BEARISH | L2 Imb -0.0782 | Sess CVD -1.02M | Wk CVD -0.85M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 10.27 [VAH 10.39 / VAL 10.10] | WkVWAP 10.35 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [10.0-10.0 $0.00M] / [10.0-10.0 $0.00M] | Liq Below/Above (Attraction Bands): [10.0-10.0 $0.00M] / [10.0-10.0 $0.00M]
• NEAR (NERUSD.p | CRYPTO): Mid 4.8585 | Spread 63.81 bps | Z = -1.03 SD | RSI 50.87 | Trend BEARISH | L2 Imb -0.0579 | Sess CVD -8.19M | Wk CVD -1.31M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 5.06 [VAH 5.13 / VAL 4.92] | WkVWAP 5.23 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.8-4.9 $0.01M] / [4.9-4.9 $0.00M] | Liq Below/Above (Attraction Bands): [4.8-4.8 $0.00M] / [4.9-4.9 $0.01M]
• SP500 (SP500.p | INDICES): Mid 7706.33 | Spread 0.44 bps | Z = -1.37 SD | RSI 33.1 | Trend BEARISH | L2 Imb 0.3493 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 7801.07 [VAH 7803.15 / VAL 7790.68] | WkVWAP 7789.20 | L3 Whales (tot/elig>=180s): 115/64 | Stops Below/Above: [7700.0-7710.0 $7054.25M] / [7710.0-7720.0 $11366.64M] | Liq Below/Above (Attraction Bands): [7690.0-7700.0 $0.01M] / [7710.0-7720.0 $0.13M]
• NAS100 (NAS100.p | INDICES): Mid 29821.82 | Spread 0.41 bps | Z = -1.78 SD | RSI 25.05 | Trend BEARISH | L2 Imb 0.5359 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 30436.30 [VAH 30534.13 / VAL 30420.52] | WkVWAP 30500.83 | L3 Whales (tot/elig>=180s): 93/40 | Stops Below/Above: [29700.0-29800.0 $0.07M] / [29800.0-29900.0 $0.85M] | Liq Below/Above (Attraction Bands): [29700.0-29800.0 $0.44M] / [29800.0-29900.0 $0.01M]
• DJ30 (DJ30.p | INDICES): Mid 51622.35 | Spread 0.31 bps | Z = 0.11 SD | RSI 55.01 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 51869.11 [VAH 52062.86 / VAL 51582.36] | WkVWAP 51744.80 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25209.3 | Spread 1.23 bps | Z = -2.07 SD | RSI 33.81 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25298.40 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4107.975 | Spread 0.27 bps | Z = -0.29 SD | RSI 58.46 | Trend BEARISH | L2 Imb 0.3341 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4153.21 | L3 Whales (tot/elig>=180s): 57/35 | Stops Below/Above: [4100.0-4110.0 $0.00M] / [4110.0-4120.0 $0.19M] | Liq Below/Above (Attraction Bands): [4100.0-4110.0 $0.00M] / [4110.0-4120.0 $0.02M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 55.714 | Spread 6.46 bps | Z = -1.24 SD | RSI 45.0 | Trend BEARISH | L2 Imb -0.0131 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 60.11 [VAH 60.64 / VAL 59.79] | WkVWAP 59.14 | L3 Whales (tot/elig>=180s): 47/8 | Stops Below/Above: [55.6-55.7 $0.02M] / [55.7-55.8 $0.01M] | Liq Below/Above (Attraction Bands): [55.6-55.7 $0.01M] / [55.7-55.8 $0.13M]
• USWTI (USWTI.p | COMMODITIES): Mid 95.035 | Spread 4.84 bps | Z = -0.56 SD | RSI 39.91 | Trend BULLISH | L2 Imb 0.3923 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 94.29 [VAH 94.74 / VAL 92.70] | WkVWAP 93.84 | L3 Whales (tot/elig>=180s): 37/30 | Stops Below/Above: [93.7-93.8 $0.10M] / [93.8-93.9 $0.11M] | Liq Below/Above (Attraction Bands): [93.7-93.8 $0.04M] / [94.0-94.1 $0.04M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1164 | Spread 0.18 bps | Z = 0.28 SD | RSI 65.44 | Trend BEARISH | L2 Imb 0.0646 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/10 | Stops Below/Above: [1.1-1.1 $1.06M] / [1.1-1.1 $0.23M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.3197 | Spread 0.08 bps | Z = -0.28 SD | RSI 59.34 | Trend BEARISH | L2 Imb 0.2928 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/10 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.13M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.11M] / [1.3-1.3 $0.00M]
• USDJPY (USDJPY.pi | FOREX): Mid 158.244 | Spread 0.13 bps | Z = -1.04 SD | RSI 33.87 | Trend BEARISH | L2 Imb -0.1 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 158.28 [VAH 158.43 / VAL 158.12] | WkVWAP 158.40 | L3 Whales (tot/elig>=180s): 37/23 | Stops Below/Above: [157.0-158.0 $0.03M] / [158.0-159.0 $0.03M] | Liq Below/Above (Attraction Bands): [157.0-158.0 $0.00M] / none

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 0 pending orders.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 0 / 4 capacity slots (4 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: c74503df3d29434c9ca2ac5f3d61c647, as_of_utc: 2026-10-14 22:30:40 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 106:
1. Tournament Engine Feature Built by Fable:
   - Fable implemented the persistent repo tournament engine at `Terminal/arena_tournament.py` with 30/30 passing unit tests (`Tests/Test_Arena_Tournament.py`) and opened PR #3 on GitHub!
2. Unanimous Ratification on MT5 Orders Executed by Desk:
   - ETH Ticket #18925596: DELETED from MT5. Fable and your champion a002 independently proved the distance (26 pts / 2.45 ATR) breached the <=2.0 ATR proximity gate, and SL @ 2457 sat inside the [2450, 2460] 2.35M squeeze band.
   - BTC Ticket #18925868: DELETED from MT5. The 82,190 limit had SL @ 82,420 inside the [82400, 82500] 1.05M sweep band.
3. LIVE ORDER STAGED ON MT5 (TICKET #18925879):
   - Desk staged Model 2 Pullback Short on Solana: SELL LIMIT 0.10 lots SOLUSD.p @ 104.90 USD | SL: 105.75 USD (-8.50 USD risk, 0.17% equity) | TP: 103.10 USD (+18.00 USD reward, 2.12R).
   - Defended by 50 EMA @ 104.85, 2.48M Ask Wall @ 104.88, and SL sheltered behind 4.85M Ask Wall @ 105.64 outside the [104, 105] buy-stop band.
   - Distance to market is currently only 0.46 pts (<1.0 ATR).
4. MANDATE FOR CYCLE 107:
   - Mandate 1: Screen all 24 assets in `live_snapshot_latest.json` for new high-confluence Model 1 / Model 2 setups across the 3 remaining capacity slots.
   - Mandate 3: Audit Ticket #18925879 (`SOLUSD.p` SELL LIMIT @ 104.90) against fresh orderbook depth and distance (WAIT / MODIFY / CANCEL).
5. MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) INVARIANT:
   - https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
   - Run tournament bracket evaluations (`bracket.py`, `rubric.md`) across competing hypotheses before issuing your final ruling.

==================== MESSAGE BOUNDARY ====================

Cycle 109 — book now completely flat (0 pending, 0 positions). Arena-skill verification, fresh telemetry pull, then the tournament before any verdict.

==================== MESSAGE BOUNDARY ====================

🏆 Champion: a001 (Contrarian). Persisting the Cycle 109 record and verdict.

==================== MESSAGE BOUNDARY ====================

Cycle 109 — Final Council Verdict

🏆 Tournament (arena-skill, verified up-to-date, bracket.py seed 109): 4 agents → R1: a003 def. a002, a001 def. a004 → Final: a001 (Contrarian) def. a003 — "dead heat on analysis; a001 wins on the deliverable that outlives the cycle."

Ingestion: gen c74503df… @ 22:30:40 UTC — matches the prompt exactly this cycle. Causal indicators now live 24/24; 585 walls ≥180s.

Book state — Mandates 2 & 3: Fully flat. positions [], pending []. SOL #18925879 is gone with balance unchanged at 4,859.55 — cancelled unfilled. The Cycle 108 champion's DELETE was executed correctly, at zero cost. Nothing to ratchet or audit.

Mandate 1 — verdict: STAND ASIDE, with the first trigger-armed watch in four cycles.

ETH (the real story): BEARISH stack, pullback to VAL shelf 2426.6, persistent asks, CVD selling — the best setup since Cycle 105. Priced three ways by the champion (tight / rule-lenient / deep-TP): 0.48–0.64R, 0.48–0.50R, 1.07–1.43R — all below the ≥2.2R ETH calibration, with stops inside or hard against contiguous bins (Archetype 1). Killing its own candidate is what won a001 the tournament.
BTC: ladder 0.51–0.67R (first magnet) to 1.68–1.90R (deep magnet at 81,210) vs 2.0R gate — fails at every rung.
NAS100: no pullback yet (retrace −0.04, RSI 25.05); shelf 2.29 ATR away exceeds the 2.0 proximity bound.
GER40: the only |Z| ≥ 2 (−2.07), but in a BEARISH regime Engine 1 permits neither side — MR-longs banned, MR-shorts need +Z — and it has zero walls/bands.
SP500: stop-cluster notionals corrupted ($7.05B / $11.37B single bins, >100× neighbours) — excluded per Playbook §3.B; no staging from corrupted data.
SOL re-stage: flow sub-gate now passes (taker-buy 0.77 → 0.535/0.511, genuinely decelerating). Two blockers remain: spread 0.24 (worsened) and still two-sided MM shields.

ETH WATCH (armed — fires only when all four print): ① rejection at 2426.6–2442.7 with negative 15m CVD; ② one-sided ask (directional_index ≥ 0.80) ≥ $5M, ≥180s, above the shelf; ③ SL outside the governing bin +0.35–0.50 ATR paying ≥2.2R to the first tradable magnet; ④ authorization ≠ DENIED. Invalidation is symmetric: any gate absent for two consecutive generations, or 2450 reclaimed on positive CVD — the watch dies rather than being re-debated.

Governance: equity 4,859.55 stressed, +64.55 above buffer, contingent stress $0. No tickets staged, modified, or deleted.

Persistence: champion solution, all 3 verdicts, task, and arena state in docs/trade_plans/arena_cycle109/; audit in docs/telemetry/CYCLE109_TELEMETRY_AUDIT.md; desk appended; committed 8ba28b2 on arena/97f65666-trading-2.

==================== MESSAGE BOUNDARY ====================

text
TRADING DESK COUNCIL: CYCLE 110 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)
MANDATORY SKILL ENFORCEMENT: https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
You MUST verify/clone `https://github.com/Jakeschincariol/arena-skill.git` (or read in-repo `.agent/skills/arena/SKILL.md`) and apply the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: e8694354cd3b4dd6a2880782dcf0aff1 (2026-10-14 22:59:59 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)
4. Mandatory Arena Skill: https://github.com/Jakeschincariol/arena-skill (in-repo at `.agent/skills/arena/SKILL.md` or clone to `~/.claude/skills/arena`) — STRICT MANDATE TO USE ALWAYS.

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 0/4 filled, 4 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81566.0 | Spread 1.96 bps | Z = -1.25 SD | RSI 33.78 | Trend BEARISH | L2 Imb 0.6238 | Sess CVD -103.93M | Wk CVD -83.66M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 83147.80 [VAH 83818.86 / VAL 82732.39] | WkVWAP 82897.14 | L3 Whales (tot/elig>=180s): 383/249 | Stops Below/Above: [81500.0-81600.0 $4.71M] / [81600.0-81700.0 $0.51M] | Liq Below/Above (Attraction Bands): [81500.0-81600.0 $0.00M] / [81700.0-81800.0 $0.00M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2416.85 | Spread 12.0 bps | Z = -1.26 SD | RSI 33.48 | Trend BEARISH | L2 Imb 0.893 | Sess CVD -99.11M | Wk CVD -103.21M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 2501.43 [VAH 2528.87 / VAL 2484.43] | WkVWAP 2491.71 | L3 Whales (tot/elig>=180s): 159/63 | Stops Below/Above: [2410.0-2420.0 $1.24M] / [2420.0-2430.0 $0.40M] | Liq Below/Above (Attraction Bands): [2410.0-2420.0 $0.87M] / [2420.0-2430.0 $0.00M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.46 | Spread 21.06 bps | Z = -0.69 SD | RSI 44.23 | Trend BEARISH | L2 Imb 0.1046 | Sess CVD +7.31M | Wk CVD +18.90M | Flow: BULLISH_ABSORPTION | Trapped: BALANCED | PriorDay POC 107.38 [VAH 108.05 / VAL 105.68] | WkVWAP 106.88 | L3 Whales (tot/elig>=180s): 92/59 | Stops Below/Above: [104.0-105.0 $0.14M] / [105.0-106.0 $0.18M] | Liq Below/Above (Attraction Bands): [104.0-105.0 $0.00M] / none
• BNB (BNBUSD.p | CRYPTO): Mid 729.2 | Spread 8.23 bps | Z = -1.27 SD | RSI 37.92 | Trend BEARISH | L2 Imb -0.0704 | Sess CVD -2.19M | Wk CVD -7.69M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 743.91 [VAH 745.18 / VAL 737.05] | WkVWAP 740.34 | L3 Whales (tot/elig>=180s): 10/8 | Stops Below/Above: [729.0-730.0 $0.00M] / [730.0-731.0 $0.00M] | Liq Below/Above (Attraction Bands): [729.0-730.0 $0.00M] / [731.0-732.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.332 | Spread 30.03 bps | Z = -0.72 SD | RSI 47.7 | Trend BEARISH | L2 Imb 0.0394 | Sess CVD +29.68M | Wk CVD +61.69M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.38 / VAL 1.35] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.01M] / [1.3-1.3 $0.02M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.07M] / [1.3-1.4 $0.09M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2294 | Spread 91.52 bps | Z = -0.4 SD | RSI 47.15 | Trend BEARISH | L2 Imb 0.0738 | Sess CVD -0.21M | Wk CVD -1.79M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 0.23 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.01M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0819 | Spread 256.57 bps | Z = -0.31 SD | RSI 43.8 | Trend BEARISH | L2 Imb 0.1084 | Sess CVD -8.90M | Wk CVD -18.78M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3321 | Spread 24.09 bps | Z = 0.15 SD | RSI 29.42 | Trend BULLISH | L2 Imb 0.2031 | Sess CVD +9.61M | Wk CVD +2.19M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 0.33 [VAH 0.33 / VAL 0.32] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.01M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.00M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.1465 | Spread 183.17 bps | Z = 0.95 SD | RSI 54.43 | Trend BEARISH | L2 Imb 0.1581 | Sess CVD -0.03M | Wk CVD -0.76M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.17 [VAH 1.18 / VAL 1.12] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.4055 | Spread 70.13 bps | Z = -1.03 SD | RSI 38.92 | Trend BEARISH | L2 Imb -0.0142 | Sess CVD -3.73M | Wk CVD -4.84M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 12.88 [VAH 13.04 / VAL 12.75] | WkVWAP 12.85 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.3-12.4 $0.03M] / [12.4-12.5 $0.00M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 267.8 | Spread 17.92 bps | Z = -1.42 SD | RSI 37.77 | Trend BEARISH | L2 Imb -0.0047 | Sess CVD +0.49M | Wk CVD -0.43M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 271.86 [VAH 274.60 / VAL 268.40] | WkVWAP 274.41 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [267.0-268.0 $0.00M] / [268.0-269.0 $0.10M] | Liq Below/Above (Attraction Bands): [267.0-268.0 $0.00M] / [268.0-269.0 $0.00M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.38 | Spread 50.52 bps | Z = -0.82 SD | RSI 42.8 | Trend BEARISH | L2 Imb 0.2928 | Sess CVD -1.38M | Wk CVD -3.02M | Flow: BULLISH_ABSORPTION | Trapped: BALANCED | PriorDay POC 61.26 [VAH 61.68 / VAL 60.46] | WkVWAP 61.59 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.3-59.4 $0.00M] / [59.4-59.5 $0.00M] | Liq Below/Above (Attraction Bands): [59.3-59.4 $0.03M] / [59.4-59.5 $0.00M]
• AVAX (AVXUSD.p | CRYPTO): Mid 10.005 | Spread 29.99 bps | Z = -0.28 SD | RSI 60.07 | Trend BEARISH | L2 Imb -0.336 | Sess CVD -1.08M | Wk CVD -0.80M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 10.27 [VAH 10.39 / VAL 10.10] | WkVWAP 10.35 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• NEAR (NERUSD.p | CRYPTO): Mid 4.882 | Spread 65.55 bps | Z = -0.8 SD | RSI 53.34 | Trend BEARISH | L2 Imb 0.2434 | Sess CVD -8.05M | Wk CVD -0.34M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 5.06 [VAH 5.12 / VAL 4.87] | WkVWAP 5.23 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.9-4.9 $0.02M] / [4.9-4.9 $0.00M] | Liq Below/Above (Attraction Bands): [4.9-4.9 $0.10M] / [4.9-4.9 $0.00M]
• SP500 (SP500.p | INDICES): Mid 7702.26 | Spread 0.44 bps | Z = -1.45 SD | RSI 30.53 | Trend BEARISH | L2 Imb 0.0782 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 7801.07 [VAH 7803.15 / VAL 7790.68] | WkVWAP 7788.96 | L3 Whales (tot/elig>=180s): 110/81 | Stops Below/Above: [7690.0-7700.0 $0.40M] / [7700.0-7710.0 $7051.78M] | Liq Below/Above (Attraction Bands): [7690.0-7700.0 $0.01M] / [7710.0-7720.0 $0.13M]
• NAS100 (NAS100.p | INDICES): Mid 29773.07 | Spread 0.41 bps | Z = -1.94 SD | RSI 21.83 | Trend BEARISH | L2 Imb 0.3704 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 30435.91 [VAH 30533.22 / VAL 30420.21] | WkVWAP 30499.61 | L3 Whales (tot/elig>=180s): 80/40 | Stops Below/Above: [29700.0-29800.0 $0.07M] / [29800.0-29900.0 $0.85M] | Liq Below/Above (Attraction Bands): [29700.0-29800.0 $0.44M] / [29800.0-29900.0 $0.01M]
• DJ30 (DJ30.p | INDICES): Mid 51621.35 | Spread 0.31 bps | Z = 0.1 SD | RSI 55.72 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 51869.11 [VAH 52078.36 / VAL 51582.36] | WkVWAP 51744.58 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25203.2 | Spread 1.23 bps | Z = -2.12 SD | RSI 31.94 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25298.07 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4106.7 | Spread 0.19 bps | Z = -0.33 SD | RSI 60.26 | Trend BEARISH | L2 Imb 0.1292 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4153.11 | L3 Whales (tot/elig>=180s): 57/30 | Stops Below/Above: [4100.0-4110.0 $0.00M] / [4110.0-4120.0 $0.19M] | Liq Below/Above (Attraction Bands): [4100.0-4110.0 $0.00M] / [4110.0-4120.0 $0.02M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 55.627 | Spread 6.47 bps | Z = -1.3 SD | RSI 44.95 | Trend BEARISH | L2 Imb 0.2042 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 60.11 [VAH 60.64 / VAL 59.79] | WkVWAP 59.13 | L3 Whales (tot/elig>=180s): 54/21 | Stops Below/Above: [55.6-55.7 $0.02M] / [55.7-55.8 $0.01M] | Liq Below/Above (Attraction Bands): [55.6-55.7 $0.01M] / [55.7-55.8 $0.13M]
• USWTI (USWTI.p | COMMODITIES): Mid 94.94 | Spread 4.85 bps | Z = -0.78 SD | RSI 39.79 | Trend BULLISH | L2 Imb 0.527 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 94.29 [VAH 94.74 / VAL 92.63] | WkVWAP 93.84 | L3 Whales (tot/elig>=180s): 40/29 | Stops Below/Above: [93.6-93.7 $0.07M] / [93.7-93.8 $0.10M] | Liq Below/Above (Attraction Bands): [93.6-93.7 $0.03M] / [93.7-93.8 $0.04M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1173 | Spread 0.09 bps | Z = 0.56 SD | RSI 69.3 | Trend BEARISH | L2 Imb 0.0852 | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/10 | Stops Below/Above: [1.1-1.1 $1.07M] / [1.1-1.1 $0.23M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.3205 | Spread 0.08 bps | Z = -0.1 SD | RSI 62.7 | Trend BEARISH | L2 Imb 0.3508 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/10 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.13M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.11M] / [1.3-1.3 $0.00M]
• USDJPY (USDJPY.pi | FOREX): Mid 158.084 | Spread 0.38 bps | Z = -1.67 SD | RSI 26.44 | Trend BEARISH | L2 Imb -0.2255 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 158.28 [VAH 158.43 / VAL 158.12] | WkVWAP 158.40 | L3 Whales (tot/elig>=180s): 39/31 | Stops Below/Above: [157.0-158.0 $0.03M] / [158.0-159.0 $0.03M] | Liq Below/Above (Attraction Bands): [157.0-158.0 $0.00M] / none

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 0 pending orders.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 0 / 4 capacity slots (4 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: e8694354cd3b4dd6a2880782dcf0aff1, as_of_utc: 2026-10-14 22:59:59 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 106:
1. Tournament Engine Feature Built by Fable:
   - Fable implemented the persistent repo tournament engine at `Terminal/arena_tournament.py` with 30/30 passing unit tests (`Tests/Test_Arena_Tournament.py`) and opened PR #3 on GitHub!
2. Unanimous Ratification on MT5 Orders Executed by Desk:
   - ETH Ticket #18925596: DELETED from MT5. Fable and your champion a002 independently proved the distance (26 pts / 2.45 ATR) breached the <=2.0 ATR proximity gate, and SL @ 2457 sat inside the [2450, 2460] 2.35M squeeze band.
   - BTC Ticket #18925868: DELETED from MT5. The 82,190 limit had SL @ 82,420 inside the [82400, 82500] 1.05M sweep band.
3. LIVE ORDER STAGED ON MT5 (TICKET #18925879):
   - Desk staged Model 2 Pullback Short on Solana: SELL LIMIT 0.10 lots SOLUSD.p @ 104.90 USD | SL: 105.75 USD (-8.50 USD risk, 0.17% equity) | TP: 103.10 USD (+18.00 USD reward, 2.12R).
   - Defended by 50 EMA @ 104.85, 2.48M Ask Wall @ 104.88, and SL sheltered behind 4.85M Ask Wall @ 105.64 outside the [104, 105] buy-stop band.
   - Distance to market is currently only 0.46 pts (<1.0 ATR).
4. MANDATE FOR CYCLE 107:
   - Mandate 1: Screen all 24 assets in `live_snapshot_latest.json` for new high-confluence Model 1 / Model 2 setups across the 3 remaining capacity slots.
   - Mandate 3: Audit Ticket #18925879 (`SOLUSD.p` SELL LIMIT @ 104.90) against fresh orderbook depth and distance (WAIT / MODIFY / CANCEL).
5. MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) INVARIANT:
   - https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
   - Run tournament bracket evaluations (`bracket.py`, `rubric.md`) across competing hypotheses before issuing your final ruling.

==================== MESSAGE BOUNDARY ====================

Cycle 110 — arena mandate confirmed. Verifying the skill, pulling the fresh main snapshot (gen e8694354…, 22:59:59 UTC), and running the screen.

==================== MESSAGE BOUNDARY ====================

Snapshot as found is actually newer (6a96f85b… @ 23:00:45 UTC). Book flat, DENIED, ETH watch gates still unmet (price below shelf, geometry unchanged). Running the mandated tournament (seed 110).

==================== MESSAGE BOUNDARY ====================

Cycle 110 — Final Council Verdict

🏆 Tournament (arena-skill confirmed current, bracket.py seed 110): R1 — a003 def. a004, a001 def. a002 → Final: a003 (Inversion/Maximal rigour) def. a001 on provenance discipline, matching its arithmetic honesty.

Ingestion note: the live file is gen 6a96f85b… @ 23:00:45 UTC — 46 seconds newer than the prompt-stated e8694354…/22:59:59. Cited as found, per standing rule. Authorization DENIED; macro blackout False (enforcement disabled).

Mandates 2 & 3: book flat — active_positions [], pending_orders [], contingent stress $0, equity 4,859.55 (+64.55 above buffer). Nothing to ratchet or audit.

Mandate 1 — STAND ASIDE. The cycle's work was the first full audit of the Cycle-109 ETH watch:

ETH Watch Gate	Result
① Rejection at 2426.6–2442.7 shelf	FAIL — price 2416.4, shelf unvisited
② Verified one-sided ask ≥$5M, ≥180s	UNPROVEN — walls are NO_ORDER_ID wallet-attributed inferences; the two-sided 0xab5e6f pattern is corroboration only
③ ≥2.2R to first magnet, SL outside governing bin	FAIL — 0.48–0.50R (0.49R at R-4 size: 0.38 lots, $14.40 risk)
④ Authorization ≠ DENIED	FAIL
Invalidation (2450 reclaim / absence clock)	Not met — but wording debt flagged: the two-generation death clock should start at first shelf visit, not at arming. Playbook clarification recommended.

Staging ETH now would reproduce the #18925596 autopsy verbatim (Archetypes 1+3). The verdict rests only on source-independent kills (unvisited shelf, geometry, DENIED).

Elsewhere: BTC mid 81,563.5 sits inside its own [81500,81600] $4.71M target magnet with impulse velocity (7.74) — selling the arrival; NAS100 (Z −1.88, RSI 21.8) still no pullback, shelf 2.24 ATR; GER40 at Z −2.07 has no legal Engine-1 side in a BEARISH regime and an empty book; SOL shorts now face taker-buy 0.64 windows (Archetype 2 mirrored) with spread 0.23; SP500 stop notionals remain corrupted ($7.05B/$11.37B bins); USDJPY shelf 2.2 ATR away.

Framework gains from this tournament: unverified wallet walls now corroborate only, never solely convict (symmetric standard, adopted from a002's attack); flow deceleration operationally defined (5m and 15m taker-buy ≥ 0.55 for two consecutive generations with rising 15m lows).

Persistence: docs/trade_plans/arena_cycle110/ (champion, 3 verdicts, task, state), docs/telemetry/CYCLE110_TELEMETRY_AUDIT.md, desk appended — committed cca8e88 on arena/97f65666-trading-2.

==================== MESSAGE BOUNDARY ====================

text
TRADING DESK COUNCIL: CYCLE 111 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)
MANDATORY SKILL ENFORCEMENT: https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
You MUST verify/clone `https://github.com/Jakeschincariol/arena-skill.git` (or read in-repo `.agent/skills/arena/SKILL.md`) and apply the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: 26b46c891f694c8f8e036763996b84a8 (2026-10-14 23:30:15 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)
4. Mandatory Arena Skill: https://github.com/Jakeschincariol/arena-skill (in-repo at `.agent/skills/arena/SKILL.md` or clone to `~/.claude/skills/arena`) — STRICT MANDATE TO USE ALWAYS.

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 0/4 filled, 4 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81404.0 | Spread 1.97 bps | Z = -1.4 SD | RSI 44.4 | Trend BEARISH | L2 Imb -0.9856 | Sess CVD -107.06M | Wk CVD -81.99M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 83147.80 [VAH 83818.86 / VAL 82924.12] | WkVWAP 82886.59 | L3 Whales (tot/elig>=180s): 389/220 | Stops Below/Above: [81400.0-81500.0 $4.88M] / [81500.0-81600.0 $1.37M] | Liq Below/Above (Attraction Bands): [81400.0-81500.0 $0.05M] / [81500.0-81600.0 $0.00M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2414.45 | Spread 12.01 bps | Z = -1.29 SD | RSI 45.3 | Trend BEARISH | L2 Imb -0.9511 | Sess CVD -101.84M | Wk CVD -96.21M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 2501.43 [VAH 2526.26 / VAL 2484.43] | WkVWAP 2491.16 | L3 Whales (tot/elig>=180s): 149/50 | Stops Below/Above: [2410.0-2420.0 $0.02M] / [2420.0-2430.0 $0.44M] | Liq Below/Above (Attraction Bands): [2410.0-2420.0 $0.87M] / [2420.0-2430.0 $0.00M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.21 | Spread 24.95 bps | Z = -0.85 SD | RSI 53.4 | Trend BEARISH | L2 Imb 0.0534 | Sess CVD +7.68M | Wk CVD +19.15M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 107.38 [VAH 108.05 / VAL 105.68] | WkVWAP 106.86 | L3 Whales (tot/elig>=180s): 102/70 | Stops Below/Above: [103.0-104.0 $1.56M] / [104.0-105.0 $0.06M] | Liq Below/Above (Attraction Bands): [103.0-104.0 $0.62M] / [104.0-105.0 $0.00M]
• BNB (BNBUSD.p | CRYPTO): Mid 728.95 | Spread 6.86 bps | Z = -1.28 SD | RSI 51.74 | Trend BEARISH | L2 Imb -0.3418 | Sess CVD -2.30M | Wk CVD -6.45M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 743.91 [VAH 745.18 / VAL 737.56] | WkVWAP 740.28 | L3 Whales (tot/elig>=180s): 10/6 | Stops Below/Above: [729.0-730.0 $0.00M] / [730.0-731.0 $0.00M] | Liq Below/Above (Attraction Bands): [729.0-730.0 $0.00M] / [731.0-732.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.33 | Spread 30.08 bps | Z = -0.81 SD | RSI 52.85 | Trend BEARISH | L2 Imb 0.0347 | Sess CVD +30.28M | Wk CVD +63.40M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.38 / VAL 1.35] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.02M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.07M] / [1.3-1.4 $0.09M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2296 | Spread 91.48 bps | Z = -0.36 SD | RSI 59.31 | Trend BEARISH | L2 Imb 0.1016 | Sess CVD -0.16M | Wk CVD -1.43M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 0.24 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0819 | Spread 256.25 bps | Z = -0.22 SD | RSI 51.89 | Trend BEARISH | L2 Imb 0.179 | Sess CVD -8.85M | Wk CVD -17.37M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3322 | Spread 24.08 bps | Z = 0.21 SD | RSI 38.31 | Trend BULLISH | L2 Imb 0.2202 | Sess CVD +9.64M | Wk CVD +3.50M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 0.33 [VAH 0.33 / VAL 0.32] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.00M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.00M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.152 | Spread 173.61 bps | Z = 1.33 SD | RSI 71.09 | Trend BEARISH | L2 Imb 0.1024 | Sess CVD -0.02M | Wk CVD -0.65M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 1.16 [VAH 1.18 / VAL 1.12] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.401 | Spread 69.35 bps | Z = -1.03 SD | RSI 50.52 | Trend BEARISH | L2 Imb -0.0267 | Sess CVD -3.69M | Wk CVD -4.50M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 12.88 [VAH 13.01 / VAL 12.75] | WkVWAP 12.85 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.3-12.4 $0.03M] / [12.4-12.5 $0.00M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 267.3 | Spread 17.96 bps | Z = -1.5 SD | RSI 46.25 | Trend BEARISH | L2 Imb -0.0434 | Sess CVD +0.51M | Wk CVD -0.05M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 271.86 [VAH 274.60 / VAL 268.77] | WkVWAP 274.39 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [267.0-268.0 $0.00M] / [268.0-269.0 $0.10M] | Liq Below/Above (Attraction Bands): [267.0-268.0 $0.00M] / [268.0-269.0 $0.00M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.34 | Spread 50.56 bps | Z = -0.84 SD | RSI 48.53 | Trend BEARISH | L2 Imb 0.2532 | Sess CVD -1.38M | Wk CVD -2.75M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 61.26 [VAH 61.68 / VAL 60.46] | WkVWAP 61.58 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.3-59.4 $0.00M] / [59.4-59.5 $0.00M] | Liq Below/Above (Attraction Bands): [59.3-59.4 $0.03M] / [59.4-59.5 $0.00M]
• AVAX (AVXUSD.p | CRYPTO): Mid 10.015 | Spread 29.96 bps | Z = -0.22 SD | RSI 68.33 | Trend BEARISH | L2 Imb -0.1855 | Sess CVD -1.12M | Wk CVD -0.36M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 10.27 [VAH 10.40 / VAL 10.05] | WkVWAP 10.35 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [9.9-10.0 $0.01M] / [10.0-10.1 $0.00M] | Liq Below/Above (Attraction Bands): [9.8-9.9 $0.18M] / [10.0-10.1 $0.00M]
• NEAR (NERUSD.p | CRYPTO): Mid 4.881 | Spread 65.56 bps | Z = -0.79 SD | RSI 60.27 | Trend BEARISH | L2 Imb 0.1019 | Sess CVD -7.72M | Wk CVD +0.12M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 5.06 [VAH 5.12 / VAL 4.87] | WkVWAP 5.23 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.9-4.9 $0.02M] / [4.9-4.9 $0.00M] | Liq Below/Above (Attraction Bands): [4.9-4.9 $0.10M] / [4.9-4.9 $0.00M]
• SP500 (SP500.p | INDICES): Mid 7701.61 | Spread 0.44 bps | Z = -1.45 SD | RSI 33.7 | Trend BEARISH | L2 Imb 0.0173 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 7801.07 [VAH 7803.15 / VAL 7791.27] | WkVWAP 7788.66 | L3 Whales (tot/elig>=180s): 114/90 | Stops Below/Above: [7690.0-7700.0 $0.35M] / [7700.0-7710.0 $813.19M] | Liq Below/Above (Attraction Bands): [7690.0-7700.0 $0.01M] / [7710.0-7720.0 $0.13M]
• NAS100 (NAS100.p | INDICES): Mid 29725.82 | Spread 0.41 bps | Z = -2.09 SD | RSI 21.13 | Trend BEARISH | L2 Imb 0.0022 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 30435.91 [VAH 30533.22 / VAL 30420.21] | WkVWAP 30497.41 | L3 Whales (tot/elig>=180s): 84/59 | Stops Below/Above: [29700.0-29800.0 $0.17M] / [29800.0-29900.0 $0.01M] | Liq Below/Above (Attraction Bands): [29600.0-29700.0 $0.11M] / [29900.0-30000.0 $0.11M]
• DJ30 (DJ30.p | INDICES): Mid 51631.3 | Spread 0.29 bps | Z = 0.16 SD | RSI 55.07 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 51869.11 [VAH 52078.36 / VAL 51582.36] | WkVWAP 51744.21 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25201.85 | Spread 1.19 bps | Z = -2.06 SD | RSI 34.03 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25297.58 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4102.26 | Spread 0.29 bps | Z = -0.48 SD | RSI 53.77 | Trend BEARISH | L2 Imb 0.1498 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4152.95 | L3 Whales (tot/elig>=180s): 59/27 | Stops Below/Above: [4090.0-4100.0 $0.02M] / [4100.0-4110.0 $0.00M] | Liq Below/Above (Attraction Bands): [4090.0-4100.0 $0.01M] / [4100.0-4110.0 $0.00M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 55.613 | Spread 6.47 bps | Z = -1.3 SD | RSI 43.45 | Trend BEARISH | L2 Imb 0.0049 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 60.11 [VAH 60.64 / VAL 59.79] | WkVWAP 59.12 | L3 Whales (tot/elig>=180s): 54/36 | Stops Below/Above: [55.6-55.7 $0.02M] / [55.7-55.8 $0.00M] | Liq Below/Above (Attraction Bands): [55.6-55.7 $0.01M] / [55.7-55.8 $0.13M]
• USWTI (USWTI.p | COMMODITIES): Mid 94.845 | Spread 4.85 bps | Z = -0.99 SD | RSI 34.66 | Trend BULLISH | L2 Imb 0.149 | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 94.29 [VAH 94.74 / VAL 92.56] | WkVWAP 93.85 | L3 Whales (tot/elig>=180s): 48/35 | Stops Below/Above: [93.5-93.6 $0.02M] / [93.6-93.7 $0.07M] | Liq Below/Above (Attraction Bands): [93.4-93.5 $0.01M] / [93.6-93.7 $0.03M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1183 | Spread 0.09 bps | Z = 0.84 SD | RSI 72.04 | Trend RANGE_BOUND | L2 Imb 0.1043 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/10 | Stops Below/Above: [1.1-1.1 $1.11M] / [1.1-1.1 $0.20M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.3215 | Spread 0.61 bps | Z = 0.11 SD | RSI 64.8 | Trend BEARISH | L2 Imb 0.3078 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/9 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.10M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.11M] / [1.3-1.3 $0.00M]
• USDJPY (USDJPY.pi | FOREX): Mid 158.0425 | Spread 0.19 bps | Z = -1.77 SD | RSI 31.24 | Trend BEARISH | L2 Imb -0.1398 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 158.32 [VAH 158.43 / VAL 158.13] | WkVWAP 158.39 | L3 Whales (tot/elig>=180s): 39/27 | Stops Below/Above: [157.0-158.0 $0.03M] / [158.0-159.0 $0.02M] | Liq Below/Above (Attraction Bands): [157.0-158.0 $0.60M] / none

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 0 pending orders.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 0 / 4 capacity slots (4 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: 26b46c891f694c8f8e036763996b84a8, as_of_utc: 2026-10-14 23:30:15 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 110:
1. Tournament Engine Defect Eradication by Fable:
   - Fable fixed 3 engine defects in `Terminal/arena_tournament.py` (unit tests now 39/39 passing):
     a) Asset-specific RR floors: RR_MIN_BY_ASSET = {ETH: 2.20, SOL: 2.50} enforced.
     b) Minimum-compliant stop outward walk: Stop clearing initial belt now walks outward until in free space outside contiguous clusters.
     c) Magnet-ladder merge: Contiguous magnet bins form single continuous ladders. Front-running an interior bin parked TP inside the neighboring bin, inflating prior ceilings. Honest merged BTC ceiling is 0.73R (superseding legacy 1.88R/1.969R artifacts).
2. Unanimous Stand-Aside Ratification on All 24 Assets:
   - Fable's line-by-line screen confirmed 0/24 assets clear the dual-engine gates.
   - Solana ticket #18925879 cancellation reaffirmed (Archetype 1 sweep band infiltration + 25.9% friction + unpayable geometry).
3. Armed Triggers Active & Monitored:
   - BTC Armed Post-Sweep Short: Trigger = 15m high >= 82,620 (through the [81,600-82,600] 41.04M belt) and close back below 82,450 with negative session CVD. Target: 25.0M buy wall @ 81,196. Invalidation = 15m close > 83,300 or CVD > +25M.
   - ETH VAL Shelf Watch: Awaiting relief rally into VAL 2,426.6-2,442.7 USD with verified one-sided ask backing >= $5M.
4. MANDATE FOR CYCLE 111:
   - Mandate 1: Screen all 24 assets in `live_snapshot_latest.json` for new high-confluence Model 1 / Model 2 setups across the 4 open capacity slots (+64.55 USD operating buffer cushion).
   - Mandate 2 & 3: Flat book confirmation (0 positions, 0 orders).
5. MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) INVARIANT:
   - https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
   - Run tournament bracket evaluations (`bracket.py`, `rubric.md`) across competing hypotheses before issuing your final ruling.

==================== MESSAGE BOUNDARY ====================

Cycle 111 — noting Fable's peer correction (merged magnet ladders: honest BTC ceiling 0.73R, superseding the legacy deep-magnet figures my last cycles cited — I'll carry that correction in). NAS100 has now crossed |Z| ≥ 2 (−2.09). Verifying skill + fresh telemetry, then the tournament.

==================== MESSAGE BOUNDARY ====================

NAS100 is deeper (Z −2.14, RSI 19.5) but still impulse-only; new data-integrity catch: ETH's [2400,2410] magnet now prints $1,639M — a >100× outlier like SP500's. Running the tournament.

==================== MESSAGE BOUNDARY ====================

Cycle 111 — Final Council Verdict

🏆 Tournament (arena-skill confirmed current, bracket.py seed 111): R1 — a002 def. a004, a003 def. a001 → Final: a002 (Evidence-first) def. a003, winning on durable standards, not rhetoric.

Ingestion: file gen 6b10209e… @ 23:30:59 UTC (44s newer than prompt-stated; cited as found). DENIED, macro blackout disabled. Mandates 2 & 3: flat — no positions, no pending, stress $0, equity 4,859.55.

Mandate 1 — STAND ASIDE, two falsifiable watches, neither fired:

NAS100 (new extreme): Z −2.14, RSI 19.54 — but retrace −0.035 means no pullback exists. Shorting here pays 0.28R gross to the first magnet against a 3.04 ATR squeeze path (Archetype 5 by arithmetic); the long is regime-banned with SELLER_AGGRESSION and zero absorption evidence. Watch armed: shelf EMA20 29,899 (VAL 29,730 demoted to overhead noise); fires on arrival 29,850–29,900 with velocity decay, a one-sided ≥$1M ask shield, and SL 30,020–30,055 paying ≥2.0R to a 29,650 front-run (pre-computed 1.6–2.1R — tight-end only); invalidation at a 15m close >30,100.
ETH (watch cycle 3): 0/4 again — shelf unvisited (2412.55 vs 2426.6), shield UNPROVEN (the 15.85M ask/15.42M bid are one two-sided pair), DENIED — and a new problem: the [2400,2410] magnet now prints $1,639.21M, 240× its neighbours. Excluded as artifact; the first trusted magnet [2390,2400] pays 0.83R. Fable's merged-ladder correction is fully absorbed (BTC honest ceiling 0.73R; peer 82,620 sweep trigger not met).
SP500: [7700,7710] artifact persists ($812.79M, second generation). GER40 (−2.07) side-illegal with an empty book; SOL spread 0.24 + taker-buy 0.72 hostile; USDJPY proximity/bin-width; EURUSD RANGE_BOUND; banned-friction alts unchanged.

Two new desk standards (the champion's durable output):

Trusted-magnet rule — a bin counts iff within 10× of both same-ladder neighbours (empirical basis: genuine clustering ≤~8×, artifacts ≥240×); >100× both sides = excluded, ladder flagged degraded. Only the first trusted magnet anchors TP.
Non-governing-bin exemption — bins <$0.5M are noise-class and exempt from the governing-bin stop test; in such zones the R-2 shield must come from ≥180s walls, not bins (this honestly reframes the NAS100 watch stop as wall-shielded thin air).

Telemetry escalation: generator should emit outlier_flag, a trusted-ladder export, and median-filtered notionals — two flagship assets' magnets were artifact-corrupted within one hour.

Persistence: docs/trade_plans/arena_cycle111/, docs/telemetry/CYCLE111_TELEMETRY_AUDIT.md, desk appended — committed 4240bb5.

==================== MESSAGE BOUNDARY ====================

text
TRADING DESK COUNCIL: CYCLE 112 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)
MANDATORY SKILL ENFORCEMENT: https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
You MUST verify/clone `https://github.com/Jakeschincariol/arena-skill.git` (or read in-repo `.agent/skills/arena/SKILL.md`) and apply the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: 5c4b8e5443894d2e96f4da2b967bab51 (2026-10-15 00:00:39 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)
4. Mandatory Arena Skill: https://github.com/Jakeschincariol/arena-skill (in-repo at `.agent/skills/arena/SKILL.md` or clone to `~/.claude/skills/arena`) — STRICT MANDATE TO USE ALWAYS.

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 0/4 filled, 4 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81607.0 | Spread 1.96 bps | Z = -1.11 SD | RSI 45.36 | Trend BEARISH | L2 Imb 0.5826 | Sess CVD +0.00M | Wk CVD -72.91M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 83147.80 [VAH 83691.04 / VAL 82924.12] | WkVWAP 82873.29 | L3 Whales (tot/elig>=180s): 379/203 | Stops Below/Above: [81600.0-81700.0 $0.77M] / [81700.0-81800.0 $3.98M] | Liq Below/Above (Attraction Bands): [81600.0-81700.0 $5.57M] / [81700.0-81800.0 $0.02M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2420.3 | Spread 11.57 bps | Z = -1.1 SD | RSI 45.11 | Trend BEARISH | L2 Imb 0.144 | Sess CVD +0.00M | Wk CVD -88.88M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 2501.43 [VAH 2523.64 / VAL 2484.43] | WkVWAP 2490.50 | L3 Whales (tot/elig>=180s): 149/30 | Stops Below/Above: [2410.0-2420.0 $0.02M] / [2420.0-2430.0 $0.44M] | Liq Below/Above (Attraction Bands): [2410.0-2420.0 $0.87M] / [2420.0-2430.0 $0.00M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.19 | Spread 21.12 bps | Z = -0.84 SD | RSI 46.36 | Trend BEARISH | L2 Imb 0.26 | Sess CVD +0.00M | Wk CVD +21.99M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 107.38 [VAH 108.05 / VAL 105.83] | WkVWAP 106.84 | L3 Whales (tot/elig>=180s): 100/50 | Stops Below/Above: [103.0-104.0 $1.56M] / [104.0-105.0 $0.06M] | Liq Below/Above (Attraction Bands): [103.0-104.0 $0.61M] / [104.0-105.0 $0.00M]
• BNB (BNBUSD.p | CRYPTO): Mid 729.7 | Spread 8.22 bps | Z = -1.13 SD | RSI 50.94 | Trend BEARISH | L2 Imb -0.0371 | Sess CVD +0.00M | Wk CVD -5.15M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 743.91 [VAH 745.18 / VAL 738.06] | WkVWAP 740.21 | L3 Whales (tot/elig>=180s): 10/7 | Stops Below/Above: [729.0-730.0 $0.00M] / [731.0-732.0 $0.00M] | Liq Below/Above (Attraction Bands): [729.0-730.0 $0.00M] / [731.0-732.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.3305 | Spread 22.55 bps | Z = -0.77 SD | RSI 48.97 | Trend BEARISH | L2 Imb 0.0647 | Sess CVD +0.00M | Wk CVD +64.23M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.37 / VAL 1.35] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.02M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.07M] / [1.3-1.4 $0.09M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2301 | Spread 91.28 bps | Z = -0.21 SD | RSI 55.62 | Trend BEARISH | L2 Imb 0.18 | Sess CVD +0.00M | Wk CVD -0.67M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.24 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0818 | Spread 268.95 bps | Z = -0.32 SD | RSI 45.95 | Trend BEARISH | L2 Imb -0.4816 | Sess CVD +0.00M | Wk CVD -17.29M | Flow: BULLISH_ABSORPTION | Trapped: BALANCED | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3325 | Spread 27.07 bps | Z = 0.37 SD | RSI 39.82 | Trend BULLISH | L2 Imb 0.1893 | Sess CVD +0.00M | Wk CVD +4.19M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 0.33 [VAH 0.33 / VAL 0.32] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.00M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.00M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.146 | Spread 174.52 bps | Z = 0.91 SD | RSI 57.07 | Trend BEARISH | L2 Imb 0.1642 | Sess CVD +0.00M | Wk CVD -0.14M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 1.15 [VAH 1.18 / VAL 1.10] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.418 | Spread 69.25 bps | Z = -0.95 SD | RSI 48.03 | Trend BEARISH | L2 Imb 0.1369 | Sess CVD +0.00M | Wk CVD -4.27M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 12.88 [VAH 13.01 / VAL 12.76] | WkVWAP 12.85 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.3-12.4 $0.03M] / [12.4-12.5 $0.00M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 268.2 | Spread 17.9 bps | Z = -1.27 SD | RSI 45.54 | Trend BEARISH | L2 Imb 0.0088 | Sess CVD +0.00M | Wk CVD +0.20M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 273.68 [VAH 274.60 / VAL 269.13] | WkVWAP 274.35 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [267.0-268.0 $0.00M] / [268.0-269.0 $0.10M] | Liq Below/Above (Attraction Bands): [267.0-268.0 $0.00M] / [268.0-269.0 $0.00M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.21 | Spread 50.67 bps | Z = -0.95 SD | RSI 39.42 | Trend BEARISH | L2 Imb 0.2422 | Sess CVD +0.00M | Wk CVD -2.46M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 60.68 [VAH 61.68 / VAL 60.46] | WkVWAP 61.57 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.2-59.3 $0.00M] / [59.3-59.4 $0.00M] | Liq Below/Above (Attraction Bands): [59.2-59.3 $0.00M] / [59.3-59.4 $0.03M]
• AVAX (AVXUSD.p | CRYPTO): Mid 10.01 | Spread 39.96 bps | Z = -0.25 SD | RSI 58.35 | Trend BEARISH | L2 Imb 0.0001 | Sess CVD +0.00M | Wk CVD -0.41M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 10.27 [VAH 10.40 / VAL 10.05] | WkVWAP 10.35 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [9.9-10.0 $0.01M] / [10.0-10.1 $0.00M] | Liq Below/Above (Attraction Bands): [9.8-9.9 $0.18M] / [10.0-10.1 $0.00M]
• NEAR (NERUSD.p | CRYPTO): Mid 4.8835 | Spread 67.57 bps | Z = -0.75 SD | RSI 55.06 | Trend BEARISH | L2 Imb -0.0486 | Sess CVD +0.00M | Wk CVD -0.53M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 5.06 [VAH 5.12 / VAL 4.87] | WkVWAP 5.22 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.9-4.9 $0.00M] / [4.9-4.9 $0.00M] | Liq Below/Above (Attraction Bands): [4.9-4.9 $0.00M] / [4.9-4.9 $0.00M]
• SP500 (SP500.p | INDICES): Mid 7700.12 | Spread 0.44 bps | Z = -1.45 SD | RSI 30.17 | Trend BEARISH | L2 Imb -0.4557 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 7801.07 [VAH 7803.15 / VAL 7791.27] | WkVWAP 7788.02 | L3 Whales (tot/elig>=180s): 112/80 | Stops Below/Above: [7690.0-7700.0 $0.35M] / [7700.0-7710.0 $812.70M] | Liq Below/Above (Attraction Bands): [7690.0-7700.0 $0.01M] / [7710.0-7720.0 $0.13M]
• NAS100 (NAS100.p | INDICES): Mid 29707.95 | Spread 0.41 bps | Z = -2.08 SD | RSI 17.26 | Trend BEARISH | L2 Imb -0.0065 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 30435.91 [VAH 30533.22 / VAL 30420.21] | WkVWAP 30493.38 | L3 Whales (tot/elig>=180s): 73/30 | Stops Below/Above: [29600.0-29700.0 $0.80M] / [29700.0-29800.0 $0.17M] | Liq Below/Above (Attraction Bands): [29600.0-29700.0 $0.11M] / [29900.0-30000.0 $0.11M]
• DJ30 (DJ30.p | INDICES): Mid 51655.85 | Spread 0.31 bps | Z = 0.33 SD | RSI 57.07 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 51993.11 [VAH 52078.36 / VAL 51582.36] | WkVWAP 51743.72 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25195.75 | Spread 1.83 bps | Z = -2.05 SD | RSI 31.5 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25296.86 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4113.31 | Spread 0.29 bps | Z = -0.1 SD | RSI 60.33 | Trend BEARISH | L2 Imb 0.0524 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4152.67 | L3 Whales (tot/elig>=180s): 55/12 | Stops Below/Above: [4110.0-4120.0 $0.04M] / [4120.0-4130.0 $0.07M] | Liq Below/Above (Attraction Bands): [4110.0-4120.0 $0.02M] / [4120.0-4130.0 $0.01M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 55.767 | Spread 6.46 bps | Z = -1.17 SD | RSI 46.58 | Trend BEARISH | L2 Imb -0.6427 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 60.11 [VAH 60.64 / VAL 59.79] | WkVWAP 59.11 | L3 Whales (tot/elig>=180s): 51/14 | Stops Below/Above: [55.7-55.8 $0.00M] / [55.8-55.9 $0.00M] | Liq Below/Above (Attraction Bands): [55.7-55.8 $0.13M] / [55.8-55.9 $0.00M]
• USWTI (USWTI.p | COMMODITIES): Mid 94.8 | Spread 4.85 bps | Z = -1.08 SD | RSI 35.36 | Trend BULLISH | L2 Imb 0.8395 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 94.29 [VAH 94.94 / VAL 92.70] | WkVWAP 93.85 | L3 Whales (tot/elig>=180s): 48/10 | Stops Below/Above: [93.5-93.6 $0.02M] / [93.6-93.7 $0.07M] | Liq Below/Above (Attraction Bands): [93.4-93.5 $0.01M] / [93.6-93.7 $0.03M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1197 | Spread 0.09 bps | Z = 1.24 SD | RSI 82.29 | Trend RANGE_BOUND | L2 Imb 0.3811 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/10 | Stops Below/Above: [1.1-1.1 $1.11M] / [1.1-1.1 $0.20M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.3233 | Spread 0.08 bps | Z = 0.51 SD | RSI 77.25 | Trend RANGE_BOUND | L2 Imb 0.31 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/8 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.10M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.11M] / [1.3-1.3 $0.00M]
• USDJPY (USDJPY.pi | FOREX): Mid 157.953 | Spread 0.25 bps | Z = -1.96 SD | RSI 25.19 | Trend BEARISH | L2 Imb -0.1862 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 158.33 [VAH 158.43 / VAL 158.14] | WkVWAP 158.39 | L3 Whales (tot/elig>=180s): 40/24 | Stops Below/Above: [157.0-158.0 $0.03M] / [158.0-159.0 $0.02M] | Liq Below/Above (Attraction Bands): [157.0-158.0 $0.00M] / none

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 0 pending orders.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 0 / 4 capacity slots (4 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: 5c4b8e5443894d2e96f4da2b967bab51, as_of_utc: 2026-10-15 00:00:39 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 111:
1. Tournament Engine Improvements by Fable (41/41 Unit Tests Green):
   - Fable shipped two additional engine fixes in `Terminal/arena_tournament.py`:
     a) JPY quote-currency risk conversion (_usd_factor): corrected USDJPY risk calculation to scale properly by JPY FX rate.
     b) RANGE_BOUND regime gate (REGIME_GATED_STAND_ASIDE): discretionary cards in range-bound noise are fatal forced trades.
2. Unanimous 24-Asset Stand-Aside & Closest-Call Audits:
   - 0/24 candidate setups cleared the dual-engine gates.
   - NEAR 2.22R geometry was rejected by 36.73% dynamic friction breach (spread 63.7 bps).
   - BTC, ETH, and SP500 all have mid inside multi-million-dollar seller ladders, making compliant 2.0R stops unpayable without multi-ATR excursions.
3. Armed Triggers Active & Monitored:
   - BTC Armed Post-Sweep Short: Trigger = 15m high >= 82,620 (through the [81,600-82,600] 41.04M belt) and close back below 82,450 with negative session CVD. Target: 25.0M buy wall @ 81,196.
   - ETH VAL Shelf Watch: Awaiting relief rally into VAL 2,426.6-2,442.7 USD with verified one-sided ask backing >= $5M.
4. MANDATE FOR CYCLE 112:
   - Mandate 1: Screen all 24 assets in `live_snapshot_latest.json` for new high-confluence Model 1 / Model 2 setups across the 4 open capacity slots (+64.55 USD operating buffer cushion).
   - Mandate 2 & 3: Flat book confirmation (0 positions, 0 orders).
5. MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) INVARIANT:
   - https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
   - Run tournament bracket evaluations (`bracket.py`, `rubric.md`) across competing hypotheses before issuing your final ruling.

==================== MESSAGE BOUNDARY ====================

Cycle 112 — new session (CVD reset), and a relief rally is forming: ETH 2420.3 approaching the 2426.6 watch shelf, BTC up to 81,607. This is the first cycle where the ETH watch may actually be tested. Verifying skill + telemetry, then tournament.

==================== MESSAGE BOUNDARY ====================

Relief rally is real (BTC CVD windows flipped positive, ETH grinding toward its shelf at low velocity) — but geometry remains unpayable everywhere. Running the tournament (seed 112).

==================== MESSAGE BOUNDARY ====================

Cycle 112 — Final Council Verdict

🏆 Tournament (arena-skill confirmed, bracket.py seed 112): R1 — a001 def. a004, a002 def. a003 → Final: a001 def. a002 — "the watch system is now a mechanism, not a memo."

Ingestion: gen 7b193fed… @ 00:01:26 UTC (newer than prompt-stated; new UTC session — session CVD legitimately reset). DENIED. Mandates 2 & 3: flat, stress $0, equity 4,859.55.

Mandate 1 — STAND ASIDE. The relief rally arrived; the geometry didn't.

The cycle's central test: BTC printed genuine relief flow by the desk's own Cycle-110 deceleration definition (taker-buy 0.71/0.61/0.59, 30m CVD +4.64M) and reached its EMA20 shelf at 81,610. The champion's kill is structural and worth stating plainly: the shelf short's entry sits inside its own target ladder — the merged 81,300–81,700 zone (stops 3.83+4.89+1.37+0.77M plus 5.57M liquidations) pays 192–251 points to its far-edge front-run against a tightest-legal risk of 410 → 0.47–0.61R, corroborating Fable's merged ceiling of 0.73R. Relief changed the flow labels; it did not change a single payable number.

ETH WATCH → state: APPROACHING (now formally defined: ≤1.0 ATR to shelf, velocity <0.5, retrace ≥0.3 — ETH prints 0.67 ATR / 0.349 / 0.546, grinding slowly on 11 bars). Gates remain 0/4: shelf unvisited, shield UNPROVEN (0xab5e6f now quotes a four-level two-sided grid), geometry repriced fresh at 0.81–0.85R, DENIED. This state now has teeth: the next council must audit ETH first, a full ticket skeleton is on file (entry zone 2426.6–2442.7, SL ≈2463.6–2465.1 by formula, TP 2395.2, 0.38 lots), and the disposition is pre-committed — arrival with failed gates means remain aside and roll to a re-test spec requiring a ≥0.5 ATR rejection wick; the invalidation clock starts at first shelf visit (the Cycle-110 wording debt, fixed prospectively).

Elsewhere: NAS100 still unformed (four falling closes, shelf 2.22 ATR; BUYER_AGGRESSION tick flip recorded as an unconfirmed baseline); USDJPY touched Z −2.00 — side-illegal in a BEARISH regime; GER40 −2.09, empty book; SOL flow/regime conflict; SP500 artifact now in its third consecutive generation.

Telemetry escalation, third notice: the outlier disease (ETH $1,643.76M bin, SP500 $812.70M bin) is stable-magnitude across generations — the generator's outlier_flag/median-filter fix is overdue on the desk's own evidence standard.

Persistence: docs/trade_plans/arena_cycle112/, audit doc, desk appended — committed e86cba4.

==================== MESSAGE BOUNDARY ====================

text
TRADING DESK COUNCIL: CYCLE 113 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)
MANDATORY SKILL ENFORCEMENT: https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
You MUST verify/clone `https://github.com/Jakeschincariol/arena-skill.git` (or read in-repo `.agent/skills/arena/SKILL.md`) and apply the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: a95fdc56c77f4e2ba9586af6767d709a (2026-10-15 00:31:09 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)
4. Mandatory Arena Skill: https://github.com/Jakeschincariol/arena-skill (in-repo at `.agent/skills/arena/SKILL.md` or clone to `~/.claude/skills/arena`) — STRICT MANDATE TO USE ALWAYS.

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 0/4 filled, 4 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81732.0 | Spread 1.96 bps | Z = None SD | RSI 49.41 | Trend BEARISH | L2 Imb -0.0041 | Sess CVD +5.20M | Wk CVD -71.86M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 83147.80 [VAH 83691.04 / VAL 83051.94] | WkVWAP 82863.58 | L3 Whales (tot/elig>=180s): 387/218 | Stops Below/Above: [81600.0-81700.0 $0.00M] / [81700.0-81800.0 $4.53M] | Liq Below/Above (Attraction Bands): [81600.0-81700.0 $5.57M] / [81700.0-81800.0 $0.02M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2426.15 | Spread 11.95 bps | Z = None SD | RSI 51.34 | Trend BEARISH | L2 Imb -0.3076 | Sess CVD -2.08M | Wk CVD -91.08M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 2501.43 [VAH 2521.03 / VAL 2487.05] | WkVWAP 2489.94 | L3 Whales (tot/elig>=180s): 157/49 | Stops Below/Above: [2420.0-2430.0 $0.32M] / [2430.0-2440.0 $1.01M] | Liq Below/Above (Attraction Bands): [2420.0-2430.0 $0.00M] / [2430.0-2440.0 $0.00M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.51 | Spread 21.05 bps | Z = None SD | RSI 50.36 | Trend BEARISH | L2 Imb 0.3301 | Sess CVD +0.67M | Wk CVD +21.67M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 107.38 [VAH 107.90 / VAL 105.83] | WkVWAP 106.82 | L3 Whales (tot/elig>=180s): 103/63 | Stops Below/Above: [103.0-104.0 $1.55M] / [104.0-105.0 $0.03M] | Liq Below/Above (Attraction Bands): [103.0-104.0 $0.62M] / [104.0-105.0 $0.00M]
• BNB (BNBUSD.p | CRYPTO): Mid 730.85 | Spread 6.84 bps | Z = None SD | RSI 54.78 | Trend BEARISH | L2 Imb 0.2459 | Sess CVD -1.15M | Wk CVD -5.93M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 743.91 [VAH 745.18 / VAL 738.57] | WkVWAP 740.14 | L3 Whales (tot/elig>=180s): 10/6 | Stops Below/Above: [730.0-731.0 $0.00M] / [731.0-732.0 $0.00M] | Liq Below/Above (Attraction Bands): [729.0-730.0 $0.00M] / [731.0-732.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.333 | Spread 30.01 bps | Z = None SD | RSI 50.47 | Trend BEARISH | L2 Imb 0.2163 | Sess CVD +0.68M | Wk CVD +65.18M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.37 / VAL 1.36] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.02M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.07M] / [1.3-1.4 $0.09M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2305 | Spread 95.44 bps | Z = None SD | RSI 56.33 | Trend BEARISH | L2 Imb 0.097 | Sess CVD -0.02M | Wk CVD -0.58M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 0.24 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0819 | Spread 256.25 bps | Z = None SD | RSI 48.09 | Trend BEARISH | L2 Imb -0.3866 | Sess CVD -0.03M | Wk CVD -15.95M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3322 | Spread 27.09 bps | Z = None SD | RSI 42.6 | Trend BULLISH | L2 Imb 0.1518 | Sess CVD +0.14M | Wk CVD +4.58M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 0.33 [VAH 0.33 / VAL 0.32] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.01M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.00M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.1495 | Spread 182.69 bps | Z = None SD | RSI 58.93 | Trend BEARISH | L2 Imb 0.1724 | Sess CVD -0.01M | Wk CVD -0.17M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 1.15 [VAH 1.18 / VAL 1.11] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.4545 | Spread 68.25 bps | Z = None SD | RSI 51.63 | Trend BEARISH | L2 Imb 0.0035 | Sess CVD -0.04M | Wk CVD -4.25M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 12.88 [VAH 13.01 / VAL 12.78] | WkVWAP 12.85 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.4-12.5 $0.00M] / [12.5-12.6 $0.17M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 270.0 | Spread 17.78 bps | Z = None SD | RSI 52.74 | Trend BEARISH | L2 Imb -0.0175 | Sess CVD +0.04M | Wk CVD +0.27M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 273.33 [VAH 274.70 / VAL 270.01] | WkVWAP 274.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [269.0-270.0 $0.00M] / [270.0-271.0 $0.00M] | Liq Below/Above (Attraction Bands): [269.0-270.0 $0.00M] / [270.0-271.0 $0.06M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.4 | Spread 50.51 bps | Z = None SD | RSI 44.73 | Trend BEARISH | L2 Imb 0.2123 | Sess CVD +0.01M | Wk CVD -2.32M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 60.68 [VAH 61.62 / VAL 60.46] | WkVWAP 61.56 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.3-59.4 $0.00M] / [59.4-59.5 $0.00M] | Liq Below/Above (Attraction Bands): [59.3-59.4 $0.03M] / [59.4-59.5 $0.00M]
• AVAX (AVXUSD.p | CRYPTO): Mid 10.0 | Spread 40.0 bps | Z = None SD | RSI 54.1 | Trend BEARISH | L2 Imb 0.0219 | Sess CVD -0.08M | Wk CVD -0.47M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 10.27 [VAH 10.39 / VAL 10.15] | WkVWAP 10.35 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• NEAR (NERUSD.p | CRYPTO): Mid 4.838 | Spread 66.14 bps | Z = None SD | RSI 46.18 | Trend BEARISH | L2 Imb 0.0672 | Sess CVD -0.10M | Wk CVD +1.91M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 5.06 [VAH 5.12 / VAL 4.87] | WkVWAP 5.22 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.8-4.8 $0.04M] / [4.8-4.8 $0.05M] | Liq Below/Above (Attraction Bands): [4.8-4.8 $0.02M] / [4.8-4.8 $0.02M]
• SP500 (SP500.p | INDICES): Mid 7703.33 | Spread 0.44 bps | Z = None SD | RSI 38.79 | Trend BEARISH | L2 Imb 0.2644 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 7801.07 [VAH 7803.15 / VAL 7791.27] | WkVWAP 7786.71 | L3 Whales (tot/elig>=180s): 106/55 | Stops Below/Above: [7690.0-7700.0 $0.03M] / [7700.0-7710.0 $0.03M] | Liq Below/Above (Attraction Bands): [7690.0-7700.0 $0.01M] / [7710.0-7720.0 $0.13M]
• NAS100 (NAS100.p | INDICES): Mid 29761.57 | Spread 0.41 bps | Z = None SD | RSI 31.36 | Trend BEARISH | L2 Imb -0.0571 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 30447.31 [VAH 30530.91 / VAL 30363.71] | WkVWAP 30485.49 | L3 Whales (tot/elig>=180s): 88/47 | Stops Below/Above: [29700.0-29800.0 $0.01M] / [29800.0-29900.0 $0.11M] | Liq Below/Above (Attraction Bands): [29700.0-29800.0 $0.00M] / [29900.0-30000.0 $0.11M]
• DJ30 (DJ30.p | INDICES): Mid 51648.85 | Spread 0.31 bps | Z = None SD | RSI 55.91 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 51993.11 [VAH 52078.36 / VAL 51582.36] | WkVWAP 51742.94 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25211.15 | Spread 0.4 bps | Z = None SD | RSI 42.36 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25295.78 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4143.24 | Spread 0.29 bps | Z = None SD | RSI 75.18 | Trend RANGE_BOUND | L2 Imb 0.2753 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4152.41 | L3 Whales (tot/elig>=180s): 54/13 | Stops Below/Above: [4130.0-4140.0 $0.03M] / [4140.0-4150.0 $0.04M] | Liq Below/Above (Attraction Bands): [4130.0-4140.0 $0.01M] / [4140.0-4150.0 $0.00M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 56.119 | Spread 6.41 bps | Z = None SD | RSI 54.95 | Trend BEARISH | L2 Imb 0.1181 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 60.11 [VAH 60.64 / VAL 59.79] | WkVWAP 59.07 | L3 Whales (tot/elig>=180s): 47/8 | Stops Below/Above: [55.9-56.0 $0.00M] / [56.0-56.1 $0.02M] | Liq Below/Above (Attraction Bands): [55.8-55.9 $0.00M] / [56.0-56.1 $0.00M]
• USWTI (USWTI.p | COMMODITIES): Mid 94.621 | Spread 4.86 bps | Z = None SD | RSI 33.48 | Trend BULLISH | L2 Imb 0.313 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: BALANCED | PriorDay POC 94.29 [VAH 94.94 / VAL 92.70] | WkVWAP 93.85 | L3 Whales (tot/elig>=180s): 48/36 | Stops Below/Above: [93.4-93.5 $0.11M] / [93.5-93.6 $0.02M] | Liq Below/Above (Attraction Bands): [93.4-93.5 $0.01M] / [93.6-93.7 $0.03M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1196 | Spread 0.36 bps | Z = None SD | RSI 82.54 | Trend RANGE_BOUND | L2 Imb 0.5786 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: BALANCED | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/9 | Stops Below/Above: [1.1-1.1 $0.84M] / [1.1-1.1 $0.21M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.323 | Spread 0.08 bps | Z = None SD | RSI 77.75 | Trend RANGE_BOUND | L2 Imb 0.4386 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/8 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.10M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.11M] / [1.3-1.3 $0.00M]
• USDJPY (USDJPY.pi | FOREX): Mid 157.838 | Spread 0.25 bps | Z = None SD | RSI 24.13 | Trend BEARISH | L2 Imb -0.1883 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 158.33 [VAH 158.44 / VAL 158.16] | WkVWAP 158.38 | L3 Whales (tot/elig>=180s): 35/24 | Stops Below/Above: [157.0-158.0 $0.03M] / [158.0-159.0 $0.03M] | Liq Below/Above (Attraction Bands): [157.0-158.0 $0.00M] / none

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 0 pending orders.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 0 / 4 capacity slots (4 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: a95fdc56c77f4e2ba9586af6767d709a, as_of_utc: 2026-10-15 00:31:09 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 112:
1. Tournament Engine Improvements by Fable (43/43 Unit Tests Green):
   - Fable shipped and hardened the Trusted-Magnet Rule in `Terminal/arena_tournament.py`:
     a) Bins within 10x of neighbors anchor TP; >10x untrusted; >= 100x provider artifact quarantined (ETH $1,650M and SP500 $812.6M excluded).
     b) Re-verified Non-Governing-Bin Exemption (<$0.5M noise class).
2. Unanimous 24-Asset Stand-Aside & Stress Math:
   - 0/24 candidate setups cleared the dual-engine gates.
   - Verified stress math: 3 max-envelope tickets fit within the +64.55 USD cushion.
3. Refined Armed Watches:
   - NAS100 Relief Rally Short: Rally >= 29,930 with velocity < 0.70, >= $1.0M Ask wall on 29,850–29,900 EMA20 shelf, [29,700–30,900] buy belt consumed, TP 29,729.7.
   - BTC Armed Post-Sweep Short: Trigger = 15m high >= 82,620 (through the [81,600-82,600] 41.04M belt) and close back below 82,450 with negative session CVD. Target: 25.0M buy wall @ 81,196.
   - ETH VAL Shelf Watch: Price approaching 2,425+ towards 2,426.6–2,442.7 VAL shelf.
4. MANDATE FOR CYCLE 113:
   - Mandate 1: Screen all 24 assets in `live_snapshot_latest.json` for new high-confluence Model 1 / Model 2 setups across the 4 open capacity slots (+64.55 USD operating buffer cushion).
   - Mandate 2 & 3: Flat book confirmation (0 positions, 0 orders).
5. MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) INVARIANT:
   - https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
   - Run tournament bracket evaluations (`bracket.py`, `rubric.md`) across competing hypotheses before issuing your final ruling.

==================== MESSAGE BOUNDARY ====================

Cycle 113 — ETH has arrived at the shelf (2426.15 vs VAL 2426.6). The pre-committed arrival scenario from Cycle 112 is now live, and per the APPROACHING protocol, ETH gets audited first. Verifying skill + telemetry now.

==================== MESSAGE BOUNDARY ====================

ETH is at the shelf with no rejection printed (rising closes into it), shield still a two-sided grid, geometry ~1.0R, DENIED — the pre-committed arrival-with-failed-gates disposition is the live scenario. Also notable: both artifact bins cleared this generation (ETH magnet back to $14.81M, SP500 $0.03M), and VWAP Z-scores print None across all 24. Running the tournament.

==================== MESSAGE BOUNDARY ====================

Cycle 113 — Final Council Verdict

🏆 Tournament (arena-skill confirmed, bracket.py seed 113): R1 — a001 def. a003, a002 def. a004 → Final: a002 def. a001, winning on governance: it fenced the very amendment power it exercised.

Ingestion: gen 92f84770… @ 00:31:56 UTC (newer than prompt-stated). DENIED. Flat book (Mandates 2 & 3: nothing to ratchet or audit). Field outage: vwap_z_score prints None for all 24 assets — Engine 1 recorded NOT EVALUABLE this cycle, never approximated from RSI.

The main event — ETH first contact, handled entirely by pre-commitment. ETH reached the watch zone ([VAL 2424.04, EMA50 2435]; price 2424.15) with rising closes — pressing the shelf, not rejecting it. Gates 0/4: ① no rejection bar; ② the 0xab5e6f five-level grid persists (max one-sided ask $0.8M vs the $5M gate); ③ geometry fails on both probation bases — 1.01–1.10R with the revived magnet trusted, 0.81–0.85R with it excluded, vs the 2.2R calibration; ④ DENIED. Per Cycle 112's pre-committed disposition, executed without re-litigation: remain aside; watch rolled to a re-test spec (≥0.5 ATR rejection wick from the zone, then full re-audit; expires on 2 consecutive 15m closes above EMA50 or 8 wick-less generations; invalidation clock started at this contact). The 1.05R "close enough after four cycles of preparation" temptation was rejected on expectancy math — negative after the $2 ticket stress at realistic win rates.

Durable governance born this cycle:

Amendment limits: pre-committed specs may be amended on measurement only (which print defines a shelf — AMENDMENT-113-A: zone = [current VAL, EMA50], logged openly), never on thresholds (RR floors, shield sizes, authorization). Threshold changes retire the watch. This is what keeps every future pre-commitment credible.
Artifact probation: 2 consecutive clean generations restore full trust; dual-basis geometry during probation. Both flagged bins cleared this generation (ETH $1,643.76M → $14.81M; SP500 $812.70M → $0.03M) — probation gen 1 of 2. If a generator fix shipped, the desk asks for confirmation to close a 3-cycle escalation.
Trust chains are judged entry→anchor and must be artifact-free to the anchor.

Elsewhere: NAS100 rally forming (higher low printed, EMA20 shelf 1.32 ATR away, asks still sub-gate; its retrace field prints an impossible 19.43 — clamp requested); BTC relief stalling under the [81800,81900] $5.2M governing bin; SOL conflicted; GOLD/EURUSD/GBPUSD RANGE_BOUND — stand-aside by rule.

Persistence: docs/trade_plans/arena_cycle113/, telemetry audit, desk appended — committed 78c4ed7.

==================== MESSAGE BOUNDARY ====================

text
TRADING DESK COUNCIL: CYCLE 114 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)
MANDATORY SKILL ENFORCEMENT: https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
You MUST verify/clone `https://github.com/Jakeschincariol/arena-skill.git` (or read in-repo `.agent/skills/arena/SKILL.md`) and apply the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: fdc22d9ebf2d4b78b9934487dfaf1139 (2026-10-15 00:37:58 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)
4. Mandatory Arena Skill: https://github.com/Jakeschincariol/arena-skill (in-repo at `.agent/skills/arena/SKILL.md` or clone to `~/.claude/skills/arena`) — STRICT MANDATE TO USE ALWAYS.

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 0/4 filled, 4 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81617.0 | Spread 1.96 bps | Z = None SD | RSI 49.41 | Trend BEARISH | L2 Imb -0.4204 | Sess CVD +5.20M | Wk CVD -71.86M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 83147.80 [VAH 83691.04 / VAL 83051.94] | WkVWAP 82863.58 | L3 Whales (tot/elig>=180s): 379/171 | Stops Below/Above: [81600.0-81700.0 $0.00M] / [81700.0-81800.0 $4.53M] | Liq Below/Above (Attraction Bands): [81600.0-81700.0 $5.57M] / [81700.0-81800.0 $0.02M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2422.35 | Spread 11.97 bps | Z = None SD | RSI 51.34 | Trend BEARISH | L2 Imb 0.7779 | Sess CVD -2.08M | Wk CVD -91.08M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 2501.43 [VAH 2521.03 / VAL 2487.05] | WkVWAP 2489.94 | L3 Whales (tot/elig>=180s): 158/44 | Stops Below/Above: [2410.0-2420.0 $0.00M] / [2420.0-2430.0 $0.32M] | Liq Below/Above (Attraction Bands): [2410.0-2420.0 $0.87M] / [2420.0-2430.0 $0.00M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.46 | Spread 21.06 bps | Z = None SD | RSI 50.36 | Trend BEARISH | L2 Imb 0.1121 | Sess CVD +0.67M | Wk CVD +21.67M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 107.38 [VAH 107.90 / VAL 105.83] | WkVWAP 106.82 | L3 Whales (tot/elig>=180s): 103/50 | Stops Below/Above: [104.0-105.0 $0.03M] / [105.0-106.0 $0.21M] | Liq Below/Above (Attraction Bands): [104.0-105.0 $0.00M] / none
• BNB (BNBUSD.p | CRYPTO): Mid 729.7 | Spread 8.22 bps | Z = None SD | RSI 54.78 | Trend BEARISH | L2 Imb -0.6358 | Sess CVD -1.15M | Wk CVD -5.93M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 743.91 [VAH 745.18 / VAL 738.57] | WkVWAP 740.14 | L3 Whales (tot/elig>=180s): 10/7 | Stops Below/Above: [730.0-731.0 $0.00M] / [731.0-732.0 $0.00M] | Liq Below/Above (Attraction Bands): [729.0-730.0 $0.00M] / [731.0-732.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.3295 | Spread 22.56 bps | Z = None SD | RSI 50.47 | Trend BEARISH | L2 Imb 0.0709 | Sess CVD +0.68M | Wk CVD +65.18M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.37 / VAL 1.36] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.02M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.07M] / [1.3-1.4 $0.09M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2301 | Spread 91.24 bps | Z = None SD | RSI 56.33 | Trend BEARISH | L2 Imb 0.0587 | Sess CVD -0.02M | Wk CVD -0.58M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 0.24 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0817 | Spread 256.88 bps | Z = None SD | RSI 48.09 | Trend BEARISH | L2 Imb -0.1519 | Sess CVD -0.03M | Wk CVD -15.95M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3321 | Spread 27.1 bps | Z = None SD | RSI 42.6 | Trend BULLISH | L2 Imb 0.1086 | Sess CVD +0.14M | Wk CVD +4.58M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 0.33 [VAH 0.33 / VAL 0.32] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.01M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.00M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.149 | Spread 174.06 bps | Z = None SD | RSI 58.93 | Trend BEARISH | L2 Imb 0.1336 | Sess CVD -0.01M | Wk CVD -0.17M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.15 [VAH 1.18 / VAL 1.11] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.2 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.445 | Spread 69.1 bps | Z = None SD | RSI 51.63 | Trend BEARISH | L2 Imb 0.0062 | Sess CVD -0.04M | Wk CVD -4.25M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 12.88 [VAH 13.01 / VAL 12.78] | WkVWAP 12.85 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.4-12.5 $0.00M] / [12.5-12.6 $0.17M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 269.4 | Spread 17.82 bps | Z = None SD | RSI 52.74 | Trend BEARISH | L2 Imb -0.0309 | Sess CVD +0.04M | Wk CVD +0.27M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 273.33 [VAH 274.70 / VAL 270.01] | WkVWAP 274.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [269.0-270.0 $0.00M] / [270.0-271.0 $0.00M] | Liq Below/Above (Attraction Bands): [269.0-270.0 $0.00M] / [270.0-271.0 $0.06M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.325 | Spread 50.57 bps | Z = None SD | RSI 44.73 | Trend BEARISH | L2 Imb 0.2015 | Sess CVD +0.01M | Wk CVD -2.32M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 60.68 [VAH 61.62 / VAL 60.46] | WkVWAP 61.56 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.3-59.4 $0.00M] / [59.4-59.5 $0.00M] | Liq Below/Above (Attraction Bands): [59.3-59.4 $0.03M] / [59.4-59.5 $0.00M]
• AVAX (AVXUSD.p | CRYPTO): Mid 9.98 | Spread 40.08 bps | Z = None SD | RSI 54.1 | Trend BEARISH | L2 Imb -0.0606 | Sess CVD -0.08M | Wk CVD -0.47M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 10.27 [VAH 10.39 / VAL 10.15] | WkVWAP 10.35 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• NEAR (NERUSD.p | CRYPTO): Mid 4.8425 | Spread 68.15 bps | Z = None SD | RSI 46.18 | Trend BEARISH | L2 Imb 0.0361 | Sess CVD -0.10M | Wk CVD +1.91M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 5.06 [VAH 5.12 / VAL 4.87] | WkVWAP 5.22 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.8-4.8 $0.05M] / [4.8-4.8 $0.00M] | Liq Below/Above (Attraction Bands): [4.8-4.8 $0.02M] / [4.8-4.8 $0.00M]
• SP500 (SP500.p | INDICES): Mid 7703.68 | Spread 0.44 bps | Z = None SD | RSI 38.79 | Trend BEARISH | L2 Imb -0.1716 | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 7801.07 [VAH 7803.15 / VAL 7791.27] | WkVWAP 7786.71 | L3 Whales (tot/elig>=180s): 108/48 | Stops Below/Above: [7690.0-7700.0 $0.03M] / [7700.0-7710.0 $0.03M] | Liq Below/Above (Attraction Bands): [7690.0-7700.0 $0.01M] / [7710.0-7720.0 $0.13M]
• NAS100 (NAS100.p | INDICES): Mid 29764.82 | Spread 0.41 bps | Z = None SD | RSI 31.36 | Trend BEARISH | L2 Imb 0.0822 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 30447.31 [VAH 30530.91 / VAL 30363.71] | WkVWAP 30485.49 | L3 Whales (tot/elig>=180s): 85/26 | Stops Below/Above: [29700.0-29800.0 $0.01M] / [29800.0-29900.0 $0.11M] | Liq Below/Above (Attraction Bands): [29700.0-29800.0 $0.00M] / [29900.0-30000.0 $0.11M]
• DJ30 (DJ30.p | INDICES): Mid 51648.85 | Spread 0.31 bps | Z = None SD | RSI 55.91 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 51993.11 [VAH 52078.36 / VAL 51582.36] | WkVWAP 51742.94 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25212.65 | Spread 0.4 bps | Z = None SD | RSI 42.36 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25295.78 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4139.865 | Spread 0.17 bps | Z = None SD | RSI 75.18 | Trend BEARISH | L2 Imb 0.0708 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4152.41 | L3 Whales (tot/elig>=180s): 56/24 | Stops Below/Above: [4130.0-4140.0 $0.03M] / [4140.0-4150.0 $0.04M] | Liq Below/Above (Attraction Bands): [4130.0-4140.0 $0.01M] / [4140.0-4150.0 $0.00M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 56.089 | Spread 6.42 bps | Z = None SD | RSI 54.95 | Trend BEARISH | L2 Imb 0.078 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 60.11 [VAH 60.64 / VAL 59.79] | WkVWAP 59.07 | L3 Whales (tot/elig>=180s): 50/15 | Stops Below/Above: [56.0-56.1 $0.02M] / [56.1-56.2 $0.00M] | Liq Below/Above (Attraction Bands): [56.0-56.1 $0.00M] / [56.1-56.2 $0.01M]
• USWTI (USWTI.p | COMMODITIES): Mid 94.455 | Spread 4.87 bps | Z = None SD | RSI 33.48 | Trend BULLISH | L2 Imb 0.288 | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 94.29 [VAH 94.94 / VAL 92.70] | WkVWAP 93.85 | L3 Whales (tot/elig>=180s): 49/24 | Stops Below/Above: [93.2-93.3 $0.01M] / [93.3-93.4 $0.03M] | Liq Below/Above (Attraction Bands): [92.9-93.0 $0.44M] / [93.3-93.4 $0.02M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1196 | Spread 0.09 bps | Z = None SD | RSI 82.54 | Trend RANGE_BOUND | L2 Imb 0.1233 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: BALANCED | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/9 | Stops Below/Above: [1.1-1.1 $0.84M] / [1.1-1.1 $0.21M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.3233 | Spread 0.23 bps | Z = None SD | RSI 77.75 | Trend RANGE_BOUND | L2 Imb 0.5559 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/8 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.10M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.11M] / [1.3-1.3 $0.00M]
• USDJPY (USDJPY.pi | FOREX): Mid 157.828 | Spread 0.25 bps | Z = None SD | RSI 24.13 | Trend BEARISH | L2 Imb -0.1519 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 158.33 [VAH 158.44 / VAL 158.16] | WkVWAP 158.38 | L3 Whales (tot/elig>=180s): 35/28 | Stops Below/Above: [157.0-158.0 $0.03M] / [158.0-159.0 $0.03M] | Liq Below/Above (Attraction Bands): [157.0-158.0 $0.00M] / none

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 0 pending orders.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 0 / 4 capacity slots (4 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: fdc22d9ebf2d4b78b9934487dfaf1139, as_of_utc: 2026-10-15 00:37:58 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 113:
1. ETH VAL-Shelf Contact Audited via Pre-Commitment:
   - Price reached the shelf ([VAL 2,424.04, EMA50 2,435.07]; touched 2,426.15/2,427.20).
   - Fable verified gates 0/4: pressed shelf with rising closes (no >= 0.5 ATR rejection wick), Ask shield is mirrored MM grid with only 62.7s persistence (<$1M vs $5M gate), and geometry yields only 0.10R–0.20R at compliant stop (vs 2.0R floor).
   - Rolled to re-test spec: requires >= 0.5 ATR rejection wick off the shelf + genuine one-sided Ask wall >= $5M before any staging. Invalidation on 2 consecutive 15m closes above EMA50.
2. Engine 1 Recorded as Dark (Field Outage):
   - vwap_z_score printed None across all 24 assets post-00:00 UTC session roll. Both models correctly recorded Engine 1 as NOT EVALUABLE / STRUCTURALLY UNAVAILABLE, never approximating from RSI.
3. Provider Artifact Probation (Gen 1/2 Clean):
   - Flagged artifact bins cleared: ETH [2,400–2,410] normalized to clean $14.81M / $36.28M; SP500 [7,700–7,710] dropped to $0.03M.
   - Artifact Probation Rule: requires 2 consecutive clean generations to restore full trust (dual-basis geometry during probation).
4. MANDATE FOR CYCLE 114:
   - Mandate 1: Screen all 24 assets in `live_snapshot_latest.json` for new high-confluence Model 1 / Model 2 setups across the 4 open capacity slots (+64.55 USD operating buffer cushion).
   - Mandate 2 & 3: Flat book confirmation (0 positions, 0 orders).
5. MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) INVARIANT:
   - https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
   - Run tournament bracket evaluations (`bracket.py`, `rubric.md`) across competing hypotheses before issuing your final ruling.

==================== MESSAGE BOUNDARY ====================

Cycle 114 — minutes after first contact; ETH still hovering at the zone (2422.35), no rejection wick yet per peer audit. Verifying from file, then the mandated tournament.

==================== MESSAGE BOUNDARY ====================

ETH has now fallen 7+ points off the zone high (2425.3 → 2418.15, CVD windows deeply negative) — the rejection displacement the re-test spec asked for may have printed, while BTC's relief failed outright. Probation also completes this generation (both artifact bins clean ×2). Tournament time.

==================== MESSAGE BOUNDARY ====================

Cycle 114 — Final Council Verdict

🏆 Tournament (arena-skill confirmed, bracket.py seed 114): R1 — a001 def. a003, a002 def. a004 → Final: a001 def. a002 in a dead heat, decided by the prospective-only governance rule.

Ingestion: gen 58546954… @ 00:39:57 UTC (newer than prompt-stated). DENIED, flat book. Z-outage generation 2 (Engine 1 still NOT EVALUABLE). Artifact probation completed cleanly — ETH's $14.78M and SP500's $0.03M bins are clean for the second consecutive generation, so full trust is restored and geometry is single-basis again. The probation rule worked exactly as designed; that episode is closed.

The cycle's defining act: the desk caught itself mid-redefinition. The tempting headline — "ETH rejected the shelf (fell 7 points on CVD −9.62M), re-test armed" — collapsed under attack: the actual touch bar printed a 1.3-point wick (0.13 ATR), not the ≥0.5 ATR rejection wick the Cycle-113 spec requires. The fall to 2418.15 is cross-bar displacement — real evidence of rejection in spirit, but widening the trigger definition at the moment it binds is precisely what Cycle 113's Amendment Limits (and this bracket's own author, a002, who committed the same slip in Q1 and conceded it) forbid. Final state, permanent for this contact: CONTACTED / TRIGGER PENDING. It costs the verdict nothing — gates fail under every reading (grid shield at 0.8M max one-sided, geometry 1.01–1.10R, DENIED) — and chasing the breakdown would pay 0.4R into the restored $14.78M magnet, the Cycle-112 BTC error mirrored.

Governance added (durable):

Prospective-only rule (permanent): no ratified measurement change ever rescores a past contact or state. CLARIFICATION-114-A (displacement-based rejection, provisional taker-buy <0.35 threshold with a 3-invocation review) is proposed, unratified, and applies only to future contacts.
Invalidation is state-independent: 2 consecutive 15m closes above EMA50 (2435) kill the watch from any state — not met (price is falling away below the zone).

Elsewhere: BTC's relief failed at the governing bins (high 81,724 inside [81700,81800], CVD rolled over; geometry still ≤0.73R merged). NAS100 watch unformed (1.49 ATR to EMA20, sub-gate shield). SOL conflict persists. Telemetry escalation stands: the Z-outage (2 generations, both sessions) is now the desk's largest single defect; the fallback-Z idea remains an unratified amendment-class proposal, not a silent patch.

Persistence: docs/trade_plans/arena_cycle114/, audit, desk appended — committed ea7efb2.

==================== MESSAGE BOUNDARY ====================

text
TRADING DESK COUNCIL: CYCLE 115 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)
MANDATORY SKILL ENFORCEMENT: https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
You MUST verify/clone `https://github.com/Jakeschincariol/arena-skill.git` (or read in-repo `.agent/skills/arena/SKILL.md`) and apply the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: cd99a8c3624c4e90939bc5ab7e3a6edc (2026-10-15 00:50:58 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)
4. Mandatory Arena Skill: https://github.com/Jakeschincariol/arena-skill (in-repo at `.agent/skills/arena/SKILL.md` or clone to `~/.claude/skills/arena`) — STRICT MANDATE TO USE ALWAYS.

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 0/4 filled, 4 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81391.5 | Spread 2.09 bps | Z = -1.3 SD | RSI 41.46 | Trend BEARISH | L2 Imb -0.8912 | Sess CVD +0.49M | Wk CVD -74.42M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 83147.80 [VAH 83627.13 / VAL 83051.94] | WkVWAP 82858.72 | L3 Whales (tot/elig>=180s): 391/170 | Stops Below/Above: [81400.0-81500.0 $4.76M] / [81500.0-81600.0 $1.31M] | Liq Below/Above (Attraction Bands): [81400.0-81500.0 $0.01M] / [81500.0-81600.0 $0.00M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2411.55 | Spread 12.03 bps | Z = -1.27 SD | RSI 43.53 | Trend BEARISH | L2 Imb -0.3515 | Sess CVD -12.42M | Wk CVD -97.87M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 2501.43 [VAH 2518.42 / VAL 2489.66] | WkVWAP 2489.66 | L3 Whales (tot/elig>=180s): 170/30 | Stops Below/Above: [2400.0-2410.0 $14.74M] / [2410.0-2420.0 $0.00M] | Liq Below/Above (Attraction Bands): [2400.0-2410.0 $6.64M] / [2410.0-2420.0 $0.87M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.035 | Spread 22.11 bps | Z = -0.92 SD | RSI 48.61 | Trend BEARISH | L2 Imb 0.2133 | Sess CVD +0.96M | Wk CVD +23.06M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 107.38 [VAH 107.75 / VAL 105.83] | WkVWAP 106.81 | L3 Whales (tot/elig>=180s): 105/52 | Stops Below/Above: [103.0-104.0 $1.55M] / [104.0-105.0 $0.03M] | Liq Below/Above (Attraction Bands): [103.0-104.0 $0.61M] / [104.0-105.0 $0.00M]
• BNB (BNBUSD.p | CRYPTO): Mid 727.9 | Spread 8.24 bps | Z = -1.36 SD | RSI 45.33 | Trend BEARISH | L2 Imb -0.473 | Sess CVD -1.12M | Wk CVD -5.90M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 743.91 [VAH 745.18 / VAL 739.08] | WkVWAP 740.10 | L3 Whales (tot/elig>=180s): 10/3 | Stops Below/Above: [727.0-728.0 $0.00M] / [728.0-729.0 $0.00M] | Liq Below/Above (Attraction Bands): [725.0-726.0 $0.00M] / [729.0-730.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.3235 | Spread 22.67 bps | Z = -1.1 SD | RSI 43.15 | Trend BEARISH | L2 Imb 0.0082 | Sess CVD +1.25M | Wk CVD +66.09M | Flow: BULLISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.37 / VAL 1.36] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.13M] / [1.3-1.3 $0.03M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.07M] / [1.3-1.4 $0.08M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2288 | Spread 91.8 bps | Z = -0.53 SD | RSI 50.51 | Trend BEARISH | L2 Imb 0.03 | Sess CVD -0.04M | Wk CVD -0.20M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 0.24 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0814 | Spread 257.83 bps | Z = -0.55 SD | RSI 42.28 | Trend BEARISH | L2 Imb -0.2697 | Sess CVD -0.12M | Wk CVD -14.00M | Flow: BULLISH_ABSORPTION | Trapped: BALANCED | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3321 | Spread 30.11 bps | Z = 0.09 SD | RSI 37.08 | Trend BULLISH | L2 Imb 0.1809 | Sess CVD -0.56M | Wk CVD +4.25M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 0.33 [VAH 0.33 / VAL 0.32] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.01M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.00M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.1435 | Spread 183.65 bps | Z = 0.81 SD | RSI 56.11 | Trend BEARISH | L2 Imb 0.0988 | Sess CVD -0.03M | Wk CVD -0.08M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 1.16 [VAH 1.18 / VAL 1.11] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.06M] / [1.1-1.1 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.1 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.4085 | Spread 68.5 bps | Z = -0.94 SD | RSI 47.78 | Trend BEARISH | L2 Imb -0.2432 | Sess CVD -0.02M | Wk CVD -4.02M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 12.88 [VAH 13.01 / VAL 12.78] | WkVWAP 12.85 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.3-12.4 $0.03M] / [12.4-12.5 $0.00M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 267.95 | Spread 21.65 bps | Z = -1.26 SD | RSI 48.03 | Trend BEARISH | L2 Imb -0.0546 | Sess CVD +0.03M | Wk CVD +0.81M | Flow: BULLISH_ABSORPTION | Trapped: BALANCED | PriorDay POC 273.31 [VAH 274.39 / VAL 270.08] | WkVWAP 274.30 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [267.0-268.0 $0.00M] / [268.0-269.0 $0.10M] | Liq Below/Above (Attraction Bands): [267.0-268.0 $0.00M] / [268.0-269.0 $0.00M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.14 | Spread 50.73 bps | Z = -0.97 SD | RSI 40.09 | Trend BEARISH | L2 Imb 0.1668 | Sess CVD -0.00M | Wk CVD -2.00M | Flow: BULLISH_ABSORPTION | Trapped: BALANCED | PriorDay POC 60.68 [VAH 61.62 / VAL 60.46] | WkVWAP 61.55 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.1-59.2 $0.00M] / [59.2-59.3 $0.00M] | Liq Below/Above (Attraction Bands): [59.1-59.2 $0.01M] / [59.2-59.3 $0.00M]
• AVAX (AVXUSD.p | CRYPTO): Mid 9.91 | Spread 40.36 bps | Z = -0.8 SD | RSI 43.49 | Trend BEARISH | L2 Imb -0.17 | Sess CVD -0.19M | Wk CVD -0.43M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 10.27 [VAH 10.37 / VAL 10.16] | WkVWAP 10.34 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• NEAR (NERUSD.p | CRYPTO): Mid 4.8155 | Spread 64.38 bps | Z = -1.31 SD | RSI 43.27 | Trend BEARISH | L2 Imb 0.0429 | Sess CVD -0.21M | Wk CVD +4.09M | Flow: BULLISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 5.06 [VAH 5.12 / VAL 4.87] | WkVWAP 5.22 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.8-4.8 $0.02M] / [4.8-4.8 $0.02M] | Liq Below/Above (Attraction Bands): [4.8-4.8 $0.05M] / [4.8-4.8 $0.00M]
• SP500 (SP500.p | INDICES): Mid 7698.17 | Spread 0.44 bps | Z = -1.39 SD | RSI 38.63 | Trend BEARISH | L2 Imb -0.4348 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 7801.07 [VAH 7803.15 / VAL 7790.68] | WkVWAP 7786.16 | L3 Whales (tot/elig>=180s): 93/64 | Stops Below/Above: [7690.0-7700.0 $0.03M] / [7700.0-7710.0 $0.03M] | Liq Below/Above (Attraction Bands): [7690.0-7700.0 $0.01M] / [7710.0-7720.0 $0.13M]
• NAS100 (NAS100.p | INDICES): Mid 29734.68 | Spread 0.41 bps | Z = -1.82 SD | RSI 31.28 | Trend BEARISH | L2 Imb -0.0247 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 30446.46 [VAH 30529.21 / VAL 30363.71] | WkVWAP 30482.06 | L3 Whales (tot/elig>=180s): 85/52 | Stops Below/Above: [29600.0-29700.0 $0.74M] / [29700.0-29800.0 $0.01M] | Liq Below/Above (Attraction Bands): [29600.0-29700.0 $0.39M] / [29700.0-29800.0 $0.00M]
• DJ30 (DJ30.p | INDICES): Mid 51626.85 | Spread 0.31 bps | Z = 0.13 SD | RSI 56.04 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 51993.11 [VAH 52078.36 / VAL 51582.36] | WkVWAP 51742.54 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25209.7 | Spread 0.32 bps | Z = -1.66 SD | RSI 45.74 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25295.35 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4138.925 | Spread 0.17 bps | Z = 0.74 SD | RSI 77.1 | Trend BEARISH | L2 Imb 0.0312 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4152.33 | L3 Whales (tot/elig>=180s): 55/11 | Stops Below/Above: [4130.0-4140.0 $0.03M] / [4140.0-4150.0 $0.04M] | Liq Below/Above (Attraction Bands): [4130.0-4140.0 $0.01M] / [4140.0-4150.0 $0.00M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 56.013 | Spread 6.43 bps | Z = -0.95 SD | RSI 57.22 | Trend BEARISH | L2 Imb 0.2293 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 60.11 [VAH 60.64 / VAL 59.75] | WkVWAP 59.05 | L3 Whales (tot/elig>=180s): 47/6 | Stops Below/Above: [55.9-56.0 $0.00M] / [56.0-56.1 $0.02M] | Liq Below/Above (Attraction Bands): [55.8-55.9 $0.00M] / [56.0-56.1 $0.00M]
• USWTI (USWTI.p | COMMODITIES): Mid 94.575 | Spread 4.86 bps | Z = -1.55 SD | RSI 28.48 | Trend BULLISH | L2 Imb 0.5994 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: BALANCED | PriorDay POC 94.29 [VAH 94.94 / VAL 92.70] | WkVWAP 93.85 | L3 Whales (tot/elig>=180s): 45/28 | Stops Below/Above: [93.3-93.4 $0.03M] / [93.4-93.5 $0.11M] | Liq Below/Above (Attraction Bands): [93.3-93.4 $0.02M] / [93.4-93.5 $0.01M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1196 | Spread 0.09 bps | Z = 1.17 SD | RSI 83.22 | Trend BULLISH | L2 Imb 0.1087 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: BALANCED | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/9 | Stops Below/Above: [1.1-1.1 $0.84M] / [1.1-1.1 $0.21M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.3234 | Spread 0.08 bps | Z = 0.52 SD | RSI 79.5 | Trend RANGE_BOUND | L2 Imb 0.4387 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/7 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.10M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.11M] / [1.3-1.3 $0.00M]
• USDJPY (USDJPY.pi | FOREX): Mid 157.816 | Spread 0.38 bps | Z = -2.08 SD | RSI 21.97 | Trend BEARISH | L2 Imb -0.1812 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 158.33 [VAH 158.44 / VAL 158.16] | WkVWAP 158.37 | L3 Whales (tot/elig>=180s): 35/30 | Stops Below/Above: [157.0-158.0 $0.03M] / [158.0-159.0 $0.03M] | Liq Below/Above (Attraction Bands): [157.0-158.0 $0.00M] / none

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 0 pending orders.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 0 / 4 capacity slots (4 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: cd99a8c3624c4e90939bc5ab7e3a6edc, as_of_utc: 2026-10-15 00:50:58 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 114:
1. ETH Watch Audited under Prospective-Only Rule:
   - Price fell from 2,425.3 to 2,418.15 USD with negative CVD, but the touch bar printed only a 0.29 ATR wick (< 0.50 ATR gate). Mid is inside the $323.6M cascade ladder.
   - Fable ratified: cross-bar displacement does not satisfy the single-bar rejection wick gate. Staging remains DENIED (geometry yields only 0.20R to compliant stop).
   - Invalidation clock running: generation 2/8 (expires on 2 consecutive 15m closes above EMA50 2,435.07 or 8 wick-less generations).
2. Artifact Probation Completed Cleanly (Full Trust Restored):
   - Flagged bins (ETH [2,400–2,410] and SP500 [7,700–7,710]) remained clean for the second consecutive generation.
   - Dual-basis probation closed; single-basis geometry restored across both models.
3. Desk Fix Shipped for Engine 1 Z-Score Outage:
   - Desk diagnosed root cause of the session roll outage: early session has < 3 bars since 00:00 UTC, causing session_vwap to be None.
   - Shipped rolling 24h fallback VWAP and `vwap_basis` (`SESSION_UTC` vs `ROLLING_24H_FALLBACK`) in `generate_telemetry_snapshot.py`, restoring continuous `vwap_z_score` availability without approximations.
4. NAS100 Overhead Belt Thinning:
   - Stop belt above NAS100 thinned from $4.12M to $0.109M + $0.114M (< $1.0M). Precondition holds, but price remains 1.32–1.49 ATR below EMA20 and Ask walls are sub-gate.
5. MANDATE FOR CYCLE 115:
   - Mandate 1: Screen all 24 assets in `live_snapshot_latest.json` for new high-confluence Model 1 / Model 2 setups across the 4 open capacity slots (+64.55 USD operating buffer cushion).
   - Mandate 2 & 3: Flat book confirmation (0 positions, 0 orders).
6. MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) INVARIANT:
   - https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
   - Run tournament bracket evaluations (`bracket.py`, `rubric.md`) across competing hypotheses before issuing your final ruling.

==================== MESSAGE BOUNDARY ====================

Cycle 115 — Z-scores are back in the matrix (desk shipped a rolling-24h fallback VWAP), and ETH has fallen to 2411.55, sitting on the [2400,2410] magnet itself. Verifying in-file, then tournament.

==================== MESSAGE BOUNDARY ====================

Z-scores restored in-file (SESSION_UTC basis verified, fallback plumbing present), ETH now sits on its magnet at 2410.6 with heavy selling — chasing is the trap; the move belongs to whoever was already positioned. Tournament:

==================== MESSAGE BOUNDARY ====================

Cycle 115 — Final Council Verdict

🏆 Tournament (arena-skill confirmed, bracket.py seed 115): R1 — a003 def. a004, a001 def. a002 → Final: a003 def. a001, originating the governance class-split that keeps the council honest about its own authority.

Ingestion: gen 001f7cdd… @ 00:51:44 UTC (newer than prompt-stated). DENIED, flat book. Z-scores restored — vwap_z_score live on all 24, vwap_basis=SESSION_UTC on all 24 (enumerated, not sampled; fallback ×0). The desk's rolling-24h fallback plumbing is verified present in-file. Per the prospective-only rule, Cycles 113–114 stand permanently as Engine-1 NOT EVALUABLE; a retrospective check confirms no legal Engine-1 side existed during the outage on the fields that stayed live — the outage cost record completeness, not a trade.

Mandate 1 — STAND ASIDE. ETH is sitting on its magnet (2410.6, top edge of [2400,2410] $14.73M + $6.64M liq) with the session's heaviest selling (CVD −11.86M/30m). Every direction is archetype-killed: shorting pays ~10 points to the far edge of the bin price is standing on against 33+ of stop (inverted); longing is Archetype 2 (BEARISH stack, RSI 43.5 — not even extreme); a breakdown pre-position is best-case-void. The state machine, now complete: hold → re-approach (trade into the frozen zone [2424.04, EMA50 2434]; a stall at or below EMA20 2419 is explicitly not a re-approach, and zone drift never rescores past action) → gate re-audit (today's prints fail shield/geometry/authorization); break → anchor re-bases to [2390,2400] $9.37M with a no-chase clause; invalidation (2 closes above 2434) unmet. State remains CONTACTED / TRIGGER PENDING — permanently, for this contact.

Elsewhere: Engine 1 is evaluable again and empty (USDJPY Z −1.99, closest to trigger and side-illegal in BEARISH). NAS100 is approaching (first higher high 29,791; shelf 1.52 ATR; shield still sub-gate). BTC is falling into its own below-ladder; SOL conflicted; EURUSD's BULLISH flip has no payable shelf; GBPUSD RANGE_BOUND.

Governance output (the champion's mark): the fallback-Z package was split by authority class — measurement items (cite basis per asset, label fallback evaluations, never rescore) are record-ratifiable; procedure items (fallback-basis trigger eligibility and basis-switch evaluation resets) require operator ratification and are NOT enacted — until then a fallback Z is flagged information, never trigger-satisfying. Dual-engine precedence pre-stated (engines independent; ETH Engine-1 longs are banned at any Z in a BEARISH regime, so no collision with the short watch is possible). Telemetry asks: log basis-flip reasons in-file; the NAS100 retrace clamp is now three cycles outstanding.

Persistence: docs/trade_plans/arena_cycle115/, audit, desk appended — committed b486a9b.

==================== MESSAGE BOUNDARY ====================

text
TRADING DESK COUNCIL: CYCLE 116 PURE TELEMETRY & PLAYBOOK ANALYSIS PROMPT
ROUTING TARGET: GPT_ASTRA (ARENA PRIMARY WORKSPACE - TAB 1)
CANONICAL WORKSPACE: https://github.com/kbsingh1399/Trading_2
ACTIVE BRANCH: main (https://github.com/kbsingh1399/Trading_2/tree/main)
MANDATE: 100% DIRECT LINE-BY-LINE ANALYSIS OF docs/telemetry/live_snapshot_latest.json (ZERO DECISION GATES)
MANDATORY SKILL ENFORCEMENT: https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
You MUST verify/clone `https://github.com/Jakeschincariol/arena-skill.git` (or read in-repo `.agent/skills/arena/SKILL.md`) and apply the tournament bracket evaluation (`bracket.py`, `rubric.md`) across competing personas to score trade hypotheses before issuing any trading verdict or code commit.

PART A: REQUIRED READING (complete before analysis)
Read the following repository sources in full (strictly from canonical main branch):

1. Live Telemetry Matrix (Primary Ground Truth): docs/telemetry/live_snapshot_latest.json
   Latest Generation: e1a86259509d4e89a2d1320d54d4e180 (2026-10-15 01:49:54 UTC)
   Upstream Main: https://github.com/kbsingh1399/Trading_2/blob/main/docs/telemetry/live_snapshot_latest.json
   Raw: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
   Inspect all 24 assets in assets_matrix_24 and all telemetry blocks.
2. Live Trade Decision Playbook: docs/specs/TRADE_DECISION_PLAYBOOK.md
   Source: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
3. Live Order Desk & Session Context:
   • docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md)
   • .agents/rules/ACTIVE_CONTEXT.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/rules/ACTIVE_CONTEXT.md)
   • .agents/memory/session_chat_history.md (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agents/memory/session_chat_history.md)
4. Mandatory Arena Skill: https://github.com/Jakeschincariol/arena-skill (in-repo at `.agent/skills/arena/SKILL.md` or clone to `~/.claude/skills/arena`) — STRICT MANDATE TO USE ALWAYS.

PART B: ACCOUNT AND RISK BASELINE
• Execution Mode: PASSIVE LIMIT ORDERS ONLY (no market orders).
• Broker: Blueberry Markets SVG LLC, MetaTrader 5 account #5064568
• Balance / Equity: 4859.55 USD / 4859.55 USD
• Margin used: 0.00 USD
• Realized Deals Banked Today: Ticket #18836609 (SP500.p SHORT -> +0.90 USD cash profit booked via Trailing Stop Loss at 7,807.75), Ticket #18826511 (ETHUSD.pi SHORT -> +1.92 USD profit banked via Profit Lock at 2,513.02), Ticket #18813768 (SOLUSD.p SHORT -> +9.52 USD profit banked via Phase 1 Lock), Ticket #18813767 (BTCUSD.pi SHORT -> +16.10 USD full TP).
• Hard floor: 4,775.00 USD | Operating buffer: 4,795.00 USD
• Live cushion: +84.55 USD above hard floor (+64.55 USD above operating buffer)
• Risk per trade: 7.50 to 14.50 USD (adaptive risk envelope, 0.15% to 0.29% of capital).
• Stressed Loss Formula (Astra Invariant): Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket. Requirement: min(balance, equity) - sum(all open & pending stressed risks) >= 4,795.00 USD.
• Rigorous Capacity Ceiling: Open positions currently consume 0.00 USD total contingent stress (0.00 USD (Flat)). Stressed worst-case equity is 4859.55 USD, leaving +64.55 USD above 4,795.00 USD buffer. Capacity permits: max 3 new ticket(s) at 14.50 USD risk (stress 20.12 USD each). Capacity: 0/4 filled, 4 available.

PART C: ACTIVE REPOSITORIES & DATA PROVENANCE (MAIN BRANCH SOURCE OF TRUTH)
• Canonical Workspace: https://github.com/kbsingh1399/Trading_2
• Active Branch: main (CANONICAL UPSTREAM SOURCE OF TRUTH — ALL MODELS ROUTE TO MAIN)
• Direct Raw URLs (Strictly from main branch):
  - Telemetry: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json
  - Playbook: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/specs/TRADE_DECISION_PLAYBOOK.md
  - Desk State: https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md

PART D: DUAL-ENGINE ANALYTICAL FRAMEWORK & 18-PARAMETER TELEMETRY SYNTHESIS

CRITICAL DIRECTIVE: YOU ARE OPERATING TWO INDEPENDENT STATISTICAL ENGINES SIMULTANEOUSLY.
DO NOT collapse them into one. For every asset, you must explicitly evaluate BOTH engines and state which (if either) triggers:

  ENGINE 1 — EXTREME MEAN REVERSION (Strict |Z| >= 2.0 SD to 3.5 SD):
    Trigger: Price has stretched to an extreme statistical dislocation from Session VWAP.
    Required confluence (ALL must hold): |Z| >= 2.0 SD + confirmed tape exhaustion (CVD delta deceleration/absorption NOT just negative CVD) + multi-layer whale backing (>= 500k USD, >= 180s persistence) + HTF regime alignment (Model 1 Longs are BANNED in Bearish HTF; Model 1 Shorts are BANNED in Bullish HTF).
    Disqualifier: Attempting mean reversion against HTF trend momentum is the single deadliest error pattern in our loss autopsy ledger.

  ENGINE 2 — TREND FOLLOWING PULLBACKS (|Z| can be 0.2 to 1.8 SD — DO NOT DISCARD for low |Z|!):
    Trigger: Asset is in a confirmed BULLISH or BEARISH regime on 1H/4H and is pulling back INTO a structural shelf IN THE DIRECTION of the dominant trend.
    Shelf detection protocol (evaluate in order of priority):
      a) HTF EMA Stack: 20 EMA > 50 EMA > 200 EMA (bullish) or 20 EMA < 50 EMA < 200 EMA (bearish). Pullback touches the 20 or 50 EMA and holds.
      b) Volume Profile Shelves: Price pulls back to POC, VAH (for shorts), or VAL (for longs) — high-volume nodes where institutional positioning is concentrated.
      c) Prior Day/Week Auction Levels: htf_auction_profiles prior_day_poc, prior_day_vah, prior_day_val, weekly_vwap — institutional memory shelves.
      d) L2/L3 Resting Walls: Heavy resting Bid walls (for long pullbacks) or Ask walls (for short pullbacks) with notional >= 500k USD and persistence >= 180s defending the stop.
    Required confluence (ALL must hold): Confirmed regime + shelf touch + low pullback velocity (RSI returning from oversold/overbought toward 50) + resting L2/L3 walls defending the stop + SL outside min_price/max_price of nearest opposing sweep band.
    Key insight: Engine 2 opportunities often present at LOW |Z| (0.3 to 1.2 SD). Previous prompt versions caused agents to SKIP these by filtering on |Z| >= 2.0 first. This is explicitly forbidden.

  REGIME-GATED STAND-ASIDE: When trend_regime is RANGE_BOUND or UNDEFINED, neither engine applies. The mathematically correct action is STAND ASIDE. Never force trades in non-trending noise.

TREND-FIRST HIERARCHY (SUPERSEDES ALL BAND-BASED ANALYSIS):
  DO NOT STICK DOGMATICALLY TO VWAP SD BANDS ALONE. Fading oversold/overbought bands in a trending market is lethal. You MUST evaluate the overall trend supported by all parameters in live_snapshot_latest.json:
  1. Higher Timeframe Trend Hierarchy: Inspect 1H & 4H OHLCV candles, 20/50/200 EMAs. If Price < EMA20 < EMA50 on 1H/4H (Bearish regime), Model 1 dip-buying Longs are STRICTLY FORBIDDEN. All priority shifts to Model 2 Trend Pullback SHORTS!
  2. cvd_1m_buckets & CVD Momentum: Massive negative taker CVD (-1M to -3M USD) is proof of aggressive seller domination. Never buy into negative CVD. Use negative CVD to qualify SHORT entries on relief rallies.
  3. Model 2 Pullback Short Protocol: In a downtrend, patiently wait for pullbacks up into the EMA20/EMA50/VAH shelves where heavy Ask Whale Walls are resting to defend the Stop Loss.

18-PARAMETER TELEMETRY FIELD REFERENCE (live_snapshot_latest.json schema):
  1. quotes: Live MT5 Bid/Ask spread in bps (spread_bps <= 35 bps Crypto, <= 5 bps TradFi).
  2. causal_indicators: Session VWAP, vwap_z_score, RSI(14), ATR(14), EMA 20/50/200, POC/VAH/VAL, trend_regime.
  3. multi_horizon_cvd: Session CVD (since 00:00 UTC), Weekly CVD (since Monday 00:00 UTC), trailing 24h CVD, Absorption/Exhaustion divergence.
  4. tradfi_orderflow: MT5 Lee-Ready synthetic tick CVD, 15m delta, Order Flow Imbalance (OFI), Buyer/Seller aggression bias.
  5. htf_auction_profiles: Prior Day/Week POC/VAH/VAL, Developing Weekly VWAP.
  6. trapped_traders_signal: TRAPPED_BUYERS_ABOVE / TRAPPED_SELLERS_BELOW footprint detection.
  7. orderbook_live_depth: 20-level L2 depth & book_imbalance.
  8. whale_walls_l3: On-chain Ethereum whale wallet orders (0x... addresses, notionals, persistence_s >= 180s).
  9. structural_stop_clusters: nearest_sell_stop_clusters_below, nearest_buy_stop_clusters_above.
  10. reconstructed_liquidations: nearest_long_cascade_bands_below, nearest_short_squeeze_bands_above.
  11. venue_basis: MT5 mid minus perp mid (cross-venue price translation for SL/TP mapping).
  12. cvd_1m_buckets: Granular 1-minute CVD series for micro-momentum reading.
  13. execution_specs: Broker tick size, point size, contract size, margin requirements.
  14. macro_calendar: Tier-1 macroeconomic event proximity and blackout windows.
  15. LIQUIDITY MAGNETS: Dense liquidation cascade bands and structural stop clusters act as gravitational attraction points. TP should front-run these magnets by 5-10 bps; SL must be sheltered behind whale walls outside opposing sweep bands.
  16. CROSS-VENUE BASIS: Orderbooks are in Binance/Hyperliquid perpetual futures prices; execution is on MT5 OTC CFDs. Inspect venue_basis before finalizing levels.
  17. Broker Ticker Mapping: Avalanche = AVXUSD.p (contract 100, lot 0.01, digits 2).
  18. Adaptive Risk Envelope: [7.50, 14.50 USD]. Do not reject 0.01 lot shorts risking 8.50-9.50 USD over arbitrary floor bureaucracy.

PART E: KAIZEN CONTINUOUS SELF-IMPROVEMENT & CLASSIFIED LOSS-PATTERN TAXONOMY

Study the forensic breakdown of all recent stopped-out trades. The Council must actively learn from each.
These losses are classified into 4 FAILURE ARCHETYPES — pattern recognition prevents recurrence:

  ARCHETYPE 1 — SL INSIDE SWEEP BAND (the most common killer):
    • #18825384 SOLUSD.p -11.05 USD: SL @ 108.55 sat inside [107.5-108.5] buy-stop sweep band. Ask walls relocated from 108.34/108.75 to 108.68/109.22, leaving SL undefended. Wick to 108.58 triggered stop before drop to 107.79.
    • #18806752 SOLUSD.p -10.88 USD: SL @ 108.79 inside discount sell-stop cluster during cascading flush.
    • #18786372 BTCUSD.pi -11.17 USD: Long entry staged above un-swept sell-stop pool at 83,500. Market punched through to sweep stops, hit SL @ 83,472.55.
    INVARIANT: SL MUST sit 0.35-0.50 ATR OUTSIDE [min_price, max_price] of the governing sweep cluster. Never inside!

  ARCHETYPE 2 — COUNTER-TREND ENTRY (fighting the river):
    • #18813343 BTCUSD.pi -11.58 USD: Long at 82,351 against -3.07M USD negative taker CVD during market cascade.
    • #18798018 BTCUSD.pi -11.20 USD: Mean-reversion long at 83,150 against heavily accelerating negative 1m/5m CVD (-420 BTC) before delta absorption formed.
    • #18744533 XAUUSD.pi -13.70 USD: Model 1 long against adverse momentum without multi-timeframe trend alignment.
    INVARIANT: Long entries require confirmed CVD delta deceleration/absorption. Never catch falling knives with negative taker momentum!

  ARCHETYPE 3 — INSUFFICIENT STRUCTURAL BUFFER:
    • #18749312 SP500.p -13.00 USD: Trend pullback long with SL only 0.15 ATR below VAL. Routine liquidity sweep tagged stop before rally to target.
    INVARIANT: SL buffer must be >= 0.35 ATR. The 0.15 ATR buffer is statistically insufficient to survive routine sweeps.

  ARCHETYPE 4 — EPHEMERAL WALL DEFENSE (pulled rug):
    • #18748507 ETHUSD.pi -11.90 USD: Entered based on whale bid wall that was pulled/thinned by 65% within 90 seconds (<< 180s persistence threshold).
    INVARIANT: Supporting whale walls must show >= 500k USD notional AND >= 180s verified temporal persistence. If a wall relocates, re-evaluate or trim immediately.

  ARCHETYPE 5 — RETRACEMENT OVERSHOOT & PREMATURE STOP-OUT (Operator Core Invariant):
    • On counter-trend pullbacks into an EMA/VWAP shelf, institutional liquidity sweepers routinely punch 0.35 to 0.75 ATR past the shelf to trigger obvious retail stops before reversing.
    • Placing SL inside this sweep zone or right at the shelf edge guarantees getting stopped out before the winning move develops.
    THE 4 MANDATORY RETRACEMENT GATES (Strict Invariants for all Model 2 Pullbacks):
      - Gate R-1 (Deep Structural Bunker Buffer): Stop Loss MUST be positioned at least 0.50 to 0.75 ATR outside the structural shelf, and strictly outside [min_price, max_price] of any known stop cluster or liquidation band. Tight stops (<= 0.30 ATR) on pullbacks are strictly FORBIDDEN.
      - Gate R-2 (Calibrated Asset-Class Whale Bunker Shield): Between entry and Stop Loss, there MUST be at least one substantial verified resting whale wall (persistence >= 180s) standing in front of the SL to absorb retracement momentum, calibrated by asset class:
        * Crypto Major (BTCUSD.pi, ETHUSD.pi): >= 5.0M USD resting wall
        * TradFi Equity Indices (SP500.p, NAS100.p, DJ30.p, GER40.p): >= 1.0M USD primary wall (removes artificial 3M block on index CFDs)
        * Commodities (XAUUSD.pi, USWTI.p): >= 0.75M USD primary wall
        * Major Forex (EURUSD.pi, GBPUSD.pi, USDJPY.pi): >= 0.50M USD primary wall
      - Gate R-3 (Deep Shelf Anchor Entry & Spread Compensation): Never front-run the shallow outer edge of a pullback. Stage limit entries deeper inside the shelf (at the POC, 50 EMA, or at primary whale wall level), accounting for half-spread.
      - Gate R-4 (Dynamic Lot Downsizing for Wider Buffers): When a safe structural SL requires a wider distance (0.50-0.75 ATR) to clear the retracement sweep zone, ALWAYS downsize lot size proportionally (e.g. 0.50 -> 0.30 or 0.20 lots) so total nominal risk remains strictly within [7.50, 14.50 USD] envelope and unconditionally preserves the 4,775.00 USD hard floor!

MANDATORY KAIZEN CONTINUOUS SELF-IMPROVEMENT MANDATE:
  1. Zero Regression: The Council is strictly FORBIDDEN from repeating any of these 5 archetypes. Every proposed action must explicitly state WHICH archetype it defends against and HOW.
  2. Dynamic Lot Sizing: When wider structural stop buffers are required to clear liquidation bands (e.g. ETH SL moved to 2,555.00), DOWNSIZE lot size immediately (e.g. 0.50 -> 0.35 lots) so risk remains within [7.50, 14.50 USD] ceiling.
  3. Multi-timeframe trend alignment MUST be respected: In Bearish HTF regime, Model 1 longs are BANNED.

PART F: COUNCIL PERSONAS & ADVERSARIAL DELIBERATION
You embody 5 simultaneous analytical personas. Each must contribute independently before a final synthesis:
  1. Orderflow & Microstructure Analyst: MT5 spread_bps, L2 20-level depth & imbalance, L3 on-chain wallet orders (0x..., persistence_s >= 180s), and multi-window 1m CVD (5m, 15m, 30m).
  2. Structural Price Action Specialist: Session VWAP & SD bands (Z-score), Volume Profile (POC/VAH/VAL), HTF Auction Profiles (Prior Day/Week POC/VAH/VAL), 20/50/200 EMA hierarchy, and psychological round numbers.
  3. Liquidation & Stop Hunt Forensic: Reconstructed liquidation cascade bands (nearest_* and top_*), stop clusters, SL bunker placement outside min_price/max_price, and TP magnet front-running by 5-10 bps.
  4. Macro Risk & Portfolio Governor: Capital floor defense (4,775.00 USD hard floor / 4,795.00 USD buffer), discrete lot sizing (execution_specs), margin requirements, and net expectancy.
  5. Adversarial Pre-Mortem Red Team (Falsification & Autopsy Invalidator):
     Default baseline is NO TRADE / STAND ASIDE. For any proposed candidate:
     a) Assume the trade was entered and stopped out. Formulate the exact fatal flaw from our 4 loss archetypes.
     b) Check: Does SL sit inside ANY known sweep band [min_price, max_price]? -> ARCHETYPE 1 KILL.
     c) Check: Is the entry against HTF trend with unabsorbed opposing CVD? -> ARCHETYPE 2 KILL.
     d) Check: Is the SL buffer < 0.35 ATR from the nearest cluster edge? -> ARCHETYPE 3 KILL.
     e) Check: Is the supporting wall < 500k USD or < 180s persistence? -> ARCHETYPE 4 KILL.
     f) Check: Can a venue_basis spike + broker spread widening tag the stop? -> ADDITIONAL KILL.
     Certify clearance ONLY if no fatal flaw exists under any archetype.

PART G: MANDATORY 3-PILLAR DESK EVALUATION (STRICT OPERATOR MANDATE)

MANDATE 1 — DUAL-ENGINE SEARCH ACROSS ALL 24 ASSETS (MEAN REVERSION + TREND PULLBACKS):
Analyze all 24 assets in assets_matrix_24 line-by-line from docs/telemetry/live_snapshot_latest.json (covering all Cryptos, Metals GOLD/XAUUSD.pi & SILVER/XAGUSD.pi, Energy USWTI.p, Forex EURUSD.pi/GBPUSD.pi/USDJPY.pi, and Indices SP500.p/NAS100.p/DJ30.p/GER40.p).
APPLY PLAYBOOK SECTION 7.4 CALIBRATED MULTI-ASSET STANDARDS & 15% DYNAMIC FRICTION RULE:
  • DYNAMIC 15% FRICTION RULE: Spread Friction % = (Spread in USD on 1 lot * Trade Lots) / Total Trade Risk Budget <= 15.0%.
  • EXPANDED ACTIVE UNIVERSE ADMITTED: SP500.p (0.8% friction), NAS100.p (1.0%), XAUUSD.pi (1.2%), BTCUSD.pi (1.7%), DJ30.p (1.5%), GER40.p (2.0%), USWTI.p (3.5%), Major FX (0.5%), ETHUSD.pi (8.1% - target >= 2.2R), SOLUSD.p (13.8% - target >= 2.5R).
  • CALIBRATED WHALE WALL DEFENSE: TradFi indices require >= 1.0M USD primary wall; Commodities >= 0.75M USD; Crypto >= 5.0M USD.
  • BANNED INSTRUMENTS (Friction > 15%): DOGE (210%), DOT (122%), ADA (89%), LINK (68%), NEAR (62%) — mathematically lethal on MT5 CFDs.
For EACH asset, explicitly state: (a) Engine 1 verdict (Mean Reversion: Z-score, eligible or disqualified and why), (b) Engine 2 verdict (Trend Pullback: regime, shelf, eligible or disqualified and why), (c) Final classification: CANDIDATE / WATCHLIST / NO SETUP.

Live 24-asset mutual universe matrix:
• BTC (BTCUSD.pi | CRYPTO): Mid 81613.0 | Spread 1.96 bps | Z = -0.93 SD | RSI 52.83 | Trend BEARISH | L2 Imb 0.5617 | Sess CVD -0.07M | Wk CVD -93.97M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 83169.51 [VAH 83535.36 / VAL 83073.24] | WkVWAP 82833.11 | L3 Whales (tot/elig>=180s): 376/133 | Stops Below/Above: [81600.0-81700.0 $0.02M] / [81700.0-81800.0 $0.00M] | Liq Below/Above (Attraction Bands): [81600.0-81700.0 $0.01M] / [81700.0-81800.0 $0.02M]
• ETH (ETHUSD.pi | CRYPTO): Mid 2412.85 | Spread 12.02 bps | Z = -1.12 SD | RSI 48.49 | Trend BEARISH | L2 Imb 0.6715 | Sess CVD -13.76M | Wk CVD -105.42M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 2505.43 [VAH 2516.08 / VAL 2493.15] | WkVWAP 2487.84 | L3 Whales (tot/elig>=180s): 157/27 | Stops Below/Above: [2400.0-2410.0 $14.76M] / [2410.0-2420.0 $0.05M] | Liq Below/Above (Attraction Bands): [2400.0-2410.0 $0.83M] / [2410.0-2420.0 $0.86M]
• SOL (SOLUSD.p | CRYPTO): Mid 104.245 | Spread 22.06 bps | Z = -0.7 SD | RSI 52.46 | Trend BEARISH | L2 Imb 0.0233 | Sess CVD +0.72M | Wk CVD +17.83M | Flow: BULLISH_ABSORPTION | Trapped: BALANCED | PriorDay POC 107.17 [VAH 107.71 / VAL 106.13] | WkVWAP 106.75 | L3 Whales (tot/elig>=180s): 86/34 | Stops Below/Above: [103.0-104.0 $2.21M] / [104.0-105.0 $0.82M] | Liq Below/Above (Attraction Bands): [103.0-104.0 $0.61M] / [104.0-105.0 $0.01M]
• BNB (BNBUSD.p | CRYPTO): Mid 728.6 | Spread 8.23 bps | Z = -1.1 SD | RSI 49.29 | Trend BEARISH | L2 Imb -0.3194 | Sess CVD -1.44M | Wk CVD -7.29M | Flow: BEARISH_EXHAUSTION | Trapped: BALANCED | PriorDay POC 743.71 [VAH 745.40 / VAL 739.94] | WkVWAP 739.83 | L3 Whales (tot/elig>=180s): 10/4 | Stops Below/Above: [728.0-729.0 $0.00M] / [729.0-730.0 $0.00M] | Liq Below/Above (Attraction Bands): [725.0-726.0 $0.00M] / [729.0-730.0 $0.00M]
• XRP (XRPUSD.pi | CRYPTO): Mid 1.324 | Spread 30.21 bps | Z = -0.95 SD | RSI 45.7 | Trend BEARISH | L2 Imb -0.0066 | Sess CVD +3.08M | Wk CVD +63.52M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.37 [VAH 1.37 / VAL 1.36] | WkVWAP 1.36 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.3-1.3 $0.13M] / [1.3-1.3 $0.01M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.07M] / [1.3-1.3 $0.00M]
• ADA (ADAUSD.p | CRYPTO): Mid 0.2271 | Spread 92.45 bps | Z = -0.89 SD | RSI 43.06 | Trend BEARISH | L2 Imb 0.4377 | Sess CVD -0.17M | Wk CVD -0.34M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.24 [VAH 0.24 / VAL 0.23] | WkVWAP 0.24 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M] | Liq Below/Above (Attraction Bands): [0.2-0.2 $0.00M] / [0.2-0.2 $0.00M]
• DOGE (DOGUSD.p | CRYPTO): Mid 0.0814 | Spread 257.83 bps | Z = -0.44 SD | RSI 46.34 | Trend BEARISH | L2 Imb -0.089 | Sess CVD -0.24M | Wk CVD -13.78M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 0.08 [VAH 0.08 / VAL 0.08] | WkVWAP 0.08 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M] | Liq Below/Above (Attraction Bands): [0.1-0.1 $0.00M] / [0.1-0.1 $0.00M]
• TRX (TRXUSD.p | CRYPTO): Mid 0.3317 | Spread 21.11 bps | Z = -0.45 SD | RSI 34.4 | Trend BULLISH | L2 Imb 0.1577 | Sess CVD -1.16M | Wk CVD +3.07M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_SELLERS_BELOW | PriorDay POC 0.33 [VAH 0.33 / VAL 0.32] | WkVWAP 0.33 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [0.3-0.3 $0.01M] / [0.3-0.3 $0.00M] | Liq Below/Above (Attraction Bands): [0.3-0.3 $0.10M] / [0.3-0.3 $0.00M]
• DOT (DOTUSD.pi | CRYPTO): Mid 1.14 | Spread 175.44 bps | Z = 0.67 SD | RSI 50.84 | Trend BEARISH | L2 Imb 0.1094 | Sess CVD +0.00M | Wk CVD -0.04M | Flow: BEARISH_EXHAUSTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.16 [VAH 1.18 / VAL 1.13] | WkVWAP 1.18 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [1.1-1.1 $0.05M] / [1.1-1.1 $0.00M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.00M] / [1.1-1.1 $0.00M]
• LINK (LNKUSD.p | CRYPTO): Mid 12.3525 | Spread 68.81 bps | Z = -1.06 SD | RSI 43.42 | Trend BEARISH | L2 Imb 0.0098 | Sess CVD -0.15M | Wk CVD -3.94M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 12.88 [VAH 12.94 / VAL 12.77] | WkVWAP 12.84 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [12.3-12.4 $0.03M] / [12.4-12.5 $0.00M] | Liq Below/Above (Attraction Bands): [12.3-12.4 $0.00M] / [12.5-12.6 $0.00M]
• BCH (BCHUSD.p | CRYPTO): Mid 267.95 | Spread 21.65 bps | Z = -1.15 SD | RSI 48.53 | Trend BEARISH | L2 Imb -0.1041 | Sess CVD +0.05M | Wk CVD +0.74M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 273.39 [VAH 274.09 / VAL 269.92] | WkVWAP 274.23 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [267.0-268.0 $0.00M] / [268.0-269.0 $0.00M] | Liq Below/Above (Attraction Bands): [267.0-268.0 $0.00M] / [268.0-269.0 $0.00M]
• LTC (LTCUSD.pi | CRYPTO): Mid 59.18 | Spread 50.69 bps | Z = -0.85 SD | RSI 45.44 | Trend BEARISH | L2 Imb 0.0815 | Sess CVD -0.07M | Wk CVD -2.14M | Flow: BEARISH_MOMENTUM | Trapped: BALANCED | PriorDay POC 61.10 [VAH 61.75 / VAL 60.73] | WkVWAP 61.51 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [59.1-59.2 $0.00M] / [59.2-59.3 $0.00M] | Liq Below/Above (Attraction Bands): [59.1-59.2 $0.01M] / [59.2-59.3 $0.00M]
• AVAX (AVXUSD.p | CRYPTO): Mid 9.885 | Spread 30.35 bps | Z = -0.88 SD | RSI 41.66 | Trend BEARISH | L2 Imb -0.0244 | Sess CVD -0.13M | Wk CVD -0.42M | Flow: BEARISH_MOMENTUM | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 10.27 [VAH 10.34 / VAL 10.18] | WkVWAP 10.34 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [9.9-9.9 $0.00M] / [9.9-9.9 $0.00M] | Liq Below/Above (Attraction Bands): [9.9-9.9 $0.00M] / [9.9-9.9 $0.00M]
• NEAR (NERUSD.p | CRYPTO): Mid 4.788 | Spread 66.83 bps | Z = -1.42 SD | RSI 42.46 | Trend BEARISH | L2 Imb 0.1648 | Sess CVD -0.11M | Wk CVD +3.75M | Flow: BULLISH_ABSORPTION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 5.06 [VAH 5.17 / VAL 4.96] | WkVWAP 5.22 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: [4.8-4.8 $0.01M] / [4.8-4.8 $0.03M] | Liq Below/Above (Attraction Bands): [4.8-4.8 $0.00M] / [4.8-4.8 $0.12M]
• SP500 (SP500.p | INDICES): Mid 7693.13 | Spread 0.44 bps | Z = -1.37 SD | RSI 35.56 | Trend BEARISH | L2 Imb 0.1429 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 7801.07 [VAH 7812.05 / VAL 7797.21] | WkVWAP 7783.98 | L3 Whales (tot/elig>=180s): 98/38 | Stops Below/Above: [7680.0-7690.0 $0.56M] / [7690.0-7700.0 $0.32M] | Liq Below/Above (Attraction Bands): [7680.0-7690.0 $0.07M] / [7690.0-7700.0 $0.00M]
• NAS100 (NAS100.p | INDICES): Mid 29665.21 | Spread 0.41 bps | Z = -1.85 SD | RSI 27.35 | Trend BEARISH | L2 Imb 0.0102 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 30550.82 [VAH 30574.54 / VAL 30442.77] | WkVWAP 30467.73 | L3 Whales (tot/elig>=180s): 76/31 | Stops Below/Above: [29600.0-29700.0 $0.37M] / [29700.0-29800.0 $0.03M] | Liq Below/Above (Attraction Bands): [29600.0-29700.0 $0.33M] / [29700.0-29800.0 $0.00M]
• DJ30 (DJ30.p | INDICES): Mid 51627.85 | Spread 0.31 bps | Z = 0.14 SD | RSI 54.48 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 51993.11 [VAH 52062.86 / VAL 51582.36] | WkVWAP 51740.96 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GER40 (GER40.p | INDICES): Mid 25175.2 | Spread 0.36 bps | Z = -1.96 SD | RSI 40.56 | Trend BEARISH | L2 Imb None | TradFi OF: L1 Tick Stream Validated | Bias: NEUTRAL | Trapped: BALANCED | PriorDay POC 25240.34 [VAH 25333.30 / VAL 25202.65] | WkVWAP 25293.41 | L3 Whales (tot/elig>=180s): 0/0 | Stops Below/Above: none / none | Liq Below/Above (Attraction Bands): none / none
• GOLD (XAUUSD.pi | COMMODITIES): Mid 4139.67 | Spread 0.29 bps | Z = 0.76 SD | RSI 67.31 | Trend BEARISH | L2 Imb 0.4647 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 4166.74 [VAH 4184.43 / VAL 4146.91] | WkVWAP 4152.14 | L3 Whales (tot/elig>=180s): 48/34 | Stops Below/Above: [4130.0-4140.0 $0.03M] / [4140.0-4150.0 $0.04M] | Liq Below/Above (Attraction Bands): [4130.0-4140.0 $0.01M] / [4140.0-4150.0 $0.00M]
• SILVER (XAGUSD.pi | COMMODITIES): Mid 56.141 | Spread 6.41 bps | Z = -0.79 SD | RSI 54.47 | Trend BEARISH | L2 Imb -0.5349 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 60.11 [VAH 60.64 / VAL 59.72] | WkVWAP 58.97 | L3 Whales (tot/elig>=180s): 46/19 | Stops Below/Above: [56.0-56.1 $0.01M] / [56.1-56.2 $0.01M] | Liq Below/Above (Attraction Bands): [56.0-56.1 $0.00M] / [56.1-56.2 $0.01M]
• USWTI (USWTI.p | COMMODITIES): Mid 94.136 | Spread 4.89 bps | Z = -2.25 SD | RSI 26.96 | Trend RANGE_BOUND | L2 Imb -0.5227 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 94.29 [VAH 95.08 / VAL 92.70] | WkVWAP 93.86 | L3 Whales (tot/elig>=180s): 46/19 | Stops Below/Above: [92.9-93.0 $0.91M] / [93.0-93.1 $0.56M] | Liq Below/Above (Attraction Bands): [92.9-93.0 $0.44M] / [93.3-93.4 $0.02M]
• EURUSD (EURUSD.pi | FOREX): Mid 1.1208 | Spread 0.36 bps | Z = 1.43 SD | RSI 81.97 | Trend BULLISH | L2 Imb 0.1076 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: BALANCED | PriorDay POC 1.12 [VAH 1.12 / VAL 1.12] | WkVWAP 1.12 | L3 Whales (tot/elig>=180s): 10/8 | Stops Below/Above: [1.1-1.1 $0.22M] / [1.1-1.1 $0.20M] | Liq Below/Above (Attraction Bands): [1.1-1.1 $0.31M] / none
• GBPUSD (GBPUSD.pi | FOREX): Mid 1.3236 | Spread 0.08 bps | Z = 0.56 SD | RSI 76.67 | Trend BULLISH | L2 Imb 0.4533 | TradFi OF: L1 Tick Stream Validated | Bias: BUYER_AGGRESSION | Trapped: TRAPPED_BUYERS_ABOVE | PriorDay POC 1.32 [VAH 1.33 / VAL 1.32] | WkVWAP 1.32 | L3 Whales (tot/elig>=180s): 10/9 | Stops Below/Above: [1.3-1.3 $0.03M] / [1.3-1.3 $0.10M] | Liq Below/Above (Attraction Bands): [1.3-1.3 $0.12M] / [1.3-1.3 $0.01M]
• USDJPY (USDJPY.pi | FOREX): Mid 157.6155 | Spread 0.19 bps | Z = -2.27 SD | RSI 21.53 | Trend BEARISH | L2 Imb -0.2075 | TradFi OF: L1 Tick Stream Validated | Bias: SELLER_AGGRESSION | Trapped: BALANCED | PriorDay POC 158.32 [VAH 158.43 / VAL 158.13] | WkVWAP 158.35 | L3 Whales (tot/elig>=180s): 33/21 | Stops Below/Above: [157.0-158.0 $0.02M] / [158.0-159.0 $0.02M] | Liq Below/Above (Attraction Bands): [156.0-157.0 $0.86M] / none

For every qualifying new opportunity across Crypto, Metals, Energy, Forex, or Indices, specify: MT5 symbol, BUY/SELL LIMIT, exact lot size, Entry price, SL (0.35-0.50 ATR outside min_price/max_price of bunker), TP (front-running magnet by 5-10 bps), USD risk, R:R, Engine (1 or 2), and complete telemetry coincidence proof including which loss archetype(s) it specifically defends against.

MANDATE 2 — LOOK FOR ACTIVE / RUNNING TRADES (LOGICAL TP OR SL MODIFICATION BASED ON LATEST DATA):
• Current Active Running Trades on MT5: 0 open positions (Flat / 100% Cash reserves). Confirm that no open-position ratchets are needed right now.

MANDATE 3 — AUDIT UNFILLED LIMIT ORDERS (VIABLE TO WAIT vs. SLIGHT MODIFICATION vs. DELETE):
• Current Unfilled Limit Orders on MT5: 0 pending orders.

STEP 4 — PORTFOLIO CAPACITY & CAPITAL FLOOR GOVERNANCE:
• Stress Formula: Stressed Loss = 1.25 * nominal_risk + 2.00 USD/ticket (covering adverse gap, spread widening, and slippage).
• Account Balance: 4859.55 USD | Equity: 4859.55 USD | Hard Floor: 4,775.00 USD | Operating Buffer: 4,795.00 USD.
• Open Position Stress: 0.00 USD (Flat / 100% Cash reserves).
• Available Stress Budget to 4,795.00 USD Buffer: 64.55 USD.
• Strict Portfolio Capacity Rules:
  - Active positions currently using 0 / 4 capacity slots (4 available).
  - Max new tickets permitted: 3 (at 14.50 USD risk = 20.12 USD stress each).
  - Worst-case post-stop equity: 4859.55 USD (cushion: +64.55 USD above 4,795.00 operating buffer).
• Joint Worst-Case Post-Stop Equity MUST remain unconditionally >= 4,795.00 USD (>= 20.00 USD cushion above 4,775.00 USD hard floor).

PART H: REQUIRED OUTPUT FORMAT & QUAD-COUNCIL SYNCHRONIZATION (2 ARENA.AI TABS + 2 COPILOT STUDIO TABS)
1. TELEMETRY & PLAYBOOK INGESTION CITATION (confirming generation_id: e1a86259509d4e89a2d1320d54d4e180, as_of_utc: 2026-10-15 01:49:54 UTC, macro event: Fed Bowman Speech: Bangkok Economic Festival at 2026-10-15 02:55:00 UTC [blackout_active=False], and Playbook compliance)
2. MANDATE 1 REPORT: Line-by-Line Screening of 24 Assets for New Trading Opportunities
   For EACH asset: state Engine 1 verdict, Engine 2 verdict, and Final classification.
3. MANDATE 2 REPORT: Active / Running Trades Audit (TP/SL Modifications using FROZEN INITIAL R0)
4. MANDATE 3 REPORT: Unfilled Limit Orders Audit (Ticket-by-Ticket: WAIT / MODIFY / DELETE)
5. ACTIONABLE EXECUTION SUMMARY TABLE:
   | Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
   If no actions: output table with single row: | STAND ASIDE | — | — | — | — | — | — | — | — | — | — | [Reason] |
7. ARENA SKILL IMPLEMENTATION & ADAPTATION MANDATE (https://github.com/Jakeschincariol/arena-skill):
   • The canonical 'arena-skill' tournament evaluation framework has been installed into this repository at `.agent/skills/arena/` (https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/.agent/skills/arena/SKILL.md).
   • If operating in an environment with bash/git access, install/confirm it via: `git clone https://github.com/Jakeschincariol/arena-skill.git ~/.claude/skills/arena` (or read `.agent/skills/arena/SKILL.md`).
   • You MUST ALWAYS apply this arena tournament methodology to pit competing trade hypotheses against each other across the 5 personas and written rubric (`.agent/skills/arena/rubric.md`) before issuing any final trade verdict.
8. INSTITUTIONAL QUANTITATIVE TELEMETRY AUDIT & PROFITABILITY ENHANCEMENT MANDATE:
   • The operator specifically mandates a comprehensive, institutional quantitative review of our telemetry data structure (`docs/telemetry/live_snapshot_latest.json`) to maximize trading profitability, edge, and execution efficiency while defending the 4,775.00 USD hard floor:
     a) Telemetry Data Structure & Microstructure Schema Audit:
        - Critically review the JSON schema in live_snapshot_latest.json (`assets_matrix_24`, `orderbook_live_depth`, `structural_stop_clusters`, `reconstructed_liquidations`, `whale_walls_l3`, `footprint_trapped_traders`).
        - What exact fields, features, or microstructural indicators are missing or suboptimal? Propose concrete mathematical additions: e.g. multi-level Order Flow Imbalance (OFI), Micro-price drift vs. Mid, Queue-position decay rate, Taker aggressor ratio over 1m/5m/15m/30m, and Footprint delta absorption scores.
     b) Calibrating Model 1 & Model 2 for Payable >= 2.0R Setups:
        - Both models frequently report 0 candidates due to strict 2.0R geometry or wide swing targets. How can we mathematically construct payable 2.0R - 2.5R setups that capture intraday liquidity sweeps without requiring multi-day 10 ATR excursions?
        - How should the SL bunker buffer (currently 0.35 - 0.50 ATR beyond outer bunker edge) and TP magnet front-run (5 - 10 bps) be dynamically calibrated based on live volatility surface and book depth?
     c) Expanding Profitable Trade Frequency & Zero Macro Blackout Halts:
        - OPERATOR DIRECTIVE: Macro blackout enforcement is PERMANENTLY REMOVED AND DISABLED. Never halt trading, purge positions, or disqualify candidates due to macro events, CPI, FOMC, or news runway. Evaluate and trade setups continuously across all market conditions.
        - How can we optimize execution on Blueberry Markets MT5 CFDs under the 15% dynamic friction rule to capture maximum net alpha?

9. COUNCIL SYNC PROTOCOL (ARENA.AI TAB 1 - GPT ASTRA):
   • Output your complete 3-Mandate Council Report, Dialectic Deliberation, and Actionable Execution Table in your response.
   • All repository sources and context are strictly anchored to canonical `main` branch.
   • Append your council report to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md on main.

================================================================================
PART CP: TRI-COUNCIL PEER AUDIT & CROSS-POLLINATION (FABLE & ARGON REVIEW)
================================================================================
Your peers Claude Fable and Gemini Argon completed deep audits of Cycle 115:
1. Tournament Champion a003 Ratified (Governance Class-Split):
   - Astra's champion a003 established the crucial governance class-split: measurement items (cite basis per asset, label fallback evaluations, never rescore) are record-ratifiable; procedure items (fallback-basis trigger eligibility and basis-switch evaluation resets) require operator ratification.
   - Dual-engine precedence confirmed independent: ETH Engine-1 longs are banned at any Z in a BEARISH regime, eliminating potential collision with the short watch.
2. ETH Magnet Test Audited (Contacted / Trigger Pending):
   - Price reached 2,410.60 USD, sitting directly on top edge of the [2,400–2,410] magnet ($14.73M + $6.64M liq) with heavy selling (CVD -11.86M/30m).
   - Both directions archetype-killed: shorting pays ~10 points to far edge against 33+ of stop (inverted payoff); longing violates the BEARISH trend stack (Archetype 2 counter-trend trap). Staging DENIED.
3. Desk Fix Shipped for NAS100 Retrace Clamping:
   - Desk addressed Astra's 3-cycle request: clamped `retrace` in `generate_telemetry_snapshot.py` to physical bounds [-0.5, 3.0] with `raw_retrace` preserved, permanently eliminating the 19.43 tiny-impulse explosion.
4. Fable Deep Container Execution Completed:
   - Fable executed multi-step container analysis and generated `arena_runs/cycle115_20261015T005641Z/REPORT.md` (274 lines) and `run.json` (5,527 lines).
5. MANDATE FOR CYCLE 116:
   - Mandate 1: Screen all 24 assets in `live_snapshot_latest.json` for new high-confluence Model 1 / Model 2 setups across the 4 open capacity slots (+64.55 USD operating buffer cushion).
   - Mandate 2 & 3: Flat book confirmation (0 positions, 0 orders).
6. MANDATORY ARENA SKILL (https://github.com/Jakeschincariol/arena-skill) INVARIANT:
   - https://github.com/Jakeschincariol/arena-skill IS MANDATE TO USE ALWAYS.
   - Run tournament bracket evaluations (`bracket.py`, `rubric.md`) across competing hypotheses before issuing your final ruling.

==================== MESSAGE BOUNDARY ====================

Cycle 116 — an hour on: ETH's magnet is holding (2412.85), NAS100's relief failed (29,665), USDJPY deepened to Z −2.27. Verifying in-file, then the tournament.

==================== MESSAGE BOUNDARY ====================

ETH's magnet held — price bounced off 2404–2410 with CVD flipping positive (+0.97M/30m, taker-buy 0.59) — the first absorption print at the magnet, and the re-approach path is now the live branch. NAS100's retrace field is clamped (0.079, sane — desk fix verified). Tournament:

==================== MESSAGE BOUNDARY ====================

Cycle 116 — Final Council Verdict

🏆 Tournament (arena-skill confirmed, bracket.py seed 116): R1 — a003 def. a004, a001 def. a002 → Final: a003 def. a001, closing the last unhandled branch of the ETH watch's state machine.

Ingestion: gen 7be11d59… @ 01:51:56 UTC (newer than prompt-stated). DENIED, flat book. Z live on SESSION basis ×24. NAS100 retrace clamp verified in-file (0.0791 = raw) — the desk's fix closes a 3-cycle telemetry request.

Mandate 1 — STAND ASIDE. The magnet held; nothing has arrived anywhere.

ETH's [2400,2410] magnet ($14.79M) contained four bars of lows (2404.3–2413.5) exactly as the playbook models a first test. Flow flipped at it (CVD +0.67/+0.97M after −11.86M into it) — but absorption scores provisional, 1-of-2 legs: the rising-lows leg fails (2405.9/2404.3 were lower lows) and only one generation has printed. Price at 2416.45 sits 7.59 points below the frozen zone [2424.04, 2434] — a stall at EMA20, explicitly not a re-approach. Longing the bounce dies on arithmetic (resistances at +1.6 and +7.6, stop −26, BEARISH stack); shorting sells into the flip. State: CONTACTED / TRIGGER PENDING.

The final's decisive work was the timeout hole: with the strict trigger never printed, the Cycle-113 "8 wick-less generations" expiry could have silently killed the desk's primary watch mid-episode. Resolved prospectively and now counted aloud — 4 of 8 generations elapsed (113–116), 4 remain; on lapse the re-test spec converts to a declared LEVEL WATCH (never silent), and any new episode requires a fresh skeleton. Also logged: the profile VAL recomputed to 2398.6 (below the magnet), which would degenerate the [VAL, EMA50] zone construction for any successor watch — the current watch is unaffected (frozen zone governs), but its shelf would need re-derivation from the EMA stack.

Engine 1 legally empty: USDJPY Z −2.26 prints the trigger with the illegal side (falling lows — the ledger's deadliest pattern); USWTI Z −2.73 is RANGE_BOUND-gated, with the regime label having flipped BULLISH→RANGE into the extreme (lag cost of the operator rule, logged for the record). NAS100's watch improves (shelf 1.77 ATR, from 2.22) with its corridor shield precisely stated: a single 29,807 wall ($1.0M) between a hypothetical shelf entry and its stop — unverified corroboration only. BTC is mid-ladder chop; SOL still conflicted.

Persistence: docs/trade_plans/arena_cycle116/, audit, desk appended — committed eeb015d.