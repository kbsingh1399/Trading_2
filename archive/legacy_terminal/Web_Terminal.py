"""
Engine/terminal/web_terminal.py
High-Fidelity Web/Desktop Quant Trading Terminal with FastAPI & TradingView Lightweight Charts.
ATAS & TradingView Grade: Supports Candlesticks, Hollow, Line, Area, Bars, Reset View (Alt+R),
Auto/Log/% Price Scales, Scroll-To-RealTime, Orderflow Delta, CVD, Volume Profile (VPOC/VAH/VAL),
dynamic schema detection, multi-indicator overlays, and arbitrary dimension subcharts.
"""
from __future__ import annotations
import os
import sys
import glob
import json
import webbrowser
from typing import Dict, Any, List, Optional
from pathlib import Path

# Ensure project root in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import pandas as pd
import numpy as np
import uvicorn
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from Terminal.Data_Engine import ParquetDataEngine
from Terminal.Indicator_Engine import IndicatorEngine

app = FastAPI(title="Parquet Quant Trading Terminal - TradingView & ATAS Edition")

# State management
CURRENT_ENGINE: Optional[ParquetDataEngine] = None
CURRENT_FILEPATH: Optional[str] = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoadRequest(BaseModel):
    filepath: str

class IndicatorRequest(BaseModel):
    indicator_type: str
    params: Dict[str, Any]
    max_bars: int = 1000

class DimensionRequest(BaseModel):
    column_name: str
    transform: str = 'raw'  # 'raw', 'zscore', 'ma20'
    max_bars: int = 1000

@app.get("/api/files")
def list_available_files():
    """List all available parquet files in the project directories."""
    files = []
    # Forex
    forex_pattern = os.path.join(PROJECT_ROOT, "Forex_Data", "*.parquet")
    for f in sorted(glob.glob(forex_pattern)):
        files.append({
            "name": f"Forex: {os.path.basename(f)}",
            "path": f.replace('\\', '/'),
            "category": "Forex"
        })
    # Binance Crypto Master
    crypto_pattern = os.path.join(PROJECT_ROOT, "Binance_Data", "*_master_*.parquet")
    for f in sorted(glob.glob(crypto_pattern)):
        files.append({
            "name": f"Crypto: {os.path.basename(f)}",
            "path": f.replace('\\', '/'),
            "category": "Crypto Perpetuals"
        })
    return {"files": files}

@app.post("/api/load")
def load_parquet_file(req: LoadRequest):
    """Load and detect schema for any parquet file."""
    global CURRENT_ENGINE, CURRENT_FILEPATH
    path = req.filepath
    if not os.path.isabs(path) and not os.path.exists(path):
        cand = os.path.join(PROJECT_ROOT, path)
        if os.path.exists(cand):
            path = cand
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail=f"File not found: {path}")
        
    try:
        CURRENT_ENGINE = ParquetDataEngine(path)
        CURRENT_FILEPATH = path
        
        df = CURRENT_ENGINE.df
        total_rows = len(df)
        time_col = CURRENT_ENGINE.time_col
        open_col = CURRENT_ENGINE.open_col
        high_col = CURRENT_ENGINE.high_col
        low_col = CURRENT_ENGINE.low_col
        close_col = CURRENT_ENGINE.close_col
        vol_col = CURRENT_ENGINE.vol_col
        dims = CURRENT_ENGINE.dimension_cols
        
        start_date = str(df['standard_datetime'].iloc[0])
        end_date = str(df['standard_datetime'].iloc[-1])
        
        return {
            "status": "success",
            "filepath": path,
            "filename": os.path.basename(path),
            "total_bars": total_rows,
            "date_range": [start_date, end_date],
            "schema": {
                "time": time_col,
                "open": open_col,
                "high": high_col,
                "low": low_col,
                "close": close_col,
                "volume": vol_col,
                "dimensions": dims
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/candles")
def get_candles(max_bars: int = 1000):
    """Return candle data formatted for Lightweight Charts with monotonic seconds timestamp."""
    global CURRENT_ENGINE
    if CURRENT_ENGINE is None:
        raise HTTPException(status_code=400, detail="No parquet file loaded.")
        
    try:
        candle_df = CURRENT_ENGINE.get_candle_data(max_bars=max_bars)
        records = []
        for _, row in candle_df.iterrows():
            records.append({
                "time": int(row['timestamp']),
                "open": float(row['open']),
                "high": float(row['high']),
                "low": float(row['low']),
                "close": float(row['close']),
                "volume": float(row['volume']),
                "delta": float(row['delta']),
                "cvd": float(row['cvd'])
            })
        return {
            "count": len(records),
            "candles": records
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/volume_profile")
def get_volume_profile(max_bars: int = 1000, n_bins: int = 32):
    """Return ATAS-grade volume profile across visible candles."""
    global CURRENT_ENGINE
    if CURRENT_ENGINE is None:
        raise HTTPException(status_code=400, detail="No parquet file loaded.")
    try:
        profile = CURRENT_ENGINE.get_volume_profile(max_bars=max_bars, n_bins=n_bins)
        return {"status": "success", "profile": profile}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/indicator")
def calculate_indicator(req: IndicatorRequest):
    """Calculate moving average, bollinger, vwap, vwap bands, rsi, macd, atr, cvd, delta."""
    global CURRENT_ENGINE
    if CURRENT_ENGINE is None:
        raise HTTPException(status_code=400, detail="No parquet file loaded.")
        
    try:
        candle_df = CURRENT_ENGINE.get_candle_data(max_bars=req.max_bars)
        itype = req.indicator_type.upper()
        timestamps = candle_df['timestamp'].astype(int).tolist()
        
        result_series = {}
        
        if itype == 'EMA':
            p = int(req.params.get('period', 20))
            s = IndicatorEngine.compute_ema(candle_df['close'], period=p).tolist()
            result_series[f"EMA_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, s) if not np.isnan(v)]
            
        elif itype == 'SMA':
            p = int(req.params.get('period', 20))
            s = IndicatorEngine.compute_sma(candle_df['close'], period=p).tolist()
            result_series[f"SMA_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, s) if not np.isnan(v)]
            
        elif itype == 'BOLLINGER':
            p = int(req.params.get('period', 20))
            std = float(req.params.get('std_dev', 2.0))
            u, m, l = IndicatorEngine.compute_bollinger_bands(candle_df['close'], period=p, std_dev=std)
            result_series[f"BB_UPPER_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, u.tolist()) if not np.isnan(v)]
            result_series[f"BB_MID_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, m.tolist()) if not np.isnan(v)]
            result_series[f"BB_LOWER_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, l.tolist()) if not np.isnan(v)]
            
        elif itype == 'VWAP':
            s = IndicatorEngine.compute_vwap(candle_df).tolist()
            result_series["VWAP"] = [{"time": t, "value": v} for t, v in zip(timestamps, s) if not np.isnan(v)]

        elif itype == 'VWAP_BANDS':
            u, v, l = IndicatorEngine.compute_vwap_bands(candle_df, std_multiplier=1.5)
            result_series["VWAP_UPPER"] = [{"time": t, "value": val} for t, val in zip(timestamps, u.tolist()) if not np.isnan(val)]
            result_series["VWAP"] = [{"time": t, "value": val} for t, val in zip(timestamps, v.tolist()) if not np.isnan(val)]
            result_series["VWAP_LOWER"] = [{"time": t, "value": val} for t, val in zip(timestamps, l.tolist()) if not np.isnan(val)]
            
        elif itype == 'DONCHIAN':
            p = int(req.params.get('period', 20))
            h, m, l = IndicatorEngine.compute_donchian(candle_df, period=p)
            result_series[f"DONCHIAN_H_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, h.tolist()) if not np.isnan(v)]
            result_series[f"DONCHIAN_M_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, m.tolist()) if not np.isnan(v)]
            result_series[f"DONCHIAN_L_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, l.tolist()) if not np.isnan(v)]
            
        elif itype == 'RSI':
            p = int(req.params.get('period', 14))
            s = IndicatorEngine.compute_rsi(candle_df['close'], period=p).tolist()
            result_series[f"RSI_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, s) if not np.isnan(v)]
            
        elif itype == 'MACD':
            f = int(req.params.get('fast', 12))
            sl = int(req.params.get('slow', 26))
            sig = int(req.params.get('signal', 9))
            m, s, h = IndicatorEngine.compute_macd(candle_df['close'], fast=f, slow=sl, signal=sig)
            result_series["MACD_LINE"] = [{"time": t, "value": v} for t, v in zip(timestamps, m.tolist()) if not np.isnan(v)]
            result_series["MACD_SIGNAL"] = [{"time": t, "value": v} for t, v in zip(timestamps, s.tolist()) if not np.isnan(v)]
            result_series["MACD_HIST"] = [{"time": t, "value": v} for t, v in zip(timestamps, h.tolist()) if not np.isnan(v)]
            
        elif itype == 'ATR':
            p = int(req.params.get('period', 14))
            s = IndicatorEngine.compute_atr(candle_df, period=p).tolist()
            result_series[f"ATR_{p}"] = [{"time": t, "value": v} for t, v in zip(timestamps, s) if not np.isnan(v)]

        elif itype == 'CVD':
            cvd_vals = candle_df['cvd'].tolist()
            result_series["CVD"] = [{"time": t, "value": v} for t, v in zip(timestamps, cvd_vals) if not np.isnan(v)]

        elif itype == 'DELTA':
            delta_vals = candle_df['delta'].tolist()
            result_series["DELTA"] = [{"time": t, "value": v} for t, v in zip(timestamps, delta_vals) if not np.isnan(v)]
            
        return {"status": "success", "indicator": itype, "series": result_series}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/dimension")
def get_dimension_series(req: DimensionRequest):
    """Extract and format arbitrary dimension time series."""
    global CURRENT_ENGINE
    if CURRENT_ENGINE is None:
        raise HTTPException(status_code=400, detail="No parquet file loaded.")
        
    try:
        candle_df = CURRENT_ENGINE.get_candle_data(max_bars=req.max_bars)
        col = req.column_name
        if col not in candle_df.columns:
            raise HTTPException(status_code=404, detail=f"Column '{col}' not found.")
            
        series = candle_df[col]
        if not pd.api.types.is_numeric_dtype(series):
            raise HTTPException(status_code=400, detail=f"Column '{col}' is not numeric.")
            
        series = series.astype(float)
        label = col
        if req.transform == 'zscore':
            series = IndicatorEngine.compute_dimension_zscore(series, period=40)
            label = f"{col}_ZScore"
        elif req.transform == 'ma20':
            series = series.rolling(20, min_periods=1).mean()
            label = f"{col}_MA20"
            
        timestamps = candle_df['timestamp'].astype(int).tolist()
        vals = series.tolist()
        
        points = [{"time": t, "value": v} for t, v in zip(timestamps, vals) if not np.isnan(v)]
        return {
            "status": "success",
            "column": col,
            "label": label,
            "transform": req.transform,
            "data": points
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/stats")
def get_dimension_statistics():
    """Return comprehensive summary stats across all parquet columns."""
    global CURRENT_ENGINE
    if CURRENT_ENGINE is None:
        raise HTTPException(status_code=400, detail="No parquet file loaded.")
        
    try:
        stats = CURRENT_ENGINE.get_summary_statistics()
        records = []
        for col_name, row in stats.iterrows():
            records.append({
                "column": str(col_name),
                "count": int(row.get('count', 0)),
                "mean": float(row.get('mean', 0.0)) if not pd.isna(row.get('mean')) else None,
                "std": float(row.get('std', 0.0)) if not pd.isna(row.get('std')) else None,
                "min": float(row.get('min', 0.0)) if not pd.isna(row.get('min')) else None,
                "p25": float(row.get('25%', 0.0)) if not pd.isna(row.get('25%')) else None,
                "median": float(row.get('50%', 0.0)) if not pd.isna(row.get('50%')) else None,
                "p75": float(row.get('75%', 0.0)) if not pd.isna(row.get('75%')) else None,
                "max": float(row.get('max', 0.0)) if not pd.isna(row.get('max')) else None,
                "null_pct": float(row.get('null_pct', 0.0)),
                "dtype": str(row.get('dtype', ''))
            })
        return {"statistics": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/js/lightweight-charts.js")
def get_lightweight_charts_js():
    """Serve local offline copy of lightweight-charts library."""
    cand_paths = [
        r"C:\Users\SIGMA\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\lightweight_charts\js\lightweight-charts.js",
        os.path.join(os.path.dirname(__file__), "..", "..", "node_modules", "lightweight-charts", "dist", "lightweight-charts.standalone.production.js")
    ]
    try:
        import lightweight_charts
        cand_paths.append(os.path.join(os.path.dirname(lightweight_charts.__file__), "js", "lightweight-charts.js"))
    except Exception:
        pass

    for p in cand_paths:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            return HTMLResponse(content=content, media_type="application/javascript")
    raise HTTPException(status_code=404, detail="lightweight-charts.js bundle not found locally.")

@app.get("/", response_class=HTMLResponse)
def index_page():
    """Render the master trading terminal web interface with TradingView & ATAS Exact Features."""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parquet Quant Terminal | TradingView & ATAS Edition</title>
    <!-- Tailwind CSS (via CDN) -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- TradingView Lightweight Charts (Local + CDN Fallback) -->
    <script src="/js/lightweight-charts.js"></script>
    <script>
        if (typeof LightweightCharts === 'undefined') {
            document.write('<script src="https://unpkg.com/lightweight-charts@4.1.3/dist/lightweight-charts.standalone.production.js"><\\/script>');
        }
    </script>
    <style>
        body { background-color: #131722; color: #d1d4dc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; user-select: none; }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #1e222d; }
        ::-webkit-scrollbar-thumb { background: #2a2e39; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #363c4e; }
        .pane-container { border-bottom: 1px solid #2a2e39; position: relative; }
        .subchart-title { position: absolute; top: 6px; left: 10px; z-index: 10; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; background: rgba(19, 23, 34, 0.85); padding: 2px 6px; border-radius: 3px; border: 1px solid rgba(255,255,255,0.1); }
        .scale-badge-active { background-color: #00bcd4 !important; color: #000000 !important; font-weight: 700 !important; }
    </style>
</head>
<body class="h-screen flex flex-col overflow-hidden">
    <!-- Top Header Bar -->
    <header class="h-12 bg-[#1e222d] border-b border-[#2a2e39] flex items-center justify-between px-3 z-20">
        <div class="flex items-center space-x-3">
            <div class="w-3 h-3 rounded-full bg-emerald-500 animate-pulse"></div>
            <span class="font-bold text-sm tracking-wide text-white uppercase flex items-center space-x-1.5">
                <span>TradingView</span>
                <span class="text-[10px] bg-cyan-900/60 text-cyan-300 px-1.5 py-0.5 rounded font-mono">ATAS Pro</span>
            </span>
            <span class="text-xs bg-[#2a2e39] px-2 py-0.5 rounded text-gray-300 font-mono" id="fileBadge">No file loaded</span>
            <span class="text-xs text-gray-400" id="barsCountBadge">0 bars</span>
            <span class="text-xs bg-indigo-900/60 border border-indigo-700/60 text-indigo-300 px-2 py-0.5 rounded font-mono" id="dimCountBadge">0 dims</span>
        </div>
        
        <div class="flex items-center space-x-2">
            <!-- Quick Load Menu -->
            <select id="quickLoadSelect" onchange="onQuickLoadSelected()" class="bg-[#131722] text-xs text-gray-200 border border-[#2a2e39] rounded px-2.5 py-1.5 focus:outline-none focus:border-cyan-500 font-medium">
                <option value="">📂 Quick Select Parquet...</option>
            </select>
            
            <!-- Bar Horizon Switcher -->
            <div class="flex bg-[#131722] border border-[#2a2e39] rounded p-0.5 text-xs">
                <button onclick="setBarHorizon(500)" class="px-2 py-1 rounded hover:bg-[#2a2e39] text-gray-300" id="btn500">500</button>
                <button onclick="setBarHorizon(1000)" class="px-2 py-1 rounded bg-[#2a2e39] text-white font-medium" id="btn1000">1K</button>
                <button onclick="setBarHorizon(2500)" class="px-2 py-1 rounded hover:bg-[#2a2e39] text-gray-300" id="btn2500">2.5K</button>
                <button onclick="setBarHorizon(5000)" class="px-2 py-1 rounded hover:bg-[#2a2e39] text-gray-300" id="btn5000">5K</button>
            </div>

            <!-- EXACT TRADINGVIEW RESET VIEW BUTTON -->
            <button onclick="resetView()" title="Reset View & AutoScale (Alt+R)" class="bg-[#2a2e39] hover:bg-[#363c4e] text-cyan-300 hover:text-white text-xs px-2.5 py-1.5 rounded font-semibold border border-cyan-500/40 flex items-center space-x-1 transition">
                <span>⟲ Reset View</span>
                <span class="text-[9px] bg-black/40 px-1 rounded text-cyan-400 font-mono">Alt+R</span>
            </button>

            <!-- ATAS Profile Toggle -->
            <button onclick="toggleVolumeProfile()" class="bg-cyan-600 hover:bg-cyan-500 text-black text-xs px-2.5 py-1.5 rounded font-bold flex items-center space-x-1 transition">
                <span>ATAS Profile</span>
            </button>

            <!-- Stats Drawer Toggle -->
            <button onclick="toggleStatsModal()" class="bg-indigo-600 hover:bg-indigo-700 text-white text-xs px-2.5 py-1.5 rounded font-medium flex items-center space-x-1 transition">
                <span>Stats HUD</span>
            </button>
        </div>
    </header>

    <!-- Interactive Sub-Header Controls & Toolbars -->
    <div class="h-10 bg-[#171b26] border-b border-[#2a2e39] flex items-center justify-between px-3 text-xs z-10">
        <!-- Chart Types & View Toggles -->
        <div class="flex items-center space-x-2">
            <span class="text-gray-400 font-medium">Style:</span>
            <select id="chartTypeSelect" onchange="setChartType(this.value)" class="bg-[#131722] text-gray-200 border border-[#2a2e39] rounded px-2 py-1 text-xs focus:outline-none">
                <option value="candles">Candles 🕯️</option>
                <option value="hollow">Hollow Candles 🪟</option>
                <option value="line">Line 📈</option>
                <option value="area">Area 🌊</option>
                <option value="bars">OHLC Bars 📊</option>
            </select>

            <div class="h-4 w-px bg-gray-700 mx-1"></div>

            <!-- Indicators Quick Launcher -->
            <span class="text-gray-400 font-medium">Overlays:</span>
            <button onclick="quickAddIndicator('EMA', {period: 20}, '#ffb300')" class="bg-[#222736] hover:bg-[#2e3549] text-amber-400 px-2 py-0.5 rounded border border-amber-500/30">EMA 20</button>
            <button onclick="quickAddIndicator('EMA', {period: 50}, '#00e676')" class="bg-[#222736] hover:bg-[#2e3549] text-emerald-400 px-2 py-0.5 rounded border border-emerald-500/30">EMA 50</button>
            <button onclick="quickAddIndicator('SMA', {period: 200}, '#e040fb')" class="bg-[#222736] hover:bg-[#2e3549] text-purple-400 px-2 py-0.5 rounded border border-purple-500/30">SMA 200</button>
            <button onclick="quickAddIndicator('VWAP_BANDS', {std_multiplier: 1.5}, '#00e5ff')" class="bg-[#222736] hover:bg-[#2e3549] text-cyan-400 px-2 py-0.5 rounded border border-cyan-500/30">VWAP Bands</button>
            <button onclick="quickAddIndicator('BOLLINGER', {period: 20, std_dev: 2.0}, '#2962ff')" class="bg-[#222736] hover:bg-[#2e3549] text-blue-400 px-2 py-0.5 rounded border border-blue-500/30">BB (20,2)</button>
            
            <div class="h-4 w-px bg-gray-700 mx-1"></div>
            
            <span class="text-gray-400 font-medium">Orderflow:</span>
            <button onclick="quickAddOscillator('CVD', {})" class="bg-[#222736] hover:bg-[#2e3549] text-cyan-300 px-2 py-0.5 rounded border border-cyan-500/40 font-semibold">CVD</button>
            <button onclick="quickAddOscillator('DELTA', {})" class="bg-[#222736] hover:bg-[#2e3549] text-emerald-300 px-2 py-0.5 rounded border border-emerald-500/40 font-semibold">Delta</button>
            <button onclick="quickAddOscillator('RSI', {period: 14})" class="bg-[#222736] hover:bg-[#2e3549] text-indigo-300 px-2 py-0.5 rounded border border-indigo-500/30">RSI</button>
            <button onclick="quickAddOscillator('MACD', {fast: 12, slow: 26, signal: 9})" class="bg-[#222736] hover:bg-[#2e3549] text-orange-300 px-2 py-0.5 rounded border border-orange-500/30">MACD</button>
            <button onclick="quickAddOscillator('ATR', {period: 14})" class="bg-[#222736] hover:bg-[#2e3549] text-rose-300 px-2 py-0.5 rounded border border-rose-500/30">ATR</button>
        </div>

        <!-- Custom Dimension Visualizer & Toggles -->
        <div class="flex items-center space-x-2">
            <!-- Toggle Tools -->
            <button id="toggleVolBtn" onclick="toggleVolume()" title="Toggle Volume Histogram" class="bg-[#222736] hover:bg-[#2e3549] text-gray-200 px-2 py-0.5 rounded border border-gray-600">Vol</button>
            <button id="toggleGridBtn" onclick="toggleGrid()" title="Toggle Grid Lines" class="bg-[#222736] hover:bg-[#2e3549] text-gray-200 px-2 py-0.5 rounded border border-gray-600">Grid</button>
            <button onclick="takeScreenshot()" title="Take Screenshot (Alt+S)" class="bg-[#222736] hover:bg-[#2e3549] text-amber-300 px-2 py-0.5 rounded border border-amber-500/30">📷 Snap</button>
            <button onclick="toggleFullscreen()" title="Toggle Fullscreen" class="bg-[#222736] hover:bg-[#2e3549] text-gray-300 px-2 py-0.5 rounded border border-gray-600">⛶</button>

            <div class="h-4 w-px bg-gray-700 mx-1"></div>

            <select id="dimensionColumnSelect" class="bg-[#131722] text-gray-200 border border-[#2a2e39] rounded px-2 py-0.5 text-xs focus:outline-none focus:border-cyan-500">
                <option value="">Select Parquet Column...</option>
            </select>
            <button onclick="plotSelectedDimension()" class="bg-cyan-600 hover:bg-cyan-500 text-black font-semibold px-2 py-0.5 rounded transition">+ Subchart</button>
            <button onclick="clearAllPlots()" class="bg-red-900/40 hover:bg-red-900/60 text-red-300 border border-red-800/60 px-2 py-0.5 rounded transition">Clear</button>
        </div>
    </div>

    <!-- Main Workspace (Chart + Optional ATAS Volume Profile Sidebar) -->
    <div class="flex-1 flex overflow-hidden relative">
        <!-- Main Interactive Chart Area -->
        <div class="flex-1 flex flex-col relative" id="chartsWorkspace">
            <!-- Candlestick HUD Overlay -->
            <div id="candleHud" class="absolute top-2 left-3 z-10 flex items-center space-x-3 text-xs font-mono bg-[#131722]/85 px-3 py-1.5 rounded border border-[#2a2e39] pointer-events-none">
                <span class="text-gray-400" id="hudDate">--</span>
                <span>O: <b id="hudOpen" class="text-white">--</b></span>
                <span>H: <b id="hudHigh" class="text-emerald-400">--</b></span>
                <span>L: <b id="hudLow" class="text-red-400">--</b></span>
                <span>C: <b id="hudClose" class="text-white">--</b></span>
                <span>Vol: <b id="hudVol" class="text-gray-300">--</b></span>
                <span>Delta: <b id="hudDelta" class="text-cyan-400">--</b></span>
            </div>

            <!-- Candlestick Master Pane -->
            <div id="mainChartPane" class="flex-1 w-full bg-[#131722]"></div>

            <!-- Floating TradingView Bottom-Right Badges: AUTO / LOG / % -->
            <div class="absolute bottom-6 right-3 z-20 flex items-center space-x-1.5 bg-[#131722]/90 p-1 rounded border border-[#2a2e39] shadow-lg font-mono text-[10px]">
                <button id="badgeAuto" onclick="toggleAutoScale()" title="Toggle AutoScale (Alt+A)" class="px-1.5 py-0.5 rounded scale-badge-active">AUTO</button>
                <button id="badgeLog" onclick="toggleLogScale()" title="Toggle Logarithmic Scale (Alt+L)" class="px-1.5 py-0.5 rounded bg-[#1e222d] text-gray-400 hover:text-white">LOG</button>
                <button id="badgePercent" onclick="togglePercentScale()" title="Toggle Percentage Scale" class="px-1.5 py-0.5 rounded bg-[#1e222d] text-gray-400 hover:text-white">%</button>
            </div>

            <!-- Floating Scroll-To-Realtime Button (TradingView Exact Chevron) -->
            <button id="scrollToEndBtn" onclick="scrollToEnd()" title="Scroll to Realtime (End)" class="hidden absolute bottom-16 right-5 z-20 bg-[#1e222d]/90 hover:bg-cyan-600 text-cyan-300 hover:text-black w-8 h-8 rounded-full border border-cyan-500/50 shadow-2xl flex items-center justify-center font-bold transition transform hover:scale-110">
                ⏩
            </button>

            <!-- Subcharts Scrollable Container -->
            <div id="subchartsContainer" class="flex flex-col overflow-y-auto max-h-[48vh] border-t border-[#2a2e39]"></div>
        </div>

        <!-- ATAS Volume Profile Sidebar -->
        <div id="volumeProfileSidebar" class="w-72 bg-[#171b26] border-l border-[#2a2e39] flex flex-col overflow-hidden hidden transition-all duration-300">
            <div class="h-10 bg-[#1e222d] border-b border-[#2a2e39] px-3 flex items-center justify-between text-xs font-bold text-gray-200">
                <span>ATAS Volume Profile</span>
                <span class="text-[10px] bg-cyan-900/60 text-cyan-300 px-1.5 py-0.5 rounded font-mono">VPOC / VA 70%</span>
            </div>
            
            <div class="p-2.5 bg-[#131722] border-b border-[#2a2e39] text-xs font-mono grid grid-cols-2 gap-1.5">
                <div class="bg-[#1e222d] p-1.5 rounded">
                    <span class="text-gray-400 text-[10px]">VPOC:</span>
                    <div id="vpocBadge" class="text-red-400 font-bold text-xs">--</div>
                </div>
                <div class="bg-[#1e222d] p-1.5 rounded">
                    <span class="text-gray-400 text-[10px]">Total Vol:</span>
                    <div id="totalVolBadge" class="text-cyan-300 font-bold text-xs">--</div>
                </div>
                <div class="bg-[#1e222d] p-1.5 rounded">
                    <span class="text-gray-400 text-[10px]">VAH (High):</span>
                    <div id="vahBadge" class="text-emerald-400 font-bold text-xs">--</div>
                </div>
                <div class="bg-[#1e222d] p-1.5 rounded">
                    <span class="text-gray-400 text-[10px]">VAL (Low):</span>
                    <div id="valBadge" class="text-amber-400 font-bold text-xs">--</div>
                </div>
            </div>

            <!-- Profile Ladder Bars -->
            <div id="profileLadderContainer" class="flex-1 overflow-y-auto p-2 space-y-1 text-[11px] font-mono">
                <div class="text-center text-gray-500 py-6">Loading profile...</div>
            </div>
        </div>
    </div>

    <!-- Statistics & Fat Tails HUD Modal -->
    <div id="statsModal" class="fixed inset-0 bg-black/75 z-50 flex items-center justify-center hidden">
        <div class="bg-[#1e222d] border border-[#2a2e39] rounded-lg w-11/12 max-w-5xl max-h-[85vh] flex flex-col shadow-2xl">
            <div class="h-12 border-b border-[#2a2e39] px-4 flex items-center justify-between">
                <div class="flex items-center space-x-2">
                    <span class="font-bold text-white text-sm">Parquet Statistics HUD & Distribution Analysis</span>
                    <span class="text-xs text-gray-400" id="statsFileLabel">--</span>
                </div>
                <button onclick="toggleStatsModal()" class="text-gray-400 hover:text-white text-lg">&times;</button>
            </div>
            <div class="flex-1 overflow-auto p-4">
                <table class="w-full text-left text-xs">
                    <thead class="bg-[#131722] text-gray-400 uppercase font-mono sticky top-0">
                        <tr>
                            <th class="py-2.5 px-3">Column / Dimension</th>
                            <th class="py-2.5 px-3">Mean</th>
                            <th class="py-2.5 px-3">Std Dev</th>
                            <th class="py-2.5 px-3">Min</th>
                            <th class="py-2.5 px-3">25%</th>
                            <th class="py-2.5 px-3">Median</th>
                            <th class="py-2.5 px-3">75%</th>
                            <th class="py-2.5 px-3">Max</th>
                            <th class="py-2.5 px-3">Null %</th>
                            <th class="py-2.5 px-3">Type</th>
                        </tr>
                    </thead>
                    <tbody id="statsTableBody" class="divide-y divide-[#2a2e39] text-gray-300">
                        <tr><td colspan="10" class="py-4 text-center text-gray-500">No data loaded</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Application Script -->
    <script>
        let mainChart = null;
        let candleSeries = null;
        let volumeSeries = null;
        let currentCandleData = [];
        let activeOverlays = {};
        let activeSubcharts = {};
        let currentMaxBars = 1000;
        let currentFilepath = "";
        let volumeProfileVisible = false;
        let currentChartType = 'candles';

        // Scale states
        let isAutoScale = true;
        let isLogScale = false;
        let isPercentScale = false;
        let volumeVisible = true;
        let gridVisible = true;

        // Initialize Master Chart
        function initMasterChart() {
            const container = document.getElementById('mainChartPane');
            mainChart = LightweightCharts.createChart(container, {
                width: container.clientWidth,
                height: container.clientHeight,
                layout: {
                    background: { color: '#131722' },
                    textColor: '#d1d4dc',
                    fontFamily: 'Trebuchet MS, Roboto, sans-serif',
                },
                grid: {
                    vertLines: { color: 'rgba(42, 46, 57, 0.5)', style: 1 },
                    horzLines: { color: 'rgba(42, 46, 57, 0.5)', style: 1 },
                },
                crosshair: {
                    mode: LightweightCharts.CrosshairMode.Normal,
                },
                rightPriceScale: {
                    borderColor: '#2a2e39',
                    autoScale: true,
                },
                timeScale: {
                    borderColor: '#2a2e39',
                    timeVisible: true,
                    secondsVisible: false,
                },
            });

            candleSeries = mainChart.addCandlestickSeries({
                upColor: '#089981',
                downColor: '#f23645',
                borderVisible: false,
                wickUpColor: '#089981',
                wickDownColor: '#f23645',
            });

            volumeSeries = mainChart.addHistogramSeries({
                color: '#26a69a',
                priceFormat: { type: 'volume' },
                priceScaleId: '',
                scaleMargins: { top: 0.8, bottom: 0 },
            });

            // Crosshair subscriber for HUD
            mainChart.subscribeCrosshairMove(param => {
                if (!param || !param.time || !param.seriesData.get(candleSeries)) {
                    return;
                }
                const c = param.seriesData.get(candleSeries);
                const d = new Date(param.time * 1000);
                document.getElementById('hudDate').innerText = d.toISOString().replace('T', ' ').substring(0, 19);
                
                if (c.open !== undefined) {
                    document.getElementById('hudOpen').innerText = c.open.toFixed(5);
                    document.getElementById('hudHigh').innerText = c.high.toFixed(5);
                    document.getElementById('hudLow').innerText = c.low.toFixed(5);
                    document.getElementById('hudClose').innerText = c.close.toFixed(5);
                } else if (c.value !== undefined) {
                    document.getElementById('hudClose').innerText = c.value.toFixed(5);
                }
                
                const v = param.seriesData.get(volumeSeries);
                if (v) document.getElementById('hudVol').innerText = v.value.toLocaleString();

                // Find matching delta
                const matched = currentCandleData.find(cd => cd.time === param.time);
                if (matched && matched.delta !== undefined) {
                    const deltaEl = document.getElementById('hudDelta');
                    deltaEl.innerText = (matched.delta >= 0 ? '+' : '') + Math.round(matched.delta).toLocaleString();
                    deltaEl.className = matched.delta >= 0 ? 'text-emerald-400 font-bold' : 'text-rose-400 font-bold';
                }
            });

            // Logical Range change subscriber (Scroll-to-End indicator)
            mainChart.timeScale().subscribeVisibleLogicalRangeChange(range => {
                if (range && currentCandleData.length > 0) {
                    const btn = document.getElementById('scrollToEndBtn');
                    if (range.to < currentCandleData.length - 15) {
                        btn.classList.remove('hidden');
                    } else {
                        btn.classList.add('hidden');
                    }
                }
            });

            window.addEventListener('resize', () => {
                if (mainChart) {
                    mainChart.applyOptions({
                        width: container.clientWidth,
                        height: container.clientHeight
                    });
                }
                for (const key in activeSubcharts) {
                    const sub = activeSubcharts[key];
                    if (sub && sub.chartInstance) {
                        sub.chartInstance.applyOptions({
                            width: sub.containerEl.clientWidth,
                            height: sub.containerEl.clientHeight
                        });
                    }
                }
            });
        }

        // ==========================================
        // TRADINGVIEW EXACT RESET VIEW & CONTROLS
        // ==========================================
        function resetView() {
            if (!mainChart) return;
            mainChart.timeScale().fitContent();
            mainChart.priceScale('right').applyOptions({ autoScale: true });
            
            for (const key in activeSubcharts) {
                const sub = activeSubcharts[key];
                if (sub && sub.chartInstance) {
                    sub.chartInstance.timeScale().fitContent();
                    sub.chartInstance.priceScale('right').applyOptions({ autoScale: true });
                }
            }
            isAutoScale = true;
            updateScaleBadges();
        }

        function scrollToEnd() {
            if (!mainChart) return;
            mainChart.timeScale().scrollToRealTime();
        }

        function setChartType(type) {
            currentChartType = type;
            if (!mainChart || currentCandleData.length === 0) return;
            
            mainChart.removeSeries(candleSeries);
            
            if (type === 'candles') {
                candleSeries = mainChart.addCandlestickSeries({
                    upColor: '#089981', downColor: '#f23645', borderVisible: false,
                    wickUpColor: '#089981', wickDownColor: '#f23645'
                });
                candleSeries.setData(currentCandleData.map(c => ({
                    time: c.time, open: c.open, high: c.high, low: c.low, close: c.close
                })));
            } else if (type === 'hollow') {
                candleSeries = mainChart.addCandlestickSeries({
                    upColor: 'transparent', downColor: '#f23645', borderVisible: true,
                    borderUpColor: '#089981', borderDownColor: '#f23645',
                    wickUpColor: '#089981', wickDownColor: '#f23645'
                });
                candleSeries.setData(currentCandleData.map(c => ({
                    time: c.time, open: c.open, high: c.high, low: c.low, close: c.close
                })));
            } else if (type === 'line') {
                candleSeries = mainChart.addLineSeries({
                    color: '#2962ff', lineWidth: 2
                });
                candleSeries.setData(currentCandleData.map(c => ({
                    time: c.time, value: c.close
                })));
            } else if (type === 'area') {
                candleSeries = mainChart.addAreaSeries({
                    topColor: 'rgba(41, 98, 255, 0.4)', bottomColor: 'rgba(41, 98, 255, 0.0)',
                    lineColor: '#2962ff', lineWidth: 2
                });
                candleSeries.setData(currentCandleData.map(c => ({
                    time: c.time, value: c.close
                })));
            } else if (type === 'bars') {
                candleSeries = mainChart.addBarSeries({
                    upColor: '#089981', downColor: '#f23645'
                });
                candleSeries.setData(currentCandleData.map(c => ({
                    time: c.time, open: c.open, high: c.high, low: c.low, close: c.close
                })));
            }
            
            mainChart.timeScale().fitContent();
        }

        function toggleAutoScale() {
            isAutoScale = !isAutoScale;
            mainChart.priceScale('right').applyOptions({ autoScale: isAutoScale });
            updateScaleBadges();
        }

        function toggleLogScale() {
            isLogScale = !isLogScale;
            isPercentScale = false;
            const mode = isLogScale ? LightweightCharts.PriceScaleMode.Logarithmic : LightweightCharts.PriceScaleMode.Normal;
            mainChart.priceScale('right').applyOptions({ mode: mode });
            updateScaleBadges();
        }

        function togglePercentScale() {
            isPercentScale = !isPercentScale;
            isLogScale = false;
            const mode = isPercentScale ? LightweightCharts.PriceScaleMode.Percentage : LightweightCharts.PriceScaleMode.Normal;
            mainChart.priceScale('right').applyOptions({ mode: mode });
            updateScaleBadges();
        }

        function updateScaleBadges() {
            document.getElementById('badgeAuto').className = isAutoScale ? 'px-1.5 py-0.5 rounded scale-badge-active cursor-pointer' : 'px-1.5 py-0.5 rounded bg-[#1e222d] text-gray-400 hover:text-white cursor-pointer';
            document.getElementById('badgeLog').className = isLogScale ? 'px-1.5 py-0.5 rounded scale-badge-active cursor-pointer' : 'px-1.5 py-0.5 rounded bg-[#1e222d] text-gray-400 hover:text-white cursor-pointer';
            document.getElementById('badgePercent').className = isPercentScale ? 'px-1.5 py-0.5 rounded scale-badge-active cursor-pointer' : 'px-1.5 py-0.5 rounded bg-[#1e222d] text-gray-400 hover:text-white cursor-pointer';
        }

        function toggleVolume() {
            volumeVisible = !volumeVisible;
            volumeSeries.applyOptions({ visible: volumeVisible });
            const btn = document.getElementById('toggleVolBtn');
            btn.className = volumeVisible ? 'bg-[#222736] hover:bg-[#2e3549] text-gray-200 px-2 py-0.5 rounded border border-gray-600' : 'bg-[#1e222d] text-gray-500 px-2 py-0.5 rounded border border-gray-700 line-through';
        }

        function toggleGrid() {
            gridVisible = !gridVisible;
            mainChart.applyOptions({
                grid: {
                    vertLines: { visible: gridVisible, color: 'rgba(42, 46, 57, 0.5)' },
                    horzLines: { visible: gridVisible, color: 'rgba(42, 46, 57, 0.5)' }
                }
            });
            const btn = document.getElementById('toggleGridBtn');
            btn.className = gridVisible ? 'bg-[#222736] hover:bg-[#2e3549] text-gray-200 px-2 py-0.5 rounded border border-gray-600' : 'bg-[#1e222d] text-gray-500 px-2 py-0.5 rounded border border-gray-700 line-through';
        }

        function takeScreenshot() {
            if (!mainChart) return;
            const canvas = mainChart.takeScreenshot();
            const link = document.createElement('a');
            const fname = (currentFilepath.split('/').pop() || 'trading_chart').replace('.parquet', '');
            link.download = `${fname}_${Date.now()}.png`;
            link.href = canvas.toDataURL('image/png');
            link.click();
        }

        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen();
            } else if (document.exitFullscreen) {
                document.exitFullscreen();
            }
        }

        // Keyboard Shortcuts (TradingView Exact)
        window.addEventListener('keydown', e => {
            if (e.altKey && (e.key === 'r' || e.key === 'R')) {
                e.preventDefault();
                resetView();
            } else if (e.altKey && (e.key === 'l' || e.key === 'L')) {
                e.preventDefault();
                toggleLogScale();
            } else if (e.altKey && (e.key === 'a' || e.key === 'A')) {
                e.preventDefault();
                toggleAutoScale();
            } else if (e.altKey && (e.key === 's' || e.key === 'S')) {
                e.preventDefault();
                takeScreenshot();
            } else if (e.key === 'Home') {
                if (mainChart) mainChart.timeScale().scrollToPosition(-100000, true);
            } else if (e.key === 'End') {
                scrollToEnd();
            }
        });

        // Fetch file list
        async function fetchAvailableFiles() {
            try {
                const res = await fetch('/api/files');
                const data = await res.json();
                const sel = document.getElementById('quickLoadSelect');
                data.files.forEach(f => {
                    const opt = document.createElement('option');
                    opt.value = f.path;
                    opt.innerText = f.name;
                    sel.appendChild(opt);
                });
                
                const defaultFile = data.files.find(f => f.path.includes('USDCAD_15m_real.parquet')) || data.files[0];
                if (defaultFile) {
                    sel.value = defaultFile.path;
                    loadParquet(defaultFile.path);
                }
            } catch (err) {
                console.error("Failed to fetch files:", err);
            }
        }

        // Load Parquet file
        async function loadParquet(filepath) {
            try {
                document.getElementById('fileBadge').innerText = "Loading...";
                const res = await fetch('/api/load', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ filepath })
                });
                const meta = await res.json();
                if (meta.status === 'success') {
                    currentFilepath = filepath;
                    document.getElementById('fileBadge').innerText = meta.filename;
                    document.getElementById('barsCountBadge').innerText = `${meta.total_bars.toLocaleString()} bars`;
                    
                    const dimSel = document.getElementById('dimensionColumnSelect');
                    dimSel.innerHTML = '<option value="">Select Parquet Column...</option>';
                    meta.schema.dimensions.forEach(dim => {
                        const opt = document.createElement('option');
                        opt.value = dim;
                        opt.innerText = dim;
                        dimSel.appendChild(opt);
                    });
                    document.getElementById('dimCountBadge').innerText = `${meta.schema.dimensions.length} dims`;

                    await refreshCandles();
                    clearAllPlots();

                    if (volumeProfileVisible) {
                        refreshVolumeProfile();
                    }
                }
            } catch (err) {
                alert(`Error loading parquet: ${err}`);
            }
        }

        function onQuickLoadSelected() {
            const val = document.getElementById('quickLoadSelect').value;
            if (val) loadParquet(val);
        }

        async function refreshCandles() {
            if (!currentFilepath) return;
            const res = await fetch(`/api/candles?max_bars=${currentMaxBars}`);
            const data = await res.json();
            currentCandleData = data.candles;
            
            setChartType(currentChartType);
            
            const volData = currentCandleData.map(c => ({
                time: c.time,
                value: c.volume,
                color: c.close >= c.open ? 'rgba(8, 153, 129, 0.45)' : 'rgba(242, 54, 69, 0.45)'
            }));
            volumeSeries.setData(volData);
            
            resetView();

            if (volumeProfileVisible) {
                refreshVolumeProfile();
            }
        }

        function setBarHorizon(bars) {
            currentMaxBars = bars;
            ['500', '1000', '2500', '5000'].forEach(b => {
                const el = document.getElementById(`btn${b}`);
                if (b === String(bars)) {
                    el.className = "px-2 py-1 rounded bg-[#2a2e39] text-white font-medium";
                } else {
                    el.className = "px-2 py-1 rounded hover:bg-[#2a2e39] text-gray-300";
                }
            });
            refreshCandles();
        }

        async function quickAddIndicator(itype, params, color) {
            const res = await fetch('/api/indicator', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    indicator_type: itype,
                    params: params,
                    max_bars: currentMaxBars
                })
            });
            const data = await res.json();
            if (data.status === 'success') {
                for (const key in data.series) {
                    const line = mainChart.addLineSeries({
                        color: color,
                        lineWidth: 2,
                        title: key
                    });
                    line.setData(data.series[key]);
                    activeOverlays[key] = line;
                }
            }
        }

        async function quickAddOscillator(type, params) {
            const res = await fetch('/api/indicator', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    indicator_type: type,
                    params: params,
                    max_bars: currentMaxBars
                })
            });
            const data = await res.json();
            if (data.status === 'success') {
                const colorMap = {
                    'CVD': '#00e5ff',
                    'DELTA': '#26a69a',
                    'RSI': '#b388ff',
                    'MACD': '#2962ff',
                    'ATR': '#ff5252'
                };
                createSubchartPane(type, data.series, colorMap[type] || '#00e5ff');
            }
        }

        async function plotSelectedDimension() {
            const col = document.getElementById('dimensionColumnSelect').value;
            if (!col) return;

            const res = await fetch('/api/dimension', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    column_name: col,
                    transform: 'raw',
                    max_bars: currentMaxBars
                })
            });
            const data = await res.json();
            if (data.status === 'success') {
                const seriesMap = {};
                seriesMap[data.label] = data.data;
                createSubchartPane(data.label, seriesMap, '#00e5ff');
            }
        }

        function createSubchartPane(title, seriesMap, defaultColor) {
            const container = document.getElementById('subchartsContainer');
            const pane = document.createElement('div');
            pane.className = "pane-container h-44 w-full relative";
            pane.id = `pane_${title.replace(/[^a-zA-Z0-9]/g, '_')}`;
            
            const label = document.createElement('div');
            label.className = "subchart-title text-cyan-400";
            label.innerHTML = `<span>${title}</span> <button onclick="removeSubchart('${pane.id}')" class="ml-2 text-red-400 hover:text-red-300 font-bold">&times;</button>`;
            pane.appendChild(label);
            container.appendChild(pane);

            const subChart = LightweightCharts.createChart(pane, {
                width: pane.clientWidth,
                height: pane.clientHeight,
                layout: {
                    background: { color: '#131722' },
                    textColor: '#d1d4dc',
                },
                grid: {
                    vertLines: { color: 'rgba(42, 46, 57, 0.4)' },
                    horzLines: { color: 'rgba(42, 46, 57, 0.4)' },
                },
                timeScale: {
                    visible: true,
                    borderColor: '#2a2e39',
                }
            });

            for (const sName in seriesMap) {
                if (title === 'DELTA' || sName.includes('HIST')) {
                    const hist = subChart.addHistogramSeries({
                        color: defaultColor,
                        title: sName
                    });
                    const formatted = seriesMap[sName].map(item => ({
                        time: item.time,
                        value: item.value,
                        color: item.value >= 0 ? 'rgba(8, 153, 129, 0.7)' : 'rgba(242, 54, 69, 0.7)'
                    }));
                    hist.setData(formatted);
                } else {
                    const line = subChart.addLineSeries({
                        color: defaultColor,
                        lineWidth: 2,
                        title: sName
                    });
                    line.setData(seriesMap[sName]);
                }
            }

            mainChart.timeScale().subscribeVisibleLogicalRangeChange(range => {
                if (range) subChart.timeScale().setVisibleLogicalRange(range);
            });
            subChart.timeScale().subscribeVisibleLogicalRangeChange(range => {
                if (range) mainChart.timeScale().setVisibleLogicalRange(range);
            });

            activeSubcharts[pane.id] = {
                chartInstance: subChart,
                containerEl: pane,
                title: title
            };
            
            subChart.timeScale().fitContent();
        }

        function removeSubchart(paneId) {
            if (activeSubcharts[paneId]) {
                const el = document.getElementById(paneId);
                if (el) el.remove();
                delete activeSubcharts[paneId];
            }
        }

        function clearAllPlots() {
            for (const key in activeOverlays) {
                mainChart.removeSeries(activeOverlays[key]);
            }
            activeOverlays = {};

            for (const key in activeSubcharts) {
                const el = document.getElementById(key);
                if (el) el.remove();
            }
            activeSubcharts = {};
        }

        function toggleVolumeProfile() {
            volumeProfileVisible = !volumeProfileVisible;
            const el = document.getElementById('volumeProfileSidebar');
            if (volumeProfileVisible) {
                el.classList.remove('hidden');
                refreshVolumeProfile();
            } else {
                el.classList.add('hidden');
            }
            window.dispatchEvent(new Event('resize'));
        }

        async function refreshVolumeProfile() {
            if (!currentFilepath) return;
            try {
                const res = await fetch(`/api/volume_profile?max_bars=${currentMaxBars}&n_bins=32`);
                const data = await res.json();
                if (data.status === 'success') {
                    const p = data.profile;
                    document.getElementById('vpocBadge').innerText = p.poc.toFixed(5);
                    document.getElementById('totalVolBadge').innerText = Math.round(p.total_vol).toLocaleString();
                    document.getElementById('vahBadge').innerText = p.vah.toFixed(5);
                    document.getElementById('valBadge').innerText = p.val.toFixed(5);

                    const container = document.getElementById('profileLadderContainer');
                    container.innerHTML = '';
                    
                    const maxVolInBin = Math.max(...p.bins.map(b => b.volume), 1);
                    const reversedBins = [...p.bins].reverse();
                    
                    reversedBins.forEach(b => {
                        const pct = Math.min(100, Math.round((b.volume / maxVolInBin) * 100));
                        const isPoc = b.is_poc;
                        const inVa = b.in_value_area;
                        
                        const row = document.createElement('div');
                        row.className = `flex items-center justify-between px-1.5 py-0.5 rounded text-[10px] relative overflow-hidden ${isPoc ? 'bg-red-950/70 border border-red-600/80 font-bold' : inVa ? 'bg-[#222736]' : 'bg-[#171b26]'}`;
                        
                        const barColor = isPoc ? 'rgba(239, 68, 68, 0.45)' : (b.delta >= 0 ? 'rgba(8, 153, 129, 0.35)' : 'rgba(242, 54, 69, 0.35)');
                        const fillBar = `<div class="absolute left-0 top-0 bottom-0 pointer-events-none" style="width: ${pct}%; background-color: ${barColor};"></div>`;
                        
                        row.innerHTML = `
                            ${fillBar}
                            <span class="z-10 ${isPoc ? 'text-white' : 'text-gray-300'}">${b.price.toFixed(5)}</span>
                            <span class="z-10 ${b.delta >= 0 ? 'text-emerald-400' : 'text-rose-400'}">${Math.round(b.volume).toLocaleString()} (${b.delta >= 0 ? '+' : ''}${Math.round(b.delta)})</span>
                        `;
                        container.appendChild(row);
                    });
                }
            } catch (err) {
                console.error("Error refreshing volume profile:", err);
            }
        }

        function toggleStatsModal() {
            const modal = document.getElementById('statsModal');
            modal.classList.toggle('hidden');
            if (!modal.classList.contains('hidden')) {
                loadStatsTable();
            }
        }

        async function loadStatsTable() {
            if (!currentFilepath) return;
            try {
                document.getElementById('statsFileLabel').innerText = document.getElementById('fileBadge').innerText;
                const res = await fetch('/api/stats');
                const data = await res.json();
                const tbody = document.getElementById('statsTableBody');
                tbody.innerHTML = '';
                
                data.statistics.forEach(s => {
                    const tr = document.createElement('tr');
                    tr.className = "hover:bg-[#2a2e39] font-mono";
                    tr.innerHTML = `
                        <td class="py-2 px-3 font-semibold text-white">${s.column}</td>
                        <td class="py-2 px-3 text-cyan-300">${s.mean !== null ? s.mean.toFixed(4) : '-'}</td>
                        <td class="py-2 px-3">${s.std !== null ? s.std.toFixed(4) : '-'}</td>
                        <td class="py-2 px-3 text-rose-400">${s.min !== null ? s.min.toFixed(4) : '-'}</td>
                        <td class="py-2 px-3">${s.p25 !== null ? s.p25.toFixed(4) : '-'}</td>
                        <td class="py-2 px-3 text-amber-300">${s.median !== null ? s.median.toFixed(4) : '-'}</td>
                        <td class="py-2 px-3">${s.p75 !== null ? s.p75.toFixed(4) : '-'}</td>
                        <td class="py-2 px-3 text-emerald-400">${s.max !== null ? s.max.toFixed(4) : '-'}</td>
                        <td class="py-2 px-3 ${s.null_pct > 0 ? 'text-amber-400 font-bold' : 'text-gray-500'}">${s.null_pct.toFixed(1)}%</td>
                        <td class="py-2 px-3 text-gray-400">${s.dtype}</td>
                    `;
                    tbody.appendChild(tr);
                });
            } catch (err) {
                console.error("Error loading stats:", err);
            }
        }

        window.onload = () => {
            initMasterChart();
            fetchAvailableFiles();
        };
    </script>
</body>
</html>
"""
    return HTMLResponse(content=html_content)

def start_server(port: int = 8090, auto_open: bool = True):
    """Launch the Web Trading Terminal server and open in local browser."""
    url = f"http://127.0.0.1:{port}"
    print(f"\n=======================================================")
    print(f"  Parquet Quant Trading Terminal - TradingView Edition")
    print(f"  URL: {url}")
    print(f"=======================================================\n")
    if auto_open:
        webbrowser.open(url)
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="info")

if __name__ == '__main__':
    start_server(port=8090, auto_open=True)
