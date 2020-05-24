"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

"""

"""
s1 = "abc"
s2 = "bcd"
s3 = "abcbdc"

s1: abc
i: 0
s2: bcd
j: 0
res: ""
s3: abcbdc

s1: abc
i: 1
s2: bcd
j: 0
res: a
s3: abcbdc

s1: abc
i: 2
s2: bcd
j: 0
res: ab
s3: abcbdc

s1: abc
i: 3
s2: bcd
j: 0
res: abc
s3: abcbdc

s1: abc
i: 3
s2: bcd
j: 1
res: abcb
s3: abcbdc

s1: abc
i: 3
s2: bcd
j: 2
res: abcbc
s3: abcbdc

s1: abc
i: 3
s2: bcd
j: 3
res: abcbcd
s3: abcbdc
"""
class Solution(object):
    """
    Time complexity: O(2**(m+n)). m is the length of s1 and n is the length of s2.
    Spce complexity: O(m+n). The size of stack for recursive calls can go upto m+n.
    """
    def isInterleave(self, s1, s2, s3):
        """
        :param s1: str
        :param s2: str
        :param s3: str
        :return: bool
        """
        return self._isInterleave(s1, 0, s2, 0, "", s3)

    def _isInterleave(self, s1, i, s2, j, res, s3):
        if (res == s3) and (i == len(s1)) and (j == len(s2)):
            return True
        ans = False
        if i < len(s1):
            ans |= self._isInterleave(s1, i + 1, s2, j, res + s1[i], s3)
        if j < len(s2):
            ans |= self._isInterleave(s1, i, s2, j + 1, res + s2[j], s3)
        return ans

if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    s = Solution()
    print(s.isInterleave(s1, s2, s3))