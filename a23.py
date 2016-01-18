PART = 2
insts = [inst[:-1].replace(",","").split(" ") for inst in open('a23.in')]

reg = { "a" : 0 if PART == 1 else 1, "b" : 0 }
pc = 0
while 0 <= pc < len(insts):
    inst = insts[pc]
    code = inst[0]
    r = inst[1]
    if not code.startswith("j"):
        if code == "hlf":
            reg[r] //= 2
        elif code == "tpl":
            reg[r] *= 3
        elif code == "inc":
            reg[r] += 1
        pc += 1
    else:
        offset = int(inst[-1])
        if code == "jmp":
            pc += offset
        elif code == "jie":
            pc += offset if reg[r] % 2 == 0 else 1
        elif code == "jio":
            pc += offset if reg[r] == 1 else 1
print(reg["b"])
