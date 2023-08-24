import string

REQ_FIELDS = ('byr',
                'iyr',
                'eyr',
                'hgt',
                'hcl',
                'ecl',
                'pid',
                # 'cid', # cid not required
                )

EYE_COLOR = (
            'amb',
            'blu',
            'brn',
            'gry',
            'grn',
            'hzl',
            'oth'
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
    
    count_valid = 0
    for passport in passports:
        if is_valid(passport):
            count_valid += 1

    print(count_valid)

def is_valid(passport):
    for field in REQ_FIELDS:
        if field not in passport:
            return False

        curr = passport[field]

        if field == 'byr' and not (1920 <= int(curr) <= 2002):
            return False
        if field == 'iyr' and not (2010 <= int(curr) <= 2020):
            return False
        if field == 'eyr' and not (2020 <= int(curr) <= 2030):
            return False
        if field == 'hgt':
            h_unit = curr[-2:]
            h_val = int(curr[:-2])
            
            if h_unit != 'cm' and h_unit != 'in':
                return False
            if h_unit == 'cm' and not (150 <= h_val <= 193):
                return False
            if h_unit == 'in' and not (59 <= h_val <= 76):
                return False
        if field == 'hcl':
            if curr[0] != '#':
                return False
            if len(curr) != 7:
                return False
            # https://gist.github.com/emremrah/7921d958a632956d1ab2fa357d3c8714
            # if not curr[1:].isalnum():
            if not all(c in string.digits + 'abcdef' for c in curr[1:]):
                return False
        if field == 'ecl' and curr not in EYE_COLOR:
            return False
        if field == 'pid' and not (curr.isnumeric() and len(curr) == 9):
            return False
        
    return True

ct_valid('input.txt')
ct_valid('sample_valid.txt')
ct_valid('sample_invalid.txt')

#p2 115 too high

def negative_splice():
    a = '190cm'
    print(a[-2:])
    print(a[:-2])
    b = '#3843fe'
    print(b[1:].isalnum())
    print(b.isalnum())

# negative_splice()

def test_regex():
    color = '#1234ff'
    print