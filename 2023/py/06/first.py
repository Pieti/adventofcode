import sys
from functools import reduce
from typing import NamedTuple


class Race(NamedTuple):
    time: int
    record: int


def parse_lines(lines):
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]
    races = [Race(time=int(t), record=int(d)) for t, d in list(zip(times, distances))]
    return races


def calc_distance(hold_time, race_time):
    travel_time = race_time - hold_time
    return hold_time * travel_time


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    wins_by_race = []
    races = parse_lines(lines)
    for race in races:
        num_wins = 0
        for hold_time in range(race.time):
            distance = calc_distance(hold_time, race.time)
            if distance > race.record:
                num_wins += 1
        wins_by_race.append(num_wins)

    score = reduce(lambda x, y: x * y, wins_by_race)
    print(score)
