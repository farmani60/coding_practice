"""
Description:
https://www.hackerrank.com/challenges/tree-inorder-traversal/problem?h_r=internal-search
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

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self.data, end=" ")
        if self.right:
            self.right.printInOrder()

def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.data, end=" ")
        inOrderTraversal(root.right)

tree = Tree(5)
values = [2,6,4,1,3]
for v in values: tree.insert(v)
# tree.printInOrder()

inOrderTraversal(tree)