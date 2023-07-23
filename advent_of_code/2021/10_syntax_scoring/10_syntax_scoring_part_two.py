score_dict = {')' : 1, ']' : 2, '}' : 3, '>' : 4}
open_set = set(['(', '[', '{', '<'])
close_set = set([')', ']', '}', '>'])
close_dict = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
SCORE_MULTIPLIER = 5

def scoring(filename):
    score_list = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            score = calculate(line)
            if score:
                score_list.append(score)
    qs(score_list)
    median = score_list[len(score_list) // 2]
    print(median)

def calculate(line):
    stack_unclosed = parse(line)
    score = 0
    if stack_unclosed == None:
        return None
    while len(stack_unclosed) > 0:
        score *= SCORE_MULTIPLIER
        curr_incomplete = close_dict[stack_unclosed.pop()]
        score_incomplete = score_dict[curr_incomplete]
        score += score_incomplete
    return score

def parse(line):
    return parse_inner(line, 0, [])

def parse_inner(line, idx, stack):
    if idx >= len(line):
        return stack
    curr = line[idx]
    
    if curr in open_set:
        stack.append(curr)
    elif curr in close_set:
        curr_stack = stack.pop()
        exp_close = close_dict[curr_stack]
        if curr != exp_close:
            return None
    
    return parse_inner(line, idx + 1, stack)

def qs(arr):
    qs_inner(arr, 0, len(arr) - 1)

def qs_inner(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    p = pivot(arr, lo, hi)
    
    qs_inner(arr, p + 1, hi)
    qs_inner(arr, lo, p - 1)

def pivot(arr, lo, hi):
    p_val = arr[hi]
    
    p = lo - 1
    for i in range(lo, hi):
        if arr[i] < p_val:
            p += 1
            temp = arr[i]
            arr[i] = arr[p]
            arr[p] = temp
    
    p += 1
    arr[hi] = arr[p]
    arr[p] = p_val
    return p

scoring('sample.txt')
scoring('input.txt')
