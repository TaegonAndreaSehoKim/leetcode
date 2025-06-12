class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = 0
        h = 0
        r = 0

        while h < len(haystack):
            if needle[n] == haystack[h]:
                if n == len(needle) - 1:
                    return h - len(needle) + 1
                n += 1
                h += 1
            else:
                n = 0
                r += 1
                h = r
        
        return -1
            