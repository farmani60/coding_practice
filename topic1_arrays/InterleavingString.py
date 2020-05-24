"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

The most basic idea is to find every string possible by all interleavings of the
two given strings s1 and s2. In order to implement this method, we are using
recursion. We start by taking the current character of the first string s1 and
then appending all possible interleavings of the remaining portion of the first
string s1 and the second string s2 and comparing each result formed with the
required interleaved string s3. Similarly, we choose one character from the
second string s2 and form all the interleavings with the remaining portion of s2
and s1 to check if the required string s3 can be formed.
"""

class Solution(object):
    """
    Time complexity: O(2**(m+n)). m is the length of s1 and n is the length of s2.
    Space complexity: O(m+n). The size of stack for recursive calls can go upto m+n.
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
            ans |= self._isInterleave(s1, i + 1, s2, j, res+s1[i], s3)
        if j < len(s2):
            ans |= self._isInterleave(s1, i, s2, j + 1, res+s2[j], s3)
        return ans

if __name__ == "__main__":
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbcbcac"
    s1, s2, s3 = "aa", "b", "aba"
    s = Solution()
    print(s.isInterleave(s1, s2, s3))