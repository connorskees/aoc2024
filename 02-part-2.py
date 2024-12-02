with open("input.txt") as f:
    input = f.read()

out = 0


def is_safe(elems):
    prev = elems[0]
    increasing = None

    for elem in elems[1:]:
        if abs(elem - prev) < 1 or abs(elem - prev) > 3:
            return False

        if increasing is None:
            increasing = elem > prev
        elif increasing != (elem > prev):
            return False

        prev = elem

    return True


for line in input.splitlines():
    elems = [int(s) for s in line.split()]

    if is_safe(elems) or any(
        is_safe(elems[:idx] + elems[idx + 1 :]) for idx in range(len(elems))
    ):
        out += 1

print(out)
