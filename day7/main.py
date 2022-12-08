file = open("input.txt", "r")

class files:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class directory:
    def __init__(self, name, parent_dir=None):
        self.name = name
        self.parent_dir = parent_dir
        self.sub_directories = []
        self.files = []
        self.dir_size = 0
    
    def getParentDir(self):
        return self.parent_dir
    
    def getFolderStructure(self):
        structure = []
        structure.extend(self.getSubDirectories())
        structure.extend(self.getFiles())
        return sorted(structure)
    
    def add_size(self, size):
        self.dir_size += size
        if self.parent_dir != None:
            self.parent_dir.add_size(size)
    
    def addFile(self, file):
        self.files.append(file)
        self.add_size(int(file.size))
    
    def addSubDirectory(self, directory):
        self.sub_directories.append(directory)
    
    def size(self):
        total_size = 0
        for f in self.files:
            total_size += int(f.size)
        for d in self.sub_directories:
            total_size += d.size()
        return total_size
    
    def check_sub_sizes(self, limit):
        temp = []
        for d in self.sub_directories:
            if d.dir_size > limit:
                temp.append(d.dir_size)
            temp2 = d.check_sub_sizes(limit)
            temp.extend(temp2)
        return temp
    
    def size_with_check(self, limit):
        total_size = 0
        for d in self.sub_directories:
            if d.size() < limit:
                total_size += d.size()
        return total_size

    def getSubDirectories(self):
        dirs = []
        for dir in self.sub_directories:
            dirs.append(dir.name)
        return dirs

    def getFiles(self):
        files = []
        for f in self.files:
            files.append(f.name)
        return files
    
    def searchForDir(self, query):
        for dir in self.sub_directories:
            if dir.name == query:
                return dir
        return None
    
    def searchForFile(self, query):
        for f in self.files:
            if f.name == query:
                return f
        return None

current_dir = None
top_dir = None
for line in file:
    command = line.strip().split(" ")

    # First command to check for -> cd
    if command[1] == "cd":
        # check if it's the first comand (no current directory)
        if current_dir is None:
            current_dir = directory(command[2])
            top_dir = current_dir
            continue # we've moved into this directory, and made it, so continue
        if command[2] == "..":
            parent_dir = current_dir.getParentDir()
            current_dir = parent_dir
            continue
        if command[2] == "/":
            current_dir = top_dir
            continue
        if current_dir.searchForDir(command[2]) is None:
            new_dir = directory(command[2], current_dir)
            current_dir.sub_directories.append(new_dir)
            current_dir = new_dir
            continue
        current_dir = current_dir.searchForDir(command[2])
        continue
    
    if command[0] == "dir":
        if current_dir.searchForDir(command[1]) is None:
            new_dir = directory(command[1], current_dir)
            continue
        continue

    if command[0] != "$":
        if current_dir.searchForFile(command[1]) is None:
            new_file = files(command[1], command[0])
            current_dir.addFile(new_file)
            continue

max_size = 70000000
update_size = 30000000
used_space = top_dir.dir_size
unused_space = max_size - used_space
needed_space = update_size - unused_space

print(f"unused space: {unused_space}")
print(needed_space)

totals = top_dir.check_sub_sizes(needed_space)
print(min(totals))