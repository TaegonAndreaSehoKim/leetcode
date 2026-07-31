class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        current_window = [0] * 26
        l = 0
        for char in s1:
            need[ord(char) - ord("a")] += 1
        for r, char in enumerate(s2):
            current_window[ord(char) - ord("a")] += 1
            if r - l + 1 > len(s1):
                current_window[ord(s2[l]) - ord("a")] -= 1
                l += 1
            if r - l + 1 == len(s1) and need == current_window:
                return True
        return False