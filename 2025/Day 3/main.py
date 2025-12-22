import sys


def get_max_pair(line, num_batteries=2):
    bank = list(line)
    power = ""

    while len(bank) > 0 and len(power) < num_batteries:
        max_pwr = (
            str(max(bank[: 1 - (num_batteries - len(power))]))
            if num_batteries - len(power) != 1
            else str(max(bank))
        )

        bank = bank[bank.index(max_pwr) + 1 :]
        power += max_pwr

    return int(power)


def solution(lines, num_batteries=2):
    return sum([get_max_pair(line, num_batteries) for line in lines])


if __name__ == "__main__":
    file = sys.argv[1]

    lines = open(file, "r").read().split("\n")

    print("Part 1 solution:", solution(lines, num_batteries=2))
    print("Part 2 solution:", solution(lines, num_batteries=12))
