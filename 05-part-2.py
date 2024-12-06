from collections import defaultdict

with open("input.txt") as f:
    input = f.read()

out = 0

graph = defaultdict(set)

graph_input, pages = input.split("\n\n")

for line in graph_input.splitlines():
    a, b = line.split("|")
    graph[a].add(b)

for line in pages.splitlines():
    nums = line.split(",")

    broke = False
    changed = True

    while changed:
        changed = False

        prev = {}

        for idx, num in enumerate(nums):
            for child in graph[num]:
                if child in prev:
                    nums[idx], nums[prev[child]] = nums[prev[child]], nums[idx]
                    changed = True
                    broke = True
                    break

                prev[num] = idx

    if not broke:
        continue

    out += int(nums[len(nums) // 2])

print(out)
