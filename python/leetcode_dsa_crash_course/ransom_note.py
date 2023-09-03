# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
from collections import defaultdict

def construct(ransomNote, magazine):
    count_mag = defaultdict(int)
    
    for c in magazine:
        count_mag[c] += 1
    
    for c in ransomNote:
        count_mag[c] -= 1
        if count_mag[c] < 0:
            print("False")
            return False
    
    print("True")
    return True

construct('a', 'b')
construct('aa', 'ab')
construct('aa', 'aab')