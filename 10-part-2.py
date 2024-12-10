with open("input.txt") as f:
    input = f.read()

out = 0

grid = input.splitlines()

starts = []

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != "0":
            continue

        starts.append((x, y))

is_valid = lambda x, y: x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)


def compute_score(start):
    queue = [(*start, 0, [])]

    score = set()

    while queue:
        x, y, target, visited = queue.pop()

        if not is_valid(x, y):
            continue

        if int(grid[y][x]) != target:
            continue

        if target == 9:
            score.add((x, y, tuple(visited)))

        visited = visited[:]
        visited.append((x, y))

        queue.append((x + 1, y, target + 1, visited))
        queue.append((x - 1, y, target + 1, visited))
        queue.append((x, y + 1, target + 1, visited))
        queue.append((x, y - 1, target + 1, visited))

    return len(score)


for start in starts:
    out += compute_score(start)

print(out)
