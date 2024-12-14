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

for _ in range(100):
    for idx, ((p_x, p_y), (v_x, v_y)) in enumerate(robots):
        p_x += v_x
        p_y += v_y

        p_x %= width
        p_y %= height

        robots[idx] = ((p_x, p_y), (v_x, v_y))


up_left = 0
up_right = 0
bottom_left = 0
bottom_right = 0

for (p_x, p_y), _ in robots:
    if p_x < width // 2:
        if p_y < height // 2:
            up_left += 1
        elif p_y > height // 2:
            bottom_left += 1
    elif p_x > width // 2:
        if p_y < height // 2:
            up_right += 1
        elif p_y > height // 2:
            bottom_right += 1

print(up_left * up_right * bottom_left * bottom_right)
