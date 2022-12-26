import numpy as np


def find_visible_tree(tree_array, observation_direction, row_index):
    if observation_direction == "left":
        observed_tree_index = np.argmax(tree_array)
        visible_trees[row_index, observed_tree_index] = True

        return tree_array[:observed_tree_index]

    local_observed_tree_index = np.argmax(np.flip(tree_array))
    observed_tree_index = side_length - local_observed_tree_index - 1

    visible_trees[row_index, observed_tree_index] = True

    return tree_array[len(tree_array)-local_observed_tree_index:]


def update_visible_trees(tree_heights):
    for i, row in enumerate(tree_heights):
        left_array = find_visible_tree(row, "left", i)
        right_array = find_visible_tree(row, "right", i)

        while len(left_array) != 0:
            left_array = find_visible_tree(left_array, "left", i)

        while len(right_array) != 0:
            right_array = find_visible_tree(right_array, "right", i)


with open("PuzzleInput8") as f:
    grid_array = np.array([list(d) for d in f.read().split("\n")]).astype(int)

visible_trees = np.full(grid_array.shape, False)
side_length = visible_trees.shape[0]

# update_visible_trees(grid_array)
# print(visible_trees)
update_visible_trees(grid_array)

print(visible_trees)



# # #TODO TREES OF HEIGHT 0?
# #
# # import numpy as np
# # hi = np.array([1, 3, 2, 2, 3])
# #
# # yo = np.argmax(np.flip(hi))
# # yo2 = np.argmax(hi)
# #
# # print(hi, yo, yo2)
