"""
Logarithmic time complexities usually apply to algorithms
that divide problems in half every time.

If we implement (Algorithm A) going through all the elements
in an array, it will take a running time of O(n). We can try
using the fact that the collection is already sorted.
Later, we can divide in half as we look for the element in
question. O(log(n))
"""
def binarySearch(arr, element, offest=0):
    middle = len(arr) // 2
    current = arr[middle]
    if current == element:
        return middle + offest
    elif element > current:
        right = arr[middle:]
        return binarySearch(right, element, offest+middle)
    else:
        left = arr[:middle]
        return binarySearch(left, element, offest)


arr = [1, 3, 5, 6, 8, 9, 10, 13, 15]

print(binarySearch(arr, 1))

def binarySearch(arr, element, offset=0):
    middle = len(arr) // 2
    current = arr[middle]
    if element == current:
        return middle + offset
    elif element > current:
        right = arr[middle:]
        return binarySearch(right, element, offset+middle)
    else:
        left = arr[:middle]
        return binarySearch(left, element, offset)