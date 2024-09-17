# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def check_value(arr, val):
            p = 0
            for i in range(1, len(arr)):
                if arr[i] + d - (arr[i-1] + p) < val:
                    return False
                elif arr[i] - (arr[i-1] + p) < val:
                    p = val - arr[i] + (arr[i-1] + p)
                else:
                    p = 0
            
            return True
        
        start.sort()
        l, r = 0, start[-1] + d + 1
        while l < r:
            mid = l + (r - l) // 2
            if mid == l:
                if check_value(start, r):
                    l = r
                break

            if check_value(start, mid):
                l = mid
            else:
                r = mid - 1

        return l
