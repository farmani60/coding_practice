class Node:
    def __init__(self, string):
        self.left = None
        self.right = None
        self.string = string

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, string):
        self.root = Node(string)
        self._add(self.root)

    def _add(self, node):
        if len(node.string) > 1:
            if node.left == None:
                node.left = Node(node.string[:1])
            if node.right == None:
                node.right = Node(node.string[1:])
                self._add(node.right)


if __name__ == "__main__":
    tree = Tree()
    t

