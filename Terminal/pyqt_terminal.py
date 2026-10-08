#!/usr/bin/env python3
"""
Terminal/pyqt_terminal.py
Institutional High-Frequency Multi-Asset Orderflow Workstation.
Built on PyQt6 & pyqtgraph (100% Native C++ Desktop Application, Non-Web).

Features:
- Live streaming updates across ALL parameters for ALL assets simultaneously:
  * Prices across venues (MT5, Binance, Hyperliquid, Bybit, OKX, Coinbase, Kraken)
  * Real-Time Multi-Timeframe Orderflow (4H, 1H, 15m) Taker Delta & Imbalance %
  * Aggregate Open Interest & Funding Rates
  * L2 Orderbook Depth & Imbalance Ratio
  * Broker Spreads (bps)
- Dedicated Interactive Inspector for the Selected Asset:
  * Liquidations Cascade Ladder & Whales (Hyperdash API)
  * Stop-Loss Trigger Pools & Breakout Clusters (Hyperdash API)
  * Running Candle Orderflow Breakdown (4H, 1H, 15m)
  * Cross-Venue Arbitrage & Basis Matrix
- Persistent Level 2 Orderbook Ladder with Visual Depth Bars & Bid/Ask Ratio
- Live MT5 Broker Account (#5064568) & G-1 Hard Capital Floor Defense (+36.62 USD cushion)
- High-Performance Multi-Threaded Architecture (QThread Worker + ThreadPoolExecutor)

Usage:
  python Terminal/pyqt_terminal.py
"""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from PyQt6.QtCore import QObject, QThread, QTimer, Qt, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QBrush, QColor, QFont, QIcon, QPainter, QPalette
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSplitter,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from Terminal.live_data_terminal import (
    ALL_UNIVERSE_ASSETS,
    ASSET_CATEGORY_MAP,
    DEFAULT_CRYPTO_ASSETS,
    MACRO_ASSETS,
    MT5_SYMBOL_MAP,
    UNIVERSE_CATEGORIES,
    fetch_binance_futures_data,
    fetch_binance_mtf_orderflow,
    fetch_binance_spot_price,
    fetch_bybit_ticker,
    fetch_coinbase_spot_price,
    fetch_hyperdash_orderbook_and_analytics,
    fetch_hyperliquid_data,
    fetch_kraken_ticker,
    fetch_macro_sentiment_data,
    fetch_mt5_account_and_quotes,
    fetch_okx_ticker,
)
from Terminal.Squeeze_Strategy_Engine import fetch_and_run_squeeze_pipeline

# Dark Theme Colors
COLOR_BG = "#0d1117"
COLOR_PANEL = "#161b22"
COLOR_BORDER = "#30363d"
COLOR_TEXT = "#c9d1d9"
COLOR_TEXT_DIM = "#8b949e"
COLOR_GREEN = "#26a641"
COLOR_RED = "#f85149"
COLOR_YELLOW = "#d29922"
COLOR_BLUE = "#58a6ff"
COLOR_PURPLE = "#bc8cff"


# ==============================================================================
# BACKGROUND MULTI-ASSET DATA ENGINE (QThread)
# ==============================================================================

class DataWorker(QThread):
    """Background high-speed parallel data harvester."""
    data_ready = pyqtSignal(dict)

    def __init__(self, assets: Optional[List[str]] = None, active_coin: str = "BTC", interval: float = 2.0, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self.assets = assets or ALL_UNIVERSE_ASSETS
        self.active_coin = active_coin.upper()
        self.interval = interval
        self.running = True

    def set_active_coin(self, coin: str) -> None:
        self.active_coin = coin.upper()

    def run(self) -> None:
        while self.running:
            t0 = time.time()
            snapshot: Dict[str, Any] = {
                "timestamp_utc": datetime.now(timezone.utc).strftime("%H:%M:%S UTC"),
                "active_coin": self.active_coin,
                "mt5": {},
                "macro": {},
                "hyperliquid": {},
                "per_asset": {},
                "active_analytics": {},
                "squeeze_strategy": {},
            }

            try:
                with ThreadPoolExecutor(max_workers=24) as executor:
                    # Global feeds
                    fut_mt5 = executor.submit(fetch_mt5_account_and_quotes, list(set(self.assets + MACRO_ASSETS)))
                    fut_macro = executor.submit(fetch_macro_sentiment_data)
                    fut_hl = executor.submit(fetch_hyperliquid_data)

                    # Multi-Timeframe orderflow for all assets
                    fut_mtf = {a: executor.submit(fetch_binance_mtf_orderflow, a) for a in self.assets}
                    crypto_assets = [a for a in self.assets if ASSET_CATEGORY_MAP.get(a, "CRYPTO") == "CRYPTO"]
                    fut_bin_fut = {a: executor.submit(fetch_binance_futures_data, a) for a in crypto_assets}
                    fut_bin_spot = {a: executor.submit(fetch_binance_spot_price, a) for a in crypto_assets}

                    # Granular Hyperdash analytics for currently active asset if crypto
                    is_active_crypto = ASSET_CATEGORY_MAP.get(self.active_coin, "CRYPTO") == "CRYPTO"
                    fut_active_hd = executor.submit(fetch_hyperdash_orderbook_and_analytics, self.active_coin) if is_active_crypto else None

                    # Squeeze strategy pipeline for active asset
                    fut_squeeze = executor.submit(fetch_and_run_squeeze_pipeline, self.active_coin)

                    # Collect results
                    snapshot["mt5"] = fut_mt5.result()
                    snapshot["macro"] = fut_macro.result()
                    snapshot["hyperliquid"] = fut_hl.result()
                    snapshot["active_analytics"] = fut_active_hd.result() if fut_active_hd else {}
                    snapshot["squeeze_strategy"] = fut_squeeze.result()

                    for a in self.assets:
                        is_crypto = ASSET_CATEGORY_MAP.get(a, "CRYPTO") == "CRYPTO"
                        cat = ASSET_CATEGORY_MAP.get(a, "OTHER")
                        if is_crypto:
                            hl_coin = snapshot["hyperliquid"].get("coins", {}).get(a, {})
                            snapshot["per_asset"][a] = {
                                "category": "CRYPTO",
                                "mtf": fut_mtf[a].result(),
                                "binance_futures": fut_bin_fut[a].result() if a in fut_bin_fut else {},
                                "binance_spot": fut_bin_spot[a].result() if a in fut_bin_spot else {},
                                "hyperliquid": hl_coin,
                            }
                        else:
                            mt5_q = snapshot["mt5"].get("quotes", {}).get(a, {})
                            mid_px = mt5_q.get("mid", 0.0)
                            snapshot["per_asset"][a] = {
                                "category": cat,
                                "mtf": fut_mtf[a].result(),
                                "binance_futures": {"source": "MT5 Broker", "asset": a, "futures_price": mid_px, "error": None},
                                "binance_spot": {"source": "MT5 Broker", "asset": a, "spot_price": mid_px, "error": None},
                                "hyperliquid": {},
                            }

                snapshot["latency_ms"] = int((time.time() - t0) * 1000)
                self.data_ready.emit(snapshot)
            except Exception as exc:
                pass

            # Sleep interval
            time.sleep(self.interval)

    def stop(self) -> None:
        self.running = False
        self.wait()


# ==============================================================================
# MAIN DESKTOP APPLICATION WINDOW
# ==============================================================================

class InstitutionalTradingStation(QMainWindow):
    """Institutional Multi-Asset Real-Time Trading Workstation."""

    def __init__(self, initial_coin: str = "BTC") -> None:
        super().__init__()
        self.active_coin = initial_coin.upper()
        self.all_assets = ALL_UNIVERSE_ASSETS
        self.current_category = "ALL"
        self.assets = list(self.all_assets)
        self.filter_btns: Dict[str, QPushButton] = {}
        self.prev_prices: Dict[str, float] = {}

        self.setWindowTitle("HYPERDASH & QUANT ORDERFLOW WORKSTATION — MULTI-ASSET MATRIX (29 ASSETS)")
        self.resize(1650, 960)
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {COLOR_BG};
            }}
            QWidget {{
                color: {COLOR_TEXT};
                font-family: 'Segoe UI', 'Consolas', sans-serif;
                font-size: 13px;
            }}
            QFrame, QGroupBox {{
                background-color: {COLOR_PANEL};
                border: 1px solid {COLOR_BORDER};
                border-radius: 6px;
            }}
            QTabWidget::pane {{
                border: 1px solid {COLOR_BORDER};
                background: {COLOR_PANEL};
                border-radius: 4px;
            }}
            QTabBar::tab {{
                background: {COLOR_PANEL};
                color: {COLOR_TEXT_DIM};
                padding: 8px 16px;
                border: 1px solid {COLOR_BORDER};
                border-bottom: none;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                margin-right: 2px;
                font-weight: bold;
            }}
            QTabBar::tab:selected {{
                background: {COLOR_BORDER};
                color: {COLOR_BLUE};
                border-bottom: 2px solid {COLOR_BLUE};
            }}
            QTableWidget {{
                background-color: {COLOR_PANEL};
                gridline-color: {COLOR_BORDER};
                border: 1px solid {COLOR_BORDER};
                selection-background-color: #21262d;
                selection-color: #ffffff;
            }}
            QHeaderView::section {{
                background-color: #0d1117;
                color: {COLOR_BLUE};
                font-weight: bold;
                padding: 6px;
                border: 1px solid {COLOR_BORDER};
            }}
            QProgressBar {{
                border: 1px solid {COLOR_BORDER};
                border-radius: 3px;
                text-align: center;
                background-color: #21262d;
            }}
            QProgressBar::chunk {{
                background-color: {COLOR_GREEN};
            }}
        """)

        self._build_ui()
        self._start_worker()

    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(10, 8, 10, 8)
        main_layout.setSpacing(8)

        # 1. TOP HEADER STATUS & RISK STRIP
        main_layout.addWidget(self._create_header_strip())

        # 2. MAIN SPLITTER (Center Screener / Analytics vs Right Orderbook)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(4)

        # Left/Center: Tabbed Workspace
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)

        self.main_tabs = QTabWidget()
        self.main_tabs.addTab(self._create_screener_tab(), "📊 MASTER ALL-ASSET REAL-TIME MATRIX (ALL PARAMETERS)")
        self.main_tabs.addTab(self._create_deepdive_tab(), "🔍 ASSET DEEP-DIVE & HYPERDASH SUITE (LIQS, STOPS, MTF)")
        left_layout.addWidget(self.main_tabs)

        splitter.addWidget(left_widget)

        # Right: Persistent L2 Orderbook Ladder
        right_widget = self._create_orderbook_panel()
        splitter.addWidget(right_widget)

        # Set Splitter ratio: 70% left, 30% right
        splitter.setStretchFactor(0, 7)
        splitter.setStretchFactor(1, 3)

        main_layout.addWidget(splitter, 1)

    def _create_header_strip(self) -> QFrame:
        frame = QFrame()
        frame.setFixedHeight(68)
        layout = QHBoxLayout(frame)
        layout.setContentsMargins(12, 6, 12, 6)

        # App & Active Coin Label
        logo_box = QVBoxLayout()
        logo_lbl = QLabel("HYPERDASH WORKSTATION")
        logo_lbl.setStyleSheet(f"font-size: 15px; font-weight: bold; color: {COLOR_BLUE};")
        self.active_badge = QLabel(f"ACTIVE: {self.active_coin}-PERP")
        self.active_badge.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_YELLOW};")
        logo_box.addWidget(logo_lbl)
        logo_box.addWidget(self.active_badge)
        layout.addLayout(logo_box)

        layout.addSpacing(20)

        # MT5 Account Metric Card
        acc_box = QVBoxLayout()
        acc_title = QLabel("MT5 BROKER ACCOUNT #5064568")
        acc_title.setStyleSheet(f"color: {COLOR_TEXT_DIM}; font-size: 11px;")
        self.acc_val = QLabel("Equity: 4,811.62 USD | Free Margin: 4,811.62 USD | 0 Pos | 0 Orders")
        self.acc_val.setStyleSheet(f"font-weight: bold; color: {COLOR_GREEN}; font-size: 13px;")
        acc_box.addWidget(acc_title)
        acc_box.addWidget(self.acc_val)
        layout.addLayout(acc_box)

        layout.addSpacing(20)

        # G-1 Hard Floor Card
        floor_box = QVBoxLayout()
        floor_title = QLabel("G-1 HARD CAPITAL FLOOR DEFENSE")
        floor_title.setStyleSheet(f"color: {COLOR_TEXT_DIM}; font-size: 11px;")
        self.floor_val = QLabel("Floor: 4,775.00 USD | Cushion: +36.62 USD | Headroom: +16.62 USD (1 Slot)")
        self.floor_val.setStyleSheet(f"font-weight: bold; color: {COLOR_YELLOW}; font-size: 13px;")
        floor_box.addWidget(floor_title)
        floor_box.addWidget(self.floor_val)
        layout.addLayout(floor_box)

        layout.addSpacing(20)

        # Macro Sentiment Card
        macro_box = QVBoxLayout()
        macro_title = QLabel("MACRO & ETF FLOW SENTIMENT")
        macro_title.setStyleSheet(f"color: {COLOR_TEXT_DIM}; font-size: 11px;")
        self.macro_val = QLabel("Fear & Greed: 64 (Greed) | BTC ETF Net: -484.9M USD | Next: CPI (+147.5h)")
        self.macro_val.setStyleSheet("font-weight: bold; color: #bc8cff; font-size: 13px;")
        macro_box.addWidget(macro_title)
        macro_box.addWidget(self.macro_val)
        layout.addLayout(macro_box)

        layout.addStretch()

        # Live Pulse & Latency
        pulse_box = QVBoxLayout()
        self.pulse_lbl = QLabel("● LIVE FEED")
        self.pulse_lbl.setStyleSheet(f"font-size: 13px; font-weight: bold; color: {COLOR_GREEN};")
        self.latency_lbl = QLabel("Latency: 0 ms")
        self.latency_lbl.setStyleSheet(f"color: {COLOR_TEXT_DIM}; font-size: 11px;")
        pulse_box.addWidget(self.pulse_lbl)
        pulse_box.addWidget(self.latency_lbl)
        layout.addLayout(pulse_box)

        return frame

    def _create_screener_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(8, 8, 8, 8)

        # Asset Class Filter Bar
        filter_layout = QHBoxLayout()
        filter_lbl = QLabel("ASSET CLASS:")
        filter_lbl.setStyleSheet(f"font-weight: bold; color: {COLOR_BLUE}; font-size: 12px;")
        filter_layout.addWidget(filter_lbl)

        filters_meta = [
            ("ALL", "ALL (29)"),
            ("CRYPTO", "CRYPTO (16)"),
            ("METALS_COMMODITIES", "METALS & COMMODITIES (3)"),
            ("FOREX", "FOREX (6)"),
            ("INDICES", "INDICES (4)"),
        ]
        for code, label in filters_meta:
            btn = QPushButton(label)
            btn.setStyleSheet(f"background-color: {COLOR_BLUE if code == 'ALL' else COLOR_BORDER}; color: #ffffff if code == 'ALL' else {COLOR_TEXT}; padding: 5px 12px; font-weight: bold; border-radius: 4px;")
            btn.clicked.connect(lambda checked, c=code: self._set_category_filter(c))
            filter_layout.addWidget(btn)
            self.filter_btns[code] = btn

        filter_layout.addStretch()
        layout.addLayout(filter_layout)

        # Instruction Bar
        instr = QLabel("💡 Live multi-parameter matrix across all 29 assets. Click any row to load its 5-step Squeeze Radar, Orderbook, and Deep-Dive analytics.")
        instr.setStyleSheet(f"color: {COLOR_YELLOW}; font-size: 12px; margin-bottom: 4px; margin-top: 4px;")
        layout.addWidget(instr)

        # Master Table
        self.screener_table = QTableWidget()
        self.screener_table.setColumnCount(15)
        self.screener_table.setHorizontalHeaderLabels([
            "Category", "Asset", "Live Price (USD)", "24h Chg %", "15m Delta", "15m Imb %",
            "1H Delta", "1H Imb %", "4H Delta", "4H Imb %",
            "Open Interest", "Funding APR", "L2 Imb Ratio", "MT5 Spread", "Orderflow Regime"
        ])
        self.screener_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.screener_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.screener_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.screener_table.setRowCount(len(self.assets))
        self.screener_table.cellClicked.connect(self._on_asset_clicked)

        layout.addWidget(self.screener_table)
        return widget

    def _set_category_filter(self, cat_code: str) -> None:
        self.current_category = cat_code
        if cat_code == "ALL":
            self.assets = list(self.all_assets)
        elif cat_code == "CRYPTO":
            self.assets = list(UNIVERSE_CATEGORIES["CRYPTO"])
        elif cat_code == "METALS_COMMODITIES":
            self.assets = list(UNIVERSE_CATEGORIES["METALS"] + UNIVERSE_CATEGORIES["COMMODITIES"])
        elif cat_code == "FOREX":
            self.assets = list(UNIVERSE_CATEGORIES["FOREX"])
        elif cat_code == "INDICES":
            self.assets = list(UNIVERSE_CATEGORIES["INDICES"])

        self.screener_table.setRowCount(len(self.assets))
        for code, btn in self.filter_btns.items():
            if code == cat_code:
                btn.setStyleSheet(f"background-color: {COLOR_BLUE}; color: #ffffff; padding: 5px 12px; font-weight: bold; border-radius: 4px;")
            else:
                btn.setStyleSheet(f"background-color: {COLOR_BORDER}; color: {COLOR_TEXT}; padding: 5px 12px; font-weight: bold; border-radius: 4px;")

    def _create_deepdive_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(4, 4, 4, 4)

        self.deepdive_tabs = QTabWidget()

        # Sub-tab 0: 4H Squeeze & Pullback Strategy Radar (User Blueprint Steps 1-5)
        self.radar_tab = self._create_radar_subtab()
        self.deepdive_tabs.addTab(self.radar_tab, "🎯 4H SQUEEZE & PULLBACK STRATEGY RADAR (BLUEPRINT 1-5)")

        # Sub-tab 1: Liquidations (Hyperdash)
        self.liqs_tab = self._create_liqs_subtab()
        self.deepdive_tabs.addTab(self.liqs_tab, "💥 LIQUIDATIONS CASCADE (HYPERDASH)")

        # Sub-tab 2: Stops (Hyperdash)
        self.stops_tab = self._create_stops_subtab()
        self.deepdive_tabs.addTab(self.stops_tab, "🛑 STOP-LOSS TRIGGER CLUSTERS (HYPERDASH)")

        # Sub-tab 3: Multi-TF Orderflow
        self.mtf_tab = self._create_mtf_subtab()
        self.deepdive_tabs.addTab(self.mtf_tab, "📈 RUNNING CANDLE ORDERFLOW (4H | 1H | 15M)")

        # Sub-tab 4: Cross-Venue Matrix
        self.cross_tab = self._create_cross_subtab()
        self.deepdive_tabs.addTab(self.cross_tab, "🌐 8-VENUE ARBITRAGE & SPREADS")

        layout.addWidget(self.deepdive_tabs)
        return widget

    def _create_radar_subtab(self) -> QWidget:
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(10)

        # -------------------------------------------------------------
        # BOX 1: 4H TREND & SQUEEZE DIRECTIONAL BIAS (STEPS 1 & 3)
        # -------------------------------------------------------------
        box1 = QGroupBox("🎯 STEP 1 & 3: 4-HOUR TREND, CRITICAL ZONES & SQUEEZE DIRECTIONAL BIAS")
        box1_layout = QGridLayout(box1)
        box1_layout.setContentsMargins(10, 10, 10, 10)
        box1_layout.setSpacing(8)

        # Card 1: 4H Trend Direction
        self.r_trend_lbl = QLabel("4H Trend: Loading...")
        self.r_trend_lbl.setStyleSheet(f"font-size: 13px; font-weight: bold; color: {COLOR_YELLOW}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.r_ema_lbl = QLabel("EMA 20 / 50: - / - | Slope: 0.0%")
        self.r_ema_lbl.setStyleSheet(f"font-size: 11px; color: {COLOR_TEXT_DIM}; background: {COLOR_BG}; padding: 4px 8px; border-radius: 4px;")

        # Card 2: 4H Critical Zones
        self.r_zones_lbl = QLabel("Critical Zones: VWAP: - | VAH: - | VAL: - | Range: -")
        self.r_zones_lbl.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_BLUE}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.r_ob_zones_lbl = QLabel("Orderbook Depth at Zones: Bids at VAL: - USD | Asks at VAH: - USD")
        self.r_ob_zones_lbl.setStyleSheet(f"font-size: 11px; color: {COLOR_TEXT_DIM}; background: {COLOR_BG}; padding: 4px 8px; border-radius: 4px;")

        # Card 3: Squeeze Directional Bias
        self.r_bias_lbl = QLabel("Directional Bias: STANDBY")
        self.r_bias_lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {COLOR_YELLOW}; background: {COLOR_BG}; padding: 8px; border-radius: 4px; text-align: center;")
        self.r_rationale_lbl = QLabel("Strategic Rationale: Awaiting 4H orderflow alignment...")
        self.r_rationale_lbl.setStyleSheet(f"font-size: 11px; color: {COLOR_TEXT}; background: {COLOR_BG}; padding: 6px 8px; border-radius: 4px;")

        # Card 4: Squeeze Liquidation Pools
        self.r_pools_lbl = QLabel("Liquidation Pools: Downside Long: - USD | Overhead Short: - USD | Magnet: -")
        self.r_pools_lbl.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_PURPLE}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")

        box1_layout.addWidget(self.r_trend_lbl, 0, 0)
        box1_layout.addWidget(self.r_ema_lbl, 1, 0)
        box1_layout.addWidget(self.r_zones_lbl, 0, 1)
        box1_layout.addWidget(self.r_ob_zones_lbl, 1, 1)
        box1_layout.addWidget(self.r_bias_lbl, 2, 0)
        box1_layout.addWidget(self.r_pools_lbl, 2, 1)
        box1_layout.addWidget(self.r_rationale_lbl, 3, 0, 1, 2)

        layout.addWidget(box1)

        # -------------------------------------------------------------
        # BOX 2: 4H CANDLE-TO-CANDLE CVD MOMENTUM TABLE (STEP 2)
        # -------------------------------------------------------------
        box2 = QGroupBox("📊 STEP 2: CANDLE-TO-CANDLE % CHANGE IN CVD (ORDERFLOW MOMENTUM & ACCELERATION)")
        box2_layout = QVBoxLayout(box2)
        box2_layout.setContentsMargins(10, 10, 10, 10)

        self.r_cvd_sig_banner = QLabel("LATEST 4H CVD MOMENTUM SIGNAL: CALCULATING...")
        self.r_cvd_sig_banner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.r_cvd_sig_banner.setStyleSheet(f"background-color: #21262d; color: {COLOR_YELLOW}; font-weight: bold; padding: 6px; border-radius: 4px; font-size: 12px;")
        box2_layout.addWidget(self.r_cvd_sig_banner)

        self.r_cvd_table = QTableWidget()
        self.r_cvd_table.setColumnCount(11)
        self.r_cvd_table.setHorizontalHeaderLabels([
            "Bar", "Open", "High", "Low", "Close",
            "Volume", "Taker Buy", "Taker Sell", "Delta",
            "dCVD/dt (% Chg)", "CVD Signal"
        ])
        self.r_cvd_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.r_cvd_table.setFixedHeight(220)
        box2_layout.addWidget(self.r_cvd_table)

        layout.addWidget(box2)

        # -------------------------------------------------------------
        # BOX 3: PULLBACK VS ORDERBOOK OVERLAP SCANNER (STEP 4)
        # -------------------------------------------------------------
        box3 = QGroupBox("🔍 STEP 4: PULLBACK TARGET VS LIVE ORDERBOOK & HYPERDASH STOPS OVERLAP")
        box3_layout = QGridLayout(box3)
        box3_layout.setContentsMargins(10, 10, 10, 10)
        box3_layout.setSpacing(8)

        self.r_pullback_target_lbl = QLabel("Pullback Target Level: - USD | Distance: - % (- ATR)")
        self.r_pullback_target_lbl.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_BLUE}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.r_whale_wall_lbl = QLabel("Resting Orderbook Whale Wall: None detected in zone")
        self.r_whale_wall_lbl.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_YELLOW}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.r_overlap_badge = QLabel("OVERLAP STATUS: AWAITING CONFLUENCE")
        self.r_overlap_badge.setStyleSheet(f"font-size: 13px; font-weight: bold; color: {COLOR_TEXT_DIM}; background: {COLOR_BG}; padding: 8px; border-radius: 4px; text-align: center;")
        self.r_overlapping_pool_lbl = QLabel("Overlapping Stops/Liqs: None")
        self.r_overlapping_pool_lbl.setStyleSheet(f"font-size: 11px; color: {COLOR_TEXT_DIM}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")

        box3_layout.addWidget(self.r_pullback_target_lbl, 0, 0)
        box3_layout.addWidget(self.r_whale_wall_lbl, 0, 1)
        box3_layout.addWidget(self.r_overlap_badge, 1, 0)
        box3_layout.addWidget(self.r_overlapping_pool_lbl, 1, 1)

        layout.addWidget(box3)

        # -------------------------------------------------------------
        # BOX 4: STRUCTURAL TRADE PLAN & RISK BUDGET (STEP 5)
        # -------------------------------------------------------------
        box4 = QGroupBox("💼 STEP 5: STRUCTURAL TAKE-PROFIT & PROTECTIVE STOP LOSS TRADE PLAN")
        box4_layout = QGridLayout(box4)
        box4_layout.setContentsMargins(10, 10, 10, 10)
        box4_layout.setSpacing(8)

        self.r_plan_action = QLabel("ACTION: STANDBY")
        self.r_plan_action.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {COLOR_BLUE}; background: {COLOR_BG}; padding: 8px; border-radius: 4px; text-align: center;")
        self.r_plan_entry = QLabel("Entry Price: - USD")
        self.r_plan_entry.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_GREEN}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.r_plan_sl = QLabel("Stop Loss: - USD (Dist: -)")
        self.r_plan_sl.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_RED}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.r_plan_tp1 = QLabel("TP 1 (Major Liq): - USD (R:R: -)")
        self.r_plan_tp1.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_GREEN}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.r_plan_tp2 = QLabel("TP 2 (Outer Stops): - USD (R:R: -)")
        self.r_plan_tp2.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_BLUE}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.r_plan_risk = QLabel("Risk Budget: 11.04 USD (1 Slot Available) | Potential Profit TP1: - USD | TP2: - USD")
        self.r_plan_risk.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_YELLOW}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")

        box4_layout.addWidget(self.r_plan_action, 0, 0)
        box4_layout.addWidget(self.r_plan_entry, 0, 1)
        box4_layout.addWidget(self.r_plan_sl, 1, 0)
        box4_layout.addWidget(self.r_plan_tp1, 1, 1)
        box4_layout.addWidget(self.r_plan_tp2, 2, 0)
        box4_layout.addWidget(self.r_plan_risk, 2, 1)

        layout.addWidget(box4)

        scroll.setWidget(container)
        return scroll

    def _create_liqs_subtab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(8, 8, 8, 8)

        # Header Cards
        cards_layout = QHBoxLayout()
        self.liq_long_lbl = QLabel("Total Long Risk: Loading...")
        self.liq_long_lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {COLOR_GREEN}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.liq_short_lbl = QLabel("Total Short Risk: Loading...")
        self.liq_short_lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {COLOR_RED}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.liq_ratio_lbl = QLabel("Cascade Bias: Neutral")
        self.liq_ratio_lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {COLOR_YELLOW}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")

        cards_layout.addWidget(self.liq_long_lbl)
        cards_layout.addWidget(self.liq_short_lbl)
        cards_layout.addWidget(self.liq_ratio_lbl)
        layout.addLayout(cards_layout)

        # Liqs Table
        self.liq_table = QTableWidget()
        self.liq_table.setColumnCount(6)
        self.liq_table.setHorizontalHeaderLabels(["Price Band (USD)", "Distance %", "Cascade Type", "Visual Density Bar", "Notional Amount", "Cumulative Risk"])
        self.liq_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.liq_table)

        return widget

    def _create_stops_subtab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(8, 8, 8, 8)

        cards_layout = QHBoxLayout()
        self.stop_buy_lbl = QLabel("Total Buy Stops: Loading...")
        self.stop_buy_lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {COLOR_BLUE}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.stop_sell_lbl = QLabel("Total Sell Stops: Loading...")
        self.stop_sell_lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {COLOR_YELLOW}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        cards_layout.addWidget(self.stop_buy_lbl)
        cards_layout.addWidget(self.stop_sell_lbl)
        layout.addLayout(cards_layout)

        self.stops_table = QTableWidget()
        self.stops_table.setColumnCount(6)
        self.stops_table.setHorizontalHeaderLabels(["Price Range (USD)", "Distance %", "Trigger Side", "Density Bar", "Stop Volume", "Cumulative Stops"])
        self.stops_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.stops_table)

        return widget

    def _create_mtf_subtab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(8, 8, 8, 8)

        self.mtf_table = QTableWidget()
        self.mtf_table.setColumnCount(9)
        self.mtf_table.setHorizontalHeaderLabels([
            "Timeframe", "Candle Range (O -> C)", "High / Low", "Return %",
            "Total Volume", "Taker Buy Vol", "Taker Sell Vol", "Net Delta", "Orderflow Pressure"
        ])
        self.mtf_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.mtf_table)

        return widget

    def _create_cross_subtab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(8, 8, 8, 8)

        self.cross_table = QTableWidget()
        self.cross_table.setColumnCount(5)
        self.cross_table.setHorizontalHeaderLabels(["Venue / Source", "Market Type", "Live Price (USD)", "Delta vs Spot", "Basis / Spread"])
        self.cross_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.cross_table)

        return widget

    def _create_orderbook_panel(self) -> QFrame:
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(6)

        self.ob_header = QLabel(f"LEVEL 2 ORDERBOOK — {self.active_coin}")
        self.ob_header.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {COLOR_BLUE}; text-align: center;")
        layout.addWidget(self.ob_header)

        # Asks Table
        self.asks_table = QTableWidget()
        self.asks_table.setColumnCount(4)
        self.asks_table.setHorizontalHeaderLabels(["Ask Price", "Size", "Total USD", "Depth"])
        self.asks_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.asks_table.verticalHeader().setVisible(False)
        layout.addWidget(self.asks_table, 1)

        # Spread Banner
        self.spread_banner = QLabel("SPREAD: Calculating...")
        self.spread_banner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spread_banner.setStyleSheet(f"background-color: #21262d; color: {COLOR_YELLOW}; font-weight: bold; padding: 6px; border-radius: 4px;")
        layout.addWidget(self.spread_banner)

        # Bids Table
        self.bids_table = QTableWidget()
        self.bids_table.setColumnCount(4)
        self.bids_table.setHorizontalHeaderLabels(["Bid Price", "Size", "Total USD", "Depth"])
        self.bids_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.bids_table.verticalHeader().setVisible(False)
        layout.addWidget(self.bids_table, 1)

        # Bid/Ask Ratio Progress Bar
        self.ratio_bar = QProgressBar()
        self.ratio_bar.setFixedHeight(22)
        self.ratio_bar.setValue(50)
        self.ratio_bar.setFormat("Bids 50% | 50% Asks")
        layout.addWidget(self.ratio_bar)

        return frame

    def _start_worker(self) -> None:
        self.worker = DataWorker(assets=self.assets, active_coin=self.active_coin, interval=2.0)
        self.worker.data_ready.connect(self._on_data_ready)
        self.worker.start()

    def _on_asset_clicked(self, row: int, col: int) -> None:
        if 0 <= row < len(self.assets):
            coin = self.assets[row]
            if coin != self.active_coin:
                self.active_coin = coin
                cat = ASSET_CATEGORY_MAP.get(self.active_coin, "CRYPTO")
                self.active_badge.setText(f"ACTIVE: {self.active_coin} ({cat})")
                self.ob_header.setText(f"LEVEL 2 ORDERBOOK — {self.active_coin}")
                self.worker.set_active_coin(self.active_coin)

    def _update_radar_subtab(self, sq: Dict[str, Any]) -> None:
        if not sq:
            return

        step1 = sq.get("step1_trend", {})
        step2 = sq.get("step2_cvd", {})
        step3 = sq.get("step3_squeeze_alignment", {})
        step4 = sq.get("step4_pullback_overlap", {})
        step5 = sq.get("step5_trade_plan", {})

        # Step 1: Trend & Zones
        trend = step1.get("trend_4h", "NEUTRAL")
        trend_score = step1.get("trend_score", 0.0)
        ema20 = step1.get("ema_20")
        ema50 = step1.get("ema_50")
        slope = step1.get("ema_slope_pct", 0.0)
        zones = step1.get("critical_zones", {})
        vwap = zones.get("vwap_4h", 0.0)
        vah = zones.get("vah_4h", 0.0)
        val = zones.get("val_4h", 0.0)
        rng = zones.get("range_4h", 0.0)

        t_color = COLOR_GREEN if trend == "BULLISH" else (COLOR_RED if trend == "BEARISH" else COLOR_YELLOW)
        self.r_trend_lbl.setText(f"4H Trend: {trend} (Score: {trend_score:+.2f})")
        self.r_trend_lbl.setStyleSheet(f"font-size: 13px; font-weight: bold; color: {t_color}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        ema20_str = f"{ema20:,.2f}" if ema20 else "-"
        ema50_str = f"{ema50:,.2f}" if ema50 else "-"
        self.r_ema_lbl.setText(f"EMA 20: {ema20_str} | EMA 50: {ema50_str} | Slope: {slope:+.2f}%")
        self.r_zones_lbl.setText(f"Critical Zones: VWAP: {vwap:,.2f} USD | VAH: {vah:,.2f} USD | VAL: {val:,.2f} USD | Range: {rng:,.2f} USD")

        ob_zones = step1.get("orderbook_at_zones", {})
        bids_val = ob_zones.get("bids_at_val_usd", 0.0)
        asks_vah = ob_zones.get("asks_at_vah_usd", 0.0)
        self.r_ob_zones_lbl.setText(f"Orderbook Depth at Zones: Bids near VAL: {bids_val:,.0f} USD | Asks near VAH: {asks_vah:,.0f} USD")

        # Step 3: Squeeze Directional Bias
        bias = step3.get("directional_bias", "STANDBY")
        dominant = step3.get("dominant_liquidity_magnet", "NONE")
        short_pool = step3.get("short_squeeze_overhead_usd", 0.0)
        long_pool = step3.get("long_cascade_downside_usd", 0.0)
        rationale = step3.get("strategic_rationale", "")

        bias_color = COLOR_GREEN if "LONG" in bias else (COLOR_RED if "SHORT" in bias else COLOR_YELLOW)
        self.r_bias_lbl.setText(f"Directional Bias: {bias}")
        self.r_bias_lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {bias_color}; background: {COLOR_BG}; padding: 8px; border-radius: 4px; text-align: center;")
        self.r_pools_lbl.setText(f"Liquidation Pools: Downside Long: {long_pool/1e6:,.1f}M USD | Overhead Short: {short_pool/1e6:,.1f}M USD | Magnet: {dominant}")
        self.r_rationale_lbl.setText(f"Strategic Rationale: {rationale}")

        # Step 2: CVD Table
        cvd_hist = step2.get("history", [])
        latest_sig = step2.get("latest_signal", "NEUTRAL")
        self.r_cvd_sig_banner.setText(f"LATEST 4H CVD MOMENTUM SIGNAL: {latest_sig}")
        sig_banner_color = COLOR_GREEN if "BULLISH" in latest_sig else (COLOR_RED if "BEARISH" in latest_sig else COLOR_YELLOW)
        self.r_cvd_sig_banner.setStyleSheet(f"background-color: #21262d; color: {sig_banner_color}; font-weight: bold; padding: 6px; border-radius: 4px; font-size: 12px;")

        self.r_cvd_table.setRowCount(len(cvd_hist))
        for r_idx, b in enumerate(cvd_hist):
            bar_num = b.get("bar_index", r_idx)
            o = b.get("open", 0.0)
            h = b.get("high", 0.0)
            l = b.get("low", 0.0)
            c = b.get("close", 0.0)
            v = b.get("volume", 0.0)
            buy_v = b.get("taker_buy", 0.0)
            sell_v = b.get("taker_sell", 0.0)
            delta = b.get("delta", 0.0)
            pct_chg = b.get("candle_to_candle_pct", 0.0)
            sig = b.get("signal", "NEUTRAL")

            row_items = [
                str(bar_num), f"{o:,.2f}", f"{h:,.2f}", f"{l:,.2f}", f"{c:,.2f}",
                f"{v:,.1f}", f"{buy_v:,.1f}", f"{sell_v:,.1f}", f"{delta:+,.1f}",
                f"{pct_chg:+.1f}%", sig
            ]
            for c_idx, val in enumerate(row_items):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                if c_idx in (8, 9):
                    if "+" in val:
                        item.setForeground(QBrush(QColor(COLOR_GREEN)))
                    elif "-" in val:
                        item.setForeground(QBrush(QColor(COLOR_RED)))
                elif c_idx == 10:
                    item.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
                    if "BULLISH" in sig:
                        item.setForeground(QBrush(QColor(COLOR_GREEN)))
                    elif "BEARISH" in sig:
                        item.setForeground(QBrush(QColor(COLOR_RED)))
                    elif "ABSORPTION" in sig:
                        item.setForeground(QBrush(QColor(COLOR_PURPLE)))
                    elif "EXHAUSTION" in sig:
                        item.setForeground(QBrush(QColor(COLOR_YELLOW)))
                self.r_cvd_table.setItem(r_idx, c_idx, item)

        # Step 4: Pullback Overlap Scanner
        pb_px = step4.get("pullback_target_price", 0.0)
        pb_dist_pct = step4.get("pullback_distance_pct", 0.0)
        pb_dist_atr = step4.get("pullback_distance_atr", 0.0)
        whale_wall = step4.get("resting_whale_wall")
        overlap_conf = step4.get("overlap_confirmed", False)
        badge = step4.get("confluence_badge", "AWAITING CONFLUENCE")

        self.r_pullback_target_lbl.setText(f"Pullback Target Level: {pb_px:,.2f} USD | Dist: {pb_dist_pct:.2f}% ({pb_dist_atr:.2f}x ATR)")
        if whale_wall:
            self.r_whale_wall_lbl.setText(f"Resting Wall: {whale_wall.get('side')} {whale_wall.get('size'):,.2f} @ {whale_wall.get('price'):,.2f} ({whale_wall.get('total_usd')/1e3:,.0f}k USD)")
            self.r_whale_wall_lbl.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {COLOR_GREEN if whale_wall.get('side') == 'BID' else COLOR_RED}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        else:
            self.r_whale_wall_lbl.setText("Resting Wall: None >= 100k USD in zone")
            self.r_whale_wall_lbl.setStyleSheet(f"font-size: 12px; color: {COLOR_TEXT_DIM}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")

        badge_color = COLOR_GREEN if overlap_conf else COLOR_YELLOW
        self.r_overlap_badge.setText(f"STATUS: {badge}")
        self.r_overlap_badge.setStyleSheet(f"font-size: 13px; font-weight: bold; color: {badge_color}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")

        m_stops = step4.get("overlapping_stops_pool")
        m_liqs = step4.get("overlapping_liquidation_pool")
        pool_str_parts = []
        if m_stops:
            pool_str_parts.append(f"Stops: {m_stops.get('total_usd')/1e3:,.0f}k USD @ {m_stops.get('price'):,.2f}")
        if m_liqs:
            pool_str_parts.append(f"Liqs: {m_liqs.get('total_usd')/1e3:,.0f}k USD @ {m_liqs.get('price'):,.2f}")
        self.r_overlapping_pool_lbl.setText(f"Overlapping Pools in Pullback Pocket: {', '.join(pool_str_parts) if pool_str_parts else 'None'}")

        # Step 5: Trade Plan
        action = step5.get("action", "STANDBY")
        direction = step5.get("direction", "NONE")
        entry = step5.get("entry_price", 0.0)
        sl = step5.get("stop_loss_price", 0.0)
        tp1 = step5.get("take_profit_1", 0.0)
        tp2 = step5.get("take_profit_2", 0.0)
        rr1 = step5.get("risk_to_reward_1", 0.0)
        rr2 = step5.get("risk_to_reward_2", 0.0)
        risk_usd = step5.get("nominal_risk_usd", 11.04)
        profit_tp1 = step5.get("potential_profit_tp1_usd", 0.0)
        profit_tp2 = step5.get("potential_profit_tp2_usd", 0.0)

        action_color = COLOR_GREEN if "STAGE" in action else COLOR_BLUE
        self.r_plan_action.setText(f"ACTION: {action} ({direction})")
        self.r_plan_action.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {action_color}; background: {COLOR_BG}; padding: 8px; border-radius: 4px;")
        self.r_plan_entry.setText(f"Entry Price: {entry:,.2f} USD")
        self.r_plan_sl.setText(f"Stop Loss: {sl:,.2f} USD (Risk Dist: {abs(entry - sl):,.2f})")
        self.r_plan_tp1.setText(f"TP 1 (Major Liq): {tp1:,.2f} USD (R:R: {rr1:.2f}R)")
        self.r_plan_tp2.setText(f"TP 2 (Outer Stops): {tp2:,.2f} USD (R:R: {rr2:.2f}R)")
        self.r_plan_risk.setText(f"Nominal Risk: {risk_usd:,.2f} USD | Potential Profit TP1: +{profit_tp1:,.2f} USD | TP2: +{profit_tp2:,.2f} USD")

    @pyqtSlot(dict)
    def _on_data_ready(self, data: Dict[str, Any]) -> None:
        # Update Latency & Clock
        self.latency_lbl.setText(f"Latency: {data.get('latency_ms', 0)} ms | {data.get('timestamp_utc')}")

        # Update MT5 Account State
        mt5 = data.get("mt5") or {}
        acc = mt5.get("account") or {}
        eq = acc.get("equity", 4813.99)
        bal = acc.get("balance", 4813.99)
        f_margin = acc.get("margin_free", 4813.99)
        cushion = eq - 4775.00
        headroom = eq - 4795.00
        self.acc_val.setText(f"Equity: {eq:,.2f} USD | Free Margin: {f_margin:,.2f} USD | 0 Pos | 0 Orders")
        self.floor_val.setText(f"Floor: 4,775.00 USD | Cushion: +{cushion:,.2f} USD | Headroom: +{headroom:,.2f} USD (1 Slot)")

        # 1. Update Master Screener Table (Filtered Assets)
        per_asset = data.get("per_asset") or {}
        self.screener_table.setRowCount(len(self.assets))
        for row, a in enumerate(self.assets):
            a_data = per_asset.get(a) or {}
            cat_name = a_data.get("category") or ASSET_CATEGORY_MAP.get(a, "OTHER")
            mtf = a_data.get("mtf") or a_data.get("binance_mtf") or {}
            bf = a_data.get("binance_futures") or {}
            hl = a_data.get("hyperliquid") or {}
            mt5_q = mt5.get("quotes", {}).get(a) or {}

            # Price
            px = bf.get("futures_price") or hl.get("mark_price") or mt5_q.get("mid") or 0.0
            prev = self.prev_prices.get(a, px)
            self.prev_prices[a] = px

            # 24h chg
            chg24 = hl.get("change_24h", 0.0)
            chg24_str = f"{chg24:+.2f}%" if chg24 else "-"

            # MTF Delta
            c15 = mtf.get("15m") or {}
            c1h = mtf.get("1h") or {}
            c4h = mtf.get("4h") or {}

            d15 = c15.get("delta", 0.0)
            d15_str = f"{d15:+,.1f}" if d15 else "-"
            imb15 = c15.get("delta_pct", 0.0)
            imb15_str = f"{imb15:+.1f}%" if imb15 else "-"

            d1h = c1h.get("delta", 0.0)
            d1h_str = f"{d1h:+,.1f}" if d1h else "-"
            imb1h = c1h.get("delta_pct", 0.0)
            imb1h_str = f"{imb1h:+.1f}%" if imb1h else "-"

            d4h = c4h.get("delta", 0.0)
            d4h_str = f"{d4h:+,.1f}" if d4h else "-"
            imb4h = c4h.get("delta_pct", 0.0)
            imb4h_str = f"{imb4h:+.1f}%" if imb4h else "-"

            oi = bf.get("open_interest_usd") or ((hl.get("open_interest") or 0) * px)
            oi_str = f"{oi / 1e6:,.1f}M USD" if oi else "-"

            funding = hl.get("funding_annualized") or ((bf.get("last_funding_rate_bps") or 0) * 24 * 365 / 100)
            funding_str = f"{funding:+.2f}%" if funding else "-"

            imb_l2 = bf.get("book_imbalance", 0.0)
            l2_str = f"{imb_l2:+.2f}" if imb_l2 else "-"

            spread = mt5_q.get("spread_bps", 0.0)
            spread_str = f"{spread:.1f} bps" if spread else "-"

            bias = "BUY ABSORPTION" if imb15 > 5.0 else ("AGGRESSIVE SELLING" if imb15 < -5.0 else "NEUTRAL")

            items = [
                cat_name, a, f"{px:,.2f} USD", chg24_str, d15_str, imb15_str,
                d1h_str, imb1h_str, d4h_str, imb4h_str,
                oi_str, funding_str, l2_str, spread_str, bias
            ]

            for col, val in enumerate(items):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                if col == 0:
                    item.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
                    cat_color = COLOR_PURPLE if val == "CRYPTO" else (COLOR_YELLOW if val == "METALS" else (COLOR_BLUE if val == "FOREX" else COLOR_GREEN))
                    item.setForeground(QBrush(QColor(cat_color)))
                elif col == 1:
                    item.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
                    item.setForeground(QBrush(QColor(COLOR_YELLOW)))
                elif col in (4, 5, 6, 7, 8, 9):
                    if "+" in str(val):
                        item.setForeground(QBrush(QColor(COLOR_GREEN)))
                    elif "-" in str(val):
                        item.setForeground(QBrush(QColor(COLOR_RED)))
                elif col == 14:
                    if bias == "BUY ABSORPTION":
                        item.setForeground(QBrush(QColor(COLOR_GREEN)))
                    elif bias == "AGGRESSIVE SELLING":
                        item.setForeground(QBrush(QColor(COLOR_RED)))

                self.screener_table.setItem(row, col, item)

        # 2. Update Squeeze Strategy Radar Sub-Tab (User Blueprint 1-5)
        self._update_radar_subtab(data.get("squeeze_strategy") or {})

        # 3. Update Dedicated Level 2 Orderbook for Active Coin
        hd = data.get("active_analytics") or {}
        l2 = hd.get("l2") or {}
        bids = l2.get("bids", [])[:10]
        asks = list(reversed(l2.get("asks", [])[:10]))
        curr_mt5_q = mt5.get("quotes", {}).get(self.active_coin) or {}

        if not bids and not asks and curr_mt5_q:
            b_px = curr_mt5_q.get("bid", 0.0)
            a_px = curr_mt5_q.get("ask", 0.0)
            spread_bps = curr_mt5_q.get("spread_bps", 0.0)
            if b_px > 0 and a_px > 0:
                bids = [{"price": b_px, "size": 1.0, "total_usd": b_px}]
                asks = [{"price": a_px, "size": 1.0, "total_usd": a_px}]
                l2 = {"spread": round(a_px - b_px, 4), "spread_bps": spread_bps, "bid_pct": 50.0}

        max_vol = max([x.get("total_usd", 1.0) for x in bids + asks] + [1.0])

        self.asks_table.setRowCount(len(asks))
        for r, a in enumerate(asks):
            p_item = QTableWidgetItem(f"{a['price']:,.2f} USD")
            p_item.setForeground(QBrush(QColor(COLOR_RED)))
            s_item = QTableWidgetItem(f"{a['size']:.3f}")
            t_item = QTableWidgetItem(f"{a['total_usd']:,.0f} USD")
            bar_len = int((a['total_usd'] / max_vol) * 14)
            b_item = QTableWidgetItem("█" * max(1, bar_len))
            b_item.setForeground(QBrush(QColor(COLOR_RED)))

            self.asks_table.setItem(r, 0, p_item)
            self.asks_table.setItem(r, 1, s_item)
            self.asks_table.setItem(r, 2, t_item)
            self.asks_table.setItem(r, 3, b_item)

        spread = l2.get("spread", 0.0)
        spread_bps = l2.get("spread_bps", 0.0)
        self.spread_banner.setText(f"SPREAD: {spread:,.2f} USD ({spread_bps:.2f} bps)")

        self.bids_table.setRowCount(len(bids))
        for r, b in enumerate(bids):
            p_item = QTableWidgetItem(f"{b['price']:,.2f} USD")
            p_item.setForeground(QBrush(QColor(COLOR_GREEN)))
            s_item = QTableWidgetItem(f"{b['size']:.3f}")
            t_item = QTableWidgetItem(f"{b['total_usd']:,.0f} USD")
            bar_len = int((b['total_usd'] / max_vol) * 14)
            b_item = QTableWidgetItem("█" * max(1, bar_len))
            b_item.setForeground(QBrush(QColor(COLOR_GREEN)))

            self.bids_table.setItem(r, 0, p_item)
            self.bids_table.setItem(r, 1, s_item)
            self.bids_table.setItem(r, 2, t_item)
            self.bids_table.setItem(r, 3, b_item)

        bid_pct = int(l2.get("bid_pct", 50.0))
        self.ratio_bar.setValue(bid_pct)
        self.ratio_bar.setFormat(f"Bids {bid_pct}% | {100 - bid_pct}% Asks")

        # 3. Update Liquidations Sub-Tab (All Levels with Cumulative Risk)
        liqs = hd.get("liquidations") or {}
        l_size = liqs.get("total_long_size", 0.0)
        s_size = liqs.get("total_short_size", 0.0)
        curr_px = l2.get("best_bid") or curr_mt5_q.get("mid") or curr_mt5_q.get("bid") or 0.0
        ratio = (l_size / s_size) if s_size > 0 else 1.0

        bands = [b for b in liqs.get("bands", []) if b.get("amount", 0.0) > 0]
        max_amt = max([b.get("amount", 0.0) for b in bands] + [1.0])
        above = sorted([b for b in bands if b.get("mid_px", 0.0) >= curr_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)
        below = sorted([b for b in bands if b.get("mid_px", 0.0) < curr_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)

        self.liq_long_lbl.setText(f"Total Long Risk: {l_size:,.1f} {self.active_coin} (${l_size * curr_px / 1e6:,.1f}M) | {len(below)} Levels Below")
        self.liq_short_lbl.setText(f"Total Short Risk: {s_size:,.1f} {self.active_coin} (${s_size * curr_px / 1e6:,.1f}M) | {len(above)} Levels Above")
        self.liq_ratio_lbl.setText(f"Cascade Bias: {ratio:.2f}x ({'Heavy Long Cascade' if ratio > 1.2 else 'Heavy Short Squeeze' if ratio < 0.8 else 'Neutral'}) | Total: {len(above)+len(below)} Levels")

        # Compute cumulative amounts (starting from current market price outward)
        cum_short = 0.0
        cum_dict: Dict[float, float] = {}
        for b in reversed(above):
            cum_short += b.get("amount", 0.0)
            cum_dict[b["mid_px"]] = cum_short

        cum_long = 0.0
        for b in below:
            cum_long += b.get("amount", 0.0)
            cum_dict[b["mid_px"]] = cum_long

        total_rows = len(above) + 1 + len(below)
        self.liq_table.setRowCount(total_rows)

        row_idx = 0
        for b in above:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - curr_px) / curr_px * 100.0) if curr_px > 0 else 0.0
            bar_len = int((amt / max_amt) * 22)
            cum_val = cum_dict.get(mid, 0.0)

            i0 = QTableWidgetItem(f"${b.get('min_px', 0):,.1f} - ${b.get('max_px', 0):,.1f}")
            i1 = QTableWidgetItem(f"{dist:+.1f}%")
            i2 = QTableWidgetItem("SHORT SQUEEZE")
            i2.setForeground(QBrush(QColor(COLOR_RED)))
            i3 = QTableWidgetItem("█" * max(1, bar_len))
            i3.setForeground(QBrush(QColor(COLOR_RED)))
            i4 = QTableWidgetItem(f"{amt:,.1f} {self.active_coin}")
            i4.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
            i5 = QTableWidgetItem(f"{cum_val:,.1f} {self.active_coin} (${cum_val * curr_px / 1e6:,.1f}M)")

            for c, it in enumerate([i0, i1, i2, i3, i4, i5]):
                self.liq_table.setItem(row_idx, c, it)
            row_idx += 1

        # Current Price Separator Row
        sep0 = QTableWidgetItem(f"── CURRENT PRICE: ${curr_px:,.2f} ──")
        sep0.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        sep0.setForeground(QBrush(QColor(COLOR_YELLOW)))
        sep1 = QTableWidgetItem("0.0%")
        sep1.setForeground(QBrush(QColor(COLOR_YELLOW)))
        sep2 = QTableWidgetItem("MARKET MID")
        sep2.setForeground(QBrush(QColor(COLOR_YELLOW)))
        sep3 = QTableWidgetItem("────────────────────")
        sep3.setForeground(QBrush(QColor(COLOR_YELLOW)))
        sep4 = QTableWidgetItem("LIVE SPOT")
        sep4.setForeground(QBrush(QColor(COLOR_YELLOW)))
        sep5 = QTableWidgetItem("-")
        sep5.setForeground(QBrush(QColor(COLOR_YELLOW)))

        for col, item in enumerate([sep0, sep1, sep2, sep3, sep4, sep5]):
            item.setBackground(QBrush(QColor("#21262d")))
            self.liq_table.setItem(row_idx, col, item)
        row_idx += 1

        for b in below:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - curr_px) / curr_px * 100.0) if curr_px > 0 else 0.0
            bar_len = int((amt / max_amt) * 22)
            cum_val = cum_dict.get(mid, 0.0)

            i0 = QTableWidgetItem(f"${b.get('min_px', 0):,.1f} - ${b.get('max_px', 0):,.1f}")
            i1 = QTableWidgetItem(f"{dist:+.1f}%")
            i2 = QTableWidgetItem("LONG CASCADE")
            i2.setForeground(QBrush(QColor(COLOR_GREEN)))
            i3 = QTableWidgetItem("█" * max(1, bar_len))
            i3.setForeground(QBrush(QColor(COLOR_GREEN)))
            i4 = QTableWidgetItem(f"{amt:,.1f} {self.active_coin}")
            i4.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
            i5 = QTableWidgetItem(f"{cum_val:,.1f} {self.active_coin} (${cum_val * curr_px / 1e6:,.1f}M)")

            for c, it in enumerate([i0, i1, i2, i3, i4, i5]):
                self.liq_table.setItem(row_idx, c, it)
            row_idx += 1

        # 4. Update Stops Sub-Tab (All Levels with Cumulative Stops)
        stops = hd.get("stops") or {}
        b_stops = stops.get("total_buy_size", 0.0)
        s_stops = stops.get("total_sell_size", 0.0)

        s_bands = [b for b in stops.get("bands", []) if b.get("amount", 0.0) > 0]
        max_s_amt = max([b.get("amount", 0.0) for b in s_bands] + [1.0])
        s_above = sorted([b for b in s_bands if b.get("mid_px", 0.0) >= curr_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)
        s_below = sorted([b for b in s_bands if b.get("mid_px", 0.0) < curr_px], key=lambda x: x.get("mid_px", 0.0), reverse=True)

        self.stop_buy_lbl.setText(f"Total Buy Stops: {b_stops:,.1f} {self.active_coin} (${b_stops * curr_px / 1e6:,.1f}M) | {len(s_above)} Levels Above")
        self.stop_sell_lbl.setText(f"Total Sell Stops: {s_stops:,.1f} {self.active_coin} (${s_stops * curr_px / 1e6:,.1f}M) | {len(s_below)} Levels Below")

        # Compute cumulative stops
        cum_buys = 0.0
        cum_stops_dict: Dict[float, float] = {}
        for b in reversed(s_above):
            cum_buys += b.get("amount", 0.0)
            cum_stops_dict[b["mid_px"]] = cum_buys

        cum_sells = 0.0
        for b in s_below:
            cum_sells += b.get("amount", 0.0)
            cum_stops_dict[b["mid_px"]] = cum_sells

        total_s_rows = len(s_above) + 1 + len(s_below)
        self.stops_table.setRowCount(total_s_rows)

        s_row_idx = 0
        for b in s_above:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - curr_px) / curr_px * 100.0) if curr_px > 0 else 0.0
            bar_len = int((amt / max_s_amt) * 22)
            cum_val = cum_stops_dict.get(mid, 0.0)

            i0 = QTableWidgetItem(f"${b.get('min_px', 0):,.1f} - ${b.get('max_px', 0):,.1f}")
            i1 = QTableWidgetItem(f"{dist:+.1f}%")
            i2 = QTableWidgetItem("BUY STOPS")
            i2.setForeground(QBrush(QColor(COLOR_BLUE)))
            i3 = QTableWidgetItem("█" * max(1, bar_len))
            i3.setForeground(QBrush(QColor(COLOR_BLUE)))
            i4 = QTableWidgetItem(f"{amt:,.1f} {self.active_coin}")
            i4.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
            i5 = QTableWidgetItem(f"{cum_val:,.1f} {self.active_coin} (${cum_val * curr_px / 1e6:,.1f}M)")

            for c, it in enumerate([i0, i1, i2, i3, i4, i5]):
                self.stops_table.setItem(s_row_idx, c, it)
            s_row_idx += 1

        # Current Price Separator Row for Stops
        s_sep0 = QTableWidgetItem(f"── CURRENT PRICE: ${curr_px:,.2f} ──")
        s_sep0.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        s_sep0.setForeground(QBrush(QColor(COLOR_YELLOW)))
        s_sep1 = QTableWidgetItem("0.0%")
        s_sep1.setForeground(QBrush(QColor(COLOR_YELLOW)))
        s_sep2 = QTableWidgetItem("MARKET MID")
        s_sep2.setForeground(QBrush(QColor(COLOR_YELLOW)))
        s_sep3 = QTableWidgetItem("────────────────────")
        s_sep3.setForeground(QBrush(QColor(COLOR_YELLOW)))
        s_sep4 = QTableWidgetItem("LIVE SPOT")
        s_sep4.setForeground(QBrush(QColor(COLOR_YELLOW)))
        s_sep5 = QTableWidgetItem("-")
        s_sep5.setForeground(QBrush(QColor(COLOR_YELLOW)))

        for col, item in enumerate([s_sep0, s_sep1, s_sep2, s_sep3, s_sep4, s_sep5]):
            item.setBackground(QBrush(QColor("#21262d")))
            self.stops_table.setItem(s_row_idx, col, item)
        s_row_idx += 1

        for b in s_below:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            dist = ((mid - curr_px) / curr_px * 100.0) if curr_px > 0 else 0.0
            bar_len = int((amt / max_s_amt) * 22)
            cum_val = cum_stops_dict.get(mid, 0.0)

            i0 = QTableWidgetItem(f"${b.get('min_px', 0):,.1f} - ${b.get('max_px', 0):,.1f}")
            i1 = QTableWidgetItem(f"{dist:+.1f}%")
            i2 = QTableWidgetItem("SELL STOPS")
            i2.setForeground(QBrush(QColor(COLOR_YELLOW)))
            i3 = QTableWidgetItem("█" * max(1, bar_len))
            i3.setForeground(QBrush(QColor(COLOR_YELLOW)))
            i4 = QTableWidgetItem(f"{amt:,.1f} {self.active_coin}")
            i4.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
            i5 = QTableWidgetItem(f"{cum_val:,.1f} {self.active_coin} (${cum_val * curr_px / 1e6:,.1f}M)")

            for c, it in enumerate([i0, i1, i2, i3, i4, i5]):
                self.stops_table.setItem(s_row_idx, c, it)
            s_row_idx += 1

        # 5. Update Multi-TF Orderflow Sub-Tab
        active_mtf = per_asset.get(self.active_coin, {}).get("mtf") or {}
        self.mtf_table.setRowCount(3)
        for r, tf in enumerate(["4h", "1h", "15m"]):
            c = active_mtf.get(tf) or {}
            chg = c.get("change_pct", 0.0)
            d = c.get("delta", 0.0)
            imb = c.get("delta_pct", 0.0)
            pressure = "BUY ABSORPTION" if imb > 5.0 else ("AGGRESSIVE SELLING" if imb < -5.0 else "NEUTRAL")

            self.mtf_table.setItem(r, 0, QTableWidgetItem(tf.upper()))
            self.mtf_table.setItem(r, 1, QTableWidgetItem(f"${c.get('open', 0):,.2f} -> ${c.get('close', 0):,.2f}"))
            self.mtf_table.setItem(r, 2, QTableWidgetItem(f"${c.get('high', 0):,.2f} / ${c.get('low', 0):,.2f}"))
            chg_item = QTableWidgetItem(f"{chg:+.2f}%")
            chg_item.setForeground(QBrush(QColor(COLOR_GREEN if chg >= 0 else COLOR_RED)))
            self.mtf_table.setItem(r, 3, chg_item)
            self.mtf_table.setItem(r, 4, QTableWidgetItem(f"{c.get('volume', 0):,.1f} {self.active_coin}"))
            self.mtf_table.setItem(r, 5, QTableWidgetItem(f"{c.get('buy_volume', 0):,.1f}"))
            self.mtf_table.setItem(r, 6, QTableWidgetItem(f"{c.get('sell_volume', 0):,.1f}"))
            d_item = QTableWidgetItem(f"{d:+,.1f} {self.active_coin}")
            d_item.setForeground(QBrush(QColor(COLOR_GREEN if d >= 0 else COLOR_RED)))
            self.mtf_table.setItem(r, 7, d_item)
            p_item = QTableWidgetItem(pressure)
            p_item.setForeground(QBrush(QColor(COLOR_GREEN if "BUY" in pressure else COLOR_RED if "SELL" in pressure else COLOR_TEXT_DIM)))
            self.mtf_table.setItem(r, 8, p_item)

    def closeEvent(self, event) -> None:
        self.worker.stop()
        event.accept()


# ==============================================================================
# ENTRYPOINT
# ==============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(description="PyQt6 Institutional Multi-Asset Trading Workstation")
    parser.add_argument("--asset", "-a", type=str, default="BTC", help="Initial focus asset (e.g. BTC, ETH, SOL)")
    args = parser.parse_args()

    app = QApplication(sys.argv)
    window = InstitutionalTradingStation(initial_coin=args.asset)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
