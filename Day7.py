import re

with open("PuzzleInput7") as f:
    lines = f.read()

#print(lines)

directories = {}
directory_contents = []
directory_names = []

for match in re.finditer("\$ ls", lines):
    directory_contents_start_index = match.end() + 1

    directory_content = lines[directory_contents_start_index:lines.find("$", directory_contents_start_index)].split("\n")
    directory_content = list(filter(None, directory_content))

    directory_contents.append(directory_content)
    directory_names.append(lines[lines.rfind("$", 0, match.start())+5:match.start()-1])

print(directory_contents)
print(directory_names)

