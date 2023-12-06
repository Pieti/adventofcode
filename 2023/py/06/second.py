import sys
from typing import NamedTuple


class Race(NamedTuple):
    time: int
    record: int


def parse_lines(lines):
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]
    time = int("".join(times))
    record = int("".join(distances))
    return Race(time=time, record=record)


def calc_distance(hold_time, race_time):
    travel_time = race_time - hold_time
    return hold_time * travel_time


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    race = parse_lines(lines)
    num_wins = 0
    for hold_time in range(race.time):
        distance = calc_distance(hold_time, race.time)
        if distance > race.record:
            num_wins += 1
    print(num_wins)
