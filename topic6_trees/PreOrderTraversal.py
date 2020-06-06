"""
Description:
https://www.hackerrank.com/challenges/tree-preorder-traversal/problem?h_r=internal-search
"""

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, newdata):
        if self.data:
            if newdata < self.data:
                if self.left is None:
                    self.left = Tree(newdata)
                else:
                    self.left.insert(newdata)
            else:
                if self.right is None:
                    self.right = Tree(newdata)
                else:
                    self.right.insert(newdata)
        else:
            self.data = newdata

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

tree = Tree(1)
values = [2, 5, 3, 4, 6]
for v in values: tree.insert(v)

print("In order")
inOrder(tree)
print("\n Pre order")
preOrder(tree)