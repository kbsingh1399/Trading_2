import pathlib

def scan():
    for base in ['.agents/memory', 'Data/Manditory', 'docs']:
        p_base = pathlib.Path(base)
        if not p_base.exists():
            continue
        for p in p_base.rglob('*'):
            if p.is_file() and p.suffix in ['.md', '.txt', '.json']:
                try:
                    txt = p.read_text(encoding='utf-8', errors='replace')
                    c = txt.lower().count('hyperdash')
                    if c > 0:
                        print(f"{p}: {c} occurrences")
                except Exception:
                    pass

if __name__ == '__main__':
    scan()
