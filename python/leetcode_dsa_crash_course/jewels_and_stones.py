def jewels_and_stones(jewels, stones):
    jewel_set = set(jewels)
    count = 0
    
    for stone in stones:
        if stone in jewel_set:
            count += 1
    
    print(count)
    return(count)

jewels_and_stones('aA', 'aAAbbbb')