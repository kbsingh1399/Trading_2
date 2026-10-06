import datetime

prompt_text = """You are GPT Astra, an elite institutional quantitative architect and AI systems engineer.

We are operating a live, autonomous 15-minute candle trading system on MetaTrader 5 (CFDs). 
CRITICAL CONTEXT: Unlike traditional rigid rule-based models or pure ML (XGBoost) pipelines, we are pushing the frontier by letting LLM models make real-time trading decisions based on a 360-degree data feed.

=== SYSTEM ARCHITECTURE ===
1. Data Provenance & Universe: 18 Institutional Binance USDT-M Perpetuals (3.47M 15m bars, 2020-2026).
2. Live Inputs (wakes every 14th minute of the 15m candle):
   - Hyperdash Orderflow: Real-time liquidations, L2 book imbalance, L3 whale resting limit orders.
   - Macro Intelligence: Real-time RSS sentiment, CPI/FOMC +/- 15m blackout gates.
   - MT5 Microstructure: Live spread, bid/ask, margin levels, and tick constraints.
3. Execution & Risk (Fixed 5,000.00 USD Capital):
   - Strict Frictions: 41 bps round-trip friction penalty enforced on all backtests and live execution.
   - Asymmetrical Risk: 10.00 to 20.00 USD base risk, scaling up to 50.00 USD "House Money" risk on equity high-water marks.
   - Dynamic Stops: ATR-based R-distance (1.5 * ATR).
   - Regime-Aware Trailing: 3-stage ratchet. If a strong trend is detected (Kaufman Efficiency Ratio > 0.60), fixed take-profits are removed in favor of aggressive trailing stops.
   - Correlation Throttle: Strictly vetoes taking multiple directional positions on correlated assets (e.g., no double-shorts).
4. Scorecard History: Passed 20/20 out-of-sample walk-forward windows (2021-2026) in backtesting. Current live system is rated 8/10 for institutional causal soundness.

=== THE ASK ===
Since our core alpha relies on real-time LLM cognitive reasoning evaluating this matrix of data (orderflow + macro + price action) rather than static rules, how can we improve the cognitive architecture to maximize profitability?

Please provide concrete architectural blueprints for:
1. Multi-Agent Debate in the Execution Window: (e.g., separating the LLM into a 'Conviction Analyst', 'Risk Manager', and 'Macro Economist' that debate the setup in the 30-second window before the candle closes).
2. Agentic Memory & Reflection: How should the LLM store and retrieve its past decision rationale vs. actual trade outcomes to dynamically self-correct its weightings of orderflow signals?
3. LLM State Representation: What is the optimal prompt structure/JSON schema to feed complex L3 orderbook walls and liquidation cascades into an LLM so it "understands" microstructure pressure without hallucinating?

Attached is the full unabridged source code of our master production modules. Analyze them and provide your blueprint.

=== SOURCE CODE ===
"""

with open("docs/prompts/GPT_Astra_Consultation_1.txt", "w", encoding="utf-8") as out:
    out.write(prompt_text)
    out.write("\n\n--- Terminal/OF_Strategy.py ---\n\n")
    with open("Terminal/OF_Strategy.py", "r", encoding="utf-8") as f:
        out.write(f.read())
    out.write("\n\n--- Terminal/MT5_Execution_Bridge.py ---\n\n")
    with open("Terminal/MT5_Execution_Bridge.py", "r", encoding="utf-8") as f:
        out.write(f.read())
    out.write("\n\n--- Terminal/Quantitative_Governance.py ---\n\n")
    with open("Terminal/Quantitative_Governance.py", "r", encoding="utf-8") as f:
        out.write(f.read())

print("Prompt successfully built at docs/prompts/GPT_Astra_Consultation_1.txt")
