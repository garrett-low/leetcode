def part_one(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        retval = 0
        for line in file:
            line = line.strip()
            line_split = line.split('|')
            output = line_split[1].split(' ')
            for string in output:
                len_str = len(string)
                if len_str == 2 or len_str == 3 or len_str == 4 or len_str == 7:
                    retval += 1
    print(retval)

print("PART ONE")
part_one('sample.txt')
part_one('input.txt')

def part_two(filename):
    retval = 0
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            line = line.strip()
            line_split = line.split('|')
            input_seg = line_split[0].split(' ')
            output_seg = line_split[1].split(' ')
            retval += calculate(input_seg, output_seg)
    print(retval)
    return
            
def calculate(input_seg, output_seg):
    # key = digit, val = set of segment characters
#     digit_dict = {}
    digit_dict_reverse = {}
    for i in range(10):
        digit_dict_reverse[i] = set()
    input_unk = []
    # unique segments
    for seg in input_seg:
        if len(seg) == 2:
#             digit_dict[seg] = 1
            digit_dict_reverse[1].update(seg)
        elif len(seg) == 3:
#             digit_dict[seg] = 7
            digit_dict_reverse[7].update(seg)
        elif len(seg) == 4:
#             digit_dict[seg] = 4
            digit_dict_reverse[4].update(seg)
        elif len(seg) == 7:
#             digit_dict[seg] = 9
            digit_dict_reverse[8].update(seg)
        else:
            input_unk.append(seg)
    # undetermined segments
    for seg in input_unk:
        set_seg = set(seg)
        if len(set_seg) == 5:
            if set_seg.issuperset(digit_dict_reverse[1]): # 3
#                 digit_dict[seg] = 3
                digit_dict_reverse[3] = set_seg
            else: # 2 and 5
                len_intersect = len(set_seg.intersection(digit_dict_reverse[4]))
                if len_intersect == 3:
#                     digit_dict[seg] = 5
                    digit_dict_reverse[5] = set_seg
                elif len_intersect == 2:
#                     digit_dict[seg] = 2
                    digit_dict_reverse[2] = set_seg
        elif len(seg) == 6:
            if set_seg.issuperset(digit_dict_reverse[4]):
#                 digit_dict[seg] = 9
                digit_dict_reverse[9] = set_seg
            else: # 6, 0
                len_diff = len(set_seg.difference(digit_dict_reverse[7]))
                if len_diff == 3:
#                     digit_dict[seg] = 0
                    digit_dict_reverse[0] = set_seg
                elif len_diff == 4:
#                     digit_dict[seg] = 6
                    digit_dict_reverse[6] = set_seg
    # calculate output
    output = 0
    for i in range(len(output_seg)):
        output_seg_set = set(output_seg[i])
        for j in range(10):
            test_set = digit_dict_reverse[j]
            if test_set == output_seg_set:
                output += j * pow(10, 4 - i)
                break
#     print(output)
    return output

print("PART TWO")
part_two('sample.txt')
part_two('input.txt')