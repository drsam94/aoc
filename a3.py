p1 = (0,0)
p2 = (0,0)
houses = {(0,0)}

j = 0
for c in open('a3.in').read():
    if c == '\n': continue
    i = {'>' : 0, 'v' : 1, '<' : 2, '^' : 3 }[c]
    x = [p1,p2][j%2][0] + [1,0,-1,0][i]
    y = [p1,p2][j%2][1] + [0,-1,0,1][i]
    houses.add((x,y))
    if j%2==0:
        p1 = (x,y)
    elif j%2==1:
        p2 = (x,y)
    j += 1
print(len(houses))
