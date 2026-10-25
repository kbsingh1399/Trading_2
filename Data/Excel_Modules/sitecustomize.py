"""
Data/Excel_Modules/sitecustomize.py
Auto-imported by Python whenever PYTHONPATH contains Data/Excel_Modules or cwd is Data/Excel_Modules.
Ensures excel_lock_hook is active from Line 0 for all subprocesses.
"""
try:
    import excel_lock_hook
except Exception:
    pass
