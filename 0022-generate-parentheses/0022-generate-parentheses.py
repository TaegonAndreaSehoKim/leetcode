class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]        # edge case

        for k in range(1 , n + 1):
            for i in range(k):
                j = k - 1 - i
                for inside in dp[i]:
                    for outside in dp[j]:
                        dp[k].append("(" + inside + ")" + outside)
        
        return dp[n]