
def insertionSort(input_list):
    for i in range(1, len(input_list)):
        j = i - 1
        next_element = input_list[i]
        while (input_list[j] > next_element) and (j >= 0):
            input_list[j+1] = input_list[j]
            j -= 1
        input_list[j+1] = next_element

input_list = [5, 1, 3, 9, 7, 4]
insertionSort(input_list)
print(input_list)