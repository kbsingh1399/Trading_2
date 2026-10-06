"""
Terminal package.
Production Trading Terminal for Arbitrary Parquet Data Visualization & Live Microstructure Execution.
"""
from importlib import import_module

# Headless risk/execution must not import desktop charting dependencies.
_EXPORTS = {"ParquetDataEngine": "Data_Engine", "IndicatorEngine": "Indicator_Engine",
            "ChartEngine": "Chart_Engine", "DesktopQuantTerminal": "Desktop_App",
            "HyperdashClient": "Api_Client", "HyperdashTerminal": "Hyperdash_Terminal"}

def __getattr__(name):
    if name not in _EXPORTS: raise AttributeError(name)
    value = getattr(import_module("Terminal."+_EXPORTS[name]), name)
    globals()[name] = value
    return value

__all__ = [
    "ParquetDataEngine",
    "IndicatorEngine",
    "ChartEngine",
    "DesktopQuantTerminal",
    "HyperdashClient",
    "HyperdashTerminal"
]
