# Description:
# https://www.hackerrank.com/challenges/qheap1/forum

import heapq

def qHeap1(operation, item):
    if operation == 1:
        heapq.heappush(heap, item)
    elif operation == 2:
        heap.remove(item)
        # making a heap again
        heapq.heapify(heap)
    elif operation == 3:
        smallest = heapq.heappop(heap)
        # making a heap again
        heapq.heappush(heap, smallest)
        print(smallest)
    else:
        print("There is no {} operation!".format(operation))




heap = [21, 1, 45, 78, 3, 5]
heapq.heapify(heap)
print(heap)

qHeap1(1, 4)
print(heap)

qHeap1(1, 9)
print(heap)

qHeap1(3, None)

qHeap1(2, 4)
print(heap)

qHeap1(3, None)


