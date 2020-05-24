"""
A left rotation operation on an array shifts each of the array's elements 1 unit
to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5],
then the array would become [3,4,5,1,2].

Given an array a of n integers and a number, d, perform d left rotations on the
array. Return the updated array to be printed as a single line of
space-separated integers.

Function Description:
Complete the function rotLeft in the editor below. It should return the
resulting array of integers.

rotLeft has the following parameter(s):
An array of integers a.
An integer d, the number of rotations.

Input Format:
The first line contains two space-separated integers n and d, the size of a and
the number of left rotations you must perform.
The second line contains n space-separated integers a[i].

Constraints:
1 <= n <= 10**5
1 <= d <= n
1 <= a[i] <= 10**6

Output Format:
Print a single line of n space-separated integers denoting the final state of
the array after performing d left rotations.

Sample Input:
5 4
1 2 3 4 5

Sample Output:
5 1 2 3 4


a: [1, 2, 3, 4, 5]
d: 4
len(a): 5

rotation: 4

b: []

i: 0
indexHelper(4, 5): 4
b.append(a[4]) -> b: [5]

i: 1
indexHelper(5, 5): 0
b.append(a[0]) -> b: [5, 1]

i: 2
indexHelper(6, 5): 1
b: [5, 1, 2]

i: 3
indexHelper(7, 5) : 2
b: [5, 1, 2, 3]

i: 4
indexHelper(8, 5): 3
b: [5, 1, 2, 3, 4]
"""

def rotLeft(a, d):
    if d == 0 or len(a) == 0:
        return a
    rotation = d % len(a)
    if rotation == 0:
        return a
    b = []
    for i in range(len(a)):
        b.append(a[indexHelper(i+rotation, len(a))])
    return b

def indexHelper(ind, length):
    if ind >= length:
        return ind - length
    else:
        return ind

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    d = 4
    print(rotLeft(a, d))