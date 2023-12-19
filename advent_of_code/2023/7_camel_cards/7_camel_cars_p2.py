from collections import defaultdict
from functools import cmp_to_key
from collections import namedtuple

HAND_TYPE = {
    "five_kind" : 7,
    "four_kind" : 6,
    "full_house" : 5,
    "three_kind" : 4,
    "two_pair" : 3,
    "one_pair" : 2,
    "high_card" : 1 }

FACE_VAL = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 1,
    "T" : 10
}

def cards(filename):
    hands = []
    bids = []
    with open(filename, 'rt') as file:
        for line in file:
            splits = line.strip().split()
            hands.append(splits[0])
            bids.append(int(splits[1]))
    
    # print(hands)
    # print(bids)
    
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
            if card == 'J':
                continue # don't include wildcard in card counts
            
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
    for i in range(len(hands_card_counts_reverse)):
        card_count_reverse = hands_card_counts_reverse[i]
        card_counts = hands_card_counts[i]
        count_wildcard = card_counts['J']
        if 5 in card_count_reverse:
            hands_hand_type.append("five_kind")
            continue
        elif 4 in card_count_reverse:
            if count_wildcard == 1: # AAAAJ
                hands_hand_type.append("five_kind")
                continue
            else:
                hands_hand_type.append("four_kind")
                continue
        elif 3 in card_count_reverse:
            if count_wildcard == 2: # AAAJJ
                hands_hand_type.append("five_kind")
                continue
            elif count_wildcard == 1: # AAAJ2
                hands_hand_type.append("four_kind")
                continue
            elif 2 in card_count_reverse: # AAA22
                hands_hand_type.append("full_house")
                continue
            else: # AAA23
                hands_hand_type.append("three_kind")
                continue
        elif 2 in card_count_reverse:
            count_pairs = len(card_count_reverse[2])
            if count_wildcard == 2: # AAJJ2
                hands_hand_type.append("four_kind")
                continue
            elif count_wildcard == 1:
                if count_pairs == 2: # AAJ22
                    hands_hand_type.append("full_house")
                    continue
                else: # AAJ23
                    hands_hand_type.append("three_kind")
                    continue
            elif count_pairs == 1: # AA234
                hands_hand_type.append("one_pair")
                continue
            elif count_pairs == 2: # AA223
                hands_hand_type.append("two_pair")
                continue
        else:
            hands_hand_type.append("high_card")
    
    # I just learned about named tuples
    hand_tuples = []
    Hand = namedtuple('Hand', ['hand_string', 'hand_type', 'hand_bid'])
    for i in range(len(hands)):
        this_hand_string = hands[i]
        this_hand_type = hands_hand_type[i]
        this_hand_bid = bids[i]
        this_hand_tuple = Hand(this_hand_string, this_hand_type, this_hand_bid)
        hand_tuples.append(this_hand_tuple)
    
    hand_tuples_sorted = sorted(hand_tuples, key=cmp_to_key(compare_hand_types))
    score = 0
    for i, hand_tuple in enumerate(hand_tuples_sorted):
        # print(hand_tuple)
        rank = i + 1
        bid = hand_tuple.hand_bid
        score += rank * bid
        # print(f"{score} += {rank} * {bid}")
    
    print(score)

def compare_hand_types(hand_tuple1, hand_tuple2):
    type1 = hand_tuple1.hand_type
    type2 = hand_tuple2.hand_type
    rank1 = HAND_TYPE[type1]
    rank2 = HAND_TYPE[type2]
    
    if rank1 < rank2:
        return -1
    elif rank1 > rank2:
        return 1
    else:
        # secondary sort
        return compare_hand_ordering(hand_tuple1, hand_tuple2)
        
def compare_hand_ordering(hand_tuple1, hand_tuple2):
    hand1 = hand_tuple1.hand_string
    hand2 = hand_tuple2.hand_string
    # print(f"  {hand1} vs. {hand2}")
    for i in range(len(hand1)):
        card1 = hand1[i]
        card2 = hand2[i]
        
        if card1.isalpha():
            card1 = FACE_VAL[card1.upper()]
        if card2.isalpha():
            card2 = FACE_VAL[card2.upper()]
        
        card1_int = int(card1)
        card2_int = int(card2)
        
        # print(f"  {hand1[i]}: {card1}: {card1_int}")
        # print(f"  {hand2[i]}: {card2}: {card2_int}")
        
        if card1_int < card2_int:
            return -1
        elif card1_int > card2_int:
            return 1
        else:
            continue # just making it obvious
    
    return 0

cards('sample.txt')
cards('input.txt')

# p2 first answer 249728394
# too low
# 250077062 fixed some things in pair counting

# 250829005 don't include J in card counts