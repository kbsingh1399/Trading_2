import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

assets = ['BTC', 'BNB', 'XAUUSD', 'NAS100', 'DJ30', 'EURUSD', 'USDJPY', 'ETH', 'SOL']
for a in assets:
    path = f'docs/dossiers/{a}_MASTER_DOSSIER.md'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"=== {a} MASTER DOSSIER ({len(content)} chars) ===")
        
        m = re.search(r"Mid Price`:\s*`([^`]+)`", content)
        mid = m.group(1) if m else "N/A"
        m = re.search(r"Spread BPS`:\s*`([^`]+)`", content)
        spread = m.group(1) if m else "N/A"
        
        m = re.search(r"Value Area High \(VAH\)\s*=\s*`([^`]+)`", content)
        vah = m.group(1) if m else "N/A"
        m = re.search(r"Point of Control \(POC\)\s*=\s*`([^`]+)`", content)
        poc = m.group(1) if m else "N/A"
        m = re.search(r"Value Area Low \(VAL\)\s*=\s*`([^`]+)`", content)
        val = m.group(1) if m else "N/A"
        
        m = re.search(r"14-Period ATR`:\s*`([^`]+)`", content)
        atr = m.group(1) if m else "N/A"
        m = re.search(r"Session VWAP`:\s*`([^`]+)`", content)
        vwap = m.group(1) if m else "N/A"
        
        card_idx = content.find("## 10. Quantitative Trade Formulation")
        if card_idx != -1:
            card_text = content[card_idx:card_idx+900]
        else:
            card_text = "Section 10 not found"
            
        print(f"Mid: {mid} | Spread: {spread} | ATR: {atr} | VWAP: {vwap}")
        print(f"VAH: {vah} | POC: {poc} | VAL: {val}")
        print("Card snippet:\n" + card_text.strip())
        print("-" * 60)
    except Exception as e:
        print(f"Error reading {a}: {e}")
