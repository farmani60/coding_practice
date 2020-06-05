"""
Given a string s1, we may represent it as a binary tree by partitioning it to
two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two
children.

For example, if we choose the node "gr" and swap its two children, it produces a
scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it
produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled
string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false

In order to check if the string is scramble or not we need to keep on matching
the string untils all our options are exhauseted.

As the question says, that a word would be scrambled if we choose any non-leaf
node and swap its childer.

Lets analyze one example,

great < orginal >
greta < scramble >

	greta
    /    \
   gr    eta
   /\      /\
  g  r    e  ta
             /\
           #t  a # --> This has been swapped with the original string,
Now if we consider the scramble string : "ta" and orginal string : "at"

we can validate that they are scramble if ith( in this case i==1) char of
original string is same as the last ith char of the new string, i.e we check if
org[i:] == new[:-i].

In addition to that few points to keep in mind if the size of the original
string is less than or equal to 3, the scramble would always be valid.
"""

class Solution:
    def __init__(self):
        pass

    def isScramble(self, s1, s2):
        """
        :param s1: str
        :param s2: str
        :return: bool
        """
        if sorted(s1) != sorted(s2) or len(s1) != len(s2):
            return False
        if len(s1) < 4:
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    s1 = "great"
    s2 = "rgtae"
    print(s.isScramble(s1, s2))