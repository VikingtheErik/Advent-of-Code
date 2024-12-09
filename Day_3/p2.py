from pathlib import Path
import regex as re
HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    file = f.read()
    pass

uncorruptedRegex = re.compile(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)')
active = True
total = 0
for do, dont, a, b in uncorruptedRegex.findall(file):
    if do:
        active = True
    elif dont:
        active = False
    elif active:
        total += int(a) * int(b)

print(total)
