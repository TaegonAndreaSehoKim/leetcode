class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        last_arrow_point = float("-inf")
        arrows = 0
        
        for point in points:
            if point[0] > last_arrow_point:
                arrows += 1
                last_arrow_point = point[1]
        
        return arrows