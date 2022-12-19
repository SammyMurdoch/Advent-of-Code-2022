import re

with open('Assignment Pairs') as f:
    assignment_pairs = f.readlines()

assignment_pairs = [[int(s) for s in re.findall(r'\b\d+\b', pair)] for pair in assignment_pairs]

contain_count = 0

for pair in assignment_pairs:
    if (pair[0] - pair[2]) * (pair[1] - pair[3]) <= 0:
        contain_count += 1

print(contain_count)

# PART 2

