class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None

def insertNodeAtEnd(headnode, data):
    NewNode = Node(data)
    if headnode.nextnode is None:
        headnode.nextnode = NewNode
        return headnode
    laste = headnode
    while laste.nextnode:
        laste = laste.nextnode
    laste.nextnode = NewNode
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

insertNodeAtEnd(e1, 1)

printList(e1)