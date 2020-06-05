class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._add(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._add(val, node.right)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.val:
            return node
        elif (val < node.left) and (node.left is not None):
            self._find(val, node.left)
        elif (val > node.right) and (node.right is not None):
            self._find(val, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(node.val)
            self._printTree(node.right)

if __name__ == '__main__':
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.printTree()

