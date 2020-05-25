
class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # Insert new data node in the beginning of the linked list
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        # Update the newnode's nextval to the existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    # Insert new data node at the end of the linked list
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = NewNode

    # Insert new node in between two data nodes
    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent!")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    # Remove node
    def RemoveNode(self, RemoveKey):
        HeadVal = self.headval
        if HeadVal is not None:
            if HeadVal.dataval == RemoveKey:
                self.headval = HeadVal.nextval
                HeadVal = None
                return



list1 = SLinkedList()
list1.headval = Node("Monday")

# Link first node to the seacond node
e2 = Node("Tuesday")
list1.headval.nextval = e2

# Link the second node to the third node
e3 = Node("Wednsday")
e2.nextval = e3

# Print data elemnts
list1.listprint()

# Add new node to the beginning of the list
list1.AtBeginning("Sunday")

# Print data elemnts
list1.listprint()

# Add new node at the end of the list
list1.AtEnd("Thursday")

# Print data elements
list1.listprint()

# Add new node between two data node
list1.InBetween(list1.headval.nextval, "Friday")

# Print data elements
list1.listprint()