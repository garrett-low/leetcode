def twosum(arr, target):
    dict = {}
    for i in range(len(arr)):
        val = arr[i]
        dict[val] = i
    
    for i in range(len(arr)):
        val = arr[i]
        comp = target - val
        if comp in dict and i != dict[comp]:
            print(f"twosum:\t{i}, {dict[comp]}")
            return
        
    print("twosum:\tnot found!")
    return

a = [2,7,11,15]
b = 9
twosum(a, b)

c = [3,4,5,6,1,1]
d = 2
twosum(c, d)

e = [3,2,4]
f = 6
twosum(e, f)