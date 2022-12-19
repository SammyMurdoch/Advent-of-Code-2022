import heapq

with open("Elf food") as f:
    lines = f.read()

elf_list = lines.split("\n\n")
elf_calorie_list = []

for elf in elf_list:
    elf_calorie_list.append(sum([int(calorie_count) for calorie_count in elf.split("\n")]))

print(max(elf_calorie_list))

print(sum(heapq.nlargest(3, elf_calorie_list)))

