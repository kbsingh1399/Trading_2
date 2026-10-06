"""Canonical assets; signal-market names and broker symbols remain separate."""
# Core 14 institutional assets (backward compatible with baseline tests)
UNIVERSE = ("BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "TRX", "DOT", "LINK", "BCH",
            "SP500", "GOLD", "SILVER")

# Extended 24-asset multi-asset institutional universe:
# - 14 Crypto: BTC, ETH, SOL, BNB, XRP, ADA, DOGE, TRX, DOT, LINK, BCH, LTC, AVAX, NEAR
# - 4 Global Indices: SP500, NAS100, DJ30, GER40
# - 3 Commodities & Energy: GOLD, SILVER, USWTI (Crude Oil)
# - 3 Major Forex: EURUSD, GBPUSD, USDJPY
EXTENDED_UNIVERSE = UNIVERSE + (
    "LTC", "AVAX", "NEAR",
    "NAS100", "DJ30", "GER40",
    "USWTI",
    "EURUSD", "GBPUSD", "USDJPY"
)

ALIASES = {
    "XAUUSD": "GOLD", "XAGUSD": "SILVER",
    "USA100": "NAS100", "USTEC": "NAS100", "US100": "NAS100",
    "US500": "SP500", "SPX500": "SP500",
    "US30": "DJ30", "DJI": "DJ30",
    "GER40": "GER40", "GER30": "GER40", "DE40": "GER40", "DAX40": "GER40", "DAX": "GER40",
    "USWTI": "USWTI", "WTI": "USWTI", "OIL": "USWTI", "CRUDE": "USWTI",
    "AVXUSD": "AVAX", "NERUSD": "NEAR", "DOGUSD": "DOGE", "LNKUSD": "LINK"
}

BROKER_BASES = {
    "GOLD": ("XAUUSD", "GOLD"),
    "SILVER": ("XAGUSD", "SILVER"),
    "SP500": ("SP500", "US500", "SPX500"),
    "NAS100": ("NAS100", "USTEC", "US100"),
    "DJ30": ("DJ30", "US30", "DJI"),
    "GER40": ("GER40", "GER30", "DE40"),
    "USWTI": ("USWTI", "WTI", "OIL"),
    "AVAX": ("AVXUSD", "AVAXUSD", "AVAX"),
    "NEAR": ("NERUSD", "NEARUSD", "NEAR"),
    "DOGE": ("DOGUSD", "DOGEUSD", "DOGE"),
    "LINK": ("LNKUSD", "LINKUSD", "LINK"),
    "EURUSD": ("EURUSD",),
    "GBPUSD": ("GBPUSD",),
    "USDJPY": ("USDJPY",),
}

def canonical_asset(value):
    name = str(value).split(":")[-1].upper()
    name = name.split(".")[0]
    if name in ALIASES:
        return ALIASES[name]
    for suffix in ("USDT", "USD"):
        if name.endswith(suffix):
            base = name[:-len(suffix)]
            if base in UNIVERSE or base in EXTENDED_UNIVERSE:
                return base
    return ALIASES.get(name, name)

def broker_candidates(asset):
    asset = canonical_asset(asset)
    bases = BROKER_BASES.get(asset, (asset + "USD", asset + "USDT", asset))
    if asset == "DOGE" and "DOGUSD" not in bases: bases = ("DOGUSD",) + bases
    if asset == "LINK" and "LNKUSD" not in bases: bases = ("LNKUSD",) + bases
    return [base + suffix for base in bases for suffix in (".p", ".pi", "", ".a", "m")]

