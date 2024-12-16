with open("input.txt") as f:
    input = f.read()

out = 0

grid, movements = input.split("\n\n")

start_idx = grid.replace("\n", "").index("@")

grid = [list(row) for row in grid.splitlines()]

width = len(grid[0])
height = len(grid)

start = (start_idx % width, start_idx // width)


def move(from_x, from_y, to_x, to_y, dir):
    dx, dy = dir

    if grid[to_y][to_x] == ".":
        grid[to_y][to_x], grid[from_y][from_x] = grid[from_y][from_x], grid[to_y][to_x]
        return True

    if grid[to_y][to_x] == "#":
        return False

    if move(to_x, to_y, to_x + dx, to_y + dy, dir):
        grid[to_y][to_x], grid[from_y][from_x] = grid[from_y][from_x], grid[to_y][to_x]
        return True

    return False


dirs = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}

curr_pos = start

for movement in movements:
    if movement not in dirs:
        continue

    dir = dirs[movement]
    dx, dy = dir
    curr_x, curr_y = curr_pos
    next_x, next_y = curr_x + dx, curr_y + dy

    if move(curr_x, curr_y, next_x, next_y, dir):
        curr_pos = (next_x, next_y)

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != "O":
            continue

        out += 100 * y + x

print(out)
