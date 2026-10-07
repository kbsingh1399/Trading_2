"""Macro, ETF flows & sentiment tracking (Pillar 5) - all free endpoints.

  * Spot ETF daily flows - Farside Investors tables (free HTML) parsed into
    per-fund and total net flows; SEC EDGAR full-text query builder as the
    archival cross-check. Fetchers are injectable; parsers are pure.
  * Coinbase Premium Index - (P_coinbase - P_binance) / P_binance in bps,
    computed live from the two venue mids already on the IntelligenceBus.
  * Crypto Fear & Greed - api.alternative.me/fng/ (free, no key).
  * Macro blackout - delegate to ``Market_Intelligence``'s verified calendar
    (fail-closed) rather than duplicating it; a standalone helper covers
    ad-hoc calendars with the same +/- 15-minute rule.
"""
from __future__ import annotations
import json
import re
import time
import urllib.request
from datetime import datetime, timezone
from Terminal.Risk_Sizing_Engine import number, epoch

FARSIDE_BTC_URL = "https://farside.co.uk/btc/"
FARSIDE_ETH_URL = "https://farside.co.uk/eth/"
FNG_URL = "https://api.alternative.me/fng/"
EDGAR_FULL_TEXT = "https://efts.sec.gov/LATEST/search-index?q="
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


def default_fetch(url, timeout=10.0):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


# ------------------------------------------------------------------ Farside
def _farside_number(cell: str):
    """Farside cell -> float. '(40.0)' is negative; '-' means not reported."""
    s = cell.replace(",", "").replace("(", "-").replace(")", "").strip()
    if s in ("-", "", "N/A"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def parse_farside_table(html):
    """Farside Investors flow table -> [{date, funds{...}, total_musd, date_epoch}].

    Restored per-fund contract (forensics round 2): the docstring always
    promised per-fund flows, but the parser only emitted the total - the
    committed test ``funds["GBTC"]`` proved the regression. Fund names come
    from the header row; '-' cells (not yet reported) map to None.
    """
    text = html.decode() if isinstance(html, bytes) else str(html)
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", text, flags=re.S | re.I)
    fund_names: list = []
    out = []
    for row in rows:
        cells = [re.sub(r"<[^>]+>", "", c).strip().replace("\xa0", "")
                 for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, flags=re.S | re.I)]
        if not cells:
            continue
        first = cells[0].strip().lower()
        if first == "date" and len(cells) >= 3:
            # Header row: Date | FUND... | Total
            fund_names = [c.strip() for c in cells[1:-1]]
            continue
        if not re.match(r"^\d{1,2}\s+\w{3}\s+\d{4}$", cells[0]):
            continue
        tot = _farside_number(cells[-1])
        if tot is None:
            continue
        try:
            dt = datetime.strptime(cells[0], "%d %b %Y").replace(tzinfo=timezone.utc)
            date_epoch = dt.timestamp()
        except Exception:
            continue
        funds = {}
        if fund_names:
            for name, cell in zip(fund_names, cells[1:-1]):
                value = _farside_number(cell)
                if value is not None:
                    funds[name] = value
        out.append({
            "date": cells[0],
            "date_epoch": date_epoch,
            "total_musd": tot,
            "funds": funds,
            "raw_cells": cells
        })
    out.sort(key=lambda r: r["date_epoch"])
    return out


class FarsideETFFlows:
    """Daily spot-ETF net flows (millions USD) for BTC and ETH."""

    def __init__(self, fetch=None, clock=time.time):
        self.fetch = fetch or default_fetch
        self.clock = clock
        self.cache = {"BTC": None, "ETH": None}

    def refresh(self, asset="BTC"):
        url = FARSIDE_ETH_URL if asset == "ETH" else FARSIDE_BTC_URL
        rows = list(parse_farside_table(self.fetch(url)))
        if rows:
            self.cache[asset] = rows
        return rows

    def net_flow(self, asset="BTC", lookback_days=1):
        rows = self.cache.get(asset)
        if not rows:
            return None
        now = self.clock()
        recent = [r for r in rows if 0.0 <= now - r["date_epoch"] < lookback_days * 86400]
        return {"asset": asset, "days": lookback_days,
                "total_musd": sum(r["total_musd"] for r in recent),
                "last_date": rows[-1]["date"], "rows": len(rows)}

    def streak(self, asset="BTC", n=5):
        """Last n daily totals, newest first (for consecutive-flow signals)."""
        rows = self.cache.get(asset) or []
        return [r["total_musd"] for r in rows[-n:]][::-1]


def edgar_full_text_url(query, date_from, date_to):
    """SEC EDGAR full-text search URL builder (8-K cross-check of flows)."""
    return (f"https://efts.sec.gov/LATEST/search-index?q=%22{query.replace(' ', '+')}"
            f"%22&dateRange=custom&startdt={date_from}&enddt={date_to}&forms=8-K")


# ------------------------------------------------------------------ premium
def coinbase_premium_bps(coinbase_mid, binance_mid):
    """(P_coinbase - P_binance)/P_binance * 10,000, in bps."""
    cb, bn = float(number(coinbase_mid)), float(number(binance_mid))
    if cb <= 0 or bn <= 0:
        return None
    return (cb - bn) / bn * 1e4


class CoinbasePremiumIndex:
    """Live premium from the two venue mids already streaming on the bus."""

    def __init__(self, bus, asset="BTC"):
        self.bus, self.asset = bus, asset

    def bps(self, now=None):
        mids = {}
        for tick in reversed(self.bus.ticks(self.asset, limit=64)):
            venue = tick.get("venue")
            if (venue in ("COINBASE", "BINANCE") and venue not in mids
                    and (now is None or 0 <= float(now) - float(tick.get("ts") or 0) <= 30)):
                mids[venue] = tick["price"]
        if len(mids) < 2:
            return None
        return coinbase_premium_bps(mids["COINBASE"], mids["BINANCE"])


# -------------------------------------------------------------- fear & greed
def parse_fng(payload):
    """alternative.me/fng/ JSON -> {value, classification, as_of}."""
    try:
        row = payload["data"][0]
        return {"value": int(row["value"]), "classification": row["value_classification"],
                "as_of": int(row["timestamp"])}
    except (KeyError, TypeError, ValueError, IndexError):
        return None


class FearGreedIndex:
    def __init__(self, fetch=None, clock=time.time, max_age=6 * 3600):
        self.fetch = fetch or default_fetch
        self.clock = clock
        self.max_age = float(max_age)
        self.cached = None
        self.last_fetch = 0.0

    def value(self):
        now = self.clock()
        if self.cached and now - self.last_fetch <= self.max_age:
            return self.cached
        try:
            payload = json.loads(self.fetch(FNG_URL))
            parsed = parse_fng(payload)
            if parsed:
                self.cached, self.last_fetch = parsed, now
        except (ValueError, RuntimeError, OSError):
            pass
        return self.cached


# ------------------------------------------------------------ macro blackout
def blackout_from_calendar(events, now, minutes=15.0):
    """Standalone +/- ``minutes`` blackout check over an events list
    [{name, time_utc, impact}]. Same semantics as Market_Intelligence:
    missing coverage returns (True, 'CALENDAR_UNAVAILABLE') - fail closed."""
    now = float(number(now))
    if not events:
        return True, "CALENDAR_UNAVAILABLE"
    for event in events:
        if str(event.get("impact", "")).upper() != "HIGH":
            continue
        event_time = epoch(event.get("time_utc"))
        if not event_time:
            return True, "CALENDAR_UNAVAILABLE"
        if abs(now - event_time) / 60.0 <= minutes:
            return True, str(event.get("name", "MACRO_EVENT"))
    return False, "NO_EVENT"
