"""
Description:
https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

The height of a binary tree is the number of edges between the tree's root and
its furthest leaf. For example, the following binary tree is of height 3:

       4
     /   \
    2     5
  /      / \
 1      4   6
             \
              7

"""
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def Insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.Insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.Insert(data)
        else:
            self.data = data

def getHeight(root):
    if root:
        return 1 + max(getHeight(root.left), getHeight(root.right))
    else:
        return -1

root = Tree(3)
root.Insert(2)
root.Insert(5)
root.Insert(1)
root.Insert(4)
root.Insert(6)
root.Insert(7)

print(getHeight(root))