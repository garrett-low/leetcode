from collections import defaultdict

def two_sum(filename):
    complement_set = set()
    curr_int = 0
    complement_int = 0
    is_found = False
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            curr_int = int(line.strip())
            complement_int = 2020 - curr_int
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

def three_sum(filename):
    complement_set = set()
    curr_int = 0
    complement_int = 0
    is_found = False
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            curr_int = int(line.strip())
            complement_int = 2020 - curr_int
            if complement_int in complement_set:
                is_found = True
                break
            else:
                complement_set.add(curr_int)
    
    if is_found:
        print(f"FOUND: {curr_int * complement_int}")
    else:
        print("DID NOT FIND PAIR THAT SUMS TO 2020!")