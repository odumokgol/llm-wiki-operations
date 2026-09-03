#!/usr/bin/env python3
"""Fail on common secret/private-file patterns before a handbook commit."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "node_modules", ".venv", "venv"}
PATTERNS = [
    re.compile(r"(^|/)\.env(\.|$)", re.I),
    re.compile(r"(token|password|passwd|secret|api[_-]?key|oauth)", re.I),
    re.compile(r"(CHAT-|SUM-|session-export|credentials?)", re.I),
]

bad = []
for p in ROOT.rglob("*"):
    if any(part in SKIP for part in p.parts) or not p.is_file():
        continue
    rel = p.relative_to(ROOT).as_posix()
    if any(rx.search(rel) for rx in PATTERNS):
        bad.append(rel)

if bad:
    print("Potentially unsafe filenames:")
    print("\n".join(sorted(bad)))
    sys.exit(1)
print("SAFE_FILENAME_SCAN_OK")
