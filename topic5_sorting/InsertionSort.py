"""
Insertion sort involves finding the right place for a given element in a sorted
list. So in beginning we compare the first two elements and sort them by comparing
them. Then we pick the third element and find its proper position among the
previous two sorted elements. This way we gradually go on adding more elements
to the already sorted list by putting them in their proper position.
"""

def insertionSort(input_list):
    for i in range(1, len(input_list)):
        j = i - 1
        next_element = input_list[i]
        # Compare the current element with the next one
        while (input_list[j] > next_element) and (j >= 0):
            input_list[j+1] = input_list[j]
            j = j - 1
        input_list[j+1] = next_element

list = [19, 2, 31, 45, 30, 11, 121, 27]
insertionSort(list)
print(list)
