class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        solutions = [0, 1, 2]
        if n >= 3:
            for i in range(3, n+1):
                solutions.append((solutions[i-2]) + solutions[i-1])
        return solutions[n]