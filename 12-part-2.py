with open("input.txt") as f:
    input = f.read()

out = 0

groups = []

grid = input.splitlines()

width = len(grid[0])
height = len(grid)

visited = set()

is_valid = lambda x, y: x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)


def visit_group(x, y):
    target_char = grid[y][x]

    queue = [(x, y)]

    group = []

    while queue:
        x, y = queue.pop()

        if (x, y) in visited or not is_valid(x, y) or grid[y][x] != target_char:
            continue

        visited.add((x, y))

        group.append((x, y))

        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))

    if group:
        groups.append(group)


for x in range(width):
    for y in range(height):
        visit_group(x, y)


def compute_perimeter(group: list[int]):
    cells = set(group)

    perimeter = []

    for x, y in group:
        perimeter.append((x + 1, y))
        perimeter.append((x - 1, y))
        perimeter.append((x, y + 1))
        perimeter.append((x, y - 1))

    perimeter = set(perimeter) - cells

    min_x = min(group, key=lambda cell: cell[0])[0]
    max_x = max(group, key=lambda cell: cell[0])[0]

    min_y = min(group, key=lambda cell: cell[1])[1]
    max_y = max(group, key=lambda cell: cell[1])[1]

    vertical_sides = 0

    # left
    for x in range(min_x, max_x + 1):
        y = min_y
        col_len = 0

        while y <= max_y:
            if (x - 1, y) not in perimeter or (x, y) not in cells:
                y += 1
                vertical_sides += col_len > 0
                col_len = 0
                continue

            col_len += 1
            y += 1

        vertical_sides += col_len > 0

    # right
    for x in range(min_x, max_x + 1):
        y = min_y
        col_len = 0

        while y <= max_y:
            if (x + 1, y) not in perimeter or (x, y) not in cells:
                y += 1
                vertical_sides += col_len > 0
                col_len = 0
                continue

            col_len += 1
            y += 1

        vertical_sides += col_len > 0

    horizontal_sides = 0

    # above
    for y in range(min_y, max_y + 1):
        x = min_x
        row_len = 0

        while x <= max_x:
            if (x, y - 1) not in perimeter or (x, y) not in cells:
                x += 1
                horizontal_sides += row_len > 0
                row_len = 0
                continue

            row_len += 1
            x += 1

        horizontal_sides += row_len > 0

    # below
    for y in range(min_y, max_y + 1):
        x = min_x
        row_len = 0

        while x <= max_x:
            if (x, y + 1) not in perimeter or (x, y) not in cells:
                x += 1
                horizontal_sides += row_len > 0
                row_len = 0
                continue

            row_len += 1
            x += 1

        horizontal_sides += row_len > 0

    return vertical_sides + horizontal_sides


for group in groups:
    out += compute_perimeter(group) * len(group)

print(out)
