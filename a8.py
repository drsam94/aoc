import json
a = 0
b = 0
for line in open('a8.in'):
    a += len(line) - 1 - len(eval(line))
    b += len(json.dumps(line)) - len(line) - 1
print(a)
print(b)
