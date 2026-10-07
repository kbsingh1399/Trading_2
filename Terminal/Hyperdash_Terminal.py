#!/usr/bin/env python3
"""
Terminal/Hyperdash_Terminal.py
Institutional Real-Time Continuous Hyperdash & Hyperliquid Terminal.
Features:
- Continuous live stream loop (sub-second reactive rendering, 0% CPU idle)
- Live asset switching on the fly (via 'S' modal or Left/Right arrow keys)
- Level 2 Orderbook with Cyberpunk Visual Depth Bars & Bid/Ask Ratio Meter
- Level 3 Whale Orders mapped to verified Ethereum Wallet Addresses
- Live Liquidation Risk Ladder & Concentration Heatmap
- Live Stop-Loss Clusters & Microstructure Imbalance Metrics
- Real-Time Live Trades Tape with Aggressor Side & Whale Alerts
- 234-Coin Asset Universe Screener (Volume, OI, 24h PnL, Funding APR)
- Historical Data Downloader Integration
"""

import sys
import os
import time
import datetime
import pathlib
from typing import Optional, List, Dict, Any

# Windows non-blocking keyboard input
try:
    import msvcrt
    HAS_MSVCRT = True
except ImportError:
    HAS_MSVCRT = False

# Ensure workspace root is in sys.path
root_dir = pathlib.Path(__file__).parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from Terminal.Api_Client import HyperdashClient

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.columns import Columns
from rich.prompt import Prompt
from rich import box

console = Console()

class HyperdashTerminal:
    def __init__(self, default_coin: str = "BTC"):
        self.client = HyperdashClient()
        self.current_coin = default_coin.upper()
        self.active_tab = "1"  # Default: L2 Orderbook
        self.all_assets: List[Dict[str, Any]] = []
        self.cached_asset_info: Dict[str, Any] = {}
        self.depth_levels = 15
        
        # Real-time state tracking
        self.prev_price = 0.0
        self.price_direction = "neutral"  # "up", "down", "neutral"
        self.last_update_ts = time.time()
        self.is_paused = False
        self.refresh_interval = 1.0  # seconds between live data ticks
        self.error_count = 0
        self.status_msg = "CONNECTED (LIVE FEED)"
        
        # Priority Watchlist for instant single-key cycling
        self.watchlist = ["BTC", "ETH", "SOL", "BNB", "XRP", "DOGE", "ADA", "SUI", "LINK", "AVAX"]
        
        # Caches for resilience
        self.cached_l2: Optional[Dict[str, Any]] = None
        self.cached_trades: List[Dict[str, Any]] = []
        self.cached_l3: List[Dict[str, Any]] = []
        self.cached_liqs: Dict[str, Any] = {}
        self.cached_stops: Dict[str, Any] = {}

        # Initial bootstrap
        self.refresh_universe()

    def refresh_universe(self):
        """Fetch latest market metadata and update current coin cache."""
        try:
            self.all_assets = self.client.fetch_all_assets()
            coin_match = [a for a in self.all_assets if a["coin"] == self.current_coin]
            if coin_match:
                self.cached_asset_info = coin_match[0]
            elif self.all_assets:
                self.cached_asset_info = self.all_assets[0]
                self.current_coin = self.cached_asset_info["coin"]
            self.status_msg = "CONNECTED (LIVE FEED)"
            self.error_count = 0
        except Exception as e:
            self.status_msg = f"NETWORK WARN: {str(e)[:30]}"
            self.error_count += 1

    def switch_asset(self, new_coin: str):
        """Switch active trading asset cleanly and refresh data."""
        clean_coin = new_coin.strip().upper()
        if not self.all_assets:
            self.refresh_universe()
            
        matched = [a for a in self.all_assets if a["coin"] == clean_coin]
        if matched:
            self.current_coin = clean_coin
            self.cached_asset_info = matched[0]
            self.prev_price = self.cached_asset_info.get("mark_px", 0.0)
            self.price_direction = "neutral"
            # Clear tab caches to prevent stale data
            self.cached_l2 = None
            self.cached_trades = []
            self.cached_l3 = []
            self.cached_liqs = {}
            self.cached_stops = {}
            self.status_msg = f"SWITCHED TO {self.current_coin}"
            return True
        return False

    def cycle_watchlist(self, direction: int = 1):
        """Cycle through the institutional watchlist with Left/Right keys."""
        if self.current_coin in self.watchlist:
            idx = self.watchlist.index(self.current_coin)
            new_idx = (idx + direction) % len(self.watchlist)
        else:
            new_idx = 0 if direction > 0 else (len(self.watchlist) - 1)
        self.switch_asset(self.watchlist[new_idx])

    def fetch_live_tick(self):
        """Fetch real-time data frame for the current asset."""
        try:
            now = time.time()
            # 1. Periodically update Universe context (every 10s)
            if not hasattr(self, 'last_universe_refresh'):
                self.last_universe_refresh = 0.0
            if (now - self.last_universe_refresh) > 10.0 or not self.cached_asset_info:
                self.refresh_universe()
                self.last_universe_refresh = now

            # 2. Fetch L2 Book (primary depth) & Recent Trades (tape)
            self.cached_l2 = self.client.fetch_l2_book(self.current_coin)
            self.cached_trades = self.client.fetch_recent_trades(self.current_coin)

            # 3. Dynamic Real-Time Price Resolution (ticks every second!)
            curr_px = self.cached_asset_info.get("mark_px", 0.0)
            if self.cached_trades and len(self.cached_trades) > 0:
                curr_px = float(self.cached_trades[0].get("px", curr_px))
            elif self.cached_l2:
                best_bid = self.cached_l2.get("best_bid", 0.0)
                best_ask = self.cached_l2.get("best_ask", 0.0)
                if best_bid > 0 and best_ask > 0:
                    curr_px = (best_bid + best_ask) / 2.0

            if self.prev_price > 0:
                if curr_px > self.prev_price:
                    self.price_direction = "up"
                elif curr_px < self.prev_price:
                    self.price_direction = "down"
            self.prev_price = curr_px
            self.cached_asset_info["mark_px"] = curr_px

            # 4. Fetch Active Tab Specialized Data
            if self.active_tab == "2":
                min_px = curr_px * 0.985
                max_px = curr_px * 1.015
                self.cached_l3 = self.client.fetch_l3_orders(self.current_coin, min_px, max_px)
            elif self.active_tab == "3":
                min_px = curr_px * 0.80
                max_px = curr_px * 1.20
                self.cached_liqs = self.client.fetch_liquidations(self.current_coin, min_px, max_px)
            elif self.active_tab == "4":
                min_px = curr_px * 0.80
                max_px = curr_px * 1.20
                self.cached_stops = self.client.fetch_stops(self.current_coin, min_px, max_px)

            self.status_msg = "CONNECTED (LIVE FEED)"
            self.error_count = 0
            self.last_update_ts = time.time()
        except Exception as e:
            self.status_msg = f"LIVE TICK WARN: {str(e)[:35]}"
            self.error_count += 1

    def render_header(self) -> Panel:
        """Render high-density institutional header with live status and badges."""
        info = self.cached_asset_info
        mark_px = info.get("mark_px", 0.0)
        chg_24h = info.get("change_24h", 0.0)
        vol_24h = info.get("volume_24h", 0.0)
        oi_usd = info.get("open_interest_usd", 0.0)
        funding = info.get("funding_annualized", 0.0)
        max_lev = info.get("max_leverage", 50)

        # Directional Arrow & Color
        if self.price_direction == "up":
            px_style = "bold bright_green"
            arrow = "▲ "
        elif self.price_direction == "down":
            px_style = "bold bright_red"
            arrow = "▼ "
        else:
            px_style = "bold bright_white"
            arrow = "● "

        chg_color = "bright_green" if chg_24h >= 0 else "bright_red"
        chg_sign = "+" if chg_24h >= 0 else ""

        # UTC clock
        utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S UTC")

        # Live Pulse Indicator
        status_color = "bright_yellow" if self.is_paused else ("bright_red" if self.error_count > 0 else "bright_green")
        status_text = "PAUSED ❚❚" if self.is_paused else f"LIVE ● {utc_now}"

        header_top = Text()
        header_top.append(" HYPERDASH ", style="bold black on bright_cyan")
        header_top.append(f" {status_text} ", style=f"bold black on {status_color}")
        header_top.append(f"  ASSET: {self.current_coin}-PERP ({max_lev}x)  ", style="bold white on blue")
        header_top.append(f"PRICE: ", style="dim white")
        header_top.append(f"{arrow}${mark_px:,.2f}  ", style=px_style)
        header_top.append(f"24h: {chg_sign}{chg_24h:.2f}%  ", style=f"bold {chg_color}")
        header_top.append(f"VOL: ${vol_24h:,.0f}  ", style="bright_yellow")
        header_top.append(f"OI: ${oi_usd:,.0f}  ", style="bright_magenta")
        header_top.append(f"FUNDING (APR): {funding:+.2f}%  ", style="bright_cyan")
        header_top.append(f"[{self.status_msg}]", style="dim green" if self.error_count == 0 else "dim red")

        # Tabs Navigation Bar
        nav_text = Text("\nTABS: ", style="bold bright_white")
        tabs = [
            ("1", "Orderbook (L2)"),
            ("2", "L3 Whale Orders"),
            ("3", "Liquidations Ladder"),
            ("4", "Stop Clusters"),
            ("5", "Recent Trades"),
            ("6", "Universe Screener (234 Coins)"),
        ]
        for key, label in tabs:
            if key == self.active_tab:
                nav_text.append(f" [{key}] {label} ", style="bold black on bright_green")
            else:
                nav_text.append(f" [{key}] {label} ", style="dim cyan")

        # Command Quick-Bar
        nav_text.append("  |  HOTKEYS: ", style="dim white")
        nav_text.append("[S] Switch Asset ", style="bold bright_yellow")
        nav_text.append("[←/→] Cycle Watchlist ", style="bold bright_cyan")
        nav_text.append("[Space] Pause ", style="dim yellow")
        nav_text.append("[D] Download ", style="dim white")
        nav_text.append("[Q] Quit", style="bold bright_red")

        return Panel(header_top + nav_text, style="cyan", border_style="cyan", box=box.ROUNDED)

    def render_l2_orderbook(self) -> Panel:
        """Render Level 2 Orderbook with Cyberpunk Visual Depth Bars & Bid/Ask Ratio."""
        if not self.cached_l2:
            try:
                self.cached_l2 = self.client.fetch_l2_book(self.current_coin)
            except Exception as e:
                return Panel(f"[bold red]Orderbook unavailable: {e}[/bold red]", border_style="red")

        book = self.cached_l2
        bids = book.get("bids", [])[:self.depth_levels]
        asks = list(reversed(book.get("asks", [])[:self.depth_levels]))

        table = Table(title=f"LEVEL 2 ORDERBOOK & LIQUIDITY DEPTH - {self.current_coin}", box=None, expand=True, padding=(0, 1))
        table.add_column("Price (USD)", justify="right", style="bold", ratio=2)
        table.add_column("Size", justify="right", ratio=2)
        table.add_column("Notional (USD)", justify="right", ratio=2)
        table.add_column("Visual Depth", justify="left", ratio=4)

        max_vol = max([a.get("total_usd", 1.0) for a in asks] + [b.get("total_usd", 1.0) for b in bids] + [1.0])

        # Asks (Red)
        for a in asks:
            bar_len = int((a.get("total_usd", 0.0) / max_vol) * 28)
            bar = "█" * max(1, bar_len)
            table.add_row(
                f"${a['price']:,.2f}",
                f"{a['size']:.4f}",
                f"${a['total_usd']:,.0f}",
                f"[bright_red]{bar}[/bright_red]",
                style="bright_red"
            )

        # Spread Indicator
        spread = book.get("spread", 0.0)
        spread_bps = book.get("spread_bps", 0.0)
        spread_text = f"─── SPREAD: ${spread:,.2f} ({spread_bps:.2f} bps) ───"
        table.add_row("", spread_text, "", "", style="bold bright_yellow")

        # Bids (Green)
        for b in bids:
            bar_len = int((b.get("total_usd", 0.0) / max_vol) * 28)
            bar = "█" * max(1, bar_len)
            table.add_row(
                f"${b['price']:,.2f}",
                f"{b['size']:.4f}",
                f"${b['total_usd']:,.0f}",
                f"[bright_green]{bar}[/bright_green]",
                style="bright_green"
            )

        # Volume Ratio Balance Meter
        bid_vol = book.get("bid_volume_usd", 0.0)
        ask_vol = book.get("ask_volume_usd", 0.0)
        bid_pct = book.get("bid_pct", 50.0)
        ask_pct = book.get("ask_pct", 50.0)

        meter_len = 45
        green_bars = int((bid_pct / 100.0) * meter_len)
        red_bars = meter_len - green_bars
        balance_meter = f"[bright_green]{'█' * green_bars}[/bright_green][bright_red]{'█' * red_bars}[/bright_red]"

        imbalance_label = "[bold bright_green]BUY PRESSURE[/bold bright_green]" if bid_pct > 55 else (
            "[bold bright_red]SELL PRESSURE[/bold bright_red]" if ask_pct > 55 else "[dim cyan]BALANCED[/dim cyan]"
        )

        footer = (
            f"Bids: ${bid_vol:,.0f} ({bid_pct:.1f}%) | {balance_meter} | Asks: ${ask_vol:,.0f} ({ask_pct:.1f}%)\n"
            f"Orderflow Pressure: {imbalance_label}  |  Depth Levels: ±{self.depth_levels}  |  Watchlist: {' > '.join(self.watchlist[:6])}"
        )
        return Panel(table, subtitle=footer, style="bright_green", border_style="green", box=box.ROUNDED)

    def render_l3_orders(self) -> Panel:
        """Render Level 3 Resting Whale Orders mapped to verified Ethereum Wallets."""
        orders = self.cached_l3
        if not orders:
            try:
                curr_px = self.cached_asset_info.get("mark_px", 100.0)
                orders = self.client.fetch_l3_orders(self.current_coin, curr_px * 0.985, curr_px * 1.015)
                self.cached_l3 = orders
            except Exception as e:
                return Panel(f"[bold red]Level 3 data unavailable: {e}[/bold red]", border_style="red")

        table = Table(title=f"LEVEL 3 RESTING WHALE ORDERS (VERIFIED WALLET ADDRESSES) - {self.current_coin}", box=box.SIMPLE_HEAD, expand=True)
        table.add_column("Tier", justify="center")
        table.add_column("Wallet Address", style="bold bright_cyan")
        table.add_column("Side", justify="center")
        table.add_column("Limit Price", justify="right")
        table.add_column("Size", justify="right")
        table.add_column("Notional Value", justify="right", style="bold")
        table.add_column("Distance %", justify="right")

        curr_px = self.cached_asset_info.get("mark_px", 1.0)
        for o in orders[:20]:
            val = o.get("notional_usd", 0.0)
            if val >= 500000:
                tier = "[bold bright_yellow]🐋 MEGA WHALE[/bold bright_yellow]"
            elif val >= 150000:
                tier = "[bold bright_cyan]🐳 WHALE[/bold bright_cyan]"
            elif val >= 50000:
                tier = "[bold blue]🦈 SHARK[/bold blue]"
            else:
                tier = "[dim]🐬 DOLPHIN[/dim]"

            side_color = "bright_green" if o.get("side") == "BUY" else "bright_red"
            px = o.get("price", 0.0)
            dist_pct = ((px - curr_px) / curr_px) * 100.0 if curr_px > 0 else 0.0

            addr = o.get("address", "")
            disp_addr = f"{addr[:8]}...{addr[-6:]}" if len(addr) > 16 else addr

            table.add_row(
                tier,
                disp_addr,
                f"[{side_color}]{o.get('side')}[/{side_color}]",
                f"${px:,.2f}",
                f"{o.get('size', 0.0):.4f}",
                f"${val:,.0f}",
                f"{dist_pct:+.2f}%"
            )

        summary = f"Total Whale Orders Monitored: {len(orders)}  |  Top Whale Size: ${orders[0]['notional_usd']:,.0f}" if orders else "No resting orders in filter range."
        return Panel(table, subtitle=summary, style="cyan", border_style="cyan", box=box.ROUNDED)

    def render_liquidations(self) -> Panel:
        """Render Live Liquidation Risk Ladder & Concentration Heatmap."""
        data = self.cached_liqs
        if not data:
            try:
                curr_px = self.cached_asset_info.get("mark_px", 100.0)
                data = self.client.fetch_liquidations(self.current_coin, curr_px * 0.80, curr_px * 1.20)
                self.cached_liqs = data
            except Exception as e:
                return Panel(f"[bold red]Liquidations data unavailable: {e}[/bold red]", border_style="red")

        long_size = data.get("total_long_size", 0.0)
        short_size = data.get("total_short_size", 0.0)
        curr_px = data.get("current_price", self.cached_asset_info.get("mark_px", 0.0))

        table = Table(title=f"LIQUIDATION CASCADE HEATMAP & CONCENTRATION LADDER - {self.current_coin}", box=box.SIMPLE_HEAD, expand=True)
        table.add_column("Price Band (USD)", style="bold", ratio=2)
        table.add_column("Distance %", justify="right", ratio=1)
        table.add_column("Type", justify="center", ratio=1)
        table.add_column("Estimated Liquidation Volume", ratio=4)
        table.add_column("Notional Amount", justify="right", ratio=2)

        bands = data.get("bands", [])
        max_amt = max([b.get("amount", 0.0) for b in bands] + [1.0])

        for b in sorted(bands, key=lambda x: x.get("mid_px", 0.0), reverse=True):
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            if amt <= 0:
                continue

            dist = ((mid - curr_px) / curr_px * 100.0) if curr_px > 0 else 0.0
            is_above = mid >= curr_px
            liq_type = "[bright_red]SHORT SQUEEZE[/bright_red]" if is_above else "[bright_green]LONG CASCADE[/bright_green]"
            bar_color = "bright_red" if is_above else "bright_green"

            bar_len = int((amt / max_amt) * 30)
            bar = "█" * max(1, bar_len)

            table.add_row(
                f"${b.get('min_px', 0.0):,.1f} - ${b.get('max_px', 0.0):,.1f}",
                f"{dist:+.1f}%",
                liq_type,
                f"[{bar_color}]{bar}[/{bar_color}]",
                f"${amt:,.0f}"
            )

        subtitle = f"TOTAL LONG LIQUIDATION RISK: {long_size:,.1f} {self.current_coin}  |  TOTAL SHORT LIQUIDATION RISK: {short_size:,.1f} {self.current_coin}"
        return Panel(table, subtitle=subtitle, style="bright_magenta", border_style="magenta", box=box.ROUNDED)

    def render_stops(self) -> Panel:
        """Render Live Stop-Loss Clusters & Microstructure Trigger Levels."""
        data = self.cached_stops
        if not data:
            try:
                curr_px = self.cached_asset_info.get("mark_px", 100.0)
                data = self.client.fetch_stops(self.current_coin, curr_px * 0.80, curr_px * 1.20)
                self.cached_stops = data
            except Exception as e:
                return Panel(f"[bold red]Stops data unavailable: {e}[/bold red]", border_style="red")

        buy_stops = data.get("total_buy_size", 0.0)
        sell_stops = data.get("total_sell_size", 0.0)
        curr_px = data.get("current_price", self.cached_asset_info.get("mark_px", 0.0))

        table = Table(title=f"STOP-LOSS CLUSTERS & INSTITUTIONAL TRIGGER POOLS - {self.current_coin}", box=box.SIMPLE_HEAD, expand=True)
        table.add_column("Price Range (USD)", style="bold", ratio=2)
        table.add_column("Distance %", justify="right", ratio=1)
        table.add_column("Side", justify="center", ratio=1)
        table.add_column("Stop Density", ratio=4)
        table.add_column("Volume", justify="right", ratio=2)

        bands = data.get("bands", [])
        max_amt = max([b.get("amount", 0.0) for b in bands] + [1.0])

        for b in sorted(bands, key=lambda x: x.get("mid_px", 0.0), reverse=True):
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            if amt <= 0:
                continue

            dist = ((mid - curr_px) / curr_px * 100.0) if curr_px > 0 else 0.0
            is_above = mid >= curr_px
            side_badge = "[bright_cyan]BUY STOPS[/bright_cyan]" if is_above else "[bright_yellow]SELL STOPS[/bright_yellow]"
            bar_color = "bright_cyan" if is_above else "bright_yellow"

            bar_len = int((amt / max_amt) * 30)
            bar = "█" * max(1, bar_len)

            table.add_row(
                f"${b.get('min_px', 0.0):,.1f} - ${b.get('max_px', 0.0):,.1f}",
                f"{dist:+.1f}%",
                side_badge,
                f"[{bar_color}]{bar}[/{bar_color}]",
                f"${amt:,.0f}"
            )

        subtitle = f"TOTAL BUY STOPS (BREAKOUT TRIGGER): {buy_stops:,.1f}  |  TOTAL SELL STOPS (BREAKDOWN TRIGGER): {sell_stops:,.1f}"
        return Panel(table, subtitle=subtitle, style="bright_yellow", border_style="yellow", box=box.ROUNDED)

    def render_trades(self) -> Panel:
        """Render Real-Time Live Trades Tape with Aggressor Side & Whale Alerts."""
        trades = self.cached_trades
        if not trades:
            try:
                trades = self.client.fetch_recent_trades(self.current_coin)
                self.cached_trades = trades
            except Exception as e:
                return Panel(f"[bold red]Trades tape unavailable: {e}[/bold red]", border_style="red")

        table = Table(title=f"LIVE TICKER TAPE (REAL-TIME AGGRESSOR PRINTS) - {self.current_coin}", box=box.SIMPLE_HEAD, expand=True)
        table.add_column("Time (UTC)", style="dim white")
        table.add_column("Side", justify="center")
        table.add_column("Execution Price", justify="right", style="bold")
        table.add_column("Size", justify="right")
        table.add_column("Notional Value (USD)", justify="right")
        table.add_column("Alert", justify="center")

        for t in trades[:25]:
            ts = t.get("time", int(time.time() * 1000))
            time_str = datetime.datetime.fromtimestamp(ts / 1000.0, datetime.timezone.utc).strftime("%H:%M:%S.%f")[:-3]
            side = t.get("side", "B")
            is_buy = (side == "B")
            side_label = "[bold bright_green]BUY[/bold bright_green]" if is_buy else "[bold bright_red]SELL[/bold bright_red]"
            color = "bright_green" if is_buy else "bright_red"

            px = float(t.get("px", 0.0))
            sz = float(t.get("sz", 0.0))
            notional = px * sz

            alert = "[bold bright_yellow]🐋 WHALE[/bold bright_yellow]" if notional >= 50000 else (
                "[bold cyan]🦈 SHARK[/bold cyan]" if notional >= 15000 else ""
            )

            table.add_row(
                time_str,
                side_label,
                f"[{color}]${px:,.2f}[/{color}]",
                f"{sz:.4f}",
                f"${notional:,.0f}",
                alert
            )

        return Panel(table, subtitle=f"Streamed {len(trades)} live executions from Hyperliquid matching engine", style="bright_white", border_style="blue", box=box.ROUNDED)

    def render_universe_matrix(self) -> Panel:
        """Render 234-Coin Asset Screener sorted by Volume and 24h Performance."""
        if not self.all_assets:
            self.refresh_universe()

        table = Table(title="ASSET UNIVERSE SCREENER (TOP PERPETUAL MARKETS)", box=box.SIMPLE_HEAD, expand=True)
        table.add_column("Rank", justify="center", style="dim")
        table.add_column("Asset", style="bold bright_cyan")
        table.add_column("Mark Price", justify="right")
        table.add_column("24h Change", justify="right")
        table.add_column("24h Volume (USD)", justify="right", style="bright_yellow")
        table.add_column("Open Interest (USD)", justify="right", style="bright_magenta")
        table.add_column("Funding APR", justify="right")
        table.add_column("Max Lev", justify="center")

        for idx, a in enumerate(self.all_assets[:24], 1):
            chg = a.get("change_24h", 0.0)
            chg_col = "bright_green" if chg >= 0 else "bright_red"
            chg_sign = "+" if chg >= 0 else ""
            fund = a.get("funding_annualized", 0.0)
            fund_col = "bright_cyan" if fund >= 0 else "bright_magenta"

            # Highlight currently selected coin
            is_active = (a.get("coin") == self.current_coin)
            asset_label = f"[bold black on bright_yellow] > {a['coin']} < [/]" if is_active else f"[bold]{a['coin']}[/]"

            table.add_row(
                str(idx),
                asset_label,
                f"${a.get('mark_px', 0.0):,.2f}",
                f"[{chg_col}]{chg_sign}{chg:.2f}%[/{chg_col}]",
                f"${a.get('volume_24h', 0.0):,.0f}",
                f"${a.get('open_interest_usd', 0.0):,.0f}",
                f"[{fund_col}]{fund:+.2f}%[/{fund_col}]",
                f"{a.get('max_leverage', 50)}x"
            )

        subtitle = f"Showing Top 24 of {len(self.all_assets)} Active Perpetual Assets  |  Press [S] to switch or [←/→] to cycle"
        return Panel(table, subtitle=subtitle, style="cyan", border_style="cyan", box=box.ROUNDED)

    def interactive_switch_modal(self):
        """Prompt to switch asset smoothly without breaking continuous stream."""
        console.clear()
        console.print(Panel(
            "[bold bright_cyan]LIVE ASSET SWITCHER[/bold bright_cyan]\n\n"
            f"Current Asset: [bold yellow]{self.current_coin}[/bold yellow]\n"
            f"Watchlist: [dim cyan]{', '.join(self.watchlist)}[/dim cyan]\n\n"
            "Enter any coin symbol (e.g. [bold green]BTC, ETH, SOL, DOGE, XRP, SUI, LINK, AVAX, NEAR, OP[/bold green]) "
            "or press Enter to cancel:",
            style="cyan",
            border_style="cyan",
            box=box.ROUNDED
        ))
        try:
            choice = input("\nTarget Symbol > ").strip().upper()
            if choice:
                success = self.switch_asset(choice)
                if not success:
                    console.print(f"[bold red]Symbol '{choice}' not found in active universe.[/bold red]")
                    time.sleep(1.0)
        except Exception:
            pass

    def interactive_download_modal(self):
        """Interactive Historical Data Downloader."""
        console.clear()
        console.print(Panel(f"[bold bright_cyan]HISTORICAL DATA DOWNLOADER - {self.current_coin}[/bold bright_cyan]", style="cyan", box=box.ROUNDED))
        try:
            interval = Prompt.ask("Select timeframe", choices=["1m", "5m", "15m", "1h", "4h", "1d"], default="15m")
            days = int(Prompt.ask("Enter lookback days", default="30"))

            console.print(f"\n[cyan]Starting download for {self.current_coin} ({interval}, {days} days)...[/cyan]")
            c_file = self.client.download_historical_candles(self.current_coin, interval=interval, days=days, output_dir="Data/Hyperdash_Historical")
            f_file = self.client.download_historical_funding(self.current_coin, days=days, output_dir="Data/Hyperdash_Historical")
            console.print(f"[bold bright_green]Success! Files saved:\n- {c_file}\n- {f_file}[/bold bright_green]")
        except Exception as e:
            console.print(f"[bold red]Download failed: {e}[/bold red]")

        try:
            input("\nPress Enter to return to Live Terminal...")
        except Exception:
            pass

    def render_screen(self):
        """Render the complete composite terminal view."""
        header = self.render_header()
        
        if self.active_tab == "1":
            body = self.render_l2_orderbook()
        elif self.active_tab == "2":
            body = self.render_l3_orders()
        elif self.active_tab == "3":
            body = self.render_liquidations()
        elif self.active_tab == "4":
            body = self.render_stops()
        elif self.active_tab == "5":
            body = self.render_trades()
        elif self.active_tab == "6":
            body = self.render_universe_matrix()
        else:
            body = self.render_l2_orderbook()

        console.clear()
        console.print(header)
        console.print(body)

    def run(self):
        """
        Continuous Live Stream Loop.
        Non-blocking keyboard interaction via msvcrt (Windows).
        Updates prices, orders, and orderbook live every tick.
        """
        console.clear()
        console.print("[bold bright_cyan]Initializing Hyperdash Institutional Live Terminal...[/bold bright_cyan]")
        self.refresh_universe()
        self.fetch_live_tick()
        self.render_screen()

        last_tick_time = time.time()

        while True:
            try:
                # 1. Non-blocking Keyboard Event Polling
                if HAS_MSVCRT and msvcrt.kbhit():
                    ch = msvcrt.getch()
                    # Handle special/arrow keys
                    if ch in (b'\x00', b'\xe0'):
                        arrow = msvcrt.getch()
                        if arrow == b'K':  # Left arrow -> Cycle back
                            self.cycle_watchlist(-1)
                            self.fetch_live_tick()
                            self.render_screen()
                            continue
                        elif arrow == b'M':  # Right arrow -> Cycle forward
                            self.cycle_watchlist(1)
                            self.fetch_live_tick()
                            self.render_screen()
                            continue
                        elif arrow == b'H':  # Up arrow -> Increase depth
                            self.depth_levels = min(30, self.depth_levels + 2)
                            self.render_screen()
                            continue
                        elif arrow == b'P':  # Down arrow -> Decrease depth
                            self.depth_levels = max(8, self.depth_levels - 2)
                            self.render_screen()
                            continue

                    key = ch.decode("utf-8", errors="ignore").upper()

                    if key == "Q" or ch == b'\x1b' or ch == b'\x03':  # 'Q', ESC, or Ctrl+C
                        console.clear()
                        console.print("[bold bright_yellow]Hyperdash Terminal shutdown cleanly. Happy Trading![/bold bright_yellow]")
                        break
                    elif key in ["1", "2", "3", "4", "5", "6"]:
                        self.active_tab = key
                        self.fetch_live_tick()
                        self.render_screen()
                    elif key == "S":
                        self.interactive_switch_modal()
                        self.fetch_live_tick()
                        self.render_screen()
                    elif key in ["[", ","]:
                        self.cycle_watchlist(-1)
                        self.fetch_live_tick()
                        self.render_screen()
                    elif key in ["]", "."]:
                        self.cycle_watchlist(1)
                        self.fetch_live_tick()
                        self.render_screen()
                    elif key in ["+", "="]:
                        self.depth_levels = min(30, self.depth_levels + 2)
                        self.render_screen()
                    elif key in ["-", "_"]:
                        self.depth_levels = max(8, self.depth_levels - 2)
                        self.render_screen()
                    elif key == " ":
                        self.is_paused = not self.is_paused
                        self.render_screen()
                    elif key == "D":
                        self.interactive_download_modal()
                        self.fetch_live_tick()
                        self.render_screen()
                    elif key == "R":
                        self.refresh_universe()
                        self.fetch_live_tick()
                        self.render_screen()

                # 2. Live Tick Timer (Periodic auto-refresh)
                now = time.time()
                if not self.is_paused and (now - last_tick_time >= self.refresh_interval):
                    self.fetch_live_tick()
                    self.render_screen()
                    last_tick_time = now

                # Micro-sleep to keep CPU at ~0%
                time.sleep(0.05)

            except KeyboardInterrupt:
                console.clear()
                console.print("[bold bright_yellow]Terminal closed by user interrupt. Goodbye![/bold bright_yellow]")
                break
            except Exception as e:
                self.status_msg = f"LOOP RECOVER: {str(e)[:30]}"
                time.sleep(0.5)

if __name__ == "__main__":
    initial_coin = sys.argv[1].upper() if len(sys.argv) > 1 else "BTC"
    terminal = HyperdashTerminal(default_coin=initial_coin)
    terminal.run()
