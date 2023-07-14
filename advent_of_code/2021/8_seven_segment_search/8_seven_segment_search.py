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

part_one('sample.txt')
part_one('input.txt')