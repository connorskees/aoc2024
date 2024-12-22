with open("input.txt") as f:
    input = f.read()

out = 0


def gen_secret(secret: int) -> int:
    def mix(a, b):
        return a ^ b

    def prune(n):
        return n % 16777216

    secret = mix(secret, secret * 64)
    secret = prune(secret)
    secret = mix(secret, secret // 32)
    secret = prune(secret)
    secret = mix(secret, secret * 2048)
    secret = prune(secret)
    return secret


for num in input.splitlines():
    num = int(num)
    for _ in range(2000):
        num = gen_secret(num)

    out += num

print(out)
