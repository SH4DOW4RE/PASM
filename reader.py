# Python Compiler for Linux
from tokenize import tokenize, tok_name
from io import BytesIO
import os
import subprocess

# Internal Modules
from modules.asm_functions import ASMFunctions


HEADER = ASMFunctions().header
VAR_HEADER = ASMFunctions().var_header
VAR = ASMFunctions().var
EXIT = ASMFunctions().exit
FUNCTIONS = ASMFunctions().functions


with open('script.py', 'r') as f:
    f.seek(0)
    lines = f.readlines()

toks = []

for i in range(len(lines)):
    toks.append(tokenize(BytesIO(lines[i].encode('utf-8')).readline))

tokens = []

for l in range(len(lines)):
    for t in range(len(toks)):
        for token in toks[l]:
            tokens.append(token)

TOKENS = [
    [], # TYPE
    [], # STRING
    [], # START
    []  # END
]

for i in range(len(tokens)):
    TOKENS[0].append(tok_name[tokens[i].type])
    TOKENS[1].append(tokens[i].string)
    TOKENS[2].append(tokens[i].start)
    TOKENS[3].append(tokens[i].end)

try:
    while 1:
        index = TOKENS[0].index('ENCODING')
        for i in range(len(TOKENS)):
            del(TOKENS[i][index])
except ValueError:
    pass

try:
    while 1:
        index = TOKENS[0].index('NEWLINE')
        for i in range(len(TOKENS)):
            del(TOKENS[i][index])
except ValueError:
    pass

try:
    while 1:
        index = TOKENS[0].index('ENDMARKER')
        for i in range(len(TOKENS)):
            del(TOKENS[i][index])
except ValueError:
    pass

for i in range(len(TOKENS)):
    del(TOKENS[i][0:7])

print(TOKENS)