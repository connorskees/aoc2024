from collections import Counter

with open("input.txt") as f:
    input = f.read()

left = []
right = []

for line in input.splitlines():
    a, b = line.split()
    left.append(int(a))
    right.append(int(b))

counts = Counter(right)

out = 0

for num in left:
    out += num * (counts[num] if num in counts else 0)

print(out)
