import sys

DIRECTIONS = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]


def adjacents(x, y, engine):
    for dx, dy in DIRECTIONS:
        if 0 <= x + dx < len(engine[y]) and 0 <= y + dy < len(engine):
            yield x + dx, y + dy


def is_symbol(x, y, engine):
    return not engine[y][x].isdigit() and engine[y][x] != "."


with open(sys.argv[1]) as f:
    engine = f.readlines()

sum_parts = 0

current = ""
is_part = False
for y in range(len(engine)):
    for x in range(len(engine)):
        if engine[y][x].isdigit():
            current = current + engine[y][x]
            if not is_part:
                for dx, dy in adjacents(x, y, engine):
                    if is_symbol(dx, dy, engine):
                        is_part = True
        else:
            if current and is_part:
                sum_parts += int(current)
                is_part = False
            current = ""

print(sum_parts)
