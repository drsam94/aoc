import re
from random import sample
PART = 2
molecule = ""
replacements = {}

for line in open('a19.in'):
    parts = line.split(' => ')
    if len(parts) == 1:
        if len(line) > 1:
            molecule = line[:-1]
    else:
        if parts[0] not in replacements:
            replacements[parts[0]] = []
        replacements[parts[0]].append(parts[1][:-1])

def find_all_occurrences(s, substr):
    return [m.start() for m in re.finditer(substr, s)]

def insert(s, index, length, repl):
    return s[:index] + repl + s[index+length:]

def next_possibilities(start):
    possibilities = set()
    for sym in replacements:
        for repl in replacements[sym]:
            for idx in find_all_occurrences(start, sym):
                possibilities.add(insert(start, idx, len(sym), repl))
    return possibilities

def steps_to_electron(start):
    steps = 0
    while start != "e":
        oldstart = start
        for sym in sample(replacements.keys(), len(replacements)):
            for repl in sample(replacements[sym], len(replacements[sym])):
                while repl in start:
                    start,k = re.subn(repl, sym, start)
                    steps += k
        if oldstart == start:
            start = molecule
            steps = 0
    return steps

if PART == 1:
    print(len(next_possibilities(molecule)))
else:
    print(steps_to_electron(molecule))
