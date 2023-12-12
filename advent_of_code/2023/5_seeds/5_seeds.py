def seeds(filename):
    # array of 3 number tuples
    seeds = []
    maps = []
    seed_soil = []
    soil_fert = []
    fert_water = []
    water_light = []
    light_temp = []
    temp_humid = []
    humid_loc = []
    maps_i = 0
    with open(filename, 'rt') as file:
        seed_string = file.readline()
        seeds = [int(x) for x in seed_string.strip().split(':')[1].split()]
        
        contents = file.read()
        contents = contents.strip()
        contents_split = contents.split("\n\n")
        # print(contents_split)
        for map_string in contents_split:
            maps.append([])
            colon_split = map_string.split(':')
            # print(colon_split)
            map_vals = colon_split[1].strip().split("\n")
            for map_val in map_vals:
                map_val = map_val.strip().split()
                map_tuple = (int(map_val[0]), int(map_val[1]), int(map_val[2]))
                # print(map_tuple)
                maps[maps_i].append(map_tuple)
            
            maps_i += 1
            
    # print(seeds)
    # print(maps)
    
    source_starts_ordered = [] # list of ordered list of source starts
    source_arr_of_dicts = [] # list of dicts src start -> (range length, dest start)
    
    # Structure data for P1 solving
    # Yes, this could have be done during the file reading
    # But maybe it will change for P2
    idx = 0
    for map_tuples in maps:
        source_starts_ordered.append([])
        source_arr_of_dicts.append({})
        for map_tuple in map_tuples:
           src_start = map_tuple[1]
           range_len = map_tuple[2]
           dest_start = map_tuple[0]
           
           source_starts_ordered[idx].append(src_start)
           source_arr_of_dicts[idx][src_start] = (range_len, dest_start)
           
        idx += 1
    
    for source_start_arr in source_starts_ordered:
        q_sort(source_start_arr)
        
    # process(79, source_starts_ordered, source_arr_of_dicts)
    location_arr = []
    for seed in seeds:
        location_num = process(seed, source_starts_ordered, source_arr_of_dicts)
        # print(location_num)
        location_arr.append(location_num)
    
    q_sort(location_arr)
    print(location_arr[0])
    
def process(seed, source_starts_ordered, source_arr_of_dicts):
    curr_val = seed
    map_i = 0
    
    for map_i in range(len(source_starts_ordered)):
        # print(f"{map_i}:  {curr_val}")
        source_start_arr = source_starts_ordered[map_i]
        source_dict = source_arr_of_dicts[map_i]
        
        lower_bound_source = None
        for source_start in source_start_arr:
            if curr_val < source_start:
                break
            lower_bound_source = source_start
        
        if lower_bound_source == None:
            continue # aren't mapped correspond to same destination number
        
        range_len = source_dict[lower_bound_source][0]
        dest_start = source_dict[lower_bound_source][1]
                
        # print(f"  {curr_val}, {lower_bound_source}, {range_len}, {dest_start}")
        
        upper_bound_source = lower_bound_source + range_len
        
        if curr_val > upper_bound_source:
            continue # aren't mapped correspond to same destination number
        
        # translate to destionation number
        diff = dest_start - lower_bound_source
        curr_val += diff
    
    return curr_val
    
def q_sort(arr):
    quick_sort(arr, 0, len(arr) - 1)
    # print(arr)

def quick_sort(arr, lo, hi):
    if lo < 0 or lo >= hi:
        return
    pivot_i = partition(arr, lo, hi)
    
    quick_sort(arr, lo, pivot_i - 1)
    quick_sort(arr, pivot_i + 1, hi)
    
def partition(arr, lo, hi):
    pivot_val = arr[hi]
    
    pivot_i = lo - 1
    for i in range(lo, hi):
        if arr[i] < pivot_val:
            pivot_i += 1
            arr[i], arr[pivot_i] = arr[pivot_i], arr[i]
    
    pivot_i += 1
    arr[hi], arr[pivot_i] = arr[pivot_i], pivot_val
    
    return pivot_i

seeds('sample.txt')
seeds('input.txt') # 662197086

# q_sort([69, 350, 420, 10, 9, 5, 8])
# q_sort([69, 350, 420, 10, 5, 8])