from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    file = f.read().split('\n')
    pass

safe = 0

def check_line(x):
    if x[0] < x[1]:
        increasing = True
    elif x[0] > x[1]:
        increasing = False
    else:
        return False
    for i in range(len(x) - 1):
        if not (0 < abs(x[i] - x[i+1]) <= 3):
            return False
        if x[i] < x[i+1] and increasing == False:
            return False
        if x[i] > x[i+1] and increasing == True:
            return False
    return True

for x in file:
    badLevel = 0
    x = x.split(' ')
    x = list(map(int, x))
    for place, value in enumerate(x):
        del(x[place])
        if check_line(x) == True:
            badLevel += 1
        x.insert(place, value)
    if badLevel > 0:
        print(x)
        safe += 1

print(safe)
