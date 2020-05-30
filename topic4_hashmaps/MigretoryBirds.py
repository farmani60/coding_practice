# Description:
# https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=internal-search

class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextnode = None

class LinkedList:
    def __init__(self):
        self.headnode = None

    def add(self, newdata):
        NewNode = Node(newdata)
        if self.headnode is None:
            self.headnode = NewNode
            return
        laste = self.headnode
        while laste.nextnode:
            laste = laste.nextnode

    def size(self):
        if self.headnode is None:
            return 0
        size = 1
        laste = self.headnode
        while laste.nextnode:
            size += 1
            laste = laste.nextnode
        return size

def migretoryBirsds(arr):
    birdsType = createMap(arr)
    typeBird = None
    numBird = 0
    for i in birdsType.keys():
        if birdsType[i] > numBird:
            typeBird = i
            numBird = birdsType[i]
        elif (birdsType[i] == numBird) and (i < typeBird):
            typeBird = i
    return typeBird


def createMap(arr):
    birdsType = dict()
    for i in range(len(arr)):
        if arr[i] not in birdsType.keys():
            birdsType[arr[i]] = 1
        else:
            birdsType[arr[i]] += 1
    return birdsType

arr = [1, 1, 2, 2, 3]
print(migretoryBirsds(arr))