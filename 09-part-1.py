with open("input.txt") as f:
    input = f.read()

disk = []
free = False
id = 0

for num in input:
    num = int(num)
    if not free:
        disk += [id] * num
        id += 1
    else:
        disk += list("." * num)
    free = not free

idx = 0
end_idx = len(disk) - 1

while idx < end_idx:
    if disk[idx] != ".":
        idx += 1
        continue

    while disk[end_idx] == ".":
        end_idx -= 1

    disk[idx], disk[end_idx] = disk[end_idx], disk[idx]

    idx += 1
    end_idx -= 1

out = sum(n * idx for idx, n in enumerate(disk) if n != ".")

print(out)
