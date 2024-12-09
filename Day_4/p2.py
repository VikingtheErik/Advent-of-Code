from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    file = f.read().split('\n')
    pass

total = 0
xmas = ('')

for x in range(len(file) - 2):
    for i in range(len(file[x]) - 2):#
        xmas = ('')
        if file[x+1][i+1] == 'A':
            xmas = xmas + file[x][i] + file[x][i+2] + file[x+2][i] + file[x+2][i+2]
            if xmas in ('MMSS', 'SSMM', 'MSMS', 'SMSM'):
                total += 1

print(total)