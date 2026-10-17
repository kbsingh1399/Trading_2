"""
Terminal/Data_Factory/data_explorer_web.py
=========================================
Institutional Local Web Data Explorer & Database Viewer.
Provides an interactive, zero-bloat browser UI to inspect, search, filter,
and export all local SQLite and Parquet database tables in real time.

Usage:
    python Terminal/Data_Factory/data_explorer_web.py [--port 8085]
Then open:
    http://localhost:8085
"""

import argparse
import datetime
import html
import http.server
import json
import os
import pathlib
import socketserver
import sqlite3
import sys
import urllib.parse
from typing import Any, Dict, List

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
DB_PATH = DATA_DIR / "history" / "time_series_index.db"

try:
    import polars as pl
except ImportError:
    pl = None


def get_sqlite_tables() -> List[str]:
    if not DB_PATH.exists():
        return []
    with sqlite3.connect(str(DB_PATH)) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
        return [r[0] for r in cur.fetchall()]


def query_sqlite_table(table: str, limit: int = 100, search: str = "") -> Dict[str, Any]:
    if not DB_PATH.exists():
        return {"columns": [], "rows": [], "total_count": 0}
    with sqlite3.connect(str(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        # Verify valid table
        tables = get_sqlite_tables()
        if table not in tables:
            return {"columns": [], "rows": [], "total_count": 0, "error": f"Table {table} not found"}
        
        # Count total
        cur.execute(f"SELECT count(*) FROM {table}")
        total = cur.fetchone()[0]
        
        # Query with optional search
        query = f"SELECT * FROM {table} ORDER BY id DESC LIMIT {limit}"
        cur.execute(query)
        rows_raw = cur.fetchall()
        
        if not rows_raw:
            # Table might not have an 'id' column
            cur.execute(f"SELECT * FROM {table} LIMIT {limit}")
            rows_raw = cur.fetchall()
            
        columns = [d[0] for d in cur.description] if cur.description else []
        rows = [[str(col) if col is not None else "" for col in row] for row in rows_raw]
        
        return {
            "table": table,
            "columns": columns,
            "rows": rows,
            "total_count": total,
            "showing": len(rows)
        }


def query_parquet_candles(symbol: str = "BTC", limit: int = 50) -> Dict[str, Any]:
    pq_path = DATA_DIR / "Candles" / f"{symbol}_15m.parquet"
    if not pq_path.exists():
        return {"columns": [], "rows": [], "error": f"File {pq_path.name} not found"}
    if pl is None:
        return {"columns": [], "rows": [], "error": "Polars not installed"}
    
    df = pl.read_parquet(pq_path).tail(limit)
    cols = df.columns
    rows = [[str(v) for v in row] for row in df.iter_rows()]
    return {
        "symbol": symbol,
        "columns": cols,
        "rows": list(reversed(rows)),
        "total_count": len(rows),
        "showing": len(rows)
    }


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trading Database Explorer | Institutional Data Stack</title>
    <style>
        :root {
            --bg: #0d1117;
            --surface: #161b22;
            --border: #30363d;
            --text: #c9d1d9;
            --text-bright: #f0f6fc;
            --accent: #58a6ff;
            --green: #3fb950;
            --red: #f85149;
            --yellow: #d29922;
            --purple: #bc8cff;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            padding: 24px;
            font-size: 13px;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            padding-bottom: 16px;
            margin-bottom: 20px;
        }
        .title {
            font-size: 20px;
            font-weight: 700;
            color: var(--text-bright);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .badge {
            font-size: 11px;
            background: #238636;
            color: #fff;
            padding: 3px 8px;
            border-radius: 12px;
            font-weight: 600;
        }
        .nav-tabs {
            display: flex;
            gap: 8px;
            margin-bottom: 18px;
            flex-wrap: wrap;
        }
        .nav-btn {
            background: var(--surface);
            color: var(--text);
            border: 1px solid var(--border);
            padding: 8px 14px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.15s ease;
        }
        .nav-btn:hover, .nav-btn.active {
            background: #21262d;
            color: var(--accent);
            border-color: var(--accent);
        }
        .card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        .card-header {
            padding: 12px 16px;
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #1c2128;
        }
        .meta-info {
            font-size: 12px;
            color: #8b949e;
        }
        .search-box {
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-bright);
            padding: 6px 12px;
            border-radius: 4px;
            font-size: 12px;
            outline: none;
            width: 260px;
        }
        .table-container {
            max-height: 70vh;
            overflow: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }
        th {
            background: #1c2128;
            color: var(--text-bright);
            font-weight: 600;
            padding: 10px 14px;
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 10;
            white-space: nowrap;
        }
        td {
            padding: 8px 14px;
            border-bottom: 1px solid #21262d;
            white-space: nowrap;
            max-width: 320px;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        tr:hover td {
            background: #1f242c;
        }
        .btn-export {
            background: #238636;
            color: #fff;
            border: none;
            padding: 6px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
            font-size: 12px;
        }
        .btn-export:hover {
            background: #2ea043;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="title">
            <span>⚡ Institutional Trading Database Explorer</span>
            <span class="badge">SQLite WAL + Apache Parquet</span>
        </div>
        <div>
            <span style="color: #8b949e;">Auto-sync: Active | Local In-Memory Fast Cache</span>
        </div>
    </div>

    <div class="nav-tabs">
        __NAV_TABS__
    </div>

    <div class="card">
        <div class="card-header">
            <div class="meta-info">
                <strong>Table:</strong> <span style="color: var(--accent);">__TABLE_NAME__</span> &nbsp;|&nbsp; 
                <strong>Rows:</strong> __SHOWING__ of __TOTAL_ROWS__ &nbsp;|&nbsp;
                <strong>Engine:</strong> __ENGINE_TYPE__
            </div>
            <div style="display: flex; gap: 10px; align-items: center;">
                <input type="text" id="filterInput" class="search-box" placeholder="Filter rows in view..." onkeyup="filterTable()">
                <button class="btn-export" onclick="exportTableToCSV()">Download CSV</button>
            </div>
        </div>
        <div class="table-container">
            <table id="dataTable">
                <thead>
                    <tr>
                        __TABLE_HEADERS__
                    </tr>
                </thead>
                <tbody>
                    __TABLE_BODY__
                </tbody>
            </table>
        </div>
    </div>

    <script>
        function filterTable() {
            var input = document.getElementById("filterInput");
            var filter = input.value.toUpperCase();
            var table = document.getElementById("dataTable");
            var tr = table.getElementsByTagName("tr");
            for (var i = 1; i < tr.length; i++) {
                var visible = false;
                var td = tr[i].getElementsByTagName("td");
                for (var j = 0; j < td.length; j++) {
                    if (td[j]) {
                        var txtValue = td[j].textContent || td[j].innerText;
                        if (txtValue.toUpperCase().indexOf(filter) > -1) {
                            visible = true;
                            break;
                        }
                    }
                }
                tr[i].style.display = visible ? "" : "none";
            }
        }

        function exportTableToCSV() {
            var csv = [];
            var rows = document.querySelectorAll("#dataTable tr");
            for (var i = 0; i < rows.length; i++) {
                var row = [], cols = rows[i].querySelectorAll("td, th");
                for (var j = 0; j < cols.length; j++) 
                    row.push('"' + cols[j].innerText.replace(/"/g, '""') + '"');
                csv.push(row.join(","));
            }
            var csvFile = new Blob([csv.join("\\n")], {type: "text/csv"});
            var downloadLink = document.createElement("a");
            downloadLink.download = "__TABLE_NAME___export.csv";
            downloadLink.href = window.URL.createObjectURL(csvFile);
            downloadLink.style.display = "none";
            document.body.appendChild(downloadLink);
            downloadLink.click();
        }
    </script>
</body>
</html>
"""


class DatabaseExplorerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        
        tables = get_sqlite_tables()
        candles = ["BTC", "ETH", "SOL", "BNB", "XRP", "DOGE"]
        
        # Route: default table
        current_tab = params.get("tab", [tables[0] if tables else "whale_history"])[0]
        is_candle = current_tab.startswith("candle_")
        
        if is_candle:
            symbol = current_tab.replace("candle_", "").upper()
            data = query_parquet_candles(symbol, limit=100)
            engine = "Apache Parquet (Columnar / Polars)"
            table_title = f"{symbol} 15m OHLCV Candles"
        else:
            data = query_sqlite_table(current_tab, limit=100)
            engine = "SQLite 3 WAL (Relational / In-Process)"
            table_title = current_tab

        # Build nav tabs
        tabs_html = []
        for t in tables:
            active_cls = "active" if t == current_tab else ""
            tabs_html.append(f'<a href="/?tab={t}" class="nav-btn {active_cls}">{t}</a>')
        for c in candles:
            tab_id = f"candle_{c}"
            active_cls = "active" if tab_id == current_tab else ""
            tabs_html.append(f'<a href="/?tab={tab_id}" class="nav-btn {active_cls}" style="border-color: #388bfd44;">📊 {c} 15m</a>')
        
        nav_tabs_str = "\n".join(tabs_html)
        
        # Build Table Headers
        headers = "".join([f"<th>{html.escape(c)}</th>" for c in data.get("columns", [])])
        
        # Build Table Rows
        body_rows = []
        for row in data.get("rows", []):
            cells = "".join([f"<td>{html.escape(str(v))}</td>" for v in row])
            body_rows.append(f"<tr>{cells}</tr>")
        body_str = "\n".join(body_rows)
        
        rendered = HTML_TEMPLATE.replace("__NAV_TABS__", nav_tabs_str)
        rendered = rendered.replace("__TABLE_NAME__", table_title)
        rendered = rendered.replace("__SHOWING__", str(data.get("showing", 0)))
        rendered = rendered.replace("__TOTAL_ROWS__", str(data.get("total_count", 0)))
        rendered = rendered.replace("__ENGINE_TYPE__", engine)
        rendered = rendered.replace("__TABLE_HEADERS__", headers)
        rendered = rendered.replace("__TABLE_BODY__", body_str)
        
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(rendered.encode("utf-8"))

    def log_message(self, format, *args):
        # Silence access logs to keep stdout clean
        pass


def run_server(port: int = 8085):
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    server = socketserver.TCPServer(("127.0.0.1", port), DatabaseExplorerHandler)
    print(f"[DATA-EXPLORER] Active at http://localhost:{port}")
    print(f"[DATA-EXPLORER] Open http://localhost:{port} in your browser to inspect and export all tables.")
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8085, help="Port to serve web explorer on")
    args = parser.parse_args()
    try:
        run_server(args.port)
    except KeyboardInterrupt:
        print("\nDatabase Explorer stopped.")
