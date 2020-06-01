"""
Merge sort first divides the array into equal halves and then combines them in a
sorted manner.
"""

def MergeSort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    # Find the middle point and divide the list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    left_list = MergeSort(left_list)
    right_list = MergeSort(right_list)
    return list(Merge(left_list, right_list))

# Merge the sorted halves
def Merge(left_half, right_half):
    res = []
    while (len(left_half) != 0) and (len(right_half) != 0):
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(MergeSort(unsorted_list))