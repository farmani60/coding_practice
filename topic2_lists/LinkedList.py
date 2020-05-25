
class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

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