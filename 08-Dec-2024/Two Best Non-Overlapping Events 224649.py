# Problem: Two Best Non-Overlapping Events - https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda event: event[0])
        heap = []
        res = 0
        first = 0
        for st, en, v in events:
            while len(heap) > 0 and heap[0][0] < st:
                first = max(first, heappop(heap)[1])
            
            heappush(heap, (en, v))
            res = max(res, first + v)
        
        return res
