
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def atBeginnign(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
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

    def inBetween(self, middle_node, newdata):
        NewNode = Node(newdata)
        if middle_node is None:
            return
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def removeNode(self, key):
        if self.head is not None:
            if self.head.data == key:
                self.head = self.head.next
                return
        head = self.head
        while head:
            if head.data == key:
                break
            prev = head
            head = head.next
        if head is None:
            return
        prev.next = head.next
        head = None


