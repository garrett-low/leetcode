from collections import defaultdict
from functools import cmp_to_key

HAND_TYPE = {
    "five_kind" : 1,
    "four_kind" : 2,
    "full_house" : 3,
    "three_kind" : 4,
    "two_pair" : 5,
    "one_pair" : 6,
    "high_card" : 7 }

FACE_VAL = {
    "A" : 1,
    "K" : 13,
    "Q" : 12,
    "J" : 11
}

def cards(filename):
    hands = []
    bids = []
    with open(filename, 'rt') as file:
        for line in file:
            splits = line.strip().split()
            hands.append(splits[0])
            bids.append(int(splits[1]))
    
    print(hands)
    print(bids)
    
    hands_card_counts = [] # list of hands, each item is dict of card -> count
    hands_card_counts_reverse = [] # list of hands, count -> list of cards
    idx = 0
    for hand in hands:
        card_counts = defaultdict(int)
        hands_card_counts.append(card_counts)
        for card in hand:
            card_counts[card] += 1
        
        card_counts_reverse = {}
        hands_card_counts_reverse.append(card_counts_reverse)
        for card in card_counts:
            count = card_counts[card]
            if count in card_counts_reverse:
                card_counts_reverse[count].append(card)
            else:
                card_counts_reverse[count] = [card]
        # print(card_counts)
        # print(card_counts_reverse)
        idx += 1
    
    # print(hands_card_counts)
    # print(hands_card_counts_reverse)
    
    # scoring
    hands_hand_type = []
    hand_type_hands_lookup = {}
    for card_count_reverse in hands_card_counts_reverse:
        if 5 in card_count_reverse:
            hands_hand_type.append("five_kind")
            continue
        elif 4 in card_count_reverse:
            hands_hand_type.append("four_kind")
            continue
        elif 3 in card_count_reverse:
            if 2 in card_count_reverse:
                hands_hand_type.append("full_house")
            else:
                hands_hand_type.append("three_kind")
            continue
        elif 2 in card_count_reverse:
            count_pairs = len(card_count_reverse[2])
            if count_pairs == 1:
                hands_hand_type.append("one_pair")
            elif count_pairs == 2:
                hands_hand_type.append("two_pair")
            continue
        else:
            hands_hand_type.append("high_card")
    
    print(hands_hand_type)
    
    print(sorted(hands_hand_type, key=cmp_to_key(compare_hand_types)))
    
    print(hands_hand_type)


def compare_hand_types(type1, type2):
    rank1 = HAND_TYPE[type1]
    rank2 = HAND_TYPE[type2]
    
    if rank1 < rank2:
        return 1
    elif rank1 > rank2:
        return -1
    else:
        return 0
        
def compare_hand_ordering(hand1, hand2):
    for i in range(len(hand)):
        card1 = hand1[i]
        card2 = hand2[i]
        
        if card1.isalpha():
            card1 = FACE_VAL[card1.upper()]
        if card2.isalpha():
            card2 = FACE_VAL[card2.upper()]
        
        if card1 > card2:
            return -1
        elif card2 < card1:
            return 1
        else:
            continue # just making it obvious
    
    return 0

cards('sample.txt')