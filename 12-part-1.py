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

    return len([p for p in perimeter if p not in cells])


for group in groups:
    out += compute_perimeter(group) * len(group)

print(out)
