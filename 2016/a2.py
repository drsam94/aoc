STEP = 2
if STEP == 1:
    pad = ['123', '456', '789']
else: 
    pad = [ 'XX1XX', 'X234X', '56789', 'XABCX', 'XXDXX' ]

pos = (1,1)
def safeadd(t1, t2):
    t3 = tupleadd(t1, t2)
    if 0 <= t3[0] < len(pad) and 0 <= t3[1] < len(pad[t3[0]]) and pad[t3[0]][t3[1]] != 'X':
        return t3
    else:
        return t1

def tupleadd(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def safemove(pos, c):
    return safeadd(pos, {'U': (-1, 0), 'D': (1, 0), 'L' : (0, -1), 'R' : (0, 1)}[c])
out = ""
for line in open('a2.in'):
    for c in line:
        if c in 'UDLR':
            pos = safemove(pos, c)
    out += pad[pos[0]][pos[1]]
print(out)

