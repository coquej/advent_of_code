import sys


def is_repeated_twice(x):
    if len(x) % 2 != 0:
        return False
    else:
        return x[: len(x) // 2] == x[len(x) // 2 :]


def is_repeated_n_times(x):
    max_subset = len(x) // 2
    for i in range(1, max_subset + 1):
        if len(set([x[j : j + i] for j in range(0, len(x), i)])) == 1:
            return True
    return False


def solution(ranges, func_used):
    invalids = []
    for r in ranges:
        ini, fin = r.split("-")
        for x in range(int(ini), int(fin) + 1):
            if func_used(str(x)):
                invalids.append(x)
    return sum(invalids)


if __name__ == "__main__":
    file = sys.argv[1]

    ranges = open(file, "r").read().split(",")

    print("Part 1 solution:", solution(ranges, is_repeated_twice))
    print("Part 2 solution:", solution(ranges, is_repeated_n_times))
