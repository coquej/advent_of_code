import sys


def part1(lines):
    res = [[] for _ in range(2)]
    for line in lines:
        numbers = line.split()
        for i in range(2):
            res[i].append(int(numbers[i]))

    res[0].sort()
    res[1].sort()

    return sum([abs(res[0][i] - res[1][i]) for i in range(len(res[0]))])


def part2(lines):
    res = [[] for _ in range(2)]

    for line in lines:
        numbers = line.split()
        for i in range(2):
            res[i].append(int(numbers[i]))

    a = [res[0][i] * res[1].count(res[0][i]) for i in range(len(res[0]))]

    return sum(a)


if __name__ == "__main__":
    file = sys.argv[1]

    lines = open(file, "r").read().split("\n")

    print("Part 1 solution:", part1(lines))
    print("Part 2 solution:", part2(lines))
