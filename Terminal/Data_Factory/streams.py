"""Free CEX orderflow streamers: parsers + a resilient reconnecting socket.

Pillar 1 of the Data Factory. Three venues, zero API keys:

  * Binance USD-M Futures  wss://fstream.binance.com/ws
      - ``<sym>@trade``            individual trade ticks (taker side from ``m``)
      - ``<sym>@depth20@100ms``    top-20 book snapshots every 100 ms
      - ``<sym>@forceOrder``       REAL forced liquidation prints (empirical)
  * Coinbase Exchange      wss://ws-feed.exchange.coinbase.com
      - ``matches``        trade ticks (``side`` is the MAKER side; taker = flip)
      - ``level2_batch``   book snapshots + updates
  * Hyperliquid            wss://api.hyperliquid.xyz/ws
      - ``l2Book``         full book snapshots (``levels.bids/asks`` px/sz/n)
      - ``trades``         trade ticks (side B/A)
      - ``allMids``       mid prices for every coin

Every ``parse_*`` function is PURE: it takes one decoded JSON frame and
returns bus-ready events or None. The network layer is a separate,
injectable transport so tests replay recorded frames without a socket.

``ReconnectingWebsocket`` provides exponential backoff (1s -> 60s, jitter),
heartbeat keep-alive payloads, stall detection and graceful shutdown. The
``websockets`` library is imported lazily so offline hosts can still import
this module and run every parser.
"""
from __future__ import annotations
import asyncio
import json
import math
import random
import time
from datetime import datetime, timezone
from Terminal.Risk_Sizing_Engine import number

BINANCE_FUTURES_WS = "wss://fstream.binance.com/ws"
COINBASE_WS = "wss://ws-feed.exchange.coinbase.com"
HYPERLIQUID_WS = "wss://api.hyperliquid.xyz/ws"


def binance_symbol(asset):
    return str(asset).upper() + "USDT"


def coinbase_product(asset):
    return str(asset).upper() + "-USD"


def hyperliquid_coin(asset):
    return str(asset).upper()


# ------------------------------------------------------------------ Binance
def parse_binance_trade(frame):
    """Binance futures @trade -> bus trade event. ``m`` (buyer is market
    maker) means the AGGRESSOR sold."""
    if not isinstance(frame, dict) or frame.get("e") != "trade":
        return None
    side = "SELL" if frame.get("m") else "BUY"
    return {"ts": number(frame.get("T")) / 1000.0, "price": number(frame.get("p")),
            "size": number(frame.get("q")), "side": side, "venue": "BINANCE",
            "trade_id": f"b{frame.get('t')}",
            "notional_usd": number(frame.get("p")) * number(frame.get("q"))}


def parse_binance_depth(frame):
    """Binance futures @depth20@100ms partial-book frame -> book snapshot."""
    if not isinstance(frame, dict) or frame.get("e") != "depthUpdate":
        return None
    bids = [{"price": number(level[0]), "size": number(level[1])}
            for level in (frame.get("b") or []) if number(level[1]) > 0]
    asks = [{"price": number(level[0]), "size": number(level[1])}
            for level in (frame.get("a") or []) if number(level[1]) > 0]
    if not bids or not asks:
        return None
    return {"ts": number(frame.get("T") or frame.get("E")) / 1000.0,
            "best_bid": bids[0]["price"], "best_ask": asks[0]["price"],
            "bids": bids, "asks": asks, "venue": "BINANCE"}


def parse_binance_force_order(frame):
    """Binance @forceOrder -> empirical liquidation print.

    ``o.S`` is the side of the FORCED order: SELL means a LONG position was
    liquidated; BUY means a SHORT was liquidated. ``ap`` average price, ``q``
    original quantity, ``X`` order status (only FILTED/FILLED carry size).
    """
    if not isinstance(frame, dict) or frame.get("e") != "forceOrder":
        return None
    order = frame.get("o") or {}
    forced_side = str(order.get("S", "")).upper()          # order side
    if forced_side not in ("SELL", "BUY") or order.get("X") not in ("FILLED", "PARTIALLY_FILLED"):
        return None
    price = number(order.get("ap")) or number(order.get("p"))
    qty = number(order.get("q"))
    if price <= 0 or qty <= 0:
        return None
    return {"ts": number(order.get("T")) / 1000.0, "price": price, "size": qty,
            "side": forced_side,
            "position_side_liquidated": "LONG" if forced_side == "SELL" else "SHORT",
            "notional_usd": price * qty, "venue": "BINANCE"}


# ----------------------------------------------------------------- Coinbase
def parse_coinbase_match(frame):
    """Coinbase ``matches`` -> bus trade event. ``side`` on the feed is the
    MAKER side; the aggressor is the opposite."""
    if not isinstance(frame, dict) or frame.get("type") != "match":
        return None
    maker_side = str(frame.get("side", "")).lower()
    side = "SELL" if maker_side == "buy" else "BUY" if maker_side == "sell" else None
    if side is None:
        return None
    try:
        ts = datetime.fromisoformat(frame["time"].replace("Z", "+00:00")).timestamp()
    except (KeyError, ValueError, AttributeError):
        return None
    price, size = number(frame.get("price")), number(frame.get("size"))
    if price <= 0 or size <= 0:
        return None
    return {"ts": ts, "price": price, "size": size, "side": side, "venue": "COINBASE",
            "trade_id": f"c{frame.get('trade_id')}", "notional_usd": price * size}


class CoinbaseBookAssembler:
    """Assembles ``level2_batch`` snapshot + l2update frames into a book."""

    def __init__(self):
        self._book = {}   # (product, side) -> {price: size}

    def apply(self, frame):
        msg_type = frame.get("type")
        product = frame.get("product_id", "")
        if msg_type == "snapshot":
            book = {"bids": {}, "asks": {}}
            for side_key, feed_side in (("bids", "buy"), ("asks", "sell")):
                for price, size in frame.get(side_key) or []:
                    size = number(size)
                    if size > 0:
                        book[side_key][number(price)] = size
            self._book[product] = book
            return self._snapshot(product)
        if msg_type == "l2update":
            book = self._book.get(product)
            if book is None:
                return None
            ts = None
            try:
                ts = datetime.fromisoformat(frame["time"].replace("Z", "+00:00")).timestamp()
            except (KeyError, ValueError, AttributeError):
                ts = time.time()
            for feed_side, price, size in frame.get("changes") or []:
                side_key = "bids" if feed_side == "buy" else "asks"
                size = number(size)
                px = number(price)
                if size <= 0:
                    book[side_key].pop(px, None)
                else:
                    book[side_key][px] = size
            return self._snapshot(product, ts)
        return None

    def _snapshot(self, product, ts=None):
        book = self._book.get(product)
        if not book or not book["bids"] or not book["asks"]:
            return None
        bids = sorted(book["bids"].items(), reverse=True)
        asks = sorted(book["asks"].items())
        return {"ts": ts or time.time(), "best_bid": bids[0][0], "best_ask": asks[0][0],
                "bids": [{"price": p, "size": s} for p, s in bids[:40]],
                "asks": [{"price": p, "size": s} for p, s in asks[:40]],
                "venue": "COINBASE"}


# --------------------------------------------------------------- Hyperliquid
def parse_hyperliquid(frame):
    """Hyperliquid ws -> {"book": ..., "trades": [...], "mids": ...}.

    l2Book:  {channel, data: {coin, time (ms), levels: {bids, asks}}}
    trades:  {channel, data: [{coin, side: B|A, price, sz, tid, time (ms)}]}
    allMids: {channel, data: {mids: {coin: "px"}}}
    """
    if not isinstance(frame, dict):
        return None
    channel = frame.get("channel")
    data = frame.get("data")
    if channel == "l2Book" and isinstance(data, dict):
        levels = data.get("levels") or {}
        if isinstance(levels, list) and len(levels) >= 2:
            raw_bids, raw_asks = levels[0], levels[1]
        elif isinstance(levels, dict):
            raw_bids, raw_asks = levels.get("bids") or [], levels.get("asks") or []
        else:
            raw_bids, raw_asks = [], []
        bids = [{"price": number(l.get("px")), "size": number(l.get("sz"))}
                for l in raw_bids if number(l.get("sz")) > 0]
        asks = [{"price": number(l.get("px")), "size": number(l.get("sz"))}
                for l in raw_asks if number(l.get("sz")) > 0]
        if not bids or not asks:
            return None
        return {"book": {"ts": number(data.get("time")) / 1000.0,
                         "best_bid": bids[0]["price"], "best_ask": asks[0]["price"],
                         "bids": bids, "asks": asks, "venue": "HYPERLIQUID",
                         "coin": data.get("coin")}}
    if channel == "trades" and isinstance(data, list):
        trades = []
        for t in data:
            side = "BUY" if t.get("side") == "B" else "SELL" if t.get("side") == "A" else None
            price, size = number(t.get("price") or t.get("px")), number(t.get("sz"))
            if side is None or price <= 0 or size <= 0:
                continue
            trades.append({"ts": number(t.get("time")) / 1000.0, "price": price,
                           "size": size, "side": side, "venue": "HYPERLIQUID",
                           "trade_id": f"h{t.get('tid')}", "notional_usd": price * size})
        return {"trades": trades} if trades else None
    if channel == "allMids" and isinstance(data, dict):
        mids = {coin: number(px) for coin, px in (data.get("mids") or {}).items()
                if coin and not str(coin).startswith("@") and number(px) > 0}
        return {"mids": mids} if mids else None
    return None


def hyperliquid_subscription(channel, coin):
    return {"method": "subscribe",
            "subscription": {"type": channel, **({"coin": coin} if channel != "allMids" else {})}}


# ------------------------------------------------------------ transport
class ReconnectingWebsocket:
    """Resilient async websocket runner (backoff, heartbeat, stall detection).

    ``connect`` is injectable: anything async returning an object with
    ``send``/``recv``/``close`` (the ``websockets`` client shape). The
    production default lazy-imports ``websockets``; tests inject a fake.
    """

    def __init__(self, name, url, *, on_message, subscriptions=(), heartbeat=None,
                 heartbeat_interval=30.0, stall_sec=90.0, backoff_base=1.0,
                 backoff_max=60.0, jitter=0.25, connect=None, clock=time.monotonic):
        self.name, self.url = name, url
        self.on_message = on_message
        self.subscriptions = list(subscriptions)
        self.heartbeat = heartbeat
        self.heartbeat_interval = float(heartbeat_interval)
        self.stall_sec = float(stall_sec)
        self.backoff_base, self.backoff_max = float(backoff_base), float(backoff_max)
        self.jitter = float(jitter)
        self._connect = connect
        self._clock = clock
        self._stop = asyncio.Event() if _loop_running() else None
        self.reconnects = 0
        self.messages = 0
        self.last_message_at = None
        self.last_error = None

    def stop(self):
        if self._stop is not None:
            self._stop.set()

    async def _default_connect(self, url):
        try:
            import websockets  # lazy: offline hosts can still use parsers
        except ImportError as exc:
            raise RuntimeError("install 'websockets' to run live streams") from exc
        return await websockets.connect(url, ping_interval=20, ping_timeout=20,
                                        max_queue=4096, compression=None,
                                        max_size=10 * 1024 * 1024)

    async def run(self):
        self._stop = self._stop or asyncio.Event()
        backoff = self.backoff_base
        while not self._stop.is_set():
            ws = None
            try:
                connect = self._connect or self._default_connect
                ws = await connect(self.url)
                for sub in self.subscriptions:
                    await ws.send(json.dumps(sub))
                if self.heartbeat is not None:
                    await ws.send(json.dumps(self.heartbeat))
                self.reconnects += 1
                backoff = self.backoff_base
                while not self._stop.is_set():
                    timeout = min(self.heartbeat_interval, self.stall_sec)
                    try:
                        raw = await asyncio.wait_for(ws.recv(), timeout=timeout)
                    except asyncio.TimeoutError:
                        idle = self._clock() - (self.last_message_at or self._clock())
                        if idle > self.stall_sec:
                            raise ConnectionError(f"stall:{idle:.0f}s")
                        if self.heartbeat is not None:
                            await ws.send(json.dumps(self.heartbeat))
                        continue
                    self.messages += 1
                    self.last_message_at = self._clock()
                    try:
                        frame = json.loads(raw)
                    except (TypeError, ValueError):
                        continue
                    keep_going = self.on_message(frame)
                    if keep_going is False:
                        self._stop.set()
                        break
            except asyncio.CancelledError:
                raise
            except Exception as exc:                     # noqa: BLE001 - resilience loop
                self.last_error = repr(exc)
            finally:
                if ws is not None:
                    try:
                        await ws.close()
                    except Exception:                     # noqa: BLE001
                        pass
            if self._stop.is_set():
                break
            await asyncio.sleep(min(backoff * (1 + random.uniform(0, self.jitter)),
                                    self.backoff_max))
            backoff = min(backoff * 2, self.backoff_max)


def _loop_running():
    try:
        asyncio.get_running_loop()
        return True
    except RuntimeError:
        return False
