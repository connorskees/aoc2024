with open("input.txt") as f:
    input = f.read()

out = []

registers, program = input.split("\n\n")

a, b, c = [int(reg.split(": ")[1]) for reg in registers.splitlines()]

program = [int(op) for op in program.split(": ")[1].split(",")]

ip = 0


def combo():
    val = program[ip + 1]

    if val <= 3:
        return val

    return [a, b, c][val - 4]


while ip < len(program):
    opcode = program[ip]
    literal = program[ip + 1]

    if opcode == 0:  # adv
        a = int(a / 2 ** combo())
    elif opcode == 1:  # bxl
        b ^= literal
    elif opcode == 2:  # bst
        b = combo() % 8
    elif opcode == 3:  # jnz
        if a != 0:
            ip = literal
            continue
    elif opcode == 4:  # bxc
        b ^= c
    elif opcode == 5:  # out
        out.append(str(combo() % 8))
    elif opcode == 6:  # bdv
        b = int(a / 2 ** combo())
    elif opcode == 7:  # cdv
        c = int(a / 2 ** combo())

    ip += 2

print(",".join(out))
