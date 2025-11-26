class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []

        def dfs(open, close):
            if open == close == n:
                result.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                dfs(open + 1, close)
                stack.pop()
            
            if close < open:
                stack.append(")")
                dfs(open, close + 1)
                stack.pop()
            
        dfs(0, 0)

        return result
