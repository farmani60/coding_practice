class Solution(object):
    """brute force method. O(n3) time complexity.""""
    def lengthOfLongestSubstring(self, s):
        max_sub = ""
        max_len = 0
        for i in range(len(s)):
            strs = s[i]
            for j in range(1+i, len(s)):
                if s[j] not in strs:
                    strs += s[j]
                else:
                    break
            if len(strs) > max_len:
                max_len = len(strs)
                max_sub = strs
        return max_sub, max_len

subs, length = Solution().lengthOfLongestSubstring("pwwkew")
print(subs, length)
