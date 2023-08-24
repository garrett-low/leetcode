def count_answers(filename):
    yes_count = 0
    with open(filename, 'rt', encoding = 'utf-8') as file:
        curr_group_answer_list = []
        for line in file:
            if line == '\n':
                count_answer = check_same_answer(curr_group_answer_list)
                yes_count += count_answer
                curr_group_answer_list = []
                continue
            
            person_answer_set = set(line.strip())
            curr_group_answer_list.append(person_answer_set)
        
        yes_count += check_same_answer(curr_group_answer_list)
    print(yes_count)

def check_same_answer(curr_group_answer_list):
    if len(curr_group_answer_list) <= 0:
        return 0
    
    first_person_answer_set = curr_group_answer_list[0]
    if len(curr_group_answer_list) == 1:
        return len(first_person_answer_set)
    
    # intentionally not using set.intersection built in because
    # I'll probably forget the syntax
    for i in range(1, len(curr_group_answer_list)):
        curr_answer_set = curr_group_answer_list[i]
        set_intersect = set()
        
        if len(curr_answer_set) < len(first_person_answer_set):
            smaller = curr_answer_set
            larger = first_person_answer_set
        else:
            larger = curr_answer_set
            smaller = first_person_answer_set
        
        for answer in smaller:
            if answer in larger:
                set_intersect.add(answer)
        
        if len(set_intersect) <= 0:
            return 0
        
        first_person_answer_set = set_intersect
    
    return len(set_intersect)

count_answers('sample2.txt')
count_answers('input.txt') #p2 3221