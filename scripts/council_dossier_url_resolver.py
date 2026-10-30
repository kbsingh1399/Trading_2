#!/usr/bin/env python3
"""
scripts/council_dossier_url_resolver.py
======================================
Resolves broker symbols and canonical tickers to their exact master dossier JSON
filenames and official Raw GitHub URLs.

Guarantees 100% precision:
- Base crypto tickers (BTC, ETH, SOL, BNB, etc.) map to BTC_MASTER_DOSSIER.json
- Full altcoin pairs (AVEUSD, XMRUSD, etc.) map to AVEUSD_MASTER_DOSSIER.json
- Forex and commodities map to their exact master files.
- Generates fully grounded Raw GitHub URLs hosted on kbsingh1399/Trading_2/main.
"""

from __future__ import annotations
import pathlib
import sys
from typing import Dict, List, Optional, Tuple

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOSSIERS_DIR = ROOT / "docs" / "dossiers"
REPO_RAW_BASE = "https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/dossiers"


def resolve_symbol_to_dossier(symbol: str) -> Optional[Tuple[str, str, int]]:
    """
    Returns (filename, raw_github_url, file_size_bytes) for a given broker symbol.
    """
    clean = symbol.replace(".pi", "").replace(".p", "").replace("/", "").upper()
    
    candidates = [
        f"{clean}_MASTER_DOSSIER.json",
        f"{clean}USD_MASTER_DOSSIER.json",
    ]
    if clean.endswith("USD"):
        base = clean[:-3]
        candidates.extend([f"{base}_MASTER_DOSSIER.json", f"{base}USD_MASTER_DOSSIER.json"])
    
    for cand in candidates:
        target = DOSSIERS_DIR / cand
        if target.exists() and target.stat().st_size > 50:
            url = f"{REPO_RAW_BASE}/{cand}"
            return cand, url, target.stat().st_size

    return None


def get_all_eligible_dossier_records(symbols: List[str]) -> List[Dict[str, any]]:
    """
    Resolves each symbol to its dossier file, size, and raw GitHub URL.
    """
    records = []
    for s in symbols:
        res = resolve_symbol_to_dossier(s)
        if res:
            fname, url, size = res
            
            # Determine category
            category = "FX / TradFi"
            clean = s.replace(".pi", "").replace(".p", "").upper()
            if any(c in clean for c in ["BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "AVAX", "DOGE"]):
                category = "Core Institutional Crypto"
            elif any(c in clean for c in ["XMR", "AVE", "ZEC", "DSH", "YFI", "XLM", "BCH", "UNI", "LINK"]):
                category = "Altcoin Derivatives"
            elif any(c in clean for c in ["XAU", "XAG", "COPPER", "ALUMINIUM", "ZINC", "USWTI", "UKBRENT", "GAU"]):
                category = "Metals & Commodities"
            elif any(c in clean for c in ["SP500", "NAS100", "DJ30", "GER40", "US2000", "AU200", "JP225", "UK100", "FR40", "HK50", "CHINA50"]):
                category = "Global Equity Indices"
            
            records.append({
                "symbol": s,
                "filename": fname,
                "url": url,
                "size_bytes": size,
                "category": category,
            })
    return records


def format_dossier_urls_prompt_section(records: List[Dict[str, any]]) -> str:
    """
    Formats the exact raw GitHub URLs into structured Markdown grouped by category,
    with explicit directives for Arena.ai and Z.ai to fetch and deep-analyze each asset.
    """
    cats: Dict[str, List[Dict[str, any]]] = {}
    for r in records:
        cats.setdefault(r["category"], []).append(r)

    lines = [
        f"### 🌐 PHYSICAL DOSSIER REPOSITORY REGISTRY ({len(records)} Eligible Assets)",
        "Every eligible asset below has passed broker spread clearance. You are provided with the **EXACT Raw GitHub URL** for each asset's sovereign JSON Master Dossier.",
        "",
        "> ⚠️ **MANDATORY COUNCIL DIRECTIVE (Seat #2 & Seat #3)**:",
        "> **PRIMARY INTENT & MISSION: ACTIVELY DISCOVER & FORMULATE NEW HIGH-CONFLUENCE TRADING OPPORTUNITIES**.",
        "> The desk's explicit objective is to find new, prime high-confluence trades across this universe. We are NOT in a passive or frozen stance.",
        "> You MUST fetch each candidate's raw JSON file directly (via HTTP/curl or web access) and conduct an exhaustive deep forensic examination across all 15 quantitative pillars to formulate and justify new high-confluence trade opportunities:",
        "> 1. **ETF Spot & Future Netflows** (Institutional inflow/outflow trajectory)",
        "> 2. **Spot & Futures Capital Netflows** (24h/MTF net spot vs derivatives volume delta)",
        "> 3. **Multi-Exchange Long/Short Ratios** (Binance, OKX, Bybit positioning across MTF)",
        "> 4. **12-Venue Funding Rates & Settlement** (Crowded trade skew and basis yield)",
        "> 5. **Multi-Venue Open Interest Dynamics** (OI build vs liquidation cascade indicators)",
        "> 6. **Liquidation Bands & Max Pain Pools** (Multi-horizon Short Pain & Long Pain magnets)",
        "> 7. **Institutional Whale Armor** (L2/L3 block orders > $100K defending key price nodes)",
        "> 8. **Technical Profile & Multi-Timeframe VWAP** (Session VWAP, 20 EMA, RSI momentum)",
        "> 9. **Hyperdash Intel & Stop Loss Clusters** (Exact retail liquidation liquidity maps)",
        "> 10. **L2 Orderbook Depth & Bid/Ask Liquidity** (Top-of-book depth & limit order walls)",
        "> 11. **Multi-Timeframe CVD** (5m, 15m, 1h, 4h Cumulative Volume Delta divergences)",
        "> 12. **Auction Market Value Areas & POC** (VAH, VAL, and Point of Control distribution)",
        "> 13. **Tradfye Institutional Orderflow** (Hyperliquid tape & institutional prints)",
        "> 14. **CoinGlass Footprint Signals & Tape Metrics** (Aggressive market taker absorption)",
        "> 15. **MT5 Live Broker Specifications** (Contract size, min lot, digits, spread bps)",
        "",
        "#### Exact Raw GitHub URLs by Asset Class:"
    ]

    for cat_name, items in cats.items():
        lines.append(f"\n**{cat_name} ({len(items)} assets):**")
        for it in items:
            lines.append(f"- `{it['symbol']}` ({it['filename']}): {it['url']}")

    return "\n".join(lines)


if __name__ == "__main__":
    eligible_file = ROOT / "scripts" / "cycle_036_eligible_dossiers.txt"
    if eligible_file.exists():
        raw_symbols = [s.strip() for s in eligible_file.read_text(encoding="utf-8").splitlines() if s.strip() and s.strip() != "NONE_ACTIVE"]
        recs = get_all_eligible_dossier_records(raw_symbols)
        print(f"Loaded {len(recs)} valid records.")
        print(format_dossier_urls_prompt_section(recs[:10]))
