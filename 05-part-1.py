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

    prev = set()

    for num in nums:
        if prev & graph[num]:
            break
        prev.add(num)
    else:
        out += int(nums[len(nums) // 2])

print(out)
