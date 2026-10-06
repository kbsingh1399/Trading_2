"""Canonical assets; signal-market names and broker symbols remain separate."""
UNIVERSE = ("BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "TRX", "DOT", "LINK", "BCH",
            "SP500", "GOLD", "SILVER")
ALIASES = {"XAUUSD": "GOLD", "XAGUSD": "SILVER", "USA100": "NAS100", "USTEC": "NAS100",
           "US100": "NAS100", "US500": "SP500", "SPX500": "SP500", "US30": "DJ30", "DJI": "DJ30"}
BROKER_BASES = {"GOLD": ("XAUUSD", "GOLD"), "SILVER": ("XAGUSD", "SILVER"),
                "SP500": ("SP500", "US500", "SPX500"), "NAS100": ("NAS100", "USTEC", "US100"),
                "DJ30": ("DJ30", "US30", "DJI")}

def canonical_asset(value):
    name = str(value).split(":")[-1].upper()
    name = name.split(".")[0]
    if name in ALIASES:
        return ALIASES[name]
    for suffix in ("USDT", "USD"):
        if name.endswith(suffix) and name[:-len(suffix)] in UNIVERSE:
            return name[:-len(suffix)]
    return {"DOGUSD": "DOGE", "LNKUSD": "LINK"}.get(name, name)

def broker_candidates(asset):
    asset = canonical_asset(asset)
    bases = BROKER_BASES.get(asset, (asset + "USD", asset + "USDT", asset))
    if asset == "DOGE": bases = ("DOGUSD",) + bases
    if asset == "LINK": bases = ("LNKUSD",) + bases
    return [base + suffix for base in bases for suffix in (".p", ".pi", "", ".a", "m")]
