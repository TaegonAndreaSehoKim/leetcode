class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        result = 1
        start_idx = 0
        for i in range(len(s)):
            if i == 0:
                continue
            for j in range(start_idx, i):
                if s[i] == s[j]:
                    start_idx = j + 1
            result = max(result, i - start_idx + 1)
        return result
                