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
    "outflow", "sanctions", "tariff"
]

BULLISH_KEYWORDS = [
    "etf approval", "rate cut", "dovish", "treasury reserve", "stimulus",
    "institutional inflow", "partnership", "adoption", "record high", "soft landing",
    "disinflation", "cooling cpi"
]


class MarketIntelligenceEngine:
    def __init__(self, blackout_minutes: int = 15):
        self.blackout_minutes = blackout_minutes
        self.last_fetch_time = 0.0
        self.cached_sentiment = 0.0
        self.cached_headlines: List[Dict[str, Any]] = []
        self.cached_events: List[Dict[str, Any]] = []
        self._load_static_economic_calendar()

    def _load_static_economic_calendar(self):
        """
        Pre-loads recurring institutional macro release benchmarks (UTC timestamps).
        """
        # Standard recurring release times: e.g. CPI 12:30 UTC / 13:30 UTC on second Wednesday/Thursday
        # Fed FOMC at 18:00 / 19:00 UTC, NFP first Friday 12:30 / 13:30 UTC
        self.recurring_schedules = [
            {"name": "US CPI Release", "time_utc": "12:30", "impact": "HIGH", "days": ["Wednesday", "Thursday"]},
            {"name": "FOMC Rate Decision", "time_utc": "18:00", "impact": "HIGH", "days": ["Wednesday"]},
            {"name": "US Non-Farm Payrolls (NFP)", "time_utc": "12:30", "impact": "HIGH", "days": ["Friday"]},
            {"name": "US Core PCE Price Index", "time_utc": "12:30", "impact": "HIGH", "days": ["Friday"]}
        ]

    def fetch_live_headlines(self) -> List[Dict[str, Any]]:
        """
        Fetches breaking financial and crypto RSS feeds.
        """
        now = time.time()
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
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        current_minute_of_day = now_utc.hour * 60 + now_utc.minute

        # Check major release times (12:30 UTC = 750 mins, 18:00 UTC = 1080 mins)
        target_windows = [
            (750, "US Tier-1 Macro (CPI / NFP / PCE)"),
            (1080, "FOMC Statement / Rate Decision"),
            (1110, "FOMC Press Conference")
        ]

        for target_min, name in target_windows:
            delta = abs(current_minute_of_day - target_min)
            if delta <= self.blackout_minutes:
                return True, name, delta

        return False, "NO_EVENT", 999.0

    def get_market_intelligence_report(self) -> Dict[str, Any]:
        """
        Full 360-degree macro intelligence synthesis.
        """
        headlines = self.fetch_live_headlines()
        is_blackout, event_name, delta_min = self.check_macro_blackout()

        sentiment_label = "BULLISH" if self.cached_sentiment >= 0.25 else (
            "BEARISH" if self.cached_sentiment <= -0.25 else "NEUTRAL"
        )

        return {
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "macro_sentiment_score": self.cached_sentiment,
            "macro_bias": sentiment_label,
            "blackout_active": is_blackout,
            "blackout_event": event_name,
            "minutes_to_window": delta_min,
            "headlines_count": len(headlines),
            "top_headlines": [h["title"] for h in headlines[:5]]
        }


if __name__ == "__main__":
    engine = MarketIntelligenceEngine()
    report = engine.get_market_intelligence_report()
    print(json.dumps(report, indent=2))
