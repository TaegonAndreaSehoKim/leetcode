class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []

        phone_map = {
            "2": "abc", "3": "def", "4":"ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, current_str):
            if index == len(digits):
                result.append(current_str)
                return
            
            current_digit = digits[index]
            for char in phone_map[current_digit]:
                backtrack(index + 1, current_str + char)
        
        backtrack(0, "")

        return result