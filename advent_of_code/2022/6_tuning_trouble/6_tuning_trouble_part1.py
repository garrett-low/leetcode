# tuning trouble
def tuning():
    with open('input.txt', 'rt', encoding = 'utf-8') as file:
        for line in file:
            check_set = set()
            for i in range(4, len(line), 1):
                check_set.update(line[i - 4 : i])
                if len(check_set) == 4:
                    print(f"{i}")
                    return i
                check_set.clear()
                
tuning()