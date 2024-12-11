# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        rmn, rmx = intervals[0]
        results = []
        for i in range(1, len(intervals)):
            st, en = intervals[i]
            if rmn <= st <= rmx:
                rmx = max(rmx, en)
            else:
                results.append([rmn, rmx])
                rmn, rmx = st, en
        
        results.append([rmn, rmx])
        return results