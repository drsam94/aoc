PART = 2
def next_gen(old):
    new = [ [0 for o in ol] for ol in old]
    for i in range(len(old)):
        for j in range(len(old[0])):
            N = neighbors(old,i,j)
            new[i][j] = 0 if N<2 else (
                        old[i][j] if N == 2 else (
                        1 if N == 3 else 0))
    return new

def neighbors(grid,i,j):
    d = lambda x: ([] if x == 0 else [-1]) + [0] + ([] if x == len(grid) - 1 else [1])
    return sum(grid[i + di][j + dj] for di in d(i) for dj in d(j)) - grid[i][j]

grid = [ ['#'==c for c in line[:-1]] for line in open('a18.in')]

if PART == 2:
    grid[0][0],grid[0][-1],grid[-1][0],grid[-1][-1] = (1,1,1,1)
for gen in range(100):
    grid = next_gen(grid)
    if PART == 2:
        grid[0][0],grid[0][-1],grid[-1][0],grid[-1][-1] = (1,1,1,1)

print(sum(sum(grid,[])))
