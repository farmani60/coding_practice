"""
Description:
https://www.hackerrank.com/challenges/swap-nodes/problem?h_r=internal-search

"""
class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.depth = None

class Tree:

    def __init__(self, tree):
        self.mNodes = []
        self.maxDepth = 0
        self.tree = tree

    def builTree(self, numberNodes):
        root = Node()
        root.dept = 1
        self.mNodes.append((0, root))
        for i in range(1, numberNodes+1):
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

    def addrightNode(self, node, rightPos):
        right = Node()
        right.depth = node.depth + 1
        if right.depth > self.maxDepth:
            self.maxDepth = right.depth
        self.mNodes.append((rightPos-1, right))


T = [(2, 3), (-1, -1), (-1, -1)]

tree = Tree(T)