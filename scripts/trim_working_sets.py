import ctypes
import subprocess

OpenProcess = ctypes.windll.kernel32.OpenProcess
CloseHandle = ctypes.windll.kernel32.CloseHandle
EmptyWorkingSet = ctypes.windll.psapi.EmptyWorkingSet

PROCESS_ALL = 0x0400 | 0x0100

out = subprocess.check_output(['tasklist', '/FO', 'CSV', '/NH']).decode('utf-8', errors='ignore')
trimmed = 0
for line in out.strip().split('\r\n'):
    p = [x.strip('"') for x in line.split('","')]
    if len(p) >= 2 and p[1].isdigit():
        pid = int(p[1])
        name = p[0]
        h = OpenProcess(PROCESS_ALL, False, pid)
        if h:
            res = EmptyWorkingSet(h)
            if res:
                trimmed += 1
            CloseHandle(h)

print(f"Successfully trimmed working sets of {trimmed} processes.")

class MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [
        ('dwLength', ctypes.c_ulong),
        ('dwMemoryLoad', ctypes.c_ulong),
        ('ullTotalPhys', ctypes.c_ulonglong),
        ('ullAvailPhys', ctypes.c_ulonglong),
        ('ullTotalPageFile', ctypes.c_ulonglong),
        ('ullAvailPageFile', ctypes.c_ulonglong),
        ('ullTotalVirtual', ctypes.c_ulonglong),
        ('ullAvailVirtual', ctypes.c_ulonglong),
        ('sullAvailExtendedVirtual', ctypes.c_ulonglong),
    ]

stat = MEMORYSTATUSEX()
stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))

total_gb = stat.ullTotalPhys / (1024**3)
avail_gb = stat.ullAvailPhys / (1024**3)
used_gb = total_gb - avail_gb
pct = stat.dwMemoryLoad

print(f"Total RAM: {total_gb:.2f} GB | Free RAM: {avail_gb:.2f} GB | Used RAM: {used_gb:.2f} GB ({pct} percent used)")
