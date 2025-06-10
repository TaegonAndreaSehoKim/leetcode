class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}

        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in map:
                return [i, map[num2]]
            map[nums[i]] = i