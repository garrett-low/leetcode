# tuning trouble part 2
def tuning():
    with open('input.txt', 'rt', encoding = 'utf-8') as file:
        for line in file:
            check_set = set()
            for i in range(14, len(line), 1):
                check_set.update(line[i - 14 : i])
                if len(check_set) == 14:
                    print(f"{i}")
                    return i
                check_set.clear()
                
tuning()