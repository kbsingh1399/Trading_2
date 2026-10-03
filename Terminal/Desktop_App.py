"""
Engine/terminal/desktop_app.py
Interactive Native Desktop Trading Terminal for Arbitrary Parquet Data.
Features TradingView Lightweight Charts, ATAS Orderflow Delta/CVD, Reset View, Log Scale,
Dynamic Overlays, Subcharts, and Dimension Visualizer.
"""
from __future__ import annotations
import os
import sys

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import glob
from typing import List, Optional
import webview
from Terminal.Chart_Engine import ChartEngine
from Terminal.Data_Engine import ParquetDataEngine

DEFAULT_FOREX_FILE = os.path.join(PROJECT_ROOT, "Forex_Data", "USDCAD_15m_real.parquet")
DEFAULT_CRYPTO_FILE = os.path.join(PROJECT_ROOT, "Binance_Data", "BTC_15m_master_2020_2026.parquet")

class DesktopQuantTerminal:
    """Institutional-grade desktop application for loading and visualizing arbitrary Parquet files."""
    
    def __init__(self, initial_file: Optional[str] = None, max_bars: int = 1000):
        self.max_bars = max_bars
        if initial_file:
            if not os.path.isabs(initial_file) and not os.path.exists(initial_file):
                cand = os.path.join(PROJECT_ROOT, initial_file)
                if os.path.exists(cand):
                    initial_file = cand
            self.filepath = initial_file
        else:
            self.filepath = DEFAULT_FOREX_FILE if os.path.exists(DEFAULT_FOREX_FILE) else DEFAULT_CRYPTO_FILE

        self.engine = ChartEngine(title="Parquet Quant Trading Terminal - TradingView & ATAS Edition")
        self.chart = self.engine.initialize_chart(toolbox=True)
        self._build_topbar_controls()
        
        # Bind TradingView Hotkeys
        self.chart.hotkey('alt', 'r', self._on_reset_view)
        
        # Load initial dataset
        if os.path.exists(self.filepath):
            self.load_file(self.filepath)

    def _build_topbar_controls(self) -> None:
        """Construct interactive topbar menus for data, timeframes, indicators, and dimensions."""
        tb = self.chart.topbar
        
        # 1. Reset View Button (TradingView Exact)
        tb.button(
            name='reset_view_btn',
            button_text='⟲ Reset View',
            func=self._on_reset_view
        )
        
        # 2. Scale Mode Switcher (Normal vs Log vs Percent)
        scale_options = ('Scale: Linear', 'Scale: Log', 'Scale: %')
        tb.switcher(
            name='scale_switcher',
            options=scale_options,
            default='Scale: Linear',
            func=self._on_scale_selected
        )
        
        # 3. Parquet Dataset Switcher
        available_files = self._find_available_parquet_files()
        file_options = list(available_files.keys())
        if not file_options:
            file_options = ["Default Dataset"]
            
        tb.menu(
            name='dataset_menu',
            options=tuple(file_options),
            default=file_options[0],
            func=self._on_dataset_selected
        )
        
        # File Browser Button
        tb.button(
            name='open_file_btn',
            button_text='Browse Parquet...',
            func=self._on_browse_file
        )
        
        # 4. Bar Horizon Switcher
        bar_options = ('500 Bars', '1000 Bars', '2500 Bars', '5000 Bars')
        tb.switcher(
            name='bar_switcher',
            options=bar_options,
            default='1000 Bars',
            func=self._on_bars_selected
        )
        
        # 5. Indicators Menu (Overlays)
        ind_options = (
            '+ Indicators',
            'EMA 20',
            'EMA 50',
            'SMA 200',
            'Bollinger Bands (20, 2)',
            'VWAP',
            'VWAP Bands (+-1.5 SD)',
            'Donchian (20)'
        )
        tb.menu(
            name='indicator_menu',
            options=ind_options,
            default=ind_options[0],
            func=self._on_indicator_selected
        )
        
        # 6. Oscillators & Orderflow Menu (Subcharts)
        osc_options = (
            'Orderflow & Oscillators',
            'CVD (Cumulative Delta)',
            'Bar Net Delta',
            'RSI (14)',
            'MACD (12, 26, 9)',
            'ATR (14)'
        )
        tb.menu(
            name='oscillator_menu',
            options=osc_options,
            default=osc_options[0],
            func=self._on_oscillator_selected
        )
        
        # 7. Parquet Dimension Visualizer (Populated dynamically on file load)
        self._dim_options = ['Plot Dimension']
        tb.menu(
            name='dimension_menu',
            options=tuple(self._dim_options),
            default=self._dim_options[0],
            func=self._on_dimension_selected
        )
        
        # 8. Statistics Table Button
        tb.button(
            name='stats_table_btn',
            button_text='Stats HUD',
            func=self._on_stats_clicked
        )

    def _find_available_parquet_files(self) -> dict:
        """Scan workspace for common Forex and Binance crypto parquet datasets."""
        res = {}
        # Search Forex
        forex_pattern = os.path.join(PROJECT_ROOT, "Forex_Backtesting_Data", "*.parquet")
        for f in glob.glob(forex_pattern)[:8]:
            base = os.path.basename(f).replace('.parquet', '')
            res[f"Forex: {base}"] = f
            
        # Search Binance crypto
        crypto_pattern = os.path.join(PROJECT_ROOT, "binance_backtesting_data", "*_master_*.parquet")
        for f in glob.glob(crypto_pattern)[:12]:
            base = os.path.basename(f).replace('.parquet', '')
            res[f"Crypto: {base}"] = f
            
        self._file_map = res
        return res

    def load_file(self, filepath: str) -> None:
        """Load Parquet file into chart engine and refresh dimensions menu."""
        if not os.path.isabs(filepath) and not os.path.exists(filepath):
            cand = os.path.join(PROJECT_ROOT, filepath)
            if os.path.exists(cand):
                filepath = cand
        print(f"[Terminal] Loading Parquet: {filepath}")
        self.filepath = filepath
        self.engine.load_parquet(filepath, max_bars=self.max_bars)
        
        # Update dynamic dimensions
        if self.engine.data_engine:
            dims = self.engine.data_engine.dimension_cols
            menu_items = ['Plot Dimension'] + dims[:30]
            self._dim_options = menu_items
            print(f"[Terminal] Detected {len(dims)} arbitrary feature dimensions: {dims[:8]}")

    def _on_reset_view(self, chart) -> None:
        """Reset view, auto-scale price scale, and fit content (TradingView Alt+R)."""
        print("[Terminal] Resetting View (Fitting content and auto-scaling)...")
        self.chart.fit()
        self.chart.run_script(f"""
            {self.chart.id}.chart.timeScale().fitContent();
            {self.chart.id}.chart.priceScale('right').applyOptions({{autoScale: true}});
        """)

    def _on_scale_selected(self, chart) -> None:
        """Switch price scale between Linear, Logarithmic, and Percentage."""
        val = chart.topbar['scale_switcher'].value
        mode = 'normal'
        if 'Log' in val:
            mode = 'logarithmic'
        elif '%' in val:
            mode = 'percentage'
        print(f"[Terminal] Setting Price Scale Mode: {mode}")
        self.chart.price_scale(auto_scale=True, mode=mode)

    def _on_dataset_selected(self, chart) -> None:
        val = chart.topbar['dataset_menu'].value
        if hasattr(self, '_file_map') and val in self._file_map:
            target_path = self._file_map[val]
            self.load_file(target_path)

    def _on_browse_file(self, chart) -> None:
        """Open native OS file dialog to select any arbitrary Parquet file."""
        try:
            res = chart.win.create_file_dialog(
                webview.OPEN_DIALOG,
                file_types=('Parquet Files (*.parquet)', 'All Files (*.*)')
            )
            if res and len(res) > 0:
                selected_file = res[0]
                self.load_file(selected_file)
        except Exception as e:
            print(f"[Terminal] Error in file dialog: {e}")

    def _on_bars_selected(self, chart) -> None:
        val = chart.topbar['bar_switcher'].value
        try:
            n_bars = int(val.split()[0])
            self.max_bars = n_bars
            self.engine.set_bars(n_bars)
        except Exception as e:
            print(f"[Terminal] Error changing bars: {e}")

    def _on_indicator_selected(self, chart) -> None:
        val = chart.topbar['indicator_menu'].value
        if val == 'EMA 20':
            self.engine.add_overlay_indicator('EMA', {'period': 20}, color='#ffb300')
        elif val == 'EMA 50':
            self.engine.add_overlay_indicator('EMA', {'period': 50}, color='#00e676')
        elif val == 'SMA 200':
            self.engine.add_overlay_indicator('SMA', {'period': 200}, color='#e040fb')
        elif val.startswith('Bollinger'):
            self.engine.add_overlay_indicator('BOLLINGER', {'period': 20, 'std_dev': 2.0})
        elif val == 'VWAP':
            self.engine.add_overlay_indicator('VWAP', color='#00e5ff')
        elif val.startswith('VWAP Bands'):
            self.engine.add_overlay_indicator('VWAP_BANDS')
        elif val.startswith('Donchian'):
            self.engine.add_overlay_indicator('DONCHIAN', {'period': 20})

    def _on_oscillator_selected(self, chart) -> None:
        val = chart.topbar['oscillator_menu'].value
        if val.startswith('CVD'):
            self.engine.add_subchart_oscillator('CVD')
        elif val.startswith('Bar Net Delta'):
            self.engine.add_subchart_oscillator('DELTA')
        elif val.startswith('RSI'):
            self.engine.add_subchart_oscillator('RSI', {'period': 14})
        elif val.startswith('MACD'):
            self.engine.add_subchart_oscillator('MACD', {'fast': 12, 'slow': 26, 'signal': 9})
        elif val.startswith('ATR'):
            self.engine.add_subchart_oscillator('ATR', {'period': 14})

    def _on_dimension_selected(self, chart) -> None:
        val = chart.topbar['dimension_menu'].value
        if self.engine.data_engine and val in self.engine.data_engine.dimension_cols:
            print(f"[Terminal] Plotting arbitrary dimension subchart: {val}")
            self.engine.add_dimension_subchart(val, color='#00e5ff', transform='raw')

    def _on_stats_clicked(self, chart) -> None:
        print("[Terminal] Rendering Summary Statistics HUD Table...")
        self.engine.show_summary_table()

    def run(self) -> None:
        """Launch the standalone native desktop application window."""
        print("[Terminal] Launching Parquet Quant Trading Terminal Window...")
        self.chart.show(block=True)

def main():
    target_file = sys.argv[1] if len(sys.argv) > 1 else None
    app = DesktopQuantTerminal(initial_file=target_file)
    app.run()

if __name__ == '__main__':
    main()
