class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l , r = 0 , x
        result = 0

        while l <= r:
            m = (l + r) // 2
            if m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                l = m + 1
                result = m
            elif m ** 2 == x:
                return m
        return result

        
            