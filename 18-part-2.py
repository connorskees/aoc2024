from collections import deque

with open("input.txt") as f:
    input = f.read()

out = 0

bytes = []
for row in input.splitlines():
    x, y = row.split(",")
    bytes.append((int(x), int(y)))

width = 71
height = 71

is_valid = lambda x, y: x >= 0 and y >= 0 and x < width and y < height

grid = [["."] * width for _ in range(height)]


def has_exit():
    queue = deque([(0, 0, 0)])
    visited = set()

    while queue:
        x, y, dist = queue.popleft()

        if not is_valid(x, y) or (x, y) in visited or grid[y][x] == "#":
            continue

        visited.add((x, y))

        if (x, y) == (width - 1, height - 1):
            return True

        queue.append((x + 1, y, dist + 1))
        queue.append((x - 1, y, dist + 1))
        queue.append((x, y + 1, dist + 1))
        queue.append((x, y - 1, dist + 1))

    return False


for idx, (x, y) in enumerate(bytes):
    grid[y][x] = "#"
    if not has_exit():
        print(f"{x},{y}")
        break
