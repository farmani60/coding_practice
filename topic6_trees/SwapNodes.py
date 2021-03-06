"""
Description:
https://www.hackerrank.com/challenges/swap-nodes/problem?h_r=internal-search

<<<<<<< HEAD
A binary tree is a tree which is characterized by any one of the following
properties:

* It can be an empty (null).
* It contains a root node and two subtrees, left subtree and right subtree.
  These subtrees are also binary tree.

In order traversal is performed as:

* Traverse the left subtree.
* Visit root (print it).
* Traverse the right subtree.

We define depth of a node as follow:

* Root node is at depth 1.
* If the depth of parent node is d, then the depth of current node wll be d+1.

Swapping: Swapping subtrees of a node means that if initially node has left
subtree L and right subtree R, then after swapping left subtree will be R and
right subtree L.

Eg. In the following tree, we swap children of node 1.

                                Depth
    1               1            [1]
   / \             / \
  2   3     ->    3   2          [2]
   \   \           \   \
    4   5           5   4        [3]

Inorder traversal of left tree is 2 4 1 3 5 and of right tree is 3 5 1 2 4.

Swap operation: Given a tree and a integer, K, we have to swap the subtrees of
all the nodes who are at depth h, where h ∈ [K, 2K, 3K,...].

You are given a tree of N nodes where nodes are indexed from [1..N] and it is
rooted at 1. You have to perform T swap operations on it, and after each swap
operation print the inorder traversal of the current state of the tree.

Input Format:
Here each of ith element of list T (1 <= i <= N) contains two integers, a b,
where a is the index of left child, and b is the index of right child of ith node.
-1 is used to represent null node.

Each of these line contains an integer K.
"""

class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.depth = 0


class Tree:

    def __init__(self, tree):
        self.mNodes = []
        self.maxDepth = 0
        self.tree = tree

    def builTree(self, numberNodes):
        root = Node()
        root.depth = 1
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
        left.value = leftPos
        left.depth = node.depth + 1
        if left.depth > self.maxDepth:
            self.maxDepth = left.depth
        self.mNodes.append((leftPos-1, left))

    def addRightNode(self, node, rightPos):
        right = Node()
        right.value = rightPos
        right.depth = node.depth + 1
        if right.depth > self.maxDepth:
            self.maxDepth = right.depth
        self.mNodes.append((rightPos-1, right))

    def performSwap(self, k):
        for i in range(k, self.maxDepth, k):
            for node in self.mNodes:
                node = node[1]
                if node.depth == i:
                    temp = node.left
                    node.left = node.right
                    node.right = temp
        self.printInOrder(self.mNodes[0][1])

    def printInOrder(self, node):
        if (node is None) or (node.value == -1):
            return
        if (node.left != -1):
            self.printInOrder(self.mNodes[node.left-1][1])
        print("{} ".format(node.value))
        if node.right != -1:
            self.printInOrder(self.mNodes[node.right-1][1])


# T = [(2, 3), (-1, -1), (-1, -1)]
# T = [(2, 3), (-1, 4), (-1, 5), (-1, -1), (-1, -1)]
T = [(2, 3), (4, -1), (5, -1), (6, -1), (7, 8), (-1, 9),
     (-1, -1), (10, 11), (-1, -1), (-1, -1), (-1, -1)]

tree = Tree(T)
tree.builTree(6)
tree.builTree(11)
tree.performSwap(2)
tree.performSwap(4)