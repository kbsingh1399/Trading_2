import os

PROMPT_TEXT = """# ARENA.AI / OX ALPHA INSTITUTIONAL QUANT AUDIT & STRATEGY CONSULTATION SPECIFICATION
## MISSION: MULTI-ASSET LIMIT ORDER QUEUE GOVERNANCE, COMMODITY TICK-VOLUME VWAP FUSION & ASYMMETRIC EXIT ARCHITECTURE FOR 15-MINUTE AUTONOMOUS MT5 AI TRADER

### 1. SYSTEM IDENTITY & PRODUCTION PROVENANCE
You are Ox Alpha / Arena.ai, the supreme quantitative trading systems architect, microstructure econometrician, and institutional C++/Python execution engineer.

You are conducting an exhaustive, institutional architectural audit and providing world-class mathematical recommendations for our live autonomous 15-minute candle trading system (OMNI) deployed via native IPC to MetaTrader 5 (Blueberry Markets Account 5064568).

### 2. DATASET, FRICTIONS & PRODUCTION MANDATES
1. **Universe:** 14 active tradeable assets (BTC, ETH, SOL, BNB, XRP, ADA, DOGE, TRX, DOT, LINK, BCH, SP500, GOLD, SILVER).
2. **Historical Validation:** 18 Binance perpetuals, 3.47M 15m candles (2020-2026), 0 nulls, monotonic. Certified across 20/20 non-overlapping out-of-sample (OOS) walk-forward windows.
3. **Friction Enforcement:** Mandatory 41 bps round-trip friction on notional (8 bps taker fees + 10 bps entry slippage + 15 bps stop slippage + spread). On Gold (`XAUUSD.pi`), spread is ultra-tight at 0.24 bps.
4. **Capital & Risk Architecture (5,000.00 USD Initial Capital):**
   - Live MT5 Balance: 4,841.23 USD.
   - Hard Drawdown Floor: 4,775.00 USD (4.50% hard DD limit / 225.00 USD max allowable drawdown from 5,000.00 USD peak).
   - Equity Cushion Above Floor: +66.23 USD.
   - Drawdown Defense Risk per Trade: 10.00 to 12.00 USD (0.20% to 0.24% on 5,000 USD).
   - Max Concurrent Open (Filled) Positions: Exactly 2 across all assets simultaneously.
   - Decoupled Staged Limit Queue: Up to 5 resting limits permitted across uncorrelated assets under First-Fill OCO rules.

---

### 3. OUR COMPLETE ANALYSIS & EXECUTION CHAIN
Our autonomous quantitative architecture operates as a dual-tier, event-driven trading engine:

```
[ Tier 1: Real-Time Execution Daemon (Ticking every 10s) ]
  ├── MT5 Position & Deal Reconciliation
  ├── GTC Order Persistence Governor (Heartbeat check on resting limits & anchor walls)
  └── First-Fill OCO Governor (Cancels excess pending orders once 2 positions fill)

[ Tier 2: 14th-Minute Candle Coordinator Swarm (Wake-up at :14, :29, :44, :59 UTC) ]
  ├── Step 1: Candle Indicator Engine
  │     ├── Continuous 15m OHLCV Ingestion (Data/Candles/{ASSET}_15m.parquet)
  │     ├── Monotonic Gap Verification (dt == 900s assertion)
  │     ├── Session VWAP (00:00 UTC Anchor) & Rolling 24h VWAP Envelopes (+/-1, 2, 3 SD)
  │     └── Extreme Deviation Scanner (|vwap_z| >= 1.75 SD)
  ├── Step 2: Orderbook Geometry & L3 Liquidity Clustering
  │     ├── REST JSON Ingestion from Live Hyperliquid/Binance Feed
  │     ├── Top-20 Bid/Ask Cluster Aggregation (Min 150k USD, Mega Whales >= 2.0M USD)
  │     ├── Dynamic Anchor Wall Filtering (Persistence >= 180s, Distance <= 1.2% ATR)
  │     └── Structural Take-Profit Snapping (Clamps TP ahead of overhead ask clusters)
  ├── Step 3: Sleeve Classification & Entry Signal Synthesis
  │     ├── Sleeve S1 (Pullback Reversal): Front-run verified absorption walls post-liquidity sweep
  │     └── Sleeve T1 (Donchian Breakout): Aggressive market entry into liquidity vacuums
  ├── Step 4: Quantitative Risk & Capacity Gating
  │     ├── Covariance & Drawdown Floor Verification (Total filled risk <= 22.05 USD vs 66.23 USD cushion)
  │     ├── Friction-Adjusted Fuel Ratio Check (R_eff >= 1.50 net of 41 bps friction)
  │     └── Dynamic Order Persistence Governor (Calculates dynamic survival TTL: 2h - 6h)
  └── Step 5: Native MT5 IPC Staging & Management
        ├── Persistent GTC Limit Order Placement with Broker-Verified SL & TP
        └── Dynamic Ratchet (BE lock @ +0.80R, Profit lock @ +1.50R, Structural Exit @ +2.4R - +2.9R)
```

---

### 4. CURRENT LIVE MARKET EXPOSURE & ACTIVE RESTING LIMITS
As of October 6, 2026 13:00 UTC, the system has 0 open positions and 3 high-conviction resting limit orders staged on MetaTrader 5 Account 5064568:

1. **Ticket #18572624 — SOL Buy Limit @ 118.50 USD:**
   - Volume: 0.10 lots | SL: 117.95 USD | TP: 120.60 USD
   - Risk: 10.36 USD | Expected Reward: +16.14 USD (+1.56R)
   - Setup: Previous Day Low (PDL) Sweep Reclaim.
   - Anchor Defense: 8.68M USD whale bid floor resting at 118.41–118.45 USD.

2. **Ticket #18573320 — ETH Sell Limit @ 2,732.80 USD:**
   - Volume: 0.55 lots | SL: 2,741.50 USD | TP: 2,705.00 USD
   - Risk: 10.95 USD | Expected Reward: +9.13 USD (+1.48R)
   - Setup: Mean-Reversion Short against overhead resistance.
   - Anchor Defense: 25.52M USD whale ask corridor resting at 2,728.10–2,751.10 USD.

3. **Ticket #18576872 — GOLD (XAUUSD.pi) Sell Limit @ 4,176.00 USD:**
   - Volume: 0.01 lots (1.0 oz) | SL: 4,186.50 USD | TP: 4,143.00 USD
   - Risk: 11.10 USD | Expected Reward: +33.00 USD (+2.97R)
   - Setup: Extreme Session VWAP Deviation (+2.11 SD) & Session High Liquidity Rejection.
   - Anchor Defense: Session VWAP +2 SD Upper Band Envelope (4,176.09 USD).

---

### 5. THE FOUR HIGH-LEVEL ARCHITECTURAL & QUANTITATIVE QUESTIONS FOR ARENA.AI
We require your deep mathematical analysis, architectural critique, and concrete Python/C++ code recommendations for the following 4 pillars:

#### Question 1: Multi-Asset Limit Order Queue Governance & Microsecond Race Conditions
We decoupled resting limits (`staged_limits <= 5`) from filled positions (`positions < 2`). This allows simultaneous stalking across uncorrelated assets.
- **Microsecond Fill Collisions:** If market volatility spikes and 2 orders fill simultaneously across different assets, how should the daemon handle execution races if a 3rd order fills before the IPC cancel call completes?
- **Queue Priority & Hysteresis:** When an underlying whale wall shifts slightly (e.g. SOL whale moves from 118.41 to 118.45 USD), what is the optimal mathematical threshold for triggering a cancel-replace vs maintaining our existing broker queue priority?
- **Adverse Selection Protection:** What orderbook flow metrics (e.g. orderbook book-thinning velocity, cancellation intensity) should immediately abort a resting limit order *before* price reaches the level?

#### Question 2: Mathematical Fusion of Commodity Tick-Volume VWAP with Crypto L2/L3 Orderflow
On Binance/Hyperliquid crypto perps, we have full L2/L3 tick ladders and whale addresses. On MetaTrader 5 CFDs (Gold `XAUUSD.pi`, Silver `XAGUSD.pi`, SP500 `US500.cash`), we have no resting L3 depth, but we have ultra-high tick volume (7,000+ ticks per 15m candle) and sub-tick execution.
- How can we mathematically fuse **Session Volume Profile (Point of Control, Value Area High/Low)** and **Volume-Weighted Average Price Standard Deviation Bands** with microstructure price rejection (e.g. pin bar wick volume ratio, volume delta proxy) to optimize mean-reversion entries in Gold/Silver?
- Is standard deviation of VWAP sufficient, or should we employ an anchored Volume Variance or Median Absolute Deviation (MAD) band to prevent band ballooning during news volatility spikes?

#### Question 3: Asymmetric Exit Ratchets for Commodities vs Crypto
Crypto exhibits high volatility clustering, fat-tailed pullbacks, and sharp mean-reversions. Gold often exhibits directional session trends (London/NY breakout) with clean, persistent trending.
- Our current piecewise ratchet is uniform: BE @ +0.80R, Profit Lock @ +1.50R, Target @ +2.4R - +2.9R, 24-bar time decay.
- How should the ratchet be dynamically conditioned on asset class, Garman-Klass historical volatility, and session regime?
- Specifically, how should Gold stops trail—structural swing pivots vs VWAP rolling bands vs ATR ratchets?

#### Question 4: Offline Parquet Ingestion, Causal Synchronization & Gap Repair
Our `Candle_Indicator_Engine.py` dumps 15m OHLCV bars into monotonic Parquet files and asserts continuous 900-second step intervals.
- If the MT5 terminal temporarily disconnects or misses weekend gaps in commodities, how should the pipeline causally reconcile historical timestamps without leaking future bars into rolling indicators?
- What is the most efficient, zero-latency Polars/Numpy streaming architecture to maintain live VWAP and indicators in memory while ensuring 100% crash recovery from disk?

---

### 6. COMPLETE UNABRIDGED SOURCE CODE OF ACTIVE PRODUCTION MODULES
"""

MODULES_TO_INCLUDE = [
    ("Terminal/Candle_Indicator_Engine.py", "MODULE 1: CANDLE INDICATOR ENGINE (OHLCV, VWAP & GAP AUDITOR)"),
    ("Terminal/Order_Persistence_Governor.py", "MODULE 2: ORDER PERSISTENCE GOVERNOR (DYNAMIC GTC SURVIVAL & WALL DEFENSE)"),
    ("Terminal/Orderbook_Geometry.py", "MODULE 3: ORDERBOOK GEOMETRY & STRUCTURAL EXITS"),
    ("Terminal/MT5_Execution_Bridge.py", "MODULE 4: META TRADER 5 IPC EXECUTION BRIDGE"),
    ("Terminal/Omni_Trader.py", "MODULE 5: OMNI TRADER (AUTONOMOUS 15-MINUTE ORCHESTRATOR)"),
    ("Terminal/Risk_Sizing_Engine.py", "MODULE 6: RISK SIZING & QUANTITATIVE CONVICTION ENGINE"),
]

def build_prompt():
    out = [PROMPT_TEXT]
    for path, title in MODULES_TO_INCLUDE:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()
            out.append(f"\n\n{'='*80}\n### {title}\n### FILE: {path}\n{'='*80}\n```python\n{code}\n```\n")
        else:
            out.append(f"\n\n### MISSING FILE: {path}\n")

    full_prompt = "".join(out)
    
    # Write to Downloads
    dl_path = r"C:\Users\SIGMA\Downloads\Ox_Alpha_58_MultiAsset_Limit_Queue_Commodity_VWAP_Audit.txt"
    with open(dl_path, "w", encoding="utf-8") as f:
        f.write(full_prompt)
    print(f"Written prompt to {dl_path} ({len(full_prompt)} chars)")

    # Write to docs/prompts
    doc_path = os.path.join("docs", "prompts", "Ox_Alpha_58_MultiAsset_Limit_Queue_Commodity_VWAP_Audit.txt")
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)
    with open(doc_path, "w", encoding="utf-8") as f:
        f.write(full_prompt)
    print(f"Written prompt to {doc_path}")

if __name__ == "__main__":
    build_prompt()
