from collections import Counter

with open("input.txt") as f:
    input = f.read()

out = 0

stones = [int(n) for n in input.split()]


def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        return [int(stone[: len(stone) // 2]), int(stone[len(stone) // 2 :])]

    return [stone * 2024]


stone_counts = Counter(stones)

for _ in range(75):
    next_stone_counts = Counter()
    for stone, count in stone_counts.items():
        for new_stone in blink(stone):
            next_stone_counts[new_stone] += count

    stone_counts = next_stone_counts

print(sum(stone_counts.values()))
