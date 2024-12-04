with open("input.txt") as f:
    input = f.read()


out = 0

lines = input.splitlines()

width = len(lines[0])
height = len(lines)

for line in lines:
    out += line.count("XMAS") + line.count("SAMX")

for idx in range(width):
    col = "".join(line[idx] for line in lines)

    out += col.count("XMAS") + col.count("SAMX")


def count_diag(x_range, y_range):
    diag = "".join(lines[y][x] for x, y in zip(x_range, y_range))
    return diag.count("XMAS") + diag.count("SAMX")


# X..
# .M.
for x in range(width):
    out += count_diag(range(x, width), range(height))

# ..X
# .M.
for x in range(width):
    out += count_diag(range(x + 1)[::-1], range(height))

# ...
# X..
# .M.
for y in range(1, height):
    out += count_diag(range(width), range(y, height))

# ...
# ..X
# .M.
for y in range(1, height):
    out += count_diag(range(width)[::-1], range(y, height))

print(out)
