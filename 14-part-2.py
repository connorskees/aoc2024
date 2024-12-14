import re

with open("input.txt") as f:
    input = f.read()

out = 0

width = 101
height = 103

robots = []

for robot in input.splitlines():
    matches = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", robot)

    p_x = int(matches.group(1))
    p_y = int(matches.group(2))
    v_x = int(matches.group(3))
    v_y = int(matches.group(4))

    robots.append(((p_x, p_y), (v_x, v_y)))


def visualize(i):
    output = [["."] * width for _ in range(height)]

    for (p_x, p_y), _ in robots:
        output[p_y][p_x] = "A"

    combined = "\n".join("".join(row) for row in output)

    if "A" * 10 in combined:
        print(f"{i}\n" + "\n".join("".join(row) for row in output) + "\n\n")


for i in range(15_000):
    for idx, ((p_x, p_y), (v_x, v_y)) in enumerate(robots):
        p_x += v_x
        p_y += v_y

        p_x %= width
        p_y %= height

        robots[idx] = ((p_x, p_y), (v_x, v_y))

    visualize(i + 1)
