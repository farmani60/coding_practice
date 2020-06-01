# Description:
# https://www.hackerrank.com/challenges/insertionsort1/problem?h_r=internal-search

def insertionSort1(arr):
    for i in range(len(arr)):
        if arr[i] > arr[-1]:
            temp = arr[i]
            arr[i] = arr[-1]
            arr[-1] = temp

input_list = [2, 4, 6, 8, 3]
insertionSort1(input_list)
print(input_list)
