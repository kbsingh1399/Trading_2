import subprocess
import os
import sys
import json

def get_python_processes():
    ps_cmd = 'Get-CimInstance Win32_Process -Filter "name = \'python.exe\'" | Select-Object ProcessId, CommandLine | ConvertTo-Json'
    try:
        res = subprocess.check_output(['powershell', '-NoProfile', '-Command', ps_cmd], text=True, errors='replace')
        if not res.strip():
            return []
        data = json.loads(res)
        if isinstance(data, dict):
            data = [data]
        
        my_pid = os.getpid()
        to_kill = []
        
        targets = [
            'run_pipeline_continuous_daemon.py',
            'run_master_pipeline.py',
            '4_Hyperliquid_Analysis.py',
            '8_Exchange_Liquidation_Map_1D.py',
            '8_Exchange_Liquidation_Map_7D.py',
            '5_OI.py',
            '1_Crypto_ETF_Flows.py',
            '2_Spot_Netflow_S.py',
            'test_hyperliquid',
            'check_fiber',
            'find_trigger',
            'test_bisect'
        ]
        
        for item in data:
            pid = item.get('ProcessId')
            cmd = item.get('CommandLine') or ''
            if pid == my_pid:
                continue
            if any(t in cmd for t in targets):
                to_kill.append((pid, cmd[:90]))
        return to_kill
    except Exception as e:
        print(f"Error querying CIM: {e}")
        return []

def kill_process(pid):
    try:
        os.kill(pid, 9)
        print(f"os.kill(9) killed PID {pid}")
    except Exception as e:
        subprocess.run(['taskkill', '/F', '/PID', str(pid)], capture_output=True)
        print(f"taskkill killed PID {pid}: {e}")

if __name__ == '__main__':
    procs = get_python_processes()
    print(f"Found {len(procs)} target python processes to kill:")
    for pid, cmd in procs:
        print(f"Killing PID {pid}: {cmd}")
        kill_process(pid)
    print("Process cleanup complete.")

