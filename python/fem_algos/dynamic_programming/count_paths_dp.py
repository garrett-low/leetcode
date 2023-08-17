# Here is a solution to the “Unique Paths” problem from an exercise in the
# previous chapter. Use memoization to improve its efficiency:

def count_paths_out(n_rows, n_cols):
    print("non-DP:", count_paths(n_rows, n_cols, 0))
    print("with memo:", count_paths_memo(n_rows, n_cols, {}, 0))

def count_paths(n_rows, n_cols, depth):
    depth += 1
    print(depth)
    if n_rows == 1 or n_cols == 1:
        return 1
    return count_paths(n_rows - 1, n_cols, depth) + count_paths(n_rows, n_cols - 1, depth)

def count_paths_memo(n_rows, n_cols, memo_dict, depth):
    depth += 1
    print(depth)
    if n_rows == 1 or n_cols == 1:
        return 1
        
    coord_tuple = (n_rows, n_cols)
    if coord_tuple not in memo_dict:
        memo_dict[coord_tuple] = count_paths_memo(n_rows - 1, n_cols, memo_dict, depth) + count_paths_memo(n_rows, n_cols - 1, memo_dict, depth)
    
    return memo_dict[coord_tuple]

count_paths_out(3, 8)
