class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        max_len = 0
        for l in range(0, len(s)):
            for r in range(l, len(s)):
                substr = s[l:r + 1]
                if substr == substr[::-1]:
                    if len(substr) > max_len:
                        result = substr
                        max_len = len(substr)
        return result