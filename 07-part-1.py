import functools

with open("input.txt") as f:
    input = f.read()

out = 0


def can_be_true(target: int, nums: list[int]):
    @functools.cache
    def inner(idx, total):
        if idx == len(nums):
            return target == total

        num = nums[idx]

        return inner(idx + 1, total * num) or inner(idx + 1, total + num)

    return inner(0, 0)


for equation in input.splitlines():
    target, rest = equation.split(": ")

    target = int(target)

    nums = [int(n) for n in rest.split()]

    if can_be_true(target, nums):
        out += target

print(out)
