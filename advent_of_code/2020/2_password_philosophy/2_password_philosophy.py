def count_valid_pw(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            colon_split = line.strip().split(':')
            pw = colon_split[1]
            space_split = colon_split[0].split(' ')
            required_char = space_split[1]
            hyphen_split = space_split[0].split('-')
            lower_bound = hyphen_split[0]
            upper_bound = hyphen_split[1]
            