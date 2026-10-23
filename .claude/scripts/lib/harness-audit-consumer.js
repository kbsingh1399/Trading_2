const fs = require('fs');
const path = require('path');

function countPythonTestFiles(rootDir) {
  let count = 0;
  function walk(dir) {
    if (!fs.existsSync(dir)) return;
    try {
      const entries = fs.readdirSync(dir, { withFileTypes: true });
      for (const entry of entries) {
        if (entry.name.startsWith('.') || entry.name === 'node_modules' || entry.name === '__pycache__' || entry.name === 'venv' || entry.name === '.venv') continue;
        const full = path.join(dir, entry.name);
        if (entry.isDirectory()) {
          walk(full);
        } else if (entry.isFile() && (entry.name.startsWith('test_') || entry.name.endsWith('_test.py') || entry.name.endsWith('_tests.py'))) {
          count++;
        }
      }
    } catch (e) {}
  }
  walk(rootDir);
  return count;
}

function gitignoreIgnoresEnvFiles(contentOrRootDir) {
  let content = '';
  if (typeof contentOrRootDir === 'string' && (contentOrRootDir.includes('\n') || contentOrRootDir.includes('.env') || contentOrRootDir.length > 50)) {
    content = contentOrRootDir;
  } else if (typeof contentOrRootDir === 'string' && fs.existsSync(contentOrRootDir)) {
    try {
      const p = fs.statSync(contentOrRootDir).isDirectory() ? path.join(contentOrRootDir, '.gitignore') : contentOrRootDir;
      if (fs.existsSync(p)) content = fs.readFileSync(p, 'utf8');
    } catch (e) {}
  }
  return /(^|\n)\s*\.env\b/m.test(content) || /(^|\n)\s*\*\.env\b/m.test(content) || content.includes('.env');
}

function hasPythonTestSuite(rootDir) {
  const markers = ['pytest.ini', 'pyproject.toml', 'setup.cfg', 'tox.ini', 'tests', 'test', 'Tests'];
  for (const m of markers) {
    if (fs.existsSync(path.join(rootDir, m))) return true;
  }
  return countPythonTestFiles(rootDir) > 0;
}

module.exports = {
  countPythonTestFiles,
  gitignoreIgnoresEnvFiles,
  hasPythonTestSuite,
};
