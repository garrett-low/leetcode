# sum of integers 1...N is ((N + 1) * N)/2

import ast
import math

def find_median(filename):
    ary = []
    with open(filename, 'rt', encoding='utf-8') as file:
        input_str = '[' + file.readline().strip() + ']'
        ary = ast.literal_eval(input_str)
    qs(ary)
#     print(ary)
#     print(len(ary))
#     print(len(ary)//2)
    
    if len(ary) % 2 == 0:
        median = (ary[(len(ary)//2) - 1] + ary[(len(ary)//2)]) // 2
    else:
        median = ary[len(ary)//2]
    print(f"median:\t{median}")
    
    retval = 0
    for i in range(len(ary)):
        retval += abs(ary[i] - median)
    print(f"fuel:\t{retval}")

def qs(ary):
    qs_inner(ary, 0, len(ary) - 1)
    return ary

def qs_inner(ary, lo, hi):
    if lo >= hi or lo < 0:
        return
    p = pivot(ary, lo, hi)
    qs_inner(ary, p + 1, hi)
    qs_inner(ary, lo, p - 1)

def pivot(ary, lo, hi):
    p = ary[hi]
    
    p_idx = lo - 1
    for i in range(lo, hi):
        if ary[i] < p:
            p_idx += 1
            temp = ary[i]
            ary[i] = ary[p_idx]
            ary[p_idx] = temp
    
    p_idx += 1
    ary[hi] = ary[p_idx]
    ary[p_idx] = p
    return p_idx

def part_two(filename):
    crab_sum = 0
    curr_int_str = ""
    crab_ary = []
    with open(filename, 'rt', encoding='utf-8') as file:
        while True:
            char = file.read(1)
            if char == ',' or char.isspace() or not char:
                crab_pos = int(curr_int_str)
                crab_sum += crab_pos
                crab_ary.append(crab_pos)
                curr_int_str = ""
                if not char:
                    break
            else:
                curr_int_str += char
    print(crab_sum)
    avg = crab_sum / len(crab_ary)
    print(f"mean:\t{avg}")
    avg_ceil = math.ceil(avg)
    avg_floor = math.floor(avg)
    
    fuel_min = calculate_fuel(crab_ary, avg_ceil, avg_floor)
    print(fuel_min)

def calculate_fuel(crab_ary, match_pos1, match_pos2):
    fuel_pos1 = 0
    fuel_pos2 = 0
    # (N * (N + 1)) / 2
    for crab_pos in crab_ary:
        dist1 = abs(crab_pos - match_pos1)
        dist2 = abs(crab_pos - match_pos2)
        fuel_pos1 += (dist1 * (dist1 + 1)) // 2
        fuel_pos2 += (dist2 * (dist2 + 1)) // 2
    
    if fuel_pos1 < fuel_pos2:
        return fuel_pos1
    else:
        return fuel_pos2

find_median("sample.txt")
find_median("input.txt")

part_two("sample.txt")
part_two("input.txt")