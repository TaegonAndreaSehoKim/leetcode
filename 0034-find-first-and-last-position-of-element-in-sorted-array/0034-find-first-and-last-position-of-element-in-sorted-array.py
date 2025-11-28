class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        start = -1
        end = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                end = mid
                while start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                while end + 1 <= len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [start, end]
                