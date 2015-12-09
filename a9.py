import itertools
graph = {}
for line in open('a9.in'):
    source,_,dest,_,dist = line[:-1].split(' ')
    dist = int(dist)
    if source not in graph:
        graph[source] = {}
    if dest not in graph:
        graph[dest] = {}
    graph[source][dest] = dist
    graph[dest][source] = dist

lengths = [sum(graph[p[i]][p[i+1]] for i in range(len(p)-1))
            for p in itertools.permutations(graph.keys())]
print(min(lengths))
print(max(lengths))
