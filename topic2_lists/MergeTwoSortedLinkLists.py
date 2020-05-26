class Node:
    def __index__(self, data):
        self.data = data
        self.nextdone = None

def mergeLists(head1, head2):
    x = Node(min(head1.data, head2.data))
    node1 = head1
    node2 = head2
    while (node1.data is not None) or (node1.nextnode is not None):
        while (node2.data is not None) or (node2.nextnode is not None):
            if node1.data <= node2.data:

def AddInBetween(headnode, data, position):
    NewNode = Node(data)
    if headnode is None:
        return NewNode
    if position == 0:
        NewNode.nextdone = headnode
        return NewNode
    node = headnode
    currPosition = 0
    while (currPosition < position - 1) and (node.nextdone is not None):
        node = node.nextdone
        currPosition += 1
    NewNode.nextdone = node.nextdone
    node.nextdone = NewNode
    return headnode


e1 = Node(1)
e2 = Node(2)
e3 = Node(3)

e2.nextnodet = e3
e1.nextnodet = e2

f1 = Node(3)
f2 = Node(4)

f1.nextnode = f2
