row = 2978
column = 3083

def tri(n):
    return (n * (n + 1))//2

def index(r, c):
    diag = r + c - 1
    return (diag + 1 - r) + tri(diag - 1)

def value(index):
    v = 20151125
    for _ in range(index - 1):
        v *= 252533
        v %= 33554393
    return v

print(value(index(row, column)))
