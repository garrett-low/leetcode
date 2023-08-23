# class group:
    # def __init__(self):
        # self.group.answer_set = set()
        # self.group.individual_answers = []
    
    # def __str__(self):
        # print(self.group.answer_set)

def count_answers(filename):
    groups_answer_set = []
    yes_count = 0
    with open(filename, 'rt', encoding = 'utf-8') as file:
        answer_set = set()
        for line in file:
            if line == '\n':
                yes_count += len(answer_set)
                groups_answer_set.append(answer_set)
                answer_set = set()
                continue
            
            person_answers = list(line.strip())
            answer_set.update(person_answers)
        
        yes_count += len(answer_set)
        groups_answer_set.append(answer_set)
    
    print(yes_count)

count_answers('sample2.txt')
count_answers('input.txt') # p1 6735