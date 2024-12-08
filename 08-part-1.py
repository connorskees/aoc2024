from collections import defaultdict

with open("input.txt") as f:
    input = f.read()

out = 0

antinodes = set()

grid = input.splitlines()

width = len(grid[0])
height = len(grid)

groups = defaultdict(list)

is_valid = lambda x, y: x >= 0 and y >= 0 and x < width and y < height

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == ".":
            continue

        groups[cell].append((x, y))

for group in groups.values():
    for i in range(len(group)):
        x0, y0 = group[i]
        for j in range(i + 1, len(group)):
            x1, y1 = group[j]

            dx = x1 - x0
            dy = y1 - y0

            possible_coords = [
                coord
                for coord in [
                    (x0 - dx, y0 - dy),
                    (x1 + dx, y1 + dy),
                ]
                if is_valid(*coord) and coord not in [(x0, y0), (x1, y1)]
            ]

            for c in possible_coords:
                antinodes.add(c)

print(len(antinodes))
