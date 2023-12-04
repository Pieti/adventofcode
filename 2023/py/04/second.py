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
        return len(i)


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


cards = []
for line in lines:
    cards.append(parse_line(line))

weights = [1 for _ in cards]
for i, card in enumerate(cards):
    for _ in range(weights[i]):
        value = card.value()
        end = min(i + value, len(weights))
        for j in range(i, end):
            weights[j + 1] += 1

print(sum(weights))
