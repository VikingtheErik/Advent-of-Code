from pathlib import Path
import regex as re

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    file = f.read().split('\n')
    pass

total = 0
XMASRegex = re.compile(r'XMAS')
SAMXRegex = re.compile(r'SAMX')

for row in file:
    total += len(XMASRegex.findall(row))
    total += len(SAMXRegex.findall(row))

for x in range(len(file)):
    if x <= len(file) - 4:
        for i in range(len(file[x])):
            if file[x][i] + file[x+1][i] + file[x+2][i] + file[x+3][i] in ('XMAS', 'SAMX'):
                total += 1
            if (i >= 3) and (file[x][i] + file[x+1][i-1] + file[x+2][i-2] + file[x+3][i-3] in ('XMAS', 'SAMX')):
                total += 1
            if (i <= len(file[x]) - 4) and (file[x][i] + file[x+1][i+1] + file[x+2][i+2] + file[x+3][i+3] in ('XMAS', 'SAMX')):
                total += 1

print(total)