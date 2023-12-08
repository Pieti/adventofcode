import math
import sys
from itertools import cycle


def parse_lines(lines):
    lr = lines[0].replace("L", "0").replace("R", "1").strip()
    directions = [int(d) for d in lr]
    nodes = {}

    for line in lines[2:]:
        value = line[:3]
        left = line[7:10]
        right = line[12:15]

        nodes[value] = [left, right]

    return directions, nodes


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    directions, nodes = parse_lines(lines)

    steps = 0
    currents = [n for n in nodes if n[2] == "A"]
    solutions = []
    for current in currents:
        steps = 0
        for d in cycle(directions):
            steps += 1
            current = nodes[current][d]
            if current[2] == "Z":
                solutions.append(steps)
                break
    print(math.lcm(*solutions))
