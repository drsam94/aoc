import operator
PART = 2
sues = []
for line in open('a16.in'):
    words = line.split(' ')
    sues.append({ words[i][:-1] : int(words[i+1][:-1]) for i in [2,4,6]})

data = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
        }
ops = { key : (operator.eq if PART == 1 else
               (operator.gt if key in ["cats","trees"] else (
                operator.lt if key in ["pomeranians","goldfish"] else
                operator.eq))) for key in data }
for (i, sue) in enumerate(sues):
    if all(ops[key](sue[key],data[key]) for key in sue):
        print(i + 1)
        break
