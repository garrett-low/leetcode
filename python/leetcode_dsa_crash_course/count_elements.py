def count_elements(arr):
    num_set = set(arr)
    output = 0
    
    for _, val in enumerate(arr):
        if val + 1 in num_set:
            output += 1
    
    print(output)
    return(output)

count_elements([1,2,3])
count_elements([1,1,3,3,5,5,7,7])