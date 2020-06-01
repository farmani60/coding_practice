# Description: https://www.hackerrank.com/challenges/icecream-parlor/problem

class Node:
<<<<<<< HEAD
    def __init__(self, data):
        self.data = data
        self.nextnode = None

def LinkedList(headnode, data):
    NewNode = Node(data)
    if headnode.nextnode is None:
        headnode.nextnode = NewNode
        return headnode
    laste = headnode
    while laste.nextnode:
        laste = laste.nextnode
    laste.nextnode = NewNode
    return headnode

class Solution:
    def __init__(self):
        pass

    # Complexity: O(n^2)
    def icecreamParlorBasicolution(self, m, arr):
        """
        :param m: integer, the amount of pooled money
        :param arr: list of integers, cost of each icecream flavor
        :return: tuple of integers, indices of two flavoured icecream
        """
        iceCreameOne = 0
        iceCreameTwo = 0
        for i in range(len(arr)-1):
            for j in range(1, len(arr)):
                if arr[i] + arr[j] == m:
                    iceCreameOne = i
                    iceCreameTwo = j
                    break
        iceCreameOne += 1
        iceCreameTwo += 1
        return (iceCreameOne, iceCreameTwo)

    # If we think about it, this turns into a search problem. We are trying to look to
    # elements such as m = element1 + element2; for each item in the array (element1),
    # element2 will be m - element1. Knowing that, instead of having an inner loop (for
    # inside of a for loop) that will take O(N ^ 2) to run, we can take a little bit of
    # memory hit, and create a hashMap with each of the items of the array to avoid the
    # second loop. Let's look at the solution.
    def icecreamParlor(self, m, arr):
        iceCreamOne = 0
        iceCreamTwo = 0

    def createMap(self, arr):
        # Create a hash map
        costToIndex = dict()
        for i in range(len(arr)):
            # They say that some elements might have the same cost.
            # And in that case they always prefer the lower ID (index).
            # Therefore, if the cost is already in our map, we will
            # append it into a LinkedList.
            if not arr[i] in costToIndex.keys():
                indexList = Node(i)
                indexList.append(i)
                # LinkedList(indexList, i)
                costToIndex[arr[i]] = indexList
            else:
                costToIndex[arr[i]].append(i)
        return costToIndex


m = 5
arr =[1, 4, 5, 3, 2]



=======
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextnode = None

class LinkedList:
    def __init__(self):
        self.headnode = None

    def add(self, newdata):
        NewNode = Node(newdata)
        if self.headnode == None:
            self.headnode = NewNode
            return
        laste = self.headnode
        while laste.nextnode:
            laste = laste.nextnode
        laste.nextnode = NewNode

    def size(self):
        if self.headnode in None:
            return 0
        size = 1
        laste = self.headnode
        while laste.nextnode:
            size += 1
            laste = laste.nextnode
        return size

    def printLink(self):
        printdata = self.headnode
        while True:
            print(printdata.dataval)
            if printdata.nextnode is None:
                break
            printdata = printdata.nextnode

# Complexity: O(n^2)
def icecreamParlorBasicSolution(m, arr):
    """
    :param m: integer, the amount of pooled money
    :param arr: list, cost of each flavor
    :return: tuple, flavors' indices
    """
    iceCreamOne = 0
    iceCreamTwo = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                iceCreamOne = i + 1
                iceCreamTwo = j + 1
                return (iceCreamOne, iceCreamTwo)
    return "No flavors with input costs!"


# If we think about it, this turns into a search problem. We are trying to look
# to elements such as m = element1 + element2; for each item in the array (element1),
# element2 will be m - element1. Knowing that, instead of having an inner loop
# (for inside of a for loop) that will take O(N ^ 2) to run, we can take a little
# bit of memory hit, and create a hashMap with each of the items of the array to
# avoid the second loop. Let's look at the solution.
def icecreamParlor(m, arr):
    """
    :param m: integer, the amount of pooled money
    :param arr: list, cost of each flavor
    :return: tuple, flavors' indices
    """
    iceCreamOne = 0
    iceCreamTwo = 0
    costToIndex = createMap(arr)
    # This loop takes O(n) time to run. Much faster than the previous solution.
    for i in range(len(arr)-1):
        if (m - arr[i]) in costToIndex.keys():
            iceCreamOne = i
            iceCreamTwo = costToIndex[m-arr[i]].headnode.dataval
            # In case where we need two different IceCreams of the same price.
            if iceCreamOne == iceCreamTwo:
                if costToIndex[m-arr[i]].size() > 1:
                    iceCreamTwo = costToIndex[m-arr[i]].headnode.nextdata.dataval
                    break
            else:
                break
    iceCreamOne += 1
    iceCreamTwo += 1
    return (iceCreamOne, iceCreamTwo)

def createMap(arr):
    # Creat a hash map
    costToIndex = dict()
    for i in range(len(arr)):
        # They say that some elements might have the same cost. And
        # in that case they always prefer the lower ID (index).
        # Therefore, if the cost is already in our map, we will append it into a
        # LinkedList.
        if arr[i] not in costToIndex.keys():
            indexList = LinkedList()
            indexList.add(i)
            costToIndex[arr[i]] = indexList
        else:
            costToIndex[arr[i]].add(i)
    return costToIndex

arr = [1, 4, 5, 3, 2]
m = 5
print(icecreamParlorBasicSolution(m, arr))
print(icecreamParlor(m, arr))
>>>>>>> 50520e55d81a64306e191953a0b02a444019f707
