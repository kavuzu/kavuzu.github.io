"""Dependency-free HTML integrity and JavaScript syntax gate for the single file."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile


class AtlasParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.ids = []
        self.scripts = []
        self.script = None
        self.script_type = ''
        self.external_scripts = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag == 'script':
            self.script = []
            self.script_type = attrs.get('type', '').lower()
            if attrs.get('src'):
                self.external_scripts.append(attrs['src'])

    def handle_data(self, data):
        if self.script is not None:
            self.script.append(data)

    def handle_endtag(self, tag):
        if tag == 'script' and self.script is not None:
            if self.script_type in ('', 'text/javascript', 'application/javascript', 'module'):
                self.scripts.append((''.join(self.script), self.script_type))
            self.script = None


for filename in sys.argv[1:] or ['index.html']:
    text = Path(filename).read_text(encoding='utf-8')
    parser = AtlasParser()
    parser.feed(text)
    duplicates = [key for key, count in Counter(parser.ids).items() if count > 1]
    if duplicates:
        raise SystemExit(f'{filename}: duplicate HTML IDs: {duplicates}')
    if parser.external_scripts:
        raise SystemExit(f'{filename}: core scripts must remain bundled')
    if len(parser.scripts) != 4 or text.count('const ATLAS_VERSION=') != 1:
        raise SystemExit(f'{filename}: incomplete Atlas or competing version constants')
    if 'Interactive Trade &amp; Supply Chain Intelligence' not in text and 'Interactive Trade & Supply Chain Intelligence' not in text:
        raise SystemExit(f'{filename}: final tagline is missing')
    with tempfile.TemporaryDirectory() as temporary:
        for index, (script, kind) in enumerate(parser.scripts):
            path = Path(temporary) / f'script-{index}.{"mjs" if kind == "module" else "js"}'
            path.write_text(script, encoding='utf-8')
            subprocess.run(['node', '--check', str(path)], check=True)
    print(f'{filename}: {len(parser.scripts)} JavaScript blocks valid; {len(parser.ids)} unique IDs; all scripts bundled.')
