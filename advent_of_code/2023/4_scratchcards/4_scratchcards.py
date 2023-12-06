import math

def scratchcards(filename):
    winning_sets = []
    my_nums_list = []
    with open(filename, 'rt') as file:
        for line in file:
            all_nums = line.strip().split(':')[1].split('|')
            winning_nums = set()
            for winning_num in all_nums[0].strip().split():
                winning_nums.add(int(winning_num))
            my_nums = [int(x) for x in all_nums[1].strip().split()]
            
            winning_sets.append(winning_nums)
            my_nums_list.append(my_nums)
            
    print(winning_sets)
    print(my_nums_list)
    
    total_score = 0
    
    for i in range(len(winning_sets)):
        score_exp = 0
        for my_num in my_nums_list[i]:
            if my_num in winning_sets[i]:
                score_exp += 1
                # print(f"Round {i}: {my_num} win!")
            
        if score_exp > 0:
            total_score += math.pow(2, score_exp - 1)
    
    total_score = int(total_score)
    print(total_score)
    
    
scratchcards('sample.txt')
scratchcards('input.txt') # 23028

