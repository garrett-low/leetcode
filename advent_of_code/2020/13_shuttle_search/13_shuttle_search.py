import sys

def shuttle_search_p1(filename):
    # print(939//59)
    # print(59*15)
    # print(59*16)
    earliest_time = 0
    bus_id_ary = []
    with open(filename, 'rt', encoding='utf-8') as file:
        earliest_time = int(file.readline().strip())
        bus_string = file.readline().strip()
        # bus_id_ary = [int(x) for x in bus_string.split(',')]
        bus_id_ary = bus_string.split(',')
    
    min_wait = sys.maxsize
    min_bus_id = None
    for bus_id in bus_id_ary:
        if bus_id == 'x':
            continue
        
        bus_id = int(bus_id)
        interval_before_earliest = earliest_time // bus_id
        next_bus_time = bus_id * (interval_before_earliest + 1)
        # print("next_bus_time: ", next_bus_time)
        
        test_wait = next_bus_time - earliest_time
        if test_wait < min_wait:
            min_wait = test_wait
            min_bus_id = bus_id
    
    # print(earliest_time)
    # print(bus_id_ary)
    print(filename)
    print("  min_wait: ", min_wait)
    print("  P1: ", min_wait * min_bus_id)

shuttle_search_p1('sample.txt')
shuttle_search_p1('input.txt')