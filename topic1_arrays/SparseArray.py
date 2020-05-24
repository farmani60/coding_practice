"""
There is a collection of input strings and a collection of query strings. For
each query string, determine how many times it occurs in the list of input
strings.

For example, given input strings = ['ab', 'ab', 'abc'] and
queries = ['ab', 'abc', 'bc'], we find 2 instances of 'ab', 1 of 'abc' and 0 of
'bc'. For each query, we add an element to our return array, results = [2, 1, 0].

Function Description:
Complete the function matchingStrings in the editor below. The function must
return an array of integers representing the frequency of occurrence of each
query string in strings.

matchingStrings has the following parameters:
strings - an array of strings to search
queries - an array of query strings

Input Format:
The first line contains and integer n, the size of strings.
Each of the next n lines contains a string strings[i].
The next line contains q, the size of queries.
Each of the next q lines contains a string q[i].

4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Constraints:
1 <= n <= 1000
1 <= q <= 1000
1 <= |strigs[i], queries[i]| <= 20

Output Format:
Return an integer array of the results of all queries in order.
2
1
0
"""
from collections import defaultdict

def matchingStrings(strings, queries):
    results = []
    for q in queries:
        k = 0
        for s in strings:
            if q == s:
                k += 1
        results.append(k)
    return results

def matchingStrings_(strings, queries):
    # time complexity O(N*Q*20)
    words = defaultdict(int)
    result = []
    for s in strings:
        words[s] += 1
    for q in queries:
        try:
            result.append(words[q])
        except:
            result.append(0)
    return result

from collections import defaultdict

if __name__ == '__main__':
    strings = ["aba", "baba", "aba", "xzxb"]
    queries = ["aba", "xzxb", "ab"]
    print(matchingStrings_(strings, queries))