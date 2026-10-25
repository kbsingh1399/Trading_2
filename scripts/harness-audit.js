#!/usr/bin/env node
/**
 * scripts/harness-audit.js
 * ========================
 * Root entrypoint wrapper for deterministic repository harness audit.
 * Forwards arguments directly to .claude/scripts/harness-audit.js.
 */

import { spawn } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const targetScript = path.resolve(__dirname, '..', '.claude', 'scripts', 'harness-audit.js');

const child = spawn(process.execPath, [targetScript, ...process.argv.slice(2)], {
  stdio: 'inherit'
});

child.on('exit', (code) => {
  process.exit(code ?? 0);
});
