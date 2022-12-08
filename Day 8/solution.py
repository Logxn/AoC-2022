playing_grid = []


def init():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            playing_grid.append(list(line.strip()))


# This function is correct =)
# 392 Trees
def get_edge_trees():
    return (2 * len(playing_grid[0])) + (2 * (len(playing_grid) - 2))


# The visibility is meassured without the edges
# A tree is visible if all trees until the edge is smaller in height than the current tree
def is_visible_top(depth, tree_index, tree):
    score = 0
    for new_depth in range(depth-1, -1, -1):
        new_tree = int(playing_grid[new_depth][tree_index])

        if new_tree >= tree:
            return score + 1
        else:
            score += 1

    return score


def is_visible_bottom(depth, tree_index, tree):
    score = 0
    for new_depth in range(depth + 1, len(playing_grid)):
        new_tree = int(playing_grid[new_depth][tree_index])

        if new_tree >= tree:
            return score + 1
        else:
            score += 1

    return score


def is_visible_right(depth, tree_index, tree):
    score = 0
    for new_tree_index in range(tree_index + 1, len(playing_grid[depth])):
        new_tree = int(playing_grid[depth][new_tree_index])

        if new_tree >= tree:
            return score + 1
        else:
            score += 1

    return score


def is_visible_left(depth, tree_index, tree):
    score = 0
    for new_tree_index in range(tree_index - 1, -1, -1):
        new_tree = int(playing_grid[depth][new_tree_index])

        if new_tree >= tree:
            return score + 1
        else:
            score += 1

    return score


def main():
    global playing_grid

    init()
    edge_trees = get_edge_trees()
    visible_trees = []

    max_score = 0

    for depth in range(1, len(playing_grid) - 1):
        for tree_index in range(1, len(playing_grid[depth]) - 1):
            current_tree = int(playing_grid[depth][tree_index])

            visible_top = is_visible_top(depth, tree_index, current_tree)
            visible_bottom = is_visible_bottom(depth, tree_index, current_tree)
            visible_left = is_visible_left(depth, tree_index, current_tree)
            visible_right = is_visible_right(depth, tree_index, current_tree)

            tree_score = visible_top * visible_bottom * visible_left * visible_right

            if tree_score > max_score:
                max_score = tree_score

    # solution = len(visible_trees) + edge_trees
    print(max_score)  # Current: 585 (too low)


main()
