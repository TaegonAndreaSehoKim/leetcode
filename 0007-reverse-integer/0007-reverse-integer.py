class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        abs_number = abs(x)
        result = int(str(abs_number)[::-1])
        limit = 2**31
        if x < 0:
            result *= -1
        if result > limit - 1 or result < -1 * limit:
            return 0
        return result