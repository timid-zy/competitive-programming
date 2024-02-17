import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findDistance(point):
            return math.sqrt( pow(point[0], 2)  + pow(point[1], 2) )
        
        def returnDistance(point):
            return dict1[(point[0], point[1])]
        
        dict1 = {}
        for i in range(len(points)):
            dict1[(points[i][0], points[i][1])] = findDistance(points[i])

        points.sort(key=returnDistance)
        return points[:k]