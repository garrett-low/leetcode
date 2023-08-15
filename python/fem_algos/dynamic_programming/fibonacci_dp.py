# Print fibonacci with and without dynamic programming through memoization
# and going botom up

def fib_non_dp(nth):
    nth_val = fib_non_dp_inner(nth)
    print(nth_val)

def fib_non_dp_inner(nth):
    if nth <= 1:
        return nth
    
    return fib_non_dp_inner(nth - 1) + fib_non_dp_inner(nth - 2)

fib_non_dp(8)

def fib(nth):
    nth_val = fib_inner(nth, {})
    print(nth_val)

def fib_inner(nth, sum_dict):
    if nth <= 1:
        return nth
    
    if (nth - 1)  not in sum_dict:
        sum_dict[nth - 1] = fib_inner(nth - 1, sum_dict)
    if (nth - 2) not in sum_dict:
        sum_dict[nth - 2] = fib_inner(nth - 2, sum_dict)
    
    return sum_dict[nth - 1] + sum_dict[nth - 2]

fib(8)

def fib_bot_up(nth):
    nth_val = fib_bot_up_inner(nth)
    print(nth_val)

def fib_bot_up_inner(nth):
    if nth <= 1:
        return nth
    
    prev = 0
    curr = 1
    for i in range(1, nth):
        prev_prev = prev
        prev = curr
        curr = prev + prev_prev
    
    return curr

fib_bot_up(8)