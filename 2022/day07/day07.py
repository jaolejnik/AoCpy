import pathlib
from dataclasses import dataclass

@dataclass 
class Directory:
    name: str
    parent: 'Directory'
    children: list

    def get_size(self):
        return sum([child.get_size() for child in self.children])
    
    def __str__(self):
        return f"- {self.name} (dir, size={self.get_size()})"

@dataclass
class File:
    name: str
    parent: 'Directory'
    size: int

    def get_size(self):
        return self.size

    def __str__(self):
        return f"- {self.name} (file, size={self.size})"


WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
with open(WORKDIR + "/input") as f:
    terminal_output = f.read().splitlines()


def recreate_dir_structure(root, term_out):
    current_dir = root 

    for line in term_out:
        if line.startswith("$"):
            command, *arg = line.split()[1:]

            if command == "cd":
                if arg[0] == ".." and current_dir.parent:
                    current_dir = current_dir.parent
                else:
                    for child in current_dir.children:
                        if type(child) == Directory and child.name == arg[0]:
                            current_dir = child
                            break
            else: # ls
                continue
        else:
            if line.startswith("dir"):
                dir_name = line.split()[1]
                current_dir.children.append(Directory(dir_name, current_dir, []))
            else:
                size, file_name = line.split()
                current_dir.children.append(File(file_name, current_dir, int(size)))


def print_dir_structure(root, depth):
    print(' ' * depth, root)
    
    depth += 1

    for child in root.children:
        if (type(child) == Directory):
            print_dir_structure(child, depth)
        else:
            print(' ' * depth , child)
            

def find_dir_leq_sizes(root, dir_sizes, leq_size):
    for child in root.children:
        if (type(child) != Directory):
            continue 

        size = child.get_size()
        if size <= leq_size :
            dir_sizes.append(size)

        find_dir_leq_sizes(child, dir_sizes, leq_size)
           


root = Directory('/', None, [])
recreate_dir_structure(root, terminal_output[1:])
# print_dir_structure(root, 0)

dir_sizes = []
find_dir_leq_sizes(root, dir_sizes, 100000)
print("Part 1:", sum(dir_sizes))

# ----------- PART 2 -------------------
TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000

def find_delete_candidates_sizes(root, dir_sizes, missing_space):
    for child in root.children:
        if (type(child) != Directory):
            continue

        size = child.get_size()
        if size >= missing_space:
            dir_sizes.append(size)

        find_delete_candidates_sizes(child, dir_sizes, missing_space)    
    

dir_sizes = []
missing_space = REQUIRED_SPACE - (TOTAL_SPACE - root.get_size())  
find_delete_candidates_sizes(root, dir_sizes, missing_space)
print("Part 2:", min(dir_sizes))
