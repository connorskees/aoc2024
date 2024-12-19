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
        return True

    for idx in range(len(towel) + 1):
        if towel[:idx] in towels and is_possible(towel[idx:]):
            return True
    return False


out = sum(is_possible(pat) for pat in patterns)

print(out)
