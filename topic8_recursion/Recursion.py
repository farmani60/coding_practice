"""
Recursion allows a function to call itself. Fixed steps of code get executed
again and again for new values. We also have to set criteria for deciding when
the recursive call ends.

Binary Search using Recursion
We use an ordered list of items and design a recursive function to take in the list
along with starting and ending index as input. Then the binary search function
calls itself till find the the searched item or concludes about its absence in
the list.
"""

def binarySearch(list, idx0, idxn, val):
    if idxn < idx0:
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
        # Compare the serach item with middle value
        if list[midval] > val:
            return binarySearch(list, idx0, midval-1, val)
        elif list[midval] < val:
            return binarySearch(list, midval+1, idxn, val)
        else:
            return midval

list = [8, 11, 24, 56, 88, 131]
print(binarySearch(list, 0, 5, 24))
print(binarySearch(list, 0, 5, 51))