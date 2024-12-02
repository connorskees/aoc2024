with open("input.txt") as f:
    input = f.read()

out = 0

for line in input.splitlines():
    elems = [int(s) for s in line.split()]

    prev = elems[0]
    increasing = None
    for elem in elems[1:]:
        if abs(elem - prev) < 1 or abs(elem - prev) > 3:
            break

        if increasing is None:
            increasing = elem > prev
        elif increasing != (elem > prev):
            break

        prev = elem
    else:
        out += 1

print(out)
