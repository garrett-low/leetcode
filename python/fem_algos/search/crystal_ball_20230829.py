import math

# crystal ball from memory

def crystal_ball(floors):
    prev = 0
    curr = 0
    squirt = int(math.sqrt(len(floors)))
    
    while curr < len(floors):
        if floors[curr]:
            break
        prev = curr
        curr += squirt
    
    for i in range(prev, curr + 1):
        if floors[i]:
            print(f"crystal ball breaks at:\t{i}")
            return
    
    print("no break!")
    return

crystal_ball([False, False, False, False, False, False, False, False, False, True, True, True, True, True])