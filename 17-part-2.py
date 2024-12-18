# ruff: noqa: F403, F405

from z3 import *

with open("input.txt") as f:
    input = f.read()

out = []

registers, program = input.split("\n\n")

_, b, c = [int(reg.split(": ")[1]) for reg in registers.splitlines()]

program = [int(op) for op in program.split(": ")[1].split(",")]

a = BitVec("a", 64)
b = BitVecVal(b, 64)
c = BitVecVal(c, 64)

orig_a = a


def simulate(a, b, c, target):
    ip = 0

    out = None

    def combo():
        val = program[ip + 1]

        if val <= 3:
            return val

        return [a, b, c][val - 4]

    while ip < len(program):
        opcode = program[ip]
        literal = program[ip + 1]

        if opcode == 0:  # adv
            a = a >> combo()
        elif opcode == 1:  # bxl
            b ^= literal
        elif opcode == 2:  # bst
            b = combo() & 0b111
        elif opcode == 3:  # jnz
            return [a, b, c, out]
        elif opcode == 4:  # bxc
            b ^= c
        elif opcode == 5:  # out
            out = (combo() & 0b111) == target
        elif opcode == 6:  # bdv
            b = a >> combo()
        elif opcode == 7:  # cdv
            c = a >> combo()

        ip += 2

    return [a, b, c, out]


s = Solver()

for idx, e in enumerate(program):
    a, b, c, expr = simulate(a, b, c, e)

    s.add(expr)

    if idx == len(program) - 1:
        s.add(a == 0)

while s.check() == sat:
    print(s.model()[orig_a])
    s.add(orig_a < s.model()[orig_a])
