class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLists(head1, head2):
    if (head1 is None) and (head2 is not None):
        return head2
    if (head1 is not None) and (head2 is None):
        return head1
    if (head1 is None) and (head2 is None):
        return  None
    if head1.data <= head2.data:
        head1.next = mergeLists(head1.next, head2)
    else:
        temp = head2
        head2 = head2.next
        temp.next = head1
        head1 = temp
        head1.next = mergeLists(head1.next, head2)
    return head1

def printList(head):
    if head is None:
        return
    printval = head
    while printval:
        print(printval.data, end=" ")
        printval = printval.next

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e2.next = e3
e1.next = e2

f1 = Node(3)
f2 = Node(4)
f1.next = f2

l = mergeLists(e1, f1)
printList(l)

