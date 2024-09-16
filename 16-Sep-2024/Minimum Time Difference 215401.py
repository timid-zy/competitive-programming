# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findTimeDifference(self, startTime, endTime):
        return (endTime[0] - startTime[0]) * 60 + endTime[1] - startTime[1]

    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        for tc in timePoints:
            arr.append((int(tc[:2]), int(tc[3:])))
        
        arr.sort()
        res = self.findTimeDifference(arr[-1], [arr[0][0] + 24, arr[0][1]])
        for i in range(1, len(arr)):
            res = min(res, self.findTimeDifference(arr[i-1], arr[i]))
        
        return res
