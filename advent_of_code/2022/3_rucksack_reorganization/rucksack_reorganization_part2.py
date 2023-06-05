def rucksack_reorg():
    first_set = set()
    second_set = set()
    third_set = set()
    intersect_one = set()
    intersect_two = set()
    line_counter = 0
    sum_pri = 0
    with open('input.txt', 'rt', encoding='utf-8') as file:
        for line in file:
            line_counter += 1
            val = line.strip()
            if line_counter % 3 == 1:
                first_set.update(val)
            if line_counter % 3 == 2:
                second_set.update(val)
            if line_counter % 3 == 0:
                third_set.update(val)
                intersect_one = first_set.intersection(second_set)
                intersect_two = intersect_one.intersection(third_set)
                for item in intersect_two:
                    sum_pri += priority(item)
                
                first_set.clear()
                second_set.clear()
                third_set.clear()
                intersect_one.clear()
                intersect_two.clear()
                line_counter = 0        
    
    print(sum_pri)

def priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96
    
rucksack_reorg()
