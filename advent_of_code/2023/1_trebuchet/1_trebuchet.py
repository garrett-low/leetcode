# def forgot_syntax(string):
    # for c in string:
        # if c.isnumeric():
            # print(int(c))

# forgot_syntax('asdf123fdadf3j3kl8l9dfd')
import sys

def trebuchet(filename):
    vals = []
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            for i in range(len(line)):
                if line[i].isnumeric():
                    first_digit = line[i]
                    break
            
            for i in range(len(line) - 1, -1, -1):
                if line[i].isnumeric():
                    last_digit = line[i]
                    break
            
            vals.append(int(first_digit + last_digit))
    
    sum = 0
    for val in vals:
        sum += val
    
    print(sum)

trebuchet('sample.txt')
trebuchet('input.txt')

NUM_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def trebuchet_p2(filename):
    vals = []
    line_idx = 0
    with open(filename, 'rt') as file:
        for line in file:
            # print(f"LINE #{line_idx}")
            line = line.strip()
            line_len = len(line)
            first_digit_num_idx = sys.maxsize
            first_digit_word_idx = sys.maxsize
            last_digit_num_idx = -1
            last_digit_word_idx = -1
            
            for i in range(line_len):
                if line[i].isnumeric():
                    first_digit_num = line[i]
                    first_digit_num_idx = i
                    break
            
            for i in range(line_len):
                if i + 3 < line_len:
                    test_val = line[i : i + 3]
                    if test_val in NUM_DICT:
                        first_digit_word = NUM_DICT[test_val]
                        first_digit_word_idx = i
                        break
                if i + 4 < line_len:
                    test_val = line[i : i + 4]
                    if test_val in NUM_DICT:
                        first_digit_word = NUM_DICT[test_val]
                        first_digit_word_idx = i
                        break
                if i + 5 < line_len:
                    test_val = line[i : i + 5]
                    if test_val in NUM_DICT:
                        first_digit_word = NUM_DICT[test_val]
                        first_digit_word_idx = i
                        break
            
            if first_digit_num_idx < first_digit_word_idx or first_digit_word_idx == sys.maxsize:
                first_digit = first_digit_num
            else:
                first_digit = first_digit_word
            
            for i in range(line_len - 1, -1, -1):
                if line[i].isnumeric():
                    last_digit_num = line[i]
                    last_digit_num_idx = i
                    break
            
            for i in range(line_len, -1, -1):
                if i - 3 >= 0:
                    test_val = line[i - 3 : i]
                    if test_val in NUM_DICT:
                        last_digit_word = NUM_DICT[test_val]
                        last_digit_word_idx = i - 3
                        break
                if i - 4 >= 0:
                    test_val = line[i - 4 : i]
                    if test_val in NUM_DICT:
                        last_digit_word = NUM_DICT[test_val]
                        last_digit_word_idx = i - 4
                        break
                if i - 5 >= 0:
                    test_val = line[i - 5 : i]
                    if test_val in NUM_DICT:
                        last_digit_word = NUM_DICT[test_val]
                        last_digit_word_idx = i - 5
                        break
            
            # print(f"  {first_digit_num_idx}: {first_digit_num}")
            # print(f"  {first_digit_word_idx}: {first_digit_word}")
            # print(f"  {last_digit_num_idx}: {last_digit_num}")
            # print(f"  {last_digit_word_idx}: {last_digit_word}")
            if last_digit_num_idx > last_digit_word_idx or last_digit_word_idx == -1:
                last_digit = last_digit_num
            else:
                last_digit = last_digit_word
            
            # print(f"  RESULT:  {first_digit}{last_digit}")
            
            vals.append(int(first_digit + last_digit))
            
            line_idx += 1
    
    # print(vals)
    
    sum = 0
    for val in vals:
        sum += val
    
    print(sum)
            
trebuchet_p2('sample_p2.txt')
trebuchet_p2('input.txt')

# not 53261 for P2 (too low)
# 53268