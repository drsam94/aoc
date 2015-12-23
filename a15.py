PART = 2
highest_score = 0
ingredients = []
for line in open('a15.in'):
    words = line.split(' ')
    ingredients.append([int(words[k][:-1]) for k in (2,4,6,8,10)])

for i in range(100**(len(ingredients) - 1)):
    def coeff(j):
        if j == len(ingredients) - 1:
            return 100 - sum(coeff(k) for k in range(j))
        else:
            return (i//(100**j))%(100)

    props = [sum(coeff(k)*ingredients[k][prop]
             for k in range(len(ingredients)))
             for prop in range(len(ingredients[0]))]
    prod = 1
    for factor in props[:-1]:
        prod *= max(factor,0)
    if PART == 1 or props[-1] == 500:
        highest_score = max(highest_score, prod)
print(highest_score)
