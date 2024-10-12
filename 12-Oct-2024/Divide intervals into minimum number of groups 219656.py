# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, I: List[List[int]]) -> int:
        heap = []
        I.sort(key=lambda x: x[0])
        ans = 0
        for l, r in I:
            while heap and heap[0] < l:
                heappop(heap)
            
            heappush(heap, r)
            ans = max(ans, len(heap))
        
        return ans