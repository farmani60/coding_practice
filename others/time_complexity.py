"""
Run some algorithms to practice time and space complexity (Big-O)
"""

# Constant Run Time: O(1) describes algorithms that take the same amount of time
# to compute regardless of the input size.
def isEven(arr, ind):
    """As the length of array grows larger, the number of operation remains
    constant. O(1)"""
    return arr[ind] % 2 == 0

def getWordFrequency(dictionary, word):
    """Look-up table. Given a dictionary, finds its word frequency data.
    O(1)"""
    return dictionary[word]

# Linear Run Time: O(n)
# These algorithms imply that the program visits every element from the input in
# the worst case.
def getMin(arr):
    """Find minimum or maximum of an input array. As the length of input array
    grows, the number of operations grows linearly. O(n)"""
    min_val = arr[0]
    for i in arr[1:]:
        if i < min_val:
            min_val = i
    return min_val

def findElement(arr, el):
    """Find a given element in a collection. O(n)"""
    for i in arr:
        if el == i:
            return True
    return False

def printAllElements(arr):
    """Print all elements of a collection. O(n)"""
    for i in arr:
        print(i)

# A function with a quadratic time complexity has grown rate of n^2. If the
# input size is 2, it will do 4 operations. If the input size is 8, it will
# take 64, and so on. O(n^2)
def hasDuplicates(arr):
    """Check if a collection has duplicate values. O(n^2)"""
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] == arr[j]:
                return True
    return False

# bubble sort: O(n^2)
# insertion sort: O(n^2)
# selection sort: O(n^2)
def bubbleSort(arr):
    """Bubble sort. O(n^2)"""
    for i in range(len(arr)):
        x = arr[i]
        for j in range(i+1, len(arr)):
            y = arr[j]
            if x > y:
                arr[i] = y
                arr[j] = x
                x = arr[i]
                y = arr[j]
    return arr

def findAllPairs(arr):
    """Find all possible ordered pairs in an array."""
    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            pairs.append((arr[i], arr[j]))
    return pairs

# Polynomial time complexity: O(n^c)

def findXYZ(n):
    """Find the solutions for 3x+9y+8z=79 equation. This naïve program will give
    you all the solutions that satisfy the equation where x, y, and z < n.
    cubic run time: O(n^3)"""
    solutions = []
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if 3*x + 9*y + 8*z == 79:
                    solutions.append((x, y, z))
    return solutions


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    # print(isEven(arr, ind=1))
    # print(getMin(arr))
    # dictionary = {'the': 22038615, 'be': 12545825, 'and': 10741073,
    #               'of': 10343885, 'a': 10144200, 'in': 6996437, 'to': 6332195}
    # print(getWordFrequency(dictionary, 'to'))
    # arr, counter = bubbleSort([5, 4, 3, 2, 1])
    # pairs = findAllPairs([1, 2, 3])
    # print(pairs)
    sols = findXYZ(10)
    print(sols)