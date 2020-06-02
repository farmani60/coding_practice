# Description:
# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

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

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

H = [21, 1, 45, 78, 3, 5]

tree = Tree(4)
tree.Insert(2)
tree.Insert(1)
tree.Insert(3)
tree.Insert(7)
tree.Insert(6)

tree.PrintTree()
