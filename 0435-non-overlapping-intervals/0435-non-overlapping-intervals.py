class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removals = 0
        intervals.sort(key=lambda interval:interval[1])
        last_end = float("-inf")
        for interval in intervals:
            if interval[0] < last_end:
                removals += 1
            else:
                last_end = interval[1]
        return removals
    