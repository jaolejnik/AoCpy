import pathlib
import numpy as np

WORKDIR = str(pathlib.Path(__file__).parent.resolve())

# ----------- PART 1 -------------------
with open(WORKDIR + "/input") as f:
    tree_mat = np.array(np.mat([list(map(int, line.strip())) for line in f]))


def is_tree_visible(tree_mat, x, y):
    if is_tree_on_edge(tree_mat, x, y):
        return True

    current_tree = tree_mat[y, x]
    for trees in get_surrounding_trees(tree_mat, x, y):
        geq_trees = trees[trees >= current_tree]
        if len(geq_trees) == 0:
            return True

    return False


def is_tree_on_edge(tree_mat, x, y):
    max_x, max_y = tree_mat.shape
    max_x -= 1
    max_y -= 1

    return x == 0 or x == max_x or y == 0 or y == max_y


def get_surrounding_trees(tree_mat, x, y):
    return [
        tree_mat[y, :x],  # left of the tree
        tree_mat[:y, x],  # above the tree
        tree_mat[y, x + 1 :],  # right of the tree
        tree_mat[y + 1 :, x],  # below the tree
    ]


X, Y = tree_mat.shape
print(
    "Part 1:",
    sum([is_tree_visible(tree_mat, x, y) for y in range(Y) for x in range(X)]),
)

# ----------- PART 2 -------------------
def calculate_scenic_score(tree_mat, x, y):
    if is_tree_on_edge(tree_mat, x, y):
        return 0

    directional_scores = []
    current_tree = tree_mat[y, x]
    for i, trees in enumerate(get_surrounding_trees(tree_mat, x, y)):
        if i < 2:
            trees = trees[::-1]

        for distance, tree in enumerate(trees, 1):
            if tree >= current_tree:
                directional_scores.append(distance)
                break

        if len(directional_scores) < i + 1:
            directional_scores.append(distance)

    return np.prod(directional_scores)


print(
    "Part 2:",
    max([calculate_scenic_score(tree_mat, x, y) for y in range(Y) for x in range(X)]),
)
