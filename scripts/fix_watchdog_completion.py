path = 'Terminal/rock_hard_dual_watchdog.py'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Arena condition
code = code.replace(
    'has_cycle = expected_cycle in cur_text if expected_cycle else (cur_hash != a_initial_hash)',
    'has_cycle = (expected_cycle in cur_text) or (cur_hash != a_initial_hash and len(cur_text) >= 1000) if expected_cycle else (cur_hash != a_initial_hash)'
)

# Replace Z.ai condition
code = code.replace(
    'has_cycle = expected_cycle in cur_text if expected_cycle else (cur_hash != z_initial_hash)',
    'has_cycle = (expected_cycle in cur_text) or (cur_hash != z_initial_hash and len(cur_text) >= 1000) if expected_cycle else (cur_hash != z_initial_hash)'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Patched rock_hard_dual_watchdog.py completion condition successfully!")
