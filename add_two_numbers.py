# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single
# digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1 = l1[::-1]
        l2 = l2[::-1]
        n1 = str(l1[0])
        n2 = str(l2[0])
        for i in range(1, len(l1)):
            n1 += str(l1[i])
        for i in range(1, len(l2)):
            n2 += str(l2[i])
        result = int(n1) + int(n2)
        result = list(str(result))[::-1]
        result = map(lambda x: int(x), result)
        return result



if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    print(result)

