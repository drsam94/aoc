x = "3113322113"
for _ in range(50):
    split = [[x[0]]]
    for i in range(len(x) - 1):
        if x[i+1] == x[i]:
            split[-1].append(x[i+1])
        else:
            split.append([x[i+1]])
    x = ""
    for seq in split:
        x += "%d%s" % (len(seq), seq[0])
print(len(x))
