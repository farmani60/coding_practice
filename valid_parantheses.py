class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        status = ''
        i = 0
        while i < len(s):
            if s[i] == '(':
                if s[i+1] == ')':
                    status = 'valid'
                    i += 2
                else:
                    status = 'not valid'
                    return status
            elif s[i] == '[':
                if s[i+1] == ']':
                    status = 'valid'
                    i += 2
                else:
                    status = 'not valid'
                    return status
            elif s[i] == '{':
                if s[i+1] == '}':
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
