"""
Heap is a special tree structure in which each parent node is less than or equal
to its child node. Then it is called a Min Heap. If each parent node is greater
than or equal to its child node then it is called a max heap.

Here, a heap is created by using python’s inbuilt library named heapq. This
library has the relevant functions to carry out various operations on heap data
structure. Below is a list of these functions.

heapify - This function converts a regular list to a heap. In the resulting heap
          the smallest element gets pushed to the index position 0. But rest of
          the data elements are not necessarily sorted.
heappush – This function adds an element to the heap without altering the
           current heap.
heappop - This function returns the smallest data element from the heap.
heapreplace – This function replaces the smallest data element with a new value
              supplied in the function.

Complextity: O(n log(n))
"""

import heapq

H = [21, 1, 45, 78, 3, 5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
# Add an element at the last index of the heap
heapq.heappush(H, 8)
print(H)
# Apply heapify function again to bring the newly added element to the first
# index only if it is the smallest in value.
heapq.heapify(H)
print(H)
# Remove the element from the heap
heapq.heappop(H)
print(H)
# Replace an element
H = [21, 1, 45, 78, 3, 5] # Create the heap
heapq.heapify(H)
print(H)
heapq.heapreplace(H, 6) # Replace an element with the smallest one in the heap
print(H)