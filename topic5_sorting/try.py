

def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j+1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def quickSort(arr):
    pivot = arr[0]
    equal = []
    left = []
    right = []
    for x in arr:
        if x == pivot:
            equal.append(x)
        elif x > pivot:
            right.append(x)
        else:
            left.append(x)
        if len(left) > 1:
            left = quickSort(left)
        if len(right) > 1:
            right = quickSort(right)
    return left + equal + right

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        next_element = arr[i]
        while (arr[j] > next_element) and (j >= 0):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = next_element
    return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)
    return Merge(left_half, right_half)

def Merge(left_half, right_half):
    res = []
    while (len(left_half) != 0) and (len(right_half) != 0):
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half)
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

def selectionSort(arr):
    for i in range(len(arr)):
        min_id = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_id]:
                min_id = j
        arr[i], arr[min_id] = arr[min_id], arr[i]
    return arr


if __name__ == '__main__':
    list = [19, 2, 31, 45, 6, 11, 121, 27]
    print(selectionSort(list))