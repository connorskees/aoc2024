from collections import deque

with open("input.txt") as f:
    input = f.read()

out = 0

grid = input.splitlines()

width = len(grid[0])
height = len(grid)

start_idx = input.replace("\n", "").index("S")
end_idx = input.replace("\n", "").index("E")

start = (start_idx % width, start_idx // width)
end = (end_idx % width, end_idx // width)

is_valid = lambda x, y: x >= 0 and y >= 0 and x < width and y < height


def compute_min_dists(start):
    dists = {}

    queue = deque([(*start, 0)])

    visited = set()

    while queue:
        x, y, cost = queue.popleft()

        if (x, y) in visited or not is_valid(x, y):
            continue

        if grid[y][x] == "#":
            continue

        dists[(x, y)] = cost

        visited.add((x, y))

        queue.append((x + 1, y, cost + 1))
        queue.append((x - 1, y, cost + 1))
        queue.append((x, y + 1, cost + 1))
        queue.append((x, y - 1, cost + 1))

    return dists


dists_from_start = compute_min_dists(start)
dists_from_end = compute_min_dists(end)

initial = dists_from_start[end]


def adjacent(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


for y1 in range(height):
    for x1 in range(width):
        if grid[y1][x1] == "#":
            continue

        for x2, y2 in adjacent(x1, y1):
            if not is_valid(x2, y2) or grid[y2][x2] != "#":
                continue

            for x3, y3 in adjacent(x2, y2):
                if not is_valid(x3, y3) or grid[y3][x3] == "#":
                    continue

                val = dists_from_start[(x1, y1)] + 2 + dists_from_end[(x3, y3)]

                if val < initial and initial - val >= 100:
                    out += 1

print(out)
