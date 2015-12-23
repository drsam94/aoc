PART = 2
if PART == 1:
    x = 1
    presents = 0
    while presents < 29000000:
        presents = 0
        x += 1
        for d in range(1, int(x**0.5)):
            if x % d == 0:
                presents += 10*(d + x//d)
        if int(x**0.5)**2 == x:
            presents += 10*x**0.5
    print(x)
else:
    houses = [0 for i in range(100000000)]
    for e in range(1,len(houses)//50):
        for k in range(1, 51):
            houses[e*k] += e*11
    for i, val in enumerate(houses):
        if val >= 29000000:
            print(i)
            break
