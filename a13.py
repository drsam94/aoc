from itertools import permutations
PART = 2
data = {}
for line in open('a13.in'):
    # kill newline and ending '.'
    words = line[:-2].split(' ')
    source    = words[0]
    amount    = int(words[3]) * (1 if words[2] == "gain" else -1)
    dest      = words[-1]
    if source not in data:
        data[source] = { "me" : 0 }
    data[source][dest] = amount

if PART == 2:
    data["me"] = { k:0 for k in data}

N = len(data)
print(max(sum(data[p[i]][p[(i+1)%N]] + data[p[i]][p[(i-1)%N]] for i in range(N))
    for p in permutations(data.keys())))
