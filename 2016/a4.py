SPLIT = 2
def getCS(data):
    cs = list(set(data))
    cs.sort()
    cs.sort(key=lambda c: -data.count(c))
    return ''.join(cs[:5])

def cipher(data, sector):
    return ''.join([chr(ord('a') + (ord(c) - ord('a') + sector) % 26) for c in data])

ans = 0
for line in open('a4.in'):
    first, csum = line.split('[')
    csum = csum[:csum.find(']')]
    splits = first.split('-')
    data = ''.join(splits[:-1])
    sector = int(splits[-1])
    if getCS(data) == csum:
        if SPLIT == 1:
            ans += sector
        else:
            if 'pole' in cipher(data, sector):
                print(sector)
                break
if SPLIT == 1:
    print(ans)

