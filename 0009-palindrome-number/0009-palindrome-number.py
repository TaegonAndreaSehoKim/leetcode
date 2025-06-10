class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):       # when x is negative number or x's last digit is 0, return false
            return False
        
        y = 0       # reverted number variable declaration
        while x > y:        # until reverted digit exceeds remain digit
            y = y * 10 + x % 10     # add last digit of x to y
            x = x // 10     # remove last digit from x
        
        return x == y or x == y // 10       # when input's length is odd, we can ignore the middle number by y // 10
        