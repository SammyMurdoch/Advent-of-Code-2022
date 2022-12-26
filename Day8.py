import numpy as np


def find_visible_tree(tree_array, observation_direction, row_index, visible_trees):
    if observation_direction == "left":
        observed_tree_index = np.argmax(tree_array)
        visible_trees[row_index, observed_tree_index] = True

        return tree_array[:observed_tree_index], visible_trees

    local_observed_tree_index = np.argmax(np.flip(tree_array))
    observed_tree_index = side_length - local_observed_tree_index - 1

    visible_trees[row_index, observed_tree_index] = True

    return tree_array[len(tree_array)-local_observed_tree_index:], visible_trees


def update_visible_trees(tree_heights, visible_trees):
    for i, row in enumerate(tree_heights):
        left_array, visible_trees = find_visible_tree(row, "left", i, visible_trees)
        right_array, visible_trees = find_visible_tree(row, "right", i, visible_trees)

        while len(left_array) != 0:
            left_array, visible_trees = find_visible_tree(left_array, "left", i, visible_trees)

        while len(right_array) != 0:
            right_array, visible_trees = find_visible_tree(right_array, "right", i, visible_trees)

    return visible_trees


with open("PuzzleInput8") as f:
    grid_array = np.array([list(d) for d in f.read().split("\n")]).astype(int)

horizontal_visible_trees = np.full(grid_array.shape, False)
vertical_visible_trees = np.full(grid_array.shape, False)

side_length = horizontal_visible_trees.shape[0]

horizontal_visible_trees = update_visible_trees(grid_array, horizontal_visible_trees)
vertical_visible_trees = update_visible_trees(grid_array.transpose(), vertical_visible_trees).transpose()

visible_tree_count = np.logical_or(horizontal_visible_trees, vertical_visible_trees).sum()

print(visible_tree_count)
