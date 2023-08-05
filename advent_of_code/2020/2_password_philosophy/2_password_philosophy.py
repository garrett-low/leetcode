def count_valid_pw(filename):
    count_valid = 0
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            # extract
            colon_split = line.strip().split(':')
            pw = colon_split[1]
            space_split = colon_split[0].split(' ')
            required_char = space_split[1]
            hyphen_split = space_split[0].split('-')
            lower_bound = int(hyphen_split[0])
            upper_bound = int(hyphen_split[1])
            
            # transform
            count_required = pw.count(required_char)
            if count_required >= lower_bound and count_required <= upper_bound:
                count_valid += 1
    
    # load
    print(count_valid)

count_valid_pw('sample.txt')
count_valid_pw('input.txt')

def count_valid_pw_part_two(filename):
    count_valid = 0
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            # extract
            colon_split = line.strip().split(':')
            pw = colon_split[1]
            space_split = colon_split[0].split(' ')
            required_char = space_split[1]
            hyphen_split = space_split[0].split('-')
            first_i = int(hyphen_split[0])
            second_i = int(hyphen_split[1])
            
            # transform
            if pw[first_i] == required_char and pw[second_i] != required_char:
                count_valid += 1
            elif pw[second_i] == required_char and pw[first_i] != required_char:
                count_valid += 1
    
    # load
    print(count_valid)

count_valid_pw_part_two('sample.txt')
count_valid_pw_part_two('input.txt')