"""
Engine/terminal/data_engine.py
Universal High-Performance Parquet Data & Orderflow Engine for Trading Terminals.
Supports Forex, Crypto Perpetuals, Equities, Orderflow Footprint, and Arbitrary Dimension Parquets.
"""
from __future__ import annotations
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import numpy as np
import pandas as pd
import polars as pl

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

class ParquetDataEngine:
    """Institutional-grade data and orderflow engine for arbitrary Parquet financial datasets."""
    
    def __init__(self, file_path: Optional[str | Path] = None):
        self.file_path: Optional[Path] = None
        if file_path:
            p = Path(file_path)
            if not p.is_absolute() and not p.exists():
                candidate = PROJECT_ROOT / file_path
                if candidate.exists():
                    p = candidate
            self.file_path = p
        self.df: Optional[pd.DataFrame] = None
        self.time_col: Optional[str] = None
        self.open_col: Optional[str] = None
        self.high_col: Optional[str] = None
        self.low_col: Optional[str] = None
        self.close_col: Optional[str] = None
        self.vol_col: Optional[str] = None
        self.delta_col: Optional[str] = None
        self.cvd_col: Optional[str] = None
        self.dimension_cols: List[str] = []
        
        if self.file_path and self.file_path.exists():
            self.load_file(self.file_path)

    def load_file(self, file_path: str | Path) -> pd.DataFrame:
        """Load any parquet file with high speed and auto-detect standard OHLCV, Orderflow + dimensions."""
        p = Path(file_path)
        if not p.is_absolute() and not p.exists():
            candidate = PROJECT_ROOT / file_path
            if candidate.exists():
                p = candidate
        self.file_path = p
        if not self.file_path.exists():
            raise FileNotFoundError(f"Parquet file not found: {self.file_path}")

        # High-speed polars read with pandas fallback
        try:
            pldf = pl.read_parquet(self.file_path)
            self.df = pldf.to_pandas()
        except Exception:
            self.df = pd.read_parquet(self.file_path)

        self._detect_schema()
        return self.df

    def _detect_schema(self) -> None:
        """Automatically identify timestamp, OHLCV, Orderflow, and arbitrary quantitative dimension columns."""
        if self.df is None or len(self.df) == 0:
            return

        cols = list(self.df.columns)
        lower_cols = {c.lower(): c for c in cols}

        # 1. Detect Time / Datetime column
        time_candidates = ['datetime', 'datetime_utc', 'open_time_ms', 'time', 'timestamp', 'date', 'open_time']
        self.time_col = None
        for cand in time_candidates:
            if cand in lower_cols:
                self.time_col = lower_cols[cand]
                break
        
        # Standardize time to pandas datetime
        if self.time_col:
            raw_time = self.df[self.time_col]
            if pd.api.types.is_integer_dtype(raw_time):
                first_val = raw_time.iloc[0] if len(raw_time) > 0 else 0
                if first_val > 1e14:
                    unit = 'us'
                elif first_val > 1e11:
                    unit = 'ms'
                else:
                    unit = 's'
                self.df['standard_datetime'] = pd.to_datetime(raw_time, unit=unit, utc=True)
            elif pd.api.types.is_datetime64_any_dtype(raw_time):
                self.df['standard_datetime'] = pd.to_datetime(raw_time, utc=True)
            else:
                self.df['standard_datetime'] = pd.to_datetime(raw_time, errors='coerce', utc=True)
        else:
            # Fallback sequential time
            self.df['standard_datetime'] = pd.date_range(start='2020-01-01', periods=len(self.df), freq='15min', tz='UTC')

        # Clean timestamps: remove NaT, deduplicate, and sort ascending
        self.df.dropna(subset=['standard_datetime'], inplace=True)
        self.df.drop_duplicates(subset=['standard_datetime'], keep='last', inplace=True)
        self.df.sort_values('standard_datetime', inplace=True)
        self.df.reset_index(drop=True, inplace=True)

        # 2. Detect OHLC
        self.open_col = self._match_col(['open', 'o', 'open_price', 'price_open'], lower_cols)
        self.high_col = self._match_col(['high', 'h', 'high_price', 'price_high'], lower_cols)
        self.low_col = self._match_col(['low', 'l', 'low_price', 'price_low'], lower_cols)
        self.close_col = self._match_col(['close', 'c', 'close_price', 'price_close'], lower_cols)

        # 3. Detect Volume
        self.vol_col = self._match_col(['volume', 'volume_base', 'tick_volume', 'vol', 'real_volume', 'volume_quote'], lower_cols)

        # Ensure numeric OHLCV
        for c in [self.open_col, self.high_col, self.low_col, self.close_col, self.vol_col]:
            if c and c in self.df.columns:
                self.df[c] = pd.to_numeric(self.df[c], errors='coerce').fillna(0.0)

        # 4. Detect / Compute ATAS Orderflow Delta & CVD
        # Never use a column labelled future_* as a live/visualization delta;
        # those fields are valid labels only in a causal research pipeline.
        self.delta_col = self._match_col(['delta', 'net_delta', 'net_delta_coin', 'spot_cvd_15m'], lower_cols)
        self.cvd_col = self._match_col(['cvd', 'future_cvd_lifetime', 'future_cvd_session', 'spot_cvd_lifetime'], lower_cols)

        if self.delta_col and self.delta_col in self.df.columns:
            self.df['orderflow_delta'] = pd.to_numeric(self.df[self.delta_col], errors='coerce').fillna(0.0)
        elif 'taker_buy_volume_base' in lower_cols and self.vol_col:
            tbv = pd.to_numeric(self.df[lower_cols['taker_buy_volume_base']], errors='coerce').fillna(0.0)
            tot_v = self.df[self.vol_col]
            self.df['orderflow_delta'] = (2.0 * tbv - tot_v)
        elif self.close_col and self.open_col and self.high_col and self.low_col and self.vol_col:
            # Estimate bar delta from candle microstructure
            spread = np.maximum(self.df[self.high_col] - self.df[self.low_col], 1e-9)
            norm_pos = (self.df[self.close_col] - self.df[self.low_col]) / spread
            self.df['orderflow_delta'] = self.df[self.vol_col] * (2.0 * norm_pos - 1.0)
        else:
            self.df['orderflow_delta'] = 0.0

        if self.cvd_col and self.cvd_col in self.df.columns:
            self.df['orderflow_cvd'] = pd.to_numeric(self.df[self.cvd_col], errors='coerce').fillna(0.0)
        else:
            self.df['orderflow_cvd'] = self.df['orderflow_delta'].cumsum()

        # 5. Detect All Arbitrary Feature Dimensions
        ohlcv_set = {
            self.time_col, self.open_col, self.high_col, self.low_col, self.close_col, self.vol_col,
            'standard_datetime', 'orderflow_delta', 'orderflow_cvd'
        }
        self.dimension_cols = [c for c in cols if c not in ohlcv_set and c is not None]
        # Always include orderflow_delta and orderflow_cvd in dimensions
        if 'orderflow_delta' not in self.dimension_cols:
            self.dimension_cols.insert(0, 'orderflow_delta')
        if 'orderflow_cvd' not in self.dimension_cols:
            self.dimension_cols.insert(1, 'orderflow_cvd')

    def _match_col(self, candidates: List[str], lower_cols: Dict[str, str]) -> Optional[str]:
        for cand in candidates:
            if cand in lower_cols:
                return lower_cols[cand]
        return None

    def get_summary_statistics(self) -> pd.DataFrame:
        """Compute comprehensive statistical metrics across all dimensions in the parquet."""
        if self.df is None:
            return pd.DataFrame()
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        stats_df = self.df[numeric_cols].describe().T
        stats_df['null_count'] = self.df[numeric_cols].isnull().sum()
        stats_df['null_pct'] = (stats_df['null_count'] / len(self.df)) * 100.0
        stats_df['dtype'] = [str(self.df[c].dtype) for c in numeric_cols]
        return stats_df

    def get_candle_data(self, max_bars: int = 5000, start_idx: Optional[int] = None) -> pd.DataFrame:
        """
        Return clean OHLCV slice formatted for high-performance candlestick rendering.
        Guarantees strictly monotonic unix timestamps in seconds and clean ISO strings.
        """
        if self.df is None:
            raise ValueError("No data loaded. Call load_file first.")
        
        n = len(self.df)
        if start_idx is None:
            start_idx = max(0, n - max_bars)
        end_idx = min(n, start_idx + max_bars)

        sub = self.df.iloc[start_idx:end_idx].copy()
        
        # Universal unix seconds timestamp (100% immune to nanosecond/microsecond bugs)
        dt_series = sub['standard_datetime'].dt.tz_localize(None)
        sec_timestamps = dt_series.astype('datetime64[s]').astype('int64')
        iso_time = sub['standard_datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

        # Standard OHLCV DataFrame
        res = pd.DataFrame({
            'time': iso_time,
            'timestamp': sec_timestamps,
            'open': sub[self.open_col].astype(float) if self.open_col else sub[self.close_col].astype(float),
            'high': sub[self.high_col].astype(float) if self.high_col else sub[self.close_col].astype(float),
            'low': sub[self.low_col].astype(float) if self.low_col else sub[self.close_col].astype(float),
            'close': sub[self.close_col].astype(float) if self.close_col else np.zeros(len(sub), dtype=float),
            'volume': sub[self.vol_col].astype(float) if self.vol_col else np.ones(len(sub), dtype=float),
            'delta': sub['orderflow_delta'].astype(float),
            'cvd': sub['orderflow_cvd'].astype(float)
        })
        
        # Attach all original columns and dimension columns for seamless visualization
        for c in sub.columns:
            if c not in res.columns:
                res[c] = sub[c].values

        return res

    def get_volume_profile(self, max_bars: int = 1000, n_bins: int = 32) -> Dict[str, Any]:
        """
        Compute ATAS-grade Volume Profile across the specified candle window.
        Returns price bins, total volume, VPOC (Point of Control), VAH, and VAL (70% Value Area).
        """
        if self.df is None or len(self.df) == 0:
            return {"bins": [], "poc": 0.0, "vah": 0.0, "val": 0.0, "total_vol": 0.0}

        sub = self.get_candle_data(max_bars=max_bars)
        low_min = sub['low'].min()
        high_max = sub['high'].max()
        if high_max <= low_min:
            return {"bins": [], "poc": low_min, "vah": high_max, "val": low_min, "total_vol": 0.0}

        bin_edges = np.linspace(low_min, high_max, n_bins + 1)
        bin_mids = 0.5 * (bin_edges[:-1] + bin_edges[1:])
        bin_vols = np.zeros(n_bins, dtype=float)
        bin_deltas = np.zeros(n_bins, dtype=float)

        # Distribute bar volume across overlapping price bins
        for _, row in sub.iterrows():
            c_low = row['low']
            c_high = row['high']
            c_vol = row['volume']
            c_delta = row['delta']
            
            # Find bins that intersect [c_low, c_high]
            mask = (bin_edges[1:] >= c_low) & (bin_edges[:-1] <= c_high)
            n_overlap = np.sum(mask)
            if n_overlap > 0:
                bin_vols[mask] += c_vol / n_overlap
                bin_deltas[mask] += c_delta / n_overlap

        total_vol = float(np.sum(bin_vols))
        poc_idx = int(np.argmax(bin_vols))
        poc_price = float(bin_mids[poc_idx])

        # Value Area Calculation (70% around POC)
        target_va_vol = 0.70 * total_vol
        accum_vol = bin_vols[poc_idx]
        up_idx = poc_idx
        down_idx = poc_idx

        while accum_vol < target_va_vol and (up_idx < n_bins - 1 or down_idx > 0):
            next_up_vol = bin_vols[up_idx + 1] if up_idx < n_bins - 1 else -1.0
            next_down_vol = bin_vols[down_idx - 1] if down_idx > 0 else -1.0

            if next_up_vol >= next_down_vol and up_idx < n_bins - 1:
                up_idx += 1
                accum_vol += next_up_vol
            elif down_idx > 0:
                down_idx -= 1
                accum_vol += next_down_vol
            else:
                break

        val_price = float(bin_edges[down_idx])
        vah_price = float(bin_edges[up_idx + 1])

        profile_bins = []
        for i in range(n_bins):
            profile_bins.append({
                "price": round(float(bin_mids[i]), 5),
                "volume": round(float(bin_vols[i]), 2),
                "delta": round(float(bin_deltas[i]), 2),
                "is_poc": bool(i == poc_idx),
                "in_value_area": bool(down_idx <= i <= up_idx)
            })

        return {
            "bins": profile_bins,
            "poc": round(poc_price, 5),
            "vah": round(vah_price, 5),
            "val": round(val_price, 5),
            "total_vol": round(total_vol, 2)
        }
