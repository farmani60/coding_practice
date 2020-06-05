"""
Print numbers 1 to N using indirect recursion.
"""
N = 20
n = 1

def func1():
    global N, n
    if n <= N:
        print(n, end=" ")
        n += 1
        func2()
    else:
        return

def func2():
    global N, n
    if n <= N:
        print(n, end=" ")
        n += 1
        func1()
    else:
        return

func1()