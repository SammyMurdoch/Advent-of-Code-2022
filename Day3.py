def get_priority(letter):
    decimal_ascii_value = ord(letter)

    if 65 <= decimal_ascii_value <= 90:
        return decimal_ascii_value - 38

    else:
        return decimal_ascii_value - 96


with open("Rucksack Contents") as f:
    rucksacks = f.read().split("\n")


compartment_list = [[rucksack_contents[:int(len(rucksack_contents)/2)],
                     rucksack_contents[int(len(rucksack_contents)/2):]] for rucksack_contents in rucksacks]

priority_sum = 0

for rucksack in compartment_list:
    for letter in rucksack[0]:
        if letter in rucksack[1]:
            priority_sum += get_priority(letter)
            break

print(priority_sum)

# PART 2

priority_sum2 = 0

for group in range(int(len(rucksacks)/3)):
    for letter in rucksacks[group*3]:
        if letter in rucksacks[group*3+1]:
            if letter in rucksacks[group*3+2]:
                priority_sum2 += get_priority(letter)
                break

print(priority_sum2)
