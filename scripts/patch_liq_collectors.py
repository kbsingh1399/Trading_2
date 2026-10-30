import pathlib

for f in ['Collectors/Browser/8_Exchange_Liquidation_Map_1D.py', 'Collectors/Browser/8_Exchange_Liquidation_Map_7D.py']:
    p = pathlib.Path(f)
    if not p.exists():
        continue
    text = p.read_text(encoding='utf-8')
    norm = text.replace('\r\n', '\n')
    old_target = """        "APT", "OP", "ARB",
        "XAUT", "PAXG", "EURUSD", "GBPUSD", "USDJPY"
    ]"""
    new_target = """        "APT", "OP", "ARB"
    ]"""
    if old_target in norm:
        norm = norm.replace(old_target, new_target, 1)
        p.write_text(norm, encoding='utf-8')
        print(f"Successfully patched {f}!")
    else:
        print(f"Target not found in {f}!")
