
def race1(deer, time):
    dist = 0
    while time > 0:
        nextRun = min(time, deer["time"])
        dist += nextRun * deer["speed"]
        time -= nextRun + deer["rest"]
    return dist

def race2(deerList, time):
    for d in deerList:
        d["counter"]  = d["time"]
        d["distance"] = 0
        d["resting"]  = False
        d["points"]   = 0
    for t in range(time):
        for d in deerList:
            if not d["resting"]:
                d["distance"] += d["speed"]
                d["counter"] -= 1
                d["resting"] = d["counter"] == 0
            else:
                d["counter"] += 1
                d["resting"] = d["counter"] < d["rest"]
                if not d["resting"]:
                    d["counter"] = d["time"]


        bestDeer = { "distance" : 0 }
        for d in deerList:
            if d["distance"] > bestDeer["distance"]:
                bestDeer = d
        bestDeer["points"] += 1

deer = []
for line in open('a14.in'):
    words = line.split(' ')
    deer.append({
        "speed" : int(words[3]),
        "time"  : int(words[6]),
        "rest"  : int(words[13]) })


print(max(race1(d, 2503) for d in deer))
race2(deer, 2503)
print(max(d["points"] for d in deer))
