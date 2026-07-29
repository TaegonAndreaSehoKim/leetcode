class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10000
        max_profit = 0
        for price in prices:
            if price < buy:
                buy = price
            profit = price - buy
            max_profit = max(max_profit, profit)
        return max_profit