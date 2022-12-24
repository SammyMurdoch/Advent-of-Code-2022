import re


class DirectoriesTree:
    def __init__(self, index):
        self.index = index
        self.parent_index = None
        self.child_indices = []
        self.name = None
        self.files = None
        self.directories = None
        self.total_size = None

    def get_directory_local_size(self):
        if not len(self.files):
            return 0

        return sum([int(re.findall(r'\d+', file)[0]) for file in self.files])

    def get_directory_total_size(self, tree_size, tree_dict):
        current_node = self.index

        while len(tree_dict[current_node].child_indices) != 0:
            current_node = tree_dict[current_node].child_indices[-1]

        included_nodes = list(range(tree_size))[self.index:current_node+1]

        return sum([tree_dict[node].get_directory_local_size() for node in included_nodes])


with open("PuzzleInput7") as f:
    lines = f.read()

directories = {}

for i, match in enumerate(re.finditer("\$ ls", lines)):
    directory_contents_start_index = match.end() + 1
    directory_contents_end_index = lines.find("$", directory_contents_start_index)

    directory_content = lines[directory_contents_start_index:directory_contents_end_index].split("\n")

    directory_content = list(filter(None, directory_content))

    directory_directories = list(filter(lambda d: "dir " in d, directory_content))
    directory_files = list(filter(lambda d: "dir " not in d, directory_content))

    directories_left = lines[:directory_contents_end_index].count("$ cd ..")

    directories[i] = DirectoriesTree(i)

    directories[i].parent_index = i - directories_left - 1

    if directories[i].parent_index != -1:
        directories[directories[i].parent_index].child_indices.append(i)

    directories[i].directories = directory_directories
    directories[i].files = directory_files
    directories[i].name = lines[lines.rfind("$", 0, match.start())+5:match.start()-1]

total = 0

for directory in directories.values():
    directory_total_size = directory.get_directory_total_size(len(directories), directories)
    print(directory_total_size, directory.index, directory_content)
    if directory_total_size <= 100000:
        total += directory_total_size

print(total)






