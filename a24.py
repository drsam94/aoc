PART=2
def qe(lst):
    res = 1
    for num in lst:
        res *= num
    return res

weights = [int(line[:-1]) for line in open('a24.in')]
target_sum = sum(weights) // (2 + PART)
min_qe  = float("inf")
min_num = float("inf")

def optimal_qe(rest, optSet):
    global min_num, min_qe #pylint: disable=global-statement
    if sum(optSet) == target_sum:
        if len(optSet) < min_num:
            min_num = len(optSet)
            min_qe = qe(optSet)
        elif len(optSet) == min_num:
            min_qe = min(min_qe, qe(optSet))
    elif len(optSet) > min_num:
        return
    elif sum(optSet) > target_sum:
        return
    elif len(rest) == 0:
        return
    else:
        optimal_qe(rest[1:], optSet + [rest[0]])
        optimal_qe(rest[1:], optSet)

optimal_qe(weights, [])
print(min_qe)
