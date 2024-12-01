import heapq

with open("input.txt") as f:
    input = f.read()

left = []
right = []

for line in input.splitlines():
    a, b = line.split()
    left.append(int(a))
    right.append(int(b))

heapq.heapify(left)
heapq.heapify(right)

out = 0

while left and right:
    out += abs(heapq.heappop(left) - heapq.heappop(right))

print(out)
