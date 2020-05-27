"""
Description:
https://www.hackerrank.com/challenges/waiter/problem?h_r=internal-search
"""


class Stack:
    def __init__(self):
        self.stack = list()
    def add(self, data):
        self.stack.append(data)
    def remove(self):
        self.stack.pop()

def Waiter(A0, iter_num):
    A = [A0]
    B = [None]
    for i in range(iter_num):
        a = Stack()
        b = Stack()
        for x in A[i]:
            if x % A[i][i] == 0:
                b.add(x)
            else:
                a.add(x)
        A.append(a.stack)
        B.append(b.stack)
    del B[0]
    return A, B

A0 = [3, 3, 4, 4, 9]
A, B = Waiter(A0, iter_num=5)
print(A)
print(B)
