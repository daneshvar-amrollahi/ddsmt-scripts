#!/usr/bin/env python3

import signal
import subprocess
import sys


def handler(sig, frame):
    print("Aborted")
    sys.exit(1)


signal.signal(signal.SIGTERM, handler)


def run(cmd):
    cmd = cmd + [sys.argv[1]]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.stdout.decode('utf8').strip()


# Replace these with the absolute paths to your solver binaries
solverA_version1 = '/home/daneshvar/Documents/GitHub/cvc5/main-assert-checks/bin/cvc5'
solverA_version2 = '/home/daneshvar/Documents/GitHub/cvc5/wo-commut-ops-assert-checks/bin/cvc5'

# Command line options to be used with the solvers
solver_options = []

# Form the complete command for each solver
solverA_cmd = [solverA_version1] + solver_options
solverB_cmd = [solverA_version2] + solver_options

A = run(solverA_cmd)
B = run(solverB_cmd)

if A == B:
    sys.exit(0)
else:
    sys.exit(1)

# print(f'Output of main: {A}')
# print(f'Output of wo-commut-ops: {B}')


# if A not in ['sat', 'unsat']:
#     print(f'Unexpected output for A: {A}')
#     sys.exit(2)

# if B not in ['sat', 'unsat']:
#     print(f'Unexpected output for B: {B}')
#     sys.exit(2)

# print(f'{A} / {B}')
# if A == B:
#     sys.exit(0)
# else:
#     sys.exit(1)
