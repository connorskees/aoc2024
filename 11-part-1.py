from collections import defaultdict

with open("input.txt") as f:
    input = f.read()

out = 0

stones = [int(n) for n in input.split()]

counts = defaultdict(int)


def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        return [int(stone[: len(stone) // 2]), int(stone[len(stone) // 2 :])]

    return [stone * 2024]


for _ in range(25):
    stones = [changed for stone in stones for changed in blink(stone)]

print(len(stones))
