# Common-Sense DSA: Chapter 11
# Count unique paths
# Write a function that accepts a number of rows
# and a number of columns, and calculates the number of possible “shortest”
# paths from the upper-leftmost square to the lower-rightmost square.

def count_paths(num_rows, num_cols):
    if num_rows == 0 or num_cols == 0:
        print("invalid input")
        return
    
    count = count_inner(num_rows, num_cols)
    print(count)

def count_inner(num_rows, num_cols):
    if num_rows == 1 or num_cols == 1:
        return 1
    return count_inner(num_rows - 1, num_cols) + count_inner(num_rows, num_cols - 1)

count_paths(3, 7)