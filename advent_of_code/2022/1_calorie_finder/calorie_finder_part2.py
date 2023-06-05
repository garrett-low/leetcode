def calorie_finder():
    with open('input.txt', 'rt', encoding='utf-8') as file:
        calories_per_elf = []
        current_cal = 0
        for line in file:
            if line == '' or line == '\n':
                calories_per_elf.append(current_cal)
                current_cal = 0
            else:
                current_cal += int(line)
    
    calories_per_elf.sort(reverse=True)
    print(f"{calories_per_elf[0]}, {calories_per_elf[1]}, {calories_per_elf[2]}")
    
    top_three_cal = calories_per_elf[0] + calories_per_elf[1] + calories_per_elf[2]
    print(f"{top_three_cal}")
    return

calorie_finder()
