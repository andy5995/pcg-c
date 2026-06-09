#!/usr/bin/env python3
"""Run a check program and compare its stdout against an expected-output file.

Usage: check-output.py <program> <expected-file>

Exits 0 if the program's stdout matches the file byte-for-byte, otherwise
prints a unified diff and exits 1.
"""
import difflib
import subprocess
import sys

prog, expected = sys.argv[1], sys.argv[2]

actual = subprocess.run([prog], stdout=subprocess.PIPE).stdout
with open(expected, 'rb') as f:
    want = f.read()

if actual == want:
    sys.exit(0)

sys.stdout.writelines(
    difflib.unified_diff(
        want.decode(errors='replace').splitlines(keepends=True),
        actual.decode(errors='replace').splitlines(keepends=True),
        fromfile=expected,
        tofile='actual',
    )
)
sys.exit(1)
