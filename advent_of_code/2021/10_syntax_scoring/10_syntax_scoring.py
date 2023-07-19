score_dict = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
open_set = set(['(', '[', '{', '<'])
close_set = set([')', ']', '}', '>'])
close_dict = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}

print(open_set)

def scoring(filename):
    error_score = 0
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            print(line)
            error_score += calculate(line)
    print(error_score)

def calculate(line):
    is_unmatched, act_close_char = parse(line, 0, line[0])
    if is_unmatched:
        print(act_close_char)
        return score_dict[act_close_char]
    return 0

def parse(line, curr_idx, open_parent = None):
    curr = line[curr_idx]
    if curr_idx >= len(line):
        return False, None
    
    print(f"char: {curr}, open_parent: {open_parent}")
    if curr in close_set:
        exp_close_char = close_dict[open_parent]
        if exp_close_char != curr:
            return True, curr
        
    if curr in open_set:
        open_parent = curr
    is_unmatched, act_close_char = parse(line, curr_idx + 1, open_parent)
#     print(is_unmatched, act_close_char)
    return is_unmatched, act_close_char
    
scoring('sample.txt')