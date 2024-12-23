from collections import defaultdict

with open("input.txt") as f:
    input = f.read()

out = 0

graph = defaultdict(list)

for line in input.splitlines():
    a, b = line.split("-")
    graph[a].append(b)
    graph[b].append(a)

to_visit = [(s, []) for s in graph.keys()]

groups = set()

while to_visit:
    node, trail = to_visit.pop()

    if len(trail) > 3:
        continue

    if len(trail) == 3:
        if trail[0] == node:
            groups.add(tuple(sorted(trail)))

        continue

    for child in graph[node]:
        to_visit.append((child, [*trail, node]))

print(len([g for g in groups if any("t" == c[0] for c in g)]), len(groups))
