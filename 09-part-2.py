with open("input.txt") as f:
    input = f.read()

disk = []
free = False
id = 0


class FreeSpace:
    def __init__(self, len: int):
        self.len = len
        self.nums = []

    def __repr__(self):
        return repr(self.nums)


for num in input:
    num = int(num)
    if free:
        disk.append(FreeSpace(num))
    else:
        disk.append([id] * num)
        id += 1
    free = not free

free_spots = [
    (idx, chunk)
    for idx, chunk in enumerate(disk)
    if isinstance(chunk, FreeSpace) and chunk.len > 0
]

for idx, chunk in reversed(list(enumerate(disk))):
    if not chunk or isinstance(chunk, FreeSpace):
        continue

    for idx2, (free_idx, free_chunk) in enumerate(free_spots):
        if free_idx >= idx:
            break

        if free_chunk.len < len(chunk):
            continue

        free_chunk.len -= len(chunk)
        free_chunk.nums.append(chunk)

        if free_chunk.len == 0:
            del free_spots[idx2]

        disk[idx] = FreeSpace(len(chunk))
        break

out = []

for group in disk:
    if isinstance(group, FreeSpace):
        out += [num for group in group.nums for num in group]
        out += ["."] * group.len
    else:
        out += group

out = sum((n) * idx for idx, n in enumerate(out) if n != ".")

print(out)
