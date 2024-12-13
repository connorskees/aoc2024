import functools
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

    prize_x = int(prize.group(1))
    prize_y = int(prize.group(2))

    @functools.cache
    def simulate(x, y):
        if x < 0 or y < 0:
            return math.inf

        if x == 0 and y == 0:
            return 0

        return min(3 + simulate(x - a_x, y - a_y), 1 + simulate(x - b_x, y - b_y))

    min_coins = simulate(prize_x, prize_y)

    if min_coins != math.inf:
        out += min_coins

print(out)
