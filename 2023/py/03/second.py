import sys


def parse_number(x, y, engine):
    if x < 0 or x >= len(engine[y]) or y < 0 or y >= len(engine):
        return None

    if not engine[y][x].isdigit():
        return None

    start = x
    end = x
    while start > 0 and engine[y][start - 1].isdigit():
        start = start - 1

    while end <= len(engine) and engine[y][end + 1].isdigit():
        end = end + 1

    return int(engine[y][start : end + 1])


with open(sys.argv[1]) as f:
    engine = f.readlines()

sum_ratios = 0
for y in range(len(engine)):
    for x in range(len(engine)):
        if engine[y][x] == "*":
            numbers = []
            if u := parse_number(x, y - 1, engine):
                numbers.append(u)
            else:
                if ul := parse_number(x - 1, y - 1, engine):
                    numbers.append(ul)
                if ur := parse_number(x + 1, y - 1, engine):
                    numbers.append(ur)

            if l := parse_number(x - 1, y, engine):
                numbers.append(l)

            if r := parse_number(x + 1, y, engine):
                numbers.append(r)

            if b := parse_number(x, y + 1, engine):
                numbers.append(b)
            else:
                if bl := parse_number(x - 1, y + 1, engine):
                    numbers.append(bl)
                if br := parse_number(x + 1, y + 1, engine):
                    numbers.append(br)
            if len(numbers) == 2:
                ratio = numbers[0] * numbers[1]
                sum_ratios += ratio

print(sum_ratios)
