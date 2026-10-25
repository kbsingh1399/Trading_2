#!/usr/bin/env node
/**
 * scripts/bench.mjs
 * =================
 * Deterministic benchmark suite manager for harness-bench.
 * Implements:
 *   --op create --repo <path> [--out <path>]
 *   --op verify --suite <path>
 * Provides graceful degradation when @metaharness/darwin is absent.
 */

import fs from 'fs';
import path from 'path';

function parseArgs(args) {
  const parsed = { op: null, repo: null, out: null, suite: null };
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--op') parsed.op = args[++i];
    else if (args[i] === '--repo') parsed.repo = args[++i];
    else if (args[i] === '--out') parsed.out = args[++i];
    else if (args[i] === '--suite') parsed.suite = args[++i];
  }
  return parsed;
}

function main() {
  const args = parseArgs(process.argv.slice(2));

  if (!args.op || !['create', 'verify'].includes(args.op)) {
    console.error(JSON.stringify({
      success: false,
      error: "Missing or invalid --op. Must be 'create' or 'verify'."
    }));
    process.exit(2);
  }

  const startTime = Date.now();

  // Op 1: Create
  if (args.op === 'create') {
    if (!args.repo) {
      console.error(JSON.stringify({ success: false, error: "Missing required --repo <path>" }));
      process.exit(2);
    }
    const repoPath = path.resolve(args.repo);
    if (!fs.existsSync(repoPath)) {
      console.error(JSON.stringify({ success: false, error: `Repo path does not exist: ${repoPath}` }));
      process.exit(2);
    }

    const outPath = args.out
      ? path.resolve(args.out)
      : path.join(repoPath, '.metaharness', 'bench', 'suite.json');

    fs.mkdirSync(path.dirname(outPath), { recursive: true });

    // Built-in deterministic benchmark suite generator
    const suite = {
      name: "Blueberry-Phase1-Evaluation-Harness-Suite",
      version: "1.0.0",
      createdAt: new Date().toISOString(),
      repo: repoPath,
      tasks: [
        { id: "audit_preflight", input: "execution_preflight.py", expectedOutput: "PREFLIGHT_PASS", weight: 1.0 },
        { id: "variance_ratio_bounds", input: "VR(4) inside [-1.64, 1.64]", expectedOutput: "UNDEFINED_STAND_ASIDE", weight: 1.0 },
        { id: "whale_persistence", input: "orderbook whale wall persist >= 180s", expectedOutput: "VALID_BACKING", weight: 1.0 },
        { id: "solvency_floor", input: "equity >= 4795.00 USD", expectedOutput: "SOLVENCY_PRESERVED", weight: 2.0 },
        { id: "web2api_proxy", input: "http://127.0.0.1:8081/v1/models", expectedOutput: "STATUS_200", weight: 1.0 }
      ]
    };

    fs.writeFileSync(outPath, JSON.stringify(suite, null, 2), 'utf-8');
    const durationMs = Date.now() - startTime;

    console.log(JSON.stringify({
      success: true,
      data: {
        op: "create",
        outPath,
        taskCount: suite.tasks.length,
        durationMs
      }
    }, null, 2));
    process.exit(0);
  }

  // Op 2: Verify
  if (args.op === 'verify') {
    if (!args.suite) {
      console.error(JSON.stringify({ success: false, error: "Missing required --suite <path>" }));
      process.exit(2);
    }
    const suitePath = path.resolve(args.suite);
    if (!fs.existsSync(suitePath)) {
      console.error(JSON.stringify({ success: false, error: `Suite path not found: ${suitePath}` }));
      process.exit(2);
    }

    try {
      const suiteContent = JSON.parse(fs.readFileSync(suitePath, 'utf-8'));
      const tasks = Array.isArray(suiteContent) ? suiteContent : (suiteContent.tasks || []);
      const wellFormed = Array.isArray(tasks) && tasks.every(t => t.id && (t.input !== undefined) && (t.expectedOutput !== undefined));

      const durationMs = Date.now() - startTime;
      if (!wellFormed) {
        console.error(JSON.stringify({
          success: false,
          error: "Suite is malformed. Each task must have id, input, and expectedOutput.",
          data: { op: "verify", wellFormed: false, durationMs }
        }));
        process.exit(1);
      }

      console.log(JSON.stringify({
        success: true,
        data: {
          op: "verify",
          taskCount: tasks.length,
          wellFormed: true,
          durationMs
        }
      }, null, 2));
      process.exit(0);
    } catch (err) {
      console.error(JSON.stringify({ success: false, error: `JSON parse error: ${err.message}` }));
      process.exit(1);
    }
  }
}

main();
