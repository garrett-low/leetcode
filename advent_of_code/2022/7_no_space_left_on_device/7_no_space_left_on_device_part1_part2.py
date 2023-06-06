# no space left on device - part 1 AND part 2
def no_space():
    file_system = FileSystem()
    print(file_system.root)
    
    curr_dir = file_system.root
    
    with open('input.txt', 'rt', encoding = 'utf-8') as file:
        for line in file:
            cmd = line.strip().split(' ')
            
            if cmd[0] == "$":              
                if cmd[1] == "cd":
                    target_dir = cmd[2]
                    if target_dir == "\\":
                        curr_dir = file_system.root
                    elif target_dir == "..":
                        curr_dir = curr_dir.parent
                    else:
                        # Assume the target cd must have already been seen with ls
                        for child_dir in curr_dir.child_dir_list:
                            if target_dir == child_dir.name:
                                curr_dir = child_dir
                                continue
                
                elif cmd[1] == "ls":
                    continue
            
            elif cmd[0] == "dir":
                curr_dir.add_dir(cmd[1], curr_dir)
            
            else:
                curr_dir.add_file(cmd[1], cmd[0])
    
    print(file_system)
    file_system.get_dir_size()
    file_system.get_dir_less_than(100_000)
    file_system.part_two(30_000_000)

class Directory:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.child_file_dict = {}
        self.child_dir_list = []
        
    def __str__(self):
        retval = f"Dir:\t{self.name}"
        if self.parent:
            retval += f"parent: {self.parent.name}"
        for file in self.child_file_dict:
            retval += f"\t\t{file}: {self.child_file_dict}\n"
        for dir_name in self.child_dir_list:
            retval += f"\t\t{dir_name}: dir\n"
        return retval
    
    def get_size(self):
        size = 0
        
        for child_file in self.child_file_dict:
            size += self.child_file_dict[child_file]
        
        for child_dir in self.child_dir_list:
            self.size_recurse(child_dir, size)
            
        return size
    
    def size_recurse(self, this_dir, size):
        if len(this_dir.child_file_dict) <= 0 and len(this_dir.child_dir_list) <= 0:
            return
        
        for child_file in this_dir.child_file_dict:
            size += this_dir.child_file_dict[child_file]
        
        for child_dir in this_dir.child_dir_list:
            self.size_recurse(child_dir, size)
    
    def add_file(self, name, size):
        self.child_file_dict[name] = size
    
    def add_dir(self, name, parent_dir):
        new_dir = Directory(name, parent_dir)
        self.child_dir_list.append(new_dir)

class FileSystem:
    def __init__(self):
        self.root = Directory('/', None)
        self.total_space = 70_000_000
        self.min_for_part_two = 70_000_000
    
    def __str__(self):
        retlist = []
        self.str_inner(self.root, retlist, 0)
        
        retval = ""
        for line in retlist:
            retval += f"{line}\n"
        return retval
    
    def str_inner(self, curr_dir, retlist, indent):
        if curr_dir == None:
            return
        retlist.append((indent * "\t") + f"Dir:\t{curr_dir.name}")
        if curr_dir.parent:
            retlist.append((indent * "\t") + f"Parent:\t{curr_dir.parent.name}")
        
        if len(curr_dir.child_dir_list) <= 0 and len(curr_dir.child_file_dict) <= 0:
            return
        
        for child_file in curr_dir.child_file_dict:
            retlist.append((indent * "\t") + f"File:\t{child_file}, {curr_dir.child_file_dict[child_file]}")
        
        for child_dir in curr_dir.child_dir_list:
            self.str_inner(child_dir, retlist, indent + 1)
            
    def get_dir_size(self):
        self.get_dir_size_inner(self.root)
    
    def get_dir_size_inner(self, curr_dir):
        size = 0
        if len(curr_dir.child_file_dict) <= 0 and len(curr_dir.child_dir_list) <= 0:
            return 0
        
        for child_file in curr_dir.child_file_dict:
            size += int(curr_dir.child_file_dict[child_file])
        
        for child_dir in curr_dir.child_dir_list:
            size += self.get_dir_size_inner(child_dir)
        
        print(f"Dir:\t{curr_dir.name}, {size}")
        
        return size
    
    def get_dir_less_than(self, target_size):
        dir_to_size_dict = {}
        
        self.get_dir_less_than_inner(self.root, target_size, dir_to_size_dict)
        
        total_size = 0
        for directory in dir_to_size_dict:
            print(f"{directory.name}: {dir_to_size_dict[directory]}")
            total_size += dir_to_size_dict[directory]
        
        print(f"Answer:\t{total_size}")
        return total_size
        
    def get_dir_less_than_inner(self, curr_dir, target_size, dir_to_size_dict):
        size = 0
        if len(curr_dir.child_file_dict) <= 0 and len(curr_dir.child_dir_list) <= 0:
            return 0
        
        for child_file in curr_dir.child_file_dict:
            size += int(curr_dir.child_file_dict[child_file])
        
        for child_dir in curr_dir.child_dir_list:
            size += self.get_dir_less_than_inner(child_dir, target_size, dir_to_size_dict)
        
        if size <= target_size:
            dir_to_size_dict[curr_dir] = size
        
        return size
    
    def part_two(self, target_size):
        space_used = self.get_root_size(self.root)
        space_free = self.total_space - space_used
        space_needed = target_size - space_free
        print(f"Space used: {space_used}, Space free: {space_free}, Space_needed: {space_needed}")
        self.get_size_dir_map(space_needed)
    
    def get_root_size(self, curr_dir):
        return self.get_dir_size_inner(curr_dir)
    
    def get_size_dir_map(self, at_least_size):
        size_to_dir_map = {}
        self.min_for_part_two = 70_000_000 # global variables are bad, whatever
        self.get_size_dir_map_inner(self.root, at_least_size, size_to_dir_map)
        
        print(f"Min size: {self.min_for_part_two}, {size_to_dir_map[self.min_for_part_two].name}")
        
    def get_size_dir_map_inner(self, curr_dir, at_least_size, size_to_dir_map):
        size = 0
        if len(curr_dir.child_file_dict) <= 0 and len(curr_dir.child_dir_list) <= 0:
            return 0
        
        for child_file in curr_dir.child_file_dict:
            size += int(curr_dir.child_file_dict[child_file])
        
        for child_dir in curr_dir.child_dir_list:
            size += self.get_size_dir_map_inner(child_dir, at_least_size, size_to_dir_map)
        
        if size >= at_least_size:
            size_to_dir_map[size] = curr_dir
            if size <= self.min_for_part_two:
                self.min_for_part_two = size
        
        return size

no_space()