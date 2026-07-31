class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        char_set = set()
        for r, char in enumerate(s):
            while char in char_set:
                