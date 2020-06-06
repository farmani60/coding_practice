
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.data, end=" ")
        if root.left:
            preOrder(root.left)
        if root.right:
            preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")