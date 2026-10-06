"""Binance Data Vision bulk ingestion (Pillar 2): free tick history to parquet.

``https://data.binance.vision/`` serves daily and monthly ZIP archives of
aggTrades, klines, funding rates and liquidation snapshots back to 2019 with
no API key and no rate limit. This module:

  * builds canonical URLs for daily/monthly archives (spot & USD-M futures),
  * downloads with an INJECTABLE fetcher (tests inject bytes; production uses
    urllib with a browser UA and retries),
  * verifies SHA-256 checksums (the ``.CHECKSUM`` sidecar),
  * parses aggTrades CSVs (zip, in-memory) into {ts_ms, price, size, side},
  * validates STRICT monotonic millisecond timestamps and zero nulls, and
  * appends to partitioned local Parquet atomically (unique on ts_ms,
    keep-last for re-runs), so the store is idempotent and gap-auditable.
"""
from __future__ import annotations
import csv
import hashlib
import io
import json
import re
import time
import urllib.request
import zipfile
from pathlib import Path
from Terminal.Risk_Sizing_Engine import number

DATA_VISION = "https://data.binance.vision/data"
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


def archive_url(market, kind, symbol, *, daily=False, date):
    """Canonical archive URL. market: 'spot'|'um'; kind: 'aggTrades'|'klines'|
    'fundingRate'|'liquidationSnapshot'; date: 'YYYY-MM' or 'YYYY-MM-DD'."""
    freq = "daily" if daily else "monthly"
    date = str(date)
    if daily and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        raise ValueError("daily archive needs YYYY-MM-DD")
    if not daily and not re.fullmatch(r"\d{4}-\d{2}", date):
        raise ValueError("monthly archive needs YYYY-MM")
    if market not in ("spot", "um"):
        raise ValueError("market must be 'spot' or 'um'")
    folder = {"aggTrades": "aggTrades", "klines": "klines", "fundingRate": "fundingRate",
              "liquidationSnapshot": "liquidationSnapshot"}[kind]
    name = f"{symbol}-{folder}-{date}.zip"
    return f"{DATA_VISION}/{market}/{freq}/{folder}/{symbol}/{name}"


def checksum_url(archive):
    return archive + ".CHECKSUM"


def default_fetch(url, timeout=30.0):
    """Production fetcher: browser UA, single retry on transient errors."""
    last_error = None
    for attempt in range(2):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except Exception as exc:                      # noqa: BLE001
            last_error = exc
            if attempt == 0:
                time.sleep(1.0 + attempt)
    raise RuntimeError(f"download_failed:{url}:{last_error!r}")


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def verify_checksum(data, checksum_text):
    """The CHECKSUM sidecar is '<sha256>  <filename>'."""
    expected = (checksum_text.decode() if isinstance(checksum_text, bytes)
                else str(checksum_text)).split()[0].strip().lower()
    actual = sha256_hex(data)
    if expected and actual != expected:
        raise ValueError(f"checksum_mismatch:expected_{expected[:12]}_got_{actual[:12]}")
    return True


def parse_agg_trades_zip(data):
    """aggTrades CSV -> [{ts_ms, price, size, side}].

    Columns: agg_trade_id, price, quantity, first_trade_id, last_trade_id,
    transact_time, is_buyer_maker. ``is_buyer_maker`` True => the aggressor
    SOLD."""
    rows = []
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        member = archive.namelist()[0]
        with archive.open(member) as raw:
            text = io.TextIOWrapper(raw, encoding="utf-8")
            for record in csv.reader(text):
                if not record or record[0] in ("agg_trade_id", "aggregateTradeId"):
                    continue
                try:
                    ts_ms = int(float(record[5]))
                    price = float(record[1])
                    size = float(record[2])
                    buyer_maker = str(record[6]).strip().lower() in ("true", "1")
                except (ValueError, IndexError):
                    continue
                if ts_ms <= 0 or price <= 0 or size < 0:
                    continue
                rows.append({"ts_ms": ts_ms, "price": price, "size": size,
                             "side": "SELL" if buyer_maker else "BUY"})
    return rows


def validate_rows(rows):
    """Strict monotonic unique timestamps + zero nulls; raises on violation."""
    previous = None
    for i, row in enumerate(rows):
        if None in (row.get("ts_ms"), row.get("price"), row.get("size"), row.get("side")):
            raise ValueError(f"null_field_at_row_{i}")
        if row["price"] <= 0 or row["size"] < 0 or row["ts_ms"] <= 0:
            raise ValueError(f"invalid_field_at_row_{i}")
        if previous is not None and row["ts_ms"] <= previous:
            raise ValueError(f"non_monotonic_timestamp_at_row_{i}:{previous}->{row['ts_ms']}")
        previous = row["ts_ms"]
    return {"rows": len(rows), "first_ts_ms": rows[0]["ts_ms"] if rows else None,
            "last_ts_ms": rows[-1]["ts_ms"] if rows else None}


def append_parquet(rows, path):
    """Atomic append to the per-asset parquet store (unique on ts_ms)."""
    import polars as pl
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    frame = pl.DataFrame({
        "ts_ms": [int(r["ts_ms"]) for r in rows],
        "price": [float(r["price"]) for r in rows],
        "size": [float(r["size"]) for r in rows],
        "side": [str(r["side"]) for r in rows]})
    if path.exists():
        old = pl.read_parquet(path)
        frame = pl.concat([old, frame]).unique(subset=["ts_ms"], keep="last",
                                               maintain_order=True).sort("ts_ms")
    tmp = path.with_suffix(".tmp.parquet")
    frame.write_parquet(tmp)
    tmp.replace(path)
    return {"total_rows": len(frame), "appended": len(rows)}


class DataVisionDownloader:
    """Orchestrates archive sync with injectable network for offline tests."""

    def __init__(self, root="Data/Ticks", fetch=None, verify=True):
        self.root = Path(root)
        self.fetch = fetch or default_fetch
        self.verify = bool(verify)

    def store_path(self, symbol):
        return self.root / f"{symbol}_aggTrades.parquet"

    def download_archive(self, market, kind, symbol, *, daily, date):
        url = archive_url(market, kind, symbol, daily=daily, date=date)
        data = self.fetch(url)
        if self.verify:
            try:
                checksum = self.fetch(checksum_url(url))
                verify_checksum(data, checksum)
            except RuntimeError:
                pass  # missing sidecar on some old archives: proceed unverified
        return data

    def sync_agg_trades(self, symbol, *, daily, date, market="um"):
        """Download -> validate -> parquet. Returns the audit report."""
        data = self.download_archive(market, "aggTrades", symbol, daily=daily, date=date)
        rows = parse_agg_trades_zip(data)
        report = validate_rows(rows)
        report.update(append_parquet(rows, self.store_path(symbol)))
        report["symbol"], report["date"] = symbol, str(date)
        return report

    def audit_gaps(self, symbol, expected_step_ms=None):
        """Gap audit over the persisted store: missing buckets between first
        and last timestamp (weekends are NOT expected gaps for crypto)."""
        import polars as pl
        path = self.store_path(symbol)
        if not path.exists():
            return {"symbol": symbol, "missing": [], "rows": 0}
        frame = pl.read_parquet(path)
        times = frame.get_column("ts_ms").to_list()
        if len(times) < 2:
            return {"symbol": symbol, "missing": [], "rows": len(times)}
        step = int(expected_step_ms or (times[1] - times[0]))
        missing = [b for a, b in zip(times, times[1:])
                   if step > 0 and b - a > step * 2][:1000]
        return {"symbol": symbol, "missing": missing, "rows": len(times),
                "step_ms": step, "first": times[0], "last": times[-1]}


# ------------------------------------------------------------ OI polling (free)
def binance_open_interest_url(symbol):
    """Free, keyless USD-M futures open-interest endpoint (REST poll)."""
    return f"https://fapi.binance.com/fapi/v1/openInterest?symbol={symbol}"


def parse_open_interest(payload):
    """/openInterest response {symbol, openInterest, time} (base units)."""
    try:
        return {"oi_contracts": float(payload["openInterest"]),
                "ts_ms": int(payload.get("time") or 0)}
    except (KeyError, TypeError, ValueError):
        return None


def hyperliquid_meta_url():
    return "https://api.hyperliquid.xyz/info"


def hyperliquid_meta_request():
    """POST body for HL /info 'metaAndAssetCtxs' (mark px + OI per coin)."""
    return json.dumps({"type": "metaAndAssetCtxs"}).encode()


def parse_hyperliquid_meta(response):
    """metaAndAssetCtxs -> {coin: {mark_px, open_interest, funding}}."""
    out = {}
    try:
        universe, contexts = response[0], response[1]
        for meta, ctx in zip(universe.get("universe", []), contexts):
            coin = meta.get("name")
            if not coin:
                continue
            out[coin.upper()] = {"mark_px": float(number(ctx.get("markPx"))),
                                 "open_interest": float(number(ctx.get("openInterest"))),
                                 "funding": float(number(ctx.get("funding"))),
                                 "day_volume": float(number(ctx.get("dayNtlVlm")))}
    except (TypeError, IndexError, KeyError, ValueError):
        return {}
    return out
