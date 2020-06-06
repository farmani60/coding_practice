
class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.depth = None

class Tree:
    def __init__(self, tree):
        self.tree = tree
        self.mNodes = []
        self.maxDepth = 0

    def buildTree(self):
        root = Node()
        root.value = 0
        root.depth = 1
        self.maxDepth = root.depth
        self.mNodes.append((0, root))
        for i in range(1, len(self.tree)+1):
            node = self.mNodes[i-1][1]
            node.value = i
            leftPos = self.tree[i-1][0]
            rightPos = self.tree[i-1][1]
            if leftPos != -1:
                self.addLeftNode(node, leftPos)
            if rightPos != -1:
                self.addRightNode(node, rightPos)
            node.left = leftPos
            node.right = rightPos

    def addLeftNode(self, node, leftPos):
        left = Node()
        left.depth = node.depth + 1
        if left.depth > self.maxDepth:
            self.maxDepth = left.depth
        self.mNodes.append((leftPos-1, left))

    def addRightNode(self, node, rightPos):
        right = Node()
        right.depth = node.depth + 1
        if right.depth > self.maxDepth:
            self.maxDepth = right.depth
        self.mNodes.append((rightPos-1, right))

    def swapNodes(self, k):
        for i in range(k, self.maxDepth, k):
            for node in self.mNodes:
                node = node[1]
                if node.depth == i:
                    temp = node.left
                    node.left = node.right
                    node.right = temp

    def printInOrder(self, node):
        if (node is None) or (node.value == -1):
            return
        if node.left != -1:
            self.printInOrder(self.mNodes[node.left-1][1])
        print(node.value)
        if node.right != -1:
            self.printInOrder(self.mNodes[node.right-1][1])

T = [(2, 3), (-1, 4), (-1, 5), (-1, -1), (-1, -1)]
tree = Tree(T)
tree.buildTree()
tree.printInOrder(tree.mNodes[0][1])
print('****')
tree.swapNodes(2)
tree.printInOrder(tree.mNodes[0][1])
