"""
1, 1, 2, 3, 5, 8, 13, 21
"""

def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-2) + Fibonacci(n-1)

print([Fibonacci(x) for x in range(1, 8)])