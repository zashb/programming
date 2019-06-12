from collections import deque


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


def level_order(root):
    if not root:
        return root
    queue = deque()
    queue.append(root)
    while queue:
        next = queue.popleft()
        print(next.val)
        if next.left:
            queue.append(next.left)
        if next.right:
            queue.append(next.right)