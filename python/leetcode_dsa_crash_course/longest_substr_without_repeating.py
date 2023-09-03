# Given a string s, find the length of the longest substring without repeating characters.
from collections import defaultdict

def longest(s):
    start = 0
    curr_len = 0
    max_len = 0
    
    freq = defaultdict(int)
    for i, val in enumerate(s):
        freq[val] += 1
        
        while freq[val] > 1:
            remove_c = s[start]
            freq[remove_c] -= 1
            start += 1
        
        curr_len = i - start + 1
        if curr_len > max_len:
            max_len = curr_len
    
    print(max_len)
    return(max_len)

longest('abcabcbb')
longest('bbbbb')
longest('pwwkew')