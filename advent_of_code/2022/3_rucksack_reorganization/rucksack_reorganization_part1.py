def rucksack_reorg():
    first_set = set()
    second_set = set()
    sum_pri = 0
    with open('input.txt', 'rt', encoding='utf-8') as file:
        for line in file:
            line_len = len(line)
            split_index = line_len // 2
            first_contents = line[:split_index]
            second_contents = line[split_index:]
            first_set.update(first_contents)
            second_set.update(second_contents)
            intersect = first_set.intersection(second_set)
            for item in intersect:
                sum_pri += priority(item)
            first_set.clear()
            second_set.clear()
            
    
    print(sum_pri)

def priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96
    
rucksack_reorg()