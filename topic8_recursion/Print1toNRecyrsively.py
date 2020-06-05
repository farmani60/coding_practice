
def printRecursively(n):
    if n > 0:
        printRecursively(n-1)
        print(n, end=" ")

printRecursively(20)