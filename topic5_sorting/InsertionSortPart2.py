# Description:
# https://www.hackerrank.com/challenges/insertionsort2/problem?h_r=internal-search
# O(n^2)
def insertionSort2(input_list):
    """
    :param input_list:
    :return:
    """
    for i in range(1, len(input_list)):
        j = i - 1
        next_element = input_list[i]
        while (input_list[j] > next_element) and (j >= 0):
            input_list[j+1] = input_list[j]
            j -= 1
        input_list[j+1] = next_element

input_list = [1, 4, 3, 5, 6, 2]
insertionSort2(input_list)
print(input_list)