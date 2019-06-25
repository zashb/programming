from bintree_class import TreeNode


class Height:
    def __init__(self):
        self.height = 0


def is_balanced_efficient(root, height2):
    if root is None:
        return True
    lh = Height()
    rh = Height()
    lb = is_balanced_efficient(root.left, lh)
    rb = is_balanced_efficient(root.right, rh)
    height2.height = max(lh.height, rh.height) + 1
    if abs(lh.height - rh.height) <= 1:
        return lb and rb
    return False


def get_height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        get_height(root.right) + 1
    if root.right is None:
        get_height(root.left) + 1
    return max(get_height(root.left), get_height(root.right)) + 1


def is_balanced(root):
    if not root:
        return True
    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(8)
baseline_time = 0

actual = is_balanced(root)
print("is_balanced : {}".format(actual))

height2 = Height()
actual = is_balanced_efficient(root, height2)
print("is_balanced_efficient : {}".format(actual))
