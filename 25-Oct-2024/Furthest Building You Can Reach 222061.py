# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lj = []
        r_sum = 0
        for i in range(1, len(heights)):
            d = heights[i] - heights[i-1]
            if d <= 0:
                continue
                     
            if len(lj) < ladders:
                heappush(lj, d)
            elif ladders > 0 and lj and lj[0] < d:
                r_sum += heappop(lj)
                heappush(lj, d)
            else:
                r_sum += d
            
            if r_sum > bricks:
                return i-1
        
        return len(heights) - 1