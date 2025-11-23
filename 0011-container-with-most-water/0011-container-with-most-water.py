class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            water_amount = (right - left) * (min(height[left], height[right]))
            if  water_amount > result:
                result = water_amount
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return result
