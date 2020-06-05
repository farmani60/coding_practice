"""
These algorithms imply that the program visits every element from the input.

Linear time complexity O(n) means that as the input grows, the algorithms take
proportionally longer to complete.

Examples of linear time algorithms:

* Get the max/min value in an array.
* Find a given element in a collection.
* Print all the values in a list.
"""

# Find largest item in an unsorted list
def findMax(list):
    maxval = float('-inf')
    for i in list:
        if i > maxval:
            maxval = i
    return maxval


list = [6, -5, 3, 7, -6 , 10]
print(findMax(list))