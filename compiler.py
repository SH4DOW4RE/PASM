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
PRINT_REG = ASMFunctions().print_reg
PRINT_REG_FUNCTION = ASMFunctions().print_reg_function
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
        index = TOKENS[0].index('NEWLINE')
        for i in range(len(TOKENS)):
            del(TOKENS[i][index])
        index = TOKENS[0].index('ENDMARKER')
        for i in range(len(TOKENS)):
            del(TOKENS[i][index])
except ValueError:
    pass

for i in range(len(TOKENS)):
    del(TOKENS[i][0:7])

strs = []
nbs = []
sst = 0
nbt = 0
printReg = False
OUTPUT = HEADER
for i in range(len(TOKENS[0])):
    if TOKENS[0][i].upper() == 'NAME' and TOKENS[1][i].lower() == 'print':
        if TOKENS[0][i+2].upper() == 'STRING': # Raw string
            text = TOKENS[1][i+2]
            OUTPUT += FUNCTIONS['print'][0] + f'str{sst}' + FUNCTIONS['print'][1] + str(len(text) - 1) + FUNCTIONS['print'][2]
            strs.append(text)
            sst += 1
        elif TOKENS[0][i+2].upper() == 'NUMBER': # Number
            number = TOKENS[1][i+2]
            OUTPUT += FUNCTIONS['print'][0] + f'nb{nbt}' + FUNCTIONS['print'][1] + str(len(number) - 1) + FUNCTIONS['print'][2]
            nbs.append(number)
            nbt += 1
        elif TOKENS[0][i+2].upper() == 'NAME': # Register
            register = str(TOKENS[1][i+2].lower())
            OUTPUT += PRINT_REG[0] + register + PRINT_REG[1]
            printReg = True
    elif TOKENS[0][i].upper() == 'NAME' and TOKENS[1][i].lower() == 'epoch':
        OUTPUT += FUNCTIONS['epoch']

OUTPUT += EXIT

if printReg: OUTPUT += PRINT_REG_FUNCTION

OUTPUT += VAR_HEADER
for i in range(len(strs)):
    OUTPUT += f'str{i}' + VAR[0] + str(strs[i]) + VAR[1]
for i in range(len(nbs)):
    OUTPUT += f'nb{i}' + VAR[0] + '"' + str(nbs[i]) + '"' + VAR[1]


if os.path.exists('modules/main'):
    os.remove('modules/main')

if os.path.exists('modules/main.asm'):
    os.remove('modules/main.asm')

with open('modules/main.asm', 'w+') as o:
    o.seek(0)
    o.write(OUTPUT)

process = subprocess.Popen(['sh', 'compile.sh'], cwd='modules', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process.wait() # Wait for process to complete.


quit()