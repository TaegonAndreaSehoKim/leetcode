class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicated_num = 0

        for num in nums:
            if num in seen:
                duplicated_num = num
            seen.add(num)

        n = len(nums)
        total = n * (n + 1) // 2
        actual_sum = sum(set(nums))
        missing_num = total - actual_sum
 
        return [duplicated_num, missing_num]