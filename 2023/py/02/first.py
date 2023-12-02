import sys
from typing import NamedTuple

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


class RGB(NamedTuple):
    red: int = 0
    green: int = 0
    blue: int = 0

    def is_valid(self):
        return self.red <= MAX_RED and self.green <= MAX_GREEN and self.blue <= MAX_BLUE


class Game(NamedTuple):
    id: int
    samples: list[RGB]

    def is_valid(self):
        return all(s.is_valid() for s in self.samples)


def parse_sample(sample):
    rgb = {"red": 0, "green": 0, "blue": 0}
    for color_tuple in sample.split(","):
        num, color = color_tuple.strip().split(" ")
        rgb[color] = int(num)
    return RGB(**rgb)


def parse_line(line):
    game, line = line.split(":")
    game_id = int(game[5:])

    samples = []
    for sample in line.split(";"):
        samples.append(parse_sample(sample))

    return Game(id=game_id, samples=samples)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.readlines()

    sum_ids = 0
    for line in data:
        game = parse_line(line)
        if game.is_valid():
            sum_ids += game.id

    print(sum_ids)
