# import os

def calorie_finder():
#     print(os.path.isfile('input.txt'))
    with open('input.txt', 'rt', encoding='utf-8') as file:
        max_cal = 0
        current_cal = 0
        for line in file:
#             print(line)
            if line == '' or line == '\n':
                if current_cal >= max_cal:
                    max_cal = current_cal
#                     print(max_cal)
                current_cal = 0
            else:
                current_cal += int(line)
    print(max_cal)
    return max_cal

calorie_finder()