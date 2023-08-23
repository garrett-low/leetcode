REQ_FIELDS = ('byr',
                'iyr',
                'eyr',
                'hgt',
                'hcl',
                'ecl',
                'pid',
                # 'cid', # cid not required
                )

def ct_valid(filename):
    passports = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        passport_i = 0
        curr_passport = {}
        for line in file:
            if line == '\n':
                passports.append(curr_passport)
                curr_passport = {}
                continue
            split_space = line.strip().split(' ')
            for key_pair in split_space:
                split_key_pair = key_pair.split(':')
                key = split_key_pair[0]
                val = split_key_pair[1]
                curr_passport[key] = val
        passports.append(curr_passport)
    
    # print(len(passports))
    
    count_valid = len(passports)
    # count_valid = 0
    for passport in passports:
        # print(passport)
        # passport_is_valid = True
        for field in REQ_FIELDS:
            if field not in passport:
                # passport_is_valid = False
                count_valid -= 1
                break
        
        # if passport_is_valid:
            # count_valid += 1
    
    print(count_valid)
        
    
ct_valid('sample.txt')
ct_valid('input.txt')

# p1 answer 208 - too high
# p1 - I was missing one of the fields (typo) - real answer is 196

# def test_dict():
    # test = {}
    # test['foo'] = 'bar'
    # print(test)
    # test.clear()
    # print(test)

# test_dict()