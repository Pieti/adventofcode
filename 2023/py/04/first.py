import sys
from typing import NamedTuple

with open(sys.argv[1]) as f:
    lines = f.readlines()


class Card(NamedTuple):
    id: int
    winning: list[int]
    numbers: list[int]

    def value(self):
        i = set(self.winning).intersection(self.numbers)
        if not i:
            return 0
        return 2 ** (len(i) - 1)


def parse_line(line):
    numbers = []
    game = 0
    winning = []
    i = 5
    while i < len(line):
        if line[i] == "|":
            winning = numbers
            numbers = []
        start = i
        while line[i].isdigit():
            i += 1
        if i > start:
            numbers.append(int(line[start:i]))
            if line[i] == ":":
                game = numbers[0]
                numbers = []
        i += 1
    return Card(id=game, winning=winning, numbers=numbers)


total = 0
for line in lines:
    card = parse_line(line)
    total += card.value()

print(total)
