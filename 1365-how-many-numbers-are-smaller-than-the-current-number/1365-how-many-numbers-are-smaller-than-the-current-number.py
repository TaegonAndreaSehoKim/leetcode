class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        first_index = {}

        for i in range(len(nums)):
            num = sorted_nums[i]
            if num not in first_index:
                first_index[num] = i

        result = []

        for num in nums:
            result.append(first_index[num])
        
        return result