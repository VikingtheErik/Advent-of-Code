from pathlib import Path

HOME = Path(__file__).parent

with open(HOME/"test.txt") as f:
    rules, allpages = map(str.splitlines, f.read().split('\n\n'))
    pass

rule_dictionary = {}
for rule in rules:
    key, value = map(int, rule.split('|'))
    rule_dictionary.setdefault(key, []).append(value)


for pagesstring in allpages:
    pages = list(map(int, pagesstring.split(',')))
    for index, page in enumerate(pages):
        for index 