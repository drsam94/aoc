PART = 2
on     = lambda x: x + 1 if PART == 2 else 1
off    = lambda x: max(0, x - 1) if PART == 2 else 0
toggle = lambda x : x + 2 if PART == 2 else not x
lights = [ [0]*1000 for x in range(1000)]
for line in open('a6.in'):
    l = line.split(' ')
    if line.startswith("turn off"):
        f = off
        l = l[2:]
    elif line.startswith("turn on"):
        f = on
        l = l[2:]
    else:
        f = toggle
        l = l[1:]
    x1,y1 = map(int,l[0].split(','))
    x2,y2 = map(int,l[2].split(','))

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            lights[x][y] = f(lights[x][y])

print(sum(lights[x][y] for x in range(1000) for y in range(1000)))
