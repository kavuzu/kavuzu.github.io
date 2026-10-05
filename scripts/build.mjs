import { readFileSync, writeFileSync, mkdirSync, copyFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';

// Deployment metadata only. Research dates and datasets remain untouched.
const run = process.env.GITHUB_RUN_NUMBER || '0';
assert.match(run, /^(0|[1-9]\d*)$/, 'Invalid workflow run number');
const version = `v16.0.${run}`;
const source = readFileSync('index.html', 'utf8');
let html = source;
for (const original of [
  "major:16,label:'v16'",
  '<title>Global Trade Atlas v16 · Gold Master</title>',
  '<p>v16 · Gold Master</p>',
  '<div class="badge">v16 · Gold Master</div>',
]) {
  assert.equal(html.split(original).length - 1, 1, `Version anchor changed: ${original}`);
  html = html.replace(original, original.replace('v16', version));
}
mkdirSync('_site', { recursive: true });
writeFileSync('_site/index.html', html);
copyFileSync('.nojekyll', '_site/.nojekyll');
writeFileSync('_site/version.json', JSON.stringify({
  version,
  name: 'Gold Master',
  commit: process.env.GITHUB_SHA || null,
  runNumber: Number(run),
  runId: process.env.GITHUB_RUN_ID || null,
  deployedBuildAt: new Date().toISOString(),
  sourceSha256: createHash('sha256').update(source).digest('hex'),
  htmlSha256: createHash('sha256').update(html).digest('hex'),
}, null, 2) + '\n');
console.log(`Built ${version}. Source file and research dates are unchanged.`);
