# Description:
# https://www.hackerrank.com/challenges/quicksort2/problem

def quickSort2(input_list):
    pivot = input_list[0]
    equal_part = []
    left_part = []
    right_part = []
    for i in input_list:
        if i == pivot:
            equal_part.append(i)
        elif i < pivot:
            left_part.append(i)
        else:
            right_part.append(i)
    if len(left_part) > 1:
        left_part = quickSort2(left_part)
    if len(right_part) > 1:
        right_part = quickSort2(right_part)
    return left_part + equal_part + right_part


input_list = [5, 8, 1, 3, 7, 9, 2]
print(quickSort2(input_list))