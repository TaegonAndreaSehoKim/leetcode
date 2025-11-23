class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        abs_number = abs(x)
        result = int(str(abs_number)[::-1])
        if x < 0:
            result = result * -1
        if result > 2**31 - 1 or result < -(2**31):
            return 0
        return result