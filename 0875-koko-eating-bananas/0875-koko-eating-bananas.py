class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            total_hour = 0
            for pile in piles:
                pile_hour = (pile - 1) // mid + 1
                total_hour += pile_hour
            if total_hour > h:
                left = mid + 1
            else:
                right = mid
        return left