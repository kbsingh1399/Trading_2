"""
Engine/terminal/chart_engine.py
TradingView & ATAS Grade Interactive Chart Controller using Lightweight Charts.
Manages Candlesticks, Volume, Orderflow Delta, CVD, Overlays, Subcharts, and Dynamic Parquet Dimensions.
"""
from __future__ import annotations
import os
import sys
from typing import Dict, Any, List, Optional
import pandas as pd
import numpy as np

# Apply lethal monkey patch to lightweight_charts datetime handler
# Ensures 100% immunity to Python 3.14 / Pandas 2.2 microsecond division bug
import lightweight_charts
from lightweight_charts import Chart
from lightweight_charts.abstract import SeriesCommon

def _patched_df_datetime_format(self, df: pd.DataFrame, exclude_lowercase=None):
    df = df.copy()
    df.columns = self._format_labels(df, df.columns, df.index, exclude_lowercase)
    
    if pd.api.types.is_integer_dtype(df['time']):
        first_val = df['time'].iloc[0] if len(df) > 0 else 0
        unit = 'ms' if first_val > 1e11 else 's'
        df['time'] = pd.to_datetime(df['time'], unit=unit)
    elif not pd.api.types.is_datetime64_any_dtype(df['time']):
        df['time'] = pd.to_datetime(df['time'])
        
    df['time'] = df['time'].astype('datetime64[ns]')
    self._set_interval(df)
    
    df['time'] = df['time'].astype('int64') // 10 ** 9
    return df

SeriesCommon._df_datetime_format = _patched_df_datetime_format

from Terminal.Data_Engine import ParquetDataEngine
from Terminal.Indicator_Engine import IndicatorEngine

class ChartEngine:
    """Institutional-grade interactive chart controller for arbitrary Parquet financial data."""
    
    def __init__(self, title: str = "Parquet Quant Terminal - ATAS Edition", width: int = 1400, height: int = 900):
        self.title = title
        self.width = width
        self.height = height
        self.data_engine: Optional[ParquetDataEngine] = None
        self.current_bars: int = 1000
        self.chart: Optional[Chart] = None
        
        # Tracking active lines and subcharts
        self.active_overlays: Dict[str, Any] = {}
        self.active_subcharts: Dict[str, Any] = {}
        self.stats_table = None
        self.current_df: Optional[pd.DataFrame] = None

    def initialize_chart(self, toolbox: bool = True) -> Chart:
        """Create and configure the main TradingView chart instance."""
        self.chart = Chart(
            title=self.title,
            width=self.width,
            height=self.height,
            toolbox=toolbox
        )
        
        # Configure chart appearance (ATAS Dark Theme)
        self.chart.layout(
            background_color='#131722',
            text_color='#d1d4dc',
            font_size=12,
            font_family='Trebuchet MS, Roboto, sans-serif'
        )
        self.chart.candle_style(
            up_color='#089981',
            down_color='#f23645',
            border_up_color='#089981',
            border_down_color='#f23645',
            wick_up_color='#089981',
            wick_down_color='#f23645'
        )
        self.chart.volume_config(
            scale_margin_top=0.8,
            scale_margin_bottom=0.0,
            up_color='rgba(8, 153, 129, 0.35)',
            down_color='rgba(242, 54, 69, 0.35)'
        )
        self.chart.crosshair(
            mode='normal',
            vert_color='rgba(255, 255, 255, 0.3)',
            vert_style='dashed',
            horz_color='rgba(255, 255, 255, 0.3)',
            horz_style='dashed'
        )
        self.chart.grid(
            vert_enabled=True,
            horz_enabled=True,
            color='rgba(42, 46, 57, 0.6)',
            style='dotted'
        )
        self.chart.legend(visible=True, font_size=11, font_family='monospace')
        return self.chart

    def load_parquet(self, filepath: str, max_bars: int = 1000) -> bool:
        """Load a parquet file and populate the candlestick and volume series."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Parquet file not found: {filepath}")
            
        self.data_engine = ParquetDataEngine(filepath)
        self.current_bars = max_bars
        self.active_overlays.clear()
        self.active_subcharts.clear()
        
        # Update watermark with file basename
        basename = os.path.basename(filepath)
        if self.chart:
            self.chart.watermark(basename.replace('.parquet', ''), color='rgba(255, 255, 255, 0.05)')
            
        return self.refresh_data()

    def refresh_data(self) -> bool:
        """Fetch candle data and render onto the active chart."""
        if self.data_engine is None or self.chart is None:
            return False
            
        self.current_df = self.data_engine.get_candle_data(max_bars=self.current_bars)
        if len(self.current_df) == 0:
            return False
            
        # Candlestick + Volume DataFrame
        candle_df = self.current_df[['time', 'open', 'high', 'low', 'close', 'volume']]
        self.chart.set(candle_df)
        
        return True

    def add_overlay_indicator(self, indicator_type: str, params: Optional[Dict[str, Any]] = None, color: str = '#f7931a', name: Optional[str] = None) -> str:
        """Add moving average, bollinger, or vwap overlay on the main price chart."""
        if self.current_df is None or self.chart is None:
            return ""
            
        params = params or {}
        itype = indicator_type.upper()
        
        if itype == 'EMA':
            p = params.get('period', 20)
            col_name = name or f"EMA_{p}"
            s = IndicatorEngine.compute_ema(self.current_df['close'], period=p)
            line = self.chart.create_line(name=col_name, color=color, width=2)
            line.set(pd.DataFrame({'time': self.current_df['time'], col_name: s}))
            self.active_overlays[col_name] = {'type': 'EMA', 'params': params, 'line': line, 'color': color}
            return col_name
            
        elif itype == 'SMA':
            p = params.get('period', 20)
            col_name = name or f"SMA_{p}"
            s = IndicatorEngine.compute_sma(self.current_df['close'], period=p)
            line = self.chart.create_line(name=col_name, color=color, width=2)
            line.set(pd.DataFrame({'time': self.current_df['time'], col_name: s}))
            self.active_overlays[col_name] = {'type': 'SMA', 'params': params, 'line': line, 'color': color}
            return col_name
            
        elif itype == 'BOLLINGER':
            p = params.get('period', 20)
            std = params.get('std_dev', 2.0)
            u, m, l = IndicatorEngine.compute_bollinger_bands(self.current_df['close'], period=p, std_dev=std)
            
            u_name = f"BB_UPPER_{p}"
            m_name = f"BB_MID_{p}"
            l_name = f"BB_LOWER_{p}"
            
            u_line = self.chart.create_line(name=u_name, color='rgba(41, 98, 255, 0.7)', width=1)
            m_line = self.chart.create_line(name=m_name, color='rgba(255, 152, 0, 0.7)', width=1)
            l_line = self.chart.create_line(name=l_name, color='rgba(41, 98, 255, 0.7)', width=1)
            
            u_line.set(pd.DataFrame({'time': self.current_df['time'], u_name: u}))
            m_line.set(pd.DataFrame({'time': self.current_df['time'], m_name: m}))
            l_line.set(pd.DataFrame({'time': self.current_df['time'], l_name: l}))
            
            self.active_overlays[f"BB_{p}"] = {'type': 'BOLLINGER', 'lines': [u_line, m_line, l_line]}
            return f"BB_{p}"
            
        elif itype == 'VWAP':
            col_name = name or "VWAP"
            s = IndicatorEngine.compute_vwap(self.current_df)
            line = self.chart.create_line(name=col_name, color='#e040fb', width=2)
            line.set(pd.DataFrame({'time': self.current_df['time'], col_name: s}))
            self.active_overlays[col_name] = {'type': 'VWAP', 'line': line}
            return col_name

        elif itype == 'VWAP_BANDS':
            u, v, l = IndicatorEngine.compute_vwap_bands(self.current_df, std_multiplier=1.5)
            u_line = self.chart.create_line(name="VWAP_Upper", color='rgba(224, 64, 251, 0.6)', width=1)
            v_line = self.chart.create_line(name="VWAP", color='#e040fb', width=2)
            l_line = self.chart.create_line(name="VWAP_Lower", color='rgba(224, 64, 251, 0.6)', width=1)
            
            u_line.set(pd.DataFrame({'time': self.current_df['time'], 'VWAP_Upper': u}))
            v_line.set(pd.DataFrame({'time': self.current_df['time'], 'VWAP': v}))
            l_line.set(pd.DataFrame({'time': self.current_df['time'], 'VWAP_Lower': l}))
            
            self.active_overlays["VWAP_BANDS"] = {'type': 'VWAP_BANDS', 'lines': [u_line, v_line, l_line]}
            return "VWAP_BANDS"
            
        elif itype == 'DONCHIAN':
            p = params.get('period', 20)
            h, m, l = IndicatorEngine.compute_donchian(self.current_df, period=p)
            h_line = self.chart.create_line(name=f"DONCHIAN_H_{p}", color='rgba(0, 188, 212, 0.6)', width=1)
            l_line = self.chart.create_line(name=f"DONCHIAN_L_{p}", color='rgba(0, 188, 212, 0.6)', width=1)
            h_line.set(pd.DataFrame({'time': self.current_df['time'], f"DONCHIAN_H_{p}": h}))
            l_line.set(pd.DataFrame({'time': self.current_df['time'], f"DONCHIAN_L_{p}": l}))
            self.active_overlays[f"DONCHIAN_{p}"] = {'type': 'DONCHIAN', 'lines': [h_line, l_line]}
            return f"DONCHIAN_{p}"
            
        return ""

    def add_subchart_oscillator(self, osc_type: str, params: Optional[Dict[str, Any]] = None, height: float = 0.25) -> str:
        """Create a synchronized bottom subchart pane for RSI, MACD, ATR, CVD, Delta."""
        if self.current_df is None or self.chart is None:
            return ""
            
        params = params or {}
        otype = osc_type.upper()
        
        if otype == 'RSI':
            p = params.get('period', 14)
            sub = self.chart.create_subchart(position='bottom', width=1.0, height=height, sync=True)
            sub.layout(background_color='#131722', text_color='#d1d4dc', font_size=11)
            sub.legend(visible=True)
            
            sub.horizontal_line(70, color='rgba(242, 54, 69, 0.5)', width=1, style='dashed')
            sub.horizontal_line(30, color='rgba(8, 153, 129, 0.5)', width=1, style='dashed')
            sub.horizontal_line(50, color='rgba(255, 255, 255, 0.2)', width=1, style='dotted')
            
            s = IndicatorEngine.compute_rsi(self.current_df['close'], period=p)
            line = sub.create_line(name=f"RSI_{p}", color='#b388ff', width=2)
            line.set(pd.DataFrame({'time': self.current_df['time'], f"RSI_{p}": s}))
            
            key = f"RSI_{p}"
            self.active_subcharts[key] = {'subchart': sub, 'type': 'RSI', 'lines': [line]}
            return key
            
        elif otype == 'MACD':
            fast = params.get('fast', 12)
            slow = params.get('slow', 26)
            sig = params.get('signal', 9)
            
            sub = self.chart.create_subchart(position='bottom', width=1.0, height=height, sync=True)
            sub.layout(background_color='#131722', text_color='#d1d4dc', font_size=11)
            sub.legend(visible=True)
            sub.horizontal_line(0, color='rgba(255, 255, 255, 0.3)', width=1, style='dotted')
            
            m, s, h = IndicatorEngine.compute_macd(self.current_df['close'], fast=fast, slow=slow, signal=sig)
            
            m_line = sub.create_line(name="MACD", color='#2962ff', width=2)
            s_line = sub.create_line(name="Signal", color='#ff6d00', width=2)
            hist = sub.create_histogram(name="Histogram", color='rgba(8, 153, 129, 0.6)')
            
            m_line.set(pd.DataFrame({'time': self.current_df['time'], 'MACD': m}))
            s_line.set(pd.DataFrame({'time': self.current_df['time'], 'Signal': s}))
            hist.set(pd.DataFrame({'time': self.current_df['time'], 'Histogram': h}))
            
            key = f"MACD_{fast}_{slow}_{sig}"
            self.active_subcharts[key] = {'subchart': sub, 'type': 'MACD', 'lines': [m_line, s_line, hist]}
            return key
            
        elif otype == 'ATR':
            p = params.get('period', 14)
            sub = self.chart.create_subchart(position='bottom', width=1.0, height=height, sync=True)
            sub.layout(background_color='#131722', text_color='#d1d4dc', font_size=11)
            sub.legend(visible=True)
            
            s = IndicatorEngine.compute_atr(self.current_df, period=p)
            line = sub.create_line(name=f"ATR_{p}", color='#ff5252', width=2)
            line.set(pd.DataFrame({'time': self.current_df['time'], f"ATR_{p}": s}))
            
            key = f"ATR_{p}"
            self.active_subcharts[key] = {'subchart': sub, 'type': 'ATR', 'lines': [line]}
            return key

        elif otype == 'CVD':
            # ATAS Style Cumulative Volume Delta
            sub = self.chart.create_subchart(position='bottom', width=1.0, height=height, sync=True)
            sub.layout(background_color='#131722', text_color='#d1d4dc', font_size=11)
            sub.legend(visible=True)
            
            cvd_series = self.current_df['cvd']
            line = sub.create_line(name="CVD", color='#00e5ff', width=2)
            line.set(pd.DataFrame({'time': self.current_df['time'], 'CVD': cvd_series}))
            
            key = "CVD"
            self.active_subcharts[key] = {'subchart': sub, 'type': 'CVD', 'lines': [line]}
            return key

        elif otype == 'DELTA':
            # ATAS Style Bar Net Delta Histogram
            sub = self.chart.create_subchart(position='bottom', width=1.0, height=height, sync=True)
            sub.layout(background_color='#131722', text_color='#d1d4dc', font_size=11)
            sub.legend(visible=True)
            sub.horizontal_line(0, color='rgba(255, 255, 255, 0.3)', width=1, style='dotted')
            
            hist = sub.create_histogram(name="Bar_Delta", color='rgba(0, 229, 255, 0.6)')
            hist.set(pd.DataFrame({'time': self.current_df['time'], 'Bar_Delta': self.current_df['delta']}))
            
            key = "DELTA"
            self.active_subcharts[key] = {'subchart': sub, 'type': 'DELTA', 'lines': [hist]}
            return key
            
        return ""

    def add_dimension_subchart(self, column_name: str, color: str = '#00e5ff', transform: str = 'raw', height: float = 0.25) -> str:
        """
        Plot ANY arbitrary numerical dimension from the Parquet file onto a synchronized subchart.
        Transform can be: 'raw', 'zscore', or 'ma20'.
        """
        if self.current_df is None or self.chart is None or self.data_engine is None:
            return ""
            
        if column_name not in self.current_df.columns:
            return ""
            
        series = self.current_df[column_name]
        if not pd.api.types.is_numeric_dtype(series):
            return ""
            
        series = series.astype(float)
        plot_name = column_name
        
        if transform == 'zscore':
            series = IndicatorEngine.compute_dimension_zscore(series, period=40)
            plot_name = f"{column_name}_ZScore"
        elif transform == 'ma20':
            series = series.rolling(20, min_periods=1).mean()
            plot_name = f"{column_name}_MA20"
            
        sub = self.chart.create_subchart(position='bottom', width=1.0, height=height, sync=True)
        sub.layout(background_color='#131722', text_color='#d1d4dc', font_size=11)
        sub.legend(visible=True)
        
        if (series < 0).any() or transform == 'zscore':
            sub.horizontal_line(0, color='rgba(255, 255, 255, 0.2)', width=1, style='dotted')
            if transform == 'zscore':
                sub.horizontal_line(2.0, color='rgba(242, 54, 69, 0.4)', width=1, style='dashed')
                sub.horizontal_line(-2.0, color='rgba(8, 153, 129, 0.4)', width=1, style='dashed')
                
        line = sub.create_line(name=plot_name, color=color, width=2)
        line.set(pd.DataFrame({'time': self.current_df['time'], plot_name: series}))
        
        key = f"DIM_{plot_name}"
        self.active_subcharts[key] = {'subchart': sub, 'type': 'DIMENSION', 'column': column_name, 'lines': [line]}
        return key

    def show_summary_table(self) -> None:
        """Display an institutional floating summary stats HUD directly on the chart."""
        if self.data_engine is None or self.chart is None:
            return
            
        stats_df = self.data_engine.get_summary_statistics()
        if stats_df.empty:
            return
            
        headings = ('Dimension', 'Mean', 'Std Dev', 'Min', 'Median', 'Max', 'Null%')
        widths = (0.24, 0.12, 0.12, 0.13, 0.13, 0.13, 0.13)
        
        if self.stats_table is None:
            self.stats_table = self.chart.create_table(
                width=0.48,
                height=0.42,
                headings=headings,
                widths=widths,
                position='right',
                draggable=True,
                background_color='#181c27',
                border_color='#2a2e39',
                border_width=1
            )
            
        rows_to_show = stats_df.head(12)
        for col_name, row in rows_to_show.iterrows():
            mean_val = f"{row.get('mean', 0.0):.4f}" if not pd.isna(row.get('mean')) else "-"
            std_val = f"{row.get('std', 0.0):.4f}" if not pd.isna(row.get('std')) else "-"
            min_val = f"{row.get('min', 0.0):.4f}" if not pd.isna(row.get('min')) else "-"
            med_val = f"{row.get('50%', 0.0):.4f}" if not pd.isna(row.get('50%')) else "-"
            max_val = f"{row.get('max', 0.0):.4f}" if not pd.isna(row.get('max')) else "-"
            null_pct = f"{row.get('null_pct', 0.0):.1f}%"
            
            row_tuple = (str(col_name)[:16], mean_val, std_val, min_val, med_val, max_val, null_pct)
            self.stats_table.new_row(*row_tuple)

    def set_bars(self, n_bars: int) -> None:
        """Update visible bar horizon and re-render."""
        self.current_bars = n_bars
        self.refresh_data()
