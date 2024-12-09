from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    text = f.read().split('\n')
    pass

left = []
right = []
total = 0

for x in text:
    l, r = x.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

l = 0
r = 0

for i in left:
    r = right.count(i)
    total += r * i

print(total)