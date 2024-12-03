import re

with open("input.txt") as f:
    input = f.read()


out = 0

do = True

for result in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", input):
    if result.group(0) == "do()":
        do = True
    elif result.group(0) == "don't()":
        do = False
    elif do:
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
        self.can_parse_mul = True

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

    def parse_string(self, s: str):
        for c in s:
            if not self.expect_char(c):
                return False
        return True

    def parse_do_or_dont(self):
        if not self.parse_string("do"):
            return False

        if self.peek_char() == "n":
            if self.parse_string("n't()"):
                self.can_parse_mul = False
        elif self.parse_string("()"):
            self.can_parse_mul = True

    def parse_mul(self):
        if not self.parse_string("mul("):
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
            c = self.peek_char()
            cursor = self.cursor

            if c == "m" and self.can_parse_mul:
                if not self.parse_mul():
                    self.cursor = cursor + 1
            elif c == "d":
                self.parse_do_or_dont()
            else:
                self.cursor += 1


Parser().parse()

print(out)
