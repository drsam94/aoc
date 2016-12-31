import md5
STEP = 2
puzzleInput = 'ffykfhsq'
out = list('________')
i = 0
index = 0
while i < 8:
    m = md5.new()
    m.update("%s%d" % (puzzleInput, index))
    dig = m.hexdigest()
    if all(c == '0' for c in dig[0:5]):
        if STEP == 1:
            out[i] = dig[5]
        if STEP == 2:
            spot = int(dig[5], 16)
            if spot > 7 or out[spot] != '_': 
                index += 1
                continue
            out[spot] = dig[6]
        i += 1
        print ''.join(out), index, i
    index += 1
print ''.join(out)
