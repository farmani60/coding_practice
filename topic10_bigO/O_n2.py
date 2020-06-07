"""
https://adrianmejia.com/most-popular-algorithms-time-complexity-every-programmer-should-know-free-online-tutorial-course/#Odd-or-Even

A function with a quadratic time complexity has a growth rate of n2. If the
input is size 2, it will do four operations. If the input is size 8, it will
take 64, and so on.

Here are some examples of quadratic algorithms:

Check if a collection has duplicated values.
Sorting items in a collection using bubble sort, insertion sort, or selection sort.
Find all possible ordered pairs in an array.
"""

def hasDuplicates(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] == arr[j]:
                return True
    return False

def bubbleSort(arr):
    for i in range(len(arr)):
        outer = arr[i]
        for j in range(i+1, len(arr)):
            inner = arr[j]
            if outer > inner:
                arr[i] = inner
                arr[j] = outer
                outer = arr[j]
                inner = arr[i]
    retunr arr