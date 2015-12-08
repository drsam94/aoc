def b16(x):
    return x & ((1 << 16) - 1)

def satisfy(gate):
    if len(gate["keys"]) > 1:
        for index in [0,1]:
            z = None
            try:
                z = int(gate["keys"][0])
            except Exception:
                try:
                    z = values[gate["keys"][index]]
                except Exception:
                    pass
            if z is None: return
            gate["f"] = lambda x,y=z,f=gate["f"]: f(y,x)
            gate["keys"].pop(index)
    elif len(gate["keys"]) > 0:
        k = gate["keys"][0]
        if k in values.keys():
            values[gate["out"]] = gate["f"](values[k])
            gate["keys"].pop()


circuit = []
values = {}
def initialSetup():
    for line in open('a7.in'):
        words = line.split(' ')
        words[-1] = words[-1][:-1] # ugh newline
        if words[0] == "NOT":
            circuit.append( { "keys": [words[1]], "out" : words[3], "f" : lambda x: b16(~x) })
        elif words[1] == "RSHIFT":
            circuit.append( { "keys": [words[0]], "out" : words[4], "f" : lambda x,y=int(words[2]): b16(x>>y)})
        elif words[1] == "LSHIFT":
            circuit.append( { "keys": [words[0]], "out" : words[4], "f" : lambda x,y=int(words[2]): b16(x<<y)})
        elif words[1] == "AND":
            circuit.append( { "keys": [words[0], words[2]], "out" : words[4], "f" : lambda x,y: b16(x&y)})
        elif words[1] == "OR":
            circuit.append( { "keys": [words[0], words[2]], "out" : words[4], "f" : lambda x,y: b16(x|y)})
        elif words[1] == "->":
            try:
                values[words[2]] = b16(int(words[0]))
            except Exception:
                circuit.append( { "keys" : [words[0]], "out" : words[2], "f" : lambda x: x})
initialSetup()
while "a" not in values:
    for gate in circuit:
        satisfy(gate)
circuit = []
print(values["a"])
b = values["a"]
values = {}
initialSetup()
values["b"] = b
while "a" not in values:
    for gate in circuit:
        satisfy(gate)
print(values["a"])
