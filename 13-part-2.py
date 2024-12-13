import math
import re

with open("input.txt") as f:
    input = f.read()

out = 0

games = input.split("\n\n")

for game in games:
    a, b, prize = game.splitlines()

    button_regex = re.compile(r".*?X\+(\d+), Y\+(\d+)")
    prize_regex = re.compile(r".*?X=(\d+), Y=(\d+)")

    a = re.match(button_regex, a)
    b = re.match(button_regex, b)

    a_x = int(a.group(1))
    a_y = int(a.group(2))

    b_x = int(b.group(1))
    b_y = int(b.group(2))

    prize = re.match(prize_regex, prize)

    prize_x = int(prize.group(1)) + 10000000000000
    prize_y = int(prize.group(2)) + 10000000000000

    b = (prize_y * a_x - a_y * prize_x) / (b_y * a_x - b_x * a_y)
    a = (prize_y - b * b_y) / a_y

    if math.floor(b) != b or math.floor(a) != a:
        continue

    out += 3 * a + b

print(out)
