from pathlib import Path
import regex as re

HOME = Path(__file__).parent

with open(HOME/"input.txt") as f:
    file = f.read()
    pass

print(sum(int(a) * int(b) for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', file)))