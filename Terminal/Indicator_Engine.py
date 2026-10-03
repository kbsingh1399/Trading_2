"""
Engine/terminal/indicator_engine.py
Vectorized Technical & Microstructure Indicator Engine.
Supports classical technical indicators, ATAS-style orderflow analytics, and dynamic arbitrary column transforms.
"""
from __future__ import annotations
from typing import Dict, Any, Tuple, Optional
import numpy as np
import pandas as pd

class IndicatorEngine:
    @staticmethod
    def compute_sma(series: pd.Series, period: int = 20) -> pd.Series:
        return series.rolling(window=period, min_periods=1).mean()

    @staticmethod
    def compute_ema(series: pd.Series, period: int = 20) -> pd.Series:
        return series.ewm(span=period, adjust=False).mean()

    @staticmethod
    def compute_bollinger_bands(series: pd.Series, period: int = 20, std_dev: float = 2.0) -> Tuple[pd.Series, pd.Series, pd.Series]:
        mid = series.rolling(window=period, min_periods=1).mean()
        std = series.rolling(window=period, min_periods=1).std().fillna(0.0)
        upper = mid + (std_dev * std)
        lower = mid - (std_dev * std)
        return upper, mid, lower

    @staticmethod
    def compute_vwap(df: pd.DataFrame, high_col='high', low_col='low', close_col='close', vol_col='volume') -> pd.Series:
        """Volume Weighted Average Price (cumulative over active slice)."""
        typical_price = (df[high_col] + df[low_col] + df[close_col]) / 3.0
        vol = df[vol_col].replace(0, 1.0)
        tp_v = typical_price * vol
        cum_tp_v = tp_v.cumsum()
        cum_vol = vol.cumsum()
        vwap = cum_tp_v / np.maximum(cum_vol, 1e-9)
        return vwap

    @staticmethod
    def compute_vwap_bands(df: pd.DataFrame, std_multiplier: float = 1.5, high_col='high', low_col='low', close_col='close', vol_col='volume') -> Tuple[pd.Series, pd.Series, pd.Series]:
        """VWAP with dynamic standard deviation bands (ATAS style)."""
        vwap = IndicatorEngine.compute_vwap(df, high_col, low_col, close_col, vol_col)
        typical_price = (df[high_col] + df[low_col] + df[close_col]) / 3.0
        vol = df[vol_col].replace(0, 1.0)
        cum_vol = vol.cumsum()
        dev_sq = (typical_price - vwap) ** 2
        cum_dev = (dev_sq * vol).cumsum()
        variance = cum_dev / np.maximum(cum_vol, 1e-9)
        std = np.sqrt(np.maximum(variance, 0.0))
        upper = vwap + (std_multiplier * std)
        lower = vwap - (std_multiplier * std)
        return upper, vwap, lower

    @staticmethod
    def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
        delta = series.diff()
        gain = delta.clip(lower=0.0)
        loss = -delta.clip(upper=0.0)
        
        avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
        avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()
        
        rs = avg_gain / np.maximum(avg_loss, 1e-12)
        rsi = 100.0 - (100.0 / (1.0 + rs))
        return rsi.fillna(50.0)

    @staticmethod
    def compute_macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> Tuple[pd.Series, pd.Series, pd.Series]:
        ema_fast = series.ewm(span=fast, adjust=False).mean()
        ema_slow = series.ewm(span=slow, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        hist = macd_line - signal_line
        return macd_line, signal_line, hist

    @staticmethod
    def compute_atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
        h, l, c = df['high'], df['low'], df['close']
        tr1 = h - l
        tr2 = (h - c.shift(1)).abs()
        tr3 = (l - c.shift(1)).abs()
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        return tr.rolling(window=period, min_periods=1).mean()

    @staticmethod
    def compute_donchian(df: pd.DataFrame, period: int = 20) -> Tuple[pd.Series, pd.Series, pd.Series]:
        high_band = df['high'].rolling(window=period, min_periods=1).max()
        low_band = df['low'].rolling(window=period, min_periods=1).min()
        mid_band = (high_band + low_band) / 2.0
        return high_band, mid_band, low_band

    @staticmethod
    def compute_dimension_zscore(series: pd.Series, period: int = 40) -> pd.Series:
        """Rolling Z-score for arbitrary numerical dimensions (e.g. CVD, spread, liq)."""
        mu = series.rolling(window=period, min_periods=5).mean()
        sigma = series.rolling(window=period, min_periods=5).std().replace(0, 1e-6)
        z = (series - mu) / sigma
        return z.fillna(0.0)

    @classmethod
    def apply_indicator_config(cls, df: pd.DataFrame, indicator_name: str, params: Dict[str, Any]) -> Dict[str, pd.Series]:
        """Dynamically dispatch indicator computation based on UI config."""
        name = indicator_name.upper()
        res = {}
        
        if name == 'SMA':
            period = int(params.get('period', 20))
            col = params.get('column', 'close')
            res[f'SMA_{period}'] = cls.compute_sma(df[col], period)
            
        elif name == 'EMA':
            period = int(params.get('period', 20))
            col = params.get('column', 'close')
            res[f'EMA_{period}'] = cls.compute_ema(df[col], period)
            
        elif name == 'BOLLINGER':
            period = int(params.get('period', 20))
            std_dev = float(params.get('std_dev', 2.0))
            col = params.get('column', 'close')
            u, m, l = cls.compute_bollinger_bands(df[col], period, std_dev)
            res[f'BB_UPPER_{period}'] = u
            res[f'BB_MID_{period}'] = m
            res[f'BB_LOWER_{period}'] = l
            
        elif name == 'VWAP':
            res['VWAP'] = cls.compute_vwap(df)

        elif name == 'VWAP_BANDS':
            mult = float(params.get('std_multiplier', 1.5))
            u, v, l = cls.compute_vwap_bands(df, std_multiplier=mult)
            res['VWAP_UPPER'] = u
            res['VWAP'] = v
            res['VWAP_LOWER'] = l
            
        elif name == 'RSI':
            period = int(params.get('period', 14))
            col = params.get('column', 'close')
            res[f'RSI_{period}'] = cls.compute_rsi(df[col], period)
            
        elif name == 'MACD':
            fast = int(params.get('fast', 12))
            slow = int(params.get('slow', 26))
            signal = int(params.get('signal', 9))
            col = params.get('column', 'close')
            m, s, h = cls.compute_macd(df[col], fast, slow, signal)
            res['MACD_LINE'] = m
            res['MACD_SIGNAL'] = s
            res['MACD_HIST'] = h
            
        elif name == 'ATR':
            period = int(params.get('period', 14))
            res[f'ATR_{period}'] = cls.compute_atr(df, period)
            
        elif name == 'DONCHIAN':
            period = int(params.get('period', 20))
            h, m, l = cls.compute_donchian(df, period)
            res[f'DONCHIAN_HIGH_{period}'] = h
            res[f'DONCHIAN_MID_{period}'] = m
            res[f'DONCHIAN_LOW_{period}'] = l
            
        elif name == 'DIMENSION_ZSCORE':
            col = params.get('column')
            period = int(params.get('period', 40))
            if col in df.columns:
                res[f'{col}_ZSCORE'] = cls.compute_dimension_zscore(df[col], period)
                
        return res
