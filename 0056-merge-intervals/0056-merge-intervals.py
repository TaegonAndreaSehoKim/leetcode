class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda interval: interval[0])
        for interval in intervals:
            if not result:
                result.append(interval)
                continue
            current_start, current_end = interval
            last_start, last_end = result[-1]

            if current_start <= last_end:
                result[-1][1] = max(current_end, last_end)
            else:
                result.append(interval)
        return result
