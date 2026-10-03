"""
Terminal package.
Production Trading Terminal for Arbitrary Parquet Data Visualization & Live Microstructure Execution.
"""
from Terminal.Data_Engine import ParquetDataEngine
from Terminal.Indicator_Engine import IndicatorEngine
from Terminal.Chart_Engine import ChartEngine
from Terminal.Desktop_App import DesktopQuantTerminal
from Terminal.Api_Client import HyperdashClient
from Terminal.Hyperdash_Terminal import HyperdashTerminal

# Casing-tolerant and legacy compatibility aliases
ParquetDataEngine = ParquetDataEngine
IndicatorEngine = IndicatorEngine
ChartEngine = ChartEngine
DesktopQuantTerminal = DesktopQuantTerminal
HyperdashClient = HyperdashClient
HyperdashTerminal = HyperdashTerminal

__all__ = [
    "ParquetDataEngine",
    "IndicatorEngine",
    "ChartEngine",
    "DesktopQuantTerminal",
    "HyperdashClient",
    "HyperdashTerminal"
]
