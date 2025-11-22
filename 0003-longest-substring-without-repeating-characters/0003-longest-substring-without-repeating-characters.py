class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
            
        char_set = set()
        start_idx = 0
        result = 0
        
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[start_idx])
                start_idx += 1
            
            char_set.add(s[i])
            
            result = max(result, i - start_idx + 1)
            
        return result
                