def dive(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        x = 0
        aim = 0
        depth = 0
        for line in file:
            split = line.split(' ')
            move = split[0].strip()
            steps = int(split[1].strip())
            if move == 'forward':
                x += steps
                depth = aim * steps + depth
            elif move == 'up':
                aim -= steps
            elif move == 'down':
                aim += steps
#             print(f"x: {x}, depth: {depth}")
    
    print(f"x*depth: {x * depth}")
    return

dive('sample.txt')
dive('input.txt')