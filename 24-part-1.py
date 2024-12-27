from z3 import *

with open("input.txt") as f:
    input = f.read()

out = 0

values, gates = input.split("\n\n")

init_values = {
    k: int(v) for k, v in [value.split(": ") for value in values.splitlines()]
}

vars = {}


def get_var(name: str) -> BitVecRef:
    if name not in vars:
        vars[name] = BitVec(name, 1)
    return vars[name]


exprs = []
zs = []

for k, v in init_values.items():
    k_var = get_var(k)
    exprs.append(k_var == v)
    if k.startswith("z"):
        zs.append((k, k_var))

for gate in gates.splitlines():
    a_name, op, b_name, _, val_name = gate.split()

    a = get_var(a_name)
    b = get_var(b_name)

    val = get_var(val_name)

    if op == "OR":
        expr = a | b
    elif op == "AND":
        expr = a & b
    elif op == "XOR":
        expr = a ^ b

    exprs.append(expr == val)

    if a_name.startswith("z"):
        zs.append((a_name, a))
    if b_name.startswith("z"):
        zs.append((b_name, b))
    if val_name.startswith("z"):
        zs.append((val_name, val))

s = Solver()

for expr in exprs:
    s.add(expr)

s.check()

z = 0

for z_name, z_bit in zs:
    bit = int(z_name[1:])
    z |= s.model()[z_bit].as_long() << bit

print(z)
