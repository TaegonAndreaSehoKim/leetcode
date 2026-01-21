class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)

            current_sum = max(0, current_sum)
        
        return max_sum