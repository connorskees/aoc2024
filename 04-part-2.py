with open("input.txt") as f:
    input = f.read()


out = 0

lines = input.splitlines()

width = len(lines[0])
height = len(lines)

for x in range(1, width - 1):
    for y in range(1, height - 1):
        if lines[y][x] != "A":
            continue

        valid_vals = [("S", "M"), ("M", "S")]

        top_left = lines[y - 1][x - 1]
        bottom_right = lines[y + 1][x + 1]
        if (top_left, bottom_right) not in valid_vals:
            continue

        top_right = lines[y - 1][x + 1]
        bottom_left = lines[y + 1][x - 1]
        if (top_right, bottom_left) not in valid_vals:
            continue

        out += 1

print(out)
