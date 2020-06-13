# Description:
# https://www.hackerrank.com/challenges/quicksort1/problem?h_r=internal-search

def quickSort1(arr):
    pivot = arr[0]
    equal = []
    left = []
    right = []
    for i in arr:
        if i == pivot:
            equal.append(i)
        elif i < pivot:
            left.append(i)
        else:
            right.append(i)
    if len(left) > 1:
        left = quickSort1(left)
    if len(right) > 1:
        right = quickSort1(right)
    return left + equal + right



arr = [4, 5, 3, 7, 2]
print(quickSort1(arr))
