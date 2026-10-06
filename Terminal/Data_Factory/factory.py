"""ZeroCostDataFactory: the all-in-one orchestrator (Pillars 1-6).

Owns the IntelligenceBus, the liquidation/stop reconstruction engines, the
whale label registry and the macro trackers, and exposes:

  * ``ingest_*``      - feed entry points used by the venue streamers and tests
  * ``payload``       - the SAME payload schema ``Omni_Trader``/``Chrome_Terminal``
                        build from Hyperdash today (l2_book, recent_trades,
                        l3_orders walls, projected_liquidations, observed_stops,
                        sources receipt timestamps) so ``Risk_Sizing_Engine``
                        and ``OF_Strategy`` consume it unchanged
  * ``payload_fetcher`` - a drop-in ``fetcher=`` adapter for ``AI15mMT5Trader``
  * ``snapshot``      - sealed (SHA-256 chained) bus feature vector
  * ``run``           - async lifecycle over injectable transports (tests
                        inject fakes; production lazy-imports websockets)

Everything degrades honestly: each payload block carries its own receipt
time in ``sources``, and ``Risk_Sizing_Engine`` already refuses stale blocks
- the factory never backfills or interpolates timestamps.
"""
from __future__ import annotations
import asyncio
import math
import time
from collections import deque
from pathlib import Path
from Terminal.Risk_Sizing_Engine import number
from Terminal.Data_Factory.bus import IntelligenceBus
from Terminal.Data_Factory.streams import (ReconnectingWebsocket, binance_symbol,
                                           coinbase_product, hyperliquid_coin,
                                           hyperliquid_subscription, parse_binance_trade,
                                           parse_binance_depth, parse_binance_force_order,
                                           parse_coinbase_match, CoinbaseBookAssembler,
                                           parse_hyperliquid)
from Terminal.Data_Factory.bulk import parse_open_interest, parse_hyperliquid_meta
from Terminal.Data_Factory.liquidation_engine import (LiquidationReconstructionEngine,
                                                      StopClusterEngine, liq_price)
from Terminal.Data_Factory.onchain import LabelRegistry, WhaleTransferListener
from Terminal.Data_Factory.macro import (FarsideETFFlows, FearGreedIndex,
                                         CoinbasePremiumIndex, blackout_from_calendar)

VERSION = "omni.zero_cost_data_factory.v1"


class _WallTracker:
    """Aggregates depth snapshots into persistent wall clusters (l3_orders)."""

    def __init__(self, *, cluster_tol_bps=10.0, min_notional_usd=150_000.0,
                 min_persistence_sec=180.0, top_n=20):
        self.cluster_tol = float(cluster_tol_bps) / 1e4
        self.min_notional_usd = float(min_notional_usd)
        self.min_persistence_sec = float(min_persistence_sec)
        self.top_n = int(top_n)
        self._walls = {}   # (asset, side, rounded_px) -> {"first":, "last":, "usd":}

    def observe(self, asset, book, now):
        """Refresh cluster persistence spans; returns l3_orders rows."""
        for side, rows, sign in (("BUY", book.get("bids") or [], -1),
                                 ("SELL", book.get("asks") or [], 1)):
            clusters = {}
            for row in rows:
                px, sz = number(row.get("price")), number(row.get("size"))
                if px <= 0 or sz <= 0:
                    continue
                key = round(math.log(px) / self.cluster_tol) if px > 0 else 0
                cluster = clusters.setdefault(key, {"px": [], "usd": 0.0})
                cluster["px"].append(px)
                cluster["usd"] += px * sz
            for key, cluster in clusters.items():
                edge = max(cluster["px"]) if side == "BUY" else min(cluster["px"])
                if cluster["usd"] < self.min_notional_usd:
                    continue
                wall_key = (asset, side, round(edge, 10))
                wall = self._walls.get(wall_key)
                if wall is None or now - wall["last"] > 30:
                    wall = {"first": now, "last": now, "usd": cluster["usd"]}
                wall.update(last=now, usd=cluster["usd"])
                self._walls[wall_key] = wall
        return self.l3_orders(asset, now)

    def l3_orders(self, asset, now):
        out = []
        for (a, side, edge), wall in self._walls.items():
            if a != asset or now - wall["last"] > 30:
                continue
            out.append({"side": side, "price": edge, "notional_usd": wall["usd"],
                        "persistence_sec": wall["last"] - wall["first"],
                        "observed_at": wall["last"], "order_id": f"wall:{side}:{edge}"})
        out.sort(key=lambda w: w["notional_usd"], reverse=True)
        return out[:self.top_n]


class ZeroCostDataFactory:
    """Single object the trading loop talks to."""

    def __init__(self, assets, *, bus=None, liq_engine=None, stop_engine=None,
                 registry=None, whale_listener=None, farside=None, fng=None,
                 capacity=1024, friction_bps=41.0, min_whale_usd=50_000.0,
                 clock=time.time):
        self.assets = [str(a).upper() for a in assets]
        self.bus = bus or IntelligenceBus(capacity)
        self.liq = liq_engine or LiquidationReconstructionEngine()
        self.stops = stop_engine or StopClusterEngine()
        self.registry = registry or LabelRegistry()
        self.whale_listener = whale_listener  # optional; RPC-bound in production
        self.farside = farside or FarsideETFFlows(clock=clock)
        self.fng = fng or FearGreedIndex(clock=clock)
        self.premium = CoinbasePremiumIndex(self.bus, self.assets[0] if self.assets else "BTC")
        self.friction_bps = float(friction_bps)
        self.min_whale_usd = float(min_whale_usd)
        self.clock = clock
        self.wall_tracker = _WallTracker()
        self._coinbase_books = CoinbaseBookAssembler()
        self._bars = {}
        self._profiles = {}
        self._oi_notional = {}
        self._whales = {}          # asset -> {"observed_at", "positions": [...]}
        self._whale_flows = {}     # asset -> deque of classified on-chain transfers
        self.stats = {"trades": 0, "books": 0, "liquidations": 0, "oi_samples": 0}

    # -------------------------------------------------------------- ingestion
    def ingest_trade(self, asset, event):
        if not event:
            return None
        published = self.bus.publish_trade(asset, **event)
        if published is not None:
            self.stats["trades"] += 1
            self.liq.observe_trade(asset, ts=event["ts"], price=event["price"],
                                   notional_usd=event.get("notional_usd"))
        return published

    def ingest_book(self, asset, book):
        if not book:
            return None
        self.bus.publish_book(asset, book)
        self.stats["books"] += 1
        return book

    def ingest_liquidation(self, asset, liquidation):
        if not liquidation:
            return None
        self.bus.publish_liquidation(asset, liquidation)
        self.stats["liquidations"] += 1
        self.liq.observe_forced(asset, ts=liquidation["ts"], price=liquidation["price"],
                                notional_usd=liquidation.get("notional_usd"),
                                position_side_liquidated=liquidation.get(
                                    "position_side_liquidated", "LONG"))
        return liquidation

    def ingest_bars(self, asset, bars):
        """Completed 15m bars power the stop-cluster structural model."""
        ordered = sorted((b for b in (bars or []) if number(b.get("time")) > 0),
                         key=lambda b: number(b["time"]))
        if ordered:
            self._bars[asset] = ordered
        return len(ordered)

    def ingest_volume_profile(self, asset, profile):
        if profile and number(profile.get("poc")) > 0:
            self._profiles[asset] = profile

    def ingest_oi(self, asset, *, ts, oi_contracts, price, contract_size=1.0):
        """Open-interest poll (Binance REST or Hyperliquid meta). Contracts
        are converted to position notional USD for the cohort model."""
        notional = float(number(oi_contracts)) * float(number(contract_size)) * float(number(price))
        previous = self._oi_notional.get(asset)
        self._oi_notional[asset] = notional
        buy, sell = self.bus.taker_flow(asset, 300.0, ts)
        ratio = buy / (buy + sell) if buy + sell > 0 else 0.5
        self.stats["oi_samples"] += 1
        return self.liq.observe_oi(asset, ts=ts, price=price, oi_usd=notional,
                                   taker_buy_ratio=ratio if previous is not None else 0.5)

    def ingest_whale_positions(self, asset, positions, observed_at=None):
        """Sampled whale cohort (Hyperliquid public /info clearinghouseState +
        frontendOpenOrders for tracked addresses - the exact Api_Client
        ``fetch_wallet_risk`` positions schema, $0 and keyless)."""
        rows = [dict(p) for p in (positions or []) if p]
        if rows:
            self._whales[asset] = {"observed_at": float(number(observed_at, self.clock())),
                                   "positions": rows[-32:]}
        return len(rows)

    def ingest_whale_flow(self, asset, transfer):
        """One classified on-chain whale transfer (WhaleTransferListener)."""
        if not transfer:
            return None
        flows = self._whale_flows.setdefault(asset, deque(maxlen=256))
        flows.append(dict(transfer))
        return transfer

    def _whale_net_flow_usd(self, asset, now, window_sec=86400.0):
        """Signed net exchange flow: OUTFLOW (coins leaving exchanges) is
        bullish accumulation, INFLOW is distribution. Zero lookahead."""
        net = 0.0
        for f in self._whale_flows.get(asset, ()):
            ts = number(f.get("ts"), 0.0)
            if ts <= 0 or not 0.0 <= now - ts <= window_sec:
                continue
            direction = str(f.get("direction", "")).upper()
            usd = number(f.get("notional_usd"), 0.0)
            if direction == "EXCHANGE_OUTFLOW":
                net += usd
            elif direction == "EXCHANGE_INFLOW":
                net -= usd
        return net

    # ---------------------------------------------------------------- frames
    def on_binance_frame(self, asset, frame):
        if (event := parse_binance_trade(frame)) is not None:
            self.ingest_trade(asset, event)
        elif (book := parse_binance_depth(frame)) is not None:
            self.ingest_book(asset, book)
        elif (liq := parse_binance_force_order(frame)) is not None:
            self.ingest_liquidation(asset, liq)

    def on_coinbase_frame(self, asset, frame):
        if (event := parse_coinbase_match(frame)) is not None:
            self.ingest_trade(asset, event)
            return
        if (book := self._coinbase_books.apply(frame)) is not None:
            self.ingest_book(asset, book)

    def on_hyperliquid_frame(self, asset, frame):
        parsed = parse_hyperliquid(frame)
        if not parsed:
            return
        if "book" in parsed:
            self.ingest_book(asset, parsed["book"])
        for trade in parsed.get("trades", []):
            self.ingest_trade(asset, trade)

    # --------------------------------------------------------------- payload
    def payload(self, asset, now=None):
        """Risk_Sizing-compatible payload (same contract as Chrome_Terminal)."""
        asset = str(asset).upper()
        now = float(number(now, self.clock()))
        book = self.bus.book(asset) or {}
        if book:
            # Trader contract: l2_book carries a venue "timestamp" (epoch s or
            # ms; ``epoch()`` normalizes) plus a receipt stamp; the staleness
            # gate in Risk_Sizing_Engine fails closed on both.
            book = dict(book)
            book.setdefault("timestamp", number(book.get("ts"), 0.0))
            book["received_at"] = now
        mid = self.bus.mid(asset)
        recent = self.bus.ticks(asset, limit=100)
        # Zero lookahead: a future-stamped venue tick (clock skew) never
        # enters a payload built for ``now``; it stays on the bus until the
        # evaluation clock catches up.
        trades = [{"time": e["ts"], "trade_id": e.get("trade_id"), "side": e.get("side"),
                   "price": e["price"], "size": e["size"],
                   "notional_usd": e.get("notional_usd"),
                   "is_whale": number(e.get("notional_usd")) >= self.min_whale_usd}
                  for e in recent if e.get("kind") != "LIQUIDATION" and e["ts"] <= now]
        liq_bands = self.liq.reconstruct(asset, now=now, current_price=mid)
        stop_bands = {"kind": "OBSERVED_STOP_ORDERS", "bands": [], "observed_at": now}
        if self._bars.get(asset) and mid:
            atr = self._atr(asset)
            stop_bands = self.stops.reconstruct(self._bars[asset], now=now, mid=mid,
                                                atr=atr, profile=self._profiles.get(asset))
        l3 = self.wall_tracker.observe(asset, book, now) if book else []
        whale = self._whales.get(asset)
        whale_positions = whale["positions"] if whale and 0.0 <= now - whale["observed_at"] <= 3600.0 else []
        orderflow = self.bus.snapshot(asset, now)
        sources = {"l2": {"observed_at": number(book.get("ts"), 0.0),
                          "timestamp_basis": "VENUE_EVENT_TIME"},
                   "l3": {"observed_at": now, "timestamp_basis": "RECEIPT_ONLY",
                          "coverage": "SYNTHETIC_WALL_CLUSTERS"},
                   "wallet_risk": {"observed_at": now, "timestamp_basis": "RECEIPT_ONLY",
                                   "coverage": liq_bands.get("coverage", "")},
                   "liquidations": {"observed_at": liq_bands.get("observed_at", 0.0),
                                    "timestamp_basis": "RECEIPT_ONLY",
                                    "coverage": "SYNTHETIC_OI_DELTA_MODEL"},
                   "stops": {"observed_at": stop_bands.get("observed_at", 0.0),
                             "timestamp_basis": "RECEIPT_ONLY",
                             "coverage": "SYNTHETIC_STRUCTURAL_MODEL"}}
        return {"coin": asset, "price": mid, "l2_book": book,
                "recent_trades": trades, "l3_orders": l3,
                "orderflow": orderflow,
                "whale_positions": whale_positions,
                "whale_net_flow_usd_24h": self._whale_net_flow_usd(asset, now),
                "projected_liquidations": liq_bands,
                "observed_stops": stop_bands,
                "liquidations": {**liq_bands, "empirical_bands": self.liq.empirical_bands(asset)},
                "stops": stop_bands,
                "sources": sources, "timestamp": int(now * 1000),
                "factory_version": VERSION}

    def payload_fetcher(self):
        """Adapter for ``AI15mMT5Trader(fetcher=...)``."""
        def fetch(asset):
            payload = self.payload(asset)
            if not payload.get("l2_book"):
                raise ValueError(f"no_book_yet:{asset}")
            return payload
        return fetch

    # ------------------------------------------------------- derived analytics
    def _atr(self, asset, lookback=14):
        bars = self._bars.get(asset) or []
        if len(bars) < 2:
            return 0.0
        trs = []
        for prev, cur in zip(bars[-(lookback + 1):], bars[-lookback:]):
            tr = number(cur.get("high")) - number(cur.get("low"))
            if number(prev.get("close")):
                tr = max(tr, abs(number(cur.get("high")) - number(prev.get("close"))),
                         abs(number(cur.get("low")) - number(prev.get("close"))))
            trs.append(max(tr, 0.0))
        return sum(trs) / len(trs) if trs else 0.0

    def max_pain(self, asset, now=None):
        return self.liq.max_pain(asset, now=float(number(now, self.clock())),
                                 current_price=self.bus.mid(asset))

    def fafr(self, asset, target_price, notional_usd, now=None):
        return self.liq.fafr(asset, now=float(number(now, self.clock())),
                             target_price=target_price, notional_usd=notional_usd,
                             friction_bps=self.friction_bps,
                             current_price=self.bus.mid(asset))

    def macro_snapshot(self):
        """Pillar 5 block for ``Market_Intelligence`` enrichment."""
        premium = self.premium.bps()
        fng = self.fng.value()
        flows = {}
        for asset in ("BTC", "ETH"):
            if self.farside.cache.get(asset):
                net = self.farside.net_flow(asset, lookback_days=1)
                if net:
                    flows[asset] = net["total_musd"]
        return {"coinbase_premium_bps": premium,
                "fear_greed": fng,
                "etf_net_flow_musd_1d": flows,
                "factory_version": VERSION}

    def snapshot(self, asset, now=None):
        return self.bus.seal(asset, float(number(now, self.clock())))

    # ------------------------------------------------------------------ run
    async def run(self, *, assets=None, transports=None, oi_poller=None,
                  poll_interval=300.0):
        """Async lifecycle. ``transports`` maps ('BINANCE'|'COINBASE'|
        'HYPERLIQUID', asset) -> async connect(url) factory for tests."""
        assets = assets or self.assets
        tasks = []
        for asset in assets:
            sym, product, coin = binance_symbol(asset), coinbase_product(asset), hyperliquid_coin(asset)
            if transports and ("BINANCE", asset) in transports:
                tasks.append(self._runner(ReconnectingWebsocket(
                    f"binance-{asset}", f"{binance_ws_base()}/{sym.lower()}@trade",
                    on_message=lambda f, a=asset: self.on_binance_frame(a, f),
                    connect=transports[("BINANCE", asset)])))
            if transports and ("COINBASE", asset) in transports:
                tasks.append(self._runner(ReconnectingWebsocket(
                    f"coinbase-{asset}", "wss://ws-feed.exchange.coinbase.com",
                    on_message=lambda f, a=asset: self.on_coinbase_frame(a, f),
                    subscriptions=[{"type": "subscribe", "product_ids": [product],
                                    "channels": ["matches", "level2_batch"]}],
                    connect=transports[("COINBASE", asset)])))
            if transports and ("HYPERLIQUID", asset) in transports:
                tasks.append(self._runner(ReconnectingWebsocket(
                    f"hyperliquid-{asset}", "wss://api.hyperliquid.xyz/ws",
                    on_message=lambda f, a=asset: self.on_hyperliquid_frame(a, f),
                    subscriptions=[hyperliquid_subscription("l2Book", coin),
                                   hyperliquid_subscription("trades", coin)],
                    heartbeat={"method": "ping"},
                    connect=transports[("HYPERLIQUID", asset)])))
        if oi_poller is not None:
            tasks.append(self._oi_loop(assets, oi_poller, poll_interval))
        if tasks:
            await asyncio.gather(*tasks)

    async def _runner(self, socket):
        await socket.run()

    async def _oi_loop(self, assets, oi_poller, interval):
        while True:
            for asset in assets:
                try:
                    sample = oi_poller(asset)
                    if sample:
                        self.ingest_oi(asset, **sample)
                except Exception:                     # noqa: BLE001 - poller resilience
                    pass
            await asyncio.sleep(interval)


def binance_ws_base():
    from Terminal.Data_Factory.streams import BINANCE_FUTURES_WS
    return BINANCE_FUTURES_WS
