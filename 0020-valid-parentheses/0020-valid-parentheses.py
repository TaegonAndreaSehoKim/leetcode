class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        dic = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in dic:
                stack.append(c)
            elif stack and c == dic[stack[-1]]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
