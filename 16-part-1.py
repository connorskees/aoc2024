import heapq

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

queue = [(0, *start, RIGHT)]

visited = set()

while queue:
    score, x, y, dir = heapq.heappop(queue)

    if not is_valid(x, y):
        continue

    if (x, y, dir) in visited:
        continue

    visited.add((x, y, dir))

    if grid[y][x] == "E":
        print(score)
        break

    if grid[y][x] == "#":
        continue

    dx, dy = dir

    heapq.heappush(queue, (score + 1, x + dx, y + dy, dir))

    heapq.heappush(queue, (score + 1000, x, y, clockwise[dir]))
    heapq.heappush(queue, (score + 1000, x, y, counter_clockwise[dir]))
