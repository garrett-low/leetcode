def index_of(arr):
    bs(arr, 0, len(arr) - 1)
    return 0

def bs(arr, lo, hi):
    if lo >= hi:
        return None