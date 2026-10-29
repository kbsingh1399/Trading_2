# scripts/build_sovereign_dossier_engine_v32.py
"""
Builds the production Sovereign Dossier Engine v3.2:
- True MT5 Contract Specs & Point Values per asset class (FX 100k, Indices 10, Gold 100, etc.)
- Price-Sanity Filter eliminating cross-asset alias collision (SP500 vs SPX6900 meme coin)
- Multi-alias union in DataLakeMemoryStore (merging BTCUSD, BTCUSDT, BTC)
- Complete Sequenced Markdown Execution Ladder Tables for:
  * Section 4: Multi-Timeframe CVD Table (5m, 15m, 1h, 4h, ALL) with FX/Indices fallback
  * Section 5: Defending Institutional Whale Armor Ladder Table (Bids & Asks >= $50K, >= 180s)
  * Section 5: L2 Orderbook Depth Ladder Table (Top 5 Bids & Top 5 Asks)
  * Section 6: Liquidation Cluster Ladder Table (Monotonic price sequence)
  * Section 6: Retail Stop-Loss Cascade Map Table (Buy Stops above mid, Sell Stops below mid)
  * Section 7: 12-Venue Funding Rates & Open Interest Table
  * Section 8: Sequenced Microstructure Footprint Bars Table (last 8 bars)
  * Section 8: Multi-Horizon Capital Netflows Table (12 horizons)
- Universal Section 10 Algorithmic Trade Formulation for ALL 162 Assets:
  * Dynamic Long & Short Candidate Boxes with Spread-Padded SL, +2.5R TP, exact Lot Size
  * 6-Pillar Confluence Scorecard (0/6 to 6/6) and Execution Posture
"""
import sys
from pathlib import Path

OUT_FILE = Path("scripts/sovereign_dossier_engine.py")

print("Generating scripts/sovereign_dossier_engine.py v3.2...")
