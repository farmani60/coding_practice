class Node:
    def __init__(self, dataval):
        self.dataval  = dataval
        self.nextval = None

class SLinkdList:
    def __init__(self):
        self.headval = None

    def PrintList(self):
        if self.headval is None:
            return
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtEnd(self, newval):
        NewNode = Node(newval)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = NewNode


if __name__ == "__main__":
    list1 = SLinkdList()
    list1.headval = Node("Mon")
    e2 = Node("Tue")
    list1.headval.nextval = e2
    e3 = Node("Wed")
    e2.nextval = e3
    list1.AtEnd("Thur")
    list1.PrintList()