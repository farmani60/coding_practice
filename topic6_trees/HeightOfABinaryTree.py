"""
Description:
https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

The height of a binary tree is the number of edges between the tree's root and
its furthest leaf. For example, the following binary tree is of height 2:

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


def getHeight(tree):
    pass

tree = Tree(3)
tree.Insert(2)
tree.Insert(5)
tree.Insert(1)
tree.Insert(4)
tree.Insert(6)
tree.Insert(7)