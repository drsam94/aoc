STEP = 2
# Not the world's most elegant code for line intersections
def intsct(lines, newline):
    for line in lines:
        if line[0][0] == line[1][0]:
            # vertical line
            if (((newline[0][0] - line[0][0]) * (newline[1][0] - line[0][0]) < 0) and
                min(line[0][1], line[1][1]) <= newline[0][1] <= max(line[0][1], line[1][1])):
                print (line, newline)
                return [line[0][0], newline[0][1]]
        else:
            # horizontal line
            if (((newline[0][1] - line[0][1]) * (newline[1][1] - line[0][1]) < 0) and
                min(line[0][0], line[1][0]) <= newline[0][0] <= max(line[0][0], line[1][0])):
                print (line, newline)
                return [line[0][1], newline[0][0]]
    return None

instructions = open('a1.in').read()[:-1].replace(" ", "").split(",")
pos = [0,0]
d = 0 # 0,1,2,3 => NESW
lines = []
for ins in instructions:
    if ins[0] == 'R':
        d += 1;
    else:
        d -= 1;
    
    d %= 4;

    oldpos = pos[:]
    pos[(d+1)%2] += (-1)**(d // 2) * int(ins[1:])
    intersect = intsct(lines, [oldpos, pos])
    if STEP == 2 and intersect is not None:
        print(abs(intersect[0]) + abs(intersect[1]))
        break
    lines.append([oldpos, pos[:]])
if STEP == 1: print(abs(pos[0]) + abs(pos[1]))
