"""
Description:
https://www.hackerrank.com/challenges/waiter/problem?h_r=internal-search
"""
# create first 1000 prime numbers
lower = 2
upper = 1000
prime_numbers = [i for i in range(lower, upper+1)
                 if all([i % j == 0 for j in range(2, i)])]

class Stack:
    def __init__(self):
        self.stack = list()
    def add(self, data):
        self.stack.append(data)
    def remove(self):
        self.stack.pop()

def Waiter(A0, iterNum):
    A = [A0]
    B = [None]
    for i in range(iterNum):
        a = Stack()
        b = Stack()
        for x in A[i][::-1]:
            if x % prime_numbers[i] == 0:
                b.add(x)
            else:
                a.add(x)
        A.append(a.stack)
        B.append(b.stack)
    del B[0]
    return A, B


# A0 = [3, 4, 7, 6, 5]
A0 = [3, 3, 4, 4, 9]
A, B = Waiter(A0, 2)
print(A)
print(B)

