class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None

def mergeLists(head1, head2):
    pass

def appendNodeInNewList(head, tail, data):
    NewNode = Node(data)
    if head is not None:
        tail.nextnode = NewNode
    return NewNode



e1 = Node(1)
e2 = Node(2)
e3 = Node(3)

e2.nextnodet = e3
e1.nextnodet = e2

f1 = Node(3)
f2 = Node(4)

f1.nextnode = f2

mergeLists(e1, f1)