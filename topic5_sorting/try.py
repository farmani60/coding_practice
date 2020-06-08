
def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def quickSort(list):
    pivot = list[0]
    equal = []
    left = []
    right = []
    for e in list:
        if e == pivot:
            equal.append(e)
        elif e < pivot:
            left.append(e)
        elif e > pivot:
            right.append(e)
    if len(left) > 1:
        left = quickSort(left)
    if len(right):
        right = quickSort(right)
    return left + equal + right

list = [5, 8, 1, 3, 7, 9, 2]
print(bubbleSort(list))
print(quickSort(list))