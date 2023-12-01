import sys

with open(sys.argv[1]) as f:
    data = f.readlines()

total = 0
for line in data:
    first = last = ""
    for c in line:
        if c.isdigit():
            first = c
            break

    for c in line[::-1]:
        if c.isdigit():
            last = c
            break

    val = first + last
    s = int(val)
    total += s


print(total)
