class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2
        n = len(nums)

        dp = [[False] * (target_sum + 1) for _ in range (n + 1)]

        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            curr_num = nums[i-1]
            for j in range(1, target_sum + 1):
                if dp[i-1][j]:
                    dp[i][j] = True
                elif j >= curr_num and dp[i-1][j - curr_num]:
                    dp[i][j] = True
        
        return dp[n][target_sum]