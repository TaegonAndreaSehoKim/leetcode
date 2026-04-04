class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] <= sorted_nums[j]:
                    result[i] = j
                    break
        
        return result