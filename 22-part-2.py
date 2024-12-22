from collections import defaultdict, deque

with open("input.txt") as f:
    input = f.read()

out = 0


def gen_secret(secret: int) -> int:
    secret = secret ^ (secret * 64)
    secret %= 16777216
    secret = secret ^ (secret // 32)
    secret %= 16777216
    secret = secret ^ (secret * 2048)
    secret %= 16777216
    return secret


sequences = defaultdict(int)

for idx, num in enumerate(input.splitlines()):
    num = int(num)

    diffs = deque([])
    ones = deque([])

    seen = set()

    for _ in range(5):
        num = gen_secret(num)
        if ones:
            diffs.append((num % 10) - ones[-1])
        ones.append(num % 10)

    for _ in range(5, 2000):
        diffs.popleft()
        ones.popleft()

        num = gen_secret(num)

        diffs.append((num % 10) - ones[-1])
        ones.append(num % 10)

        key = tuple(diffs)
        if key in seen:
            continue
        seen.add(key)

        sequences[key] += ones[-1]

out = max(sequences.values())


print(out)
