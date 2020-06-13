"""
Logarithmic time complexities usually apply to algorithms that divide problems
in half every time. For instance, let’s say that we want to look for a book in a
dictionary. As you know, this book has every word sorted alphabetically. If you
are looking for a word, then there are at least two ways to do it:

Algorithm A:

1- Start on the first page of the book and go word by word until you find what
you are looking for.

Algorithm B:

1- Open the book in the middle and check the first word on it.
2- If the word that you are looking for is alphabetically more significant, then
look to the right. Otherwise, look in the left half.
3- Divide the remainder in half again, and repeat step #2 until you find the word
you are looking for.

Which one is faster? The first algorithms go word by word O(n), while the
algorithm B split the problem in half on each iteration O(log n). This 2nd
algorithm is a binary search.
"""

# Binary search: Find the index an element in a sorted arry.

# O(n)
def findIndex(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return None

# O(logn), we can use the fact that the array is already sorted.
def findIndex(arr, n, offset=0):
    middle = len(arr) // 2
    current = arr[middle]
    if current == n:
        return middle + offset
    elif n > current:
        right = arr[middle:]
        findIndex(right, n, offset+middle)
    else:
        left = arr[:middle]
        findIndex(left, n, offset)
    return None
