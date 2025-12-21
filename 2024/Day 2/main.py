from typing import List
import sys


def part1(reports: List[str]) -> int:
    c = 0
    for r in reports:
        report = list(map(int, r.split()))
        is_increasing = 1 if report[0] < report[1] else -1
        for i in range(1, len(report)):
            if is_increasing * (report[i] - report[i - 1]) not in [1, 2, 3]:
                break
            if i == len(report) - 1:
                c += 1
    return c


def is_safe(report: List[int]) -> bool:
    for i in range(len(report) - 1):
        diff = abs(report[i + 1] - report[i])
        if diff not in [1, 2, 3]:
            return False
    is_increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        if (is_increasing and report[i] > report[i + 1]) or (
            not is_increasing and report[i] < report[i + 1]
        ):
            return False
    return True


def part2(reports: List[str]) -> int:
    c = 0
    for r in reports:
        report = list(map(int, r.split()))

        if is_safe(report):
            c += 1
        else:
            found_safe = False
            for i in range(len(report)):
                new_report = report[:i] + report[i + 1 :]
                if is_safe(new_report):
                    found_safe = True
                    break
            if found_safe:
                c += 1

    return c


if __name__ == "__main__":
    file = sys.argv[1]

    lines = open(file, "r").read().split("\n")

    print("Part 1 solution:", part1(lines))
    a = part2(lines)
    print("Part 2 solution:", a)
