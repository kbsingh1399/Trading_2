import MetaTrader5 as mt5
import os
import sys
import gc
import json
import ctypes
from ctypes import wintypes
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

print('=' * 80)
print('🏛️ PART 1: FORENSIC DOSSIER RE-ANALYSIS OF LIVE RESTING LIMIT ORDERS')
print('=' * 80)

if not mt5.initialize():
    print('Failed to initialize MT5')
    sys.exit(1)

orders = mt5.orders_get()
print(f'Total Active Pending Orders on Broker: {len(orders) if orders else 0}')

dossier_dir = Path('docs/dossiers')

for o in orders:
    sym = o.symbol
    clean_sym = sym.replace('.pi', '').replace('.p', '')
    dossier_file = dossier_dir / f'{clean_sym}_MASTER_DOSSIER.md'
    
    tick = mt5.symbol_info_tick(sym)
    bid = tick.bid if tick else 0
    ask = tick.ask if tick else 0
    mid = (bid + ask) / 2
    
    order_type_str = "SELL_LIMIT" if o.type == mt5.ORDER_TYPE_SELL_LIMIT else "BUY_LIMIT"
    
    # Distance to entry
    dist_pts = o.price_open - mid if o.type == mt5.ORDER_TYPE_SELL_LIMIT else mid - o.price_open
    dist_pct = (dist_pts / mid) * 100 if mid > 0 else 0
    
    # R:R calculation
    risk_pts = abs(o.price_open - o.sl)
    reward_pts = abs(o.tp - o.price_open)
    rr = reward_pts / risk_pts if risk_pts > 0 else 0
    
    print(f'\n--- Ticket #{o.ticket} | {sym} ({clean_sym}) ---')
    print(f'Order Type: {order_type_str}')
    print(f'Live Market: Bid={bid} | Ask={ask} | Mid={mid:.4f}')
    print(f'Limit Entry: {o.price_open} | Distance from Market: {dist_pts:.4f} pts ({dist_pct:+.2f}%)')
    print(f'Stop Loss:   {o.sl} (Risk Distance: {risk_pts:.4f} pts)')
    print(f'Take Profit: {o.tp} (Reward Distance: {reward_pts:.4f} pts)')
    print(f'R:R Ratio:   {rr:.3f}R (>= 2.5R Statutory Mandate: {"PASS" if rr >= 2.499 else "FAIL"})')
    print(f'Volume:      {o.volume_current} lots')
    
    # Check dossier contents for structural levels
    if dossier_file.exists():
        d_txt = dossier_file.read_text(encoding='utf-8', errors='replace')
        
        vah, val, poc = 'N/A', 'N/A', 'N/A'
        for l in d_txt.splitlines():
            if 'Value Area High (VAH)' in l or 'Daily VAH' in l:
                vah = l.split('=')[-1].split('(')[0].strip(' `')
            elif 'Value Area Low (VAL)' in l or 'Daily VAL' in l:
                val = l.split('=')[-1].split('(')[0].strip(' `')
            elif 'Point of Control (POC)' in l or 'Daily POC' in l:
                poc = l.split('=')[-1].split('(')[0].strip(' `')
                
        print(f'Dossier Auction Profile: VAH={vah} | POC={poc} | VAL={val}')
        
        if o.type == mt5.ORDER_TYPE_SELL_LIMIT:
            is_valid = mid < o.price_open
            status = 'VALID & UN-TRIGGERED (Awaiting VAH Sweep)' if is_valid else 'INVALIDATED (Price traded above limit)'
        else:
            is_valid = mid > o.price_open
            status = 'VALID & UN-TRIGGERED (Awaiting VAL Sweep)' if is_valid else 'INVALIDATED (Price traded below limit)'
            
        print(f'⚡ Live Dossier Structural Verdict: {status}')

mt5.shutdown()

print('\n' + '=' * 80)
print('🧹 PART 2: SYSTEM RAM INSPECTION & ACTIVE OPTIMIZATION')
print('=' * 80)

class MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [
        ("dwLength", wintypes.DWORD),
        ("dwMemoryLoad", wintypes.DWORD),
        ("ullTotalPhys", ctypes.c_uint64),
        ("ullAvailPhys", ctypes.c_uint64),
        ("ullTotalPageFile", ctypes.c_uint64),
        ("ullAvailPageFile", ctypes.c_uint64),
        ("ullTotalVirtual", ctypes.c_uint64),
        ("ullAvailVirtual", ctypes.c_uint64),
        ("sullAvailExtendedVirtual", ctypes.c_uint64),
    ]

def get_ram_status():
    stat = MEMORYSTATUSEX()
    stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
    total_gb = stat.ullTotalPhys / (1024**3)
    avail_gb = stat.ullAvailPhys / (1024**3)
    used_gb = total_gb - avail_gb
    return total_gb, used_gb, avail_gb, stat.dwMemoryLoad

total_gb, used_gb, avail_gb, load = get_ram_status()
print(f'Initial System RAM: Total={total_gb:.2f} GB | Used={used_gb:.2f} GB ({load}%) | Available={avail_gb:.2f} GB')

# Execute aggressive garbage collection
gc.collect(0)
gc.collect(1)
gc.collect(2)

# Trim current process working set
ctypes.windll.psapi.EmptyWorkingSet(ctypes.windll.kernel32.GetCurrentProcess())

# Query processes via Windows EnumProcesses to trim working sets of background tasks
DWORD_ARRAY = wintypes.DWORD * 2048
pids = DWORD_ARRAY()
bytes_returned = wintypes.DWORD()
trimmed_count = 0

if ctypes.windll.psapi.EnumProcesses(ctypes.byref(pids), ctypes.sizeof(pids), ctypes.byref(bytes_returned)):
    count = int(bytes_returned.value / ctypes.sizeof(wintypes.DWORD))
    PROCESS_SET_QUOTA = 0x0100
    PROCESS_QUERY_INFORMATION = 0x0400
    for i in range(count):
        pid = pids[i]
        if pid <= 4:
            continue
        h = ctypes.windll.kernel32.OpenProcess(PROCESS_SET_QUOTA | PROCESS_QUERY_INFORMATION, False, pid)
        if h:
            res = ctypes.windll.psapi.EmptyWorkingSet(h)
            if res:
                trimmed_count += 1
            ctypes.windll.kernel32.CloseHandle(h)

total_gb, used_gb, avail_gb, load = get_ram_status()
print(f'Optimized working sets across {trimmed_count} Windows processes via psapi.EmptyWorkingSet!')
print(f'Post-Optimization RAM: Total={total_gb:.2f} GB | Used={used_gb:.2f} GB ({load}%) | Available={avail_gb:.2f} GB')
