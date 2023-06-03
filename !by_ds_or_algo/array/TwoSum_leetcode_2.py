def twosum(array, target):
    comp_set = set()
    for i in range(len(array)):
        val = array[i]
        complement = target - array[i]
        if complement in comp_set:
            return True
        comp_set.add(val)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(twosum(arr, 5))

if __name__ == "__main__":
    main()