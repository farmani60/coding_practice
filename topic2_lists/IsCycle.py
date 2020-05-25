class Node:
    def __init__(self, data):
        self.data = data
        self.nextnode = None

def has_cycle(head):
    if head is None:
        return None
    node = head
    nodes_list = [node]
    while True:
        node = node.nextnode
        if node in nodes_list:
            return True
        else:
            nodes_list.append(node)
        if node.nextnode is None:
            return False

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
#
# e1.nextnode = e2
# e2.nextnode = e3

e3.nextnode = e2
e2.nextnode = e3
e1.nextnode = e2

print(has_cycle(e1))