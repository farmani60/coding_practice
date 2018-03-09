class Solution(object):
    """Insertion sort, complexity: O(n2)"""
    def InsertionSort(self, collection):
        for i in range(1, len(collection)):
            while i > 0 and collection[i] < collection[i-1]:
                collection[i-1], collection[i] = collection[i], \
                                                 collection[i-1]
                i -= 1
        return collection


col = Solution().InsertionSort([0, 5, 3, 2, 2])
print(col)
