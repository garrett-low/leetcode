# The following function uses recursion to calculate the Nth number from
# a mathematical sequence known as the “Golomb sequence.” It’s terribly
# inefficient, though! Use memoization to optimize it. (You don’t have to
# actually understand how the Golomb sequence works to do this exercise.)
# def golomb(n)
# return 1 if n == 1
# return 1 + golomb(n - golomb(golomb(n - 1)));
# end

def golomb(n):
    if n == 1:
        return 1
    print("hello!")
    return 1 + golomb(n - golomb(golomb(n - 1)))

print(golomb(5))
# print(golomb(6))

def golomb_dp(n, inmost_dict, middle_dict, outmost_dict):
    if n == 1:
        return 1
    print("dp hello!")
    if (n - 1) not in inmost_dict:
        inmost_dict[n - 1] = golomb_dp(n - 1, inmost_dict, middle_dict, outmost_dict)
    if (n - 1) not in middle_dict:
        middle_dict[n - 1] = golomb_dp(inmost_dict[n - 1], inmost_dict, middle_dict, outmost_dict)
    if (n - 1) not in outmost_dict:
        outmost_dict[n - 1] = golomb_dp(n - middle_dict[n - 1], inmost_dict, middle_dict, outmost_dict)
    
    return 1 + outmost_dict[n - 1]

def golomb_dp_outer(n):
    inmost_dict = {}
    middle_dict = {}
    outmost_dict = {}
    print(golomb_dp(n, inmost_dict, middle_dict, outmost_dict))

golomb_dp_outer(5)
# golomb_dp_outer(6)

def golomb_book_sol_outer(n):
    result = golomb_book_sol(n, {})
    print(result)

def golomb_book_sol(n, memo_dict):
    if n == 1:
        return 1
    print("book sol!")
    if n not in memo_dict:
        memo_dict[n] = 1 + golomb_book_sol(n - golomb_book_sol(golomb_book_sol(n - 1, memo_dict), memo_dict), memo_dict)
    
    return memo_dict[n]

golomb_book_sol_outer(5)