# Common-Sense DSA: Chapter 11
# Generate anagrams

def anagram(input):
    anagram_list = ana_inner(input)
    print(anagram_list)

def ana_inner(input):
    if len(input) == 1:
        return [input[0]]
    
    anagram_list = []
    anagrams_of_substrings = ana_inner(input[1:])
    for ana in anagrams_of_substrings:
        for i in range(len(ana) + 1):
            new_ana = ana[:i] + input[0] + ana[i:]
            anagram_list.append(new_ana)
    
    return anagram_list

anagram('abcde')