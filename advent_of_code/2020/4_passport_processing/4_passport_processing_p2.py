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
    
    count_valid = len(passports)
    for passport in passports:
        for field in REQ_FIELDS:
            if field not in passport:
                count_valid -= 1
                break

    print(count_valid)

ct_valid('input.txt')