class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        status = ''
        i = 0
        par_dict = {'(': ')', '{': '}', '[': ']'}

        while i < len(s):
            if s[i] in par_dict.keys():
                if s[i+1] == par_dict[s[i]]:
                    status = 'valid'
                    i += 2
                else:
                    status = 'not valid'
                    return status
            else:
                status = 'not valid'
                return status
        return status

status = Solution().isValid('{}{}()[]')
print(status)

