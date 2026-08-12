class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        previous_end = float(-inf)
        removals = 0
        for interval in intervals:
            if interval[0] < previous_end:
                removals += 1
            else:
                previous_end = interval[1]

        return removals