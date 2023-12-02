import sys
import numpy as np


def read_n_clean_file(file):

    games = open(file, "r").read().split("\n")

    res = [
        [
            dict([
                    ( subset[1:].split(" ")[1], int(subset[1:].split(" ")[0]) )
                            for subset in set.split(",")
                ]) for set in game.split(":")[1].split(";")
        ] for game in games
    ]

    return res

def clean_bag(bag):
    colours = bag.replace(' and', '').replace(' cubes', '').split(', ')
    colours_in_tuples = [(col.split(' ')[1], int(col.split(' ')[0])) for col in colours ]

    return dict(colours_in_tuples)

def part1(games, bag):
    game_id = 1
    res = 0

    for sets in games:
        ok = True
        for set in sets:
            for colour, qty in set.items():
                if qty>bag[colour]:
                    ok = False
                    break
            if not ok:
                break

        res += game_id if ok else 0
        game_id += 1
    
    return res

def part2(games):
    res = 0

    for sets in games:
        bag = { 'green': 0, 'blue': 0, 'red': 0}
        for set in sets:
            for colour, qty in set.items():
                if qty>bag[colour]:
                    bag[colour] = qty
        res += np.prod(list(bag.values()))
    
    return res


if __name__ == "__main__":
    file1 = sys.argv[1]
    bag = sys.argv[2] if len(sys.argv) > 2 else '12 red cubes, 13 green cubes, and 14 blue cubes'
    
    games = read_n_clean_file(file1) 
    bag = clean_bag(bag)

    print('Part 1:', part1(games, bag))
    print('Part 2:', part2(games))
