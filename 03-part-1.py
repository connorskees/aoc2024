import re

with open("input.txt") as f:
    input = f.read()


out = 0

for result in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", input):
    lhs = result.group(1)
    rhs = result.group(2)

    out += int(lhs) * int(rhs)

print(out)

## and a handwritten parser for fun
out = 0


class Parser:
    def __init__(self):
        self.cursor: int = 0
        self.buffer = input

    def peek_char(self):
        c = self.read_char()
        self.cursor -= 1
        return c

    def read_char(self):
        if self.cursor >= len(self.buffer):
            return None
        c = self.buffer[self.cursor]
        self.cursor += 1
        return c

    def expect_char(self, c):
        return self.read_char() == c

    def parse_mul(self):
        if not self.expect_char("m"):
            return False
        if not self.expect_char("u"):
            return False
        if not self.expect_char("l"):
            return False
        if not self.expect_char("("):
            return False

        lhs = self.parse_integer()
        if lhs is None:
            return False
        if not self.expect_char(","):
            return False
        rhs = self.parse_integer()
        if rhs is None:
            return False
        if not self.expect_char(")"):
            return False
        global out
        out += int(lhs) * int(rhs)

    def parse_integer(self):
        val = 0
        digits = 0
        while c := self.peek_char():
            if c is not None and c.isnumeric():
                val *= 10
                val += int(c)
                digits += 1
                self.read_char()
            else:
                break
            if digits == 3:
                break
        if digits == 0:
            return None
        return val

    def parse(self):
        while self.cursor < len(self.buffer):
            self.parse_mul()


Parser().parse()

print(out)
