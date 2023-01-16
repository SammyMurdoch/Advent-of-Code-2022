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


def get_viewing_distance(tree_heights, i, direction):
    current_tree_index = i + direction
    tallest_tree = tree_heights[current_tree_index]
    viewing_distance = 0

    while tallest_tree < tree_heights[i] and (0 <= current_tree_index < len(tree_heights)-1):
        current_tree_index += direction

        tallest_tree = tree_heights[current_tree_index]
        viewing_distance += 1

    return viewing_distance


def get_viewing_distance_products(row):
    right_viewing_distances = np.array([get_viewing_distance(row, i, 1) for i in range(0, len(row)-1)] + [0])
    left_viewing_distances = np.array([0] + [get_viewing_distance(row, i, -1) for i in range(len(row)-1, 0, -1)])[::-1]

    return right_viewing_distances * left_viewing_distances


def get_scenic_scores(tree_heights):
    row_viewing_distance_products = np.array([get_viewing_distance_products(row) for row in tree_heights])
    column_viewing_distance_products = np.array([get_viewing_distance_products(row) for row in tree_heights.transpose()])

    return row_viewing_distance_products * column_viewing_distance_products


with open("PuzzleInput8") as f:
    grid_array = np.array([list(d) for d in f.read().split("\n")]).astype(int)
#
# horizontal_visible_trees = np.full(grid_array.shape, False)
# vertical_visible_trees = np.full(grid_array.shape, False)
#
# side_length = horizontal_visible_trees.shape[0]
#
# horizontal_visible_trees = update_visible_trees(grid_array, horizontal_visible_trees)
# vertical_visible_trees = update_visible_trees(grid_array.transpose(), vertical_visible_trees).transpose()
#
# visible_tree_count = np.logical_or(horizontal_visible_trees, vertical_visible_trees).sum()
#
# print(visible_tree_count)

# print(get_scenic_scores(grid_array))

print([get_viewing_distance([1, 4, 2, 5, 5, 4, 4, 4, 3, 2, 1, 6, 6, 6, 7, 4, 8], i, 1) for i in range(0, 16)])
print([get_viewing_distance([1, 4, 2, 5, 5, 4, 4, 4, 3, 2, 1, 6, 6, 6, 7, 4, 8], i, -1) for i in range(16, 0, -1)][::-1])

print(np.array([get_viewing_distance([3, 0, 3, 7, 3], i, 1) for i in range(0, 4)] + [0]))
print(np.array(np.array([0] + [get_viewing_distance([3, 0, 3, 7, 3], i, -1) for i in range(4, 0, -1)])))





