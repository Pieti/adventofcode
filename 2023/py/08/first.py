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
    target = "ZZZ"
    current = "AAA"
    for d in cycle(directions):
        steps += 1
        current = nodes[current][d]
        if current == target:
            print(steps)
            break
