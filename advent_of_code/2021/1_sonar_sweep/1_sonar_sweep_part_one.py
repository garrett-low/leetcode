def sweep(filename):
    with open(filename, 'rt', encoding='utf-8') as file:
        prev = None
        curr = None
        num_increase = 0
        for line in file:
            curr = int(line)
            if prev != None and curr > prev:
                num_increase += 1
            prev = curr
    
    print(num_increase)
    return

sweep('sample.txt')
sweep('input.txt')