import sys


class Mapper:
    def __init__(self, mappings):
        self.mappings = mappings

    def __call__(self, num, reversed=False):
        if not reversed:
            return self.map(num)
        return self.reverse_map(num)

    def map(self, num):
        for bounds, offset in self.mappings.items():
            if bounds[0] <= num < bounds[1]:
                return num + offset
        return num

    def reverse_map(self, num):
        for bounds, offset in self.mappings.items():
            if bounds[0] <= num - offset < bounds[1]:
                return num - offset
        return num


def parse_seeds(lines):
    intervals = []
    numbers = [int(s) for s in lines[0].split(" ")[1:]]
    for i in range(0, len(numbers), 2):
        intervals.append([numbers[i], numbers[i] + numbers[i + 1]])
    return intervals


def parse_maps(lines):
    mappers = []
    mappings = {}
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue

        if line.endswith("map:"):
            if mappings:
                mappers.append(Mapper(mappings))
                mappings = {}
            continue

        dst, src, rng = line.split()
        src = int(src)
        dst = int(dst)
        rng = int(rng)

        lower = src
        upper = src + rng
        offset = dst - src
        mappings[lower, upper] = offset

    mappers.append(Mapper(mappings))
    return mappers


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    seeds = parse_seeds(lines)
    mappers = parse_maps(lines)

    found = False
    i = 10000000
    while not found:
        if i % 10000000 == 0:
            print(i)
        value = i
        for mapper in mappers[::-1]:
            value = mapper(value, reversed=True)
        for seed_range in seeds:
            if seed_range[0] <= value <= seed_range[1]:
                print(i)
                found = True
                break
        i += 1
