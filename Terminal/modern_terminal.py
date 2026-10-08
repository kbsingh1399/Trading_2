#!/usr/bin/env python3
"""
Terminal/modern_terminal.py
Modern High-Density Reactive TUI Orderflow Terminal.
Powered by Textual (Non-web, Native Terminal UI).

Features:
- Full Mouse Wheel & Trackpad Vertical Scrolling across all panels
- Split-Screen Architecture:
  * Left (68%): Interactive Scrollable Tabs [1. Liquidations] [2. Stops] [3. Multi-TF Orderflow] [4. Cross-Venue] [5. MT5 Risk]
  * Right (32%): Real-Time Level 2 Orderbook Ladder with Visual Depth Bars & Bid/Ask Ratio Meter
- Multi-Timeframe Running Candle Orderflow (4H, 1H, 15m) on the same screen with Taker Delta
- Instant Asset Switching (BTC, ETH, SOL, BNB, XRP, DOGE) via 'S' hotkey
- Live Non-Blocking Background Data Stream (Thread Worker)
- Zero Web Browser / Zero Web Server Required. Pure High-Performance Terminal.

Usage:
  python Terminal/modern_terminal.py
  python Terminal/modern_terminal.py --asset BTC
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from textual import work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.widgets import Footer, Header, Static, TabbedContent, TabPane

from Terminal.live_data_terminal import (
    DEFAULT_CRYPTO_ASSETS,
    aggregate_all_data,
    fetch_binance_mtf_orderflow,
    fetch_hyperdash_orderbook_and_analytics,
)


class OrderbookWidget(Static):
    """Right-Hand Dedicated Level 2 Orderbook Ladder with Visual Depth Bars."""

    def update_book(self, l2_data: Optional[Dict[str, Any]], coin: str) -> None:
        if not l2_data or not l2_data.get("bids") or not l2_data.get("asks"):
            t = Table(title=f"ORDERBOOK (L2) - {coin}", box=box.ROUNDED, expand=True)
            t.add_column("Status", style="dim yellow")
            t.add_row("Loading orderbook depth...")
            self.update(Panel(t, border_style="cyan", box=box.ROUNDED))
            return

        bids = l2_data.get("bids", [])[:10]
        asks = list(reversed(l2_data.get("asks", [])[:10]))
        max_vol = max([x.get("total_usd", 1.0) for x in bids + asks] + [1.0])

        table = Table(title=f"LEVEL 2 ORDERBOOK DEPTH - {coin}", box=box.SIMPLE_HEAD, expand=True, padding=(0, 1))
        table.add_column("Price (USD)", justify="right", style="bold")
        table.add_column("Size", justify="right")
        table.add_column("Notional", justify="right")
        table.add_column("Depth Bar", justify="left")

        # Asks (Red)
        for a in asks:
            v = a.get("total_usd", 0.0)
            bar_len = int((v / max_vol) * 16)
            bar = "█" * max(1, bar_len)
            table.add_row(
                f"${a['price']:,.2f}",
                f"{a['size']:.3f}",
                f"${v:,.0f}",
                f"[bright_red]{bar}[/bright_red]",
                style="bright_red",
            )

        # Spread
        spread = l2_data.get("spread", 0.0)
        spread_bps = l2_data.get("spread_bps", 0.0)
        table.add_row(
            "[bold yellow]── SPREAD ──[/bold yellow]",
            f"[bold yellow]${spread:,.2f}[/bold yellow]",
            f"[bold yellow]{spread_bps:.2f} bps[/bold yellow]",
            "[dim yellow]──────────────[/dim yellow]",
            style="bold yellow",
        )

        # Bids (Green)
        for b in bids:
            v = b.get("total_usd", 0.0)
            bar_len = int((v / max_vol) * 16)
            bar = "█" * max(1, bar_len)
            table.add_row(
                f"${b['price']:,.2f}",
                f"{b['size']:.3f}",
                f"${v:,.0f}",
                f"[bright_green]{bar}[/bright_green]",
                style="bright_green",
            )

        bid_pct = l2_data.get("bid_pct", 50.0)
        ask_pct = l2_data.get("ask_pct", 50.0)
        bid_vol = l2_data.get("bid_volume_usd", 0.0)
        ask_vol = l2_data.get("ask_volume_usd", 0.0)

        meter_len = 24
        g_len = int((bid_pct / 100.0) * meter_len)
        r_len = meter_len - g_len
        ratio_meter = f"[bright_green]{'█' * g_len}[/bright_green][bright_red]{'█' * r_len}[/bright_red]"

        footer = (
            f"Bids: ${bid_vol:,.0f} ({bid_pct:.1f}%) | {ratio_meter} | Asks: ${ask_vol:,.0f} ({ask_pct:.1f}%)\n"
            f"[bold {'bright_green' if bid_pct > 52 else ('bright_red' if ask_pct > 52 else 'dim white')}]"
            f"{'BUY ABSORPTION' if bid_pct > 52 else ('SELL PRESSURE' if ask_pct > 52 else 'BALANCED DEPTH')}[/]"
        )
        self.update(Panel(table, subtitle=footer, border_style="cyan", box=box.ROUNDED))


class LiquidationsWidget(Static):
    """Liquidations Tab Content (Matching Hyperdash Screenshot 1)."""

    def update_view(self, liqs: Optional[Dict[str, Any]], coin: str, current_px: float) -> None:
        if not liqs or not liqs.get("bands"):
            t = Table(title=f"LIQUIDATIONS CASCADE - {coin}", box=box.ROUNDED, expand=True)
            t.add_column("Status")
            t.add_row("Fetching real-time liquidation clusters from Hyperdash...")
            self.update(Panel(t, border_style="magenta", box=box.ROUNDED))
            return

        long_size = liqs.get("total_long_size", 0.0)
        short_size = liqs.get("total_short_size", 0.0)
        long_usd = long_size * current_px if current_px > 0 else 0.0
        short_usd = short_size * current_px if current_px > 0 else 0.0

        # Summary Header Card
        summary_text = Text()
        summary_text.append(f"TOTAL LONG LIQUIDATION RISK (DOWNSIDE CASCADE): ", style="bold bright_green")
        summary_text.append(f"{long_size:,.1f} {coin} (${long_usd / 1e6:,.2f}M USD)\n", style="bold white")
        summary_text.append(f"TOTAL SHORT LIQUIDATION RISK (UPSIDE SQUEEZE): ", style="bold bright_red")
        summary_text.append(f"{short_size:,.1f} {coin} (${short_usd / 1e6:,.2f}M USD)\n", style="bold white")
        ratio = (long_size / short_size) if short_size > 0 else 1.0
        summary_text.append(f"CASCADE BIAS RATIO: {ratio:.2f}x ({'Heavy Long Cascade Risk' if ratio > 1.2 else 'Heavy Short Squeeze Risk' if ratio < 0.8 else 'Neutral Distribution'})", style="bold yellow")

        # Ladder Table
        table = Table(title=f"LIQUIDATION CLUSTER LADDER (HYPERDASH)", box=box.SIMPLE_HEAD, expand=True)
        table.add_column("Price Band (USD)", style="bold", ratio=2)
        table.add_column("Distance %", justify="right", ratio=1)
        table.add_column("Cascade Type", justify="center", ratio=2)
        table.add_column("Estimated Volume", ratio=4)
        table.add_column("Notional Amount", justify="right", style="bold", ratio=2)

        bands = [b for b in liqs.get("bands", []) if b.get("amount", 0.0) > 0]
        max_amt = max([b.get("amount", 0.0) for b in bands] + [1.0])

        above = sorted([b for b in bands if b.get("mid_px", 0.0) >= current_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)[:35]
        below = sorted([b for b in bands if b.get("mid_px", 0.0) < current_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)[:35]

        for b in above:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - current_px) / current_px * 100.0) if current_px > 0 else 0.0
            bar_len = int((amt / max_amt) * 26)
            bar = "█" * max(1, bar_len)
            table.add_row(
                f"${b.get('min_px', 0.0):,.1f} - ${b.get('max_px', 0.0):,.1f}",
                f"{dist:+.1f}%",
                "[bright_red]SHORT SQUEEZE[/bright_red]",
                f"[bright_red]{bar}[/bright_red]",
                f"{amt:,.1f} {coin}",
            )

        table.add_row(
            f"[bold yellow]── SPOT: ${current_px:,.2f} ──[/bold yellow]",
            "[bold yellow]0.0%[/bold yellow]",
            "[bold yellow]MARKET MID[/bold yellow]",
            "[dim yellow]────────────────────────[/dim yellow]",
            "[bold yellow]CURRENT PRICE[/bold yellow]",
        )

        for b in below:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - current_px) / current_px * 100.0) if current_px > 0 else 0.0
            bar_len = int((amt / max_amt) * 26)
            bar = "█" * max(1, bar_len)
            table.add_row(
                f"${b.get('min_px', 0.0):,.1f} - ${b.get('max_px', 0.0):,.1f}",
                f"{dist:+.1f}%",
                "[bright_green]LONG CASCADE[/bright_green]",
                f"[bright_green]{bar}[/bright_green]",
                f"{amt:,.1f} {coin}",
            )

        content = Table.grid(expand=True)
        content.add_column()
        content.add_row(Panel(summary_text, style="magenta", box=box.ROUNDED))
        content.add_row(table)
        self.update(Panel(content, title=f"[bold magenta][LIQUIDATION HEATMAP - {coin} ({len(above)+len(below)} LEVELS)][/bold magenta]", border_style="magenta", box=box.ROUNDED))


class StopsWidget(Static):
    """Stops Tab Content (Matching Hyperdash Screenshot 2)."""

    def update_view(self, stops: Optional[Dict[str, Any]], coin: str, current_px: float) -> None:
        if not stops or not stops.get("bands"):
            t = Table(title=f"STOP-LOSS TRIGGER POOLS - {coin}", box=box.ROUNDED, expand=True)
            t.add_column("Status")
            t.add_row("Fetching live resting stop clusters from Hyperdash...")
            self.update(Panel(t, border_style="yellow", box=box.ROUNDED))
            return

        buy_stops = stops.get("total_buy_size", 0.0)
        sell_stops = stops.get("total_sell_size", 0.0)
        buy_usd = buy_stops * current_px if current_px > 0 else 0.0
        sell_usd = sell_stops * current_px if current_px > 0 else 0.0

        summary_text = Text()
        summary_text.append(f"TOTAL BUY STOPS (BREAKOUT ACCELERATION POOL): ", style="bold bright_cyan")
        summary_text.append(f"{buy_stops:,.1f} {coin} (${buy_usd / 1e6:,.2f}M USD)\n", style="bold white")
        summary_text.append(f"TOTAL SELL STOPS (BREAKDOWN ACCELERATION POOL): ", style="bold bright_yellow")
        summary_text.append(f"{sell_stops:,.1f} {coin} (${sell_usd / 1e6:,.2f}M USD)\n", style="bold white")
        summary_text.append(f"STOP POOL DENSITY: {'Upside Buy Stops Clustered' if buy_stops > sell_stops else 'Downside Sell Stops Clustered'}", style="bold green")

        table = Table(title=f"STOP-LOSS BREAKOUT & BREAKDOWN POOLS", box=box.SIMPLE_HEAD, expand=True)
        table.add_column("Price Range (USD)", style="bold", ratio=2)
        table.add_column("Distance %", justify="right", ratio=1)
        table.add_column("Trigger Side", justify="center", ratio=2)
        table.add_column("Stop Density", ratio=4)
        table.add_column("Volume", justify="right", style="bold", ratio=2)

        bands = [b for b in stops.get("bands", []) if b.get("amount", 0.0) > 0]
        max_amt = max([b.get("amount", 0.0) for b in bands] + [1.0])

        above = sorted([b for b in bands if b.get("mid_px", 0.0) >= current_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)[:35]
        below = sorted([b for b in bands if b.get("mid_px", 0.0) < current_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)[:35]

        for b in above:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - current_px) / current_px * 100.0) if current_px > 0 else 0.0
            bar_len = int((amt / max_amt) * 26)
            bar = "█" * max(1, bar_len)
            table.add_row(
                f"${b.get('min_px', 0.0):,.1f} - ${b.get('max_px', 0.0):,.1f}",
                f"{dist:+.1f}%",
                "[bright_cyan]BUY STOPS[/bright_cyan]",
                f"[bright_cyan]{bar}[/bright_cyan]",
                f"{amt:,.1f} {coin}",
            )

        table.add_row(
            f"[bold yellow]── SPOT: ${current_px:,.2f} ──[/bold yellow]",
            "[bold yellow]0.0%[/bold yellow]",
            "[bold yellow]MARKET MID[/bold yellow]",
            "[dim yellow]────────────────────────[/dim yellow]",
            "[bold yellow]CURRENT PRICE[/bold yellow]",
        )

        for b in below:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - current_px) / current_px * 100.0) if current_px > 0 else 0.0
            bar_len = int((amt / max_amt) * 26)
            bar = "█" * max(1, bar_len)
            table.add_row(
                f"${b.get('min_px', 0.0):,.1f} - ${b.get('max_px', 0.0):,.1f}",
                f"{dist:+.1f}%",
                "[bright_yellow]SELL STOPS[/bright_yellow]",
                f"[bright_yellow]{bar}[/bright_yellow]",
                f"{amt:,.1f} {coin}",
            )

        content = Table.grid(expand=True)
        content.add_column()
        content.add_row(Panel(summary_text, style="yellow", box=box.ROUNDED))
        content.add_row(table)
        self.update(Panel(content, title=f"[bold yellow][STOP-LOSS CLUSTERS - {coin}][/bold yellow]", border_style="yellow", box=box.ROUNDED))


class MultiTFOrderflowWidget(Static):
    """Current Running Candle Orderflow for 4H, 1H, and 15m on the same screen."""

    def update_view(self, mtf_data: Optional[Dict[str, Any]], coin: str) -> None:
        if not mtf_data:
            t = Table(title=f"MULTI-TIMEFRAME ORDERFLOW - {coin}", box=box.ROUNDED, expand=True)
            t.add_column("Status")
            t.add_row("Fetching running candle orderflow from Binance Futures...")
            self.update(Panel(t, border_style="green", box=box.ROUNDED))
            return

        table = Table(title=f"CURRENT RUNNING CANDLE ORDERFLOW - 4H | 1H | 15M", box=box.SIMPLE_HEAD, expand=True)
        table.add_column("Timeframe", style="bold yellow", justify="center")
        table.add_column("Candle Range (O -> C)", style="white", justify="right")
        table.add_column("High / Low", style="dim white", justify="right")
        table.add_column("Return %", style="bold", justify="right")
        table.add_column("Total Volume", style="cyan", justify="right")
        table.add_column("Taker Buy Vol", style="green", justify="right")
        table.add_column("Taker Sell Vol", style="red", justify="right")
        table.add_column("Net Delta", style="bold", justify="right")
        table.add_column("Imbalance %", style="bold", justify="center")
        table.add_column("Orderflow Pressure", style="bold", justify="left")

        for tf in ["4h", "1h", "15m"]:
            c = mtf_data.get(tf)
            if not c or "error" in c:
                table.add_row(tf.upper(), "-", "-", "-", "-", "-", "-", "-", "-", "[dim red]UNAVAILABLE[/dim red]")
                continue

            chg = c.get("change_pct", 0.0)
            chg_style = "bright_green" if chg >= 0 else "bright_red"
            chg_str = f"[{chg_style}]{chg:+.2f}%[/{chg_style}]"

            d = c.get("delta", 0.0)
            d_style = "bright_green" if d >= 0 else "bright_red"
            d_str = f"[{d_style}]{d:+,.2f} {coin}[/{d_style}]"

            imb = c.get("delta_pct", 0.0)
            imb_style = "bold bright_green" if imb > 5.0 else ("bold bright_red" if imb < -5.0 else "white")
            imb_str = f"[{imb_style}]{imb:+.1f}%[/{imb_style}]"

            pressure = "[bold bright_green]BUY ABSORPTION[/bold bright_green]" if imb > 10.0 else (
                "[bold bright_red]AGGRESSIVE SELLING[/bold bright_red]" if imb < -10.0 else (
                    "[bright_green]LEAN BUY[/bright_green]" if imb > 2.0 else (
                        "[bright_red]LEAN SELL[/bright_red]" if imb < -2.0 else "[dim white]NEUTRAL CONSOLIDATION[/dim white]"
                    )
                )
            )

            table.add_row(
                f"[bold cyan]{tf.upper()}[/bold cyan]",
                f"${c.get('open', 0):,.2f} -> ${c.get('close', 0):,.2f}",
                f"${c.get('high', 0):,.2f} / ${c.get('low', 0):,.2f}",
                chg_str,
                f"{c.get('volume', 0):,.1f} {coin}",
                f"{c.get('buy_volume', 0):,.1f} {coin}",
                f"{c.get('sell_volume', 0):,.1f} {coin}",
                d_str,
                imb_str,
                pressure,
            )

        self.update(Panel(table, title=f"[bold green][RUNNING CANDLE ORDERFLOW - {coin}][/bold green]", border_style="green", box=box.ROUNDED))


class CrossVenueWidget(Static):
    """8 Venues Cross-Comparison Table."""

    def update_view(self, data: Dict[str, Any], coin: str) -> None:
        p_info = data.get("per_asset", {}).get(coin, {})
        mt5_q = data.get("mt5", {}).get("quotes", {}).get(coin, {})
        bf = p_info.get("binance_futures", {})
        bs = p_info.get("binance_spot", {})
        cb = p_info.get("coinbase_spot", {})
        hl = p_info.get("hyperliquid", {})
        bb = p_info.get("bybit_linear", {})
        okx = p_info.get("okx_swap", {})
        krk = p_info.get("kraken_spot", {})

        baseline_spot = bs.get("spot_price") or 0.0

        t_price = Table(title=f"CROSS-VENUE PRICE & BASIS ARBITRAGE (8 SOURCES) - {coin}", box=box.SIMPLE_HEAD, expand=True)
        t_price.add_column("Venue / Source", style="bold yellow")
        t_price.add_column("Market Type", style="dim white")
        t_price.add_column("Live Price (USD)", style="bold green", justify="right")
        t_price.add_column("Delta vs Spot", style="cyan", justify="right")
        t_price.add_column("Basis / Spread (bps)", style="magenta", justify="right")

        def _row(venue, m_type, price, is_base=False, extra_bps=None):
            if price:
                delta = price - baseline_spot if (baseline_spot > 0 and not is_base) else 0.0
                delta_str = f"{delta:+,.2f} USD" if not is_base else "[dim]BASELINE[/dim]"
                bps = ((delta / baseline_spot) * 1e4) if (baseline_spot > 0 and not is_base) else (extra_bps or 0.0)
                bps_str = f"{bps:+.2f} bps" if not is_base else (f"{extra_bps:.1f} bps" if extra_bps else "[dim]0.0[/dim]")
                t_price.add_row(venue, m_type, f"${price:,.2f}", delta_str, bps_str)
            else:
                t_price.add_row(venue, m_type, "-", "-", "-")

        _row("MetaTrader 5 (Blueberry)", "Broker CFD Perpetuals", mt5_q.get("mid"), extra_bps=mt5_q.get("spread_bps"))
        _row("Binance Spot", "Spot Exchange (Primary)", bs.get("spot_price"), is_base=True)
        _row("Binance Futures (USDT-M)", "Perpetual Swap", bf.get("futures_price"))
        _row("Coinbase Pro", "US Regulated Spot", cb.get("spot_price"))
        hl_p = hl.get("mid_price") or hl.get("mark_price")
        _row("Hyperliquid", "On-Chain Perpetuals DEX", hl_p)
        _row("Bybit Linear", "Linear Perpetuals", bb.get("last_price"))
        _row("OKX Swap", "Perpetuals Swap", okx.get("last_price"))
        _row("Kraken Spot", "Regulated Spot Exchange", krk.get("last_price"))

        self.update(Panel(t_price, title=f"[bold blue][8-VENUE ARBITRAGE MATRIX - {coin}][/bold blue]", border_style="blue", box=box.ROUNDED))


class AllAssetsMatrixWidget(Static):
    """All 12 Assets Real-Time Multi-Timeframe Orderflow & Market Matrix."""

    def update_view(self, data: Dict[str, Any]) -> None:
        table = Table(title="ALL-ASSETS INSTITUTIONAL ORDERFLOW MATRIX (12 ASSETS)", box=box.SIMPLE_HEAD, expand=True)
        table.add_column("Asset", style="bold yellow")
        table.add_column("Spot / MT5", justify="right")
        table.add_column("Futures", justify="right")
        table.add_column("15m Delta", justify="right")
        table.add_column("15m Imb %", justify="center")
        table.add_column("1H Delta", justify="right")
        table.add_column("4H Delta", justify="right")
        table.add_column("Book Imb", justify="center")
        table.add_column("Binance OI", justify="right")
        table.add_column("Orderflow Regime", justify="left")

        per_asset = data.get("per_asset", {})
        for sym in DEFAULT_CRYPTO_ASSETS:
            p = per_asset.get(sym, {})
            bs = p.get("binance_spot", {}).get("spot_price")
            bf = p.get("binance_futures", {})
            bf_px = bf.get("futures_price")
            mtf = p.get("binance_mtf", {})
            c15 = mtf.get("15m", {})
            c1h = mtf.get("1h", {})
            c4h = mtf.get("4h", {})

            spot_str = f"${bs:,.2f}" if bs else "-"
            fut_str = f"${bf_px:,.2f}" if bf_px else "-"

            def _d(c):
                if not c or "delta" not in c:
                    return "-", "-"
                d = c["delta"]
                d_c = "bright_green" if d > 0 else "bright_red"
                imb = c.get("delta_pct", 0.0)
                imb_c = "bold bright_green" if imb > 5.0 else ("bold bright_red" if imb < -5.0 else "white")
                return f"[{d_c}]{d:+,.1f}[/{d_c}]", f"[{imb_c}]{imb:+.1f}%[/{imb_c}]"

            d15_s, imb15_s = _d(c15)
            d1h_s, _ = _d(c1h)
            d4h_s, _ = _d(c4h)

            book_imb = bf.get("book_imbalance")
            if book_imb is not None:
                b_c = "bold green" if book_imb > 0.1 else ("bold red" if book_imb < -0.1 else "white")
                b_str = f"[{b_c}]{book_imb:+.2f}[/{b_c}]"
            else:
                b_str = "-"

            oi = bf.get("open_interest_usd")
            oi_s = f"${oi/1e6:,.1f}M" if oi else "-"

            imb_val = c15.get("delta_pct", 0.0) if c15 else 0.0
            reg = "[bold bright_green]BUY ABSORPTION[/]" if imb_val > 5.0 else (
                "[bold bright_red]AGGRESSIVE SELL[/]" if imb_val < -5.0 else "[dim white]NEUTRAL[/]"
            )

            table.add_row(sym, spot_str, fut_str, d15_s, imb15_s, d1h_s, d4h_s, b_str, oi_s, reg)

        self.update(Panel(table, title="[bold cyan][ALL-ASSET SCREENER & MTF ORDERFLOW][/bold cyan]", border_style="cyan", box=box.ROUNDED))


class AccountWidget(Static):
    """MT5 Account State & Risk Headroom."""

    def update_view(self, data: Dict[str, Any]) -> None:
        mt5 = data.get("mt5") or {}
        acc = mt5.get("account") or {}
        balance = acc.get("balance", 0.0)
        equity = acc.get("equity", 0.0)
        margin_free = acc.get("margin_free", 0.0)
        open_pos = len(mt5.get("positions", [])) if isinstance(mt5.get("positions"), list) else 0
        pending_ord = len(mt5.get("orders", [])) if isinstance(mt5.get("orders"), list) else 0

        floor = 4775.00
        cushion = equity - floor
        buffer_val = 4795.00
        headroom = equity - buffer_val

        macro = data.get("macro") or {}
        fng = macro.get("fear_and_greed") or {}
        fng_str = f"{fng.get('value', 'N/A')} ({fng.get('classification', 'N/A')})"
        btc_flow = macro.get("btc_etf_flows") or {}
        btc_flow_str = f"{btc_flow.get('total_musd', 'N/A')} M USD ({btc_flow.get('date', 'N/A')})"

        acc_table = Table(box=box.SIMPLE_HEAD, expand=True)
        acc_table.add_column("MT5 Equity", style="bold green", justify="right")
        acc_table.add_column("Balance", style="white", justify="right")
        acc_table.add_column("Free Margin", style="cyan", justify="right")
        acc_table.add_column("Open Pos", style="yellow", justify="center")
        acc_table.add_column("Pending", style="yellow", justify="center")
        acc_table.add_column("Hard Floor", style="red", justify="right")
        acc_table.add_column("Floor Cushion", style="bold green" if cushion >= 20 else "bold red", justify="right")
        acc_table.add_column("Usable Headroom", style="bold cyan" if headroom > 0 else "bold red", justify="right")
        acc_table.add_column("Fear & Greed", style="magenta", justify="center")
        acc_table.add_column("BTC ETF Flow", style="blue", justify="right")

        acc_table.add_row(
            f"{equity:,.2f} USD",
            f"{balance:,.2f} USD",
            f"{margin_free:,.2f} USD",
            str(open_pos),
            str(pending_ord),
            f"{floor:,.2f} USD",
            f"+{cushion:,.2f} USD",
            f"+{headroom:,.2f} USD",
            fng_str,
            btc_flow_str,
        )

        self.update(Panel(acc_table, title="[bold][BROKER ACCOUNT & G-1 FLOOR DEFENSE][/bold]", border_style="green", box=box.ROUNDED))


class ModernOrderflowTerminal(App):
    """Institutional Modern Orderflow Terminal Application."""

    CSS = """
    Screen {
        background: #0d1117;
        color: #c9d1d9;
    }
    #top-bar {
        dock: top;
        height: 3;
        background: #161b22;
        color: #58a6ff;
        border-bottom: solid #30363d;
        padding: 0 1;
    }
    #main-split {
        height: 1fr;
    }
    #left-panel {
        width: 68%;
        height: 100%;
        border-right: solid #30363d;
    }
    #right-panel {
        width: 32%;
        height: 100%;
        padding: 0 1;
    }
    .scroll-container {
        height: 100%;
        overflow-y: auto;
    }
    TabbedContent {
        height: 100%;
    }
    TabPane {
        padding: 0;
    }
    """

    BINDINGS = [
        Binding("1", "switch_tab('tab_matrix')", "All-Asset Matrix"),
        Binding("2", "switch_tab('tab_liqs')", "Liquidations"),
        Binding("3", "switch_tab('tab_stops')", "Stops"),
        Binding("4", "switch_tab('tab_mtf')", "Multi-TF Orderflow"),
        Binding("5", "switch_tab('tab_cross')", "Cross-Venue"),
        Binding("6", "switch_tab('tab_acc')", "Account & Risk"),
        Binding("s", "cycle_coin", "Switch Coin"),
        Binding("r", "refresh_data", "Refresh"),
        Binding("q", "quit", "Quit"),
    ]

    def __init__(self, default_coin: str = "BTC") -> None:
        super().__init__()
        self.current_coin = default_coin.upper()
        self.watchlist = DEFAULT_CRYPTO_ASSETS
        self.coin_idx = self.watchlist.index(self.current_coin) if self.current_coin in self.watchlist else 0
        self.cached_data: Dict[str, Any] = {}
        self.is_fetching = False

    def compose(self) -> ComposeResult:
        yield Static(id="top-bar")
        with Horizontal(id="main-split"):
            with Container(id="left-panel"):
                with TabbedContent(id="tabs"):
                    with TabPane("All-Asset Matrix (12 Assets)", id="tab_matrix"):
                        with VerticalScroll(classes="scroll-container"):
                            yield AllAssetsMatrixWidget(id="widget_matrix")
                    with TabPane("Liquidations (Hyperdash)", id="tab_liqs"):
                        with VerticalScroll(classes="scroll-container"):
                            yield LiquidationsWidget(id="widget_liqs")
                    with TabPane("Stops (Hyperdash)", id="tab_stops"):
                        with VerticalScroll(classes="scroll-container"):
                            yield StopsWidget(id="widget_stops")
                    with TabPane("Multi-TF Orderflow (4H|1H|15m)", id="tab_mtf"):
                        with VerticalScroll(classes="scroll-container"):
                            yield MultiTFOrderflowWidget(id="widget_mtf")
                    with TabPane("Cross-Venue (8 Venues)", id="tab_cross"):
                        with VerticalScroll(classes="scroll-container"):
                            yield CrossVenueWidget(id="widget_cross")
                    with TabPane("MT5 Account & Risk", id="tab_acc"):
                        with VerticalScroll(classes="scroll-container"):
                            yield AccountWidget(id="widget_acc")
            with Container(id="right-panel"):
                with VerticalScroll(classes="scroll-container"):
                    yield OrderbookWidget(id="widget_book")
        yield Footer()

    def on_mount(self) -> None:
        self.title = f"HYPERDASH & QUANT ORDERFLOW TERMINAL — {self.current_coin}"
        self.refresh_data()
        self.set_interval(3.0, self.refresh_data)

    def action_switch_tab(self, tab_id: str) -> None:
        try:
            tabs = self.query_one(TabbedContent)
            tabs.active = tab_id
        except Exception:
            pass

    def action_cycle_coin(self) -> None:
        self.coin_idx = (self.coin_idx + 1) % len(self.watchlist)
        self.current_coin = self.watchlist[self.coin_idx]
        self.title = f"HYPERDASH & QUANT ORDERFLOW TERMINAL — {self.current_coin}"
        self.refresh_data()

    def action_refresh_data(self) -> None:
        self.refresh_data()

    @work(thread=True)
    def refresh_data(self) -> None:
        if self.is_fetching:
            return
        self.is_fetching = True
        try:
            data = aggregate_all_data(self.watchlist)
            self.app.call_from_thread(self._apply_data, data)
        except Exception as e:
            pass
        finally:
            self.is_fetching = False

    def _apply_data(self, data: Dict[str, Any]) -> None:
        self.cached_data = data
        p_info = data.get("per_asset", {}).get(self.current_coin, {})
        hd = p_info.get("hyperdash_analytics") or {}
        l2 = hd.get("l2") or {}
        liqs = hd.get("liquidations") or {}
        stops = hd.get("stops") or {}
        mtf = p_info.get("binance_mtf") or {}

        # Mark price
        mark_px = l2.get("best_bid") or p_info.get("binance_spot", {}).get("spot_price") or 0.0

        # Update Top Bar
        now_utc = datetime.now(timezone.utc).strftime("%H:%M:%S UTC")
        bar_text = Text()
        bar_text.append(" HYPERDASH QUANT TERMINAL ", style="bold black on bright_cyan")
        bar_text.append(f"  ASSET: {self.current_coin}-PERP  ", style="bold white on blue")
        bar_text.append(f"PRICE: ${mark_px:,.2f}  ", style="bold bright_green")
        bar_text.append(f"WATCHLIST: {' > '.join(self.watchlist)}  ", style="dim white")
        bar_text.append(f"TIME: {now_utc}  ", style="bold yellow")
        bar_text.append("● LIVE", style="bold green")
        self.query_one("#top-bar", Static).update(bar_text)

        # Update Right Panel (Orderbook)
        self.query_one("#widget_book", OrderbookWidget).update_book(l2, self.current_coin)

        # Update Tabs
        self.query_one("#widget_matrix", AllAssetsMatrixWidget).update_view(data)
        self.query_one("#widget_liqs", LiquidationsWidget).update_view(liqs, self.current_coin, mark_px)
        self.query_one("#widget_stops", StopsWidget).update_view(stops, self.current_coin, mark_px)
        self.query_one("#widget_mtf", MultiTFOrderflowWidget).update_view(mtf, self.current_coin)
        self.query_one("#widget_cross", CrossVenueWidget).update_view(data, self.current_coin)
        self.query_one("#widget_acc", AccountWidget).update_view(data)


def main() -> None:
    parser = argparse.ArgumentParser(description="Modern Institutional Orderflow Terminal")
    parser.add_argument("--asset", "-a", type=str, default="BTC", help="Initial trading coin (e.g. BTC, ETH, SOL)")
    args = parser.parse_args()

    app = ModernOrderflowTerminal(default_coin=args.asset)
    app.run()


if __name__ == "__main__":
    main()
