import math 

def crystal_ball(floors):
    length = len(floors)
    squirt = int(math.sqrt(length))
    
    curr = squirt
    while curr <= length:
        if floors[curr]:
            lower_bound = curr - squirt
            for i in range(lower_bound, curr, 1):
                if floors[i]:
                    return i
        else:
            curr += squirt
    
    return -1

#test
floors = [ False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True ]
print(floors)
print(len(floors))
print("True at 10: ", crystal_ball(floors))

false_floors = [ False, False, False, False, False, False, False, False, False, False ]
print(false_floors)
print(len(false_floors))
print("-1 : ", crystal_ball(false_floors))