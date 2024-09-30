def quick_sort(arr):
   return qs_inner(arr, 0, len(arr) - 1)

def qs_inner(arr, low, high):
    if low >= high or low < 0:
        return
    
    

