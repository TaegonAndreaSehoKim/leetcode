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
            min_height = min(height[left], height[right])
            water_amount = (right - left) * min_height
            if  water_amount > result:
                result = water_amount
            if height[left] > height[right]:
                while left < right and height[right] <= min_height:
                    right = right - 1
            else:
                while left < right and height[left] <= min_height:
                    left = left + 1
        return result
