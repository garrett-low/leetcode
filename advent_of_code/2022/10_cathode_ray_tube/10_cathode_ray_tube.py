def sum_signal(filename):
    register = 1
    cycle = 1
#     target_cycle = [20, 60, 100, 140, 180, 220]s
    target_register = {}
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
#             print(f"{cycle}: {line} ({register})")
            mod_cycle = (cycle - 20) % 40
            if cycle == 20 or mod_cycle == 0:
                target_register.update({cycle : register})
            elif cycle == 19 or mod_cycle == 39:
                target_register.update({(cycle + 1) : register})
            split = line.split(' ')
            op = split[0]
            if op == 'addx':
                register += int(split[1])
                cycle += 2
            else:
                cycle += 1
    
    print(target_register)
    sum_register = 0
    for cycle, register in target_register.items():
        sum_register += cycle * register
    print(sum_register)

# part two
def crt(filename):
    register = 0
    cycle = 0
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
#             print(f"{cycle}: {line} ({register})")
            split = line.split(' ')
            op = split[0]
            if op == 'addx':
                # pre
                print_crt(register, cycle)
                cycle += 1
                print_crt(register, cycle)
                cycle += 1
                register += int(split[1])
            else:
                print_crt(register, cycle)
                cycle += 1

def print_crt(register, cycle):
    mod_cycle = cycle % 40
    if mod_cycle == 0:
        print()
    if register >= cycle - 1 and register <= cycle + 1:
        print(chr(9608), end='')
    else:
        print(chr(9617), end='')

sum_signal("sample.txt")
sum_signal("input.txt")
crt("sample.txt")