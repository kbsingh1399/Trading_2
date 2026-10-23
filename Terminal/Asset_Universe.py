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

# Additional 19 Crypto Assets available on BOTH Binance USDT-M Futures & Hyperdash (Hyperliquid):
DUAL_VENUE_CRYPTO_19 = (
    "AAVE", "ALGO", "AR", "ATOM", "AXS", "COMP", "CRV", "DASH", "FIL",
    "HBAR", "IOTA", "NEO", "SAND", "SNX", "SUSHI", "UNI", "XLM", "XMR", "ZEC"
)

# All 16 Global Indices available on Blueberry MT5:
ALL_INDICES_16 = (
    "SP500", "NAS100", "DJ30", "GER40", "UK100", "FR40", "JP225", "AU200",
    "STOXX50", "US2000", "HK50", "CHINA50", "CHINAH", "NETH25", "SWISS20", "GER30"
)

# Commodities & Metals available on MT5:
ALL_COMMODITIES_14 = (
    "GOLD", "SILVER", "USWTI", "UKBRENT", "COPPER", "GAS",
    "ALUMINIUM", "LEAD", "NICKEL", "ZINC", "PLATINUM", "PALLADIUM",
    "GAUUSD", "GAUCNH"
)

# Major Forex Pairs (7):
ALL_FOREX_MAJORS_7 = (
    "EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", "NZDUSD"
)

# Liquid Forex Crosses & Liquid Pairs (25):
ALL_FOREX_CROSSES_25 = (
    "EURGBP", "EURJPY", "GBPJPY", "AUDJPY", "CADJPY", "CHFJPY",
    "EURAUD", "EURCAD", "EURCHF", "EURNZD",
    "GBPAUD", "GBPCAD", "GBPCHF", "GBPNZD",
    "AUDCAD", "AUDCHF", "AUDNZD", "CADCHF",
    "NZDCAD", "NZDCHF", "NZDJPY",
    "USDCNH", "USDHKD", "USDSGD", "AUDSGD"
)

# All 58 Crypto Assets on MT5:
ALL_58_CRYPTO_ASSETS = (
    "BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "TRX", "DOT", "LINK", "BCH",
    "LTC", "AVAX", "NEAR", "AAVE", "ALGO", "AR", "ATOM", "AXS", "COMP", "CRV",
    "DASH", "FIL", "HBAR", "IOTA", "NEO", "SAND", "SNX", "SUSHI", "UNI", "XLM",
    "XMR", "ZEC", "BAT", "CEL", "CHR", "CHZ", "EGLD", "ENJ", "FLOW", "GRT",
    "INCH", "KAVA", "KNC", "KSM", "LRC", "MANA", "ONT", "QTUM", "SKL", "STORJ",
    "SXP", "THETA", "VET", "XTZ", "YFI", "ZIL", "ZRX"
)

# Complete expanded institutional universe:
COMPLETE_UNIVERSE = tuple(sorted(list(set(
    EXTENDED_UNIVERSE + DUAL_VENUE_CRYPTO_19 + ALL_INDICES_16 +
    ALL_COMMODITIES_14 + ALL_FOREX_MAJORS_7 + ALL_FOREX_CROSSES_25 + ALL_58_CRYPTO_ASSETS
))))

ALL_33_CRYPTO_ASSETS = (
    "BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "TRX", "DOT", "LINK", "BCH",
    "LTC", "AVAX", "NEAR"
) + DUAL_VENUE_CRYPTO_19

ALIASES = {
    # Metals & Commodities
    "XAUUSD": "GOLD", "XAGUSD": "SILVER",
    "XPTUSD": "PLATINUM", "XPDUSD": "PALLADIUM",
    "USWTI": "USWTI", "WTI": "USWTI", "OIL": "USWTI", "CRUDE": "USWTI",
    "UKBRENT": "UKBRENT", "BRENT": "UKBRENT",
    "GAS": "GAS", "NATGAS": "GAS",
    "COPPER": "COPPER", "ALUMINIUM": "ALUMINIUM", "LEAD": "LEAD", "NICKEL": "NICKEL", "ZINC": "ZINC",
    "GAUUSD": "GAUUSD", "GAUCNH": "GAUCNH",

    # Indices
    "USA100": "NAS100", "USTEC": "NAS100", "US100": "NAS100", "NAS100": "NAS100",
    "US500": "SP500", "SPX500": "SP500", "SP500": "SP500",
    "US30": "DJ30", "DJI": "DJ30", "DJ30": "DJ30",
    "GER40": "GER40", "DE40": "GER40", "DAX40": "GER40", "DAX": "GER40", "GER30": "GER30",
    "UK100": "UK100", "FTSE100": "UK100", "FTSE": "UK100",
    "FR40": "FR40", "CAC40": "FR40", "CAC": "FR40",
    "JP225": "JP225", "NIKKEI225": "JP225", "N225": "JP225",
    "AU200": "AU200", "ASX200": "AU200",
    "STOXX50": "STOXX50", "EU50": "STOXX50",
    "US2000": "US2000", "RUT": "US2000", "RUSSELL2000": "US2000",
    "HK50": "HK50", "HSI": "HK50",
    "CHINA50": "CHINA50", "A50": "CHINA50",
    "CHINAH": "CHINAH", "HSCEI": "CHINAH",
    "NETH25": "NETH25", "AEX": "NETH25",
    "SWISS20": "SWISS20", "SMI": "SWISS20",

    # Cryptos
    "AVXUSD": "AVAX", "NERUSD": "NEAR", "DOGUSD": "DOGE", "LNKUSD": "LINK",
    "AVEUSD": "AAVE", "ALGUSD": "ALGO", "ARWUSD": "AR", "ATMUSD": "ATOM",
    "AXSUSD": "AXS", "COMUSD": "COMP", "CRVUSD": "CRV", "DSHUSD": "DASH",
    "FILUSD": "FIL", "BARUSD": "HBAR", "IOTUSD": "IOTA", "NEOUSD": "NEO",
    "SNDUSD": "SAND", "SNXUSD": "SNX", "XSIUSD": "SUSHI", "UNIUSD": "UNI",
    "XLMUSD": "XLM", "XMRUSD": "XMR", "ZECUSD": "ZEC",
    "BATUSD": "BAT", "CELUSD": "CEL", "CHRUSD": "CHR", "CHZUSD": "CHZ",
    "EGLUSD": "EGLD", "ENJUSD": "ENJ", "FLWUSD": "FLOW", "GRTUSD": "GRT",
    "INCUSD": "INCH", "KAVUSD": "KAVA", "KNCUSD": "KNC", "KSMUSD": "KSM",
    "LRCUSD": "LRC", "MANUSD": "MANA", "ONTUSD": "ONT", "QTMUSD": "QTUM",
    "SKLUSD": "SKL", "STOUSD": "STORJ", "SXPUSD": "SXP", "THTUSD": "THETA",
    "VETUSD": "VET", "XTZUSD": "XTZ", "YFIUSD": "YFI", "ZILUSD": "ZIL", "ZRXUSD": "ZRX"
}

BROKER_BASES = {
    # Commodities & Metals
    "GOLD": ("XAUUSD", "GOLD"),
    "SILVER": ("XAGUSD", "SILVER"),
    "PLATINUM": ("XPTUSD", "PLATINUM"),
    "PALLADIUM": ("XPDUSD", "PALLADIUM"),
    "USWTI": ("USWTI", "WTI", "OIL"),
    "UKBRENT": ("UKBRENT", "BRENT"),
    "COPPER": ("COPPER",),
    "GAS": ("GAS",),
    "ALUMINIUM": ("ALUMINIUM",),
    "LEAD": ("LEAD",),
    "NICKEL": ("NICKEL",),
    "ZINC": ("ZINC",),
    "GAUUSD": ("GAUUSD",),
    "GAUCNH": ("GAUCNH",),

    # Indices
    "SP500": ("SP500", "US500", "SPX500"),
    "NAS100": ("NAS100", "USTEC", "US100"),
    "DJ30": ("DJ30", "US30", "DJI"),
    "GER40": ("GER40", "DE40", "DAX40"),
    "GER30": ("GER30",),
    "UK100": ("UK100",),
    "FR40": ("FR40",),
    "JP225": ("JP225",),
    "AU200": ("AU200",),
    "STOXX50": ("STOXX50",),
    "US2000": ("US2000",),
    "HK50": ("HK50",),
    "CHINA50": ("CHINA50",),
    "CHINAH": ("CHINAH",),
    "NETH25": ("NETH25",),
    "SWISS20": ("SWISS20",),

    # Forex Majors
    "EURUSD": ("EURUSD",),
    "GBPUSD": ("GBPUSD",),
    "USDJPY": ("USDJPY",),
    "AUDUSD": ("AUDUSD",),
    "USDCAD": ("USDCAD",),
    "USDCHF": ("USDCHF",),
    "NZDUSD": ("NZDUSD",),

    # Forex Crosses
    "EURGBP": ("EURGBP",), "EURJPY": ("EURJPY",), "GBPJPY": ("GBPJPY",),
    "AUDJPY": ("AUDJPY",), "CADJPY": ("CADJPY",), "CHFJPY": ("CHFJPY",),
    "EURAUD": ("EURAUD",), "EURCAD": ("EURCAD",), "EURCHF": ("EURCHF",), "EURNZD": ("EURNZD",),
    "GBPAUD": ("GBPAUD",), "GBPCAD": ("GBPCAD",), "GBPCHF": ("GBPCHF",), "GBPNZD": ("GBPNZD",),
    "AUDCAD": ("AUDCAD",), "AUDCHF": ("AUDCHF",), "AUDNZD": ("AUDNZD",), "CADCHF": ("CADCHF",),
    "NZDCAD": ("NZDCAD",), "NZDCHF": ("NZDCHF",), "NZDJPY": ("NZDJPY",),
    "USDCNH": ("USDCNH",), "USDHKD": ("USDHKD",), "USDSGD": ("USDSGD",), "AUDSGD": ("AUDSGD",),

    # Cryptos
    "BTC": ("BTCUSD", "BTC"),
    "ETH": ("ETHUSD", "ETH"),
    "SOL": ("SOLUSD", "SOL"),
    "BNB": ("BNBUSD", "BNB"),
    "XRP": ("XRPUSD", "XRP"),
    "ADA": ("ADAUSD", "ADA"),
    "DOGE": ("DOGUSD", "DOGEUSD", "DOGE"),
    "TRX": ("TRXUSD", "TRX"),
    "DOT": ("DOTUSD", "DOT"),
    "LINK": ("LNKUSD", "LINKUSD", "LINK"),
    "BCH": ("BCHUSD", "BCH"),
    "LTC": ("LTCUSD", "LTC"),
    "AVAX": ("AVXUSD", "AVAXUSD", "AVAX"),
    "NEAR": ("NERUSD", "NEARUSD", "NEAR"),
    "AAVE": ("AVEUSD", "AAVEUSD", "AAVE"),
    "ALGO": ("ALGUSD", "ALGOUSD", "ALGO"),
    "AR": ("ARWUSD", "ARUSD", "AR"),
    "ATOM": ("ATMUSD", "ATOMUSD", "ATOM"),
    "AXS": ("AXSUSD", "AXS"),
    "COMP": ("COMUSD", "COMPUSD", "COMP"),
    "CRV": ("CRVUSD", "CRV"),
    "DASH": ("DSHUSD", "DASHUSD", "DASH"),
    "FIL": ("FILUSD", "FIL"),
    "HBAR": ("BARUSD", "HBARUSD", "HBAR"),
    "IOTA": ("IOTUSD", "IOTAUSD", "IOTA", "MIOTA"),
    "NEO": ("NEOUSD", "NEO"),
    "SAND": ("SNDUSD", "SANDUSD", "SAND"),
    "SNX": ("SNXUSD", "SNX"),
    "SUSHI": ("XSIUSD", "SUSHIUSD", "SUSHI"),
    "UNI": ("UNIUSD", "UNI"),
    "XLM": ("XLMUSD", "XLM"),
    "XMR": ("XMRUSD", "XMR"),
    "ZEC": ("ZECUSD", "ZEC"),
    "BAT": ("BATUSD", "BAT"),
    "CEL": ("CELUSD", "CEL"),
    "CHR": ("CHRUSD", "CHR"),
    "CHZ": ("CHZUSD", "CHZ"),
    "EGLD": ("EGLUSD", "EGLD"),
    "ENJ": ("ENJUSD", "ENJ"),
    "FLOW": ("FLWUSD", "FLOW"),
    "GRT": ("GRTUSD", "GRT"),
    "INCH": ("INCUSD", "INCH", "1INCH"),
    "KAVA": ("KAVUSD", "KAVA"),
    "KNC": ("KNCUSD", "KNC"),
    "KSM": ("KSMUSD", "KSM"),
    "LRC": ("LRCUSD", "LRC"),
    "MANA": ("MANUSD", "MANA"),
    "ONT": ("ONTUSD", "ONT"),
    "QTUM": ("QTMUSD", "QTUM"),
    "SKL": ("SKLUSD", "SKL"),
    "STORJ": ("STOUSD", "STORJ"),
    "SXP": ("SXPUSD", "SXP"),
    "THETA": ("THTUSD", "THETA"),
    "VET": ("VETUSD", "VET"),
    "XTZ": ("XTZUSD", "XTZ"),
    "YFI": ("YFIUSD", "YFI"),
    "ZIL": ("ZILUSD", "ZIL"),
    "ZRX": ("ZRXUSD", "ZRX"),
}

def canonical_asset(value: str) -> str:
    name = str(value).split(":")[-1].upper()
    name = name.split(".")[0]
    if name in ALIASES:
        return ALIASES[name]
    for suffix in ("USDT", "USD"):
        if name.endswith(suffix):
            base = name[:-len(suffix)]
            if base in COMPLETE_UNIVERSE:
                return base
    return ALIASES.get(name, name)

def broker_candidates(asset: str) -> list[str]:
    asset = canonical_asset(asset)
    bases = BROKER_BASES.get(asset, (asset + "USD", asset + "USDT", asset))
    if asset == "DOGE" and "DOGUSD" not in bases: bases = ("DOGUSD",) + bases
    if asset == "LINK" and "LNKUSD" not in bases: bases = ("LNKUSD",) + bases
    return [base + suffix for base in bases for suffix in (".p", ".pi", "", ".a", "m")]
