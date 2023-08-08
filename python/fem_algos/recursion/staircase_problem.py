# Common-Sense DSA: Chapter 11
# Count number of paths to ascend staircase
# can take 1, 2, or 3 steps at a time

def stair(num_steps):
    num_paths = stair_inner(num_steps)
    print(num_paths)

def stair_inner(num_steps):
    if num_steps <= 0:
        return 0
    if num_steps == 1:
        return 1
    if num_steps == 2:
        return 2
    if num_steps == 3:
        return 4
    
    return stair_inner(num_steps - 1) + stair_inner(num_steps - 2) + stair_inner(num_steps - 3)

# stair(4)
# stair(5)

def stair_paths(num_steps):
    paths = []
    curr_path = []
    stair_paths_inner(num_steps, paths, curr_path)
    for path in paths:
        print(path)

def stair_paths_inner(num_steps, paths, curr_path):
    if num_steps <= 0:
        paths.append(curr_path)
        return
    if num_steps == 1:
        curr_path.append(1)
        paths.append(curr_path)
        return
    if num_steps == 2:
        path1 = curr_path.copy()
        path1.append(1)
        stair_paths_inner(num_steps - 1, paths, path1)
        path2 = curr_path.copy()
        path2.append(2)
        stair_paths_inner(num_steps - 2, paths, path2)
        return
    
    path1 = curr_path.copy()
    path1.append(1)
    stair_paths_inner(num_steps - 1, paths, path1)
    path2 = curr_path.copy()
    path2.append(2)
    stair_paths_inner(num_steps - 2, paths, path2)
    path3 = curr_path.copy()
    path3.append(3)
    stair_paths_inner(num_steps - 3, paths, path3)

# stair_paths(4)
stair_paths(5)