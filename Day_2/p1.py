from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    file = f.read().split('\n')
    pass


safe = 0


for x in file:
    increasing = False
    x = x.split(' ')
    x = list(map(int, x))
    if x[0] < x[1]:
        increasing = True
    for i in range(len(x) - 1):
        T = False
        if not (0 < abs(x[i] - x[i+1]) <= 3):
            break
        if x[i] < x[i+1] and increasing == False:
            break
        if x[i] > x[i+1] and increasing == True:
            break
        T = True
    if T == True:
        safe += 1

print(safe)