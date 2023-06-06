# find any overlap in the pairs

def camp_cleanup():
    pairs = []
    total_pairs = 0
    
    with open('input.txt', 'rt', encoding='utf-8') as file:
        for line in file:
            pairs = line.split(',')
            range_one = pairs[0]
            range_two = pairs[1]
            range_one_lower = int(range_one[ : range_one.index('-')])
            range_one_upper = int(range_one[(range_one.index('-') + 1) : ])
            range_two_lower = int(range_two[ : range_two.index('-')])
            range_two_upper = int(range_two[(range_two.index('-') + 1) : ])
            
            if range_one_upper >= range_two_lower and range_one_upper <= range_two_upper:
                total_pairs += 1
            elif range_two_upper >= range_one_lower and range_two_upper <= range_one_upper:
                total_pairs += 1
                
    print(total_pairs)
    
camp_cleanup()
