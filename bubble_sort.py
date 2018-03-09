from __future__ import print_function

class BubbleSort(object):
    """complexity: O(n2)"""
    def sortMachine(self, collections):
        for i in range(len(collections)):
            for j in range(len(collections)-1):
                if collections[j] > collections[j+1]:
                    collections[j], collections[j+1] = \
                        collections[j+1], collections[j]
        return collections

if __name__ == '__main__':
    input = [0, 7, 5, 3, 5]
    sorted = BubbleSort().sortMachine(collections=input)
    print(sorted)
