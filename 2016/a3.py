STEP = 2
def istri(lens):
    return all(lens[i] < (lens[(i+1)%3] + lens[(i+2)%3]) for i in range(3))

count = 0
data = []
for line in open('a3.in'):
    lens = line.strip().split(" ")
    lens = [int(l.strip()) for l in lens if l.strip()]
    data.append(lens)

for i in range(len(data) // (3 if STEP == 2 else 1)):
    if STEP == 1:
        count += istri(data[i])
    else:
        for tri in zip(*data[i*3:i*3+3]):
            count += istri(tri)

print(count)
