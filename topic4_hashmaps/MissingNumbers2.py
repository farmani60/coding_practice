
# problem constraints
MAX_VALUE = 10**4
DIFF = 101

def missingNumbers(arr, brr):
    # If we know the min, now we can save the ocurrence of each number in an array
    # we will use the index as a representation of a number. E.g. if the list would
    # contain elements from 200 to 300 range, if we see 205, we will increment index 5
    # by 1.
    min = findMin(brr)
    occurence = [0 for _ in range(DIFF)]
    for i in brr:
        index = i - min
        occurence[index] += 1
    # Now we have a list that tells us how many times each number occur.
    # We can build the same list for A and then compare. Or we can iterate
    # A the same way and decrement everytime we see the number.
    for i in arr:
        index = i - min
        occurence[index] -= 1
    # Now all the indexes with value > 0 are those who are actually missing.
    misingList = []
    for i in range(DIFF):
        if occurence[i] > 0:
            misingList.append(i + min)
    return misingList

# They state that the maximum value we can find is 10^4 -- let's just
# go with that.
def findMin(brr):
    min = MAX_VALUE
    for i in brr:
        if i < min:
            min = i
    return min

arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

print(missingNumbers(arr, brr))