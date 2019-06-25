from bintree_class import TreeNode


def get_min_tree(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = get_min_tree(arr[:mid])
    root.right = get_min_tree(arr[mid + 1:])
    return root


def insert(root, new_node):
    if root is None:
        root = new_node
    else:
        if new_node.val > root.val:
            if root.right is None:
                root.right = new_node
            else:
                insert(root.right, new_node)
        else:
            if root.left is None:
                root.left = new_node
            else:
                insert(root.left, new_node)


def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val, end=",")
    inorder(node.right)


arr = [10, 20, 3, 4, 5, 6, 7]
r = TreeNode(arr[0])
for i in arr[1:]:
    insert(r, TreeNode(i))
print("inorder traversal of BST :")
inorder(r)
root = get_min_tree(arr)
print("inorder traversal of BST :")
inorder(root)
