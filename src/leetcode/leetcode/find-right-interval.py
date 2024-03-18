class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = list(zip(intervals, range(len(intervals))))
        intervals.sort(key=lambda x: x[0])
        
        res = [-1] * len(intervals)
        for i in range(len(intervals)):
            [start, end], idx = intervals[i]
            l, r = 0, len(intervals) - 1

            while l < r:
                mid = l + (r - l) // 2
                [s, e], i = intervals[mid]
                if s >= end:
                    r = mid
                else:
                    l = mid + 1
            
            if intervals[l][0][0] >= end:
                res[idx] = intervals[l][1]
        
        return res
                
