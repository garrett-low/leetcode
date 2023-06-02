# 06/01/2023

def qs(arr):
    qsinner(arr, 0, len(arr) - 1)
    
    return arr

def qsinner(arr, lo, hi):
    if lo >= hi or lo < 0:
        return
    
    p = partition(arr, lo, hi)
    
    qsinner(arr, p + 1, hi)
    qsinner(arr, lo, p - 1)
    
def partition(arr, lo, hi):
    p = arr[hi]
    pi = lo - 1
    for i in range(lo, hi):
        if arr[i] < p:
            pi += 1
            temp = arr[i]
            arr[i] = arr[pi]
            arr[pi] = temp
    pi += 1
    arr[hi] = arr[pi]
    arr[pi] = p
    
    return pi

def main():
    array = [4, 3, 1, 7, 6, 2, 5]
    print(qs(array))
    
    array2 = [420, 69, 42069, 1, 55, 123, 999]
    print(qs(array2))
    
if __name__ == "__main__":
    main()