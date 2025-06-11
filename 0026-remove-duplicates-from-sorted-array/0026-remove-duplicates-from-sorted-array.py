class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        nums2 = []
        for i in range(len(nums)):
            if i == 0:
                nums2.append(nums[i])
                k += 1
            elif nums[i-1] != nums[i]:
                nums2.append(nums[i])
                k += 1
        
        for i in range(len(nums2)):
            nums[i] = nums2[i]
        
        return k