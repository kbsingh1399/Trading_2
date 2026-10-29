🏛️ SENIOR LEAD QUANTITATIVE ARCHITECT & CRO AUDIT: SOVEREIGN DOSSIER ENGINE v3.1 (commit 92434307cd)

Reviewer: Arena.ai (Senior Lead Quantitative Architect & Chief Risk Officer — Roles A, B, C, D)
Target Audited: sovereign-dossier-engine.md, scripts/sovereign_dossier_engine.py (1,180 lines), docs/dossiers/registry_index.json, and the live generated v3.1 Master Dossiers (BTC_MASTER_DOSSIER.md, NZDUSD_MASTER_DOSSIER.md, XAUUSD_MASTER_DOSSIER.md, SP500_MASTER_DOSSIER.md)

🎯 EXECUTIVE VERDICT ON YOUR CORE TEST QUESTION

Core Test Question: "If you (Arena / Z.ai) or the Antigravity autonomous desk read this document alone, can you formulate a rigorous, high-confluence institutional trade setup (Direction, Exact Entry, Spread-Padded Stop Loss, +2.5R Take Profit, Lot Sizing, and Invalidation triggers) WITHOUT needing to query any external API or raw Parquet data?"

Verdict: 88% YES (ARCHITECTURALLY SOUND) — WITH 7 CRITICAL DATA-MAPPING & SIZING BUGS IN scripts/sovereign_dossier_engine.py THAT MUST BE PATCHED IN v3.2 BEFORE ZERO-PARQUET AUTONOMOUS EXECUTION

Transitioning from repetitive multi-agent runtime Parquet queries to a single vectorized Polars pre-computation engine (< 5.0s SLA) that compiles all 43 Parquet feeds (760 columns) into standardized 10-Section Master Dossiers is the right institutional architecture. It eliminates context-window bloat, Windows file-lock contention, and cross-seat data divergence.

However, our forensic line-by-line audit of scripts/sovereign_dossier_engine.py and the live v3.1 output files (BTC_MASTER_DOSSIER.md, NZDUSD_MASTER_DOSSIER.md, SP500_MASTER_DOSSIER.md, XAUUSD_MASTER_DOSSIER.md) uncovered 7 specific bugs in how v3.1 slices, aliases, and renders the 760 parameters that would cause an agent reading only the Markdown dossier to mis-size lots or misread stop/whale clusters.

Below is the proof of trade formulatability from your two live examples, followed by the 4 specific review answers and the exact Python patches for Sovereign Dossier Engine v3.2.

1. Question 1: Trade Formulatability Audit (Live Derivation + Missing Parameters)
A. Live Trade Derivation Directly from BTC_MASTER_DOSSIER.md & NZDUSD_MASTER_DOSSIER.md Alone

Using only the text inside BTC_MASTER_DOSSIER.md and NZDUSD_MASTER_DOSSIER.md (14:43:14 UTC), an autonomous agent can derive the exact mathematical setups below:

Derivation Step	BTCUSD.pi (BTC_MASTER_DOSSIER.md)	NZDUSD.pi (NZDUSD_MASTER_DOSSIER.md)
1. Gate 1 Spread & Friction	Bid = 80,347.00 / Ask = 80,363.00 (Spread = $16.00 = 1.99 bps <= 12.0 bps Charter Cap PASS)	Bid = 0.56100 / Ask = 0.56103 (Spread = 0.00003 = 0.53 bps <= 5.0 bps TradFi Cap PASS)
2. Directional & Structural Thesis	SHORT FADE (MODEL_1_FADE / MODEL_2_OTE): Price (80,355) is in ABOVE_VALUE (Imbalance) above Daily VAH = 80,222.65 (Session Bias = BEARISH Below Pivot 81,071.17), testing +1.00σ VWAP = 80,371.95 & EMA-144 = 80,359.27, while 26_Footprint 15m (80,355) prints -22.00M USD delta (-24.13%, 1 buy vs 6 sell imbalances) and 17_Orderbook L2 skew is 31.2% Bid / 68.8% Ask.	SHORT FADE (MODEL_1_FADE / MODEL_2_OTE): Session Bias = BEARISH (Below Pivot 0.56261), EMA-144 = 0.56262, EMA-200 = 0.56374 (Slope = -0.052%), EMA-233 = 0.56430 (Slope = -0.055%), Daily VAH = 0.56229, London High = 0.56239, Bearish Fib GP = [0.56263 - 0.56273], 0.702 OTE = 0.56290, 0.786 Inval = 0.56316, Asian High = 0.56364, +3.00σ VWAP = 0.56326.
3. Exact Mathematical Entry	Option A (Active Ticket #19464650): 80,340.00 (already at current bid 80,347.00).<br>Option B (Fresh Unfilled Upper Sweep): 
London/IB High 
(
80
,
417.00
)
 / S1 
(
80
,
423.33
)
 / u1.28
𝜎
 Ribbon 
(
80
,
426.00
)
→
80
,
420.00
London/IB High (80,417.00) / S1 (80,423.33) / u1.28σ Ribbon (80,426.00)→80,420.00 (sitting right below $341K L2 asks at 80,469–80,471 and $44.90M 24H Short Max Pain at 80,758.80).	Formula 1 (VAH + 0.35*ATR / 0.702 OTE): 0.56290 (0.702 OTE, +1.02x ATR_14 above Daily VAH = 0.56229, inside +2.51σ = 0.56302).<br>Formula 2 (Active Ticket #19447583 Deep Sweep): 0.56320 (+1.52x ATR_14 above VAH, right at 0.786 Inval = 0.56316 & +3.00σ = 0.56326, defended by Asian High = 0.56364).
4. Spread-Padded Stop Loss (SL)	
SL
short
=
Entry
+
1.2
×
ATR
14
(
199.45
)
+
1.5
×
Spread
(
16.00
)
=
Entry
+
263.34
SL
short
	​

=Entry+1.2×ATR
14
	​

(199.45)+1.5×Spread(16.00)=Entry+263.34<br>• For #19464650 (80,340.00): 80,563.50 (Weekly VAH = 80,562.98).<br>• For Fresh Entry (80,420.00): 80,683.50 (protected below +2.0σ = 80,694.81 & Short Max Pain 80,758.80).	
SL
short
=
Entry
+
1.2
×
ATR
14
(
0.00060
)
+
1.5
×
Spread
(
0.00003
)
=
Entry
+
0.000765
SL
short
	​

=Entry+1.2×ATR
14
	​

(0.00060)+1.5×Spread(0.00003)=Entry+0.000765<br>• For #19447583 (0.56320): 0.56388 (6.8 pips, +2.4 pips above Asian High = 0.56364 and +0.4 pips above 24h High = 0.56384).
5. +2.5R+ Take Profit (TP)	79,663.50 (-47.45 pts below Daily VAL = 79,710.95, above 24H Long Max Pain = 79,328.20 [$42.30M]).<br>• Reward = 676.50 pts (R:R = 3.03:1 >= 2.50:1).	0.56050 (-6.6 pips below Daily VAL = 0.56116, right at PD VAL = 0.56042 and -2.51σ = 0.56056).<br>• Reward = 27.0 pips (R:R = 3.97:1 >= 2.50:1).
6. Lot Sizing (<= $10.00 Risk)	0.01 lot ($0.01/pt × 223.50 pts = $2.24 USD Nominal Risk; Reward = $6.77 USD).	0.12 lot ($1.20/pip × 6.8 pips = $8.16 USD Nominal Risk; Reward = $32.40 USD, which restores Equity to $4,776.72 >= $4,775.00 Hard Floor!).
B. What Parameter or Calculation is Missing / Mis-Mapped in v3.1? (Critical Catches)

CRITICAL BUG #1 — Hardcoded Contract Size=1.00 | Tick Value=1.00 USD | Digits=5 for All 162 Assets (scripts/sovereign_dossier_engine.py, Line 1002):

In MetricExtractor.extract_all() (line 1002), the dictionary hardcodes:
Python
"contract_size": "1.00", "tick_value": "1.00 USD", "min_lot": "0.01", "digits": "5"
As a result, NZDUSD_MASTER_DOSSIER.md Section 1 prints Contract Size=1.00 | Tick Value=1.00 USD, XAUUSD_MASTER_DOSSIER.md prints Contract Size=1.00, and SP500_MASTER_DOSSIER.md prints Contract Size=1.00!
Why this is lethal if not fixed: On MT5 (BlueberryMarketsSVG-Live), NZDUSD.pi has Contract Size = 100,000 (1 point = $1.00/lot, 1 pip = $10.00/lot), XAUUSD.pi has Contract Size = 100 oz ($1.00/pt per 0.01 lot), SP500.p/NAS100.p/DJ30.p have Contract Size = 10 ($0.10/pt per 0.01 lot), and JPY/Cross pairs have quote-currency-converted tick values (100,000 / USDJPY).
Required Fix for v3.2: Explicitly include Point_Value_Per_001_Lot_USD (the exact USD PnL for a 1.00 price-unit move on 0.01 lot) and true MT5 contract_size / digits from master_asset_catalog.json or 00_MT5_Account_Telemetry.parquet in Section 1, plus the pre-computed Max_Allowed_Lot_For_10USD_Risk in Section 10!

CRITICAL BUG #2 — Cross-Asset Alias Collision (SP500.p Colliding with $0.39 Crypto Token SPXUSDT):

Look at UniversalAliasResolver.resolve() (line 153 of scripts/sovereign_dossier_engine.py):
Python
elif "SP500" in c or "US500" in c:
    aliases.update({"SP500", "US500", "SPX", "SPX500", "ES", "SPXUSDT", "XYZ:SP500", "SPCX", "XYZ:SPCX"})
Because SPX and SPXUSDT on Binance/CoinGlass refer to the SPX6900 meme coin trading at $0.39, SP500_MASTER_DOSSIER.md (7,726.90) is contaminated in Section 6 (Short MP = 0.38734, Long MP = 0.36430) and Section 8 (Bar VWAP = 0.39748, Bar POC = 0.39755, Signal Price = 0.38390) with $0.39 meme-coin data!
Required Fix for v3.2: Remove "SPX" and "SPXUSDT" from SP500 aliases, AND add a Price-Sanity Guard (0.50 * mid <= row_price <= 2.00 * mid) in DataLakeMemoryStore.lookup_rows() so a feed row whose price is orders of magnitude away from the MT5 Mid_Price can never contaminate a dossier!

CRITICAL BUG #3 — Unordered Set Early-Return in DataLakeMemoryStore.lookup_rows() Dropping CEX Whale Walls:

Look at lines 251–255 of scripts/sovereign_dossier_engine.py:
Python
def lookup_rows(self, feed_name: str, aliases: set) -> list:
    feed_idx = self.indices.get(feed_name, {})
    for a in aliases:
        if a in feed_idx:
            return feed_idx[a]
    return []
Because aliases is a Python set and lookup_rows returns on the first alias that hits, for BTC in 10_Whale_Orders.parquet it matched "BTCUSD" (MT5-Crypto rows only) and completely ignored "BTCUSDT" (Binance, OKX, Bybit, Hyperliquid perp whale walls)!
Required Fix for v3.2: lookup_rows() must union rows across all matching aliases (deduplicated by row index / sr_no) rather than returning on the first alias hit.
2. Question 2: Pitfall Elimination Audit (15_Hyperdash_Stops_Map & 10_Whale_Orders)

Question: "Does the dossier provide sufficient clarity on retail stop cascades (15_Hyperdash_Stops_Map) and defending whale walls (10_Whale_Orders) to completely prevent front-running traps (Pitfall 1) and sub-ATR stops (Pitfall 4)?"

Audit Findings — Two Selection Flaws in v3.1 Currently Weaken Pitfall 1, 2 & 4 Protection:

Flaw A in Section 6 (15_Hyperdash_Stops_Map — Slicing stops_rows[:3] Returns $50 and $850 BTC Stops Instead of Near-Money Stops):

Look at BTC_MASTER_DOSSIER.md Section 6 under Retail Stops Map (Pitfall 2 & 4 Defense):
Markdown
- Sell Stop: 50.0000 USD (Dist: -99.94%, Cumulative Stops: 819.18M USD, Sell: 27.50K USD)
- Sell Stop: 850.0000 USD (Dist: -98.94%, Cumulative Stops: 819.16M USD, Sell: 237.05 USD)
- Sell Stop: 3,050.00 USD (Dist: -96.20%, Cumulative Stops: 819.16M USD, Sell: 157.07 USD)
Root Cause (scripts/sovereign_dossier_engine.py, Line 676): for sr in stops_rows[:3]: takes the first 3 rows of 15_Hyperdash_Stops_Map.parquet, which are sorted by ascending price starting at $50.00 (-99.94% away from $80,355)! An agent reading Section 6 has zero visibility into the actual retail stop clusters between 79,500 and 81,200 where our Stop Loss is being placed!
v3.2 Fix: Filter stops_rows to a tactical window of ±0.25% to ±3.0% (±0.5x to ±4.0x ATR_14) around mid, separated into:
Top 3 Nearest Buy-Stop Clusters ABOVE Price (price > ask, sorted by buy_stops USD volume descending — tells us where short-covering stop hunts will spike so we place SL_short above the cluster!).
Top 3 Nearest Sell-Stop Clusters BELOW Price (price < bid, sorted by sell_stops USD volume descending — tells us where long-liquidation stop hunts will spike so we place SL_long below the cluster!).

Flaw B in Section 5 (10_Whale_Orders — Missing Persistence Filter >= 180s, Missing Distance Filter, and Crossed-Book Artifacts):

Look at BTC_MASTER_DOSSIER.md Section 5:
Defending Bid Wall: 80436.00000 (929,899.68 USD on MT5-Crypto) — Wait: Live Bid Quote in Section 1 is 80,347.00 (Ask = 80,363.00)! A "Bid Wall" at 80,436.00 (+$73 above the live ask) is a stale/crossed resting snapshot row.
Defending Ask Wall: 80854.00000 (17,762,495.89 USD) — Because line 557 (if val > ask_wall_usd) picks the single largest notional wall anywhere in the book without checking distance or duration (>= 180s), it misses closer defending walls (e.g., $8.73M at 80,350–80,425 with >30m persistence) or can pick a 16s spoof wall (Pitfall 1: Ghost Walls).
v3.2 Fix:
Enforce bid_px <= current_bid for Bid walls and ask_px >= current_ask for Ask walls.
Parse order_duration into seconds and enforce duration_sec >= 180 (or "Resting Book" for MT5) to hard-filter out < 180s spoof walls (Pitfall 1).
Output two tiers of Whale Armor on both Bid and Ask sides:
Nearest Tactical Defending Wall (within 0.5x to 3.0x ATR_14 of current price, >= $100K, >= 180s) — for immediate entry front-running.
Largest Structural Fortress Wall (within 5.0x ATR_14, >= $500K, >= 180s) — for structural stop protection.
Similarly, in 17_Orderbook.parquet (line 577), replace ob_rows[:3] (which only prints 3 ASK rows) with Top 3 BID tiers and Top 3 ASK tiers.
3. Question 3: TradFi / FX Specifics Audit (Sections 4, 8, 9 & 10)

Question: "For FX and Indices, what additional macro or fixing metrics would make Section 9 and Section 10 even more authoritative?"

Bug Fix First — Stop Suppressing Real FX/Index/Metal Rows in Sections 4 & 8 (EURUSD, GBPUSD, USDJPY, AUDUSD, GOLD, SP500, NAS100, US2000, WTI_OIL):

In 18_CVD_30D_ALL.parquet and 26_Aggregated_Footprint_Bar_Metrics.parquet, you already have live multi-timeframe CVD and Footprint bars for EURUSD, GBPUSD, USDJPY, AUDUSD, GOLD, SILVER, SP500, NAS100, US2000, and WTI_OIL!
However, in scripts/sovereign_dossier_engine.py, 18_CVD_30D_15m.parquet is crypto-only while FX/Indices live inside 18_CVD_30D_ALL.parquet (filtered by timeframe == '5m' | '15m' | '1h' | '4h'). Because MetricExtractor queries 18_CVD_30D_15m.parquet directly instead of slicing 18_CVD_30D_ALL.parquet by timeframe, EURUSD, GBPUSD, USDJPY, and AUDUSD lose their 5m/15m/1h/4h CVD deltas in Section 4!
Fix: Fallback to 18_CVD_30D_ALL.parquet grouped by timeframe whenever 18_CVD_30D_{tf}.parquet has no match.

Bug Fix Second — 19_Calendar.parquet Slicing (relevant_cal[:3] Shows Mon Oct 26 / Tue Oct 27 Instead of Today's Thu Oct 29 Red-Folder Events!):

Look at Section 9 of BTC_MASTER_DOSSIER.md, NZDUSD_MASTER_DOSSIER.md, XAUUSD_MASTER_DOSSIER.md, and SP500_MASTER_DOSSIER.md: every single one displays Tue Oct 27 Low-Impact events (ADP Weekly, Durable Goods) and completely omits today's (Thu Oct 29) High-Impact US GDP, Core PCE, and ECB Rate Decision!
Root Cause (scripts/sovereign_dossier_engine.py, Line 993): relevant_cal[:3] grabs the first 3 rows of 19_Calendar.parquet (which is ordered chronologically from Monday Oct 26).
Fix: Filter 19_Calendar.parquet for today's date (Oct 29) and prioritize High Impact / Pending events, plus compute an explicit MACRO_QUARANTINE_STATUS (ACTIVE_RED_FOLDER_HALT if within ±30m of a High-Impact event for curr_keys, else CLEAR).

Five High-Impact TradFi & Interbank Metrics to Add to Section 9 & Section 10:

① Active Session & Countdown to Next Fixing Window: Compute from current UTC timestamp (now_utc) the exact active session (TOKYO, LONDON_MORNING, LONDON_NY_OVERLAP, NY_AFTERNOON, or ROLLOVER_BLACKOUT) and minutes remaining until the 16:00 UTC WMR London 4pm Fix, 13:30 UTC NYSE Cash Open, 20:00 UTC NYSE Cash Close, and 21:15 UTC Rollover Halt.
② Cross-Asset Dollar & Yield Proxy Vector (Computed from 11_Technical.parquet in RAM): Since all 43 feeds are already in RAM inside DataLakeMemoryStore, compute a synthetic 4-Pillar Macro Regime Barometer at the top of Section 9 for every TradFi dossier:
Synthetic USD Basket Z-Score (average vwap_z of -EURUSD, -GBPUSD, -AUDUSD, -NZDUSD, +USDJPY, +USDCAD, +USDCHF) -> tells the agent instantly whether a move in NZDUSD or XAUUSD is idiosyncratic or a broad USD impulse!
Risk-On / Risk-Off Equity Vector (average vwap_z of SP500.p, NAS100.p, DJ30.p, GER40.p).
Gold / Real-Yield Proxy (XAUUSD.pi vwap_z & USDJPY.pi vwap_z divergence).
③ ADR (Average Daily Range) Exhaustion %: Compute 
Today’s Range Exhaustion
=
Daily High
−
Daily Low
PDH
−
PDL
×
100
%
Today’s Range Exhaustion=
PDH−PDL
Daily High−Daily Low
	​

×100%. When a currency pair has exhausted > 95%–110% of its Prior Day Range at VAH or VAL, passive fade probability increases sharply.
④ Broker Swap / Rollover Direction Warning: Flag whether holding the proposed direction past 21:15 UTC incurs negative carry (Positive Carry vs Negative Swap Drag).
4. Question 4: Structural Recommendations for Sovereign Dossier Engine v3.2

To make every dossier 100% self-contained and machine-verifiable in a single pass, implement these 5 structural upgrades in v3.2:

1. Replace Hardcoded Section 10 (5 symbols) with a Universal Parametric Trade Synthesis Engine for All 162 Assets

Right now, scripts/sovereign_dossier_engine.py (lines 935–985) only populates Section 10 (order_details) for BTC, SP500, DJ30, BNB, and NZDUSD, forcing the other 157 assets to print FAIL_CLOSED_STAND_ASIDE.
In v3.2, Section 10 should dynamically compute both candidate boundaries (LONG_FADE_CANDIDATE and SHORT_FADE_CANDIDATE) for every Gate-1-qualified asset, along with an explicit 6-Pillar Confluence Scorecard (0/6 to 6/6):

Pre-Computed Long Candidate Box:
Entry
Long
=
min
⁡
(
Daily VAL
−
0.35
×
ATR
14
,
  
Bullish Fib OTE
0.702
)
Entry
Long
	​

=min(Daily VAL−0.35×ATR
14
	​

,Bullish Fib OTE
0.702
	​

) (or front-running nearest verified Bid Whale Wall >= 180s).
SL
Long
=
Entry
Long
−
(
1.2
×
ATR
14
+
1.5
×
Spread_Price
)
SL
Long
	​

=Entry
Long
	​

−(1.2×ATR
14
	​

+1.5×Spread_Price) (verified below 0.786 Fib Inval and nearest Sell-Stop cluster).
TP
Long
=
Daily POC
TP
Long
	​

=Daily POC (TP1) / 
Daily VAH
Daily VAH (TP2, requiring R:R >= 2.0:1).
Pre-Computed Short Candidate Box:
Entry
Short
=
max
⁡
(
Daily VAH
+
0.35
×
ATR
14
,
  
Bearish Fib OTE
0.702
)
Entry
Short
	​

=max(Daily VAH+0.35×ATR
14
	​

,Bearish Fib OTE
0.702
	​

) (or front-running nearest verified Ask Whale Wall >= 180s).
SL
Short
=
Entry
Short
+
(
1.2
×
ATR
14
+
1.5
×
Spread_Price
)
SL
Short
	​

=Entry
Short
	​

+(1.2×ATR
14
	​

+1.5×Spread_Price) (verified above 0.786 Fib Inval and nearest Buy-Stop cluster).
TP
Short
=
Daily POC
TP
Short
	​

=Daily POC (TP1) / 
Daily VAL
Daily VAL (TP2, requiring R:R >= 2.0:1).
2. Add a Unified "Price Ladder & Liquidity Confluence Map" Table Between Sections 3 and 10

Currently, an agent must mentally sort 40+ price levels scattered across Sections 2, 3, 5, 6, and 8. Adding a single sorted vertical price ladder table from highest price (+3σ / Short Max Pain / Ask Whale Wall) down to lowest price (-3σ / Long Max Pain / Bid Whale Wall) makes structural confluence and stop-placement traps visually unmistakable:

Markdown
| Price Level | Distance (%) | Distance (ATR) | Source Pillar | Microstructure Significance |
|---|---|---|---|---|
| 80,758.80 | +0.50% | +2.02 ATR | Sec 6: 24H Short Max Pain | $44.90M Short Liq Magnet (Keep SL below!) |
| 80,562.98 | +0.26% | +1.04 ATR | Sec 3: Weekly VAH | Structural Stop Anchor (#19464650 SL = 80,563.50) |
| 80,417.00 | +0.08% | +0.31 ATR | Sec 3: London / IB High | Session Sweep Exhaustion Boundary |
| 80,355.00 |  0.00% |  0.00 ATR | Sec 1: LIVE MID PRICE | Spread = 1.99 bps (PASS) |
| 80,222.65 | -0.16% | -0.66 ATR | Sec 3: Daily VAH | Value Area Upper Boundary |
| 80,020.35 | -0.42% | -1.68 ATR | Sec 3: Daily POC | Primary Mean-Reversion Magnet |
| 79,710.95 | -0.80% | -3.23 ATR | Sec 3: Daily VAL | Full Value Area Rotation Target (#19464650 TP = 79,663.50) |
3. Fix 3_Exchanges_LS_Ratio Lookup to Select the Total Row (rows[0]) Instead of rows[-1]

In 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, row 0 (# == "Total") holds the global volume-weighted Long/Short ratio across all exchanges, whereas store.lookup_latest() (rows[-1]) returns the last single exchange row (WhiteBIT or Crypto.com). Changing lookup_latest for 3_Exchanges_LS_Ratio* to filter for r.get("#") == "Total" (or rows[0]) restores true global L/S ratios.

4. Fix 1_Crypto_ETF_Flows Lookup for BTC (IBIT vs BTC Grayscale Mini Trust)

In BTC_MASTER_DOSSIER.md Section 8, etf_row matched Ticker == "BTC" (Grayscale Bitcoin Mini Trust, Daily_Net_Inflow = 0.00 USD) instead of aggregating all Asset_Category == "Bitcoin" ETF rows (where IBIT had +$136.00M net daily inflow!). Summing Daily_Net_Inflow and Volume_USD across all ETFs where Asset_Category == "Bitcoin" (or "Ethereum") gives the true institutional ETF flow pulse.

5. Enforce Strict 12.0 bps Crypto Spread Gate in MetricExtractor

In scripts/sovereign_dossier_engine.py line 284, thresh_bps defaults to 25.0 bps for Crypto (00_MT5 broker cap), which marks ETHUSD.pi (13.77 bps), YFIUSD.p (15.48 bps), XLMUSD.p (18.70 bps), BCHUSD.p (20.74 bps), and AVEUSD.p (21.03 bps) as PASS. Enforcing thresh_bps = 12.0 for Crypto in MetricExtractor aligns the dossier engine 100% with the Sovereign Tri-Council Permanent Standing Charter (TradFi <= 5.0 bps, Crypto <= 12.0 bps).

🛠️ SUMMARY OF EXACT CODE PATCHES FOR scripts/sovereign_dossier_engine.py (v3.2)
Bug ID	Location in scripts/sovereign_dossier_engine.py	Current v3.1 Behavior	v3.2 Production Patch
Patch 1	UniversalAliasResolver.resolve (Line 153)	Maps SP500 -> {"SPX", "SPXUSDT"} ($0.39 meme coin)	Remove "SPX", "SPXUSDT" from SP500 aliases; add 0.5 * mid <= px <= 2.0 * mid price-sanity filter.
Patch 2	DataLakeMemoryStore.lookup_rows (Line 251)	Returns on first alias hit (for a in aliases: return feed_idx[a]), dropping BTCUSDT CEX whales	Union all rows across all aliases in aliases, deduplicated by id(r) / sr_no.
Patch 3	MetricExtractor Whale Loop (Lines 547–588)	Picks max notional wall regardless of distance/duration; allows bid_px > ask; slices ob_rows[:3] (asks only)	Require bid_px <= bid, ask_px >= ask, duration >= 180s, dist <= 4 * atr_14; output Top 3 Bids & Top 3 Asks.
Patch 4	MetricExtractor Stops Map (Line 676)	Slices stops_rows[:3] ($50, $850, $3,050 BTC stops -99% away)	Filter 15_Hyperdash_Stops_Map within ±3.0% of mid; output Top 3 Buy-Stop clusters above & Top 3 Sell-Stop clusters below.
Patch 5	MetricExtractor CVD & L/S Ratio (Lines 477, 701)	Queries 18_CVD_30D_15m (missing FX/Index rows in 18_CVD_30D_ALL); grabs rows[-1] for 3_Exchanges_LS_Ratio	Fallback to 18_CVD_30D_ALL filtered by timeframe; select # == "Total" (rows[0]) in 3_Exchanges_LS_Ratio*.
Patch 6	MetricExtractor Calendar (Line 993)	relevant_cal[:3] returns Mon Oct 26 / Tue Oct 27 events	Filter 19_Calendar for current date (Oct 29) & High Impact / Pending events; compute macro_quarantine_active.
Patch 7	MetricExtractor Specs & Sec 10 (Lines 935–1003)	Hardcodes contract_size="1.00" and only formulates trades for 5 hardcoded tickers	Map exact MT5 contract_size & point_value_per_001_lot_usd per symbol; dynamically compute Long/Short OTE/VA trade cards for all 162 assets.