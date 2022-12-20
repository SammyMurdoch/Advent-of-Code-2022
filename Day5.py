import re

with open("PuzzleInput5") as f:
    stack_rows, instructions = f.read().split("\n\n")

stack_rows = stack_rows.split("\n")

crate_indices = [match.start() for match in re.finditer(r'\b\d+\b', stack_rows[-1])]

formatted_stacks = []

for crate_index in crate_indices:
    formatted_stack = []

    for stack_row in stack_rows[:-1]:
        if len(stack_row) >= crate_index:
            if stack_row[crate_index] != " ":
                formatted_stack.append(stack_row[crate_index])

    formatted_stacks.append(formatted_stack)
    

formatted_stacks1 = formatted_stacks.copy()

instructions = [[int(s) for s in re.findall(r'\b\d+\b', instruction)] for instruction in instructions.split("\n")]

for instruction in instructions:
    for move_count in range(instruction[0]):
        formatted_stacks1[instruction[2]-1] = formatted_stacks1[instruction[1]-1][0:1] + formatted_stacks1[instruction[2]-1]
        formatted_stacks1[instruction[1]-1] = formatted_stacks1[instruction[1]-1][1:]

plan_view1 = "".join([formatted_stack[0] for formatted_stack in formatted_stacks1])

print(plan_view1)

formatted_stacks2 = formatted_stacks.copy()

for instruction in instructions:
    formatted_stacks2[instruction[2]-1] = formatted_stacks2[instruction[1]-1][0:instruction[0]] + formatted_stacks2[instruction[2]-1]
    formatted_stacks2[instruction[1]-1] = formatted_stacks2[instruction[1]-1][instruction[0]:]

plan_view2 = "".join([formatted_stack[0] for formatted_stack in formatted_stacks2])

print(plan_view2)






