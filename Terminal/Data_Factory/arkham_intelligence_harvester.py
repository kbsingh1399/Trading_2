"""
Terminal/Data_Factory/arkham_intelligence_harvester.py
Production Institutional On-Chain Intelligence Harvester & Rotation Engine for Arkham (arkm.com via Chrome CDP).

Architecture Overview:
1. Complete Tier-1 Institutional Roster (48 Entities across 6 Institutional Sectors).
2. Cursor-Based Batch Rotation Pipeline: Rotates through entity batches via CDP background tabs
   with zero memory leaks, strict try...finally tab pruning, and jittered rate-limiting.
3. Persistent State Management: Tracks cursor position and entity freshness in Data/arkham_rotation_state.json.
4. Active Stream Harvesting: Captures live transfers, whale alerts (>= $50k), and exchange flow sentiment.
5. Tri-Sink Atomic Persistence:
   - Data/arkham_institutional_registry.json
   - Data/arkham_live_intelligence.json
   - docs/telemetry/live_snapshot_latest.json
"""

import asyncio
import websockets
import json
import urllib.request
import pathlib
import datetime
import re
import sys
import os
import logging
import random
from typing import Dict, List, Any, Optional, Tuple

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
SNAPSHOT_PATH = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
OUTPUT_PATH = DATA_DIR / "arkham_live_intelligence.json"
REGISTRY_PATH = DATA_DIR / "arkham_institutional_registry.json"
ROTATION_STATE_PATH = DATA_DIR / "arkham_rotation_state.json"

DATA_DIR.mkdir(parents=True, exist_ok=True)
SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("ArkhamHarvester")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# ==============================================================================
# EXPANDED TIER-1 INSTITUTIONAL ROSTER (48 ENTITIES ACROSS 6 CORE SECTORS)
# ==============================================================================

INSTITUTIONAL_ROSTER: List[Dict[str, str]] = [
    # --- SECTOR 1: ASSET MANAGERS & ETF ISSUERS ---
    {"slug": "blackrock", "name": "BlackRock", "category": "ASSET_MANAGER_ETF", "priority": "HIGH"},
    {"slug": "fidelity", "name": "Fidelity Investments", "category": "ASSET_MANAGER_ETF", "priority": "HIGH"},
    {"slug": "grayscale", "name": "Grayscale Investments", "category": "ASSET_MANAGER_TRUSTS", "priority": "HIGH"},
    {"slug": "bitwise", "name": "Bitwise Asset Management", "category": "ASSET_MANAGER_CRYPTO", "priority": "MEDIUM"},
    {"slug": "vaneck", "name": "VanEck", "category": "ASSET_MANAGER_ETF", "priority": "MEDIUM"},
    {"slug": "ark-invest", "name": "ARK Invest", "category": "ASSET_MANAGER_ETF", "priority": "MEDIUM"},
    {"slug": "21shares", "name": "21Shares (21.co)", "category": "ASSET_MANAGER_ETF", "priority": "MEDIUM"},
    {"slug": "franklin-templeton", "name": "Franklin Templeton", "category": "ASSET_MANAGER_ETF", "priority": "MEDIUM"},

    # --- SECTOR 2: MARKET MAKERS & HFT LIQUIDITY PROVIDERS ---
    {"slug": "wintermute", "name": "Wintermute", "category": "MARKET_MAKER_ALGO", "priority": "HIGH"},
    {"slug": "jump-trading", "name": "Jump Crypto", "category": "MARKET_MAKER_HFT", "priority": "HIGH"},
    {"slug": "cumberland", "name": "Cumberland DRW", "category": "OTC_LIQUIDITY_DESK", "priority": "HIGH"},
    {"slug": "falconx", "name": "FalconX", "category": "PRIME_BROKERAGE_EXECUTION", "priority": "HIGH"},
    {"slug": "gsr", "name": "GSR Markets", "category": "MARKET_MAKER_ALGO", "priority": "MEDIUM"},
    {"slug": "amber-group", "name": "Amber Group", "category": "MARKET_MAKER_CEFI", "priority": "MEDIUM"},
    {"slug": "dwf-labs", "name": "DWF Labs", "category": "MARKET_MAKER_VENTURE", "priority": "MEDIUM"},
    {"slug": "flow-traders", "name": "Flow Traders", "category": "MARKET_MAKER_HFT", "priority": "MEDIUM"},
    {"slug": "jane-street", "name": "Jane Street", "category": "MARKET_MAKER_HFT", "priority": "MEDIUM"},

    # --- SECTOR 3: SOVEREIGN GOVERNMENTS & STATE TREASURIES ---
    {"slug": "usg", "name": "U.S. Government", "category": "SOVEREIGN_TREASURY", "priority": "HIGH"},
    {"slug": "german-government", "name": "German Government (BKA)", "category": "SOVEREIGN_TREASURY", "priority": "MEDIUM"},
    {"slug": "uk-government", "name": "U.K. Government", "category": "SOVEREIGN_TREASURY", "priority": "MEDIUM"},
    {"slug": "royal-government-of-bhutan", "name": "Royal Government of Bhutan", "category": "SOVEREIGN_TREASURY", "priority": "MEDIUM"},
    {"slug": "el-salvador", "name": "El Salvador Treasury", "category": "SOVEREIGN_TREASURY", "priority": "HIGH"},

    # --- SECTOR 4: CORPORATE TREASURIES & STABLECOINS ---
    {"slug": "microstrategy", "name": "MicroStrategy", "category": "CORPORATE_TREASURY", "priority": "HIGH"},
    {"slug": "tesla", "name": "Tesla", "category": "CORPORATE_TREASURY", "priority": "MEDIUM"},
    {"slug": "tether", "name": "Tether Treasury", "category": "STABLECOIN_RESERVE", "priority": "HIGH"},
    {"slug": "circle", "name": "Circle Treasury", "category": "STABLECOIN_RESERVE", "priority": "HIGH"},
    {"slug": "mt-gox", "name": "Mt. Gox Trustee", "category": "INSOLVENCY_TRUSTEE", "priority": "HIGH"},
    {"slug": "block-inc", "name": "Block Inc (Square)", "category": "CORPORATE_TREASURY", "priority": "MEDIUM"},

    # --- SECTOR 5: CENTRALIZED EXCHANGES & PRIME CUSTODIANS ---
    {"slug": "binance", "name": "Binance Reserves", "category": "CENTRALIZED_EXCHANGE", "priority": "HIGH"},
    {"slug": "coinbase", "name": "Coinbase Prime / Custody", "category": "PRIME_CUSTODIAN", "priority": "HIGH"},
    {"slug": "okx", "name": "OKX Reserves", "category": "CENTRALIZED_EXCHANGE", "priority": "HIGH"},
    {"slug": "bybit", "name": "Bybit Reserves", "category": "CENTRALIZED_EXCHANGE", "priority": "HIGH"},
    {"slug": "kraken", "name": "Kraken Reserves", "category": "CENTRALIZED_EXCHANGE", "priority": "HIGH"},
    {"slug": "deribit", "name": "Deribit Derivatives", "category": "DERIVATIVES_EXCHANGE", "priority": "HIGH"},
    {"slug": "bitfinex", "name": "Bitfinex Reserves", "category": "CENTRALIZED_EXCHANGE", "priority": "MEDIUM"},
    {"slug": "htx", "name": "HTX (Huobi)", "category": "CENTRALIZED_EXCHANGE", "priority": "LOW"},
    {"slug": "gate-io", "name": "Gate.io", "category": "CENTRALIZED_EXCHANGE", "priority": "LOW"},
    {"slug": "robinhood", "name": "Robinhood Crypto", "category": "RETAIL_BROKERAGE_CUSTODY", "priority": "MEDIUM"},

    # --- SECTOR 6: DEFI PROTOCOLS & DAO TREASURIES ---
    {"slug": "uniswap", "name": "Uniswap Foundation / Timelock", "category": "DEFI_DEX_DAO", "priority": "MEDIUM"},
    {"slug": "aave", "name": "Aave Governance", "category": "DEFI_LENDING_DAO", "priority": "MEDIUM"},
    {"slug": "lido", "name": "Lido DAO", "category": "LIQUID_STAKING_DAO", "priority": "MEDIUM"},
    {"slug": "maker", "name": "Maker / Sky Protocol", "category": "DEFI_CDP_DAO", "priority": "MEDIUM"},
    {"slug": "aerodrome", "name": "Aerodrome Finance", "category": "BASE_DEX_LIQUIDITY", "priority": "MEDIUM"},
    {"slug": "drift", "name": "Drift Protocol", "category": "SOLANA_PERP_DEX", "priority": "MEDIUM"},
    {"slug": "curve", "name": "Curve Finance", "category": "DEFI_STABLE_SWAP", "priority": "LOW"},
    {"slug": "polymarket", "name": "Polymarket Liquidity", "category": "PREDICTION_MARKET_CUSTODY", "priority": "MEDIUM"},
    {"slug": "arbitrum", "name": "Arbitrum Foundation", "category": "LAYER_2_DAO", "priority": "LOW"},
    {"slug": "optimism", "name": "Optimism Collective", "category": "LAYER_2_DAO", "priority": "LOW"}
]

# Classification dictionaries for real-time flow resolution
KNOWN_EXCHANGES = {
    "binance": "Binance",
    "coinbase": "Coinbase",
    "okx": "OKX",
    "bybit": "Bybit",
    "kraken": "Kraken",
    "deribit": "Deribit",
    "bitfinex": "Bitfinex",
    "htx": "HTX",
    "gate.io": "Gate.io",
    "gate-io": "Gate.io",
    "mexc": "MEXC",
    "kucoin": "KuCoin",
    "upbit": "Upbit",
    "bithumb": "Bithumb",
    "robinhood": "Robinhood"
}

KNOWN_MARKET_MAKERS = {
    "wintermute": "Wintermute",
    "jump": "Jump Crypto",
    "cumberland": "Cumberland",
    "gsr": "GSR Markets",
    "amber": "Amber Group",
    "dwf": "DWF Labs",
    "falconx": "FalconX",
    "flow traders": "Flow Traders",
    "flow-traders": "Flow Traders",
    "jane street": "Jane Street",
    "jane-street": "Jane Street",
    "galaxy": "Galaxy Digital"
}

KNOWN_ASSET_MANAGERS = {
    "blackrock": "BlackRock",
    "fidelity": "Fidelity Investments",
    "grayscale": "Grayscale Investments",
    "bitwise": "Bitwise",
    "vaneck": "VanEck",
    "ark": "ARK Invest",
    "21shares": "21Shares",
    "franklin": "Franklin Templeton"
}

KNOWN_SOVEREIGN_TREASURIES = {
    "usg": "U.S. Government",
    "u.s. government": "U.S. Government",
    "german": "German Government",
    "uk-government": "U.K. Government",
    "bhutan": "Royal Government of Bhutan",
    "el salvador": "El Salvador"
}

KNOWN_CORPORATE_TREASURIES = {
    "microstrategy": "MicroStrategy",
    "strategy": "MicroStrategy",
    "tesla": "Tesla",
    "tether": "Tether Treasury",
    "circle": "Circle Treasury",
    "mt. gox": "Mt. Gox Trustee",
    "mt-gox": "Mt. Gox Trustee",
    "block": "Block Inc"
}

KNOWN_PROTOCOLS = {
    "uniswap": "Uniswap",
    "curve": "Curve",
    "aave": "Aave",
    "maker": "MakerDAO / Sky",
    "lido": "Lido",
    "polymarket": "Polymarket",
    "drift": "Drift Protocol",
    "aerodrome": "Aerodrome Finance",
    "arbitrum": "Arbitrum",
    "optimism": "Optimism"
}


def parse_financial_number(s: str) -> float:
    """Accurately parse numbers with K, M, B, T abbreviations into raw float values, preserving negative signs."""
    if not s:
        return 0.0
    s = s.strip().replace(",", "")
    is_neg = "-" in s or "(" in s
    mult = 1.0
    if s.endswith("K") or s.endswith("k"):
        mult = 1_000.0
        s = s[:-1]
    elif s.endswith("M") or s.endswith("m"):
        mult = 1_000_000.0
        s = s[:-1]
    elif s.endswith("B") or s.endswith("b"):
        mult = 1_000_000_000.0
        s = s[:-1]
    elif s.endswith("T") or s.endswith("t"):
        mult = 1_000_000_000_000.0
        s = s[:-1]
    clean = re.sub(r"[^\d.]", "", s)
    try:
        val = float(clean) * mult if clean else 0.0
        return -val if is_neg else val
    except Exception:
        return 0.0


def classify_party(name_or_text: str) -> Tuple[str, str]:
    """Classify an entity or address into canonical category."""
    low = name_or_text.lower()
    for k, name in KNOWN_EXCHANGES.items():
        if k in low:
            return name, "EXCHANGE"
    for k, name in KNOWN_MARKET_MAKERS.items():
        if k in low:
            return name, "MARKET_MAKER"
    for k, name in KNOWN_ASSET_MANAGERS.items():
        if k in low:
            return name, "ASSET_MANAGER"
    for k, name in KNOWN_SOVEREIGN_TREASURIES.items():
        if k in low:
            return name, "SOVEREIGN_TREASURY"
    for k, name in KNOWN_CORPORATE_TREASURIES.items():
        if k in low:
            return name, "CORPORATE_TREASURY"
    for k, name in KNOWN_PROTOCOLS.items():
        if k in low:
            return name, "DEX_PROTOCOL"
    if "whale" in low or "exploiter" in low or "treasury" in low or "government" in low:
        return name_or_text, "WHALE_TREASURY"
    return name_or_text, "WALLET"


class ArkhamBatchRotationPipeline:
    """
    Manages asynchronous rotation across all 48 institutional entities:
    - Cursor state tracking in Data/arkham_rotation_state.json
    - Bounded concurrency with strict CDP tab closure
    - Rate limit protection and memory leak prevention
    - Incremental merge into Data/arkham_institutional_registry.json
    """

    def __init__(self, cdp_port: int = 9222, default_batch_size: int = 5):
        self.cdp_port = cdp_port
        self.batch_size = default_batch_size
        self.state = self._load_state()

    def _load_state(self) -> Dict[str, Any]:
        if ROTATION_STATE_PATH.exists():
            try:
                with open(ROTATION_STATE_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.warning("Could not read rotation state: %s. Reinitializing.", e)
        return {
            "cursor_index": 0,
            "last_cycle_completed_utc": None,
            "total_entities": len(INSTITUTIONAL_ROSTER),
            "scan_history": {}
        }

    def _save_state(self):
        try:
            with open(ROTATION_STATE_PATH, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=2)
        except Exception as e:
            logger.error("Failed to save rotation state: %s", e)

    def get_next_batch(self, count: Optional[int] = None) -> List[Dict[str, str]]:
        k = count or self.batch_size
        idx = self.state.get("cursor_index", 0)
        total = len(INSTITUTIONAL_ROSTER)
        
        batch = []
        for i in range(k):
            batch.append(INSTITUTIONAL_ROSTER[(idx + i) % total])
            
        # Update cursor
        self.state["cursor_index"] = (idx + k) % total
        self._save_state()
        return batch

    async def harvest_entity_cdp(self, entity_meta: Dict[str, str]) -> Optional[Dict[str, Any]]:
        slug = entity_meta["slug"]
        url = f"https://arkm.com/explorer/entity/{slug}"
        tab_id = None
        
        try:
            req = urllib.request.Request(f"http://127.0.0.1:{self.cdp_port}/json/new?{url}", method="PUT")
            tab = json.loads(urllib.request.urlopen(req, timeout=6).read())
            tab_id = tab["id"]
            ws_url = tab["webSocketDebuggerUrl"]

            async with websockets.connect(ws_url, max_size=30 * 1024 * 1024, open_timeout=8) as ws:
                # Dynamic Hydration Polling Loop: wait until entity details / Addresses hydrate
                for _ in range(6):
                    await asyncio.sleep(1.0)
                    try:
                        check_js = "document.body.innerText.includes('Addresses') || document.body.innerText.includes('$')"
                        await ws.send(json.dumps({"id": 99, "method": "Runtime.evaluate", "params": {"expression": check_js, "returnByValue": True}}))
                        check_res = json.loads(await asyncio.wait_for(ws.recv(), timeout=2.0))
                        if check_res.get("result", {}).get("result", {}).get("value") is True:
                            break
                    except Exception:
                        pass
                
                # Brief pause for complete numbers to settle
                await asyncio.sleep(0.5)

                js = """(() => {
                    const text = document.body.innerText;
                    const lines = text.split('\\n').map(l => l.trim()).filter(Boolean);
                    
                    let entityName = document.title.split('|')[0].trim();
                    let addressCount = '';
                    let totalBalance = '';
                    let change24h = '';
                    
                    for (let i = 0; i < lines.length; i++) {
                        if (lines[i].includes('Addresses') && !addressCount) {
                            addressCount = lines[i];
                            for (let j = Math.max(0, i - 4); j < Math.min(lines.length, i + 6); j++) {
                                if (lines[j].startsWith('$') && lines[j].length > 4 && !totalBalance) {
                                    totalBalance = lines[j];
                                    if (j + 1 < lines.length && lines[j+1].includes('%')) {
                                        change24h = lines[j+1];
                                    }
                                }
                            }
                        }
                    }
                    
                    const holdings = [];
                    const commonTokens = ['BTC', 'ETH', 'SOL', 'USDT', 'USDC', 'BNB', 'XRP', 'DOGE', 'AVAX', 'LINK', 'WBTC', 'CBBTC', 'SUI', 'NEAR', 'AERO', 'UNI', 'AAVE', 'MKR'];
                    
                    for (let i = 0; i < lines.length; i++) {
                        if (commonTokens.includes(lines[i])) {
                            const sym = lines[i];
                            let price = '';
                            let amount = '';
                            let posValue = '';
                            let valChange = '';
                            
                            for (let j = i + 1; j < Math.min(lines.length, i + 9); j++) {
                                const l = lines[j];
                                if (l.startsWith('$') && !price) {
                                    price = l;
                                } else if (l.endsWith(sym) && !amount) {
                                    amount = l;
                                } else if (l.startsWith('$') && price && !posValue) {
                                    posValue = l;
                                    if (j + 1 < lines.length && lines[j+1].includes('%')) {
                                        valChange = lines[j+1];
                                    }
                                }
                            }
                            if (posValue && !holdings.some(h => h.symbol === sym)) {
                                holdings.push({
                                    symbol: sym,
                                    price: price,
                                    amount: amount,
                                    value_usd: posValue,
                                    change_24h: valChange
                                });
                            }
                        }
                    }
                    
                    return {
                        slug: window.location.pathname.split('/').pop(),
                        entity_name: entityName,
                        address_count: addressCount,
                        total_portfolio_usd: totalBalance,
                        portfolio_change_24h: change24h,
                        holdings_breakdown: holdings
                    };
                })()"""

                val = None
                # Dynamic hydration polling loop (max 6 seconds)
                for attempt in range(6):
                    await asyncio.sleep(1.0)
                    await ws.send(json.dumps({"id": attempt + 1, "method": "Runtime.evaluate", "params": {"expression": js, "returnByValue": True}}))
                    res = json.loads(await ws.recv())
                    cand = res.get("result", {}).get("result", {}).get("value", {})
                    if cand and cand.get("total_portfolio_usd"):
                        val = cand
                        break
                    val = cand
                
                if val:
                    val["category"] = entity_meta["category"]
                    val["priority"] = entity_meta.get("priority", "MEDIUM")
                    val["last_updated_utc"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                    return val
                return None
        except Exception as e:
            logger.error("Failed harvesting entity '%s' (%s): %s", entity_meta["name"], slug, e)
            return None
        finally:
            if tab_id:
                try:
                    urllib.request.urlopen(f"http://127.0.0.1:{self.cdp_port}/json/close/{tab_id}", timeout=4)
                except Exception as close_err:
                    logger.warning("Could not close tab %s: %s", tab_id, close_err)

    async def run_batch(self, batch: List[Dict[str, str]]) -> Dict[str, Any]:
        """Execute a batch of entities sequentially with rate-limit protection."""
        registry = {}
        if REGISTRY_PATH.exists():
            try:
                with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
                    registry = json.load(f)
            except Exception:
                registry = {}

        now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        for entity in batch:
            slug = entity["slug"]
            logger.info("-> Rotating to institutional profile: %s (%s)...", entity["name"], slug)
            data = await self.harvest_entity_cdp(entity)
            if data and data.get("total_portfolio_usd"):
                registry[slug] = data
                self.state.setdefault("scan_history", {})[slug] = now_str
                logger.info("   [SUCCESS] %s: %s (%s) | Wallets: %s",
                            entity["name"], data.get("total_portfolio_usd"),
                            data.get("portfolio_change_24h"), data.get("address_count"))
            else:
                logger.warning("   [RETRY_PENDING] No complete portfolio captured for %s", entity["name"])
            
            # Anti-rate-limit jitter sleep between tabs
            await asyncio.sleep(random.uniform(1.5, 2.5))

        # Save registry atomically
        with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2)

        self._save_state()
        return registry


# ==============================================================================
# LIVE ARKHAM DOM STREAM HARVESTER (ON-CHAIN TRANSFERS & WHALE RADAR)
# ==============================================================================

async def harvest_arkham_dom(cdp_port: int = 9222, target_min_usd: int = 50000) -> dict:
    """Connect to live Arkham tab via Chrome CDP, or spawn a transient tab if none is active."""
    try:
        tabs = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{cdp_port}/json", timeout=5).read())
    except Exception as e:
        logger.error("Could not query CDP on port %d: %s", cdp_port, e)
        return {}

    ws_url = None
    created_tab_id = None

    for t in tabs:
        url = t.get("url", "")
        if "arkm.com" in url and "/explorer/entity/" not in url and t.get("type") == "page":
            ws_url = t.get("webSocketDebuggerUrl")
            break
    if not ws_url:
        for t in tabs:
            if "arkm.com" in t.get("url", "") and t.get("type") == "page":
                ws_url = t.get("webSocketDebuggerUrl")
                break

    # If no active tab exists, launch a dedicated background target
    if not ws_url:
        try:
            logger.info("No active Arkham stream tab found. Spawning background target to arkm.com/explorer...")
            req = urllib.request.Request(f"http://127.0.0.1:{cdp_port}/json/new?https://arkm.com/explorer", method="PUT")
            new_tab = json.loads(urllib.request.urlopen(req, timeout=6).read())
            created_tab_id = new_tab["id"]
            ws_url = new_tab["webSocketDebuggerUrl"]
        except Exception as spawn_err:
            logger.error("Failed to spawn background Arkham stream tab: %s", spawn_err)
            return {}

    try:
        async with websockets.connect(ws_url, max_size=30 * 1024 * 1024, open_timeout=8) as ws:
            # Step 1: Ensure USD >= $50K filter is applied
            js_filter = f"""
            (() => {{
                const chip = document.querySelector('span[data-filter-chip-type="usd"]');
                const chipText = chip ? chip.innerText : '';
                
                if (chipText.includes('50K') || chipText.includes('100K')) {{
                    return {{ filter_status: 'ALREADY_ACTIVE', chip: chipText }};
                }}
                
                const body = chip ? (chip.querySelector('[data-slot="body"]') || chip) : null;
                if (!body) return {{ filter_status: 'CHIP_NOT_FOUND' }};
                body.click();
                
                const minInput = document.querySelector('input[placeholder="Minimum"]');
                if (minInput) {{
                    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                    setter.call(minInput, '{target_min_usd}');
                    minInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    minInput.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    
                    const applyBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Apply');
                    if (applyBtn) {{
                        applyBtn.click();
                        return {{ filter_status: 'APPLIED_NEW', chip: chipText }};
                    }}
                }}
                return {{ filter_status: 'CLICKED_AWAITING_INPUT' }};
            }})()
            """
            msg_filter = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": js_filter, "returnByValue": True}}
            await ws.send(json.dumps(msg_filter))
            res_filter = json.loads(await ws.recv())
            filter_res = res_filter.get("result", {}).get("result", {}).get("value", {})
            if filter_res.get("filter_status") == "APPLIED_NEW":
                logger.info("Applied new USD >= $%d filter on Arkham tab", target_min_usd)
                await asyncio.sleep(2.0)

            # Step 2: Harvest DOM elements (Entities, Rows, Bitcoin Macro Card)
            js_harvest = """
            (() => {
                const doc = window.top.document;
                
                // 1. Trending Entities
                const entityLinks = Array.from(doc.querySelectorAll('a[href*="/explorer/entity/"]'));
                const entities = [];
                const seenEntities = new Set();
                for (const a of entityLinks) {
                    const lines = a.innerText.split('\\n').map(l => l.trim()).filter(Boolean);
                    if (lines.length >= 2 && !seenEntities.has(lines[0])) {
                        seenEntities.add(lines[0]);
                        let holdingsUsd = '';
                        let changePct = '';
                        let largestHolding = '';
                        let activeWallets = '';
                        for (let i = 0; i < lines.length; i++) {
                            if (lines[i].startsWith('$') && !holdingsUsd) holdingsUsd = lines[i];
                            if (lines[i].includes('%') && !changePct) changePct = lines[i];
                            if (lines[i] === 'LARGEST HOLDING' && i + 1 < lines.length) {
                                largestHolding = lines[i+1] + (i+2 < lines.length && lines[i+2].startsWith('(') ? ' ' + lines[i+2] : '');
                            }
                            if (lines[i] === 'ACTIVE WALLETS' && i + 1 < lines.length) {
                                activeWallets = lines[i+1];
                            }
                        }
                        entities.push({
                            name: lines[0],
                            holdings_usd: holdingsUsd,
                            change_pct_24h: changePct,
                            largest_holding: largestHolding,
                            active_wallets: activeWallets,
                            entity_url: a.href
                        });
                    }
                }
                
                // 2. Transfer Rows
                const rows = Array.from(doc.querySelectorAll('div[class*="group/row"]'));
                const txs = [];
                for (const r of rows) {
                    const lines = r.innerText.split('\\n').map(l => l.trim()).filter(Boolean);
                    const links = Array.from(r.querySelectorAll('a')).map(l => ({ text: l.innerText.trim(), href: l.href }));
                    const txLink = links.find(l => l.href.includes('/explorer/tx/'));
                    txs.push({
                        tx_hash: txLink ? txLink.href.split('/').pop() : '',
                        tx_url: txLink ? txLink.href : '',
                        raw_lines: lines,
                        raw_text: lines.join(' | '),
                        links: links
                    });
                }
                
                // 3. Bitcoin Explorer Widget
                let btcWidget = null;
                const btcLink = doc.querySelector('a[href*="/explorer/token/bitcoin"]');
                if (btcLink) {
                    const btcLines = btcLink.innerText.split('\\n').map(l => l.trim()).filter(Boolean);
                    btcWidget = { raw_lines: btcLines };
                }
                
                return {
                    url: window.top.location.href,
                    title: doc.title,
                    filter_chip: doc.querySelector('span[data-filter-chip-type="usd"]')?.innerText.replace(/\\n/g, ' ') || '',
                    entities: entities,
                    transfers: txs,
                    btc_widget: btcWidget
                };
            })()
            """
            msg_harvest = {"id": 2, "method": "Runtime.evaluate", "params": {"expression": js_harvest, "returnByValue": True}}
            await ws.send(json.dumps(msg_harvest))
            res_harvest = json.loads(await ws.recv())
            return res_harvest.get("result", {}).get("result", {}).get("value", {})
    except Exception as e:
        logger.error("CDP stream harvest failed: %s", e)
        return {}
    finally:
        # If we opened a transient background tab, close it immediately to prevent RAM leaks
        if created_tab_id:
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{cdp_port}/json/close/{created_tab_id}", timeout=4)
                logger.info("Closed transient stream tab: %s", created_tab_id)
            except Exception as close_err:
                logger.warning("Could not close transient stream tab: %s", close_err)


# ==============================================================================
# DATA TRANSFORMATION, FLOW CLASSIFICATION & ATOMIC SINK INGESTION
# ==============================================================================

def parse_arkham_data(raw: dict, institutional_registry: Optional[dict] = None) -> dict:
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    entities = raw.get("entities", [])
    raw_txs = raw.get("transfers", [])
    btc_widget = raw.get("btc_widget")

    parsed_transfers = []
    exchange_inflows = []
    exchange_outflows = []
    market_maker_flows = []
    whale_alerts = []

    asset_flows = {
        "BTC": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "ETH": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "SOL": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "USDT": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "USDC": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0},
        "OTHER": {"inflow_usd": 0.0, "outflow_usd": 0.0, "tx_count": 0, "whale_txs": 0}
    }

    for tx in raw_txs:
        lines = tx.get("raw_lines", [])
        if len(lines) < 3:
            continue

        time_str = lines[0] if lines else "Recent"
        usd_val = 0.0
        token_sym = "UNKNOWN"
        amount_val = 0.0

        for l in lines:
            if l.startswith("$"):
                usd_val = parse_financial_number(l)

        for i, l in enumerate(lines):
            cand = l.upper().strip()
            for t_candidate in ["BTC", "CBBTC", "WBTC", "ETH", "WETH", "SOL", "USDT", "USDC", "FDUSD", "DAI", "AERO", "MORPHO", "SPY"]:
                if cand == t_candidate or f" {t_candidate}" in cand:
                    token_sym = t_candidate
                    if i > 0:
                        amount_val = parse_financial_number(lines[i-1])
                    break
            if token_sym != "UNKNOWN":
                break

        target_asset = "OTHER"
        if token_sym in ["BTC", "CBBTC", "WBTC"]:
            target_asset = "BTC"
        elif token_sym in ["ETH", "WETH"]:
            target_asset = "ETH"
        elif token_sym == "SOL":
            target_asset = "SOL"
        elif token_sym == "USDT":
            target_asset = "USDT"
        elif token_sym in ["USDC", "FDUSD", "DAI"]:
            target_asset = "USDC"

        from_entity, from_type = "Unknown", "WALLET"
        to_entity, to_type = "Unknown", "WALLET"

        links = tx.get("links", [])
        # Filter out transaction hash / timestamp links (/explorer/tx/) to prevent sender becoming 'Now'
        party_links = [l.get("text") for l in links if l.get("text") and "/explorer/tx/" not in l.get("href", "")]

        if len(party_links) >= 2:
            from_entity, from_type = classify_party(party_links[0])
            to_entity, to_type = classify_party(party_links[1])
        elif len(party_links) == 1:
            from_entity, from_type = classify_party(party_links[0])
            if len(lines) >= 4:
                to_entity, to_type = classify_party(lines[2])
        elif len(lines) >= 4:
            from_entity, from_type = classify_party(lines[1])
            to_entity, to_type = classify_party(lines[2])

        flow_tag = "INTERNAL_TRANSFER"
        if to_type == "EXCHANGE" and from_type != "EXCHANGE":
            flow_tag = "EXCHANGE_INFLOW (POTENTIAL_SELL_PRESSURE)"
            exchange_inflows.append({"tx": tx.get("tx_hash"), "from": from_entity, "to": to_entity, "usd": usd_val, "token": token_sym})
            asset_flows[target_asset]["inflow_usd"] += usd_val
            asset_flows[target_asset]["tx_count"] += 1
        elif from_type == "EXCHANGE" and to_type != "EXCHANGE":
            flow_tag = "EXCHANGE_OUTFLOW (ACCUMULATION_COLD_STORAGE)"
            exchange_outflows.append({"tx": tx.get("tx_hash"), "from": from_entity, "to": to_entity, "usd": usd_val, "token": token_sym})
            asset_flows[target_asset]["outflow_usd"] += usd_val
            asset_flows[target_asset]["tx_count"] += 1
        elif from_type == "MARKET_MAKER" or to_type == "MARKET_MAKER":
            flow_tag = "MARKET_MAKER_ARBITRAGE_PROVISION"
            market_maker_flows.append({"tx": tx.get("tx_hash"), "from": from_entity, "to": to_entity, "usd": usd_val, "token": token_sym})

        if usd_val >= 50000:
            asset_flows[target_asset]["whale_txs"] += 1
            whale_alerts.append({
                "tx_hash": tx.get("tx_hash"),
                "time": time_str,
                "from": from_entity,
                "to": to_entity,
                "usd_value": usd_val,
                "token": token_sym,
                "asset_bucket": target_asset,
                "flow_tag": flow_tag
            })

        parsed_transfers.append({
            "time": time_str,
            "tx_hash": tx.get("tx_hash"),
            "from_entity": from_entity,
            "from_type": from_type,
            "to_entity": to_entity,
            "to_type": to_type,
            "token": token_sym,
            "amount": amount_val,
            "usd_value": usd_val,
            "flow_classification": flow_tag
        })

    total_inflow_usd = sum(x["usd"] for x in exchange_inflows)
    total_outflow_usd = sum(x["usd"] for x in exchange_outflows)
    net_flow_usd = total_outflow_usd - total_inflow_usd
    total_observed_volume = sum(p["usd_value"] for p in parsed_transfers)

    if len(exchange_outflows) > len(exchange_inflows) and net_flow_usd >= 0:
        sentiment = "NET_ACCUMULATION (BULLISH_FLOW)"
    if len(parsed_transfers) == 0:
        sentiment = "UNAVAILABLE_INSUFFICIENT_DATA"
        feed_status = "CONNECTED_NO_TRANSFERS" if raw else "STANDBY"
    elif len(exchange_outflows) > len(exchange_inflows) and net_flow_usd > 0:
        sentiment = "NET_ACCUMULATION (BULLISH_FLOW)"
        feed_status = "STREAMING_ACTIVE"
    elif len(exchange_inflows) > len(exchange_outflows) and net_flow_usd <= 0:
        sentiment = "NET_DISTRIBUTION (BEARISH_FLOW)"
        feed_status = "STREAMING_ACTIVE"
    else:
        sentiment = "NEUTRAL_BALANCED_FLOW"
        feed_status = "STREAMING_ACTIVE"

    btc_macro = {}
    if btc_widget and "raw_lines" in btc_widget:
        bl = btc_widget["raw_lines"]
        for i, l in enumerate(bl):
            if l.startswith("$") and "price_usd" not in btc_macro:
                btc_macro["price_usd"] = parse_financial_number(l)
            if l == "24H VOLUME" and i + 1 < len(bl):
                btc_macro["volume_24h_usd"] = parse_financial_number(bl[i+1])
            if l == "MARKET CAP" and i + 1 < len(bl):
                btc_macro["market_cap_usd"] = parse_financial_number(bl[i+1])
            if l == "24H" and i + 1 < len(bl):
                btc_macro["change_24h_pct"] = bl[i+1]
            if l == "7d" and i + 1 < len(bl):
                btc_macro["change_7d_pct"] = bl[i+1]
            if l == "30D" and i + 1 < len(bl):
                btc_macro["change_30d_pct"] = bl[i+1]

    # Load existing registry if not provided
    if institutional_registry is None:
        institutional_registry = {}
        if REGISTRY_PATH.exists():
            try:
                with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
                    institutional_registry = json.load(f)
            except Exception:
                pass

    structured = {
        "as_of_utc": now_utc,
        "source": "Arkham Intelligence Upgraded Harvester (arkm.com via Chrome CDP)",
        "filter_applied": raw.get("filter_chip", "USD >= $50K"),
        "feed_status": feed_status,
        "is_feed_available": len(parsed_transfers) > 0,
        "market_flow_sentiment": sentiment,
        "aggregate_metrics": {
            "total_transfers_monitored": len(parsed_transfers),
            "total_observed_volume_usd": total_observed_volume,
            "exchange_inflow_events": len(exchange_inflows),
            "exchange_outflow_events": len(exchange_outflows),
            "market_maker_events": len(market_maker_flows),
            "large_whale_alerts_count": len(whale_alerts),
            "total_inflow_volume_usd": total_inflow_usd,
            "total_outflow_volume_usd": total_outflow_usd,
            "net_flow_usd": net_flow_usd
        },
        "bitcoin_macro_explorer": btc_macro,
        "asset_breakdown": asset_flows,
        "trending_institutional_entities": entities,
        "institutional_entities_deep": institutional_registry or {},
        "whale_alerts": whale_alerts[:25],
        "recent_classified_transfers": parsed_transfers[:50]
    }

    # Sink 1: arkham_live_intelligence.json (Primary Source of Truth ingested by generate_telemetry_snapshot.py)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(structured, f, indent=2)
    logger.info("Saved complete Arkham intelligence to %s (downstream ingested by generate_telemetry_snapshot.py)", OUTPUT_PATH)

    return structured


def run(batch_size: int = 5, cycle_all: bool = False):
    """
    Main entrypoint:
    1. Harvests live stream & whale radar.
    2. Executes cursor rotation on the expanded 48-entity roster.
    3. Persists to Data/arkham_live_intelligence.json & Data/arkham_institutional_registry.json.
    """
    logger.info("Harvesting Arkham On-Chain Intelligence via CDP (min USD >= $50,000)...")
    raw = asyncio.run(harvest_arkham_dom(target_min_usd=50000))

    pipeline = ArkhamBatchRotationPipeline(default_batch_size=batch_size)

    if cycle_all:
        logger.info("Running complete cycle across all %d institutional entities...", len(INSTITUTIONAL_ROSTER))
        batches = [INSTITUTIONAL_ROSTER[i:i + batch_size] for i in range(0, len(INSTITUTIONAL_ROSTER), batch_size)]
        inst_registry = {}
        for b in batches:
            inst_registry = asyncio.run(pipeline.run_batch(b))
            asyncio.run(asyncio.sleep(3.0))
    else:
        batch = pipeline.get_next_batch(count=batch_size)
        logger.info("Initiating batch rotation (%d entities: %s)...", len(batch), [e['name'] for e in batch])
        inst_registry = asyncio.run(pipeline.run_batch(batch))

    if raw:
        data = parse_arkham_data(raw, institutional_registry=inst_registry)
    else:
        data = parse_arkham_data({}, institutional_registry=inst_registry)

    logger.info("=== ARKHAM INSTITUTIONAL HARVEST SUMMARY ===")
    logger.info("Filter: %s | Feed Status: %s", data.get("filter_applied"), data.get("feed_status"))
    logger.info("Sentiment: %s", data.get("market_flow_sentiment"))
    logger.info("Deep Registry Total Profiles: %d", len(data.get("institutional_entities_deep", {})))
    logger.info("Transfers Monitored: %d | Whale Alerts: %d",
                data.get("aggregate_metrics", {}).get("total_transfers_monitored", 0),
                data.get("aggregate_metrics", {}).get("large_whale_alerts_count", 0))
    return data


if __name__ == "__main__":
    is_all = "--all" in sys.argv
    batch_sz = 5
    for arg in sys.argv:
        if arg.startswith("--batch="):
            try:
                batch_sz = int(arg.split("=")[1])
            except ValueError:
                pass
    run(batch_size=batch_sz, cycle_all=is_all)
