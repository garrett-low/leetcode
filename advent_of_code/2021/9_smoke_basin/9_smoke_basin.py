directions = [(0, 1),
              (1, 0),
              (0, -1),
              (-1, 0)]

def smoke(filename):
    heightmap = []
    with open(filename, 'rt', encoding = 'utf-8') as file:
        for line in file:
            heightmap.append(line.strip())
    
    print(heightmap)
    for row in heightmap:
        for col in row:
            pass

smoke('sample.txt')