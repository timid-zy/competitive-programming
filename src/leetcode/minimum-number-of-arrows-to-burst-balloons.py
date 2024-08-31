class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def getFirst(balloon):
            return balloon[0]
        
        i = 0
        points.sort(key=getFirst)
        arrows = 0
        while i < len(points):
            x1 = points[i][0]
            x2 = points[i][1]

            while i < len(points) and (points[i][0] >= x1 and points[i][0] <= x2):
                x1 = max(x1, points[i][0])
                x2 = min(x2, points[i][1])
                i += 1
            
            arrows += 1

        return arrows