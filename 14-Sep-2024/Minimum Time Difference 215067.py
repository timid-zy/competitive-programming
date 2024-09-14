# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        for s in timePoints:
            arr.append((int(s[:2]), int(s[3:])))
        
        arr.sort()
        res = (arr[0][0] + 24 - arr[-1][0]) * 60 + arr[0][1] - arr[-1][1] 
        for i in range(1, len(arr)):
            res = min(
                res,
                (arr[i][0] - arr[i-1][0]) * 60 + arr[i][1] - arr[i-1][1],
                (arr[i-1][0] + 24 - arr[i][0]) * 60 + arr[i-1][1] - arr[i][1]
            )

        return res
