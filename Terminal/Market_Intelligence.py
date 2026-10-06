#!/usr/bin/env python3
"""
Terminal/Market_Intelligence.py
===============================
Macro Economic Calendar & Web Market Intelligence Engine.
Monitors:
- Tier-1 High-Impact Economic Releases (CPI, PCE, FOMC, NFP, GDP)
- Event Blackout Window Controller (vetoes entries within +/- 15 mins of high-impact releases)
- Real-time RSS & Web News sentiment parser for breaking macro and crypto catalysts
- Normalized Macro Sentiment Score (-1.0 to +1.0)
"""

import sys
import time
import json
import urllib.request
import xml.etree.ElementTree as ET
import datetime
import logging
from pathlib import Path
from email.utils import parsedate_to_datetime
from Terminal.Asset_Universe import UNIVERSE
from Terminal.Risk_Sizing_Engine import epoch
from typing import Dict, List, Any, Tuple, Optional

logger = logging.getLogger("MarketIntel")
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("[%(asctime)s][MarketIntel] %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Known high-impact keywords triggering risk blackout or sentiment shifts
BEARISH_KEYWORDS = [
    "sec lawsuit", "insolvency", "hack", "exploit", "ban", "depeg", "fraud",
    "recession", "rate hike", "hawkish", "subpoena", "default", "liquidation spike",
    "outflow", "sanctions", "tariff", "bearish", "shed", "drop", "plunge", "dump",
    "slump", "crash", "fall", "loss"
]

BULLISH_KEYWORDS = [
    "etf approval", "rate cut", "dovish", "treasury reserve", "stimulus",
    "institutional inflow", "partnership", "adoption", "record high", "soft landing",
    "disinflation", "cooling cpi", "bullish", "inflow", "rally", "surge", "gain",
    "rebound", "breakout", "soar"
]


class MarketIntelligenceEngine:
    def __init__(self, blackout_minutes: int = 15, calendar_path=None, clock=time.time):
        self.blackout_minutes = blackout_minutes
        self.last_fetch_time = 0.0
        self.cached_sentiment = 0.0
        self.cached_headlines: List[Dict[str, Any]] = []
        self.cached_events: List[Dict[str, Any]] = []
        self.calendar_path = Path(calendar_path or Path(__file__).resolve().parents[1]/"Data/macro_calendar.json")
        self.clock = clock
        self.calendar_error = None
        self.last_calendar_attempt = 0.0

    def fetch_live_headlines(self) -> List[Dict[str, Any]]:
        """
        Fetches breaking financial and crypto RSS feeds.
        """
        now = self.clock()
        if self.cached_headlines and (now - self.last_fetch_time < 300.0):
            return self.cached_headlines

        feeds = [
            "https://feeds.content.dowjones.com/public/rss/mw_topstories",
            "https://cointelegraph.com/rss",
            "https://www.coindesk.com/arc/outboundfeeds/rss/"
        ]

        headlines = []
        for url in feeds:
            try:
                req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
                with urllib.request.urlopen(req, timeout=5) as resp:
                    xml_data = resp.read()
                    root = ET.fromstring(xml_data)
                    for item in root.findall(".//item")[:10]:
                        title = item.find("title")
                        pub_date = item.find("pubDate")
                        if title is not None and title.text:
                            headlines.append({
                                "title": title.text.strip(),
                                "date": pub_date.text.strip() if pub_date is not None and pub_date.text else "",
                                "source": url.split("//")[-1].split("/")[0]
                            })
            except Exception:
                continue

        if headlines:
            self.cached_headlines = headlines[:25]
            self.last_fetch_time = now
            self._compute_sentiment_score()

        return self.cached_headlines

    def _compute_sentiment_score(self):
        """
        Computes a bounded score [-1.0, +1.0] from cached headlines.
        """
        if not self.cached_headlines:
            self.cached_sentiment = 0.0
            return

        bull_count = 0
        bear_count = 0
        total_matched = 0

        for h in self.cached_headlines:
            text = h["title"].lower()
            for kw in BEARISH_KEYWORDS:
                if kw in text:
                    bear_count += 1
                    total_matched += 1
            for kw in BULLISH_KEYWORDS:
                if kw in text:
                    bull_count += 1
                    total_matched += 1

        if total_matched == 0:
            self.cached_sentiment = 0.0
        else:
            raw_score = (bull_count - bear_count) / max(total_matched, 1)
            # Bound and smooth
            self.cached_sentiment = round(max(-1.0, min(1.0, raw_score)), 2)

    def check_macro_blackout(self) -> Tuple[bool, str, float]:
        """
        Checks whether current time is within +/- blackout_minutes of high-impact releases.
        Returns: (is_blackout: bool, event_name: str, minutes_delta: float)
        """
        now = self.clock()
        try:
            calendar = json.loads(self.calendar_path.read_text(encoding="utf-8"))
            if calendar.get("required_series") != ["CPI", "NFP", "FOMC"]: raise ValueError("calendar coverage unverified")
            if not epoch(calendar.get("coverage_start")) <= now < epoch(calendar.get("coverage_end")):
                raise ValueError("calendar outside verified coverage")
            events = calendar.get("events")
            if not events or not isinstance(events, list) or len(events) == 0:
                raise ValueError("calendar events missing or empty")
            self.calendar_error = None
            for event in events:
                if event.get("impact") != "HIGH": continue
                event_time = epoch(event.get("time_utc"))
                if not event_time: raise ValueError("calendar event timestamp invalid")
                delta = abs(now-event_time)/60
                if delta <= self.blackout_minutes: return True, event["name"], delta
            return False, "NO_EVENT", 999.0
        except (OSError, ValueError, KeyError, TypeError) as exc:
            self.calendar_error = str(exc)
            return True, "CALENDAR_UNAVAILABLE", 0.0
    def get_market_intelligence_report(self) -> Dict[str, Any]:
        """
        Full 360-degree macro intelligence synthesis.
        """
        if self.clock()-self.last_calendar_attempt > 86400:
            self.last_calendar_attempt = self.clock()
            try:
                from Terminal.Macro_Calendar import refresh_calendar
                refresh_calendar(self.calendar_path)
            except Exception as exc:
                logger.warning("Dated macro calendar refresh failed: %s", exc)
        headlines = self.fetch_live_headlines()
        is_blackout, event_name, delta_min = self.check_macro_blackout()

        sentiment_label = "BULLISH" if self.cached_sentiment >= 0.25 else (
            "BEARISH" if self.cached_sentiment <= -0.25 else "NEUTRAL"
        )

        return {
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "macro_sentiment_score": self.cached_sentiment,
            "asset_scores": self.asset_sentiment_scores(),
            "sentiment_valid": bool(self.cached_headlines and self.clock()-self.last_fetch_time <= 900),
            "calendar_error": self.calendar_error,
            "macro_bias": sentiment_label,
            "blackout_active": is_blackout,
            "blackout_event": event_name,
            "minutes_to_window": delta_min,
            "headlines_count": len(headlines),
            "top_headlines": [h["title"] for h in headlines[:5]]
        }

    def asset_sentiment_scores(self):
        """Keyword sentiment is a weak feature; crypto headlines do not become gold signals."""
        names = {"BTC": ("bitcoin", "btc"), "ETH": ("ethereum", "eth"), "SOL": ("solana", "sol"),
                 "BNB": ("binance", "bnb"), "XRP": ("ripple", "xrp"), "ADA": ("cardano", "ada"),
                 "DOGE": ("dogecoin", "doge"), "TRX": ("tron", "trx"), "DOT": ("polkadot", "dot"),
                 "LINK": ("chainlink", "link"), "BCH": ("bitcoin cash", "bch"), "GOLD": ("gold",),
                 "SILVER": ("silver",), "SP500": ("s&p", "sp500"), "NAS100": ("nasdaq",), "DJ30": ("dow jones",)}
        scores = {}
        for asset in UNIVERSE:
            numerator = denominator = 0.0
            for h in self.cached_headlines:
                text = h["title"].lower()
                try: published = parsedate_to_datetime(h["date"]).timestamp()
                except (ValueError, TypeError, KeyError): continue
                age = self.clock()-published
                if not 0 <= age <= 86400: continue
                macro = any(k in text for k in ("fed", "fomc", "cpi", "payroll", "inflation", "rate cut", "rate hike"))
                relevant = macro or any(k in text for k in names[asset])
                if not relevant: continue
                bulls = sum(k in text for k in BULLISH_KEYWORDS)
                bears = sum(k in text for k in BEARISH_KEYWORDS)
                weight = 2**(-age/14400)
                numerator += weight*(bulls-bears); denominator += weight*(bulls+bears)
            scores[asset] = max(-1, min(1, numerator/denominator)) if denominator else 0.0
        return scores


if __name__ == "__main__":
    engine = MarketIntelligenceEngine()
    report = engine.get_market_intelligence_report()
    print(json.dumps(report, indent=2))
