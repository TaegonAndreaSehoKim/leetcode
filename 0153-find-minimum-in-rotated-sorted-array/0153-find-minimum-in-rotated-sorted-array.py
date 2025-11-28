class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = 5000
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < result:
                result = nums[mid]
            if nums[left] <= nums[mid]:
                if nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid - 1] < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return result