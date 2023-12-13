import sys
from collections import Counter
from operator import itemgetter

cards_order_p1 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cards_order_p2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def clean_input(file):
    return [[line.split()[0], int(line.split()[1])] for line in open(file, "r").read().split("\n")]

def hand_strength(card, part):
    dict_cards = Counter(card)

    wildcards = 0 if 'J' not in dict_cards.keys() or part==1 else dict_cards.pop('J')

    repeated_cards = list(dict_cards.values())
    repeated_cards.sort(reverse=True)

    if wildcards!=5:
        repeated_cards[0]+=wildcards
    else:
        repeated_cards.append(wildcards)

    if repeated_cards[0]>=5: # Five of a kind
        return 6
    elif repeated_cards[0]==4: # Four of a kind
        return 5
    elif repeated_cards[0]==3 and repeated_cards[1]==2: # Full house
        return 4
    elif repeated_cards[0]==3: # Three of a kind
        return 3
    elif repeated_cards[0]==2 and repeated_cards[1]==2: # Two pair
        return 2
    elif repeated_cards[0]==2: # One pair
        return 1
    else: # High card 
        return 0

def calculate_winnings(hands, part):
    points, i = [], 0
    cards_order = cards_order_p1 if part==1 else cards_order_p2

    # calculate score per hand
    for hand in hands:
        points.append([i] + [hand_strength(hand[0], part)] + [cards_order.index(x) for x in hand[0]])
        i += 1

    # calculate rank
    points.sort(key=itemgetter(1,2,3,4,5,6))
    
    # calculate winnings
    winnings = 0
    for i in range(0,len(points)):
        original_i = points[i][0]
        winnings += hands[original_i][1] * (i+1)

    return winnings

if __name__ == "__main__":
    hands = clean_input(sys.argv[1])

    print(calculate_winnings(hands, part=1))
    print(calculate_winnings(hands, part=2))