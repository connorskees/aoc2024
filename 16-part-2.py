import heapq
import math
from collections import defaultdict

with open("input.txt") as f:
    input = f.read()

out = 0

is_valid = lambda x, y: x >= 0 and y >= 0 and x < width and y < height

RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
UP = (0, -1)

clockwise = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}
counter_clockwise = {UP: LEFT, LEFT: DOWN, DOWN: RIGHT, RIGHT: UP}


start_idx = input.replace("\n", "").index("S")

grid = [list(row) for row in input.splitlines()]

width = len(grid[0])
height = len(grid)

start = (start_idx % width, start_idx // width)

queue = [(0, *start, RIGHT, set())]

visited = set()

tiles = set()

best = math.inf

best_for_tile = [
    [defaultdict(lambda: [math.inf, set()]) for _ in range(width)]
    for _ in range(height)
]

while queue:
    score, x, y, dir, path = heapq.heappop(queue)

    if not is_valid(x, y):
        continue

    if grid[y][x] == "#":
        continue

    if score > best_for_tile[y][x][dir][0]:
        continue

    if score == best_for_tile[y][x][dir][0]:
        best_for_tile[y][x][dir][1] |= path
    else:
        best_for_tile[y][x][dir] = [score, set(path)]

    if score > best:
        break

    path = set(path)
    path.add((x, y))

    if grid[y][x] == "E":
        tiles.add((x, y))
        best = score
        tiles |= best_for_tile[y][x][dir][1]
        continue

    dx, dy = dir

    heapq.heappush(queue, (score + 1, x + dx, y + dy, dir, path))

    heapq.heappush(queue, (score + 1000, x, y, clockwise[dir], path))
    heapq.heappush(queue, (score + 1000, x, y, counter_clockwise[dir], path))


for x, y in tiles:
    grid[y][x] = "O"

print("\n".join("".join(row) for row in grid) + "\n\n")

print(len(tiles))
