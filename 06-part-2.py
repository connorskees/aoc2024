from collections import defaultdict

with open("input.txt") as f:
    input = f.read()

out = 0

visited = set()

grid = [list(line) for line in input.splitlines()]

width = len(grid[0])
height = len(grid)

start_idx = input.replace("\n", "").index("^")

start = (start_idx % width, start_idx // height)

RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
UP = (0, -1)

rotate = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}


def is_valid(x, y):
    return x >= 0 and y >= 0 and x < width and y < height


def has_loop():
    curr_pos = start

    visited = defaultdict(set)

    dir = UP

    while is_valid(*curr_pos):
        x, y = curr_pos

        if dir in visited[(x, y)]:
            return True

        visited[(x, y)].add(dir)

        dx, dy = dir

        x += dx
        y += dy

        if not is_valid(x, y):
            break

        new_val = grid[y][x]

        if new_val == "#":
            dir = rotate[dir]
        else:
            curr_pos = (x, y)

    return False


def candidate_obstacle_coords() -> list[tuple[int, int]]:
    curr_pos = start

    visited = set()

    dir = UP

    while is_valid(*curr_pos):
        x, y = curr_pos

        visited.add((x, y))

        dx, dy = dir

        x += dx
        y += dy

        if not is_valid(x, y):
            break

        new_val = grid[y][x]

        if new_val == "#":
            dir = rotate[dir]
        else:
            curr_pos = (x, y)

    return list(visited)


for x, y in candidate_obstacle_coords():
    prev = grid[y][x]
    grid[y][x] = "#"

    if has_loop():
        out += 1

    grid[y][x] = prev

print(out)
