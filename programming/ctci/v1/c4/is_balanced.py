import time
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
    return max(get_height(root.left), get_height(root.right)) + 1


def is_balanced(root):
    if not root:
        return True
    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


class Test(unittest.TestCase):
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)
    baseline_time = 0

    def test_is_balanced(self):
        start = time.time()
        actual = is_balanced(self.root)
        end = time.time()
        print("is_balanced : {}".format(actual))
        self.baseline_time = end - start
        print("Baseline time : {}".format(self.baseline_time))

    def test_is_balanced_efficient(self):
        start = time.time()
        height2 = Height()
        actual = is_balanced_efficient(self.root, height2)
        end = time.time()
        print("is_balanced_efficient : {}".format(actual))
        efficient = end - start
        print("is it more efficient : {}".format(self.baseline_time > efficient))
