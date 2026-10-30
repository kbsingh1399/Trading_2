import re

# 1. Update C:/Users/SIGMA/.gemini/config/rules/AGENTS.md
rule_path = 'C:/Users/SIGMA/.gemini/config/rules/AGENTS.md'
with open(rule_path, 'r', encoding='utf-8') as f:
    r_content = f.read()

r_content = r_content.replace(
    '2. **Mandatory 5-Day Chat History & Persistent Memory System Integration (OPERATOR MANDATE - STRICT NON-NEGOTIABLE)**:',
    '2. **Mandatory 7-Day Chat History & Persistent Memory System Integration (OPERATOR MANDATE - STRICT NON-NEGOTIABLE)**:'
)
r_content = r_content.replace(
    '- *Compulsory 5-Day Chat & Memory Ingestion Gate*: On EVERY single turn, cycle wakeup, candidate scan, and subagent dispatch, the coordinator and all agents MUST systematically read and ingest the last 5 days of session history (`.agents/memory/session_chat_history.md`, past turns, transcript)',
    '- *Compulsory 7-Day Chat & Memory Ingestion Gate*: On EVERY single turn, cycle wakeup, candidate scan, and subagent dispatch, the coordinator and all agents MUST systematically read and ingest the last 7 days of session history (`.agents/memory/session_chat_history.md`, past turns, transcript)'
)
r_content = r_content.replace(
    '- *Layer 5 (5-Day Session History)*: `@[.agents/memory/session_chat_history.md]` (Last 5 days of logs)',
    '- *Layer 5 (7-Day Session History)*: `@[.agents/memory/session_chat_history.md]` (Last 7 days of logs)'
)
r_content = r_content.replace(
    'If an error or trap was identified in the past 5 days',
    'If an error or trap was identified in the past 7 days'
)

with open(rule_path, 'w', encoding='utf-8') as f:
    f.write(r_content)
print("Updated AGENTS.md rule!")

# 2. Update .agents/memory/MEMORY.md
mem_path = '.agents/memory/MEMORY.md'
with open(mem_path, 'r', encoding='utf-8') as f:
    m_content = f.read()

m_content = m_content.replace(
    'Read last 5 days of chat → coordinator and all agents must read and ingest the last 5 days of chat',
    'Read last 7 days of chat (Upgraded) → coordinator and all agents must read and ingest the last 7 days of chat'
)
with open(mem_path, 'w', encoding='utf-8') as f:
    f.write(m_content)
print("Updated MEMORY.md!")

# 3. Update .agents/memory/operator-directives.md if present
op_path = '.agents/memory/operator-directives.md'
try:
    with open(op_path, 'r', encoding='utf-8') as f:
        op_content = f.read()
    op_content = op_content.replace('5 days', '7 days').replace('5-day', '7-day').replace('5-Day', '7-Day')
    with open(op_path, 'w', encoding='utf-8') as f:
        f.write(op_content)
    print("Updated operator-directives.md!")
except Exception as e:
    print(f"operator-directives.md error: {e}")

# 4. Update .agents/memory/feedback-history.md if present
fb_path = '.agents/memory/feedback-history.md'
try:
    with open(fb_path, 'r', encoding='utf-8') as f:
        fb_content = f.read()
    fb_content = fb_content.replace('5 days', '7 days').replace('5-day', '7-day').replace('5-Day', '7-Day')
    with open(fb_path, 'w', encoding='utf-8') as f:
        f.write(fb_content)
    print("Updated feedback-history.md!")
except Exception as e:
    print(f"feedback-history.md error: {e}")
