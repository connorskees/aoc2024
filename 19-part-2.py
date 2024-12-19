import functools

with open("input.txt") as f:
    input = f.read()

out = 0

towels, patterns = input.split("\n\n")

towels = set(towels.split(", "))
patterns = patterns.splitlines()


@functools.cache
def is_possible(towel):
    if not towel:
        return 1

    n = 0

    for idx in range(len(towel) + 1):
        if towel[:idx] in towels:
            n += is_possible(towel[idx:])
    return n


out = sum(is_possible(pat) for pat in patterns)

print(out)
