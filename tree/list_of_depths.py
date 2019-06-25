from bintree_class import TreeNode


def list_of_depths(root):
    if not root:
        return None
    depths = []
    q = [root]
    while q:
        parents = q
        depths.append(q)
        q = []
        for parent in parents:
            if parent.left:
                q.append(parent.left)
            if parent.right:
                q.append(parent.right)
    return depths


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
depths = list_of_depths(root)
for depth, list_nodes in enumerate(depths):
    print('Depth', depth, end=': ')
    for n in list_nodes:
        print(n.val, end=' -> ')
    print('end')
