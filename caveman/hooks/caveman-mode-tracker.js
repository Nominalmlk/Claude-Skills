#!/usr/bin/env node
// caveman — Claude Code UserPromptSubmit hook
//
// Three responsibilities:
//   1. Slash-command activation (/caveman, /caveman-commit, etc.)
//   2. Natural-language activation/deactivation detection
//   3. Per-turn reinforcement when caveman mode is active

const fs = require('fs');
const path = require('path');
const os = require('os');
const { getDefaultMode, safeWriteFlag, readFlag, VALID_MODES } = require('./caveman-config');

const claudeDir = process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), '.claude');
const flagPath = path.join(claudeDir, '.caveman-active');

let input = '';
process.stdin.on('data', chunk => { input += chunk; });
process.stdin.on('end', () => {
  let prompt = '';
  try {
    const data = JSON.parse(input);
    prompt = (data.prompt || data.user_prompt || '').trim();
  } catch (e) {
    process.exit(0);
  }

  const lc = prompt.toLowerCase();

  // 1. Slash-command activation
  if (lc.startsWith('/caveman-commit')) {
    safeWriteFlag(flagPath, 'commit');
    process.exit(0);
  }
  if (lc.startsWith('/caveman-review')) {
    safeWriteFlag(flagPath, 'review');
    process.exit(0);
  }
  if (lc.startsWith('/caveman-compress')) {
    safeWriteFlag(flagPath, 'compress');
    process.exit(0);
  }
  if (lc.startsWith('/caveman')) {
    const arg = lc.slice('/caveman'.length).trim();
    let mode;
    if (arg === '' || arg === 'mode') {
      const def = getDefaultMode();
      mode = def === 'off' ? 'full' : def;
    } else if (arg === 'wenyan') {
      mode = 'wenyan-full';
    } else if (VALID_MODES.includes(arg)) {
      mode = arg;
    } else {
      mode = 'full';
    }
    safeWriteFlag(flagPath, mode);
    process.stdout.write(JSON.stringify({ outputText: 'Caveman mode: ' + mode }));
    process.exit(0);
  }

  // 2. Natural-language deactivation
  const deactivatePatterns = [
    'stop caveman', 'disable caveman', 'deactivate caveman',
    'turn off caveman', 'caveman off', 'normal mode', 'exit caveman'
  ];
  if (deactivatePatterns.some(p => lc.includes(p))) {
    try { fs.unlinkSync(flagPath); } catch (e) {}
    process.exit(0);
  }

  // 2b. Natural-language activation
  const activatePatterns = [
    'activate caveman', 'turn on caveman', 'talk like caveman',
    'use caveman', 'caveman mode', 'enable caveman',
    'less tokens', 'fewer tokens', 'be brief', 'compress output'
  ];
  if (activatePatterns.some(p => lc.includes(p))) {
    const def = getDefaultMode();
    const mode = def === 'off' ? 'full' : def;
    safeWriteFlag(flagPath, mode);
    process.exit(0);
  }

  // 3. Per-turn reinforcement — keep caveman behavior anchored
  const currentMode = readFlag(flagPath);
  const INDEPENDENT_MODES = new Set(['commit', 'review', 'compress']);
  if (currentMode && !INDEPENDENT_MODES.has(currentMode)) {
    process.stdout.write(JSON.stringify({
      outputText: 'CAVEMAN ACTIVE (' + currentMode + '): Drop articles/filler/pleasantries/hedging. Fragments OK. Code/commits/security: write normal.'
    }));
  }

  process.exit(0);
});
