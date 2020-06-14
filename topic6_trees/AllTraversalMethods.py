"""
Tree Traversal:

         1
       /   \
     2      3
   /  \
 4     5

 Breadth First Serach (Level Order): 1 2 3 4 5

 Time Complexity: O(n^2) in worst case. For a skewed tree, printGivenLevel()
 takes O(n) time where n is the number of nodes in the skewed tree. So time
 complexity of printLevelOrder() is O(n) + O(n-1) + O(n-2) + .. + O(1) which is
 O(n^2).

Space Complexity: O(n) in worst case. For a skewed tree, printGivenLevel() uses
 O(n) space for call stack. For a Balanced tree, call stack uses O(log n) space,
 (i.e., height of the balanced tree).

 Deapth First Search:
 * in order (left, root, right): 4 2 5 1 3
 * pre order (root, left, right): 1 2 4 5 3
 * post order (left right root): 4 5 2 3 1

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.data, end=" ")
        if root.left:
            preOrder(root.left)
        if root.right:
            preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")

def printLevelOrder(root):
    h = Height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def Height(node):
    if node is None:
        return 0
    else:
        left_height = Height(node.left)
        right_height = Height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


# make the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# breadth first traversal
printLevelOrder(root)
print("\n")
# depth first traversal: in order
inOrder(root)
print("\n")
# depth first traversal: pre order
preOrder(root)
print("\n")
# depth first traversal: post order
postOrder(root)


