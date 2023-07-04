from collections import deque
import sys

def sweep(filename):
    with open(filename, 'rt', encoding='utf-8') as file:
        window = deque()
        window_sums = deque()
        num_increase = 0
        
        for line in file:
            curr = int(line)
            window.append(curr)
            
            if len(window) == 3:
                threesum = 0
                for num in window:
                    threesum += num
                window_sums.append(threesum)
                window.popleft()
            
            if len(window_sums) != 2:
                continue

            prev = window_sums.popleft()
            curr = window_sums[0]
#            print(f"prev: {prev}, curr: {curr}")
            if curr > prev:
                num_increase += 1
    
#     curr = sys.maxsize
#     prev = sys.maxsize
#     num_increase = 0
#     for sums in window_sums
#         curr = sums
#         if prev != sys.maxsize and curr > prev:
#             num_increase += 1
#         prev = curr
    
    print(num_increase)
    return

sweep('sample.txt')
sweep('input.txt')