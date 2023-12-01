import sys

WORDS = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


def forward(line):
    for i, c in enumerate(line):
        yield i, c


def backward(line):
    for i, c in reversed(list(enumerate(line))):
        yield i, c


def find_digit(line, iterator):
    for i, c in iterator(line):
        if c.isdigit():
            return c
        for value, word in enumerate(WORDS):
            if line[i:].startswith(word):
                return str(value + 1)
    raise ValueError(f"Found no digits on line: {line}")


with open(sys.argv[1]) as f:
    data = f.readlines()

total = 0
for line in data:
    first = find_digit(line, forward)
    last = find_digit(line, backward)
    total += int(first + last)

print(total)
