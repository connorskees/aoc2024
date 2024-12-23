from collections import defaultdict

with open("input.txt") as f:
    input = f.read()

out = 0

graph = defaultdict(set)

for line in input.splitlines():
    a, b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)

max_len = ""

visited = set()

for start in graph.keys():
    nodes = set([start])
    for start2 in graph.keys():
        if graph[start2] & nodes == nodes:
            nodes.add(start2)

    max_len = max(max_len, ",".join(sorted(nodes)), key=len)

print(max_len)
