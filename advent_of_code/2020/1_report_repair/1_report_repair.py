from collections import defaultdict

TARGET_SUM = 2020

def two_sum(filename):
    complement_set = set()
    curr_int = 0
    complement_int = 0
    is_found = False
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            curr_int = int(line.strip())
            complement_int = TARGET_SUM - curr_int
            if complement_int in complement_set:
                is_found = True
                break
            else:
                complement_set.add(curr_int)
    
    if is_found:
        print(f"FOUND: {curr_int * complement_int}")
    else:
        print("DID NOT FIND PAIR THAT SUMS TO 2020!")

print("PART ONE")
two_sum('sample.txt')
two_sum('input.txt')

# assuming no duplicates in input...
def three_sum(filename):
    int_list = []
    int_set = set()
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            # int_list.append[int(line.strip())]
            int_set.add(int(line.strip()))
    # print(int_set)
    
    is_found = False
    for first_int in int_set:
        first_remainder = TARGET_SUM - first_int
        for second_int in int_set:
            if first_int == second_int:
                continue
            
            test_remainder = first_remainder - second_int
            if test_remainder in int_set:
                is_found = True
                break
        if is_found:
            break
    if is_found:
        print(f"FOUND: {first_int} * {second_int} * {test_remainder} = {first_int * second_int * test_remainder}")
    else:
        print("DID NOT FIND PAIR THAT SUMS TO 2020!")
    
    
    
    # complement_set = set()
    # is_found = False
    # for i in range(len(int_list)):
        # int_i = int_list[i]
        # complement_int_i = TARGET_SUM - int_i
        # for j in range(len(int_list)):
            # if i == j:
                # continue
            
            # int_j = int_list[j]
            # complement_int_j = complement_int_i - int_j
            # if complement_int_j in complement_set:
                # is_found = True
                # break;
            # else:
                # complement_set.add(

print("PART TWO")
three_sum('sample.txt')
three_sum('input.txt')