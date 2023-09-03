# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.
from collections import defaultdict
import sys

TARGET = 'balloon'

def max_target(text):
    count_char = defaultdict(int)
    for c in text:
        count_char[c] += 1
    
    count_target = 0
    done = False
    while not done:
        for c in TARGET:
            count_char[c] -= 1
            if count_char[c] < 0:
                done = True
                break
        if not done:
            count_target += 1
        
    print(count_target)
    return(count_target)

max_target("nlaebolko")
max_target("loonbalxballpoon")
max_target("leetcode")
max_target("balon")