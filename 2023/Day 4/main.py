import sys

def clean_input(file):
    lines = open(file, "r").read().split("\n")
    cards = [
        [
            [int(x) for x in card.split(" ") if x != ""]
            for card in line.split(":")[1].split("|")
        ]
        for line in lines
    ]     
    return cards

def part1(cards):
    card_points = []
    for card in cards:
        coincidences = len(list(set(card[0]) & set(card[1])))
        points = 0 if coincidences==0 else 2**(coincidences-1)
        card_points.append(points)

    return sum(card_points)


def part2(cards):
    card_instances = [1]*len(cards)
    i_card = 0

    for card in cards:
        coincidences = len(list(set(card[0]) & set(card[1])))
        for i in range(i_card, i_card+coincidences) :
            card_instances[i+1] += card_instances[i_card]
        i_card += 1

    return sum(card_instances)

if __name__ == "__main__":
    cards = clean_input(sys.argv[1])
    print(part1(cards))
    print(part2(cards))