import bisect

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


row_wise = [[] for _ in range(height)]
col_wise = [[] for _ in range(width)]

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != "#":
            continue

        row_wise[y].append(x)
        col_wise[x].append(y)


def closest_for_dir(x, y, dir) -> tuple[int, int]:
    oob = (-1, -1)
    if dir == UP:
        arr = col_wise[x]
        candidate = bisect.bisect_left(arr, y)

        if candidate == 0:
            return oob

        return (x, arr[candidate - 1] + 1)
    elif dir == DOWN:
        arr = col_wise[x]
        candidate = bisect.bisect_left(arr, y)

        if candidate >= len(arr):
            return oob

        return (x, arr[candidate] - 1)
    elif dir == LEFT:
        arr = row_wise[y]
        candidate = bisect.bisect_left(arr, x)

        if candidate == 0:
            return oob

        return (arr[candidate - 1] + 1, y)
    elif dir == RIGHT:
        arr = row_wise[y]
        candidate = bisect.bisect_left(arr, x)

        if candidate >= len(arr):
            return oob

        return (arr[candidate] - 1, y)


def has_loop():
    curr_pos = start

    visited = set()

    dir = UP

    while is_valid(*curr_pos):
        x, y = curr_pos

        key = (x, y, dir)

        if key in visited:
            return True

        visited.add(key)

        x, y = closest_for_dir(x, y, dir)

        if not is_valid(x, y):
            break

        dir = rotate[dir]
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
    insert_y = bisect.bisect_left(col_wise[x], y)
    insert_x = bisect.bisect_left(row_wise[y], x)
    row_wise[y].insert(insert_x, x)
    col_wise[x].insert(insert_y, y)

    if has_loop():
        out += 1

    del row_wise[y][insert_x]
    del col_wise[x][insert_y]

print(out)
