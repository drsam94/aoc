import hashlib
z = 0
k = 6
h = hashlib.md5().hexdigest()
while h[0:k] != "0" * k:
    h = hashlib.md5(("yzbqklnj" + str(z)).encode()).hexdigest()
    z += 1
print(z)
