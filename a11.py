alph = list(map(chr, range(ord('a'), ord('z') + 1)))

def itos(n):
    s = ""
    while n > 0:
        s = alph[n%26] + s
        n //= 26
    return s

def stoi(s):
    n = 0
    for i,c in enumerate(s):
        n += (ord(c) - ord('a')) * 26**(len(s) - i - 1)
    return n

def cinc(c,x):
    return chr(ord(c) + x)

def winc(w):
    return itos(stoi(w) + 1)

def nextpw(pw):
    pw = winc(pw)

    while(any(c in pw for c in 'iol') or
         (not any(c + cinc(c,1) + cinc(c,2) in pw for c in alph[:-2])) or
         (sum(pw.count(c*2) for c in alph) < 2)):
        pw = winc(pw)
    return pw

if __name__ == "__main__":
    pw = "cqjxjnds"
    pw = nextpw(pw)
    print(pw)
    print(nextpw(pw))
