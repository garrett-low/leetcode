score_dict = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
open_set = set(['(', '[', '{', '<'])
close_set = set([')', ']', '}', '>'])
close_dict = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}

def scoring(filename):
    error_score = 0
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
#             print(line)
            error_score += calculate(line)
    print(error_score)

def calculate(line):
    act_close_char = parse(line)
#     print(act_close_char)
    if act_close_char:
        return score_dict[act_close_char]
    return 0

def parse(line):
    return parse_inner(line, 0, [])

def parse_inner(line, idx, stack):
    if idx >= len(line):
        return None
    curr = line[idx]
    
    if curr in open_set:
        stack.append(curr)
    elif curr in close_set:
        curr_stack = stack.pop()
        exp_close = close_dict[curr_stack]
        if curr != exp_close:
            return curr
    
    return parse_inner(line, idx + 1, stack)

scoring('sample.txt')
scoring('input.txt')