"""
Description:
https://www.hackerrank.com/challenges/swap-nodes/problem?h_r=internal-search

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
"""

class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.depth = None

mNodes = []
maxDepth = 0

def buildTree(numberNodes, ):
    root = Node()
    root.depth = 1
    mNodes.append((0, root))
    for i in range(1, numberNodes+1):
        node = mNodes[i-1][0]
        node.value = i
        leftPos =
        rightPos =
        if leftPos != -1:
            addLeftNode(node, leftPos)
        if rightPos != -1:
            addRightNode(node, rightPos)
        node.left = leftPos
        node.right = rightPos


def addLeftNode(node, leftPos):
    left = Node()
    left.depth = node.depth + 1
    if left.depth > maxDepth:
        maxDepth = left.depth
    mNodes.append((leftPos-1, left))

def addRightNode(node, rightPos):
    right = Node()
    right.depth = node.depth + 1
    if right.depth > maxDepth:
        maxDepth = right.depth
    mNodes.append((rightPos-1, right))




