import sys


class Mapper:
    def __init__(self, mappings):
        self.mappings = mappings

    def __call__(self, num):
        for bounds, offset in self.mappings.items():
            if bounds[0] <= num < bounds[1]:
                return num + offset
        return num


def parse_seeds(lines):
    return [int(s) for s in lines[0].split(" ")[1:]]


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

    converted = []
    for i in range(len(seeds)):
        converted.append([seeds[i]])
        for mapper in mappers:
            converted[i].append(mapper(converted[i][-1]))

    print(min(c[-1] for c in converted))
