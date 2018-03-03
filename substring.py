# Given a string, find the length of the longest substring
# without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence
# and not a substring.



def allUnique(s, start, end):
    set = ""
    for i in range(start, end):
        ch = s[i]
        if ch in set:
            return False
        set += ch
    return True

class BruteForce(object):
    """This approch has O(n3) time complexity."""
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n+1):
                if allUnique(s, i, j):
                    ans = max(ans, j-i)
        return ans

class SligdingWindow(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        i = 0
        j = 0
        ans = 0
        set = ""
        while i < n and j < n:
            if s[j] not in set:
                set += s[j]
                j += 1
                ans = max(ans, j-i)
            else:
                ind = set.find(s[i])
                Lset = list(set)
                Lset.pop(ind)
                i += 1
                set = "".join(Lset)
        return ans

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # when char already in dictionary
            if ch in dic:
                # check length from start of string to index
                res = max(res, i-start)
                # update start of string index to the next index
                start = max(start, dic[ch]+1)
            # add/update char to/of dictionary
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        return max(res, len(s)-start)



if __name__ == '__main__':
    s = 'abcabcefgh'
    ans = Solution().lengthOfLongestSubstring(s)
    # ans = SligdingWindow().lengthOfLongestSubstring(s)
    print(ans)



