# You’re working on some more stock-prediction software. The function
# you’re writing accepts an array of predicted prices for a particular stock
# over the course of time.
# For example, this array of seven prices:
# [10, 7, 5, 8, 11, 2, 6]
# predicts that a given stock will have these prices over the next seven days.
# (On Day 1, the stock will close at $10; on Day 2, the stock will close at
# $7; and so on.)

def greatest_profit_single(arr):
    start_i = 0
    max_start_i = 0
    max_end_i = 0
    max_profit = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[start_i]:
            start_i = i
        else:
            test_profit = arr[i] - arr[start_i]
            if test_profit > max_profit:
                max_profit = test_profit
                max_end_i = i
                max_start_i = start_i
    
    print(f"Max single-sell profit:\t{max_profit}\tBuy:\t{arr[max_start_i]}\tSell:\t{arr[max_end_i]}")

greatest_profit_single([10, 7, 5, 8, 11, 2, 6])