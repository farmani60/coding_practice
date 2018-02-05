# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in
# reverse order and each of their nodes contain a single
# digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading
# zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Definition for singly-linked list.

import sys

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def StringToListNode(input):
    # Generate list from the input.
    numbers = [int(i) for i in list(input)]
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def ListNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


class Solution(object):
    def addTwoNumber(self, l1, l2):
        """
        Args:
            l1: type, ListNode
            l2: type, ListNode
            root: type, ListNode
        """
        l1 = StringToListNode(l1)
        l2 = StringToListNode(l2)
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

def main():
    buffer = []
    ind = 0
    while ind < 2:
        userinput = sys.stdin.readline().rstrip('\n')
        buffer.append(userinput)
        ind += 1
    ret = Solution().addTwoNumber(l1=buffer[0], l2=buffer[1])
    out = ListNodeToString(rest)
    print(out)

if __name__ == '__main__':
    main()