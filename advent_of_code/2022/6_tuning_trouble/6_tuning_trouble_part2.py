import time
# tuning trouble part 2
def tuning():
    t1 = time.perf_counter()
    with open('input.txt', 'rt', encoding = 'utf-8') as file:
        for line in file:
            check_set = set()
            for i in range(14, len(line), 1):
                check_set.update(line[i - 14 : i])
                if len(check_set) == 14:
                    print(f"{i}")
                    break
                check_set.clear()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
                
tuning()