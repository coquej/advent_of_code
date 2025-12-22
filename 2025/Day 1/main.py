import sys


def part1(lines):
    pointer = 50
    res = 0

    for line in lines:
        direction = (-1 if line[0]=='L' else 1)
        for _ in range(int(line[1:])):
            pointer = pointer + (direction)
            pointer = pointer%100
        if pointer==0:
            res+=1

    return res

def part2(lines):
    pointer = 50
    res = 0

    for line in lines:
        direction = (-1 if line[:1]=='L' else 1)
        for _ in range(int(line[1:])):
            pointer = pointer + (direction)
            pointer = pointer%100
            if pointer==0:
                res+=1

    return res


if __name__ == "__main__":
    file = sys.argv[1]

    lines = open(file, "r").read().split("\n")

    print("Part 1 solution:", part1(lines))
    print("Part 2 solution:", part2(lines))