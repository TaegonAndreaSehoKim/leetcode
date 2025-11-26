class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(path)
                    path.pop()

        dfs([])

        return result