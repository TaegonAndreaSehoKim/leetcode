class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        max_len = 0
        for i in range(len(s)):
            for k in range(2): 
                l = i
                r = i + k
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        if r - l + 1 > max_len:
                            result = s[l : r + 1]
                            max_len = r - l + 1
                        l = l - 1
                        r = r + 1
                    else:
                        break
        return result