"""
In selection sort we start by finding the minimum value in a given list and move
it to a sorted list. Then we repeat the process for each of the remaining elements
in the unsorted list. The next element entering the sorted list is compared with
the existing elements and placed at its correct position. So at the end all the
elements from the unsorted list are sorted.
"""

def SelectionSort(input_list):
    for i in range(len(input_list)):
        min_id = i
        for j in range(i+1, len(input_list)):
            if input_list[min_id] > input_list[j]:
                min_id = j
        # Swap the minimum value with the compared value
        input_list[i], input_list[min_id] = input_list[min_id], input_list[i]

input_list = [19,2,31,45,30,11,121,27]
SelectionSort(input_list)
print(input_list)