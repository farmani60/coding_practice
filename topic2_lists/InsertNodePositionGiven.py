
class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None

def insertNodeAtPosition(headnode, data, position):
    NewNode = Node(data)
    if headnode is None:
        return NewNode
    if position == 0:
        NewNode.nextnode = headnode
        return NewNode
    node = headnode
    currPositioin = 0
    while (currPositioin < position - 1) and (node.nextnode is not None):
        node = node.nextnode
        currPositioin += 1
    NewNode.nextnode = node.nextnode
    node.nextnode = NewNode
    return headnode

def printList(head):
    printdata = head
    while True:
        print(printdata.data)
        if printdata.nextnode is None:
            break
        printdata = printdata.nextnode

e1 = Node(16)
e2 = Node(13)
e3 = Node(7)
e2.nextnode = e3
e1.nextnode = e2

printList(e1)

insertNodeAtPosition(e1, 1, 2)
printList(e1)