import collections
STEP = 2
print ''.join(map(lambda x: collections.Counter(''.join(x)).most_common()[0 if STEP == 1 else -1][0],
map(lambda x: ''.join(x), zip(*map(lambda x: x.strip(), open('a6.in'))))))
