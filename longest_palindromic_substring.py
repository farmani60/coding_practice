# Given a strin s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Wikipedia: In computer science, the longest palindromic substring or longest
# symmetric factor problem is the problem of finding a maximum-length
# contiguous substring of a given string that is also a palindrome. For example
# , the longest palindromic substring of "bananas" is "anana".

class Solution(object):
    """Time complexity : O(n^3). Assume that n is the length of the input string, 
    there are a total of n(n-1)/2 such substrings (excluding the trivial solution 
    where a character itself is a palindrome). Since verifying each substring takes 
    O(n) time, the run time complexity is O(n^3).
    Space complexity : O(1)."""
    
    def longestPalindrome(self, s):
        longest_pal = ""
        if len(s) <= 1000:
            for i in range(len(s)):
                for j in range(len(s), i, -1):
                    s1 = s[i:j]
                    s2 = s1[::-1]
                    if s1 == s2 and len(s1) > len(longest_pal):
                        longest_pal = s1
        else:
            print('Length of the string is more than 1000!')
        return longest_pal

longest_pal = Solution().longestPalindrome('babad')
print(longest_pal)
