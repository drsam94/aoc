PART = 2
amounts = [int(line[:-1]) for line in open('a17.in')]
if PART == 1:
    print(sum(150==sum(amounts[k]*((N>>k)&1) for k in range(len(amounts)))
          for N in range(2**len(amounts))))
else:
    amounts_per_num = { i : 0 for i in range(len(amounts)+1) }
    for N in range(2**len(amounts)):
        amounts_per_num[sum((N>>k)&1 for k in range(len(amounts)))] += 150==sum(
                amounts[k]*((N>>k)&1) for k in range(len(amounts)))
    print(amounts_per_num[min(k for k,v in amounts_per_num.items() if v > 0)])
