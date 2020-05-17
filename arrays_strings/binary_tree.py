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
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left != None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right != None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if (self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if (val == node.v):
            return node
        elif (val < node.v and node.l != None):
            self._find(val, node.l)
        elif (val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node != None:
            self._printTree(node.left)
            print(str(node.val) + ' ')
            self._printTree((node.right))

class Node:
    def __init__(self, string, level):
        self.string = string
        self.level = level
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.tree = dict()

    def add_string(self, string, level=0):
        if self.root == None:
            self.root = Node(string, level)
            self.tree[level] = (string)
        else:
            add_string

    def add_string(self, string):
        if self.root == None:
            self.root = Node(string, 0)
            self.tree[0] = (string)
        else:
            self._add_string(string, self.root)

    def _add_string(self, string, node):
        if len(string) > 1:
            for i in range(1, len(string)):
                node.left = string[:i]
                node.right = string[i:]
            if len(self.root.left) > 1:

if __name__ == '__main__':
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.printTree()


