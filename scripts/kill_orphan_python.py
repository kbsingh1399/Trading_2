import subprocess
import os
import signal
import sys

def get_python_processes():
    try:
        # Use tasklist with csv output
        out = subprocess.check_output(['wmic', 'process', 'get', 'ProcessId,CommandLine'], text=True, errors='replace')
        lines = out.splitlines()
        to_kill = []
        for line in lines:
            line_str = line.strip()
            if not line_str:
                continue
            # Look for python processes running pipeline or collectors
            if 'python' in line_str.lower():
                parts = line_str.rsplit(None, 1)
                if len(parts) == 2 and parts[1].isdigit():
                    cmd = parts[0]
                    pid = int(parts[1])
                    if pid == os.getpid():
                        continue
                    # Check targets
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
                    if any(t in cmd for t in targets):
                        to_kill.append((pid, cmd[:80]))
        return to_kill
    except Exception as e:
        print(f"Error listing processes: {e}")
        return []

def kill_process(pid):
    try:
        subprocess.run(['taskkill', '/F', '/PID', str(pid)], capture_output=True, text=True)
        print(f"Successfully killed PID {pid}")
    except Exception as e:
        print(f"Failed to kill PID {pid}: {e}")

if __name__ == '__main__':
    procs = get_python_processes()
    print(f"Found {len(procs)} candidate processes to kill:")
    for pid, cmd in procs:
        print(f"Killing PID {pid}: {cmd}")
        kill_process(pid)
    print("Done killing orphan python processes.")
