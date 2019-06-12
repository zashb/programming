from tree.bintree_class import TreeNode


def get_io_successor(root, target):
    candidate = None
    while root:
        if root.val == target:
            if root.right is not None:
                candidate = root.right
                while candidate.left is not None:
                    candidate = candidate.left
            root = None
        elif target < root.val:
            candidate = root
            root = root.left
        else:
            root = root.right
    return candidate.val


def get_inorder(root):
    if root is None:
        return None
    get_inorder(root.left)
    print(root.val)
    get_inorder(root.right)


def insert(root, val):
    if root is None:
        root = TreeNode(val)
    else:
        if val > root.val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                insert(root.right, val)
        else:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                insert(root.left, val)


root = TreeNode(20)
insert(root, 8)
insert(root, 22)
insert(root, 4)
insert(root, 12)
insert(root, 10)
insert(root, 14)
get_inorder(root)
expected = 20
actual = get_io_successor(root, 14)
print(expected == actual)
