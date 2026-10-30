import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

dossiers = [f for f in os.listdir('docs/dossiers') if f.endswith('_MASTER_DOSSIER.md') or f.endswith('_360_DOSSIER.md')]
print(f"Total dossier files: {len(dossiers)}")
for d in sorted(dossiers):
    size = os.path.getsize(os.path.join("docs/dossiers", d))
    kb = size / 1024
    print(f"  {d:50s}  {kb:8.1f} KB")
