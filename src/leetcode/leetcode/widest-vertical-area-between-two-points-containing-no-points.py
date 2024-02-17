class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        lst = []
        for i in range(len(points)):
            lst.append(points[i][0])
        sortedLst = sorted(lst)
        maxDiff = 0
        for i in range(1, len(sortedLst)):
            if sortedLst[i] - sortedLst[i - 1] > maxDiff:
                maxDiff = sortedLst[i] - sortedLst[i - 1]
        return maxDiff