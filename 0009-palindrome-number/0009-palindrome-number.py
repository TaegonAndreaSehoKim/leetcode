class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        abs_num = abs(x)
        reversed_num = 0
        
        while abs_num > 0:
            digit = abs_num % 10
            abs_num = abs_num // 10
            reversed_num = reversed_num * 10 + digit
        
        return abs(x) == reversed_num
