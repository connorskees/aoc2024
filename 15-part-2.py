with open("input.txt") as f:
    input = f.read()

out = 0

grid, movements = input.split("\n\n")


def map_row(row: str) -> list[str]:
    new_row = []

    for c in row:
        if c == "O":
            new_row += "[]"
        elif c == "@":
            new_row += "@."
        else:
            new_row += c * 2

    return new_row


grid = [map_row(row) for row in grid.splitlines()]

width = len(grid[0])
height = len(grid)

row, start_y = next((row, y) for y, row in enumerate(grid) if "@" in row)
start = (row.index("@"), start_y)


def move_horizontal(from_x, from_y, to_x, to_y, dir):
    dx, _ = dir

    if grid[to_y][to_x] == ".":
        grid[to_y][to_x], grid[from_y][from_x] = grid[from_y][from_x], grid[to_y][to_x]
        return True

    if grid[to_y][to_x] == "#":
        return False

    if grid[to_y][to_x] in "[]":
        if move_horizontal(to_x + dx, to_y, to_x + dx + dx, to_y, dir):
            grid[to_y][to_x + dx], grid[to_y][to_x] = (
                grid[to_y][to_x],
                grid[to_y][to_x + dx],
            )
            grid[to_y][to_x], grid[from_y][from_x] = (
                grid[from_y][from_x],
                grid[to_y][to_x],
            )
            return True

    return False


def move_vertical(x, y, dir):
    _, dy = dir
    queue = [(x, y)]
    to_move = []

    while queue:
        x, y = queue.pop()

        to_move.append((x, y))

        if grid[y + dy][x] == ".":
            continue

        if grid[y + dy][x] == "#":
            return False

        if grid[y + dy][x] == "[":
            queue.append((x, y + dy))
            queue.append((x + 1, y + dy))

        if grid[y + dy][x] == "]":
            queue.append((x, y + dy))
            queue.append((x - 1, y + dy))

    visited = set()

    while to_move:
        x, y = to_move.pop()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        grid[y][x], grid[y + dy][x] = grid[y + dy][x], grid[y][x]

    return True


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

    if movement in "<>":
        if move_horizontal(*curr_pos, curr_pos[0] + dx, curr_pos[1] + dy, dir):
            curr_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
    elif movement in "^v":
        if move_vertical(*curr_pos, dir):
            curr_pos = (curr_pos[0] + dx, curr_pos[1] + dy)


for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != "[":
            continue

        out += 100 * y + x

print(out)
