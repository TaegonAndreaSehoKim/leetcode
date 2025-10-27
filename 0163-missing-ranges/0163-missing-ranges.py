class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        l = lower
        for number in nums:
            if number > upper:
                break
            if l >= number:
                l = number + 1
                continue
            result.append([l, number - 1])
            l = number + 1
        if l <= upper:
            result.append([l , upper])
        return result