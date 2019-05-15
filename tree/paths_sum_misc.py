from tree.tree_class import TreeNode


def pathSum(root, sum):
    return helper(root, sum, [])


def helper(root, sum, visited):
    if not root:
        return 0
    visited = visited + [root.val]
    found, currentsum = 0, 0
    for n in visited[::-1]:
        currentsum += n
        if currentsum == sum:
            found += 1
    return found + helper(root.left, sum, visited) + helper(root.right, sum, visited)


def count_subtrees_with_sum(node, target_sum, running_sum, path_count):
    if node is None:
        return 0
    running_sum += node.val
    _sum = running_sum - target_sum
    total_paths = path_count.get(_sum, 0)
    if running_sum == target_sum:
        total_paths += 1
    path_count = increment_path_count(path_count, running_sum, 1)
    total_paths += count_subtrees_with_sum(node.left, target_sum, running_sum, path_count)
    total_paths += count_subtrees_with_sum(node.right, target_sum, running_sum, path_count)
    path_count = increment_path_count(path_count, running_sum, -1)
    return total_paths


def increment_path_count(path_count, key, delta):
    new_count = path_count.get(key, 0) + delta
    if new_count == 0:
        path_count.pop(key, None)
    else:
        path_count[key] = new_count
    return path_count


root = TreeNode(5)
root.left = TreeNode(-10)
root.right = TreeNode(3)
root.left.left = TreeNode(9)
root.left.right = TreeNode(8)
root.right.left = TreeNode(-4)
root.right.right = TreeNode(7)
target_sum = 7
actual = pathSum(root, target_sum)
print("count_of_subtrees_with_sum {} : {}".format(target_sum, actual))
actual = count_subtrees_with_sum(root, target_sum, 0, {})
print("count_of_subtrees_with_sum {} : {}".format(target_sum, actual))
