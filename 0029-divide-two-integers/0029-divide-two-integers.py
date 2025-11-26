class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negative = (dividend < 0) ^ (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            chunk = divisor
            multiple = 1

            while dividend >= (chunk << 1):
                chunk <<= 1
                multiple <<= 1
            
            dividend -= chunk
            quotient += multiple
        
        return -quotient if negative else quotient