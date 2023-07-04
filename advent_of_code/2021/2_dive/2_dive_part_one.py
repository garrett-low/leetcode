def dive(filename):
    with open(filename, 'rt', encoding = 'utf-8') as file:
        x = 0
        y = 0
        for line in file:
            split = line.split(' ')
            move = split[0].strip()
            steps = int(split[1].strip())
            if move == 'forward':
                x += steps
            elif move == 'up':
                y -= steps
            elif move == 'down':
                y += steps
        
    print(f"x: {x}, y: {y}")
    print(f"x*y: {x * y}")
    return

dive('sample.txt')
dive('input.txt')