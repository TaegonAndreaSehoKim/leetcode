class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        l = 0
        need = [0] * 26
        current_window = [0] * 26
        result = []

        

        for char in p:
            need[ord(char) - ord("a")] += 1

        for r, char in enumerate(s):
            current_window[ord(char) - ord("a")] += 1

            if r - l + 1 > len(p):
                current_window[ord(s[l]) - ord("a")] -= 1
                l += 1
            
            if need == current_window:
                result.append(l)
        
        return result