# Common-sense guide to DSA: Chapter 8 - Exercise 3
# Find missing letter in alphabet. input string will have one missing letter.

def missing_letter(test_string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    for char in test_string:
        if char.lower() in alphabet:
            alphabet.remove(char.lower())
    
    if len(alphabet) > 0:
        print(alphabet)
    else:
        print("input string contains all letters!")

missing_letter("the quick brown box jumps over the lazy dog")
missing_letter("The five boxing wizards jump quickly")
missing_letter("The five boxing wizards pump quickly")