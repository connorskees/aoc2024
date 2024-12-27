with open("input.txt") as f:
    input = f.read()

out = 0

grids = [grid.split("\n") for grid in input.split("\n\n")]

width = len(grids[0][0])
height = len(grids[0])

keys = []
locks = []

for grid in grids:
    heights = []
    for x in range(width):
        y = 0
        init = grid[y][x]
        while grid[y][x] == init:
            y += 1
        if init == ".":
            heights.append(height - y - 1)
        else:
            heights.append(y - 1)

    if grid[0][0] == "#":
        keys.append(heights)
    else:
        locks.append(heights)

for key in keys:
    for lock in locks:
        if all(kk + ll < height - 1 for kk, ll in zip(key, lock)):
            out += 1


print(out)
