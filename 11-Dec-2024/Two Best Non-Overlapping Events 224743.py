# Problem: Two Best Non-Overlapping Events - https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        res = prev = 0
        heap = []
        for st, en, val in events:
            heappush(heap, (en, val))
            while heap and heap[0][0] < st:
                prev = max(prev, heappop(heap)[1])
            
            res = max(res, prev + val)
        
        return res