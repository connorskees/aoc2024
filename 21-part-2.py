import functools
import re

with open("input.txt") as f:
    input = f.read()

out = 0

numeric_coords = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

valid_numeric_coords = tuple(numeric_coords.values())

arrow_coords = {
    "^": (1, 0),
    "A": (2, 0),
    ">": (2, 1),
    "<": (0, 1),
    "v": (1, 1),
}

valid_arrow_coords = tuple(arrow_coords.values())


@functools.cache
def permute(pos, new_pos, coords):
    x1, y1 = pos
    x2, y2 = new_pos

    if x1 == x2 and y1 == y2:
        return [""]

    if x1 == x2 and y1 > y2:
        return ["^" * (y1 - y2)]

    if x1 == x2 and y1 < y2:
        return ["v" * (y2 - y1)]

    if x1 > x2 and y1 == y2:
        return ["<" * (x1 - x2)]

    if x1 < x2 and y1 == y2:
        return [">" * (x2 - x1)]

    x_first = ""
    y_first = ""

    if x1 > x2:
        x_first += "<" * (x1 - x2)
    else:
        x_first += ">" * (x2 - x1)

    if y1 > y2:
        y_first = "^" * (y1 - y2) + x_first
        x_first += "^" * (y1 - y2)
    else:
        y_first = "v" * (y2 - y1) + x_first
        x_first += "v" * (y2 - y1)

    can_skip_check = (
        coords == valid_arrow_coords
        and (x1, y1) != arrow_coords["<"]
        and (x2, y2) != arrow_coords["<"]
    )

    return [
        p
        for p in (x_first, y_first)
        if can_skip_check or movement_is_valid(pos, p, coords)
    ]


@functools.cache
def movement_is_valid(start, path, coords):
    x, y = start
    for p in path:
        if p == ">":
            x += 1
        elif p == "<":
            x -= 1
        elif p == "v":
            y += 1
        elif p == "^":
            y -= 1
        if (x, y) not in coords:
            return False

    return (x, y) in coords


def permutations(
    code: str,
    start: tuple[int, int],
    coord_idxs: dict[str, list[tuple[int, int]]],
    valid_coords: list[tuple[int, int]],
) -> list[str]:
    pos = start
    out = [""]

    for c in code:
        new_pos = coord_idxs[c]

        next = set()

        for perm in permute(pos, new_pos, valid_coords):
            next |= set([o + perm + "A" for o in out])

        out = next
        pos = new_pos

    return list(out)


def initial_code(code: str) -> list[str]:
    return permutations(code, (2, 3), numeric_coords, valid_numeric_coords)


@functools.cache
def dfs(code: str, depth: int, pos: tuple[int, int]) -> int:
    if depth == 0:
        return len(code)

    out = 0
    for c in code:
        new_pos = arrow_coords[c]
        perms = permute(pos, new_pos, valid_arrow_coords)
        out += min(dfs(perm + "A", depth - 1, (2, 0)) for perm in perms)
        pos = new_pos

    return out


for code in input.splitlines():
    numeric = int(next(re.finditer(r"\d+", code)).group(0))

    init = initial_code(code)
    length = min(dfs(v, 25, (2, 0)) for v in init)

    out += numeric * length

print(out)
