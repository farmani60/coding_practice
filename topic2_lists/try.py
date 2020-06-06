
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node

    def printList(self):
        if self.head is None:
            return
        printval = self.head
        while printval:
            print(printval.data, end=" ")
            printval = printval.next

    def inBeginning(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head = NewNode

    def atEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while laste:
            laste = laste.next
        laste.next = NewNode

    def inBetween(self, newdata, middle_key):
        NewNode = Node(newdata)
        NewNode.next = middle_key.next
        middle_key.next = NewNode

    def removeNode(self, key):
        head = self.head
        if head is not None:
            if head == key:
                self.head = head.next
                head = None
                return
        while head:
            prev = head
            if head.next == key:
                head = head.next
                break
            head = head.next
        if head is None:
            return
        prev.next = head.next


def has_cycle(head):
    if head is None:
        return False
    node = head
    node_list = []
    while node:
        if node in node_list:
            return True
        else:
            node_list.append(node)
            node = node.next
    return False


