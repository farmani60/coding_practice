class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None

def mergeLists(head1, head2):
    if (head1 is None) and (head2 is None):
        return None
    if (head1 is not None) and (head2 is None):
        return head1
    if (head1 is None) and (head2 is not None):
        return head2
    if head1.data <= head2.data:
        head1.nextnode = mergeLists(head1.nextnode, head2)
    elif head1.data > head2.data:
        temp = head2
        head2 = head2.nextnode
        temp.nextnode = head1
        head1 = temp
        head1.nextnode = mergeLists(head1.nextnode, head2)
    return head1

def printList(head):
    printdata = head
    while True:
        print(printdata.data)
        if printdata.nextnode is None:
            break
        printdata = printdata.nextnode

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e2.nextnode = e3
e1.nextnode = e2
printList(e1)

f1 = Node(3)
f2 = Node(4)
f1.nextnode = f2
printList(f1)

g1 = mergeLists(e1, f1)
printList(g1)
